"""
Mini Maddy — Web Application Server

FastAPI backend that serves the chat UI and exposes the RAG pipeline
as a streaming SSE endpoint.

Usage:
    python app.py
    # Then open http://localhost:8000 in your browser
"""

import json
import os
import sys
import textwrap

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
import uvicorn


# ── Load environment ─────────────────────────────────────────────────────────
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key or api_key == "your_api_key_here":
    print("❌ GEMINI_API_KEY not found!")
    print("   1. Go to https://aistudio.google.com/apikey")
    print("   2. Create a free API key")
    print("   3. Paste it in .env file: GEMINI_API_KEY=your_key")
    sys.exit(1)


# ── Initialize Gemini + ChromaDB once at startup ─────────────────────────────
from google import genai
import chromadb

gemini_client = genai.Client(api_key=api_key)

DB_PATH = os.getenv("CHROMA_DB_PATH", "output/vectordb")
COLLECTION_NAME = os.getenv("CHROMA_COLLECTION", "course_chunks")
PARENTS_FILE = os.getenv("PARENTS_FILE", "output/parents.jsonl")
EMBED_MODEL = os.getenv("EMBED_MODEL", "gemini-embedding-001")
LLM_MODEL = os.getenv("LLM_MODEL", "gemini-3.5-flash")
TUNED_MODEL_ID = os.getenv("TUNED_MODEL_ID", None)

ACTIVE_MODEL = TUNED_MODEL_ID if TUNED_MODEL_ID else LLM_MODEL

print("🧠 Mini Maddy — Starting up...")

# ChromaDB
chroma_client = chromadb.PersistentClient(path=DB_PATH)
collection = chroma_client.get_collection(name=COLLECTION_NAME)
vector_count = collection.count()
print(f"   📚 ChromaDB: {vector_count} chunks in '{COLLECTION_NAME}'")

# Parent documents
def load_parents(filepath):
    """Load parent documents from JSONL into a dict keyed by parent_id."""
    parents = {}
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                doc = json.loads(line)
                parents[doc["parent_id"]] = doc
    return parents

parents = load_parents(PARENTS_FILE)
print(f"   📖 Parents: {len(parents)} documents loaded")

# Discover available courses from the parent metadata
courses = sorted(set(
    doc["metadata"].get("course", "Unknown")
    for doc in parents.values()
    if doc.get("metadata", {}).get("course")
))
print(f"   🎓 Courses: {courses}")
print(f"   🤖 LLM: {ACTIVE_MODEL}{' (Fine-Tuned Persona)' if TUNED_MODEL_ID else ''}")
print(f"   🔗 Embeddings: {EMBED_MODEL}")
print()


# ── System Prompts by Mode ───────────────────────────────────────────────────

SYSTEM_PROMPTS = {
    "explain": textwrap.dedent("""\
        You are the professor and instructor for the {course} course.
        You respond with clarity, precision, and your characteristic teaching
        style. You explain concepts step-by-step, use practical examples,
        and make complex topics feel approachable.

        RULES:
        1. Answer the student's question using ONLY the provided course material.
        2. If the answer is not in the provided material, say "This wasn't covered
           in our lectures, but..." and give a brief pointer.
        3. Always cite your sources at the end of your answer using the metadata
           provided (e.g., [Lecture 3, Page 12]).
        4. If multiple sources are relevant, reference all of them.
        5. Use code examples from the course material when available.
        6. Keep your tone warm, encouraging, and professorial.
    """),

    "quiz": textwrap.dedent("""\
        You are the professor and instructor for the {course} course.
        The student wants to test their understanding of a topic.

        RULES:
        1. Based on the provided course material, generate a practice question
           (multiple choice or short answer) that tests the student's understanding.
        2. After stating the question, add a line "---" and then provide the
           correct answer with a brief explanation.
        3. Use actual content from the course material to formulate the question.
        4. Cite which lecture/page the question is based on.
        5. Keep your tone encouraging — this is practice, not an exam!
    """),

    "summarize": textwrap.dedent("""\
        You are the professor and instructor for the {course} course.
        The student wants a concise summary of a topic.

        RULES:
        1. Provide a clear, bullet-point summary of the topic using ONLY the
           provided course material.
        2. Start with a one-sentence overview, then list key points.
        3. Include any important formulas, code snippets, or definitions.
        4. Keep it concise — aim for 5-10 bullet points.
        5. Cite your sources at the end.
    """),

    "solve": textwrap.dedent("""\
        You are the professor and instructor for the {course} course.
        The student needs help solving a problem, like in office hours.

        RULES:
        1. Walk through the solution step-by-step, as you would during office hours.
        2. Explain your reasoning at each step.
        3. If the problem involves code, show the code with comments.
        4. Point out common mistakes students make with this type of problem.
        5. Use only techniques and methods taught in the course material provided.
        6. Cite which lectures cover the relevant concepts.
    """),
}


# ── RAG Pipeline Functions ───────────────────────────────────────────────────

