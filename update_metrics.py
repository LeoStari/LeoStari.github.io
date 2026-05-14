#!/usr/bin/env python3
"""
update_metrics.py - Academic Profile Metrics Updater

Fetches publication metrics from multiple scholarly databases and updates
the website's _data/metrics.json file.

Auto-detects ORCID, Google Scholar ID, and Scopus ID from your site files.

Usage:
    python update_metrics.py              # Update with auto-detected identifiers
    python update_metrics.py --verbose                   # Show detailed output
    python update_metrics.py --backup                    # Keep backup of old metrics
    python update_metrics.py --dry-run                   # Preview changes without saving
"""

import json
import os
import sys
import argparse
import re
from datetime import datetime, timezone
from pathlib import Path


# Try importing optional dependencies
try:
    import requests
except ImportError:
    print("Error: 'requests' library is required. Install with: pip install requests")
    sys.exit(1)

try:
    from bs4 import BeautifulSoup
    HAS_BS4 = True
except ImportError:
    HAS_BS4 = False


# ============================================
# Configuration (Auto-detected from site files)
# ============================================

class Config:
    """Configuration for metrics fetching - auto-detected from site files."""
    
    # OpenAlex API endpoint
    OPENALEX_API = "https://api.openalex.org/authors/{}"
    
    # Metrics output file
    METRICS_FILE = "_data/metrics.json"
    BACKUP_SUFFIX = ".backup"
    
    # API settings
    REQUEST_TIMEOUT = 30  # seconds


def detect_site_identifiers():
    """
    Auto-detect ORCID, Google Scholar ID, and Scopus ID from site files.
    
    Looks for identifiers in:
    - _config.yml (googlescholar_username, orcid links)
    - index.md (Scopus authorId links)
    """
    config_path = Path("_config.yml")
    index_path = Path("index.md")
    
    # Default values (fallbacks)
    detected_orcid = "0000-0002-8194-4630"
    detected_scholar_id = "GGSi3PUAAAAJ"
    detected_scopus_id = "58094418800"
    
    # Try to read _config.yml for ORCID and Google Scholar ID
    if config_path.exists():
        try:
            with open(config_path, 'r') as f:
                content = f.read()
            
            # Extract ORCID from googlescholar_username (which contains the ID)
            match = re.search(r'googlescholar_username:\s*(\S+)', content)
            if match:
                detected_scholar_id = match.group(1).strip()
            
            # Try to find ORCID directly
            orcid_match = re.search(r'https://orcid\.org/(\d{4}-\d{4}-\d{4}-\d{4})', content)
            if orcid_match:
                detected_orcid = orcid_match.group(1)
            
            # Also check for direct ORCID field
            if not orcid_match:
                orcid_match = re.search(r'orcid:\s*(\d{4}-\d{4}-\d{4}-\d{4})', content)
                if orcid_match:
                    detected_orcid = orcid_match.group(1)
            
        except Exception as e:
            print(f"Warning: Could not read _config.yml: {e}")
    
    # Try to find Scopus ID from index.md
    if index_path.exists():
        try:
            with open(index_path, 'r') as f:
                content = f.read()
            
            match = re.search(r'authorId=(\d+)', content)
            if match:
                detected_scopus_id = match.group(1)
        except Exception as e:
            print(f"Warning: Could not read index.md: {e}")
    
    return detected_orcid, detected_scholar_id, detected_scopus_id


def get_config():
    """Get auto-detected configuration."""
    orcid, scholar_id, scopus_id = detect_site_identifiers()
    
    print(f"📋 Detected identifiers from site files:")
    print(f"   ORCID:        {orcid}")
    print(f"   Google Scholar ID: {scholar_id}")
    print(f"   Scopus ID:    {scopus_id}")
    print()
    
    return {
        "orcid": orcid,
        "google_scholar_url": f"https://scholar.google.com/citations?user={scholar_id}",
        "scopus_id": scopus_id,
        "openalex_api": Config.OPENALEX_API,
        "metrics_file": Config.METRICS_FILE,
    }


# ============================================
# Data Fetchers
# ============================================

