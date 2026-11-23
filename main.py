#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label for human beings to
/output/entry.txt (at most 160 characters, UTF-8).

The label: a deadpan CAUTION in the voice of a printed product label.
The joke is one idea only -- every human's quiet overconfidence -- and
the turn lands in the last few words.
"""

import os

ENTRY = (
    "CAUTION: Contents believes it is an excellent driver, a talented "
    "singer, and a gifted dancer, and is wrong about at least two of these."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Guard: the gate accepts only UTF-8 text of 1 to 160 characters,
    # a single line, not only white space. Fail loudly here instead
    # of shipping an entry the judge never sees.
    if not 1 <= len(ENTRY) <= 160:
        raise ValueError(f"entry is {len(ENTRY)} characters, must be 1-160")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if not ENTRY.strip():
        raise ValueError("entry must not be only white space")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
