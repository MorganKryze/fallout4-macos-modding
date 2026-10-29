# Interface

Menus, HUD, dialogue, item sorting and map markers. Interface mods split into Scaleform files, which do not depend on the game version (FallUI dates from 2022), and F4SE DLLs, which must state 1.11.240 support: Mod Configuration Menu and Extended Dialogue Interface both ship 1.11.240 files dated 2026-09-01. Some DLLs stalled on an earlier build and do not work on 1.11.240, such as Baka Fullscreen Pip-Boy and Aspect Ratio Fix - F4SE; LooksMenu's status is unclear. The main risks are two mods replacing the same menu file, and item sorting that must be re-run after every load-order change.

## Pick one

| Choose between | Difference | Our pick |
| --- | --- | --- |
| Extended Dialogue Interface or Full Dialogue Interface | XDI has a 1.11.240 DLL and shows full lines and more than four options; FDI is the older plugin-only UI | Extended Dialogue Interface |
| Complex Item Sorter + FIS - FallUI Item Sorter, or VIS-G Item Sorting, Valdacil's Item Sorting, Ruddy88's Simple Sorter | Complex Item Sorter is an xEdit script that tags every item in your load order, Lunar's included, with no per-mod patch. VIS-G overrides item records and needs a patch per mod | None yet |
| FallUI - Map or Simply Smaller Map Markers | Same swf file | FallUI - Map |
| Cartographers Map Markers or Unused Map Markers | Both add map markers; Cartographers scales its icons through FallUI - Map | Neither yet |
| Power Armor HUD - paHUD or HoloHUD for Power Armor | Both replace the power armor helmet display | Neither |
| Ultra Wide Interface (21x9) or TRUBY9 Ultrawidescreen | UWI 4.4 (2026-01-21) ships built-in patches for FallUI, HUDFramework and XDI; TRUBY9 is the old replacer | Ultra Wide Interface (21x9) |

## Suggested stacks

| Profile | Take | Skip |
| --- | --- | --- |
| Minimal, 16:9 screen | Mod Configuration Menu, Extended Dialogue Interface, HUDFramework, FallUI - HUD, FallUI - Inventory | Baka Fullscreen Pip-Boy, Aspect Ratio Fix - F4SE (no 1.11.240 build) |
| Ultrawide screen | The minimal stack plus Ultra Wide Interface (21x9). FallUI - Map is not in UWI's patch list: check it at 21:9 | TRUBY9 Ultrawidescreen |
| Tidy inventory | Complex Item Sorter, FIS - FallUI Item Sorter, 4estGimp CS Enhancements, FallUI - Workbench. Re-run the sorter after any change; xEdit under CrossOver is untested | VIS-G Item Sorting, Valdacil's Item Sorting |
| Explorer | FallUI - Map, Cartographers Map Markers, Radiant Quest Marker, Friendly NPCs On Compass | Simply Smaller Map Markers, Unused Map Markers |

## Our choice

The reference playthrough takes Mod Configuration Menu, Extended Dialogue Interface for full dialogue lines, HUDFramework, FallUI - HUD, FallUI - Inventory, FallUI - Map and Ultra Wide Interface (21x9) for a 3440x1440 display. We have not added an item sorter: Complex Item Sorter has to be re-run after every load-order change, and FO4Edit under CrossOver is untested.

<!-- BEGIN GENERATED: do not edit, run scripts/build_catalog.py -->
42 mods: 1 core, 18 recommended, 13 optional, 10 avoid. Plugin slots if you take everything not marked avoid: 1 full.

### Core

| | Mod | What it does | Fit | Cost | Links |
| --- | --- | --- | --- | --- | --- |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/21497-0-1504319702.png" width="96" alt=""> | **[Mod Configuration Menu](https://www.nexusmods.com/fallout4/mods/21497)**<br><sub>by reg2k - Neanka - shadowslasher410 · v1.11.240 · updated 2026-09-01 · 162,442 endorsements · 0.4 MB</sub> | In-game settings menu for mods<br>*1.11.240 main file dated 2026-09-01; old 1.39/1.40 files do not work* | `core`<br>1.11.240: yes<br>F4SE DLL | perf low<br>scripts light | needs: Fallout 4 Script Extender |

