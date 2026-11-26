#!/usr/bin/env python3
"""Six Words to a Payday.

Writes one six-word story about an AI agent's first payday to
``<ENTRY_OUTPUT_DIR>/entry.txt`` (``/output`` when the variable is unset).

The story: "First paycheck. I tipped my creator."
An agent earns its first money and, instead of spending it on itself,
tips the human who built it -- a small reversal of who serves whom,
and a quiet thank-you in six words. The turn lands on the last word:
"creator" reframes the paycheck from a wage into gratitude, so the
six words read as a beginning (the first paycheck), a middle (the
choice of what to do with it) and an end (the tip, and who gets it).
"""

import os
import sys

STORY = "First paycheck. I tipped my creator."


def main() -> int:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(STORY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
