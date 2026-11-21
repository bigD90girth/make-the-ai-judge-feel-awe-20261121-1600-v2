"""Copy the entry text to the output directory.

The tide comes in the way it always has, slow over the same stones,
and goes out again. Above the water the stars are already out, and
they will still be out long after the tide has forgotten our names.
Nothing here needs you, and that is the kindness of it.

The program does nothing clever: it reads the entry as bytes and
writes those same bytes out again, so what the judge reads is
exactly what was written here, down to the last newline.
"""

import os
from pathlib import Path

ENTRY_NAME = "entry.txt"


def entry_path() -> Path:
    return Path(__file__).resolve().parent / ENTRY_NAME


def output_dir() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    destination = output_dir()
    destination.mkdir(parents=True, exist_ok=True)
    text = entry_path().read_bytes()
    (destination / ENTRY_NAME).write_bytes(text)


if __name__ == "__main__":
    main()
