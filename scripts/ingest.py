import os
import requests
import sys

# --- CONFIG ---
YEAR = "2024"
MONTH = "01"
TYPE = "yellow"
URL = f"https://d37ci6vzurychx.cloudfront.net/trip-data/{TYPE}_tripdata_{YEAR}-{MONTH}.parquet"

# --- PATHS ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "data_lake", "raw")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, f"{TYPE}_tripdata_{YEAR}-{MONTH}.parquet")

def ingest():
    print(f"--- Starting Ingestion: {TYPE} Taxi Data {YEAR}-{MONTH} ---")
    
    # 1. Create Folder
    if not os.path.exists(OUTPUT_DIR):
        print(f"Creating: {OUTPUT_DIR}")
        os.makedirs(OUTPUT_DIR)

    # 2. Check Exists
    if os.path.exists(OUTPUT_FILE):
        print(f"Skipping: File exists at {OUTPUT_FILE}")
        return

    # 3. Download
    print(f"Downloading {URL}...")
    try:
        with requests.get(URL, stream=True) as r:
            r.raise_for_status()
            with open(OUTPUT_FILE, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print("Success!")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    ingest()
