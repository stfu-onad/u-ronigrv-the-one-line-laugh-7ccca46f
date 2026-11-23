"""The One-Line Laugh — entry for make.fun bounty
u-ronigrv-the-one-line-laugh-7ccca46f.

Writes a single funny line (one sentence, <= 200 characters) to
/output/entry.txt. The line: a setup about buying a standing desk to be
healthier, with the twist landing at the very end — the buyer now just
sits all day on a taller chair. Everyday truth: buying the gear never
changed the habit.
"""

import os

LINE = "I bought a standing desk to be healthier, so now I sit all day on a taller chair."


def main() -> None:
    # Self-check the gate the sealed scorer enforces: 1-200 chars, one line.
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars"
    assert "\n" not in line, "line must be a single line"

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
