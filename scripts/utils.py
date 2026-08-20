"""
Utility functions for the MadhavanGPT data ingestion pipeline.

Handles:
- Filename parsing → metadata extraction
- Text cleaning (Unicode fixes, whitespace normalization)
- Document ID generation
"""

import re
import os
import ftfy


def parse_filename(filename):
    """
    Extract metadata from a PDF filename.
    
    Supports these naming patterns:
    
    Lecture slides:
        {CourseCode}_Lecture{Number}_{DateOrTopic}.pdf
        Examples: PDSP2025_Lecture05_20nov2025.pdf
                  PDSP2025_Lecture11_11sep2025_python.pdf
                  CS301_Lecture05_Trees.pdf
    
    Books:
        {CourseCode}_Book.pdf  OR  {CourseCode}_Book_{Topic}.pdf
        Examples: PDSP2025_Book.pdf, CS301_Book_DataStructures.pdf
    
    Assignments / Exams:
        {CourseCode}_Assignment{Number}.pdf
        {CourseCode}_{Year}_{ExamType}.pdf
        Examples: PDSP2025_Assignment1.pdf, CS301_2024_Midterm.pdf
    
    Falls back to extracting whatever it can if the filename doesn't
    match any pattern exactly.
    
    Returns:
        dict with keys: course, doc_type, lecture_number, topic, year
    """
    # Remove extension (handle double extensions like .ipynb_Colab.pdf)
    name = filename
    # Strip .pdf first, then any secondary extension artifacts
    if name.lower().endswith(".pdf"):
        name = name[:-4]
    # Remove common artifacts like .ipynb_Colab
    name = re.sub(r'\.ipynb_Colab$', '', name, flags=re.IGNORECASE)
    
    metadata = {
        "course": None,
        "doc_type": None,
        "lecture_number": None,
        "topic": None,
        "year": None,
    }
    
    # Pattern 1: Lecture slides
    # e.g., PDSP2025_Lecture05_20nov2025 or PDSP2025_Lecture11_11sep2025_python
    # or CS301_Lecture05_Trees
    lecture_pattern = re.compile(
        r'^([A-Za-z]+\d+)_Lecture(\d+)(?:_(.+))?$', 
        re.IGNORECASE
    )
    match = lecture_pattern.match(name)
    if match:
        metadata["course"] = match.group(1).upper()
        metadata["doc_type"] = "lecture_slide"
        metadata["lecture_number"] = int(match.group(2))
        if match.group(3):
            # Convert underscores/hyphens to spaces, then lowercase
            raw_topic = match.group(3).replace("_", " ").replace("-", " ").strip().lower()
            # Remove date patterns (e.g., "20nov2025", "11sep2025") from topic
            raw_topic = re.sub(r'\d{1,2}\s*(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\s*\d{4}', '', raw_topic, flags=re.IGNORECASE)
            raw_topic = raw_topic.strip()
            metadata["topic"] = raw_topic if raw_topic else None
        return metadata
    
    # Pattern 2: Books / textbooks
    # e.g., PDSP2025_Book or CS301_Book_DataStructures
    book_pattern = re.compile(
        r'^([A-Za-z]+\d+)_(?:Book|Textbook)(?:_(.+))?$', 
        re.IGNORECASE
    )
    match = book_pattern.match(name)
    if match:
        metadata["course"] = match.group(1).upper()
        metadata["doc_type"] = "book"
        if match.group(2):
            metadata["topic"] = match.group(2).replace("_", " ").replace("-", " ").strip().lower()
        else:
            metadata["topic"] = "textbook"
        return metadata
    
    # Pattern 3: Assignments
    # e.g., PDSP2025_Assignment1 or PDSP2025_Assignment4
    assignment_pattern = re.compile(
        r'^([A-Za-z]+\d+)_Assignment(\d+)(?:_(.+))?$', 
        re.IGNORECASE
    )
    match = assignment_pattern.match(name)
    if match:
        metadata["course"] = match.group(1).upper()
        metadata["doc_type"] = "assignment"
        metadata["topic"] = f"assignment {match.group(2)}"
        return metadata
    
    # Pattern 4: Exam papers with explicit year
    # e.g., CS301_2024_Midterm or DS201_2023_Final_Solutions
    exam_pattern = re.compile(
        r'^([A-Za-z]+\d+)_(\d{4})_(.+)$', 
        re.IGNORECASE
    )
    match = exam_pattern.match(name)
    if match:
        metadata["course"] = match.group(1).upper()
        metadata["year"] = int(match.group(2))
        exam_type = match.group(3).replace("_", " ").strip().lower()
        metadata["doc_type"] = "exam"
        metadata["topic"] = exam_type
        return metadata
    
    # Fallback: extract whatever we can
    # Try to find a course code (letters followed by digits)
    course_match = re.search(r'([A-Za-z]+\d+)', name)
    if course_match:
        metadata["course"] = course_match.group(1).upper()
    
    # Try to find a year — but ONLY if it's a standalone year, 
    # not part of the course code (e.g., don't match "2025" in "PDSP2025")
    if metadata["course"]:
        # Remove the course code, then look for a year in the remainder
        remainder = name.replace(course_match.group(0), "", 1) if course_match else name
        year_match = re.search(r'(20\d{2})', remainder)
        if year_match:
            metadata["year"] = int(year_match.group(1))
    
    # Try to find a lecture number
    lec_match = re.search(r'[Ll]ecture\s*(\d+)', name)
    if lec_match:
        metadata["lecture_number"] = int(lec_match.group(1))
        metadata["doc_type"] = "lecture_slide"
    
    # If we still don't know the doc_type, guess from keywords
    if metadata["doc_type"] is None:
        name_lower = name.lower()
        if any(kw in name_lower for kw in ["assignment", "homework", "hw"]):
            metadata["doc_type"] = "assignment"
        elif any(kw in name_lower for kw in ["exam", "midterm", "final", "quiz", "test", "paper"]):
            metadata["doc_type"] = "exam"
        elif any(kw in name_lower for kw in ["book", "textbook"]):
            metadata["doc_type"] = "book"
        elif any(kw in name_lower for kw in ["lecture", "slide", "lec", "class", "week"]):
            metadata["doc_type"] = "lecture_slide"
        else:
            metadata["doc_type"] = "unknown"
    
    # Use the full filename (cleaned) as topic if we couldn't extract one
    if metadata["topic"] is None:
        # Remove course code and year if found, use the rest as topic
        topic = name
        if metadata["course"]:
            topic = topic.replace(metadata["course"], "").replace(metadata["course"].lower(), "")
        if metadata["year"]:
            topic = topic.replace(str(metadata["year"]), "")
        topic = re.sub(r'^[_\-\s]+|[_\-\s]+$', '', topic)  # strip leading/trailing separators
        topic = topic.replace("_", " ").replace("-", " ").strip().lower()
        metadata["topic"] = topic if topic else None
    
    return metadata


