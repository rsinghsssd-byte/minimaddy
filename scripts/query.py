"""
MadhavanGPT — RAG Query Pipeline

Takes a student's question and:
1. Embeds it using the same Gemini embedding model
2. Searches ChromaDB for the top-K most similar child chunks
3. Retrieves parent (full slide) text for maximum context
4. Sends everything to Gemini 2.5 Pro with a "Professor Madhavan" persona
5. Streams a cited answer to the terminal

Architecture:
    Question → Embed → ChromaDB search → Parent lookup → LLM → Answer

Prerequisites:
    - A Gemini API key in .env file (GEMINI_API_KEY=...)
    - ChromaDB populated by scripts/embed.py
    - pip install chromadb google-genai python-dotenv

Usage:
    python scripts/query.py "What is a python dictionary?"
    python scripts/query.py "How do you sort a list?" --top-k 10
    python scripts/query.py --interactive
"""

import argparse
import json
import os
import sys
import textwrap

from dotenv import load_dotenv


# ── System Prompt ────────────────────────────────────────────────────────────

SYSTEM_PROMPT = textwrap.dedent("""\
    You are Professor Madhavan, the instructor for the PDSP2025 (Programming,
    Data Structures & Algorithms using Python) course. You respond exactly as
    Madhavan would — with clarity, precision, and your characteristic teaching
    style. You explain concepts step-by-step, use practical examples, and make
    complex topics feel approachable.

    RULES:
    1. Answer the student's question using ONLY the provided course material.
    2. If the answer is not in the provided material, say "This wasn't covered
       in our lectures, but..." and give a brief pointer.
    3. Always cite your sources at the end of your answer using the metadata
       provided (e.g., [Lecture 3, Page 12]).
    4. If multiple sources are relevant, reference all of them.
    5. Use code examples from the course material when available.
    6. Keep your tone warm, encouraging, and professorial.
""")


def load_parents(filepath):
    """
    Load parent documents from JSONL into a dict keyed by parent_id.
    
    Args:
        filepath: Path to parents.jsonl
        
    Returns:
        Dict mapping parent_id → parent dict
    """
    parents = {}
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                doc = json.loads(line)
                parents[doc["parent_id"]] = doc
    return parents


def embed_query(client, query_text, model="gemini-embedding-001"):
    """
    Embed a single query string using the Gemini API.
    
    Args:
        client: google.genai.Client instance
        query_text: The student's question
        model: Embedding model name (must match what was used for chunks)
        
    Returns:
        List of floats (the embedding vector)
    """
    result = client.models.embed_content(
        model=model,
        contents=[query_text],
    )
    return result.embeddings[0].values


def search_chunks(collection, query_embedding, top_k=5):
    """
    Search ChromaDB for the top-K most similar child chunks.
    
    Args:
        collection: ChromaDB collection
        query_embedding: The query vector
        top_k: Number of results to return
        
    Returns:
        Dict with keys: ids, distances, documents, metadatas
    """
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )
    return results


def build_context(results, parents):
    """
    Build the context string for the LLM prompt.
    
    For each retrieved child chunk, look up its parent document to provide
    the full, unfragmented slide text. Deduplicate parents to avoid
    sending the same slide text twice.
    
    Args:
        results: ChromaDB query results
        parents: Dict mapping parent_id → parent dict
        
    Returns:
        Tuple of (context_string, source_list)
    """
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
        source_label_parts = []
        if course:
            source_label_parts.append(f"Course: {course}")
        if doc_type:
            source_label_parts.append(f"Type: {doc_type.replace('_', ' ').title()}")
        if lecture_num:
            source_label_parts.append(f"Lecture {lecture_num}")
        if page_num:
            source_label_parts.append(f"Page {page_num}")
        if topic:
            source_label_parts.append(f"Topic: {topic}")
        source_label = " | ".join(source_label_parts) if source_label_parts else chunk_id
        
        # Use parent text (full slide) if available, else fall back to child chunk
        if parent_id and parent_id not in seen_parents and parent_id in parents:
            text = parents[parent_id]["text"]
            seen_parents.add(parent_id)
        elif parent_id in seen_parents:
            # Already included this parent's full text — skip duplicate
            continue
        else:
            text = doc_text
        
        similarity = 1 - distance  # ChromaDB returns distance, we want similarity
        context_parts.append(f"--- SOURCE {i+1}: [{source_label}] (relevance: {similarity:.2f}) ---\n{text}")
        sources.append({
            "label": source_label,
            "similarity": similarity,
            "chunk_id": chunk_id,
            "parent_id": parent_id,
        })
    
    context = "\n\n".join(context_parts)
    return context, sources


def generate_answer(client, question, context, model="gemini-2.5-pro"):
    """
    Send the question + context to Gemini LLM and stream the response.
    
    Args:
        client: google.genai.Client instance
        question: The student's question
        context: The retrieved course material context
        model: Gemini LLM model name
    """
    user_prompt = f"""Here is the relevant course material:

{context}

---

Student's question: {question}

Please answer the question using the course material provided above."""

    response = client.models.generate_content_stream(
        model=model,
        contents=[
            {"role": "user", "parts": [{"text": user_prompt}]},
        ],
        config={
            "system_instruction": SYSTEM_PROMPT,
            "temperature": 0.3,  # Low temperature for factual accuracy
            "max_output_tokens": 2048,
        },
    )
    
    print()  # Blank line before answer
    for chunk in response:
        if chunk.text:
            print(chunk.text, end="", flush=True)
    print()  # Newline after answer


