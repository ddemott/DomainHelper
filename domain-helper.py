# Import required modules
import requests  # For making HTTP requests to the domain API
import time      # For rate limiting API calls
from itertools import product  # For generating combinations of prefixes and suffixes
import os        # For operating system dependent functionality


# ---- API Configuration ----:
API_KEY_FILE = "api_key.txt"  # File containing your API key
API_URL = "https://api.api-ninjas.com/v1/domain"      # API endpoint for domain checking

# Load the API key from an external file
if os.path.exists(API_KEY_FILE):
    with open(API_KEY_FILE, "r") as f:
        API_KEY = f.read().strip()
else:
    raise FileNotFoundError(f"API key file '{API_KEY_FILE}' not found. Please create it and add your API key.")

HEADERS = {"X-Api-Key": API_KEY}                     # HTTP headers for authentication


# ---- Domain Generation Config ----
WORDLIST_FILE = "words.txt"  # File containing base words for domain names
PREFIXES = ["", "the", "my"]  # Prefixes to prepend to base words
SUFFIXES = ["", "app", "hub", "tech", "hq", "lab"]  # Suffixes to append to base words
RATE_LIMIT = 1.0  # Seconds between API calls (to avoid hitting rate limits)


def load_words(file):
    """
    Load a list of words from a file, stripping whitespace and converting to lowercase.
    Returns a list of words.
    """
    with open(file, "r") as f:
        return [w.strip().lower() for w in f if w.strip()]


def check_domain(domain):
    """
    Check if a domain is available using the API.
    Returns True if available, False otherwise.
    """
    try:
        r = requests.get(API_URL, headers=HEADERS, params={"domain": domain})
        if r.status_code == 200:
            data = r.json()
            return data.get("available", False)
        else:
            print(f"Error {r.status_code} for {domain}")
    except Exception as e:
        print(f"Failed {domain}: {e}")
    return False


def main():
    """
    Main function to generate domain candidates, check their availability, and save results.
    """
    # Load base words from file
    bases = load_words(WORDLIST_FILE)

    # Generate all possible domain candidates with prefixes, suffixes, and .com TLD
    candidates = [
        f"{p}{b}{s}.com"
        for b in bases
        for p, s in product(PREFIXES, SUFFIXES)
        if p or s  # skip empty-empty duplicate
    ]

    available = []  # List to store available domains
    for domain in candidates:
        time.sleep(RATE_LIMIT)  # Respect API rate limit
        if check_domain(domain):
            available.append(domain)
            print(f"[AVAILABLE] {domain}")
        else:
            print(f"[TAKEN] {domain}")

    # Write available domains to output file
    with open("available_com.txt", "w") as out:
        out.write("\n".join(available))
    print(f"\n✅ Done — {len(available)} .com domains available (saved to available_com.txt)")


# Entry point for the script
if __name__ == "__main__":
    main()