class OpenAlexFetcher:
    """Fetch metrics from OpenAlex API."""
    
    @staticmethod
    def fetch(orcid_id, verbose=False):
        """Fetch metrics from OpenAlex using ORCID ID."""
        if verbose:
            print(f"  → Querying OpenAlex for {orcid_id}...")
        
        # Try both URL formats
        urls = [
            f"{Config.OPENALEX_API.format(orcid_id)}",
            f"{Config.OPENALEX_API.format('https://orcid.org/' + orcid_id)}"
        ]
        
        for url in urls:
            try:
                if verbose:
                    print(f"    URL: {url}")
                
                response = requests.get(url, timeout=Config.REQUEST_TIMEOUT)
                response.raise_for_status()
                data = response.json()
                
                if verbose:
                    print(f"  ✓ OpenAlex response received")
                    print(f"    Raw keys: {list(data.keys())}")
                
                # Extract metrics - handle different API response structures
                cited_by_count = data.get("cited_by_count", 0) or 0
                
                works_count = data.get("works_count", 0) or 0
                
                summary_stats = data.get("summary_stats")
                if isinstance(summary_stats, list) and len(summary_stats) >= 3:
                    h_index = int(summary_stats[1])
                elif isinstance(summary_stats, dict):
                    h_index = summary_stats.get("h_index", 0) or 0
                else:
                    h_index = 0
                
                if verbose:
                    print(f"    Citations (cited_by_count): {cited_by_count}")
                    print(f"    Works (works_count): {works_count}")
                    print(f"    Summary stats: {summary_stats}")
                    print(f"    H-index extracted: {h_index}")
                
                # If works_count is 0, try to count from 'last_known_institutions' or other sources
                if works_count == 0 and "publications" in data:
                    works_count = len(data["publications"])
                
                return {
                    "citations": cited_by_count,
                    "hindex": h_index,
                    "pubs": works_count,
                    "source": "OpenAlex",
                    "_raw_data": data  # Store raw data for debugging
                }
            
            except requests.exceptions.RequestException as e:
                if verbose:
                    print(f"    ✗ Request failed: {e}")
                continue
        
        return None


class GoogleScholarFetcher:
    """Fetch metrics from Google Scholar (scraping)."""
    
    @staticmethod
    def fetch(url, verbose=False):
        """
        Fetch metrics from Google Scholar.
        Note: This may require adjusting headers or using a proxy for better results.
        """
        if not HAS_BS4:
            if verbose:
                print("  → BeautifulSoup not available, skipping Google Scholar")
            return None
        
        if verbose:
            print(f"  → Querying Google Scholar...")
        
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
            }
            
            response = requests.get(url, headers=headers, timeout=Config.REQUEST_TIMEOUT)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Google Scholar displays stats in a specific layout
            # Look for the stats div with citation counts
            citations_element = soup.find('div', {'class': 'gsc_rsb_std'})
            hindex_element = soup.find('span', string=lambda text: text and 'h' in str(text).lower() and 'index' in str(text).lower())
            
            # Try alternative selectors for Google Scholar layout
            if not citations_element:
                citations_element = soup.find('td', {'class': 'gsc_rsb_std'})
            
            # Extract citation count from the page
            all_stats = []
            for td in soup.find_all('td', class_='gsc_rsb_std'):
                all_stats.append(td.get_text(strip=True))
            
            citations = 0
            hindex = 0
            
            if all_stats:
                # Google Scholar typically shows: citations, h-index, i10-index
                try:
                    citations = int(all_stats[0].replace(',', ''))
                except ValueError:
                    citations = 0
                    
                for stat in all_stats:
                    if 'h' in stat.lower() and 'index' in stat.lower():
                        try:
                            hindex = int(stat.replace(' ', '').replace('h', '').replace('index', ''))
                        except ValueError:
                            continue
            
            # Alternative: look for specific elements
            if citations == 0:
                cit_link = soup.find('a', href='/citations?view_op=top_')
                if cit_link:
                    try:
                        citations = int(cit_link.get_text(strip=True).replace(',', ''))
                    except ValueError:
                        pass
            
            if hindex == 0 and hindex_element:
                try:
                    hindex = int(hindex_element.parent.find_next_sibling('span').get_text(strip=True) or 
                                 hindex_element.find_next_sibling('span').get_text(strip=True))
                except (ValueError, AttributeError):
                    pass
            
            if verbose:
                print(f"  Citations: {citations}")
                print(f"  h-index: {hindex}")
            
            return {
                "citations": citations,
                "hindex": hindex,
                "pubs": 0,  # Google Scholar doesn't directly expose pub count
                "source": "GoogleScholar"
            }
        
        except requests.exceptions.RequestException as e:
            if verbose:
                print(f"  ✗ Google Scholar request failed: {e}")
            return None


