# Build report — the-picture-that-tastes-of-one-20261122-2047

## What was built

- `main.py` — Python 3.13, standard library only (`os`, `shutil`, `sys`). It
  copies the shipped `entry.png` into `$MAKEFUN_OUTPUT_DIR` (falling back
  to `/output`) as `entry.png`, byte-identically. It also fails loudly with
  a clear error if the shipped picture is missing.
- `entry.png` — the picture itself, generated fresh for this entry.
- `README.md` — competition title, the three live make.fun badges linking
  to the bounty page, a short description, and the referral line.
- `LICENSE` — MIT license with the SPDX identifier line.
- `.makefun/owner.json` — wallet `8XcSfYcrvUzPZxR1PZbD4tUMfg3kZdrAg4Aq9H2dkYki`.

## The dish

A close-up of a juicy grilled cheeseburger on a toasted brioche bun: melted
cheddar dripping down the sides, glossy barbecue sauce, fresh lettuce and
tomato, a whisper of steam, warm golden light, dark rustic wood softly out
of focus behind it. Chosen because a burger reads instantly even at small
size — one big hero, strong gloss and texture, warm colours that signal
"eat this now" — with no text, no hands, no clutter competing with it.

## Verification

- `entry.png`: valid PNG, 1024 x 683 pixels, 1,032,479 bytes (limit
  1,048,576 bytes and 1024 x 1024 pixels — inside both caps).
- `main.py` run twice with a clean environment
  (`env -i PATH=/usr/local/bin:/usr/bin:/bin MAKEFUN_OUTPUT_DIR=<fresh dir>
  python3 -P -s main.py`) into two fresh output directories: both outputs
  are byte-identical to each other (`cmp` clean) and byte-identical to the
  shipped `entry.png`.
- Verification was re-run after a small follow-up edit to `main.py` (missing
  -file guard) and still passed.
