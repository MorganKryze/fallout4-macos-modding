# Base: script extender and unofficial patch

Every list on runtime 1.11.240 starts from three pieces: Fallout 4 Script Extender, Address Library and the Unofficial Fallout 4 Patch. All three caught up with 1.11.240 in August 2026: F4SE 0.7.9 (2026-08-18) requires it, the Address Library All In One file for 1.11.240 is dated 2026-08-22, and UFO4P 2.2.2a needs 1.11.221 or later plus the free update content. The main risk sits downstream: every F4SE DLL mod must state 1.11.240 support, because DLLs built for 1.10.163 (old-gen) or 1.10.984 (next-gen) do not work. RobCo Patcher and Runtime Database are listed here because the "Improved" faction series depends on them.

## Suggested stacks

| Profile | Take | Skip |
| --- | --- | --- |
| Any list | Fallout 4 Script Extender (copied into the game folder by hand, not through Mod Organizer 2), Address Library, Unofficial Fallout 4 Patch (PRP requires it) | Nothing: all three are core |
| Plugin-only list on a Mac under Wine | The three core mods | RobCo Patcher, Runtime Database |
| Player who wants Improved Minutemen, Improved Brotherhood of Steel or Improved Hostile Factions | The three core mods, RobCo Patcher 6.0.6, Runtime Database 1.0.0 | Nothing here, but test on a throwaway save first: Runtime Database dates from 2026-08-26 and has no stability reports under Wine either way |

## Our choice

The reference playthrough takes the three core rows: Fallout 4 Script Extender, Address Library and Unofficial Fallout 4 Patch. We leave out RobCo Patcher and Runtime Database: RobCo 6.0.6 is days old on 1.11.240, untested under Wine, invisible to FO4Edit and likely to override Lunar at runtime, and a mod built on it cannot be removed mid-game.

<!-- BEGIN GENERATED: do not edit, run scripts/build_catalog.py -->
7 mods: 3 core, 4 optional. Plugin slots if you take everything not marked avoid: 1 full.

### Core

