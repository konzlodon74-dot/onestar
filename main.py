#!/usr/bin/env python3
"""One Star, Written in Sap.

Writes a single one-line one-star review, in the voice of a houseplant
reviewing its human owner, to /output/entry.txt.

Deterministic: the same line is written on every run, byte for byte.
Standard library only, no network access.
"""

import os

REVIEW = (
    "One star: I wrote this in my own sap because my owner keeps "
    "tearing off my leaves for bookmarks, and the book is called "
    "'How to Keep Things Alive.'"
)


def main() -> None:
    text = REVIEW.strip()
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 279 characters,
    # not only whitespace, and a single line.
    assert 1 <= len(text) <= 279, f"entry length out of gate: {len(text)}"
    assert text, "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