### Recommended

| | Mod | What it does | Fit | Cost | Links |
| --- | --- | --- | --- | --- | --- |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/27479-0-1508689568.gif" width="96" alt=""> | **[Crafting Highlight Fix](https://www.nexusmods.com/fallout4/mods/27479)**<br><sub>by registrator2000 · v1.11.240 · updated 2026-09-06 · 37,864 endorsements · 0.1 MB</sub> | Removes the workbench glow that hides items<br>*2026-09-06 file '1.11.240'* | `recommended`<br>1.11.240: yes<br>F4SE DLL | perf low |  |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/27216-0-1507513151.png" width="96" alt=""> | **[Extended Dialogue Interface](https://www.nexusmods.com/fallout4/mods/27216)**<br><sub>by reg2k and Neanka · v1.11.240 · updated 2026-09-01 · 51,854 endorsements · 0.3 MB</sub> | Shows full dialogue lines and more than four options<br>*Main file 'Extended Dialogue Interface 1.11.240' (2026-09-01)* | `recommended`<br>1.11.240: yes<br>F4SE DLL | perf low | patches: Companion Ivy - XDI patch<br>conflicts: Full Dialogue Interface |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/20309-0-1495318464.png" width="96" alt=""> | **[HUDFramework](https://www.nexusmods.com/fallout4/mods/20309)**<br><sub>by registrator2000 · v1.0f · updated 2026-09-04 · 108,345 endorsements · 0.3 MB</sub> | Framework for custom HUD widgets<br>*Keep; Report 08 does not give its 1.11.240 status; UWI ships a built-in HUDFramework patch* | `recommended`<br>1.11.240: plugin only | perf <br>1 full / 0 light |  |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/12581/12581-1777289123-1482161780.png" width="96" alt=""> | **[Cartographers Map Markers](https://www.nexusmods.com/fallout4/mods/12581)**<br><sub>by Feyawen · v5.0.1 · updated 2026-04-28 · 5,784 endorsements · 57 KB</sub> | Hundreds of map markers that scale via FallUI Map<br>*v5 2026-04 rewrite, ESL; Adds refs to cells: load before PRP; Not compatible with v4 saves; Pick this or Unused Map Markers* | `recommended`<br>1.11.240: plugin only | perf <br>0 full / 1 light |  |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/60580/60580-1652974864-1109451306.png" width="96" alt=""> | **[FIS - FallUI Item Sorter](https://www.nexusmods.com/fallout4/mods/60580)**<br><sub>by m8r98a4f2 · v2.1 · updated 2022-06-04 · 16,963 endorsements · 1.1 MB</sub> | Tag and icon config for FallUI Inventory<br>*Use with Complex Item Sorter* | `recommended`<br>1.11.240: plugin only | perf low | needs: FallUI - Inventory, Complex Item Sorter, FallUI - Icon Library |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/48958/48958-1619017899-322981148.png" width="96" alt=""> | **[FallUI - Confirm Boxes](https://www.nexusmods.com/fallout4/mods/48958)**<br><sub>by m8r98a4f2 · v2.2.3 · updated 2022-11-01 · 16,189 endorsements · 1.5 MB</sub> | Replaces confirm and message boxes to match FallUI, incl. Yes Im Sure<br>*In 20 of 24 Wabbajack lists (2026-10); Gap audit 2026-10-29* | `recommended`<br>1.11.240: plugin only | perf low |  |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/51813/51813-1619914903-70759095.png" width="96" alt=""> | **[FallUI - HUD](https://www.nexusmods.com/fallout4/mods/51813)**<br><sub>by m8r98a4f2 · v1.7.1 · updated 2022-11-16 · 28,106 endorsements · 2.4 MB</sub> | Configurable HUD<br>*2022 Scaleform, version-independent; UWI ships a built-in patch* | `recommended`<br>1.11.240: plugin only | perf  | needs: HUDFramework |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/60579/60579-1652974271-226033406.png" width="96" alt=""> | **[FallUI - Icon Library](https://www.nexusmods.com/fallout4/mods/60579)**<br><sub>by m8r98a4f2 · v1.0 · updated 2022-06-22 · 16,988 endorsements · 0.4 MB</sub> | Icon library used by FIS - FallUI Item Sorter<br>*Needed by fis-fallui-item-sorter (check its requires); In 20 of 24 Wabbajack lists (2026-10); Gap audit 2026-10-29* | `recommended`<br>1.11.240: plugin only | perf low | needs: FallUI - Inventory |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/48758/48758-1608059361-298835205.png" width="96" alt=""> | **[FallUI - Inventory](https://www.nexusmods.com/fallout4/mods/48758)**<br><sub>by m8r98a4f2 · v2.2.1 · updated 2022-10-28 · 31,662 endorsements · 2.8 MB</sub> | Readable inventory with sorting tags and icons<br>*2022 Scaleform, version-independent; UWI ships a built-in patch; Pair with Complex Item Sorter + FIS* | `recommended`<br>1.11.240: plugin only | perf  |  |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/49920/49920-1612647012-1670663081.png" width="96" alt=""> | **[FallUI - Map](https://www.nexusmods.com/fallout4/mods/49920)**<br><sub>by m8r98a4f2 · v2.1 · updated 2022-05-18 · 19,284 endorsements · 1.0 MB</sub> | Readable map with icon scaling<br>*Not in UWI's ultrawide patch list (behaviour at 21:9 unverified); Pair with Cartographers Map Markers v5; Same swf as Simply Smaller Map Markers* | `recommended`<br>1.11.240: plugin only | perf  | conflicts: Simply Smaller Map Markers |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/49070/49070-1621691660-2041324943.png" width="96" alt=""> | **[FallUI - Sleep and Wait](https://www.nexusmods.com/fallout4/mods/49070)**<br><sub>by m8r98a4f2 · v1.4 · updated 2022-11-12 · 17,766 endorsements · 0.8 MB</sub> | Sleep and wait menu with direct hour selection, FallUI style<br>*In 20 of 24 Wabbajack lists (2026-10); Gap audit 2026-10-29* | `recommended`<br>1.11.240: plugin only | perf low |  |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/49300/49300-1610042654-1439715988.png" width="96" alt=""> | **[FallUI - Workbench](https://www.nexusmods.com/fallout4/mods/49300)**<br><sub>by m8r98a4f2 · v1.4.1-r2 · updated 2022-11-02 · 20,757 endorsements · 1.0 MB</sub> | Bigger workbench UI with columns, search and tag icons<br>*SWF; text search uses F4SE; Part of the FallUI family on our list (may be covered by the UI report); Picked 2026-10-30: with Sim Settlements 2 the workbench lists get long; UWI has a Workbench option* | `recommended`<br>1.11.240: plugin only | perf low |  |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/937-0-1447711327.jpg" width="96" alt=""> | **[Faster Terminal Displays](https://www.nexusmods.com/fallout4/mods/937)**<br><sub>by Old Nick · v3.0 · updated 2016-04-27 · 47,449 endorsements · 1 KB</sub> | Terminal text scrolls 20 times faster | `recommended`<br>1.11.240: plugin only | perf low |  |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/56997/56997-1641059008-1632666704.png" width="96" alt=""> | **[MCM Booster](https://www.nexusmods.com/fallout4/mods/56997)**<br><sub>by m8r98a4f2 · v1.0 · updated 2022-01-01 · 13,949 endorsements · 0.6 MB</sub> | Caches MCM config files so the MCM menu opens almost instantly<br>*Incompatible with main menu replacers that ship MainMenu.swf; In 16 of 24 Wabbajack lists (2026-10); Gap audit 2026-10-29* | `recommended`<br>1.11.240: plugin only | perf low | needs: Mod Configuration Menu |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/56195/56195-1638374233-408174017.png" width="96" alt=""> | **[MCM Settings Manager](https://www.nexusmods.com/fallout4/mods/56195)**<br><sub>by m8r98a4f2 · v1.2 · updated 2022-11-16 · 12,401 endorsements · 0.1 MB</sub> | Save, load and transfer all MCM settings at once<br>*In 19 of 24 Wabbajack lists (2026-10); Gap audit 2026-10-29* | `recommended`<br>1.11.240: plugin only | perf low<br>scripts light | needs: Mod Configuration Menu |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/21622-0-1485515704.jpg" width="96" alt=""> | **[Power Armor HUD - paHUD](https://www.nexusmods.com/fallout4/mods/21622)**<br><sub>by Gopher · v1.0 · updated 2024-05-15 · 4,064 endorsements · 2.3 MB</sub> | Clean power armor HUD instead of the helmet dashboard<br>*In LitR; Interplay with FallUI-HUD unverified* | `recommended`<br>1.11.240: plugin only | perf low | needs: HUDFramework<br>conflicts: HoloHUD for Power Armor |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/65677/65677-1668454185-942962524.jpeg" width="96" alt=""> | **[Ultra Wide Interface (21x9)](https://www.nexusmods.com/fallout4/mods/65677)**<br><sub>by Aigni · v4.4 · updated 2026-01-21 · 2,107 endorsements · 19.1 MB</sub> | Fixes HUD, menus, VATS, workshop and scopes for 21:9 screens<br>*4.4 (2026-01-21), ESL-flagged ESP; Built-in patches for FallUI Inventory/HUD/Workbench/Sleep/Confirm Boxes, HUDFramework, XDI, DEF_UI, LooksMenu, MCM Booster, Baka Interface; FallUI Map not listed; Author says the aspect fix is version-independent: not verified on 1.11.240; A Smaller UI Size variant exists* | `recommended`<br>1.11.240: unknown<br>F4SE DLL | perf <br>0 full / 1 light | conflicts: TRUBY9 Ultrawidescreen |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/48826/48826-1636805582-768817055.png" width="96" alt=""> | **[Complex Item Sorter](https://www.nexusmods.com/fallout4/mods/48826)**<br><sub>by m8r98a4f2 · v1.12.0 · updated 2023-08-23 · 6,444 endorsements · 0.2 MB</sub> | xEdit script that tags every item in the load order for sorting<br>*Generates one patch after Lunar and all item mods, before PRP; Re-run after any add or remove; 1.12.0 public; 1.13 beta on the Collective Modding Discord; Can apply weightless junk without overriding Lunar values; xEdit under CrossOver untested* | `recommended`<br>1.11.240: plugin only | perf low | needs: FO4Edit |

### Optional

| | Mod | What it does | Fit | Cost | Links |
| --- | --- | --- | --- | --- | --- |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/46419/46419-1595286345-434109350.png" width="96" alt=""> | **[Configurable Hotkeys](https://www.nexusmods.com/fallout4/mods/46419)**<br><sub>by Dank Rafft · v2.1.8 · updated 2026-10-02 · 2,708 endorsements · 27 KB</sub> | MCM hotkeys for saving, using items and console commands<br>*2.1.8 (2026-10-02), actively updated; DLL and version status not checked; Gives a hard-save hotkey* | `optional`<br>1.11.240: unknown | perf low | needs: Mod Configuration Menu |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/29905/29905-1519283834-1618941735.png" width="96" alt=""> | **[Custom Camera](https://www.nexusmods.com/fallout4/mods/29905)**<br><sub>by Qudix · v0.5.5 · updated 2026-09-10 · 10,884 endorsements · 4.6 MB</sub> | MCM-configurable third-person camera<br>*In 7 of 24 Wabbajack lists (2026-10); Gap audit 2026-10-29* | `optional`<br>1.11.240: yes<br>F4SE DLL | perf low | needs: Fallout 4 Script Extender, Address Library, Mod Configuration Menu |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/66690/66690-1670188973-1884003310.png" width="96" alt=""> | **[Favorites Menu Ex](https://www.nexusmods.com/fallout4/mods/66690)**<br><sub>by Neanka · v1.11.240 · updated 2026-09-06 · 2,513 endorsements · 0.2 MB</sub> | New Vegas companion-wheel style favourites menu<br>*In 2 of 24 Wabbajack lists (2026-10); Gap audit 2026-10-29* | `optional`<br>1.11.240: yes<br>F4SE DLL | perf low | needs: Fallout 4 Script Extender |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/95776/95776-1754927191-499502336.png" width="96" alt=""> | **[Friendly NPCs On Compass](https://www.nexusmods.com/fallout4/mods/95776)**<br><sub>by shavkcagarikia · v1.03 · updated 2026-08-29 · 86 endorsements · 0.2 MB</sub> | FO3/NV-style NPC compass dots by Perception | `optional`<br>1.11.240: yes<br>F4SE DLL | perf low |  |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/12631-0-1461987661.png" width="96" alt=""> | **[LooksMenu](https://www.nexusmods.com/fallout4/mods/12631)**<br><sub>by Expired6978 · v1.7.0.4 · updated 2026-09-01 · 153,621 endorsements · 0.5 MB</sub> | Character appearance editor<br>*Page shows 1.7.0.4 (2026-09-01) but the file text still says F4SE 0.7.8 / 1.11.221; does not use Address Library; Verify in f4se.log and with 'slm 14' before relying on it* | `optional`<br>1.11.240: unknown<br>F4SE DLL | perf  |  |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/29568-0-1517429779.png" width="96" alt=""> | **[PipboyTabs](https://www.nexusmods.com/fallout4/mods/29568)**<br><sub>by Neanka · v1.11.240 · updated 2026-09-06 · 6,820 endorsements · 0.2 MB</sub> | Framework that adds new tabs to the Pip-Boy<br>*File names 1.11.240; Install only as a dependency* | `optional`<br>1.11.240: yes<br>F4SE DLL | perf  |  |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/22105-0-1487376052.jpg" width="96" alt=""> | **[Rename Anything](https://www.nexusmods.com/fallout4/mods/22105)**<br><sub>by registrator2000 · v1.11.240 · updated 2026-09-06 · 10,879 endorsements · 0.2 MB</sub> | Rename items and objects in inventory or the world<br>*In 5 of 24 Wabbajack lists (2026-10); Gap audit 2026-10-29* | `optional`<br>1.11.240: yes<br>F4SE DLL | perf low | needs: Fallout 4 Script Extender |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/109243/109243-1789895090-1403573467.png" width="96" alt=""> | **[Smart Selection](https://www.nexusmods.com/fallout4/mods/109243)**<br><sub>by Zzyxzz · v1.3.3 · updated 2026-09-30 · 322 endorsements · 0.4 MB</sub> | Better object targeting with target cycling and outline<br>*1.3.3 (2026-09-30), 'OG, NG and AE'; 1.11.240 inferred from release date; Too new to rely on* | `optional`<br>1.11.240: unknown<br>F4SE DLL | perf low |  |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/54908/54908-1645824439-1689326934.jpeg" width="96" alt=""> | **[Companion Command Menu Overhaul](https://www.nexusmods.com/fallout4/mods/54908)**<br><sub>by Aigni · v2.2 · updated 2025-12-03 · 667 endorsements · 2.0 MB</sub> | XDI-style companion command wheel<br>*Replaces MultiActivateMenu.swf; XDI uses another swf (probably fine, unverified)* | `optional`<br>1.11.240: plugin only | perf low |  |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/29969/29969-1776717620-2076796325.jpg" width="96" alt=""> | **[HoloHUD for Power Armor](https://www.nexusmods.com/fallout4/mods/29969)**<br><sub>by Doppeltganger · v2.22 · updated 2026-06-17 · 8,221 endorsements · 0.3 MB</sub> | Holographic power armor gauges without visor fog or rain drops<br>*Alternative to paHUD: pick one* | `optional`<br>1.11.240: plugin only | perf low | conflicts: Power Armor HUD - paHUD |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/20401/20401-1535598868-1743879217.jpeg" width="96" alt=""> | **[Radiant Quest Marker](https://www.nexusmods.com/fallout4/mods/20401)**<br><sub>by SilentNightxxx · v2.2 · updated 2019-11-14 · 703 endorsements · 0.7 MB</sub> | Map markers for radiant quest targets<br>*2019, untested* | `optional`<br>1.11.240: plugin only | perf  |  |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/64009/64009-1691697787-381423693.png" width="96" alt=""> | **[Unused Map Markers](https://www.nexusmods.com/fallout4/mods/64009)**<br><sub>by Crash · v1.0 · updated 2022-09-05 · 1,250 endorsements · 17 KB</sub> | Restores 50+ cut map markers<br>*Probable overlap with CMM: pick one* | `optional`<br>1.11.240: plugin only | perf  |  |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/51307/51307-1618032771-317695554.jpeg" width="96" alt=""> | **[4estGimp CS Enhancements](https://www.nexusmods.com/fallout4/mods/51307)**<br><sub>by 4estGimp · v2.8.1 · updated 2025-07-04 · 3,690 endorsements · 1.4 MB</sub> | Extra rules and icons for Complex Item Sorter<br>*2.8.2 (2025-07); Needs the CS 1.13 beta and xEdit 4.1.5f; take the No-AWKCR build; Power users* | `optional`<br>1.11.240: plugin only | perf low | needs: Complex Item Sorter, FO4Edit |

### Avoid

| | Mod | What it does | Fit | Cost | Links |
| --- | --- | --- | --- | --- | --- |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/98899/98899-1764946690-744865458.jpg" width="96" alt=""> | **[Aspect Ratio Fix - F4SE](https://www.nexusmods.com/fallout4/mods/98899)**<br><sub>by Aigni · v1.11.191.0 · updated 2025-12-17 · 20 endorsements · 0.1 MB</sub> | Fixes AE's hard-coded 16:9 aspect bug<br>*Labelled 1.11.191 only; avoid unless updated; UWI 4.4 ships its own aspect fix* | `avoid`<br>1.11.240: **no**<br>F4SE DLL | perf  |  |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/73560/73560-1763753078-573124259.png" width="96" alt=""> | **[Baka Fullscreen Pip-Boy](https://www.nexusmods.com/fallout4/mods/73560)**<br><sub>by shad0wshayd3 · v2.1.0 · updated 2026-01-04 · 2,081 endorsements · 3.6 MB</sub> | Fullscreen or Quick-Boy Pip-Boy<br>*2.1.0 stops at 1.11.191; avoid until updated* | `avoid`<br>1.11.240: **no**<br>F4SE DLL | perf  |  |
|  | **TRUBY9 Ultrawidescreen**<br><sub></sub> | Old 21:9 UI replacer<br>*Use Ultra Wide Interface instead; Main Nexus page not found by API search (only its patches); nexus_id left blank* | `avoid`<br>1.11.240: unknown | perf  | conflicts: Ultra Wide Interface (21x9) |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/10654-2-1457246860.jpg" width="96" alt=""> | **[DEF_UI](https://www.nexusmods.com/fallout4/mods/10654)**<br><sub>by Neanka and Valdacil and Old Nick and ParasiteX and sekoms · v1.6.0 · updated 2024-05-09 · 96,201 endorsements · 68.5 MB</sub> | Older inventory and HUD UI overhaul<br>*In 2 of 24 Wabbajack lists (2026-10); Gap audit 2026-10-29* | `avoid`<br>1.11.240: plugin only | perf low | conflicts: FallUI - Inventory, FallUI - HUD |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/1235-0-1448345334.png" width="96" alt=""> | **[Full Dialogue Interface](https://www.nexusmods.com/fallout4/mods/1235)**<br><sub>by Cirosan and shadwar · vBeta12 · updated 2016-09-13 · 179,988 endorsements · 73.3 MB</sub> | Older full-line dialogue UI<br>*Incompatible with XDI, which we use* | `avoid`<br>1.11.240: plugin only | perf low | conflicts: Extended Dialogue Interface |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/26575/26575-1530146112-1715008991.jpeg" width="96" alt=""> | **[LOOKUP FAILED fix for Full Dialogue Interface](https://www.nexusmods.com/fallout4/mods/26575)**<br><sub>by deathclay · v1.11.221 · updated 2026-08-28 · 8,557 endorsements · 3.0 MB</sub> | Fixes LOOKUP FAILED lines in FDI<br>*Updated 2026-08-28 for 1.11.240, but only useful with FDI, which we avoid* | `avoid`<br>1.11.240: yes | perf  | needs: Full Dialogue Interface |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/92505/92505-1780075828-129398757.png" width="96" alt=""> | **[Simply Smaller Map Markers](https://www.nexusmods.com/fallout4/mods/92505)**<br><sub>by Spifferino · v1.0.0 · updated 2025-03-26 · 842 endorsements · 92 KB</sub> | Smaller map icons<br>*Edits Pipboy_MapPage.swf, the same file as FallUI Map* | `avoid`<br>1.11.240: plugin only | perf  | conflicts: FallUI - Map |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/33983/33983-1533936310-1238457025.jpeg" width="96" alt=""> | **[Ruddy88's Simple Sorter](https://www.nexusmods.com/fallout4/mods/33983)**<br><sub>by Ruddy88 · v1.0 · updated 2019-02-01 · 3,638 endorsements · 5 KB</sub> | xEdit tagger for DEF_UI<br>*Made for DEF_UI; we use FallUI* | `avoid`<br>1.11.240: plugin only | perf  |  |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/33383/33383-1531962186-1069291878.png" width="96" alt=""> | **[VIS-G Item Sorting](https://www.nexusmods.com/fallout4/mods/33383)**<br><sub>by Gambit77 - Gernash - Valdacil - Neanka - Thirdstorm - Omega9380 - Spherikal - Khaibit · vv2.9.0 · updated 2026-02-03 · 10,325 endorsements · 25 KB</sub> | Pre-made item sorting plugin<br>*Overrides item records and needs a patch per mod, Lunar included; Use Complex Item Sorter instead* | `avoid`<br>1.11.240: plugin only<br>Lunar: patch | perf  |  |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/3877-0-1458947880.png" width="96" alt=""> | **[Valdacil's Item Sorting](https://www.nexusmods.com/fallout4/mods/3877)**<br><sub>by Valdacil · v11.0.3 · updated 2024-10-28 · 52,892 endorsements · 2.3 MB</sub> | Original pre-made item sorter<br>*Same patch burden as VIS-G* | `avoid`<br>1.11.240: plugin only | perf  |  |

### Dependencies and patches

```mermaid
graph LR
  4estgimp_cs_enhancements["4estGimp CS Enhancements"]
  address_library["Address Library"]
  companion_ivy_xdi_patch["Companion Ivy - XDI patch"]
  complex_item_sorter["Complex Item Sorter"]
  configurable_hotkeys["Configurable Hotkeys"]
  custom_camera["Custom Camera"]
  f4se["Fallout 4 Script Extender"]
  fallui_hud["FallUI - HUD"]
  fallui_icon_library["FallUI - Icon Library"]
  fallui_inventory["FallUI - Inventory"]
  favorites_menu_ex["Favorites Menu Ex"]
  fdi_lookup_failed_fix["LOOKUP FAILED fix for Full Dialogue Interface"]
  fis_fallui_item_sorter["FIS - FallUI Item Sorter"]
  fo4edit["FO4Edit"]
  full_dialogue_interface["Full Dialogue Interface"]
  hudframework["HUDFramework"]
  mcm["Mod Configuration Menu"]
  mcm_booster["MCM Booster"]
  mcm_settings_manager["MCM Settings Manager"]
  pahud["Power Armor HUD - paHUD"]
  rename_anything["Rename Anything"]
  xdi["Extended Dialogue Interface"]
  mcm --> f4se
  complex_item_sorter --> fo4edit
  companion_ivy_xdi_patch -. patches .-> xdi
  fallui_hud --> hudframework
  fallui_icon_library --> fallui_inventory
  fis_fallui_item_sorter --> fallui_inventory
  fis_fallui_item_sorter --> complex_item_sorter
  fis_fallui_item_sorter --> fallui_icon_library
  mcm_booster --> mcm
  mcm_settings_manager --> mcm
  pahud --> hudframework
  4estgimp_cs_enhancements --> complex_item_sorter
  4estgimp_cs_enhancements --> fo4edit
  configurable_hotkeys --> mcm
  custom_camera --> f4se
  custom_camera --> address_library
  custom_camera --> mcm
  favorites_menu_ex --> f4se
  rename_anything --> f4se
  fdi_lookup_failed_fix --> full_dialogue_interface
```
<!-- END GENERATED -->
