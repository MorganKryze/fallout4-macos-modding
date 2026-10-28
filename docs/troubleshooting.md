# Troubleshooting

Problems met while building this setup, each with the symptom, the cause and the fix that worked. The setup guide already includes every fix; this page explains why the steps look the way they do.

## MO2 runs in its own prefix

**Symptom.** A non-Steam shortcut gets a prefix of its own (`compatdata/<shortcut id>`), where MO2 sees neither the game nor `My Games`.

**Cause.** Steam assigns one prefix per app ID, and a shortcut has its own ID.

**Fix.** Add `STEAM_COMPAT_DATA_PATH=".../compatdata/377160"` before `%command%` in the shortcut's launch options. Check `compatdata/377160/notproton-run.log`: it must show `STEAM_COMPAT_DATA_PATH=…/compatdata/377160` and the launch of `ModOrganizer.exe`.

## MO2 cannot find the game on S:

**Symptom.** "Cannot open instance 'Portable', the managed game was not found in the INI file". MO2 offers "Fallout 4, S:/steamapps/common/Fallout 4", then rejects it: "the game directory 'S:\steamapps\common\Fallout 4' doesn't exist".

**Cause.** Not Proton's `run` script (`map_game_drive`, `unmap_game_drive`) mounts `S:` only when the program being launched lives inside a Steam library. MO2 lives in `~/Games`, and `STEAM_COMPAT_LIBRARY_PATHS` is empty for shortcuts, so Not Proton removes `S:` from the prefix. The registry still points to `S:`.

**Fix.** Also set `STEAM_COMPAT_INSTALL_PATH` to the game folder and `STEAM_COMPAT_LIBRARY_PATHS` to `steamapps` in the launch options (see [setup.md](setup.md#4-mod-organizer-2-in-the-game-prefix)). The game, the registry and MO2 then share the same path.

**Rejected.** Browsing to the game through `Z:\Users\<you>\Library\…` works for MO2, but leaves MO2 and the registry on different paths, which tools such as LOOT and FO4Edit may trip over.

## No F4SE entry in MO2

**Symptom.** The executables list shows only Fallout 4, Fallout Launcher and Explore Virtual Folder, even after a refresh (F5).

**Cause.** MO2 adds F4SE when it creates the instance. F4SE was installed afterwards, and a refresh does not repeat the detection.

**Fix.** Add it by hand, with **Start in** set to the game folder (the field is empty by default). See [setup.md](setup.md#5-f4se).

## Harmless log lines

| Line | Where | Meaning |
| --- | --- | --- |
| `WinVerifyTrust: 00000000 80090008` | `f4se_loader.log` | Wine does not check signatures; the next line, `DLL and EXE signature/serial match`, is the one that matters |
| `os = 6.2 (9200)` | `f4se.log` | Wine reports Windows 8; no effect seen |
| `plugins.txt empty` | MO2 log | Normal for a new profile |
| `cxcompatdb:verify_file invalid signature` | `notproton-run.log` | Printed on every launch, including working ones |

## Known risks, not yet seen

| Risk | Why | What to do |
| --- | --- | --- |
| A Steam client update breaks Not Proton | Not Proton hooks specific Steam client builds and reports `updatesBlocked=false` | If Windows games stop launching after a Steam update, check `~/Library/Application Support/notproton/notproton.log` and wait for a Not Proton update |
| A Fallout 4 patch gets through | The `uchg` lock on the update manifest has not been tested against a real patch | Keep the clean clone from `fo4-backup.sh game`, and never press Play on Fallout 4 in Steam |