| | Mod | What it does | Fit | Cost | Links |
| --- | --- | --- | --- | --- | --- |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/47327/47327-1599728447-276378518.png" width="96" alt=""> | **[Address Library](https://www.nexusmods.com/fallout4/mods/47327)**<br><sub>by Ryan · v1.11.240 · updated 2026-08-21 · 68,559 endorsements · 57.7 MB</sub> | Memory addresses for F4SE plugins<br>*All In One 1.11.240 file dated 2026-08-22* | `core`<br>1.11.240: yes | perf low | needs: Fallout 4 Script Extender |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/42147/42147-1574018373-1181117442.jpeg" width="96" alt=""> | **[Fallout 4 Script Extender](https://www.nexusmods.com/fallout4/mods/42147)**<br><sub>by F4SE Team · v0.7.9 · updated 2026-08-18 · 101,706 endorsements · 0.9 MB</sub> | Script extender every DLL mod depends on<br>*Copy into the game folder by hand; not through MO2; 0.7.9 (2026-08-18) requires game 1.11.240* | `core`<br>1.11.240: yes<br>F4SE DLL | perf low |  |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/4598-0-1456989707.png" width="96" alt=""> | **[Unofficial Fallout 4 Patch](https://www.nexusmods.com/fallout4/mods/4598)**<br><sub>by The Unofficial Patch Project Team · v2.2.2a · updated 2026-08-18 · 214,839 endorsements · 41.8 MB</sub> | Thousands of community bug fixes<br>*Needs 1.11.221 or later and the free update content; 2.2.2a (2026-08-18); PRP requires it* | `core`<br>1.11.240: yes<br>Lunar: patch | perf low<br>scripts light<br>1 full / 0 light | patches: Lunar - UFO4P, Nora Spouse Companion Bug Fixes |

### Optional

| | Mod | What it does | Fit | Cost | Links |
| --- | --- | --- | --- | --- | --- |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/67528/67528-1672913269-611380998.png" width="96" alt=""> | **[Base Object Swapper](https://www.nexusmods.com/fallout4/mods/67528)**<br><sub>by powerofthree · v2.2.1 · updated 2025-11-30 · 4,746 endorsements · 0.3 MB</sub> | F4SE framework that swaps base objects and references from INI configs<br>*Install only as a dependency; In 18 of 24 Wabbajack lists (2026-10); Gap audit 2026-10-29* | `optional`<br>1.11.240: yes<br>F4SE DLL | perf low | needs: Fallout 4 Script Extender, Address Library |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/69798/69798-1679152528-1530192852.jpeg" width="96" alt=""> | **[RobCo Patcher](https://www.nexusmods.com/fallout4/mods/69798)**<br><sub>by Zzyxzz · v6.0.6 · updated 2026-10-23 · 18,316 endorsements · 0.7 MB</sub> | F4SE plugin that patches game records at runtime from ini files<br>*6.0.6 (2026-10-23); main file labelled 'Game Version OG, NG, AE'; 1.11.240 support comes through Runtime Database; Only install it if a chosen mod needs it (Improved Minutemen, Improved BoS, Improved Hostile Factions, Improved Guards); The Midnight Ride removed its last RobCo requirement; 6.0.6 (2026-10-23): OG, NG, AE; Needed by Improved Minutemen, Improved BoS, TR RobCo patch, Ragged Thunder RobCo; Injected items skip Lunar's balance rules; STEP 1.1 still says RobCo is not yet stable on AE (older note); 6.0.6 (2026-10-23) supports OG/NG/AE (not 1.11.240 by name); SS2 wiki: RobCo INIs with NONE/keyword filters break SS2 weapons and are invisible to xEdit; Required by Improved Minutemen; test carefully* | `optional`<br>1.11.240: yes<br>F4SE DLL | perf low | needs: Fallout 4 Script Extender, Runtime Database |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/108394/108394-1787679221-2045338526.png" width="96" alt=""> | **[Runtime Database](https://www.nexusmods.com/fallout4/mods/108394)**<br><sub>by Zzyxzz · v1.0.0 · updated 2026-08-26 · 1,844 endorsements · 46.4 MB</sub> | Address-search layer that RobCo Patcher 6.x depends on<br>*1.0.0 (2026-08-26); States support for 1.11.x including 1.11.221 and 1.11.240; Very new; no stability reports under Wine either way; 1.0.0 lists 1.11.240; Required by RobCo 6.0.6, Bastion, Energy Weapon Calculation Fix, VATS Freeze Fix, Modern Combat AI* | `optional`<br>1.11.240: yes<br>F4SE DLL | perf low | needs: Fallout 4 Script Extender |
| <img src="https://staticdelivery.nexusmods.com/mods/1151/images/thumbnails/48365/48365-1605096722-1428299081.png" width="96" alt=""> | **[Spell Perk Item Distributor](https://www.nexusmods.com/fallout4/mods/48365)**<br><sub>by powerofthree-sasnikol · v3.1.1 · updated 2025-11-30 · 7,376 endorsements · 0.3 MB</sub> | F4SE plugin that distributes perks, items, spells and packages to NPCs from config files<br>*AE 3.1.1 (2025-11-30) states 'version 1.11.137 +'; no explicit 1.11.240 statement or user report found; Also needs VC++ 2022 and Baka Framework (5.0.0 states 1.11.240); Do not take the OG 2.0 or NG 3.0.0 files; Check po3_SpellPerkItemDistributorF4.log after first launch* | `optional`<br>1.11.240: unknown<br>F4SE DLL | perf low | needs: Fallout 4 Script Extender, Address Library, Baka Framework |

### Dependencies and patches

```mermaid
graph LR
  address_library["Address Library"]
  baka_framework["Baka Framework"]
  base_object_swapper["Base Object Swapper"]
  f4se["Fallout 4 Script Extender"]
  lunar_ufo4p_patch["Lunar - UFO4P"]
  nora_spouse_bug_fixes["Nora Spouse Companion Bug Fixes"]
  robco_patcher["RobCo Patcher"]
  runtime_database["Runtime Database"]
  spid["Spell Perk Item Distributor"]
  ufo4p["Unofficial Fallout 4 Patch"]
  address_library --> f4se
  lunar_ufo4p_patch -. patches .-> ufo4p
  nora_spouse_bug_fixes -. patches .-> ufo4p
  base_object_swapper --> f4se
  base_object_swapper --> address_library
  robco_patcher --> f4se
  robco_patcher --> runtime_database
  runtime_database --> f4se
  spid --> f4se
  spid --> address_library
  spid --> baka_framework
```
<!-- END GENERATED -->
