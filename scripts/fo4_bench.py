#!/usr/bin/env python3
"""Frame-time summary from the Metal HUD's per-frame log.

Launch the game with MTL_HUD_ENABLED=1 MTL_HUD_LOG_ENABLED=1. The HUD writes
its statistics to stderr, which Not Proton sends to
~/Library/Application Support/notproton/launchers/377160/notproton-wine.log
(emptied at every launch: copy it before relaunching). The unified log
(log stream) is useless: it redacts the values as <private>.

  python3 fo4_bench.py [--hz 60] [--proc NAME] [--from HH:MM:SS] [--to HH:MM:SS] LOG...

Each line is "metal-HUD: <frame>,<n>,<memory>," then one
"<present interval ms>,<gpu time ms>" pair per frame. On macOS 26.5 each pair
is written twice in a row; the script drops the copies.
"""
import re, statistics, sys

LINE = re.compile(r"(\d\d:\d\d:\d\d)\.\d+ (\S+?)\[\d+:\d+\] metal-HUD: ([0-9.,]+)")


def frames(text, proc=None, start=None, end=None):
    """Return [(interval_ms, gpu_ms)] for the frames in a stderr capture."""
    stream = []
    for m in LINE.finditer(text):
        if (proc and m[2] != proc) or (start and m[1] < start) or (end and m[1] > end):
            continue
        v = [float(x) for x in m[3].strip(",").split(",") if x][3:]
        stream += [(v[i], v[i + 1]) for i in range(0, len(v) - 1, 2)]
    pairs = list(zip(stream[0::2], stream[1::2]))
    # ponytail: "every frame twice" is detected on the whole stream, not per line
    if pairs and sum(a == b for a, b in pairs) / len(pairs) > 0.9:
        stream = stream[0::2]
    return [f for f in stream if f[0] > 0]


def summary(data, hz):
    iv = sorted(f[0] for f in data)
    gpu = sorted(f[1] for f in data)
    q = lambda s, p: round(s[min(len(s) - 1, int(len(s) * p))], 1)
    worst = iv[-max(1, len(iv) // 100):]  # slowest 1% of frames
    spike = 2000 / hz  # a frame held for more than two refreshes
    return {
        "frames": len(iv),
        "seconds": round(sum(iv) / 1000),
        "fps": round(1000 * len(iv) / sum(iv), 1),
        "1%low": round(1000 / statistics.mean(worst), 1),
        "p50ms": q(iv, 0.5),
        "p99ms": q(iv, 0.99),
        f">{spike:.0f}ms": sum(v > spike for v in iv),
        "gpu50": q(gpu, 0.5),
        "gpu95": q(gpu, 0.95),
    }


def selftest():
    log = ("12:00:01.000 Fallout4.exe[1:2] metal-HUD: 9,0,800,22.2,17.0,22.2,17.0,44.4,20.0,44.4,20.0,\n"
           "12:00:01.500 other[3:4] metal-HUD: 9,0,800,5.0,1.0,\n")
    data = frames(log, proc="Fallout4.exe")
    assert data == [(22.2, 17.0), (44.4, 20.0)], data
    s = summary(data * 100, 60)
    assert s["frames"] == 200 and s[">33ms"] == 100 and s["1%low"] == 22.5, s
    assert frames(log, start="12:00:02") == []


if __name__ == "__main__":
    selftest()
    args, opt = sys.argv[1:], {}
    while args and args[0].startswith("--"):
        opt[args[0][2:]] = args[1]
        args = args[2:]
    if not args:
        sys.exit(__doc__)
    for path in args:
        data = frames(open(path, errors="replace").read(), opt.get("proc"), opt.get("from"), opt.get("to"))
        if not data:
            print(f"{path}: no metal-HUD lines (MTL_HUD_LOG_ENABLED=1 set? log copied before relaunch?)")
            continue
        print(path, " ".join(f"{k}={v}" for k, v in summary(data, float(opt.get("hz", 60))).items()))
