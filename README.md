# Fallout 4 on macOS, modded

A tested setup for running a modded Fallout 4 on an Apple Silicon Mac: the macOS Steam client launches the Windows game through Not Proton and CrossOver, Mod Organizer 2 runs inside the game's Wine prefix, and F4SE loads on runtime 1.11.240. Every step was run on a real machine and logged, including the ones that failed.

**Status: work in progress.** The base works (game, MO2, F4SE up to the main menu). Mods are being added in batches; the mod list will be published with v1.0.0.

## What works so far

| Piece | Version | State |
| --- | --- | --- |
| Fallout 4 (Steam, GOTY) | 1.11.240 | Runs, updates locked |
| CrossOver + Not Proton | 26.3 + 1.2.2 | Runs the game from the macOS Steam client |
| Mod Organizer 2 | 2.5.2 | Runs in the game's prefix |
| F4SE | 0.7.9 | Loads, main menu reached |

Reference machine: Apple M3, 16 GB, macOS 26.5.1.

## Documentation

| File | Contents |
| --- | --- |
| [docs/setup.md](docs/setup.md) | Step-by-step setup, paths and launch options |
| [docs/troubleshooting.md](docs/troubleshooting.md) | Problems met, their causes and fixes |
| [docs/journal.md](docs/journal.md) | Dated build log: what worked, what failed, what is unverified |
| [scripts/fo4-backup.sh](scripts/fo4-backup.sh) | APFS-clone backups of the game, MO2 and profiles; Steam update lock |

## Requirements

- An Apple Silicon Mac
- [CrossOver](https://www.codeweavers.com/crossover) 26.3, licensed or on trial
- [Not Proton](https://www.ithinkdiff.com/notproton-steam-play-macos/) 1.2.2
- Fallout 4 on Steam
- A Nexus Mods account, for F4SE and the mods

## License

[MIT](LICENSE)
