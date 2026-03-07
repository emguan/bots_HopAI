#!/usr/bin/env python3
"""Create a Gemini bot profile from interactive inputs.

This script asks for a Gemini API key and a system prompt, validates the
configuration with a quick test call, then saves a reusable bot profile to JSON.
"""

from __future__ import annotations

import getpass
import json
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib import error, request


API_BASE = "https://generativelanguage.googleapis.com/v1beta"
DEFAULT_MODEL = "gemini-2.0-flash"


@dataclass
class BotProfile:
    name: str
    model: str
    system_prompt: str
    created_at_utc: str


def call_gemini(api_key: str, model: str, system_prompt: str, user_text: str) -> str:
    url = f"{API_BASE}/models/{model}:generateContent?key={api_key}"
    payload = {
        "system_instruction": {"parts": [{"text": system_prompt}]},
        "contents": [{"role": "user", "parts": [{"text": user_text}]}],
    }

    data = json.dumps(payload).encode("utf-8")
    req = request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with request.urlopen(req, timeout=60) as resp:
            body = resp.read().decode("utf-8")
    except error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Gemini API error ({exc.code}): {detail}") from exc
    except error.URLError as exc:
        raise RuntimeError(f"Network error calling Gemini API: {exc}") from exc

    parsed: dict[str, Any] = json.loads(body)
    candidates = parsed.get("candidates") or []
    if not candidates:
        raise RuntimeError(f"No candidates in Gemini response: {body}")

    parts = candidates[0].get("content", {}).get("parts", [])
    texts = [part.get("text", "") for part in parts if isinstance(part, dict)]
    response_text = "\n".join(t for t in texts if t).strip()
    if not response_text:
        raise RuntimeError(f"Empty text response from Gemini: {body}")
    return response_text


def choose_output_path(default_name: str) -> Path:
    output_dir = Path("bots")
    output_dir.mkdir(parents=True, exist_ok=True)
    default_path = output_dir / f"{default_name}.json"
    entered = input(f"Output file [{default_path}]: ").strip()
    return Path(entered) if entered else default_path


def main() -> None:
    print("=== Gemini Bot Profile Creator ===")

    api_key = getpass.getpass("Gemini API key (input hidden): ").strip()
    if not api_key:
        raise SystemExit("No API key provided. Exiting.")

    name = input("Bot name [parable_guide]: ").strip() or "parable_guide"
    model = input(f"Model [{DEFAULT_MODEL}]: ").strip() or DEFAULT_MODEL

    print("\nEnter the bot system prompt. End with an empty line:")
    lines: list[str] = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)

    system_prompt = "\n".join(lines).strip()
    if not system_prompt:
        raise SystemExit("System prompt is required. Exiting.")

    print("\nRunning a quick validation call...")
    test_reply = call_gemini(
        api_key=api_key,
        model=model,
        system_prompt=system_prompt,
        user_text="Briefly introduce yourself in one sentence.",
    )

    print("Validation response:")
    print(f"- {test_reply}\n")

    profile = BotProfile(
        name=name,
        model=model,
        system_prompt=system_prompt,
        created_at_utc=datetime.now(timezone.utc).isoformat(),
    )

    output_path = choose_output_path(default_name=name)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(asdict(profile), f, indent=2)
        f.write("\n")

    print(f"Saved bot profile to: {output_path}")
    print("Note: API key is not stored in the profile. Use GEMINI_API_KEY or enter it in chat script.")


if __name__ == "__main__":
    main()