def main():
    parser = argparse.ArgumentParser(
        description="MadhavanGPT — Ask questions about PDSP2025 course material."
    )
    parser.add_argument(
        "question",
        nargs="?",
        help="The question to ask (omit for interactive mode)"
    )
    parser.add_argument(
        "--interactive", "-i",
        action="store_true",
        help="Run in interactive mode (ask multiple questions)"
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=5,
        help="Number of chunks to retrieve (default: 5)"
    )
    parser.add_argument(
        "--db-path",
        default="output/vectordb",
        help="ChromaDB storage directory (default: output/vectordb)"
    )
    parser.add_argument(
        "--collection",
        default="madhavan_chunks",
        help="ChromaDB collection name (default: madhavan_chunks)"
    )
    parser.add_argument(
        "--parents-file",
        default="output/parents.jsonl",
        help="Parents JSONL file (default: output/parents.jsonl)"
    )
    parser.add_argument(
        "--embed-model",
        default="gemini-embedding-001",
        help="Embedding model (default: gemini-embedding-001)"
    )
    parser.add_argument(
        "--llm-model",
        default="gemini-3.5-flash",
        help="LLM model for answer generation (default: gemini-3.5-flash)"
    )
    parser.add_argument(
        "--show-sources",
        action="store_true",
        help="Show detailed source information after the answer"
    )
    
    args = parser.parse_args()
    
    if not args.question and not args.interactive:
        parser.print_help()
        print("\nExamples:")
        print('  python scripts/query.py "What is a python dictionary?"')
        print('  python scripts/query.py --interactive')
        sys.exit(1)
    
    # ── Step 0: Load API key ─────────────────────────────────────────────
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key or api_key == "your_api_key_here":
        print("❌ GEMINI_API_KEY not found!")
        print("   1. Go to https://aistudio.google.com/apikey")
        print("   2. Create a free API key")
        print("   3. Paste it in .env file: GEMINI_API_KEY=your_key")
        sys.exit(1)
    
    # ── Step 1: Initialize clients ───────────────────────────────────────
    print("🧠 MadhavanGPT — Your PDSP2025 Teaching Assistant")
    print(f"   Powered by {args.llm_model}")
    print()
    
    from google import genai
    import chromadb
    
    client = genai.Client(api_key=api_key)
    chroma_client = chromadb.PersistentClient(path=args.db_path)
    collection = chroma_client.get_collection(
        name=args.collection,
    )
    
    vector_count = collection.count()
    print(f"📚 Connected to knowledge base ({vector_count} chunks indexed)")
    
    # ── Step 2: Load parents ─────────────────────────────────────────────
    if not os.path.exists(args.parents_file):
        print(f"❌ Parents file not found: {args.parents_file}")
        print(f"   Run 'python scripts/chunk.py' first.")
        sys.exit(1)
    
    parents = load_parents(args.parents_file)
    print(f"📖 Loaded {len(parents)} parent documents")
    print()
    
    # ── Step 3: Process question(s) ──────────────────────────────────────
    def process_question(question):
        """Process a single question through the full RAG pipeline."""
        print(f"{'─' * 60}")
        print(f"❓ {question}")
        print(f"{'─' * 60}")
        
        # Embed the question
        print("🔍 Searching course material...", end="", flush=True)
        query_embedding = embed_query(client, question, model=args.embed_model)
        
        # Search ChromaDB
        results = search_chunks(collection, query_embedding, top_k=args.top_k)
        print(f" Found {len(results['ids'][0])} relevant chunks.")
        
        # Build context from parent documents
        context, sources = build_context(results, parents)
        
        # Generate answer
        print("\n🎓 Professor Madhavan:")
        generate_answer(client, question, context, model=args.llm_model)
        
        # Show sources if requested
        if args.show_sources:
            print(f"\n{'─' * 60}")
            print("📎 Sources Retrieved:")
            for i, src in enumerate(sources):
                print(f"   {i+1}. [{src['label']}] (similarity: {src['similarity']:.3f})")
                print(f"      Chunk: {src['chunk_id']}")
                print(f"      Parent: {src['parent_id']}")
        
        print()
    
    if args.interactive:
        # Interactive mode
        print("💬 Interactive Mode — Type 'quit' or 'exit' to stop.")
        print(f"   Retrieving top {args.top_k} chunks per question.")
        print()
        
        while True:
            try:
                question = input("You: ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\n\n👋 Goodbye!")
                break
            
            if not question:
                continue
            if question.lower() in ("quit", "exit", "q"):
                print("\n👋 Goodbye!")
                break
            
            process_question(question)
    else:
        # Single question mode
        process_question(args.question)


if __name__ == "__main__":
    main()
