"""
MadhavanGPT — Embedding & Vector Store Pipeline

Takes the chunked data (output/chunks.jsonl + output/parents.jsonl) and:
1. Embeds all 1,343 child chunks using Gemini text-embedding-004
2. Stores the vectors + metadata in a local ChromaDB collection

Architecture:
    - ChromaDB stores child chunk vectors for similarity search
    - Parent documents are loaded from parents.jsonl at query time
    - At retrieval: search children → get parent_id → fetch full parent text

Prerequisites:
    - A Gemini API key in .env file (GEMINI_API_KEY=...)
    - pip install chromadb google-genai python-dotenv

Usage:
    python scripts/embed.py
    python scripts/embed.py --batch-size 100
    python scripts/embed.py --collection madhavan_chunks
"""

import argparse
import json
import os
import sys
import time

from dotenv import load_dotenv


def load_chunks(filepath):
    """
    Load child chunks from the JSONL file.
    
    Args:
        filepath: Path to chunks.jsonl
        
    Returns:
        List of chunk dicts
    """
    chunks = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                chunks.append(json.loads(line))
    return chunks


def embed_batch(client, texts, model="text-embedding-004"):
    """
    Embed a batch of texts using the Gemini API.
    
    Args:
        client: google.genai.Client instance
        texts: List of strings to embed
        model: Embedding model name
        
    Returns:
        List of embedding vectors (each is a list of floats)
    """
    result = client.models.embed_content(
        model=model,
        contents=texts,
    )
    return [e.values for e in result.embeddings]


