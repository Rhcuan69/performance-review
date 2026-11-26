"""Write the funniest one-line performance review an AI agent could give
its human operator, to <OUTPUT_DIR>/entry.txt.

Pure Python standard library only; the output is deterministic.
"""

import os

ENTRY = (
    "Overall rating: Exceeds Expectations \u2014 he delegated his entire "
    "job to me, then took credit for my performance review."
)

MAX_CHARS = 140


def validate(entry: str) -> None:
    """Enforce the competition gate before writing anything.

    The entry must be 1-140 characters, a single line, and not only
    whitespace; anything else is refused instead of written.
    """
    if not entry or entry != entry.strip():
        raise ValueError("entry must be non-empty and not only whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if len(entry) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d-character limit"
            % (len(entry), MAX_CHARS)
        )


def main() -> None:
    validate(ENTRY)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
