# Running the Gemini Bot Workflow (Notebook)

This project now uses a single interactive notebook for creating and chatting with Gemini bot profiles.

## Primary File

- `notebooks/run_gemini_scripts.ipynb`

## Prerequisites

- Python 3 with Jupyter support
- A valid Gemini API key
- Internet access (Gemini REST API calls)

## How to Run

1. Open `notebooks/run_gemini_scripts.ipynb` in Jupyter.
2. Run cells top-to-bottom.
3. Provide your API key when prompted (or set `GEMINI_API_KEY` first).
4. Configure bot fields (`BOT_NAME`, `MODEL`, `SYSTEM_PROMPT`).
5. Run validation, save profile to `bots/*.json`, load a profile, and start chat.

## Notebook Sections

- Setup/imports and HTTP helper
- Bot configuration
- API key loading
- Validation call
- Save profile JSON
- Load saved profile
- Interactive multi-turn chat (`/exit` to quit)
- Optional one-shot helper

## Optional: set API key in shell first

```bash
export GEMINI_API_KEY="your_api_key_here"
```

## File Output

The notebook writes profiles to:

- `bots/<bot_name>.json`

API keys are not written to disk by default.

## Validation

Check notebook JSON validity:

```bash
python -m json.tool notebooks/run_gemini_scripts.ipynb > /dev/null
```
