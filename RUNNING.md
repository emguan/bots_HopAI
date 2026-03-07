# Running the Gemini Bot Tools

This project includes two Python scripts and one Jupyter notebook for creating and chatting with Gemini-powered bot profiles.

## Prerequisites

- Python 3.10+ (or another modern Python 3 version)
- A valid Gemini API key
- Internet access (scripts call Gemini REST APIs)

## Project Files

- `scripts/create_gemini_bot.py` – create and validate a bot profile
- `scripts/chat_with_gemini_bot.py` – interactive chat with a saved profile
- `notebooks/run_gemini_scripts.ipynb` – notebook wrapper to run both scripts

## 1) Create a Bot Profile

Run:

```bash
python scripts/create_gemini_bot.py
```

You will be prompted for:

1. Gemini API key (hidden input)
2. Bot name (default: `parable_guide`)
3. Model (default: `gemini-2.0-flash`)
4. System prompt (multi-line; end with empty line)

What happens next:

- The script performs a quick validation request to Gemini.
- If successful, it saves a profile JSON to `bots/<name>.json` (or your custom path).
- The API key is **not** saved in the profile.

## 2) Chat with a Saved Bot Profile

Run:

```bash
python scripts/chat_with_gemini_bot.py
```

Behavior:

- Lists profiles in `bots/*.json`
- Lets you choose a profile by number
- Uses `GEMINI_API_KEY` if present, otherwise asks for key interactively
- Starts chat loop and preserves conversation history across turns
- Use `/exit` (or `exit` / `quit`) to stop

### Optional: set API key once per shell session

```bash
export GEMINI_API_KEY="your_api_key_here"
python scripts/chat_with_gemini_bot.py
```

## 3) Run from Jupyter Notebook

Open:

```text
notebooks/run_gemini_scripts.ipynb
```

Notebook flow:

- Verifies script paths
- Runs `create_gemini_bot.py`
- Runs `chat_with_gemini_bot.py`

> Note: Both scripts are interactive, so they will still prompt for input when launched from notebook cells.

## Quick Validation Commands

You can validate local script syntax and notebook JSON format with:

```bash
python -m py_compile scripts/create_gemini_bot.py scripts/chat_with_gemini_bot.py
python -m json.tool notebooks/run_gemini_scripts.ipynb > /dev/null
```
