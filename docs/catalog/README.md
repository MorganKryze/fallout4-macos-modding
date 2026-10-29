# Mod catalogue

Fallout 4 mods evaluated for runtime 1.11.240, one page per module. Each page opens with a short hand-written guide: what the module covers and its main risk, the mutually exclusive choices ("Pick one"), suggested stacks for a few player profiles, and what the reference playthrough takes ("Our choice"). Below that, a table generated from [`data/mods.csv`](../../data/mods.csv) and Nexus Mods metadata lists every mod in the module, grouped by tier.

## How to read a page

- **Tiers.** `core`: every list needs it. `recommended`: worth taking in most lists. `optional`: depends on taste, machine or faction. `avoid`: listed so you know why not; the italic note under the summary gives the reason.
- **Fit column.** The tier, then 1.11.240 support: `yes` means the author states support, `plugin only` means no DLL and version-independent in practice, `unknown` is a risk to check. It also flags an F4SE DLL, a faction ending the mod locks, and a needed patch or a conflict with Lunar Fallout Overhaul or Sim Settlements 2.
- **Cost column.** Performance on the reference Mac (base M3, 16 GB, under Wine), Papyrus script load, NPCs added, plugin slots used (full and light), and whether the mod breaks precombines.
- **Links column and graph.** What the mod needs, the patches to add when both mods are present, and what it conflicts with.
- **`our_pick`.** A column in `mods.csv` marking what the [reference playthrough](../reference-playthrough.md) uses (`yes`). Each page's "Our choice" section names those mods and what we left out. It is one road through the catalogue, not a requirement.

Column definitions and allowed values: [data/README.md](../../data/README.md). If an AI assistant is building a list for you, point it at [llms.txt](../../llms.txt).

<!-- BEGIN GENERATED: do not edit, run scripts/build_catalog.py -->
| Module | Mods | Core | Recommended |
| --- | --- | --- | --- |
| [Base: script extender and unofficial patch](base.md) | 6 | 3 | 0 |
| [Stability and performance](stability.md) | 74 | 4 | 15 |
| [Interface](interface.md) | 33 | 1 | 13 |
| [Gameplay overhaul and enemies](gameplay.md) | 102 | 0 | 12 |
| [Brotherhood of Steel](brotherhood.md) | 68 | 0 | 9 |
| [Minutemen](minutemen.md) | 54 | 0 | 13 |
| [The Institute](institute.md) | 44 | 0 | 5 |
| [The Railroad](railroad.md) | 55 | 0 | 11 |
| [Raiders and hostile factions](raiders.md) | 32 | 0 | 3 |
| [Factions, endings and starts](factions.md) | 30 | 0 | 4 |
| [Settlements](settlements.md) | 80 | 0 | 14 |
| [DLC](dlc.md) | 65 | 0 | 12 |
| [Quests and locations](quests.md) | 127 | 0 | 39 |
| [Weapons and armor](weapons-armor.md) | 77 | 0 | 12 |
| [Immersion and quality of life](immersion.md) | 63 | 0 | 11 |
| [Companions](companions.md) | 40 | 0 | 5 |
<!-- END GENERATED -->
