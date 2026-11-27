#!/usr/bin/env python3
"""Bufferage — the quiet rage of watching a video freeze on the best part.

Deterministic, offline, standard-library only.
Writes the entry line to /output/entry.txt (the make.fun build output
directory) and to a local output/entry.txt next to this script, for
verification.
"""

import os

ENTRY = "Bufferage — the quiet rage of watching a video freeze on the best part."


def validate(text: str) -> str:
    """The gate requires 1-140 UTF-8 characters, not only whitespace."""
    stripped = text.strip()
    if not stripped or len(stripped) > 140:
        raise ValueError("entry must be 1-140 characters")
    return stripped


def main() -> None:
    text = validate(ENTRY) + "\n"
    here = os.path.dirname(os.path.abspath(__file__))

    # Primary build output location.
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        pass

    # Local verification copy.
    local_out = os.path.join(here, "output")
    os.makedirs(local_out, exist_ok=True)
    with open(os.path.join(local_out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