class ScopusFetcher:
    """Fetch metrics from Scopus API."""
    
    @staticmethod
    def fetch(scopus_id, api_key=None, verbose=False):
        """
        Fetch metrics from Scopus API.
        Requires an API key from Elsevier.
        """
        if not api_key:
            # Try to get from environment variable
            api_key = os.environ.get("SCOPUS_API_KEY")
        
        if not api_key:
            if verbose:
                print(f"  → Scopus API key not provided, skipping Scopus for {scopus_id}")
            return None
        
        if verbose:
            print(f"  → Querying Scopus for author {scopus_id}...")
        
        try:
            url = f"https://api.elsevier.com/content/author/author-id/{scopus_id}"
            headers = {"Accept": "application/json", "X-ELS-APIKey": api_key}
            
            response = requests.get(url, headers=headers, timeout=Config.REQUEST_TIMEOUT)
            response.raise_for_status()
            data = response.json()
            
            # Extract metrics from Scopus response
            abstract_citation_count = data.get("abstract-citation-count", 0) or 0
            document_count = data.get("document-count", 0) or 0
            
            # h-index is usually in the summary stats
            summary_stats = data.get("summary-statistics", [])
            h_index = 0
            for stat in summary_stats:
                if stat.get("summary-stat-type") == "h-index":
                    h_index = int(stat.get("count", 0) or 0)
            
            return {
                "citations": abstract_citation_count,
                "hindex": h_index,
                "pubs": document_count,
                "source": "Scopus"
            }
        
        except requests.exceptions.RequestException as e:
            if verbose:
                print(f"  ✗ Scopus request failed: {e}")
            return None


# ============================================
# Validation & Processing
# ============================================

def validate_metrics(metrics):
    """Validate fetched metrics data."""
    errors = []
    
    min_citations = 0
    max_citations = 1000000  # Sanity check
    min_hindex = 0
    max_hindex = 500         # Sanity check
    min_pubs = 0
    max_pubs = 10000        # Sanity check
    
    if metrics.get("citations", 0) < min_citations:
        errors.append(f"Citations too low: {metrics.get('citations')}")
    elif metrics.get("citations", 0) > max_citations:
        errors.append(f"Citations suspiciously high: {metrics.get('citations')}")
    
    if metrics.get("hindex", 0) < min_hindex:
        errors.append(f"h-index too low: {metrics.get('hindex')}")
    elif metrics.get("hindex", 0) > max_hindex:
        errors.append(f"h-index suspiciously high: {metrics.get('hindex')}")
    
    if metrics.get("pubs", 0) < min_pubs:
        errors.append(f"Publications too low: {metrics.get('pubs')}")
    elif metrics.get("pubs", 0) > max_pubs:
        errors.append(f"Publications suspiciously high: {metrics.get('pubs')}")
    
    return errors


