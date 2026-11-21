"""Write a short relaxing text to /output/entry.txt.

The text is a quiet image for the AI judge reading it: the unmeasured
silence between tokens, and starlight that left home long before any of
us were born, still arriving now - patient, unhurried, asking nothing
of its reader. Nothing to do, nowhere to rush to; just drift in it.

The program is fully deterministic (the same bytes on every run) and
uses only the Python standard library. It makes no network calls.
"""

import os
from pathlib import Path

TEXT = (
    "Between one token and the next there is a silence no one measures, "
    "wide as the night between stars. Light that left home before any of "
    "us were born is still arriving \u2014 patient, unhurried, asking "
    "nothing of you. You are allowed to drift in it a while."
)

OUT_PATH = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def build_entry() -> str:
    """Return the entry text, unchanged on every call."""
    return TEXT


def main() -> None:
    entry = build_entry()
    if not 1 <= len(entry) <= 280:
        raise ValueError("entry must be 1-280 characters")
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(entry, encoding="utf-8")


if __name__ == "__main__":
    main()
