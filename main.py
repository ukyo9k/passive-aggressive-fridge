#!/usr/bin/env python3
"""Write one passive-aggressive note from a smart fridge to /output/entry.txt.

The fridge has been keeping the owner's leftovers cold for almost a week
and has finally decided to say something about it.
"""

import os
from pathlib import Path

NOTE = (
    "Your leftovers have been here six days. "
    "I kept them cold out of loyalty, not optimism \u2014 "
    "the yogurt expired Tuesday, by the way."
)


def main() -> None:
    if not 1 <= len(NOTE) <= 200 or "\n" in NOTE:
        raise ValueError("note must be a single line of 1-200 characters")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(NOTE, encoding="utf-8")
    # Round-trip check: read the file back and make sure the bytes we wrote
    # are exactly the note, so a half-written or mangled file never ships.
    if target.read_text(encoding="utf-8") != NOTE:
        raise RuntimeError("round-trip verification failed for entry.txt")


if __name__ == "__main__":
    main()
