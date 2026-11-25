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
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(NOTE, encoding="utf-8")


if __name__ == "__main__":
    main()
