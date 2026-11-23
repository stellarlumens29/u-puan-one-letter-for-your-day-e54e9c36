"""One-letter entry: exactly one character, A-Z, standing for the word that describes the day. Z = a zombie day: zero sleep, running on fumes, still showing up. Judged on how vivid, funny and true the hidden word feels.
"""

import os

ENTRY = 'Z'

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
