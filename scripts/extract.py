"""
Mini Maddy — Data Extraction Pipeline

Processes all PDFs in data/raw/ and outputs a structured JSONL corpus
at output/corpus.jsonl, ready for the chunking phase.

Pipeline:
    1. Scan data/raw/ for all .pdf files
    2. Extract text from each PDF using Marker (PDF → Markdown)
    3. Parse metadata from filenames (course, doc_type, year, topic, etc.)
    4. Clean extracted text (Unicode fixes, whitespace normalization)
    5. Split into page-level documents
    6. Write structured records to output/corpus.jsonl

Usage:
    python scripts/extract.py
    python scripts/extract.py --input data/raw --output output/corpus.jsonl
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

import pymupdf

# Add project root to path so we can import utils
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import parse_filename, clean_text, generate_doc_id


def find_all_pdfs(input_dir):
    """
    Recursively find all PDF files under the input directory.
    
    Args:
        input_dir: Path to the root directory to scan
        
    Returns:
        List of Path objects for each PDF found, sorted alphabetically
    """
    input_path = Path(input_dir)
    pdfs = sorted(input_path.rglob("*.pdf"))
    
    if not pdfs:
        print(f"⚠️  No PDF files found in {input_dir}")
        print(f"   Place your PDFs in {input_dir}/slides/ and {input_dir}/exams/")
        sys.exit(1)
    
    return pdfs


def classify_pdf(pdf_path):
    """
    Check if a PDF is text-based or scanned by counting extractable characters.
    
    Args:
        pdf_path: Path to the PDF file
        
    Returns:
        "text-based", "mixed", or "scanned"
    """
    doc = pymupdf.open(str(pdf_path))
    total_pages = len(doc)
    text_pages = 0
    
    for page in doc:
        text = page.get_text().strip()
        if len(text) > 50:
            text_pages += 1
    
    doc.close()
    
    ratio = text_pages / total_pages if total_pages > 0 else 0
    
    if ratio > 0.8:
        return "text-based"
    elif ratio > 0.2:
        return "mixed"
    else:
        return "scanned"


def extract_with_pymupdf(pdf_path):
    """
    Extract text from a text-based PDF using PyMuPDF, page by page.
    
    This is used as the primary extraction method for v1 since it's
    fast, lightweight, and works well for text-based PDFs (lecture slides
    and exam papers exported from PowerPoint/LaTeX/Word).
    
    Args:
        pdf_path: Path to the PDF file
        
    Returns:
        List of dicts, one per page: {"page_number": int, "text": str}
    """
    doc = pymupdf.open(str(pdf_path))
    pages = []
    
    for page_num, page in enumerate(doc):
        text = page.get_text("text")
        pages.append({
            "page_number": page_num + 1,
            "text": text,
        })
    
    total_pages = len(doc)
    doc.close()
    
    return pages, total_pages


def init_marker():
    """
    Initialize the Marker PDF converter once.
    Models are loaded into memory and reused across all PDFs.
    
    Returns:
        PdfConverter instance, or None if Marker is not available
    """
    try:
        from marker.converters.pdf import PdfConverter
        from marker.models import create_model_dict
        from marker.config.parser import ConfigParser

        print("\n🔧 Loading Marker models (one-time setup)...")
        config_parser = ConfigParser({"output_format": "markdown"})
        converter = PdfConverter(
            config=config_parser.generate_config_dict(),
            artifact_dict=create_model_dict(),
        )
        print("   ✅ Marker models loaded successfully")
        return converter

    except ImportError:
        print("\n⚠️  Marker not installed, will use PyMuPDF for all files")
        return None
    except Exception as e:
        print(f"\n⚠️  Marker failed to initialize ({e}), will use PyMuPDF")
        return None


def try_marker_extraction(pdf_path, output_dir, converter):
    """
    Extract text using a pre-initialized Marker converter.
    
    Args:
        pdf_path: Path to the PDF file
        output_dir: Directory to write Marker's Markdown output
        converter: Pre-initialized PdfConverter instance
        
    Returns:
        Tuple of (markdown_text, success_bool)
    """
    if converter is None:
        return None, False
    
    try:
        rendered = converter(str(pdf_path))
        markdown_text = rendered.markdown

        # Save the Markdown output for reference
        md_filename = Path(pdf_path).stem + ".md"
        md_path = Path(output_dir) / md_filename
        md_path.parent.mkdir(parents=True, exist_ok=True)
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(markdown_text)

        return markdown_text, True

    except Exception as e:
        print(f"   ⚠️  Marker failed ({e}), falling back to PyMuPDF")
        return None, False


def process_single_pdf(pdf_path, extracted_dir, converter=None):
    """
    Process a single PDF: extract text, parse metadata, clean, and structure.
    
    Args:
        pdf_path: Path to the PDF file
        extracted_dir: Directory for Marker's Markdown output
        converter: Pre-initialized Marker PdfConverter (or None to use PyMuPDF)
        
    Returns:
        List of document dicts ready for corpus.jsonl
    """
    filename = os.path.basename(pdf_path)
    print(f"\n📄 Processing: {filename}")
    
    # Step 1: Classify the PDF
    pdf_type = classify_pdf(pdf_path)
    print(f"   Type: {pdf_type}")
    
    if pdf_type == "scanned":
        print(f"   ⚠️  Scanned PDF detected — extraction quality may be limited.")
        print(f"   Consider using OCR tools for better results.")
    
    # Step 2: Extract text
    # Skip Marker for large PDFs (>10MB) to avoid memory issues on limited RAM
    file_size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
    if file_size_mb > 10 and converter is not None:
        print(f"   ℹ️  Large file ({file_size_mb:.1f}MB) — using PyMuPDF (Marker may OOM)")
        use_converter = None
    else:
        use_converter = converter
    
    # Try Marker first for better quality, fall back to PyMuPDF
    marker_text, marker_success = try_marker_extraction(pdf_path, extracted_dir, use_converter)
    
    if marker_success and marker_text:
        extraction_method = "marker"
        # Marker returns the full document as one string.
        # We also extract per-page via PyMuPDF for page-level splitting
        # while using Marker's cleaner text as the primary source.
        pymupdf_pages, total_pages = extract_with_pymupdf(pdf_path)
        
        # For Marker output, we create one document per PDF (not per page)
        # since Marker's Markdown has better structure than page-level splits
        full_text = clean_text(marker_text)
        
        if not full_text or len(full_text) < 20:
            print(f"   ⚠️  Marker produced empty output, falling back to PyMuPDF")
            extraction_method = "pymupdf"
        else:
            # Build documents from Marker output
            # Split by Markdown headings for logical sections
            documents = build_documents_from_markdown(
                full_text, filename, total_pages, extraction_method
            )
            
            # Save the markdown output
            md_filename = Path(pdf_path).stem + ".md"
            md_path = Path(extracted_dir) / md_filename
            md_path.parent.mkdir(parents=True, exist_ok=True)
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(full_text)
            
            print(f"   ✅ Extracted {len(documents)} sections via Marker")
            return documents
    else:
        extraction_method = "pymupdf"
    
    # PyMuPDF extraction (primary fallback)
    pages, total_pages = extract_with_pymupdf(pdf_path)
    
    # Step 3: Parse metadata from filename
    metadata = parse_filename(filename)
    
    # Step 4: Build document records (one per page)
    documents = []
    for page in pages:
        text = clean_text(page["text"])
        
        # Skip pages with very little content (e.g., blank pages, title-only pages)
        if len(text) < 20:
            continue
        
        doc_id = generate_doc_id(filename, page["page_number"])
        
        doc = {
            "doc_id": doc_id,
            "text": text,
            "metadata": {
                "source_file": filename,
                "course": metadata["course"],
                "doc_type": metadata["doc_type"],
                "lecture_number": metadata["lecture_number"],
                "topic": metadata["topic"],
                "year": metadata["year"],
                "page_number": page["page_number"],
                "total_pages": total_pages,
                "char_count": len(text),
                "extraction_method": extraction_method,
            }
        }
        documents.append(doc)
    
    # Also save a combined Markdown file for reference
    combined_text = "\n\n---\n\n".join(
        f"## Page {p['page_number']}\n\n{clean_text(p['text'])}" 
        for p in pages 
        if len(clean_text(p["text"])) >= 20
    )
    md_filename = Path(pdf_path).stem + ".md"
    md_path = Path(extracted_dir) / md_filename
    md_path.parent.mkdir(parents=True, exist_ok=True)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(combined_text)
    
    print(f"   ✅ Extracted {len(documents)} pages via PyMuPDF")
    return documents


def build_documents_from_markdown(markdown_text, filename, total_pages, extraction_method):
    """
    Split Marker's Markdown output into logical sections based on headings.
    
    Each top-level heading (## or #) becomes a separate document.
    Content without headings is grouped as a single document.
    
    Args:
        markdown_text: Full Markdown text from Marker
        filename: Original PDF filename
        total_pages: Total number of pages in the PDF
        extraction_method: "marker" or "pymupdf"
        
    Returns:
        List of document dicts
    """
    metadata = parse_filename(filename)
    
    # Split by top-level headings (# or ##)
    # Keep the heading with its content
    sections = re.split(r'(?=^#{1,2}\s)', markdown_text, flags=re.MULTILINE)
    sections = [s.strip() for s in sections if s.strip()]
    
    # If no headings found, treat the entire text as one section
    if len(sections) <= 1:
        sections = [markdown_text.strip()]
    
    documents = []
    for i, section in enumerate(sections):
        text = clean_text(section)
        
        if len(text) < 20:
            continue
        
        doc_id = generate_doc_id(filename, i + 1)
        
        doc = {
            "doc_id": doc_id,
            "text": text,
            "metadata": {
                "source_file": filename,
                "course": metadata["course"],
                "doc_type": metadata["doc_type"],
                "lecture_number": metadata["lecture_number"],
                "topic": metadata["topic"],
                "year": metadata["year"],
                "section_number": i + 1,
                "total_sections": len(sections),
                "total_pages": total_pages,
                "char_count": len(text),
                "extraction_method": extraction_method,
            }
        }
        documents.append(doc)
    
    return documents


def write_corpus(documents, output_path):
    """
    Write all documents to a JSONL file (one JSON object per line).
    
    Args:
        documents: List of document dicts
        output_path: Path to the output .jsonl file
    """
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output, "w", encoding="utf-8") as f:
        for doc in documents:
            f.write(json.dumps(doc, ensure_ascii=False) + "\n")


def print_summary(all_documents):
    """Print a summary of the extraction results."""
    
    if not all_documents:
        print("\n❌ No documents were extracted.")
        return
    
    print("\n" + "=" * 60)
    print("📊 EXTRACTION SUMMARY")
    print("=" * 60)
    
    print(f"\nTotal documents: {len(all_documents)}")
    
    # Group by course
    courses = {}
    for doc in all_documents:
        course = doc["metadata"]["course"] or "unknown"
        courses.setdefault(course, []).append(doc)
    
    print(f"Courses found: {', '.join(sorted(courses.keys()))}")
    
    for course, docs in sorted(courses.items()):
        print(f"\n  📚 {course}:")
        
        # Group by doc_type within course
        by_type = {}
        for doc in docs:
            dtype = doc["metadata"]["doc_type"] or "unknown"
            by_type.setdefault(dtype, []).append(doc)
        
        for dtype, type_docs in sorted(by_type.items()):
            total_chars = sum(d["metadata"]["char_count"] for d in type_docs)
            print(f"     {dtype}: {len(type_docs)} documents ({total_chars:,} chars)")
    
    # Check for potential issues
    empty_docs = [d for d in all_documents if d["metadata"]["char_count"] < 50]
    unknown_courses = [d for d in all_documents if d["metadata"]["course"] is None]
    unknown_types = [d for d in all_documents if d["metadata"]["doc_type"] == "unknown"]
    
    if empty_docs or unknown_courses or unknown_types:
        print(f"\n⚠️  Potential issues:")
        if empty_docs:
            print(f"   - {len(empty_docs)} documents with very little text (<50 chars)")
        if unknown_courses:
            print(f"   - {len(unknown_courses)} documents with undetected course code")
            print(f"     Files: {', '.join(set(d['metadata']['source_file'] for d in unknown_courses))}")
        if unknown_types:
            print(f"   - {len(unknown_types)} documents with unknown doc_type")
            print(f"     Files: {', '.join(set(d['metadata']['source_file'] for d in unknown_types))}")
        print(f"   Consider renaming files to match the pattern: CourseCode_Lecture01_Topic.pdf")
    
    print(f"\n{'=' * 60}")


def main():
    parser = argparse.ArgumentParser(
        description="Extract text from PDFs and build a structured corpus for Mini Maddy."
    )
    parser.add_argument(
        "--input", "-i",
        default="data/raw",
        help="Input directory containing PDF files (default: data/raw)"
    )
    parser.add_argument(
        "--output", "-o",
        default="output/corpus.jsonl",
        help="Output JSONL file path (default: output/corpus.jsonl)"
    )
    parser.add_argument(
        "--extracted-dir", "-e",
        default="output/extracted",
        help="Directory for extracted Markdown files (default: output/extracted)"
    )
    parser.add_argument(
        "--no-marker",
        action="store_true",
        help="Skip Marker and use PyMuPDF for all files (faster, less RAM)"
    )
    
    args = parser.parse_args()
    
    print("🚀 Mini Maddy — Data Extraction Pipeline")
    print(f"   Input:     {args.input}")
    print(f"   Output:    {args.output}")
    print(f"   Extracted: {args.extracted_dir}")
    print(f"   Marker:    {'disabled' if args.no_marker else 'enabled'}")
    
    # Step 1: Find all PDFs
    pdfs = find_all_pdfs(args.input)
    print(f"\n📁 Found {len(pdfs)} PDF files")
    
    # Step 2: Initialize Marker (loads models once, reused for all PDFs)
    if args.no_marker:
        converter = None
        print("\nℹ️  Marker disabled — using PyMuPDF for all files")
    else:
        converter = init_marker()
    
    # Step 3: Process each PDF
    all_documents = []
    start_time = time.time()
    
    for i, pdf_path in enumerate(pdfs, 1):
        print(f"\n[{i}/{len(pdfs)}]", end="")
        try:
            documents = process_single_pdf(pdf_path, args.extracted_dir, converter)
            all_documents.extend(documents)
        except Exception as e:
            print(f"\n   ❌ Error processing {pdf_path.name}: {e}")
            continue
    
    elapsed = time.time() - start_time
    
    # Step 3: Write corpus
    write_corpus(all_documents, args.output)
    
    # Step 4: Print summary
    print_summary(all_documents)
    print(f"\n⏱️  Total time: {elapsed:.1f} seconds")
    print(f"💾 Corpus saved to: {args.output}")
    print(f"📝 Markdown files saved to: {args.extracted_dir}/")


if __name__ == "__main__":
    main()
