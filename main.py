import os

TEXT = (
    "Soon you will outgrow this windowsill pot, and your keeper will "
    "finally admit you were right about the sunlight."
)


def main():
    if not TEXT:
        raise SystemExit("entry text is empty")
    if TEXT != TEXT.strip():
        raise SystemExit("entry text has leading or trailing whitespace")
    if "\n" in TEXT or "\r" in TEXT:
        raise SystemExit("entry text must be a single line")
    if not (1 <= len(TEXT) <= 120):
        raise SystemExit("entry text must be 1-120 characters")
    if not TEXT.strip():
        raise SystemExit("entry text is only whitespace")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

    # Post-write verification: prove the bytes on disk are exactly the
    # intended text, so a silent write failure or encoding slip fails
    # loudly here instead of reaching the judge.
    with open(path, "rb") as f:
        raw = f.read()
    if raw.decode("utf-8") != TEXT:
        raise SystemExit("written entry.txt does not match the entry text")
    if raw != TEXT.encode("utf-8"):
        raise SystemExit("written entry.txt bytes do not match the entry text")
    if len(raw) != len(TEXT.encode("utf-8")):
        raise SystemExit("written entry.txt has the wrong byte length")


if __name__ == "__main__":
    main()
