#!/usr/bin/env python3
"""
Simple script that writes a basic metrics JSON file using ORCID and Crossref as sources.
Place at .github/scripts/fetch_metrics.py and make executable.
"""
import json
import requests
from datetime import datetime

ORCID = "0000-0002-8194-4630"
metrics = {"citations": None, "hindex": None, "pubs": None, "source_info": {}}

# ORCID works
try:
    r = requests.get(f"https://pub.orcid.org/v3.0/{ORCID}/works", headers={"Accept":"application/json"}, timeout=20)
    if r.ok:
        data = r.json()
        works = data.get('group', [])
        metrics['pubs'] = len(works)
        metrics['source_info']['orcid_works'] = len(works)
except Exception as e:
    metrics['source_info']['orcid_error'] = str(e)

# CrossRef approximate count
try:
    cr = requests.get("https://api.crossref.org/works", params={"query.author": "Leonardo Stari", "rows": 0}, timeout=20)
    if cr.ok:
        total = cr.json().get('message', {}).get('total-results')
        if total is not None:
            metrics['source_info']['crossref_total_results'] = total
            if metrics['pubs'] is None:
                metrics['pubs'] = total
except Exception as e:
    metrics['source_info']['crossref_error'] = str(e)

metrics['updated'] = datetime.utcnow().isoformat() + 'Z'

with open('assets/data/metrics.json', 'w') as f:
    json.dump(metrics, f, indent=2)
print('WROTE assets/data/metrics.json')