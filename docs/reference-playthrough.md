# Reference playthrough

The mod list we play ourselves, and why. It is one way through the [catalogue](catalog/README.md), not the only one: every choice below names the alternative, so you can take a different road where your taste differs. In `data/mods.csv`, these choices are the rows with `our_pick = yes`.

## The rule behind every choice

**Stable and smooth comes before more features.** The target is a game that runs at a steady 40-45 fps on a base Apple M3 under Wine and does not crash, for a player who has already finished Fallout 4 and wants to rediscover it. A mod gets in when it changes something you will feel while playing. When in doubt it stays out: light mods can be added mid-game, but a heavy scripted mod cannot be removed from a long save.

## What the game feels like

| You notice | What does it |
| --- | --- |
| It does not crash | Addictol, Unofficial Fallout 4 Patch, Community Fixes Merged, PRP, small engine-fix DLLs, Mac-specific settings |
| The game feels new | Lunar Fallout Overhaul rebalances gear, enemies, perks and vendors; enemies flank and take cover (Adaptive Combat Tactics) |
| Settlements live | Sim Settlements 2: settlers build, a voiced campaign, an army for the Minutemen |
| The Minutemen are present | Who's The General, You And What Army 2, Minuteman Watchtowers, the Castle restored, Minutemen Takeover in Nuka-World |
| The Brotherhood is credible | Lunar's BoS gear, Show No Mercy (Fort Strong), David Hunter, Baseline Plots Brotherhood, He's With Me, A New Dawn |
| New content | America Rising 2, Far Better Far Harbor, Tales from the Commonwealth, Goodneighbor Expanded, Diamond City Expansion |
| A new companion | Heather Casdin |
| Fewer chores | No endless "another settlement needs your help", full dialogue lines, a readable interface |

## Decisions and their alternatives

| Question | Our choice | Why | If you think differently |
| --- | --- | --- | --- |
| Gameplay overhaul | **Lunar Fallout Overhaul** | Maintained again (several releases in 2026), plugin only, no scripts, works with Sim Settlements 2 | Horizon conflicts with SS2. Vanilla-plus: The Midnight Ride's gameplay stack |
| RobCo Patcher and the "Improved" faction series | **Not in this playthrough** | RobCo 6.0.6 is days old on 1.11.240, untested under Wine, invisible to FO4Edit, and likely to override Lunar at runtime. The Midnight Ride dropped it in its 1.11.240 rebuild. These mods cannot be removed mid-game | Improved Brotherhood of Steel is the best BoS overhaul if you accept the risk: test it on a throwaway save first |
| We Are The Minutemen | **Not used** | Rewrites the same Minutemen spawn tables as Lunar with no patch, duplicates Sim Settlements 2's army, and gates the Castle at level 20 | Without Lunar, WATM + its eXoPatch is the classic Minutemen overhaul |
| Big weapon pack | **Not yet** | Lunar already brings variety; a large pack means many patches | Lunar Fallout Arsenal is the Lunar-native choice: reconsider after 20-30 stable hours |
| Starts Dead Alive | **Not used** | The largest CPU cost in the list for a modest gain | Fine on a stronger machine |
| Faction ending | **Kept open** | A New Dawn adds a Minutemen ending that keeps the Brotherhood as an ally (with the cut Sentinel promotion); Delay Tactical Thinking keeps the BoS/Railroad fork open longer | Subversion adds Institute endings that spare other factions |
| Visual mods | **None for now** | The M3's GPU is the limit | Add weather or textures only with fps to spare |

## Keeping the frame rate

1. Compare the two Metal graphics backends (DXMT, D3DMetal) on the same route and keep the faster.
2. Cap the frame rate at 40-45 fps with High FPS Physics Fix: a steady 45 feels better than a 60 that keeps dropping.
3. Render below native resolution on wide screens if needed (for example 2580×1080 on a 3440×1440 display).
4. In Sim Settlements 2's performance options, turn off decorative actors, animations, sounds, radios and effects, and keep the number of large city plans small.
5. Install in batches and measure after each one, so a drop points to one batch.

## Before the real game

- Check the Lunar patches (UFO4P, SS2, Tales from the Commonwealth, NPCs Travel) against Lunar 114f in FO4Edit: they were made for earlier Lunar versions.
- Play a throwaway test of at least an hour through Sanctuary, Concord and Boston with the full list.