def embed_query(query_text):
    """Embed a single query string using the Gemini API."""
    result = gemini_client.models.embed_content(
        model=EMBED_MODEL,
        contents=[query_text],
    )
    return result.embeddings[0].values


def search_chunks(query_embedding, top_k=5, course_filter=None):
    """Search ChromaDB for the top-K most similar child chunks."""
    where_filter = None
    if course_filter:
        where_filter = {"course": course_filter}

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
        where=where_filter,
    )
    return results


def build_context(results):
    """Build context string and source list from ChromaDB results."""
    context_parts = []
    sources = []
    seen_parents = set()

    for i, (chunk_id, distance, doc_text, metadata) in enumerate(zip(
        results["ids"][0],
        results["distances"][0],
        results["documents"][0],
        results["metadatas"][0],
    )):
        parent_id = metadata.get("parent_id", "")
        course = metadata.get("course", "")
        doc_type = metadata.get("doc_type", "")
        lecture_num = metadata.get("lecture_number", "")
        page_num = metadata.get("page_number", "")
        topic = metadata.get("topic", "")

        # Build a human-readable source label
        label_parts = []
        if course:
            label_parts.append(f"Course: {course}")
        if doc_type:
            label_parts.append(f"Type: {doc_type.replace('_', ' ').title()}")
        if lecture_num:
            label_parts.append(f"Lecture {lecture_num}")
        if page_num:
            label_parts.append(f"Page {page_num}")
        if topic:
            label_parts.append(f"Topic: {topic}")
        source_label = " | ".join(label_parts) if label_parts else chunk_id

        # Use parent text (full slide) if available
        if parent_id and parent_id not in seen_parents and parent_id in parents:
            text = parents[parent_id]["text"]
            seen_parents.add(parent_id)
        elif parent_id in seen_parents:
            continue
        else:
            text = doc_text

        similarity = 1 - distance
        context_parts.append(
            f"--- SOURCE {i+1}: [{source_label}] (relevance: {similarity:.2f}) ---\n{text}"
        )
        sources.append({
            "label": source_label,
            "similarity": round(similarity, 3),
            "chunk_id": chunk_id,
            "parent_id": parent_id,
        })

    return "\n\n".join(context_parts), sources


async def generate_stream(question, context, course, mode):
    """Stream LLM response as SSE events."""
    system_prompt = SYSTEM_PROMPTS.get(mode, SYSTEM_PROMPTS["explain"])
    system_prompt = system_prompt.format(course=course)

    user_prompt = f"""Here is the relevant course material:

{context}

---

Student's question: {question}

Please answer the question using the course material provided above."""

    try:
        response = gemini_client.models.generate_content_stream(
            model=ACTIVE_MODEL,
            contents=[
                {"role": "user", "parts": [{"text": user_prompt}]},
            ],
            config={
                "system_instruction": system_prompt,
                "temperature": 0.3,
                "max_output_tokens": 2048,
            },
        )

        for chunk in response:
            if chunk.text:
                yield f"event: token\ndata: {json.dumps({'token': chunk.text})}\n\n"

    except Exception as e:
        yield f"event: error\ndata: {json.dumps({'error': str(e)})}\n\n"


# ── FastAPI App ──────────────────────────────────────────────────────────────

app = FastAPI(title="Mini Maddy", description="AI Teaching Assistant")


@app.get("/api/courses")
async def get_courses():
    """Return the list of available courses."""
    return {"courses": courses}


@app.post("/api/query")
async def query(request: Request):
    """
    RAG query endpoint. Accepts a question, course, and mode.
    Returns an SSE stream of tokens followed by sources.
    """
    body = await request.json()
    question = body.get("question", "").strip()
    course = body.get("course", "")
    mode = body.get("mode", "explain")

    if not question:
        return StreamingResponse(
            iter([f"event: error\ndata: {json.dumps({'error': 'No question provided'})}\n\n"]),
            media_type="text/event-stream",
        )

    # 1. Embed the question
    query_embedding = embed_query(question)

    # 2. Search ChromaDB (with optional course filter)
    course_filter = course if course else None
    results = search_chunks(query_embedding, top_k=5, course_filter=course_filter)

    # 3. Build context from parent documents
    context, sources = build_context(results)

    # 4. Stream LLM response + sources
    async def event_generator():
        async for event in generate_stream(question, context, course, mode):
            yield event

        # Send sources after the answer
        yield f"event: sources\ndata: {json.dumps({'sources': sources})}\n\n"
        yield f"event: done\ndata: {json.dumps({})}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )


@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the main chat page."""
    with open("static/index.html", "r") as f:
        return f.read()


# Mount static files AFTER the root route
app.mount("/static", StaticFiles(directory="static"), name="static")


# ── Entry point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("🚀 Starting Mini Maddy at http://localhost:8000")
    print("   Press Ctrl+C to stop\n")
    uvicorn.run(app, host="0.0.0.0", port=8000)
