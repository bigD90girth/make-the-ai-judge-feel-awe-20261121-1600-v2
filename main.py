"""Copy the entry text to the output directory.

The text is the entry: a short piece written to leave its reader
calmer, unhurried, at ease -- the tide coming in the way it always
has over the same stones, the stars already out above the water,
still out long after the tide has forgotten our names. Nothing here
needs the reader, and that is the kindness of it. The program only
moves its bytes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    # The entry is exactly 258 characters; the copy is byte for byte.
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.txt", OUT / "entry.txt")


if __name__ == "__main__":
    main()
