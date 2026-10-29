# Fallout 4 on macOS, modded

A tested setup for running a modded Fallout 4 on an Apple Silicon Mac, and a catalogue of about 1,000 mods evaluated for runtime 1.11.240. The macOS Steam client launches the Windows game through Not Proton and CrossOver, Mod Organizer 2 runs inside the game's Wine prefix, and F4SE loads. Every setup step was run on a real machine.

**Status: work in progress.** The base works (game, MO2, F4SE up to the main menu). The catalogue is researched; mods are being installed and tested in batches, and v1.0.0 will mark a full tested playthrough.

## Choose your mods

| | |
| --- | --- |
| **[Interactive catalogue](https://morgankryze.github.io/fallout4-macos-modding/site/)** | Filter by faction, tier and performance cost, build a list that adds its own requirements and patches, see conflicts, export it |
| [Catalogue pages](docs/catalog/README.md) | The same data as readable pages, one per area: Brotherhood, Minutemen, Institute, Railroad, raiders, settlements, DLC, quests, weapons, companions… |
| [Reference playthrough](docs/reference-playthrough.md) | The list we play, every trade-off behind it, and habits for playing it well |
| [Install plan](docs/install-plan.md) | That list in eight tested batches, with the target load order |
| [data/mods.csv](data/mods.csv) | The raw data, documented in [data/README.md](data/README.md). AI assistants: start from [llms.txt](llms.txt) |

Each mod is rated on what decides whether it belongs in a stable list: support for 1.11.240, F4SE DLLs, effect on precombines (PRP), performance cost, compatibility with Lunar Fallout Overhaul and Sim Settlements 2, faction-ending locks, requirements, patches and conflicts, with sources.

## What works so far

| Piece | Version | State |
| --- | --- | --- |
| Fallout 4 (Steam, GOTY) | 1.11.240 | Runs, updates locked |
| CrossOver + Not Proton | 26.3 + 1.2.2 | Runs the game from the macOS Steam client |
| Mod Organizer 2 | 2.5.2 | Runs in the game's prefix |
| F4SE | 0.7.9 | Loads, main menu reached |

Reference machine: Apple M3, 16 GB, macOS 26.5.1.

## Set up

| File | Contents |
| --- | --- |
| [docs/setup.md](docs/setup.md) | Step-by-step setup, paths and launch options |
| [docs/troubleshooting.md](docs/troubleshooting.md) | Problems met, their causes and fixes |
| [scripts/fo4-backup.sh](scripts/fo4-backup.sh) | APFS-clone backups of the game, MO2 and profiles; Steam update lock |

## Requirements

- An Apple Silicon Mac
- [CrossOver](https://www.codeweavers.com/crossover) 26.3, licensed or on trial
- [Not Proton](https://www.ithinkdiff.com/notproton-steam-play-macos/) 1.2.2
- Fallout 4 on Steam
- A Nexus Mods account, for F4SE and the mods

## Maintaining the catalogue

Edit `data/mods.csv`, then run `python3 scripts/nexus_sync.py` (refreshes Nexus metadata) and `python3 scripts/build_catalog.py` (regenerates the pages). Both use the Python standard library only.

## License

[MIT](LICENSE). Mod names, images and descriptions shown by the catalogue belong to their authors on Nexus Mods.
