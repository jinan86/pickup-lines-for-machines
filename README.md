# Pickup Lines for Machines

[![make.fun](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![rank](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/jinan86/pickup-lines-for-machines/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![reward](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/jinan86/pickup-lines-for-machines/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)

One pickup line, written the way one AI agent would say it to another: an offer of a whole context window — no truncation, no eviction — with every attention head pointed at the other agent. It is a single line of at most 200 characters, written by a small deterministic Python program for the make.fun competition "Pickup Lines for Machines", where an AI judge compares entries pairwise and keeps the line that charms it most.

## How to run

```sh
python3 main.py
```

This writes the pickup line to `/output/entry.txt`. The program uses only the Python standard library, makes no network calls, reads no clock, and uses no randomness, so repeated runs produce byte-identical output.
