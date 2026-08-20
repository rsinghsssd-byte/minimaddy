# Mini Maddy — Project Handoff Document

> **Repository:** [https://github.com/rsinghsssd-byte/minimaddy](https://github.com/rsinghsssd-byte/minimaddy)  
> **Last Updated:** August 21, 2026  
> **Author:** Rajveer Singh

---

## 1. What is Mini Maddy?

Mini Maddy is an AI-powered teaching assistant that answers student questions about university courses **in the voice of Professor Madhavan**. It uses a Retrieval-Augmented Generation (RAG) pipeline to pull relevant lecture slides, textbook pages, and exam content from a vector database, then feeds that context to a Gemini LLM that responds as the professor.

The system supports four query modes:
- **Explain** — Breaks down a concept step-by-step like a lecture
- **Quiz Me** — Generates a practice question from the relevant material
- **Summarize** — Returns a concise bullet-point summary
- **Solve** — Walks through a problem step-by-step like office hours

Every response includes **source citations** showing which lecture slides were used and their relevance scores.

---

## 2. Project History & Decisions Made

### Phase 1–3: Data Pipeline (Completed)
We built a 4-stage pipeline to go from raw PDFs to a searchable vector database:
1. **Extract** — Convert PDFs to structured text (Markdown)
2. **Chunk** — Split into parent (full page) and child (small overlapping) pieces
3. **Embed** — Convert child chunks into 768-dimensional vectors via Gemini Embeddings
4. **Store** — Index everything in ChromaDB for similarity search

**Key Decision:** We used a **Parent-Child chunking strategy**. Small child chunks (500 chars) are embedded for precise search, but when a match is found, the full parent page is sent to the LLM for complete context. This prevents the model from receiving fragmented, out-of-context snippets.

**Key Decision:** We used `gemini-embedding-001` for embeddings and `gemini-3.5-flash` for generation, both on the free tier.

### Phase 4: CLI Query Tool (Completed)
We built `scripts/query.py` as a command-line interface to test the RAG pipeline before building the web app.

### Phase 5: Web Application (Completed)
We built a full-stack web app using:
- **Backend:** FastAPI (Python) with SSE streaming
- **Frontend:** Vanilla HTML/CSS/JS with a dark-blue/white design inspired by a reference screenshot

**Key Decision:** We chose FastAPI over Flask because it natively supports async streaming (SSE), which gives the ChatGPT-like token-by-token typing effect.

**Key Decision:** The UI was redesigned to have a light mode as default, no emojis, and a clean academic aesthetic with light-blue code blocks.

### Phase 6: Persona Fine-Tuning (Partially Completed)
We attempted to fine-tune a Gemini model to natively speak like the professor.

**What was completed:**
- Collected 10 lecture transcripts + 1 interview transcript
- Built `scripts/prep_finetuning.py` to synthetically generate Q&A training pairs
- Successfully generated **148 high-quality training pairs** in `output/finetuning_dataset.jsonl`
- Built `scripts/finetune.py` to trigger the tuning job
- Pre-wired `app.py` to accept a `TUNED_MODEL_ID` environment variable

**What was NOT completed:**
- The actual fine-tuning job was never executed

**CRITICAL NOTE:** Google deprecated free-tier fine-tuning in May 2025. The model `gemini-1.5-flash-001-tuning` no longer exists, and `client.tunings` cannot be called with a standard API key. Fine-tuning now requires Google Cloud Vertex AI with a billing account. The `finetune.py` script **will not work** as-is.

**Alternatives discussed but not implemented:**
1. **In-Context Learning (Few-Shot Prompting):** Inject 5-10 of the best transcript Q&A pairs directly into the system prompt. Free, no code changes needed beyond updating the prompt in `app.py`.
2. **Local Fine-Tuning:** Download an open-source model (Llama 3, Mistral), fine-tune locally using MLX (Mac) or Unsloth (NVIDIA GPU), host via Ollama.
3. **Vertex AI Fine-Tuning:** Use Google Cloud's $300 free trial (requires credit card for identity verification).

---

## 3. Architecture Overview

```
+-----------------------------------------------------------+
|                    USER (Browser)                         |
|              http://localhost:8000                         |
+---------------------------+-------------------------------+
                            | HTTP / SSE
+---------------------------v-------------------------------+
|               app.py (FastAPI Server)                     |
|                                                           |
|  1. Receives question + course + mode                     |
|  2. Embeds question via Gemini Embeddings API             |
|  3. Queries ChromaDB for top-5 matching child chunks      |
|  4. Looks up parent documents for full-page context       |
|  5. Sends context + question to Gemini LLM                |
|  6. Streams response token-by-token via SSE               |
|  7. Sends source citations after answer completes         |
+-------+----------------+------------------+--------------+
        |                |                  |
  +-----v-----+  +------v-------+  +-------v------+
  | ChromaDB  |  | parents.jsonl|  |  Gemini API  |
  | (vectordb)|  | (full pages) |  | (LLM +       |
  |           |  |              |  |  Embeddings) |
  +-----------+  +--------------+  +--------------+
```

### Data Pipeline (Run Once)

```
  Raw PDFs              extract.py           chunk.py             embed.py
  (data/raw/) ---------> corpus.jsonl ------> chunks.jsonl ------> ChromaDB
                                      ------> parents.jsonl        (output/vectordb/)
```

---

## 4. File-by-File Breakdown

### Root Files

| File | Purpose |
|------|---------|
| `app.py` | **The main web server.** FastAPI backend that serves the chat UI and exposes the RAG pipeline as SSE streaming endpoints. Endpoints: `GET /api/courses`, `POST /api/query`, `GET /`. Loads ChromaDB and parent documents at startup. Contains 4 system prompts (explain, quiz, summarize, solve) with the Professor Madhavan persona. |
| `requirements.txt` | Python dependencies: `marker-pdf`, `pymupdf`, `ftfy`, `langchain-text-splitters`, `chromadb`, `google-genai`, `python-dotenv`, `fastapi`, `uvicorn` |
| `README.md` | Basic project overview with setup and naming conventions |
| `.gitignore` | Excludes `.env` (API keys), `__pycache__/`, `.DS_Store` |
| `.env` (**NOT in repo**) | Must be manually created. Contains `GEMINI_API_KEY=your_key_here` |

---

### `scripts/` — Data Pipeline & Utilities

| File | Purpose |
|------|---------|
| `extract.py` | **Stage 1.** Reads all PDFs from `data/raw/` (slides, exams, books). Converts them to Markdown using Marker (with PyMuPDF fallback). Outputs structured records to `output/corpus.jsonl` and individual `.md` files to `output/extracted/`. Auto-classifies each PDF by type (lecture, exam, book) and extracts metadata (course code, lecture number, page count) from filenames. |
| `chunk.py` | **Stage 2.** Reads `output/corpus.jsonl`. Creates full-page parent records in `output/parents.jsonl`. Splits each page into overlapping 500-char child chunks with contextual metadata headers prepended. Outputs to `output/chunks.jsonl`. Uses `RecursiveCharacterTextSplitter` with 100-char overlap. |
| `embed.py` | **Stage 3.** Reads `output/chunks.jsonl`. Embeds each chunk's text using `gemini-embedding-001` (768-dim vectors). Stores vectors + metadata in ChromaDB at `output/vectordb/`. Supports resuming (skips already-embedded chunks) and handles API rate limits with exponential backoff. |
| `query.py` | **Standalone CLI tool.** Query the RAG pipeline from terminal. Supports single queries, `--interactive` mode, and `--show-sources`. Useful for testing without the web app. |
| `utils.py` | **Shared utilities.** `parse_filename()` extracts course/lecture/type metadata from PDF filenames via regex. `clean_text()` fixes Unicode encoding issues via `ftfy`. `generate_doc_id()` creates unique document identifiers. |
| `prep_finetuning.py` | **Fine-tuning data generator.** Reads transcripts from `data/raw/transcripts/`. Chunks them into ~1200-char blocks. Sends batches of 4 blocks to Gemini asking it to reverse-engineer a student question for each block. Outputs `{"text_input": "...", "output": "..."}` pairs to `output/finetuning_dataset.jsonl`. Supports resuming. |
| `finetune.py` | **Fine-tuning trigger (NON-FUNCTIONAL).** Was designed to upload the dataset and start a tuning job on `gemini-1.5-flash-001-tuning`. This model has been deprecated and the script will fail. See Phase 6 notes above. |

---

### `static/` — Frontend

| File | Purpose |
|------|---------|
| `index.html` | Single-page chat interface. Contains course dropdown (`#course-select`), mode selector buttons (Explain, Quiz Me, Summarize, Solve), chat message area (`#chat-messages`), and input box. Loads Google Font `Inter`, Highlight.js for code syntax highlighting, and Marked.js for Markdown rendering. |
| `style.css` | Visual design. Dark blue header (`#323299`), light assistant bubbles (`#f9f9f9`), blue user bubbles (`#e6e6f2`). Includes slide-up animations for messages, bounce animation for typing indicator, pulse animation for streaming dot. Mobile-responsive at 600px breakpoint. Light-blue code blocks. |
| `script.js` | Client-side logic. Fetches courses from `/api/courses` on load. Sends questions to `/api/query` via fetch. Consumes SSE stream using `ReadableStreamDefaultReader`, parsing `token`, `sources`, `error`, and `done` events. Progressively renders streamed Markdown via `marked.parse()` and highlights code blocks with `hljs`. Renders expandable source citation cards with similarity percentages. |

---

### `data/raw/` — Source Material

| Directory | Contents |
|-----------|----------|
| `slides/` | 25 lecture slide PDFs for PDSP2025 (Lectures 1-26, Aug-Nov 2025) |
| `exams/` | 4 assignment PDFs (Assignments 1-4) |
| `transcripts/` | 8 lecture transcript TXT files + 2 interview/talk transcripts (`life_of_dijkstra.txt`, `where_a_math_degree_can_take_you.txt`) |
| `PDSP2025_Book.pdf.bak` | Backup of the course textbook PDF (~32MB) |

---

### `output/` — Generated Data (All Committed to Git)

| File/Dir | Contents |
|----------|----------|
| `corpus.jsonl` (679 KB) | Raw extracted text records from all PDFs. Each line: `{doc_id, text, metadata}` |
| `parents.jsonl` (661 KB) | Full-page parent documents. Each line: `{parent_id, text, metadata}`. **617 documents.** |
| `chunks.jsonl` (1.05 MB) | Overlapping child chunks with metadata headers. Each line: `{chunk_id, parent_id, text, metadata}`. **1,343 chunks.** |
| `finetuning_dataset.jsonl` (202 KB) | Synthetic Q&A pairs for persona training. Each line: `{text_input, output}`. **148 pairs.** |
| `extracted/` | 30 Markdown files — one per source PDF. Human-readable versions of the extracted text. |
| `vectordb/` | ChromaDB persistent storage. Contains `chroma.sqlite3` (17.3MB) and 3 segment directories with HNSW index binary files. |

---

## 5. How to Clone and Run

```bash
# 1. Clone the repository
git clone https://github.com/rsinghsssd-byte/minimaddy.git
cd minimaddy

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create your .env file with your Gemini API key
echo "GEMINI_API_KEY=your_key_here" > .env

# 4. Run the web app
python app.py

# 5. Open browser to http://localhost:8000
```

**Important:** You do NOT need to re-run the data pipeline (extract, chunk, embed). All the processed data, including the ChromaDB vector database, is already committed to the repository. You just need the API key to start chatting.

### If you ever need to re-run the pipeline from scratch:

```bash
# Stage 1: Extract PDFs to text
python scripts/extract.py

# Stage 2: Chunk into parent + child documents
python scripts/chunk.py

# Stage 3: Embed and index into ChromaDB
python scripts/embed.py

# Test via CLI
python scripts/query.py "What is a dictionary in Python?" --show-sources
```

---

## 6. Environment Variables

| Variable | Required | Default | Purpose |
|----------|----------|---------|---------|
| `GEMINI_API_KEY` | **Yes** | — | Your Google AI Studio API key |
| `LLM_MODEL` | No | `gemini-3.5-flash` | Base LLM model for generation |
| `EMBED_MODEL` | No | `gemini-embedding-001` | Embedding model |
| `TUNED_MODEL_ID` | No | `None` | If set, overrides `LLM_MODEL` with a fine-tuned model |
| `CHROMA_DB_PATH` | No | `output/vectordb` | Path to ChromaDB storage |
| `CHROMA_COLLECTION` | No | `madhavan_chunks` | ChromaDB collection name |
| `PARENTS_FILE` | No | `output/parents.jsonl` | Path to parent documents |

---

## 7. Open Items / Future Work

| Item | Status | Notes |
|------|--------|-------|
| Persona fine-tuning | Blocked | Free-tier Gemini fine-tuning deprecated. Options: Vertex AI ($), local open-source fine-tuning (free, needs GPU), or few-shot prompting (free, no fine-tuning). |
| Sliding window retrieval | Discussed, not implemented | Alternative to parent-child chunking: retrieve the matched chunk plus +/-5 neighboring chunks for seamless context across page boundaries. Needs sequential chunk IDs and document-boundary checks. |
| Multi-course support | Partially built | The UI has a course dropdown and the backend filters by course metadata. Currently only PDSP2025 data is ingested. Adding a new course = dropping new PDFs in `data/raw/` and re-running the pipeline. |
| Light/dark mode toggle | Not implemented | UI currently has a fixed light theme. A toggle was in the original plan. |

---

## 8. Key Technical Details to Remember

- **API Key Quota:** The free Gemini API key has strict rate limits (~15 RPM, ~1500 RPD for `gemini-3.5-flash`). The embed script and prep_finetuning script both have built-in rate-limit handling with sleep/retry logic.
- **ChromaDB is file-based:** The entire vector database lives in `output/vectordb/`. No external database server needed. It loads from disk when `app.py` starts.
- **Parent-Child Retrieval:** When ChromaDB returns a matching child chunk, the code looks up the `parent_id` to retrieve the full page text from `parents.jsonl`. Multiple child chunks from the same parent are deduplicated so the LLM doesn't receive duplicate context.
- **SSE Streaming:** The frontend uses `fetch()` + `ReadableStreamDefaultReader` (not `EventSource`) to consume the SSE stream. This allows POST requests with a JSON body, which standard `EventSource` does not support.
- **Contextual Headers:** Each child chunk has a one-line metadata header prepended (e.g., `Course: PDSP2025 | Lecture 5 | Page 3`) before embedding. This improves retrieval accuracy by giving the embedding model semantic context about what each chunk belongs to.
