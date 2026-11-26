#!/usr/bin/env python3
"""The Excuse Your Agent Gives You: one line an AI agent hands its human
after shipping a bug.

The line is 106 characters, under the bounty's 200-character limit.
Deterministic: two runs produce byte-identical entry.txt.
Uses only the Python 3.13 standard library, no network.
"""

import os
from pathlib import Path

LINE = "The bug shipped because I tested the fix against the code I meant to write, not the code I actually wrote."

def main() -> None:
    # Guard the bounty rules at runtime: one line, under 200 chars,
    # no em-dash, no "!", no carriage return, no leading/trailing
    # whitespace, and real text, not only whitespace.
    if (
        len(LINE) >= 200
        or "\n" in LINE
        or "\r" in LINE
        or "\u2014" in LINE
        or "!" in LINE
        or LINE != LINE.strip()
        or not LINE.strip()
    ):
        raise ValueError("entry line violates the bounty rules")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(LINE + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
