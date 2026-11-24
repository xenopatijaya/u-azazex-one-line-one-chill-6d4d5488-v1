"""One Line, One Chill — make.fun entry.

Writes one line of horror (130 characters) to /output/entry.txt: a single
sentence that has to frighten a reader in one breath.

The scare: adoption papers say the son is an only child — a cold, official
fact — and then the attic photographs contradict it with a boy who has the
narrator's own face. Three beats, each one tightening the last: the papers
deny a sibling, the photographs prove a boy exists, the face proves the
boy is connected to the narrator himself. Nothing is explained — who is
the boy, why does he have my face, how long has he been in the attic —
so the dread outlasts the line. No mirror, no doll, no basement, no gore:
one concrete, domestic image (papers, photographs, a face) and the last
word lands the blow.

Python standard library only; no network, no input files.
"""

import os

LINE = (
    "The adoption papers said my son was an only child, so I don't know "
    "who the boy in the attic photographs is, or why he has my face."
)


def main() -> None:
    text = LINE.strip()
    assert "\n" not in text, "line must be a single line"
    # Exactly one sentence: one terminal period, and no other
    # sentence-ending punctuation anywhere in the line, so the judge
    # reads it as a single breath, not a paragraph in disguise.
    assert text.endswith("."), "line must end with a period"
    assert text.count(".") == 1, "line must contain exactly one period"
    assert "!" not in text and "?" not in text, \
        "line must not contain other sentence-ending punctuation"
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    # Verify the file holds exactly the line, byte for byte.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        assert f.read() == text, "entry.txt does not match the line"
    print(f"{text} ({len(text)} chars)")


if __name__ == "__main__":
    main()
