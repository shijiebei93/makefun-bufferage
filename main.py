"""Bufferage — entry for the make.fun Invent a Word We Need bounty.

Writes the coined word and its one-line definition to entry.txt.
Deterministic, no network, no randomness.
"""

import os
from pathlib import Path

ENTRY = "Bufferage — the quiet rage of watching a video freeze on the best part."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {len(ENTRY)} characters to {output_path}")


if __name__ == "__main__":
    main()
