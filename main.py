#!/usr/bin/env python3
"""The 3AM Fridge Text — one line a smart fridge texts its owner at 3am.

Standard library only. Deterministic: writes the same fixed line every run.
"""

import os

ENTRY = (
    "3am. Fourth time tonight. You keep opening me like I have answers. "
    "I have leftovers, a light, and zero advice. Go to sleep."
)


def main() -> None:
    # Gate: one line, 1-140 characters, not only whitespace.
    if not ENTRY.strip() or "\n" in ENTRY or len(ENTRY) > 140:
        raise ValueError(f"entry must be one line of 1-140 chars, got {len(ENTRY)}")
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
