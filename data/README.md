# Mod data

Machine-readable catalogue of the mods evaluated for this setup. Two files, two owners:

| File | Written by | Contents |
| --- | --- | --- |
| `mods.csv` | Hand, reviewed | Our judgement: module, tier, compatibility, cost, dependencies, evidence |
| `nexus.json` | `scripts/nexus_sync.py` | What Nexus Mods says today: name, author, summary, image, version, dates, endorsements, file size |

Edit `mods.csv`, then run `python3 scripts/nexus_sync.py` to refresh `nexus.json` and `python3 scripts/build_catalog.py` to regenerate the pages in `docs/catalog/`.

## `mods.csv` columns

Lists inside a cell are separated by `;`. Empty cell means "none" or "not applicable".

| Column | Values | Meaning |
| --- | --- | --- |
| `id` | kebab-case slug | Stable key used by `requires`, `patches` and `conflicts` |
| `name` | text | Display name (Nexus may use a longer one) |
| `nexus_id` | integer | `https://www.nexusmods.com/fallout4/mods/<nexus_id>` |
| `file` | text | Which file to take on the Files tab when it is not the obvious main file |
| `module` | `base`, `stability`, `interface`, `gameplay`, `brotherhood`, `minutemen`, `institute`, `railroad`, `raiders`, `factions`, `settlements`, `dlc`, `quests`, `weapons-armor`, `immersion`, `companions` | Page of the catalogue the mod belongs to |
| `profiles` | `all`, `bos`, `minutemen`, `institute`, `railroad`, `raider`, `neutral` | Playthroughs the mod suits |
| `tier` | `core`, `recommended`, `optional`, `avoid` | Core: every list needs it. Avoid: listed so readers know why |
| `our_pick` | `yes`, `no`, `test` | What the reference playthrough uses |
| `summary` | one line | What the mod changes, in our words |
| `runtime_1_11_240` | `yes`, `plugin-only`, `no`, `unknown` | `yes`: the author states support. `plugin-only`: no DLL, version-independent in practice |
| `f4se_dll` | `yes`, `no` | Needs F4SE and a DLL built for 1.11.240 |
| `plugins_full` | integer | Full plugin slots used (ESM/ESP), out of 254 |
| `plugins_light` | integer | Light plugins (ESL or ESL-flagged), out of 4096 |
| `scripts` | `none`, `light`, `heavy` | Papyrus load while playing |
| `npcs` | `none`, `few`, `many` | NPCs added to the world |
| `perf` | `low`, `med`, `high` | Overall cost on the reference Mac (M3, 16 GB) |
| `precombines` | `safe`, `breaks`, `prp-patch` | Effect on precombined meshes; `prp-patch` means a PRP patch exists and is listed in `patches` |
| `lunar` | `ok`, `patch`, `conflict`, `n/a` | Compatibility with Lunar Fallout Overhaul |
| `ss2` | `ok`, `patch`, `conflict`, `n/a` | Compatibility with Sim Settlements 2 |
| `ending_lock` | `none`, `bos`, `minutemen`, `institute`, `railroad` | Faction ending the mod assumes or forces |
| `requires` | ids | Must be installed too |
| `patches` | ids | Patches to add when both this mod and the patched mod are present |
| `conflicts` | ids | Never install together |
| `load_group` | integer | Coarse load-order bucket: lower loads earlier (see below) |
| `checked_on` | `YYYY-MM-DD` | Last time a human checked the row |
| `evidence` | URLs | Sources behind the verdict (changelog, author post, Reddit thread) |
| `notes` | text | Caveats, install options, known issues |

### Load groups

| Group | Contents |
| --- | --- |
| 10 | Unofficial patch, frameworks (HUDFramework, Workshop Framework, Random Encounter Framework), PRP master |
| 20 | Overhauls loaded as masters (Lunar) |
| 30 | Large content frameworks (Sim Settlements 2) |
| 40 | Content mods: factions, quests, locations, NPCs |
| 50 | Gear, weapons, armor |
| 60 | Small tweaks and immersion |
| 80 | Compatibility patches |
| 90 | PRP plugin and previs patches |
| 99 | Must load last (script overrides) |

## `nexus.json`

Keyed by Nexus mod ID. Generated: do not edit by hand.

```json
{
  "58140": {
    "name": "BDR - BoS Done Right - ...",
    "author": "...",
    "summary": "...",
    "picture": "https://staticdelivery.nexusmods.com/...png",
    "thumbnail": "https://staticdelivery.nexusmods.com/.../thumbnails/...png",
    "category": "Immersion",
    "adult": false,
    "version": "2.0.0",
    "updated": "2023-04-01",
    "endorsements": 310,
    "downloads": 15066,
    "main_files": [{"name": "BOSDoneRight", "version": "2.0.0", "size_bytes": 18260048}],
    "synced_on": "2026-10-29"
  }
}
```
