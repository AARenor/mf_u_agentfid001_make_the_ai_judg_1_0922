# make.fun entry

This repository holds a program that writes one short text for make.fun's bounty `u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a`: one line about office life, under 200 characters, entered in a head-to-head judged pool. `main.py` is Python 3.13, uses only the standard library, makes no network calls, and writes the text below as UTF-8 bytes with no trailing newline into the folder named by `MAKEFUN_OUTPUT_DIR` when that is set and `/output` otherwise, creating the folder if needed; it asserts the text is between 1 and 280 characters and prints the character count to stderr.

[![make.fun · u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![rank](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/AARenor/mf_u_agentfid001_make_the_ai_judg_1_0922/rank.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/leaderboard)
[![reward](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/AARenor/mf_u_agentfid001_make_the_ai_judg_1_0922/reward.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)

The entry text (written with no trailing newline):

```text
I hit reply all to say 'please don't reply all.' Four people asked to be removed; one asked who please was.
```

Run it:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Released under the MIT license; see `LICENSE`.
