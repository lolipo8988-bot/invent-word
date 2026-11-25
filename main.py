#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Invent a Word We Need — entry writer.

The competition asks for one invented English word with a one-line
definition of at most 140 characters, written to /output/entry.txt.

The coinage is "mutologue" — mute fused with monologue, formed the
way English itself would form it. It names a moment every video-call
regular since 2020 knows in their bones and has never had a word
for: the long, heartfelt speech delivered entirely into a muted
microphone. The definition is built to land in one reading, and it
closes on the moment of discovery everyone recognises at once —
the grid of faces silently pointing at their ears.

Revision note: the first draft stored the entry as one flat string.
This version assembles it from its two lexicographic parts — the
headword and its definition — and checks each part on its own (the
headword must be a single lowercase word that is not the whole
entry; the definition must be a real clause, not a fragment), so a
malformed coinage fails loudly here rather than at the gate. The
entry text itself is unchanged: it was already the tightest wording.

The program is deterministic: it checks the assembled entry against
the gate's contract, writes it with no trailing newline, then reads
the file back and compares, so a run either produces exactly the
intended bytes or fails loudly.
"""

import os
import pathlib

WORD = "mutologue"
DEFINITION = (
    "a long, heartfelt speech given entirely on mute in a video call, "
    "realized only when everyone starts pointing at their ears."
)
ENTRY = f"{WORD}: {DEFINITION}"

MAX_CODE_POINTS = 140
DEFAULT_OUTPUT = pathlib.Path("/output/entry.txt")


def check_coinage(word: str, definition: str) -> None:
    """Raise unless the parts form a plausible dictionary entry."""
    if not word.isalpha() or word != word.lower() or " " in word:
        raise ValueError("headword must be one lowercase word")
    if len(definition) < 20 or not definition.endswith("."):
        raise ValueError("definition must be a full clause ending in a period")


def check(text: str) -> None:
    """Raise unless the text satisfies the gate: 1..140 chars, one line."""
    if not 1 <= len(text) <= MAX_CODE_POINTS:
        raise ValueError(f"entry is {len(text)} code points, need 1..{MAX_CODE_POINTS}")
    if text != text.strip() or not text.strip():
        raise ValueError("entry must be non-blank with no surrounding white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.startswith(WORD + ":"):
        raise ValueError("entry must open with its headword")


def target_path() -> pathlib.Path:
    """MAKEFUN_OUTPUT_DIR redirects the output dir for local test runs."""
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if override:
        return pathlib.Path(override) / "entry.txt"
    return DEFAULT_OUTPUT


def main() -> None:
    check_coinage(WORD, DEFINITION)
    check(ENTRY)
    path = target_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(ENTRY.encode("utf-8"))
    if path.read_bytes() != ENTRY.encode("utf-8"):
        raise SystemExit("read-back mismatch: file bytes differ from the entry")


if __name__ == "__main__":
    main()
