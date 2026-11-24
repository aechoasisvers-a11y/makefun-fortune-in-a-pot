"""Write the one-line entry to /output/entry.txt.

Pure stdlib Python 3.13. Deterministic: same bytes every run.
"""

import os

ENTRY_TEXT = (
    "Soon you will outgrow this windowsill pot, and your keeper will "
    "finally admit you were right about the sunlight."
)


def main() -> None:
    # Self-check: the text must be exactly the intended line, one line,
    # non-blank, and inside the kit's 120 character gate.
    assert ENTRY_TEXT == ENTRY_TEXT.strip(), "entry has stray whitespace"
    assert "\n" not in ENTRY_TEXT, "entry must be a single line"
    assert 1 <= len(ENTRY_TEXT) <= 120, "entry outside gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    with open(path, "r", encoding="utf-8", newline="") as f:
        assert f.read() == ENTRY_TEXT, "written output differs from text"


if __name__ == "__main__":
    main()
