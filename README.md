### Transcript to Summary

A small Python project that reads a document (TXT, DOCX, or PDF) and produces a concise extractive summary. Includes structured logging, config management, and a simple CLI.

### Features
- Reads `.txt` by default; `.docx` if `python-docx` installed; `.pdf` if `PyPDF2` installed
- Extractive summarization using a lightweight frequency-based method
- Logs to `logs/app.log` and console
- Config support via `config/local-settings.json` (ignored by git). Example provided

### Quickstart
1. Create and activate a virtual environment
```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. (Optional) Create `config/local-settings.json` for local credentials/keys
```json
{
  "openai_api_key": "YOUR_KEY_HERE"
}
```
Note: This file is git-ignored. Do not commit credentials.

4. Run the CLI
```bash
python -m transcript_to_summary --input tests/data/sample.txt --sentences 3
```

5. Run tests
```bash
pytest -q
```

### Security and Git Hygiene
- Sensitive files like `config/local-settings.json` and generated logs are ignored by git
- `logs/` directory is kept in repo via `logs/.gitkeep` but actual log files are not committed

### Project Structure
```
src/
  transcript_to_summary/
    __init__.py
    __main__.py
    cli.py
    config.py
    logger.py
    reader.py
    summarizer.py
config/
  .gitkeep
  local-settings.example.json
logs/
  .gitkeep
tests/
  data/sample.txt
  test_reader.py
  test_summarizer.py
```

### Notes
- PDF and DOCX support are optional; install extras from `requirements.txt`.
- The summarizer is intentionally simple; swap in your preferred algorithm easily in `summarizer.py`.
