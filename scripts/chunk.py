"""
Mini Maddy — Parent-Child Chunking Pipeline

Takes the extracted corpus (output/corpus.jsonl) and produces two files:

1. output/parents.jsonl  — Document Store (one line per page/slide)
2. output/chunks.jsonl   — Vector Store input (multiple child chunks per parent)

Architecture:
    - Each page from the extraction phase becomes a "Parent Document"
    - Each parent is split into smaller "Child Chunks" (500 chars, 100 overlap)
    - Child chunks are what get embedded and searched in the vector DB
    - At retrieval time, the matching child's parent_id is used to look up
      the full parent text from the document store

Uses LangChain's RecursiveCharacterTextSplitter which splits by:
    \\n\\n → \\n → . → " " → character (in order of priority)

Usage:
    python scripts/chunk.py
    python scripts/chunk.py --chunk-size 500 --overlap 100
    python scripts/chunk.py --input output/corpus.jsonl
"""

import argparse
import json
import os
import sys
import time


def build_metadata_header(metadata):
    """
    Build a concise metadata header string to prepend to child chunks.
    
    This header is embedded alongside the chunk text so the embedding
    model always has context about what document this text came from.
    This technique is known as "Contextual Retrieval" (Anthropic, 2024).
    
    Args:
        metadata: dict with keys like course, doc_type, lecture_number, page_number, topic
        
    Returns:
        A single-line header string, e.g.:
        "Course: PDSP2025 | Lecture 5 | Page 3 | Topic: python"
    """
    parts = []
    
    if metadata.get("course"):
        parts.append(f"Course: {metadata['course']}")
    
    if metadata.get("doc_type"):
        doc_type = metadata["doc_type"].replace("_", " ").title()
        parts.append(f"Type: {doc_type}")
    
    if metadata.get("lecture_number") is not None:
        parts.append(f"Lecture {metadata['lecture_number']}")
    
    if metadata.get("page_number") is not None:
        parts.append(f"Page {metadata['page_number']}")
    
    if metadata.get("topic"):
        parts.append(f"Topic: {metadata['topic']}")
    
    return " | ".join(parts)


def create_parent_record(doc):
    """
    Transform a corpus document into a parent record for the document store.
    
    Args:
        doc: A document dict from corpus.jsonl
        
    Returns:
        A parent record dict with parent_id, text, and metadata
    """
    return {
        "parent_id": doc["doc_id"],
        "text": doc["text"],
        "metadata": {
            "source_file": doc["metadata"].get("source_file"),
            "course": doc["metadata"].get("course"),
            "doc_type": doc["metadata"].get("doc_type"),
            "lecture_number": doc["metadata"].get("lecture_number"),
            "topic": doc["metadata"].get("topic"),
            "year": doc["metadata"].get("year"),
            "page_number": doc["metadata"].get("page_number"),
            "total_pages": doc["metadata"].get("total_pages"),
            "char_count": doc["metadata"].get("char_count"),
        }
    }


def chunk_parent(doc, text_splitter):
    """
    Split a single parent document into child chunks.
    
    Each child chunk gets:
    - A unique chunk_id (parent_id + chunk index)
    - A reference back to its parent via parent_id
    - A metadata header prepended to the text for better embeddings
    - Relevant metadata fields for filtering
    
    Args:
        doc: A document dict from corpus.jsonl
        text_splitter: An initialized RecursiveCharacterTextSplitter
        
    Returns:
        List of child chunk dicts
    """
    parent_id = doc["doc_id"]
    text = doc["text"]
    metadata = doc["metadata"]
    
    # Skip documents with very little text
    if not text or len(text.strip()) < 30:
        return []
    
    # Build the metadata header for contextual retrieval
    header = build_metadata_header(metadata)
    
    # Split the text into child chunks
    chunks = text_splitter.split_text(text)
    
    child_records = []
    for i, chunk_text in enumerate(chunks):
        # Prepend the metadata header to the chunk text
        # This is what gets embedded in the vector store
        enriched_text = f"{header}\n{chunk_text}" if header else chunk_text
        
        child_record = {
            "chunk_id": f"{parent_id}_chunk_{i + 1:02d}",
            "parent_id": parent_id,
            "text": enriched_text,
            "metadata": {
                "course": metadata.get("course"),
                "doc_type": metadata.get("doc_type"),
                "lecture_number": metadata.get("lecture_number"),
                "topic": metadata.get("topic"),
                "page_number": metadata.get("page_number"),
                "chunk_index": i + 1,
                "total_chunks": len(chunks),
                "char_count": len(enriched_text),
            }
        }
        child_records.append(child_record)
    
    return child_records


