# Performance on Apple Silicon

What the reference Mac delivers, measured, and what that means for your list. Read this before choosing how many mods to install.

## The short answer

On a base Apple M3 MacBook Air, the game with the stability and interface mods holds a steady 40-45 fps. The full [reference playthrough](reference-playthrough.md) (81 mods) installs and runs, but outdoors it falls to 20-30 fps after half an hour of play. That is below what we call playable, so on this Mac keep a light list.

The limit is the GPU. The game already renders at half resolution with MetalFX upscaling and reduced shadows ([setup](setup.md#6-mo2-profile)), and GPU time per frame still reaches 30 ms outdoors with the full list.

## Measurements

Reference machine: MacBook Air, Apple M3 (10-core GPU), 16 GB, fanless, macOS 26.5.1, 3440×1440 screen at 60 Hz, game capped at 45 fps by High FPS Physics Fix. Each session was recorded with [`fo4_watch.sh`](../scripts/fo4_watch.sh) and summarised with [`fo4_bench.py`](../scripts/fo4_bench.py). At 45 fps a frame lasts 22.2 ms; a frame over 33 ms is a visible stutter.

| Mods active | Session | Median frame | 1% low | Frames over 33 ms | GPU time, median / 95th percentile |
| --- | --- | --- | --- | --- | --- |
| [Batch 1](install-plan.md#batches): engine, fixes, PRP | 5 min, new game to Sanctuary | 22.0 ms | 15.9 fps | 7.7 % | 13.3 / 34.7 ms |
| Batches 1-2: plus frameworks and interface | 8 min | 21.9 ms | 19.6 fps | 3.0 % | 12.2 / 33.6 ms |
| Batches 1-8: the full list | 35 min, new game, vault exit, Sanctuary | 22.1 ms | 10.5 fps | 8.9 % | 13.2 / 35.0 ms |

The session averages hide the end of the full-list session: walking outdoors at Sanctuary after 30 minutes, GPU time had risen to a 24-31 ms median with spikes to 85 ms, and the game used 2.5 CPU cores. We did not isolate the cause between heat build-up in the fanless chassis, other apps loading the Mac, and the scripts of the content mods. The mods themselves place almost nothing in Sanctuary's cells and do not break its precombined meshes, so the cost is not static geometry.

## Which Mac for which list

| Mac | What to install |
| --- | --- |
| Base M-series chip, fanless (MacBook Air) | Batches 1 and 2: stability, fixes, interface. Add content mods one at a time and measure each |
| Base chip with a fan (MacBook Pro, Mac mini) | Same start. The fan should hold clocks over long sessions, but the GPU is the same size: not measured |
| Pro or Max chip, or a newer generation (M4, M5) | The full reference list is the target. These GPUs have more cores or a newer design, which addresses the bottleneck measured above. Not measured: report your numbers in an issue |

Whatever the Mac, the steps that saved the most frame time were the graphics settings and the half-resolution render in [setup.md](setup.md#6-mo2-profile), then the frame cap ([troubleshooting](troubleshooting.md#slow-menu-lagging-mouse-crackling-sound)). Sim Settlements 2's performance options and keeping city plans few come next.

## Measure your own Mac

1. Launch with `MTL_HUD_ENABLED=1 MTL_HUD_LOG_ENABLED=1` in the launch options.
2. Start `scripts/fo4_watch.sh <label>` before the game; it copies the Metal HUD log and samples CPU, memory and load while you play.
3. Play the same route every time, then run `python3 scripts/fo4_bench.py --hz 60 <session folder>/wine.log`.
4. Close other heavy apps first: a busy Mac makes the numbers meaningless.
