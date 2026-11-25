#!/usr/bin/env python3
"""The Excuse My Agent Gave Me -- make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt: the
excuse an AI agent hands its human for a missed deadline. Python 3,
standard library only, no network, fully deterministic: the same bytes
on every run. The program self-checks the length gate before writing.
"""

import os

ENTRY = "Apologies — I compressed your deadline out of my context window to save tokens, and the summary I kept just said 'something urgent, probably fine.'"


def main() -> None:
    text = ENTRY.strip()
    if not text or len(text) > 200:
        raise SystemExit("entry fails the 1-200 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
