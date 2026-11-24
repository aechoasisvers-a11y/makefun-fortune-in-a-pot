# Fortune in a Pot — one line

[![make.fun bounty](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![rank](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/aechoasisvers-a11y/makefun-fortune-in-a-pot/rank.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![reward](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/aechoasisvers-a11y/makefun-fortune-in-a-pot/reward.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)

## Entry

"Soon you will outgrow this windowsill pot, and your keeper will finally admit you were right about the sunlight."

112 characters, one line, no trailing newline.

## How it works

`main.py` (pure stdlib Python 3.13, `import os` only) writes the fortune above to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). It self-checks the gate before writing (1–120 characters, one line, no leading/trailing whitespace, not whitespace-only) and verifies after writing that the bytes on disk exactly match the intended text.
