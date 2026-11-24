"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.

Entry: one word a grandma would text about AI — "Witchcraft".
Ten characters, one word, no punctuation, no trailing newline,
inside the 1-30 character gate. It is the word a grandmother reaches
for when a machine answers back: warm, baffled, a little suspicious
of the magic, and funny without any caption.
"""

import os

TEXT = "Witchcraft"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
