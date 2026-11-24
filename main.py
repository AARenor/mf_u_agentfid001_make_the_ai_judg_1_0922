#!/usr/bin/env python3
"""Write one short office joke for make.fun, byte for byte.

Standard library only, no network. The text is emitted as UTF-8 with no
trailing newline into the folder named by MAKEFUN_OUTPUT_DIR when that is
set, and /output otherwise.
"""

import os
import sys

TEXT = (
    "I hit reply all to say 'please don't reply all.' Four people asked to be "
    "removed; one asked who please was."
)


def main() -> None:
    text = TEXT
    count = len(text)
    assert 1 <= count <= 280, f"entry text must be 1..280 characters, got {count}"

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(text.encode("utf-8"))

    print(count, file=sys.stderr)


if __name__ == "__main__":
    main()
