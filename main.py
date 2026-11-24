"""The Funniest Out-of-Office — one-line entry.

Writes exactly one line of text to /output/entry.txt (the comp's output
contract: UTF-8, 1 to 140 characters, one line, nothing else) and prints
the same line to stdout. Fixed string literal: no randomness, no time,
no network, no input — byte-identical on every run.
"""

import os

ENTRY = (
    "Thank you for applying to reach me. "
    "We received 287 emails this week; "
    "yours did not make the shortlist. "
    "Interviews resume Monday."
)


def main() -> None:
    # No trailing newline: the file is exactly the 129-character line,
    # so the gate counts 129 whether or not it strips a newline.
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, cap is 140"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
