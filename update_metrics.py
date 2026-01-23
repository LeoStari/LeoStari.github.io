import requests
import json
import os

# Your ORCID to identify you in OpenAlex
ORCID_ID = "https://orcid.org/0000-0002-8194-4630"

def update_metrics():
    print(f"Fetching metrics for {ORCID_ID}...")
    
    # 1. Get Author Data from OpenAlex
    url = f"https://api.openalex.org/authors/{ORCID_ID}"
    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
        
        # 2. Extract metrics
        stats = {
            "citations": data.get("cited_by_count", 0),
            "hindex": data.get("summary_stats", {}).get("h_index", 0),
            "pubs": data.get("works_count", 0)
        }
        
        print(f"Found: {stats}")
        
        # 3. Save to _data/metrics.json
        os.makedirs("_data", exist_ok=True)
        with open("_data/metrics.json", "w") as f:
            json.dump(stats, f, indent=2)
            
        print("Success! _data/metrics.json updated.")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_metrics()