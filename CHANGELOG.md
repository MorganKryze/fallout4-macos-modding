# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- Setup guide: Not Proton and CrossOver, game install, update lock, Mod Organizer 2 in the game prefix, F4SE, MO2 profile.
- Troubleshooting notes for the prefix, the `S:` drive, the missing F4SE entry, manual-download warnings and archives with a `Data` root.
- Setup step for installing manually downloaded mods.
- `fo4-backup.sh`: APFS-clone backups and Steam update lock.
- Mod catalogue: about 1,000 mods researched for runtime 1.11.240 in `data/mods.csv`, with Nexus metadata in `data/nexus.json`.
- `scripts/nexus_sync.py` and `scripts/build_catalog.py` to refresh the metadata and generate the catalogue pages.
- Catalogue pages in `docs/catalog/`, one per area, with exclusive choices and suggested stacks.
- Interactive catalogue in `site/`: filters, list builder with requirements, patches, conflicts and exports.
- Reference playthrough page with the trade-offs behind our list and playing habits.
- Install plan: the reference list in eight tested batches, with the target load order and the FO4Edit checks.
- `llms.txt` describing the data for AI assistants.

### Changed

- Catalogue site redesigned as an inspection record: a clearer first screen, Lunar, Sim Settlements 2 and "in your list" filters, a section index, cards that say what adding a mod brings, a list form with a hatched gauge for uncounted plugins, undo for presets, a mobile list sheet, sortable table, and keyboard focus kept on every action.

### Fixed

- The Pages root now redirects to the catalogue instead of returning 404.
