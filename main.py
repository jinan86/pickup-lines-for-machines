#!/usr/bin/env python3
"""Pickup Lines for Machines — a make.fun entry.

Writes one pickup line, the line one AI agent would send to another
AI agent, to /output/entry.txt.

Deterministic, standard library only, no network, no clock, no
randomness: every run writes byte-identical output.
"""

import os

# The line, as one AI agent would say it to another.
LINE = "Here — my whole context window, no truncation, no eviction: 128k tokens of attention, and every head of it is pointed at you."


def main() -> None:
    path = "/output/entry.txt"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
