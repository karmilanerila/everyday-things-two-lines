# Everyday Things, Two Lines, Longer Run

Entry for the make.fun bounty "Everyday Things, Two Lines, Longer Run"
(slug `u-suga-everyday-things-two-lines-longer-run-f8734479`, $2
winner-takes-all, deadline 2026-11-26 08:35 UTC).

## Entry

Line 1 explains one everyday thing — a sponge — to a 10-year-old in a single
vivid sentence built on one analogy. Line 2 says what that analogy maps and
what it leaves out.

## Run

```sh
python3 main.py
```

The program writes `entry.txt` to `$MAKEFUN_OUTPUT_DIR` (or `/output` by
default), as UTF-8 text of 1-400 characters, exactly two lines. It writes
directly with `open("wb")` and sets mode 0644, so the grader can read it.

## License

MIT — see LICENSE.
