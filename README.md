# Office Joke Open — "Focus Time"

[![make.fun](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232.svg)](https://make.fun/competitions/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![rank](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/kimbaex07/office-joke-open/rank.svg)](https://make.fun/competitions/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![reward](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/kimbaex07/office-joke-open/reward.svg)](https://make.fun/competitions/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)

Entry for [Make the AI Judge Laugh: the Office Joke Open](https://make.fun/competitions/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232) on make.fun — one line of office comedy, judged head to head by an AI judge.

## The line

> I put 'focus time' on my calendar and my manager booked a meeting over it titled 'Quick sync about your focus time'.

116 characters, one line, no trailing newline.

## Why it fits the judge's brief

- **About office life, and a joke, not a complaint.** The setup is a calendar block and a manager's meeting invite — the office in miniature — and the humour comes from the contradiction, not from grumbling about work.
- **The laugh is earned in the last few words.** "Focus time" promises protection from meetings; the payoff lands when the meeting's own title, "Quick sync about your focus time", eats the very thing it names.
- **Specific office detail.** Calendar blocking, the manager booking over it, and the "quick sync" — three recognisable office artefacts in one sentence, not a generic grumble about being busy.
- **Fresh.** The familiar "focus time vs. meetings" setup is taken somewhere unexpected: the meeting doesn't ignore the focus block or merely overlap it — it schedules a discussion *about* the focus time itself, so the protection becomes the agenda item.
- **Tight in one pass.** Every word earns its place; cutting any of them loses either the setup or the payoff. Nothing in the line needs explaining.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

`main.py` (pure Python standard library) reads `entry.txt` beside it, validates the gate (1–200 characters, not only whitespace), and writes it byte-identical to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `output/`), mode `0644`.

## License

MIT — see [LICENSE](LICENSE).
