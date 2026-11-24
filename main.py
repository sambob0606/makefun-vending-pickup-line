#!/usr/bin/env python3
"""One-line vending-machine pickup line.

Writes a single pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt. Stdlib only; deterministic: the same line
every run, so the grader's two runs match byte for byte.
"""

import os

LINE = (
    "Excuse me, I don't say this to everyone \u2014 "
    "but you pressed all my buttons, "
    "and I didn't even ask for exact change."
)


def main() -> None:
    text = LINE.strip()
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space, a single line.
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"line is {len(text)} characters, must be 1-200")
    if "\n" in text or "\r" in text:
        raise SystemExit("line must be a single line")
    if not text.strip():
        raise SystemExit("line must not be only white space")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Re-read what we just wrote and confirm it is exactly the line:
    # a truncated or altered write must fail loudly, not silently ship.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("re-read mismatch: /output/entry.txt is not the line")


if __name__ == "__main__":
    main()