def main():
    parser = argparse.ArgumentParser(
        description="Parent-Child Chunking Pipeline for Mini Maddy."
    )
    parser.add_argument(
        "--input", "-i",
        default="output/corpus.jsonl",
        help="Input corpus JSONL file (default: output/corpus.jsonl)"
    )
    parser.add_argument(
        "--parents-output",
        default="output/parents.jsonl",
        help="Output file for parent documents (default: output/parents.jsonl)"
    )
    parser.add_argument(
        "--chunks-output",
        default="output/chunks.jsonl",
        help="Output file for child chunks (default: output/chunks.jsonl)"
    )
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=500,
        help="Child chunk size in characters (default: 500)"
    )
    parser.add_argument(
        "--overlap",
        type=int,
        default=100,
        help="Overlap between consecutive chunks in characters (default: 100)"
    )
    
    args = parser.parse_args()
    
    print("🔪 Mini Maddy — Parent-Child Chunking Pipeline")
    print(f"   Input:          {args.input}")
    print(f"   Parents output: {args.parents_output}")
    print(f"   Chunks output:  {args.chunks_output}")
    print(f"   Chunk size:     {args.chunk_size} chars")
    print(f"   Overlap:        {args.overlap} chars")
    
    # ── Step 1: Load corpus ──────────────────────────────────────────────
    print(f"\n📂 Loading corpus from {args.input}...")
    
    if not os.path.exists(args.input):
        print(f"   ❌ File not found: {args.input}")
        print(f"   Run 'python scripts/extract.py' first.")
        sys.exit(1)
    
    documents = []
    with open(args.input, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                documents.append(json.loads(line))
    
    print(f"   ✅ Loaded {len(documents)} parent documents")
    
    # ── Step 2: Initialize the text splitter ─────────────────────────────
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=args.chunk_size,
        chunk_overlap=args.overlap,
        length_function=len,
        separators=["\n\n", "\n", ". ", ", ", " ", ""],
        is_separator_regex=False,
    )
    
    print(f"\n🔧 Splitter: RecursiveCharacterTextSplitter")
    print(f"   Separators: [\\n\\n, \\n, '. ', ', ', ' ', '']")
    
    # ── Step 3: Process each document ────────────────────────────────────
    print(f"\n⚙️  Chunking {len(documents)} parent documents...")
    start_time = time.time()
    
    all_parents = []
    all_chunks = []
    skipped = 0
    
    for doc in documents:
        # Create parent record
        parent = create_parent_record(doc)
        all_parents.append(parent)
        
        # Create child chunks
        children = chunk_parent(doc, text_splitter)
        
        if not children:
            skipped += 1
            continue
        
        all_chunks.extend(children)
    
    elapsed = time.time() - start_time
    
    # ── Step 4: Write output files ───────────────────────────────────────
    # Write parents
    os.makedirs(os.path.dirname(args.parents_output), exist_ok=True)
    with open(args.parents_output, "w", encoding="utf-8") as f:
        for parent in all_parents:
            f.write(json.dumps(parent, ensure_ascii=False) + "\n")
    
    # Write chunks
    os.makedirs(os.path.dirname(args.chunks_output), exist_ok=True)
    with open(args.chunks_output, "w", encoding="utf-8") as f:
        for chunk in all_chunks:
            f.write(json.dumps(chunk, ensure_ascii=False) + "\n")
    
    # ── Step 5: Print summary ────────────────────────────────────────────
    print(f"\n{'=' * 60}")
    print(f"📊 CHUNKING SUMMARY")
    print(f"{'=' * 60}")
    
    print(f"\n   Parent documents:  {len(all_parents)}")
    print(f"   Child chunks:      {len(all_chunks)}")
    print(f"   Skipped (empty):   {skipped}")
    
    if all_chunks:
        avg_chunks_per_parent = len(all_chunks) / (len(all_parents) - skipped) if (len(all_parents) - skipped) > 0 else 0
        chunk_sizes = [c["metadata"]["char_count"] for c in all_chunks]
        avg_size = sum(chunk_sizes) / len(chunk_sizes)
        min_size = min(chunk_sizes)
        max_size = max(chunk_sizes)
        
        print(f"\n   Avg chunks/parent: {avg_chunks_per_parent:.1f}")
        print(f"   Avg chunk size:    {avg_size:.0f} chars")
        print(f"   Min chunk size:    {min_size} chars")
        print(f"   Max chunk size:    {max_size} chars")
    
    # Breakdown by doc_type
    doc_types = {}
    for chunk in all_chunks:
        dt = chunk["metadata"].get("doc_type", "unknown")
        doc_types[dt] = doc_types.get(dt, 0) + 1
    
    if doc_types:
        print(f"\n   Chunks by type:")
        for dt, count in sorted(doc_types.items()):
            print(f"     {dt}: {count} chunks")
    
    print(f"\n{'=' * 60}")
    print(f"\n⏱️  Total time: {elapsed:.2f} seconds")
    print(f"💾 Parents saved to: {args.parents_output}")
    print(f"💾 Chunks saved to:  {args.chunks_output}")


if __name__ == "__main__":
    main()
