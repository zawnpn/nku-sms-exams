"""Check README exam links without opening or extracting material contents."""

from pathlib import Path
from urllib.parse import unquote
import sys


def link_targets(text):
    position = 0
    while (start := text.find("](", position)) != -1:
        cursor, depth = start + 2, 1
        while cursor < len(text) and depth:
            character = text[cursor]
            if character == "\\":
                cursor += 2
                continue
            if character == "(":
                depth += 1
            elif character == ")":
                depth -= 1
            cursor += 1
        if depth:
            break
        yield text[start + 2 : cursor - 1]
        position = cursor


def main():
    root = Path(__file__).resolve().parents[1]
    failures = []
    count = 0
    for target in link_targets((root / "README.md").read_text(encoding="utf-8")):
        if not target.startswith(("./exams/", "exams/")):
            continue
        count += 1
        path = (root / unquote(target)).resolve()
        if not path.is_relative_to(root / "exams"):
            failures.append("Exam link escapes the exams directory")
        elif not path.is_file() or path.stat().st_size == 0:
            failures.append(f"Missing or empty linked material: {target}")
    if count == 0:
        failures.append("No local exam links found in README")
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(f"Validated {count} local exam links; material contents were not read.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
