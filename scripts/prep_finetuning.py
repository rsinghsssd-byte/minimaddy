"""
prep_finetuning.py

Reads raw transcripts and synthetically generates Q&A pairs for fine-tuning.
Uses Gemini to reverse-engineer student questions from the professor's answers.
"""

import os
import json
import glob
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ GEMINI_API_KEY not found in .env")
    exit(1)

client = genai.Client(api_key=api_key)
MODEL = "gemini-3.5-flash"

TRANSCRIPT_DIR = "data/raw/transcripts"
OUTPUT_FILE = "output/finetuning_dataset.jsonl"

def chunk_text(text, chunk_size=1000):
    """Split text into rough chunks based on character length."""
    words = text.split()
    chunks = []
    current_chunk = []
    current_len = 0
    
    for word in words:
        current_chunk.append(word)
        current_len += len(word) + 1
        if current_len >= chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            current_len = 0
            
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

def generate_pairs(blocks):
    """Send multiple text blocks to Gemini and get Q&A pairs."""
    prompt = """
    You are an AI data preparation assistant. I will provide you with several blocks of text 
    from a transcript of the professor speaking (either in a lecture or an interview).
    
    For EACH block:
    1. Read the text and capture the exact vernacular, tone, and teaching style.
    2. Imagine a student asked a specific, relevant question that led to him giving EXACTLY this response.
    3. The answer MUST be the exact text snippet from the block (you can clean up 'ums' and 'uhs' slightly, but keep his exact phrasing and tone).
    
    Output MUST be valid JSON, exactly like this:
    [
      {
        "text_input": "The synthetic student question...",
        "output": "The professor's response..."
      },
      ...
    ]
    
    Here are the text blocks:
    """
    
    for i, block in enumerate(blocks):
        prompt += f"\n\n--- BLOCK {i+1} ---\n{block}"
        
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=[prompt],
            config=types.GenerateContentConfig(
                response_mime_type="application/json"
            )
        )
        return json.loads(response.text)
    except Exception as e:
        print(f"Error generating pairs: {e}")
        return []

def main():
    if not os.path.exists(TRANSCRIPT_DIR):
        print(f"❌ Directory {TRANSCRIPT_DIR} not found.")
        return
        
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    files = glob.glob(os.path.join(TRANSCRIPT_DIR, "*.txt"))
    
    print(f"Found {len(files)} transcript files.")
    
    all_chunks = []
    for fpath in files:
        with open(fpath, "r", encoding="utf-8") as f:
            text = f.read()
            chunks = chunk_text(text, chunk_size=1200) # roughly 200 words
            all_chunks.extend(chunks)
            
    print(f"Total blocks extracted: {len(all_chunks)}")
    
    # Count existing pairs to resume
    existing_pairs = 0
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, 'r') as f:
            existing_pairs = sum(1 for line in f if line.strip())
            
    print(f"Found {existing_pairs} existing pairs. Resuming from chunk {existing_pairs}...")
    
    # Process in batches of 4 to save API calls
    BATCH_SIZE = 4
    total_generated = 0
    
    with open(OUTPUT_FILE, "a", encoding="utf-8") as out_file:
        # For demo purposes, limit to 50 batches (200 pairs)
        max_batches = min(50, (len(all_chunks) - existing_pairs) // BATCH_SIZE)
        
        # Start from where we left off
        for i in range(existing_pairs, existing_pairs + (max_batches * BATCH_SIZE), BATCH_SIZE):
            batch = all_chunks[i:i+BATCH_SIZE]
            print(f"Processing batch {i//BATCH_SIZE + 1}/{max_batches}...")
            
            pairs = generate_pairs(batch)
            
            for pair in pairs:
                if "text_input" in pair and "output" in pair:
                    json.dump(pair, out_file)
                    out_file.write('\n')
                    total_generated += 1
                    
            # Be nice to the rate limit
            time.sleep(4)
            
    print(f"✅ Finished! Generated {total_generated} training pairs.")
    print(f"Data saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