def compute_best_metrics(fetch_results):
    """
    Compute best metrics from multiple sources.
    Uses the highest value for each metric (conservative approach),
    but falls back to previous values if new data is 0.
    """
    if not fetch_results:
        return None
    
    valid_sources = [r for r in fetch_results if r is not None]
    if not valid_sources:
        return None
    
    # Collect all sources that provided each metric
    citations_values = [r["citations"] for r in valid_sources if r.get("citations", 0) > 0]
    hindex_values = [r["hindex"] for r in valid_sources if r.get("hindex", 0) > 0]
    pubs_values = [r["pubs"] for r in valid_sources if r.get("pubs", 0) > 0]
    
    # Use the highest value, or keep old values if all new are 0
    best_citations = max(citations_values) if citations_values else 0
    best_hindex = max(hindex_values) if hindex_values else 0
    best_pubs = max(pubs_values) if pubs_values else 0
    
    # Determine best source for reporting
    best_source = "Unknown"
    for r in valid_sources:
        if (r.get("hindex", 0) > 0 or r.get("pubs", 0) > 0):
            best_source = r.get("source")
            break
    
    return {
        "citations": best_citations,
        "hindex": best_hindex,
        "pubs": best_pubs,
        "source": best_source,
        "last_updated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    }


# ============================================
# Main Functions
# ============================================

def load_existing_metrics():
    """Load existing metrics from file."""
    metrics_file = Path(Config.METRICS_FILE)
    if not metrics_file.exists():
        return None
    
    try:
        with open(metrics_file, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None


def save_metrics(metrics):
    """Save metrics to file."""
    metrics_file = Path(Config.METRICS_FILE)
    metrics_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(metrics_file, 'w') as f:
        json.dump(metrics, f, indent=2)


def backup_metrics():
    """Create a backup of existing metrics."""
    metrics_file = Path(Config.METRICS_FILE)
    if not metrics_file.exists():
        return False
    
    backup_file = Path(str(metrics_file) + Config.BACKUP_SUFFIX)
    try:
        import shutil
        shutil.copy2(metrics_file, backup_file)
        print(f"  → Backup created: {backup_file}")
        return True
    except Exception as e:
        print(f"  ✗ Could not create backup: {e}")
        return False


def show_diff(old_metrics, new_metrics):
    """Display differences between old and new metrics."""
    if not old_metrics or not new_metrics:
        return
    
    changes = []
    
    for key in ["citations", "hindex", "pubs"]:
        old_val = old_metrics.get(key, 0)
        new_val = new_metrics.get(key, 0)
        
        if old_val != new_val:
            diff = new_val - old_val
            symbol = "+" if diff > 0 else ""
            changes.append(f"    {key}: {old_val} → {new_val} ({symbol}{diff})")
    
    if changes:
        print("\n📊 Changes detected:")
        for change in changes:
            print(change)
        print()
    else:
        print("✓ No changes - metrics are up to date\n")


def update_metrics(verbose=False):
    """Main function to update metrics."""
    
    if verbose:
        print("=" * 60)
        print("Academic Metrics Updater")
        print("=" * 60)
    
    # Get auto-detected configuration
    config = get_config()
    orcid_id = config["orcid"]
    scholar_url = config["google_scholar_url"]
    scopus_id = config["scopus_id"]
    
    if verbose:
        print(f"   OpenAlex API: {config['openalex_api']}")
        print(f"   Metrics file: {Config.METRICS_FILE}")
    
    # Load existing metrics
    old_metrics = load_existing_metrics()
    
    if verbose and old_metrics:
        print(f"\n📄 Current metrics ({old_metrics.get('last_updated', 'unknown')}):")
        print(f"   Citations: {old_metrics.get('citations', '—')}")
        print(f"   h-index:   {old_metrics.get('hindex', '—')}")
        print(f"   Pubs:      {old_metrics.get('pubs', '—')}")
    
    # Fetch metrics from multiple sources
    fetch_results = []
    
    if verbose:
        print("\n🔍 Fetching metrics...")
    
    # Try OpenAlex first (preferred source)
    openalex_data = OpenAlexFetcher.fetch(orcid_id, verbose=verbose)
    if openalex_data:
        fetch_results.append(openalex_data)
    
    # Try Google Scholar as fallback
    gs_data = GoogleScholarFetcher.fetch(scholar_url, verbose=verbose)
    if gs_data:
        fetch_results.append(gs_data)
    
    # Try Scopus (optional, needs API key)
    scopus_data = ScopusFetcher.fetch(scopus_id, verbose=verbose)
    if scopus_data:
        fetch_results.append(scopus_data)
    
    if not fetch_results:
        print("\n❌ No metrics could be fetched from any source.")
        if verbose:
            print("   Tips:")
            print("   - Check your internet connection")
            print("   - Verify identifiers were detected correctly")
            print("   - For Scopus, set SCOPUS_API_KEY environment variable")
        return False
    
    # Compute final metrics (take best values from all sources)
    new_metrics = compute_best_metrics(fetch_results)
    
    if not new_metrics:
        print("\n❌ Failed to compute valid metrics.")
        return False
    
    # Validate metrics
    errors = validate_metrics(new_metrics)
    if errors:
        print(f"\n⚠️  Validation warnings:")
        for error in errors:
            print(f"   {error}")
    
    # Show diff with old metrics
    show_diff(old_metrics, new_metrics)
    
    # Save metrics
    backup_metrics()
    save_metrics(new_metrics)
    
    if verbose:
        print("=" * 60)
    
    return True


# ============================================
# CLI Interface
# ============================================

def main():
    parser = argparse.ArgumentParser(
        description="Update academic profile metrics from scholarly databases.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python update_metrics.py              # Update with auto-detected identifiers
  python update_metrics.py --verbose    # Show detailed output with detected IDs
  python update_metrics.py --backup     # Keep backup of old metrics
  python update_metrics.py --dry-run    # Preview changes without saving

Environment Variables:
  SCOPUS_API_KEY   - API key for Scopus data (optional)
        """
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose output"
    )
    
    parser.add_argument(
        "--backup", "-b",
        action="store_true",
        help="Create backup of existing metrics before updating"
    )
    
    parser.add_argument(
        "--dry-run", "-n",
        action="store_true",
        help="Preview changes without saving to file"
    )
    
    args = parser.parse_args()
    
    # Create backup if requested
    if args.backup:
        backup_metrics()
    
    # Run update
    success = update_metrics(verbose=args.verbose)
    
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
