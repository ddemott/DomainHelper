# Domain Helper

A Python script to help you find available domain names based on a list of words, prefixes, and suffixes. The script checks domain availability using the API Ninjas Domain API.

## Features
- Generates domain name candidates using configurable prefixes, suffixes, and a word list
- Checks availability for each candidate (currently for `.com` and `.info` domains)
- Respects API rate limits
- Outputs available domains to a text file

## Requirements
- Python 3.7+
- `requests` library
- API Ninjas Domain API key (free tier supported)

## Usage
1. **Install dependencies:**
   ```sh
   pip install requests
   ```
2. **Prepare your word list:**
   - Add your base words (one per line) to `words.txt` in the project directory.
3. **Configure the script (optional):**
   - Edit `PREFIXES`, `SUFFIXES`, and `WORDLIST_FILE` in `domain-helper.py` as needed.
   - Set your API key in the script.
4. **Run the script:**
   ```sh
   python domain-helper.py
   ```
5. **Results:**
   - Available domains will be saved to `available_com.txt`.

## Output
- `available_com.txt`: List of available domain names found.

## Notes
- The script is rate-limited to avoid exceeding free API quotas.
- You can adjust the `RATE_LIMIT` variable for faster or slower checking.
- The script can be extended to support more TLDs or custom logic.

## License
MIT License

## Suggestions for Improvement
- Add support for additional TLDs (e.g., `.net`, `.org`, `.io`).
- Implement multithreading to speed up domain availability checks.
- Add a configuration file to manage settings externally.
- Include a feature to filter domains based on length or specific patterns.
- Enhance error handling and logging for better debugging.