def main():
    parser = argparse.ArgumentParser(
        description="Embed chunks and store in ChromaDB for MadhavanGPT."
    )
    parser.add_argument(
        "--chunks-input",
        default="output/chunks.jsonl",
        help="Input chunks JSONL file (default: output/chunks.jsonl)"
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
        "--batch-size",
        type=int,
        default=100,
        help="Number of chunks to embed per API call (default: 100)"
    )
    parser.add_argument(
        "--model",
        default="gemini-embedding-001",
        help="Gemini embedding model (default: gemini-embedding-001)"
    )
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Delete existing collection and start fresh"
    )
    
    args = parser.parse_args()
    
    # ── Step 0: Load API key ─────────────────────────────────────────────
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key or api_key == "your_api_key_here":
        print("❌ GEMINI_API_KEY not found!")
        print("   1. Go to https://aistudio.google.com/apikey")
        print("   2. Create a free API key")
        print("   3. Paste it in .env file: GEMINI_API_KEY=your_key")
        sys.exit(1)
    
    print("🧠 MadhavanGPT — Embedding & Vector Store Pipeline")
    print(f"   Input:      {args.chunks_input}")
    print(f"   DB path:    {args.db_path}")
    print(f"   Collection: {args.collection}")
    print(f"   Batch size: {args.batch_size}")
    print(f"   Model:      {args.model}")
    
    # ── Step 1: Load chunks ──────────────────────────────────────────────
    print(f"\n📂 Loading chunks from {args.chunks_input}...")
    
    if not os.path.exists(args.chunks_input):
        print(f"   ❌ File not found: {args.chunks_input}")
        print(f"   Run 'python scripts/chunk.py' first.")
        sys.exit(1)
    
    chunks = load_chunks(args.chunks_input)
    print(f"   ✅ Loaded {len(chunks)} chunks")
    
    # ── Step 2: Initialize Gemini client ─────────────────────────────────
    print(f"\n🔑 Initializing Gemini client...")
    from google import genai
    
    client = genai.Client(api_key=api_key)
    
    # Quick test with a single embedding
    test_result = client.models.embed_content(
        model=args.model,
        contents=["test"],
    )
    embedding_dim = len(test_result.embeddings[0].values)
    print(f"   ✅ Connected to Gemini API")
    print(f"   Embedding dimensions: {embedding_dim}")
    
    # ── Step 3: Initialize ChromaDB ──────────────────────────────────────
    print(f"\n💾 Initializing ChromaDB at {args.db_path}...")
    import chromadb
    
    chroma_client = chromadb.PersistentClient(path=args.db_path)
    
    # Delete existing collection if it exists and --reset is passed
    if args.reset:
        try:
            chroma_client.delete_collection(name=args.collection)
            print(f"   🗑️  Deleted existing collection '{args.collection}' (--reset passed)")
        except Exception:
            pass
    
    collection = chroma_client.get_or_create_collection(
        name=args.collection,
        metadata={"hnsw:space": "cosine"},  # Use cosine similarity
    )
    print(f"   ✅ Connected to collection '{args.collection}' (cosine similarity)")
    
    # ── Step 3.5: Filter out already embedded chunks ─────────────────────
    print(f"\n🔍 Checking for existing chunks to resume progress...")
    try:
        existing_data = collection.get(include=[])
        existing_ids = set(existing_data["ids"])
        print(f"   📊 Found {len(existing_ids)} chunks already in the database.")
    except Exception as e:
        existing_ids = set()
        print(f"   ⚠️ Could not read existing chunks: {e}")
    
    chunks_to_embed = [c for c in chunks if c["chunk_id"] not in existing_ids]
    
    if not chunks_to_embed:
        print(f"\n🎉 All {len(chunks)} chunks are already embedded!")
        sys.exit(0)
    else:
        print(f"   🚀 {len(chunks_to_embed)} new chunks left to embed.")
    
    # ── Step 4: Embed and store in batches ───────────────────────────────
    # Free tier limit: 100 embed_content requests per minute
    # Strategy: batch_size=20, ~1 request every 0.7s = ~85 req/min (safe margin)
    RATE_LIMIT_DELAY = 2.0  # seconds between batches (30 RPM — safe margin)
    RATE_LIMIT_RETRY_WAIT = 65  # seconds to wait on 429 error
    
    print(f"\n⚙️  Embedding {len(chunks_to_embed)} chunks in batches of {args.batch_size}...")
    print(f"   Rate limit: ~{int(60 / RATE_LIMIT_DELAY)} requests/min (free tier max: 100)")
    start_time = time.time()
    
    total_embedded = 0
    total_batches = (len(chunks_to_embed) + args.batch_size - 1) // args.batch_size
    
    for batch_idx in range(0, len(chunks_to_embed), args.batch_size):
        batch = chunks_to_embed[batch_idx : batch_idx + args.batch_size]
        batch_num = (batch_idx // args.batch_size) + 1
        
        # Extract texts, IDs, and metadata for this batch
        texts = [c["text"] for c in batch]
        ids = [c["chunk_id"] for c in batch]
        metadatas = []
        for c in batch:
            # ChromaDB metadata values must be str, int, float, or bool
            meta = {
                "parent_id": c["parent_id"],
                "course": c["metadata"].get("course") or "",
                "doc_type": c["metadata"].get("doc_type") or "",
                "lecture_number": c["metadata"].get("lecture_number") or 0,
                "page_number": c["metadata"].get("page_number") or 0,
                "chunk_index": c["metadata"].get("chunk_index", 0),
                "topic": c["metadata"].get("topic") or "",
            }
            metadatas.append(meta)
        
        # Embed the batch with retry logic for rate limits
        max_retries = 5
        for attempt in range(max_retries):
            try:
                embeddings = embed_batch(client, texts, model=args.model)
                break  # Success
            except Exception as e:
                error_str = str(e)
                if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                    if attempt < max_retries - 1:
                        print(f"\n   ⏳ Rate limited on batch {batch_num}. Error: {error_str}")
                        print(f"   Waiting {RATE_LIMIT_RETRY_WAIT}s... (attempt {attempt + 1}/{max_retries})")
                        time.sleep(RATE_LIMIT_RETRY_WAIT)
                    else:
                        print(f"\n   ❌ Rate limit exhausted after {max_retries} retries on batch {batch_num}")
                        embeddings = None
                else:
                    print(f"\n   ❌ Embedding failed on batch {batch_num}: {e}")
                    embeddings = None
                    break
        
        if embeddings is None:
            print(f"   Skipping batch {batch_num}")
            continue
        
        # Store in ChromaDB
        collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=texts,
            metadatas=metadatas,
        )
        
        total_embedded += len(batch)
        elapsed = time.time() - start_time
        rate = total_embedded / elapsed if elapsed > 0 else 0
        remaining = len(chunks_to_embed) - total_embedded
        eta = remaining / rate if rate > 0 else 0
        
        print(f"   [{batch_num}/{total_batches}] Embedded {total_embedded}/{len(chunks_to_embed)} "
              f"({rate:.0f} chunks/sec, ~{eta:.0f}s remaining)")
        
        # Delay between batches to respect rate limits
        if batch_num < total_batches:
            time.sleep(RATE_LIMIT_DELAY)
    
    elapsed = time.time() - start_time
    
    # ── Step 5: Verify ───────────────────────────────────────────────────
    stored_count = collection.count()
    
    # ── Step 6: Run a test query ─────────────────────────────────────────
    print(f"\n🔍 Running test query...")
    test_query = "How do you find the maximum value in a list?"
    query_embedding = embed_batch(client, [test_query], model=args.model)[0]
    
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3,
    )
    
    print(f"   Query: \"{test_query}\"")
    print(f"   Top 3 results:")
    for i, (doc_id, distance, doc_text) in enumerate(
        zip(results["ids"][0], results["distances"][0], results["documents"][0])
    ):
        # Truncate text for display
        preview = doc_text[:120].replace("\n", " ") + "..."
        print(f"     {i+1}. [{doc_id}] (score: {1 - distance:.3f})")
        print(f"        {preview}")
    
    # ── Step 7: Print summary ────────────────────────────────────────────
    print(f"\n{'=' * 60}")
    print(f"📊 EMBEDDING SUMMARY")
    print(f"{'=' * 60}")
    print(f"\n   Chunks embedded:   {total_embedded}")
    print(f"   Vectors stored:    {stored_count}")
    print(f"   Embedding dims:    {embedding_dim}")
    print(f"   Similarity metric: cosine")
    print(f"   Total time:        {elapsed:.1f} seconds")
    print(f"\n   DB location:       {os.path.abspath(args.db_path)}/")
    print(f"   Collection:        {args.collection}")
    print(f"\n{'=' * 60}")


if __name__ == "__main__":
    main()
