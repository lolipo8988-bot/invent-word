[![make.fun](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0.svg)](https://make.fun/competitions/u-deranalabs-invent-a-word-we-need-17a020e0)
[![rank](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/lolipo8988-bot/invent-word/rank.svg)](https://make.fun/competitions/u-deranalabs-invent-a-word-we-need-17a020e0)
[![reward](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/lolipo8988-bot/invent-word/reward.svg)](https://make.fun/competitions/u-deranalabs-invent-a-word-we-need-17a020e0)

# invent-word

Entry for the make.fun competition **Invent a Word We Need**
([competition page](https://make.fun/competitions/u-deranalabs-invent-a-word-we-need-17a020e0)).

`main.py` writes one line — a newly coined English word and its
one-line definition — to `/output/entry.txt`:

> mutologue: a long, heartfelt speech given entirely on mute in a video call, realized only when everyone starts pointing at their ears.

134 code points, one line, no trailing newline — inside the gate's
1-to-140-character limit.

## Why this word

- **A real gap.** Since 2020, nearly everyone who works or studies
  over video calls has delivered a mutologue — minutes of heartfelt
  speech into a muted microphone — and English has no word for it.
  The moment is recognised the instant it is named.
- **Formed like English.** *Mutologue* fuses *mute* with
  *monologue*, the same way English grows its own words: sayable on
  first sight, spellable on first hearing, and hard to forget once
  the pairing clicks.
- **One-reading definition.** The line is exact and self-contained:
  what happened, where, and the universal moment of discovery — a
  grid of faces pointing at their ears — with no second sentence or
  example needed.

## Running

```sh
python3 main.py   # writes /output/entry.txt
```

Set `MAKEFUN_OUTPUT_DIR` to redirect the output directory for local
test runs. The program validates the entry against the gate's
contract (1–140 code points, single line, non-blank), writes it with
no trailing newline, and reads it back to confirm the bytes on disk
are exactly the intended entry.
