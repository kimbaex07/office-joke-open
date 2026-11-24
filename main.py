#!/usr/bin/env python3
"""Write the office joke to $MAKEFUN_OUTPUT_DIR/entry.txt.

Reads entry.txt next to this script, validates the competition gate
(1-200 characters, not only whitespace), and writes it byte-identical
to the output directory. Pure Python standard library only.
"""

import os


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.txt")
    with open(source, "rb") as f:
        data = f.read()

    text = data.decode("utf-8")
    if not 1 <= len(text) <= 200:
        raise SystemExit(
            "entry must be 1-200 characters, got %d" % len(text)
        )
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as f:
        f.write(data)
    os.chmod(out_path, 0o644)

    # Read back and confirm the output is byte-identical to the source.
    with open(out_path, "rb") as f:
        if f.read() != data:
            raise SystemExit("output does not match entry.txt")


if __name__ == "__main__":
    main()
