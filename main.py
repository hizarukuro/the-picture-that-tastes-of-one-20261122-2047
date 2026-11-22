#!/usr/bin/env python3
"""Entry program for the-picture-that-tastes-of-one-20261122-2047.

The picture itself ships in the repo as entry.png, next to this file.
All this program does is place an exact copy of that picture into the
output directory the harness asks for, so the judge sees the very same
bytes we shipped. Nothing is generated or transformed at run time.
"""

import os
import shutil
import sys

# Name of the picture shipped alongside this program.
SOURCE_NAME = "entry.png"

# Name the picture must have in the output directory.
OUTPUT_NAME = "entry.png"


def main() -> int:
    # Where the harness wants the picture: the env var wins, and
    # /output is the documented fallback when it is not set.
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

    # The shipped picture lives right next to this file.
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)

    # Fail loudly instead of silently producing no picture if the
    # shipped image is missing from the repo checkout.
    if not os.path.isfile(source):
        print(f"error: shipped picture not found: {source}", file=sys.stderr)
        return 1

    # Create the output directory if it is not there yet.
    os.makedirs(output_dir, exist_ok=True)

    destination = os.path.join(output_dir, OUTPUT_NAME)

    # copyfile copies the raw bytes, so the output is identical to the
    # shipped file, byte for byte.
    shutil.copyfile(source, destination)

    return 0


if __name__ == "__main__":
    sys.exit(main())
