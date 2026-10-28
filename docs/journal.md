# Build journal

Dated record of everything done on the reference machine: what worked, what failed, what was worked around and what is still unverified. [setup.md](setup.md) is the clean procedure; this file is the raw history behind it, newest day last.

Marks: **OK** works · **FAIL** failed · **FIXED** problem worked around · **UNVERIFIED** not tested yet

## 2026-10-28

### Windows layer: Not Proton instead of a CrossOver bottle

- **OK** CrossOver 26.3 (26.3.0.39832) installed in `/Applications`.
- **OK** Not Proton 1.2.2 installed. It hooks the macOS Steam client and adds the "CrossOver 26.3" compatibility tool (`notproton-26.3`, running under Rosetta), with one Wine prefix per game.
- **OK** Test game (Moving Out, app 996770): clean launch and exit, `session health: healthy`.
- The original plan used a CrossOver bottle with Windows Steam inside. Not Proton replaces both.
- **UNVERIFIED** Not Proton reports `updatesBlocked=false` for the Steam client. A Steam client update could break its hooks.

### Game install

- **OK** 34.4 GB downloaded, 38.3 GB on disk.
- **OK** Automatic updates set to "Wait until I launch the game" (`AutoUpdateBehavior=1` in the manifest).
- **OK** Steam Cloud off for Fallout 4.
- **OK** First launch through Steam's Play button. Only `Fallout4Launcher.exe` ran (45 s), which was enough to create prefix 377160 with `Fallout4.ini` and `Fallout4Prefs.ini`.
- **OK** `Fallout4.exe` reports `FileVersion 1.11.240.0`, Steam build 24564252.
- **OK** Plugins: `Fallout4.esm`, the 6 DLC `.esm` files and 8 Creation Club `.esl` files, 15 in total.

### Backup and update lock

- **OK** `fo4-backup.sh game` cloned the clean game. Free space went from 226 GB to 188 GB, which matches the download alone: the APFS clone itself costs almost nothing.
- **OK** `fo4-backup.sh lock`: the manifest now carries the `uchg` flag.
- **UNVERIFIED** Whether the lock holds against the next Bethesda patch. No patch has shipped since.

### Mod Organizer 2

- **OK** MO2 2.5.2 from the official GitHub release, extracted to `~/Games/MO2` with `portable.txt`. The release publishes no checksum, so the archive could not be verified (sha256 `e6376efd87fd5ddd95aee959405e8f067afa526ea6c2c0c5aa03c5108bf4a815`).
- **OK** Added to Steam as a non-Steam game, with CrossOver 26.3 as compatibility tool.
- **FIXED** The shortcut got its own prefix. Forcing `STEAM_COMPAT_DATA_PATH` to `compatdata/377160` in the launch options moved MO2 into the game's prefix, confirmed in `notproton-run.log`.
- **FAIL** MO2 then rejected the game at `S:\steamapps\common\Fallout 4`: Not Proton had removed drive `S:` because MO2 is not inside a Steam library.
- **FIXED** Adding `STEAM_COMPAT_INSTALL_PATH` and `STEAM_COMPAT_LIBRARY_PATHS` to the launch options brought `S:` back. MO2 now manages Fallout 4 (Steam variant, app 377160) with the 15 vanilla plugins.
- **UNVERIFIED** Whether `SteamAppId=377160` is needed. It was added as a precaution and never tested without.

### F4SE 0.7.9

- f4se.silverlock.org no longer hosts 0.7.9 and links to Nexus, where it was downloaded.
- **OK** Copied `f4se_1_11_240.dll`, `f4se_loader.exe` and `Data/Scripts` (58 files) into the game folder. `Data/Scripts` did not exist before, so nothing was overwritten.
- **FIXED** MO2 had no F4SE entry, even after a refresh. Added by hand with "Start in" set to the game folder.
- **OK** Launched through MO2 → F4SE: the main menu shows `v (F4SE 0.7.9) 1.11.240.0.0`. `f4se.log` reaches `init complete` and `f4se_loader.log` ends with `launching`.

### MO2 profile

- **OK** Profile created with "Default Game INI Settings" unchecked; local INI files, local saves and automatic archive invalidation turned on.
- **OK** Added `bDisableAllGore=1` and `bBackgroundMouse=1` to the profile's `fallout4custom.ini`.
- **UNVERIFIED** Neither INI change has been tested in game yet.
- **FIXED** The first profile backup failed: the script still pointed to the MO2 path from the bottle-based plan. Fixed to `~/Games/MO2`, then the empty profile was backed up.

### Changes to the mod plan

- Weapon Debris Crash Fix dropped: it fixes a crash specific to Nvidia cards, which a Mac does not have.
- BethINI not used so far; the two INI changes were made by hand.

## Status

| Step | State |
| --- | --- |
| Game on 1.11.240, updates locked, clean clone | Done |
| MO2 in the game prefix, with `S:` | Done |
| F4SE through MO2 up to the main menu | Done |
| MO2 profile, backed up | Done |
| Batch 1: Address Library, UFO4P, Addictol, High FPS Physics Fix, PRP, MCM | Waiting for downloads |
| Graphics backend (D3DMetal or DXVK), frame rate | Not measured |
