#!/usr/bin/env python3
"""the-picture-that-tastes-of-one-20261122-2047.

Copies the shipped entry.png (which sits next to this file) into the
output directory named by MAKEFUN_OUTPUT_DIR (falling back to /output),
writing it there as entry.png, byte-identical.

Standard library only.
"""

import os
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")

    # Fail loudly (instead of a bare traceback) if the shipped image is
    # missing, so a broken bundle is obvious before anything is written.
    if not os.path.isfile(source):
        print("error: entry.png not found next to main.py", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    destination = os.path.join(output_dir, "entry.png")

    with open(source, "rb") as src:
        data = src.read()
    with open(destination, "wb") as dst:
        dst.write(data)

    return 0


if __name__ == "__main__":
    sys.exit(main())
