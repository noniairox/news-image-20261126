# news-image-20261126

[![news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/c/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/noniairox/news-image-20261126/rank.svg)](https://make.fun/c/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/noniairox/news-image-20261126/reward.svg)](https://make.fun/c/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

One image that sums up the world news of **Thursday, 26 November 2026** — a
neat broadsheet front page, *The World Today*, built from the day's real
reporting.

## The front page

The lead story is Washington's proposal of new tariffs on 14 trading partners,
with China facing duties of up to 20%. The main picture is the storm that
grounded New York: the 100th Macy's Thanksgiving Day Parade postponed to
Saturday, the first weather delay in its century of history, as a nor'easter
battered the US East Coast and left 800,000 people without power.

Inside, 28 more stories in three columns:

- **World** — EU leaders debate a €45bn Ukraine loan and the 2028–2034 budget;
  Kim Jong Un orders wider tactical nuclear deployment; Trump and NATO chief
  Mark Rutte warn Russia not to widen the Ukraine war; Russian missiles hit a
  Kyiv shopping centre as 113 drones fly overnight; Ukraine strikes two
  refineries in Russia's Samara region; Houthis claim a strike on Saudi
  Arabia's Ras Tanura refinery and mines hit ships in the Strait of Hormuz;
  Israeli strikes kill nine in Gaza; judges urge dropping the bribery charge
  in Netanyahu's trial; Solomon Islands names Australia its main security
  partner; Russian jets enter South Korea's air defence zone; a Pakistani
  astronaut boards China's Tiangong station; Germany foils a synagogue attack
  plot; an Iranian drone kills two Italians in Kuwait; Ebola cases top
  12,000 in eastern Congo.
- **Disasters** — a Cairo fuel tanker blast kills 31; a gold mine flood in
  Bogor, Indonesia kills 13 with 13 missing; a diesel tanker capsizes off
  Ibiza; a Bangkok refinery blast injures nine.
- **United States** — a judge blocks the FCC's early review of eight ABC
  licences; a second judge blocks the birthright citizenship order; US GDP
  grew 3.4% in the third quarter.
- **Business** — Nvidia pauses shipments to Southeast Asia and S&P puts its
  rating on downgrade watch; SpaceX is cleared for a million satellites;
  UniCredit seeks the Commerzbank chair role; Babcock signs a record
  $11.4bn submarine deal; gold slumps to a 15-month low; Altria eyes
  Imperial Brands.
- **Sport** — Champions League: Liverpool 3–0 Club Brugge, Barcelona 4–1
  Sabah, Lille stun Bayern 2–1, Manchester United held 2–2 at Sporting.

## How it works

`main.py` (Python 3.13, standard library only) copies `entry.png` — the
front page, drawn for this entry — to `$MAKEFUN_OUTPUT_DIR/entry.png`
(or `/output/entry.png`). The image is a 1024×1024 PNG under 1 MiB. The
program runs with no network and writes the same bytes on every run.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
