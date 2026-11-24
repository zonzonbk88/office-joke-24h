#!/usr/bin/env python3
"""One-line office joke entry.

Writes a single-line joke about office life (<= 200 chars) to
/output/entry.txt (or ./output/entry.txt when run locally).
Standard library only.
"""

import os

JOKE = "This meeting could have been an email, but then nobody would have watched me nod for 45 minutes."


def main() -> None:
    line = JOKE.strip()
    assert 1 <= len(line) <= 200, f"joke length {len(line)} out of gate"
    assert "\n" not in line, "joke must be a single line"
    out_dir = "/output" if os.path.isdir("/output") else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "output"
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
