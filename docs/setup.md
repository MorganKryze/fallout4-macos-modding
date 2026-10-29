# Setup guide

Fallout 4 (Steam, 1.11.240) on an Apple Silicon Mac, modded with Mod Organizer 2 and F4SE. The macOS Steam client runs the Windows game through Not Proton and CrossOver; there is no CrossOver bottle and no Windows Steam. Mod Organizer 2 runs as a non-Steam shortcut forced into the game's Wine prefix. Every step below was run on the reference machine. [troubleshooting.md](troubleshooting.md) explains the problems behind the less obvious steps.

## Requirements

| Item | Version used |
| --- | --- |
| Mac | Apple M3, 16 GB, macOS 26.5.1 |
| [CrossOver](https://www.codeweavers.com/crossover) | 26.3, with a paid licence or the trial |
| [Not Proton](https://www.ithinkdiff.com/notproton-steam-play-macos/) | 1.2.2 |
| Steam | macOS client, as supported by Not Proton |
| Fallout 4 | Steam, GOTY, runtime 1.11.240 |
| [Mod Organizer 2](https://github.com/ModOrganizer2/modorganizer/releases) | 2.5.2 |
| [F4SE](https://www.nexusmods.com/fallout4/mods/42147) | 0.7.9 |

## Paths

Not Proton gives each Steam game its own Wine prefix, the way Proton does on Linux. Inside a game's prefix, drive `S:` points at the Steam folder and `Z:` at the Mac's root.

| What | macOS path | Seen from Wine |
| --- | --- | --- |
| Game | `~/Library/Application Support/Steam/steamapps/common/Fallout 4` | `S:\steamapps\common\Fallout 4` |
| Game prefix | `~/Library/Application Support/Steam/steamapps/compatdata/377160/pfx` | `C:\` |
| My Games | `<prefix>/drive_c/users/steamuser/Documents/My Games/Fallout4` | |
| F4SE logs | `<My Games>/F4SE/` | |
| Not Proton launch log | `…/compatdata/377160/notproton-run.log` | |
| Mod Organizer 2 | `~/Games/MO2` | `Z:\Users\<you>\Games\MO2` |
| Update manifest | `…/steamapps/appmanifest_377160.acf` | |

## 1. Not Proton and CrossOver

1. Install CrossOver 26.3 in `/Applications`.
2. Install Not Proton and let it patch the Steam client. It adds a compatibility tool called "CrossOver 26.3".
3. Test with a small Windows game first. The launch log in `compatdata/<appid>/notproton-run.log` should end with `session health: healthy`.

## 2. Install the game

1. Install Fallout 4 from the macOS Steam client. It weighs 34 GB to download and 38 GB on disk.
2. Properties → Updates → Automatic Updates: **Wait until I launch the game**.
3. Properties → General: turn **Steam Cloud** off. MO2 keeps saves in its profile, so sync adds nothing.
4. Launch once with Steam's Play button, then quit. This creates the prefix `compatdata/377160` and the game's INI files.
5. Check the runtime version. It must read `1.11.240.0`:

   ```sh
   python3 -c 'import re,sys; d=open(sys.argv[1],"rb").read(); m=re.search("FileVersion".encode("utf-16-le")+rb"\x00+((?:[0-9.]\x00)+)",d); print(m.group(1).decode("utf-16-le"))' \
     ~/Library/Application\ Support/Steam/steamapps/common/Fallout\ 4/Fallout4.exe
   ```

## 3. Back up the clean game and lock updates

[`scripts/fo4-backup.sh`](../scripts/fo4-backup.sh) makes APFS clones, which take almost no space when the backup folder sits on the same volume.

```sh
ln -s "$PWD/scripts/fo4-backup.sh" ~/bin/fo4-backup.sh   # any folder in PATH
fo4-backup.sh game    # clone of the clean game
fo4-backup.sh lock    # chflags uchg on the update manifest
```

The manifest is a native macOS file, so the lock applies. From here on, never press Play on Fallout 4 in Steam: start everything from the MO2 shortcut. `fo4-backup.sh unlock` removes the lock.

## 4. Mod Organizer 2 in the game prefix

1. Download `Mod.Organizer-2.5.2.7z` from the GitHub release, extract it to `~/Games/MO2` and create an empty `portable.txt` in that folder.
2. Steam → Games → Add a Non-Steam Game → `~/Games/MO2/ModOrganizer.exe`.
3. Shortcut properties → Compatibility → CrossOver 26.3.
4. Shortcut properties → Launch Options, on one line:

   ```
   DXMT_METALFX_SPATIAL_SWAPCHAIN=1 DXMT_CONFIG="d3d11.metalSpatialUpscaleFactor=2.0" STEAM_COMPAT_DATA_PATH="$HOME/Library/Application Support/Steam/steamapps/compatdata/377160" STEAM_COMPAT_INSTALL_PATH="$HOME/Library/Application Support/Steam/steamapps/common/Fallout 4" STEAM_COMPAT_LIBRARY_PATHS="$HOME/Library/Application Support/Steam/steamapps" SteamAppId=377160 %command%
   ```

5. Launch the shortcut. MO2 asks which game to manage: pick **Fallout 4** at `S:/steamapps/common/Fallout 4`.

Why each variable is there:

| Variable | Effect |
| --- | --- |
| `STEAM_COMPAT_DATA_PATH` | Runs MO2 in the game's prefix (377160) instead of the shortcut's own |
| `STEAM_COMPAT_INSTALL_PATH`, `STEAM_COMPAT_LIBRARY_PATHS` | Make Not Proton mount `S:`, which it only does for programs inside a Steam library |
| `DXMT_METALFX_SPATIAL_SWAPCHAIN=1`, `DXMT_CONFIG=…` | DXMT upscales the game's image with Apple's MetalFX by the given factor, so the game can render at half resolution and still fill the screen (see step 6) |
| `MTL_HUD_ENABLED=1` (optional) | Shows Apple's Metal HUD: fps, GPU time per frame, frame interval |
| `SteamAppId=377160` | Makes the game see Fallout 4's app ID rather than the shortcut's (precaution, not tested on its own) |

Not Proton passes launch options through a shell, as Steam does on Linux, so `NAME=value` entries before `%command%` become environment variables.

## 5. F4SE

1. Download F4SE 0.7.9 from Nexus. The silverlock.org site now only links there.
2. Copy `f4se_1_11_240.dll`, `f4se_loader.exe` and the `Data` folder into the game folder. Skip `src`.
3. In MO2, open the executables list → `<Edit…>` → `+` → Add from file:

   | Field | Value |
   | --- | --- |
   | Title | `F4SE` |
   | Binary | `S:\steamapps\common\Fallout 4\f4se_loader.exe` |
   | Start in | `S:\steamapps\common\Fallout 4` |
   | Arguments | empty |

4. Select **F4SE** and click **Run**. The main menu shows `v (F4SE 0.7.9) 1.11.240.0.0`, and `F4SE/f4se.log` ends with `init complete`.

## 6. MO2 profile

1. Profiles → Create. Leave "Default Game INI Settings" unchecked so the profile copies the INI files the launcher wrote for this Mac.
2. Tick **Use profile-specific Game INI Files**, **Use profile-specific Save Games** and **Automatic Archive Invalidation**.
3. Add these lines to the profile's `fallout4custom.ini`:

   | Section | Line | Reason |
   | --- | --- | --- |
   | `[General]` | `bDisableAllGore=1` | Crash on dismemberment under CrossOver |
   | `[Controls]` | `bBackgroundMouse=1` | Mouse input under Wine |

4. Fallout 4's launcher detects an unknown GPU and picks Ultra, far too heavy for an M3 (69-94 ms of GPU time per frame). In the profile's `fallout4prefs.ini`, under `[Display]` and `[Imagespace]`:

   | Lines | Value |
   | --- | --- |
   | `iSize W`, `iSize H` | `1720`, `720`: half of 3440×1440, upscaled by MetalFX (factor `2.0` in the launch options). For another screen, use half its resolution |
   | In `HighFPSPhysicsFix.ini`, `[Display]` | `Fullscreen=false`, `Borderless=true`, `BorderlessUpscale=true`. Without them the game takes exclusive fullscreen at 1720×720, and the main menu is shifted with its buttons off screen |
   | `bVolumetricLightingEnable`, `iVolumetricLightingQuality` | `0`, `0` (godrays) |
   | `bSAOEnable`, `bScreenSpaceBokeh`, `bMBEnable`, `bLensFlare` | `0` |
   | `bEnableWetnessMaterials`, `bEnableRainOcclusion`, `bPrecipitationOcclusion` | `0` |
   | `iShadowMapResolution`, `fShadowDistance`, `fDirShadowDistance` | `2048`, `3000.0000`, `3000.0000` |
   | `uiShadowFilter`, `uiOrthoShadowFilter`, `iDirShadowSplits` | `1`, `1`, `2` |
   | `iMaxFocusShadows`, `iMaxFocusShadowsDialogue`, `iMaxAnisotropy` | `1`, `1`, `8` |

5. Back it up before installing any mod: `fo4-backup.sh profile "<profile name>"`.

On an AZERTY keyboard, the game reads keys as QWERTY under Wine. In game, Settings → Controls: Forward on **Z**, Strafe Left on **Q**, VATS on **A**.

## 7. Install mods

Nexus "Mod Manager" download links need MO2 registered as the `nxm://` handler, which this setup does not do. Use "Manual download" instead:

1. Download the archive from the mod's Files tab.
2. Copy it to `~/Games/MO2/downloads`. On the same volume, `cp -c` makes an instant APFS clone.
3. In MO2, open the **Downloads** tab (right pane, after Plugins, Archives, Data and Saves) and press **Refresh** if the list is empty.
4. Double-click the archive, give the mod a short name, then **OK**.
5. Tick the mod in the left pane.

Manual downloads carry no Nexus metadata, so each line in the Downloads tab shows a red warning triangle; see [troubleshooting.md](troubleshooting.md#red-triangle-on-manual-downloads).
