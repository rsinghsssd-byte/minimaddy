"""
finetune.py

Uploads the synthesized dataset and kicks off a fine-tuning job on Gemini.
"""

import os
import time
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ GEMINI_API_KEY not found in .env")
    sys.exit(1)

client = genai.Client(api_key=api_key)

DATASET_FILE = "output/finetuning_dataset.jsonl"
# We fine-tune a smaller model because 1.5-flash supports tuning perfectly
BASE_MODEL = "models/gemini-1.5-flash-001-tuning"
TUNED_MODEL_NAME = "mini-maddy-persona"

def main():
    if not os.path.exists(DATASET_FILE):
        print(f"❌ Dataset not found at {DATASET_FILE}")
        sys.exit(1)
        
    print(f"1. Uploading dataset {DATASET_FILE} to Google AI Studio...")
    # Read how many lines there are
    with open(DATASET_FILE, "r") as f:
        num_pairs = sum(1 for _ in f)
    print(f"   Found {num_pairs} training pairs.")
    
    if num_pairs < 20:
        print("   ⚠️ Warning: Google recommends at least 20 pairs for tuning. Ideally 100+.")
        
    try:
        # Upload the file
        dataset_file = client.files.upload(file=DATASET_FILE)
        print(f"   Uploaded as: {dataset_file.name}")
        
        # Wait for file processing
        print("   Waiting for file processing to complete...")
        while True:
            dataset_file = client.files.get(name=dataset_file.name)
            if dataset_file.state.name != "PROCESSING":
                break
            time.sleep(2)
            
        if dataset_file.state.name == "FAILED":
            print("❌ File processing failed.")
            sys.exit(1)
            
        print("   File processed successfully!")
        
        # Start tuning
        print(f"\n2. Starting fine-tuning job on {BASE_MODEL}...")
        
        # In the new SDK, tunings is available via client.tunings
        # We wrap in a try-except because SDK syntax sometimes varies (create vs tune)
        operation = client.tunings.tune(
            base_model=BASE_MODEL,
            training_dataset=dataset_file,
            config={
                "display_name": TUNED_MODEL_NAME,
                "epoch_count": 3
            }
        )
        
        print(f"\n✅ Tuning job started successfully!")
        print(f"   Operation Name: {operation.name}")
        print("\n   The job will take anywhere from 10 to 30 minutes to complete.")
        print("   You can check its status in the Google AI Studio console.")
        print("   Once complete, your tuned model ID will be available (e.g., tunedModels/mini-maddy-persona-123).")
        print("\n   Add it to your .env file:")
        print("   TUNED_MODEL_ID=tunedModels/your-new-id")
        
    except Exception as e:
        print(f"\n❌ Error during tuning: {e}")
        # Try alternate syntax if client.tunings.tune fails
        print("Attempting alternate SDK syntax (client.models.create_tuned_model)...")
        try:
            operation = client.models.create_tuned_model(
                source_model=BASE_MODEL,
                training_data=dataset_file,
                id=TUNED_MODEL_NAME,
            )
            print(f"✅ Tuning job started successfully! Model ID: {operation.name}")
        except Exception as e2:
            print(f"❌ Alternate syntax also failed: {e2}")

if __name__ == "__main__":
    main()
