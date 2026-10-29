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

## MO2 asks to handle nxm links

**Symptom.** At startup MO2 asks "Mod Organizer is not set up to handle nxm links. Associate it with nxm links?"

**Cause.** Accepting writes the `nxm://` handler into the Wine prefix registry. macOS browsers never read it, so Nexus "Mod manager download" buttons would still not reach MO2.

**Fix.** Click **No, don't ask again** and use manual downloads ([setup.md](setup.md#7-install-mods)).

## Red triangle on manual downloads

**Symptom.** Every archive in MO2's Downloads tab shows a red warning triangle: "Information missing, please select 'Query Info' from the context menu to re-retrieve."

**Cause.** MO2 stores the Nexus mod ID and version in a `.meta` file it writes for downloads it made itself. Archives copied in by hand have none.

**Fix.** None needed: the archives install normally. "Query Info" only works once MO2 is logged in to the Nexus API.

## Archive with a `Data` folder at its root

**Symptom.** Some archives, such as MCM, put everything under `Data/`. Installed as is, the files would land in `Data/Data/` and the game would not see them.

**Fix.** MO2 usually detects this and unwraps the folder. If it opens the manual install window instead, right-click `Data` → **Set data directory** → OK. Check the result in `~/Games/MO2/mods/<mod>/`: it must hold `F4SE`, `Interface`, `Scripts` and so on, not `Data`.

## Slow menu, lagging mouse, crackling sound

**Symptom.** 25-30 fps on the intro and main menu, the cursor trails behind the mouse, and the sound crackles. The Metal HUD (`MTL_HUD_ENABLED=1`) shows the GPU at about 5 ms per frame, the frame interval at 34-39 ms jumping between about 16 and 33 ms.

**Cause.** The GPU is idle most of each frame: the time goes to the CPU (x86 code under Rosetta) and to VSync. With VSync on, a frame that misses one 60 Hz refresh waits for the next, so the frame time doubles. Other heavy apps on the Mac make it worse.

**Fix.** In `HighFPSPhysicsFix.ini` (in the mod's `F4SE/Plugins` folder), set `EnableVSync=false` and `InGameFPS=45.0`, and keep `AllowTearing=true`. Close heavy apps and restart the Mac if it has been up for days with swap in use. Result on a base M3 at 3440×1440: 44-45 fps, frame interval steady at 22.5 ms. If the sound still crackles, see [Crackling sound](#crackling-sound).

## Crackling sound

**Symptom.** The sound crackles in game on the MacBook's speakers, even at a steady 45 fps.

**Cause.** Not confirmed. The game used Wine's own XAudio2 (built on FAudio): CodeWeavers' recipe for Fallout 4 sets `xaudio2_7` and `x3daudio1_7` to native, but Not Proton does not apply it, and the prefix's `DllOverrides` key is empty.

**Fix.** Add `WINEDLLOVERRIDES="xaudio2_7,x3daudio1_7=n,b"` to the launch options. The Microsoft DLLs are already in the prefix's `system32`. Check while the game runs: `lsof -p <pid of Fallout4.exe> | grep -i xaudio` must list `windows/system32/xaudio2_7.dll`. Result: no crackling over a full session. The speakers' output was also set to 96 kHz in Audio MIDI Setup beforehand, so that change may play a part.

## Game cursor drifts from the macOS cursor

**Symptom.** In menus and dialogues, the game's cursor sits up and to the left of where the mouse points, and stays off for the rest of the session. The macOS cursor shows up at times.

**Cause.** Two cursors move independently: the game's, driven by mouse movement, and the macOS one. Anything that takes the mouse from the game for a moment shifts one against the other: the macOS cursor reaching another display or a hot corner (with `bBackgroundMouse=1` nothing holds it in the window), or a click on the top row of the screen, which opens the menu bar even when it is hidden. `winemac.drv` releases the mouse whenever a menu opens.

**Fix.** `bBackgroundMouse=0`, Wine's `MouseWarpOverride=force`, and the menu bar plugin, all in [setup.md](setup.md#6-mo2-profile). What did not help: exclusive fullscreen (`Fullscreen=true` in `HighFPSPhysicsFix.ini`, shifts the menus), the menu bar always shown, Wine's `CaptureDisplaysForFullscreen`, and Wine's event-tap cursor clipping (`UseConfinementCursorClipping=n`).

## Low frame rate in game

**Symptom.** 15-20 fps outside and in the pre-war house, while the main menu ran at 45. The Metal HUD shows 69-94 ms of GPU time per frame.

**Cause.** The game is GPU-bound. Fallout 4's launcher does not recognise the Apple GPU and writes the Ultra preset: 4096 shadows out to 20,000 units, godrays, ambient occlusion, bokeh. Lowering those settings alone still left 69 ms outside at 3440×1440.

**Fix.** The settings and the half-resolution render with MetalFX upscaling in [setup.md](setup.md#6-mo2-profile). The game fills the screen at 1720×720 upscaled to 3440×1440.

## Keys act as QWERTY

**Symptom.** On an AZERTY keyboard, moving needs the keys labelled W and A.

**Fix.** Remap in game, Settings → Controls: Forward on Z, Strafe Left on Q, VATS on A.

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
| A second launch kills the running game | Not Proton's `run` script releases its lock before starting the game, and every later launch on app 377160 runs `wineserver -k` | While MO2 or the game runs, do not start the Steam Fallout 4 entry, another shortcut on 377160, or a Wine tool through Not Proton in that prefix. Calling the runner's `wine` directly does not go through this script |
| A Fallout 4 patch gets through | The `uchg` lock on the update manifest has not been tested against a real patch | Keep the clean clone from `fo4-backup.sh game`, and never press Play on Fallout 4 in Steam |
