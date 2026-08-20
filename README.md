# GPT — RAG Learning Tool

A Retrieval-Augmented Generation (RAG) system that serves as a learning tool for CS/DS courses, preserving Professor Madhavan's teaching style, terminology, and explanations.

## Project Structure

```
madhavan/
├── data/
│   └── raw/                     ← Place your PDFs here
│       ├── slides/              ← Lecture slide PDFs
│       └── exams/               ← Previous year papers
├── scripts/
│   ├── extract.py               ← Main extraction pipeline
│   └── utils.py                 ← Helper functions
├── output/
│   ├── extracted/               ← Marker's Markdown output
│   └── corpus.jsonl             ← Structured corpus (feeds into chunking)
├── requirements.txt
└── README.md
```

## Setup

```bash
pip install -r requirements.txt
```

## File Naming Convention

Name your PDFs following this pattern for automatic metadata tagging:

**Lecture slides:**
```
{CourseCode}_Lecture{Number}_{Topic}.pdf
Examples:
  CS301_Lecture05_Trees.pdf
  DS201_Lecture12_Regression.pdf
```

**Exam papers:**
```
{CourseCode}_{Year}_{ExamType}.pdf
Examples:
  CS301_2024_Midterm.pdf
  DS201_2023_Final.pdf
```

## Usage

```bash
# Extract all PDFs and build the corpus
python scripts/extract.py

# The output will be in output/corpus.jsonl
```
