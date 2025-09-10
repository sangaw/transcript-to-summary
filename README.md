### Transcript to Summary

A small Python project that reads a document (TXT, DOCX, or PDF) and produces a concise extractive summary. Includes structured logging, config management, and a simple CLI.

### Features
- Reads `.txt` by default; `.docx` if `python-docx` installed; `.pdf` if `PyPDF2` installed
- Extractive summarization using a local TextRank implementation (sumy + NLTK)
- Logs to `logs/app.log` and console
- Config support via `config/local-settings.json` (ignored by git). Example provided

### Quickstart
1. Create and activate a virtual environment
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
python -m venv .venv
.venv\Scripts\activate
```

2. Install in editable mode (recommended)
```powershell
pip install -e .
```

3. (Optional) Create `config/local-settings.json` for local credentials/keys
```json
{
  "openai_api_key": "YOUR_KEY_HERE"
}
```
Note: This file is git-ignored. Do not commit credentials.

4. Run the CLI on a single file
```powershell
python -m transcript_to_summary --input tests\data\sample.txt --sentences 3
```

5. Data folders mode (DOCX -> DOCX summaries)
- Place your `.docx` files into `data/input/`
- Run:
```powershell
python -m transcript_to_summary --use-data-folders --sentences 5
```
- Summaries will be written as `.docx` files to `data/output/` with suffix `_summary.docx`

6. (Optional) Create a sample DOCX if missing and summarize it
```powershell
python -m transcript_to_summary --input tests\data\sample_transcript.docx --sentences 3 --generate-sample-docx
```

7. Run tests
```powershell
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
data/
  input/
    .gitkeep
  output/
    .gitkeep
tests/
  data/sample.txt
  test_reader.py
  test_summarizer.py
```

### Notes
- First run downloads NLTK resources automatically (`punkt`, `punkt_tab`). If offline, run:
  `python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"`
- The summarizer uses TextRank via `sumy`; ensure `numpy` is installed (included in dependencies).
