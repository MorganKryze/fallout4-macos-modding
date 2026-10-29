# Install plan for the reference playthrough

The [reference playthrough](reference-playthrough.md) installed in eight batches, each followed by a short test, then the target load order. Installing in batches means a crash or a frame-rate drop points to one batch instead of eighty mods. Install every mod as described in [setup.md](setup.md#7-install-mods), and back up the MO2 profile before each batch (`fo4-backup.sh profile "<profile>"`).

## Rules for every batch

1. Install the batch in MO2, sort with LOOT (MO2's **Sort** button), then apply the positions in [the load order below](#target-load-order).
2. Launch through F4SE. Before playing, read `My Games/Fallout4/F4SE/f4se.log` (every DLL should say it loaded) and the Addictol log.
3. Test on a throwaway character. Lunar needs a new game, so create the test character at batch 3 and again whenever a test says "fresh save".
4. Note the frame rate at the same four spots every time: Sanctuary bridge, Concord museum steps, Diamond City market, Goodneighbor gate. The console command `coc` gets you there.

## Batches

| Batch | Mods, in install order | Test after it |
| --- | --- | --- |
| **0. Root** (by hand) | F4SE 0.7.9 in the game folder; FO4Edit 4.1.5f added as an MO2 tool | The main menu shows `F4SE 0.7.9`; `f4se.log` ends with `init complete` |
| **1. Engine and base** | Address Library (All In One); Addictol + Addictol Crash Logger (pick AE 1.11.240.0); High FPS Physics Fix; Runtime Database; Empty Vendor List Fix; Magic Effect and Spell Engine Fixes; Follower AI Approach Fix; Combat AI Nearby Object Search; Encounter Zone Recalculation; Energy Weapon Calculation Fix; Unofficial Fallout 4 Patch; Community Fixes Merged; TMR Glitchfinder AIO; PRP Full (1.11.240) only, not the update packs; MCM | Every DLL loaded in `f4se.log` (Energy Weapon Calculation Fix only loads with Runtime Database). New game, leave the vault, walk to Sanctuary, save, quit, load. In `HighFPSPhysicsFix.ini`, set `EnableVSync=false` and `InGameFPS=45.0` ([why](troubleshooting.md#slow-menu-lagging-mouse-crackling-sound)). Write down the baseline fps |
| **2. Frameworks and interface** | HUDFramework; Workshop Framework (main file only, not the Old-Gen replacers); Extended Dialogue Interface; Random Encounter Framework; FallUI Inventory, HUD, Map, Confirm Boxes, Sleep and Wait; Place Everywhere (togglable Place.ini); Ultra Wide Interface, Anniversary file (21:9 screens only; tick only the interface mods you installed) | `f4se.log`: Workshop Framework's plugin is not reported incompatible, Ultra Wide Interface's DLL loaded. MCM shows the FallUI and Workshop Framework pages. Dialogue shows full lines. Build a wall at Sanctuary with Place Everywhere off (F8) |
| **3. Lunar** | Lunar Fallout Overhaul 114f (no difficulty file); Lunar - UFO4P; Lunar - Community Fixes Merged Patch; Lunar - CC Remnants only if Lunar does not list `ccOTMFO4001-Remnants.esl` as a master; Adaptive Combat Tactics ("Tested" profile) | **Before installing:** open the three Lunar patches in FO4Edit against Lunar 114f; they were made for older versions. Then a new character: in the Concord fight, raiders take cover; the perk chart shows Lunar's text; the Concord vendor has stock; no crash on the Deathclaw |
| **4. Sim Settlements 2** | Sim Settlements 2 All Chapters Pack (keep SS2Extended.esp active); SS2 Wasteland Reconstruction Kit; SS2 - XDI Compatibility Patch; Lunar - SS2; Baseline Plots Brotherhood; Midnight Cult Fix (main file) | New game. **Decline the Prepopulation offer.** Wait for SS2's ready message after the vault, then save. Turn on SS2's performance options. Place two plots at Sanctuary and watch them build. Compare Sanctuary's fps with batch 1 |
| **5. Minutemen** | Minutemen Takeover; Who's The General; Keeper of the Commonwealth Radiants; Who's The General Patch Hub (tick Keeper); You And What Army 2; Minuteman Watchtowers (ESL); Restoring The Castle; Restoring The Castle Extended; Minutemen Ending Dialogue Fix | Finish *When Freedom Calls*: Preston gives the next quest through "How are you doing?" with no report-back. `coc` to a watchtower: no floating geometry. Radio Freedom plays |
| **6. Brotherhood, factions, companions** | David Hunter (main file only); He's With Me (No BoS Hostility, MAIN); Show No Mercy - Fort Strong Expansion; A New Dawn + its UFO4P patch; Delay Tactical Thinking; Fort Hagen Prydwen Flyover Fix; Map Marker Fix - Prydwen and Airport; Heather Casdin; Simple Everyone's Best Friend | Fresh save: *A Promising Partnership* starts near Concord. Dogmeat and one companion both follow. Check Danse's record in FO4Edit (He's With Me and Lunar may both edit it). Fort Strong may flicker until batch 8 |
| **7. Content, locations, DLC** | America Rising 2 + The Remnants Patch; Tales from the Commonwealth + Emirals Tales From The Commonwealth Fixes + the TftC eXoPatch + Lunar - TftC; Diamond City Expansion + its eXoPatch (main plugins only: `DiamondCity-PreVis.esp` waits for batch 8); Goodneighbor Expanded; Far Better Far Harbor; Nuka World Open Season Extend II; Integrated Addons (AE option); Commonwealth Encounter Pack; Commonwealth Broadcasting Services; Random Encounter Cell Reset Fix | Fresh save. America Rising 2's first quest appears after leaving the vault. No DLC or CC quest starts at the vault exit (Integrated Addons). `coc DiamondCityExt` and Goodneighbor: fps against the baseline (flicker is expected until batch 8). Tales from the Commonwealth's radio station is there |
| **8. Patches and previs** | Random Encounter Framework Patch Hub (let it detect America Rising 2, CEP, CBS, Integrated Addons); YAWA2 Patch Hub (tick Watchtowers ESL and America Rising 2); XDI - America Rising 2 Patch; then **after PRP.esp**: Restoring The Castle Extended's PRP patch, Show No Mercy's PRP 81 patch, Goodneighbor Expanded's Patch for PRP 81, `DiamondCity-PreVis.esp` (enable it now), the TftC ExoEm PRP patch, Emiral's America Rising 2 PRP 81 patch (and disable `AmericaRising2-NBPD.esp`), `FBFH_EE_Acadia_Cleanup.esp` if installed | In FO4Edit, check that the TftC and Diamond City previs patches do not override the same cells. Walk Diamond City, Goodneighbor, the NBPD station, Tucker Memorial Bridge, the Castle, Fort Strong and General Atomics: no missing walls, no flicker. Final fps at the four spots. Then the hour-long Sanctuary, Concord and Boston run |

## Target load order

Sort with LOOT, then check these positions. ESM-flagged plugins always load before ESPs whatever the list shows, and light plugins (ESL) do not use a full slot. Names in angle brackets or marked `*` were not confirmed from the archives.

```
Fallout4.esm, the 6 DLC, the 9 free Creation Club .esl files
Unofficial Fallout 4 Patch.esp       (ESM-flagged)
PPF.esm                              (PRP master, early)
TMR_GlitchfinderAIO.esm
HUDFramework.esm
WorkshopFramework.esm
XDI.esm
RandomEncounterFramework.esm*
LunarFalloutOverhaul.esp             (LOOT places it)
SS2.esm, SS2_XPAC_Chapter2.esm, SS2_XPAC_Chapter3.esm
YouAndWhatArmy2.esm
AmericaRising2.esm
SSTMinutemanWatchtowers.esl
Community Fixes Merged.esp
Lunar - UFO4.esp
Lunar - Community Fixes Merged Patch.esp*
SS2Extended.esp
<Minutemen Takeover>                 (above the other Minutemen plugins)
WhoIsTheGeneral.esp
Keeper of the Commonwealth Radiants.esp
WTG_KCR_Patch.esp
Castle walls restored.esp
<Restoring The Castle Extended>
<A New Dawn>, <A New Dawn UFO4P patch>
<Delay Tactical Thinking>
<He's With Me>
BoSStory.esp                         (David Hunter)
<Show No Mercy>
<Heather Casdin>
<Simple Everyone's Best Friend>
3DNPC_FO4.esp
<Emirals TftC Fixes>
3DNPC-eXoPatch.esp
Lunar - TalesFromTheCommonwealth.esp
Stm_DiamondCityExpansion.esp
DiamondCityExpansion-eXoPatch.esp
GoodneighborExpanded.esp
<America Rising 2 - The Remnants Patch>
BetterFarHarbor_Open.esp
<Nuka World Open Season Extend II>
<Integrated Addons>                  (after Random Encounter Framework)
<Commonwealth Encounter Pack>, <Commonwealth Broadcasting Services>
<Random Encounter Framework Patch Hub patches>
YAWA2_MW_Patch.esp, YAWA2_AmericaRising2_Patch.esp
<XDI - America Rising 2 Patch>
<SS2 - XDI Compatibility Patch>      (after SS2 and XDI)
Lunar - SS2.esp
<Baseline Plots Brotherhood>
<Midnight Cult Fix>
<Adaptive Combat Tactics>            (after Lunar)
Aigni_UltraWide.esp                  (after every other interface plugin)
<FallUI plugins>
PRP.esp                              everything above loads before PRP
prp-compat-CastleWallsExtended.esp   (first after PRP, per its author)
<Show No Mercy PRP 81 patch>
GoodneighborExpanded[Patch-Previs].esp
<TftC ExoEm PRP patch>
<Emirals America Rising 2 PRP 81 patch>   (AmericaRising2-NBPD.esp disabled)
DiamondCity-PreVis.esp               (after anything touching Diamond City, PRP included)
FBFH_EE_Acadia_Cleanup.esp           (only if installed)
```

Only previs patches go after `PRP.esp`. If Workshop Framework ever reports a script conflict, its Script Override file goes last.

## Checks only FO4Edit can do

These are known unknowns from the research. Do them before starting the real game:

| Check | Why |
| --- | --- |
| Lunar - UFO4P, Lunar - SS2 and Lunar - Community Fixes Merged against Lunar 114f | Patches made for older Lunar versions can silently restore old values |
| Lunar's masters include `ccOTMFO4001-Remnants.esl` | If not, add Lunar - CC Remnants |
| He's With Me and Lunar on Danse's record | Both may edit it |
| Emiral's America Rising 2 PRP patch only edits cell headers | It was made for America Rising 2 1.1.2; the current version is 1.1.7 |
| TftC ExoEm PRP patch and `DiamondCity-PreVis.esp` | They may cover the same Diamond City cells |
| The Remnants Patch and Integrated Addons | Both change when the Enclave Remnants quest starts |
| A New Dawn and Who's The General | Both may edit the Minutemen ending quest |
