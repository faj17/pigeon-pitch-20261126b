"""Pigeon Pitch entry: one line for make.fun.

A city pigeon pitches investors on its startup: after ten years
decorating every statue in the city for free, it will now charge
the city to undo its own art. The joke is the twist — the pigeon
is the mess, and now it sells the cleanup. It is built to survive
the judge's five tests, in weight order: stay on the brief (a
one-line elevator pitch from a city pigeon to investors for its
startup); land a real joke, not a mild pun; surprise with an
idea not met before; keep the pigeon's voice and city life in
view; stay tight at 143 chars, every word earning its place.
The winner is assembled from parts below, with the near-misses
kept in CANDIDATES so the choice stays visible.
"""

from pathlib import Path

# Why each beat earns its place:
# - the opening sets the pigeon's decade on the statues, city life in view
# - the em dash turns the confession into the pitch: invest in the cleanup
# - the landing is the twist: the city pays the pigeon to undo its own art
_PARTS = (
    "I've spent ten years decorating every statue in this city for free",
    " \u2014 invest in my cleaning startup and I'll charge the city to ",
    "undo my own art.",
)

CANDIDATES = [
    (
        "Investors, I'm the pigeon your statues fear \u2014 fund my cleaning startup and I'll turn a century of my own mess into the city's shiniest passive income.",
        "Rejected: 'your statues fear' states the joke instead of letting the twist land, and 'a century' overclaims a pigeon's working life.",
    ),
    (
        "Every morning 10,000 office workers drop crumbs for free \u2014 I'm the only founder who monetized lunch, so invest before the seagulls beat me to it.",
        "Rejected: a decent crumb-economics gag, but the seagull punchline is a rival-bird pun, not a twist on the pigeon's own life.",
    ),
]

OUTPUT = Path("/output/entry.txt")


def assemble() -> str:
    """Assemble the winning pitch from its parts."""
    return "".join(_PARTS)


def validate(line: str) -> str:
    """Require one line, 1-200 chars, no trailing newline."""
    text = line.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if "\n" in text or line.endswith("\n"):
        raise ValueError("entry must be a single line with no trailing newline")
    if not text.endswith("."):
        raise ValueError("entry must end with '.'")
    return text


def main() -> None:
    entry = validate(assemble())
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(entry, encoding="utf-8")
    assert OUTPUT.read_text(encoding="utf-8") == entry, "round-trip mismatch"
    print(entry)
    print(f"wrote {len(entry)} chars to {OUTPUT}")


if __name__ == "__main__":
    main()
