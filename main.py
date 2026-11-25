"""Write the competition entry line to /output/entry.txt."""

import os

ENTRY_PARTS = [
    "I set five alarms.",
    "All five snoozed themselves.",
    "I have filed a complaint with the alarms.",
    "They are investigating.",
]

OUTPUT_PATH = "/output/entry.txt"


ENTRY = " ".join(ENTRY_PARTS)


def write_entry(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def main():
    write_entry(OUTPUT_PATH, ENTRY)


if __name__ == "__main__":
    main()
