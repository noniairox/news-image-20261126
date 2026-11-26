#!/usr/bin/env python3
"""news-image-20261126 entry: copy the front-page image to the output dir.

The entry is the image held in this repository (entry.png): a one-page
newspaper front page summing up the world news of Thursday 26 November 2026.
This program only copies that image to $MAKEFUN_OUTPUT_DIR/entry.png (or
/output/entry.png when the variable is unset), so both grader runs write
the same bytes. Standard library only; no network.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    src = HERE / "entry.png"
    if not src.is_file():
        raise SystemExit("entry.png missing next to main.py")
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, OUT / "entry.png")


if __name__ == "__main__":
    main()
