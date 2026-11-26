#!/usr/bin/env python3
"""What the Elevator Would Say — entry writer.

Writes the elevator's one-liner to entry.txt in MAKEFUN_OUTPUT_DIR
(default /output), with the gate (1-120 chars, single line, non-whitespace)
asserted in-program.
"""

import os
import stat

TEXT = "Floor 12, doors opening: I have carried 7,254 people up here and not one of them asked how I was getting back down."
# Title: "How I Get Back Down" — the elevator's own doors/floors vocabulary,
# a precise fresh count (7,254), and the self-pity punchline in the final clause.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Gate: 1-120 chars, single line, not only whitespace.
    assert 1 <= len(TEXT) <= 120, f"entry is {len(TEXT)} chars"
    assert "\n" not in TEXT, "entry must be a single line"
    assert TEXT.strip(), "entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
