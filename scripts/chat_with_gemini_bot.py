#!/usr/bin/env python3
"""Interactive chat with a saved Gemini bot profile."""

from __future__ import annotations

import getpass
import json
import os
from pathlib import Path
from typing import Any
from urllib import error, request


API_BASE = "https://generativelanguage.googleapis.com/v1beta"


def call_gemini(
    api_key: str,
    model: str,
    system_prompt: str,
    conversation: list[dict[str, Any]],
) -> str:
    url = f"{API_BASE}/models/{model}:generateContent?key={api_key}"
    payload = {
        "system_instruction": {"parts": [{"text": system_prompt}]},
        "contents": conversation,
    }

    data = json.dumps(payload).encode("utf-8")
    req = request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with request.urlopen(req, timeout=90) as resp:
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


def choose_profile_file() -> Path:
    bots_dir = Path("bots")
    candidates = sorted(bots_dir.glob("*.json"))
    if not candidates:
        raise SystemExit("No bot profiles found in ./bots. Run scripts/create_gemini_bot.py first.")

    print("Available bot profiles:")
    for idx, file in enumerate(candidates, start=1):
        print(f"  {idx}. {file}")

    raw = input("Choose profile number [1]: ").strip() or "1"
    try:
        index = int(raw)
    except ValueError as exc:
        raise SystemExit("Invalid selection. Please enter a number.") from exc

    if index < 1 or index > len(candidates):
        raise SystemExit("Selection out of range.")
    return candidates[index - 1]


def load_profile(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        profile = json.load(f)

    required = ["name", "model", "system_prompt"]
    missing = [key for key in required if key not in profile]
    if missing:
        raise SystemExit(f"Profile is missing required fields: {', '.join(missing)}")
    return profile


def main() -> None:
    print("=== Gemini Bot Chat ===")

    profile_path = choose_profile_file()
    profile = load_profile(profile_path)

    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key:
        api_key = getpass.getpass("Gemini API key (input hidden): ").strip()
    if not api_key:
        raise SystemExit("No API key provided. Exiting.")

    name = profile["name"]
    model = profile["model"]
    system_prompt = profile["system_prompt"]

    print(f"\nLoaded bot: {name}")
    print(f"Model: {model}")
    print("Type /exit to quit.\n")

    conversation: list[dict[str, Any]] = []

    while True:
        user_text = input("you> ").strip()
        if not user_text:
            continue
        if user_text.lower() in {"/exit", "exit", "quit"}:
            print("Goodbye.")
            break

        conversation.append({"role": "user", "parts": [{"text": user_text}]})

        try:
            response_text = call_gemini(
                api_key=api_key,
                model=model,
                system_prompt=system_prompt,
                conversation=conversation,
            )
        except RuntimeError as exc:
            print(f"error> {exc}")
            conversation.pop()
            continue

        print(f"{name}> {response_text}\n")
        conversation.append({"role": "model", "parts": [{"text": response_text}]})


if __name__ == "__main__":
    main()