def clean_text(text):
    """
    Clean extracted text using industry-standard techniques.
    
    Steps:
    1. Fix Unicode issues (mojibake, broken encodings) via ftfy
    2. Normalize whitespace (collapse multiple blank lines, strip trailing spaces)
    3. Remove common PDF artifacts (page numbers, headers/footers)
    
    Args:
        text: Raw extracted text string
        
    Returns:
        Cleaned text string
    """
    if not text:
        return ""
    
    # Step 1: Fix Unicode / encoding issues
    # ftfy handles things like:
    #   "â€™" → "'"  (broken right single quote)
    #   "Ã©"  → "é"  (broken accented characters)
    text = ftfy.fix_text(text)
    
    # Step 2: Normalize whitespace
    # Replace multiple consecutive blank lines with a single blank line
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Remove trailing whitespace from each line
    text = '\n'.join(line.rstrip() for line in text.split('\n'))
    # Strip leading/trailing whitespace from the entire document
    text = text.strip()
    
    # Step 3: Remove common PDF artifacts
    # Remove standalone page numbers (a line that's just a number)
    text = re.sub(r'^\s*\d{1,3}\s*$', '', text, flags=re.MULTILINE)
    # Remove common header/footer patterns
    # e.g., "Page 5 of 42", "- 5 -", "5/42"
    text = re.sub(r'^\s*Page\s+\d+\s+of\s+\d+\s*$', '', text, flags=re.MULTILINE | re.IGNORECASE)
    text = re.sub(r'^\s*-\s*\d+\s*-\s*$', '', text, flags=re.MULTILINE)
    
    # Clean up any whitespace artifacts left by the removals above
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.strip()
    
    return text


def generate_doc_id(filename, page_num=None):
    """
    Generate a unique document ID from filename and optional page number.
    
    Examples:
        generate_doc_id("CS301_Lecture05_Trees.pdf", 3) 
            → "CS301_Lecture05_Trees_page_03"
        generate_doc_id("CS301_2024_Midterm.pdf")
            → "CS301_2024_Midterm"
    
    Args:
        filename: Original PDF filename (with or without extension)
        page_num: Optional page number (1-indexed)
        
    Returns:
        String ID suitable for use as a document identifier
    """
    # Remove extension
    name = os.path.splitext(filename)[0]
    
    # Remove any characters that aren't alphanumeric, underscore, or hyphen
    name = re.sub(r'[^\w\-]', '_', name)
    
    # Remove consecutive underscores
    name = re.sub(r'_+', '_', name)
    name = name.strip('_')
    
    if page_num is not None:
        return f"{name}_page_{page_num:02d}"
    
    return name
