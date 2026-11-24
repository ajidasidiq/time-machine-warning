"""Writes one warning label for a time machine to /output/entry.txt.

The label is embedded in the program: the sandbox has no network,
so the text must be carried in the code itself.

The joke: the label warns the traveller never to meet their past self,
and the punchline lands in the last few words -- the previous passenger
who broke the rule is now his own grandfather. A real hazard of time
travel (the grandfather paradox) told with a straight face, like a
genuine safety notice.
"""

import os

LABEL = (
    "WARNING: Do not meet yourself in the past. "
    "The last passenger who did is now his own grandfather."
)


def main() -> None:
    # The gate rejects anything outside 1-120 characters, anything
    # whitespace-only, or anything that is not a single line of text,
    # so validate before writing instead of silently emitting an
    # invalid entry.
    if not 1 <= len(LABEL) <= 120 or not LABEL.strip():
        raise SystemExit(f"entry text invalid: {len(LABEL)} characters")
    if "\n" in LABEL or "\r" in LABEL:
        raise SystemExit("entry text invalid: label must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LABEL)
    print(f"wrote {len(LABEL)}-character label to /output/entry.txt")


if __name__ == "__main__":
    main()
