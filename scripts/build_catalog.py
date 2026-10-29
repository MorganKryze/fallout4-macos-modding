#!/usr/bin/env python3
"""Generate docs/catalog/*.md tables and graphs from data/mods.csv and data/nexus.json.

Each module page keeps its hand-written text; only the block between the GENERATED
markers is rewritten.
"""
import csv
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
CATALOG = ROOT / "docs/catalog"
BEGIN, END = "<!-- BEGIN GENERATED: do not edit, run scripts/build_catalog.py -->", "<!-- END GENERATED -->"

MODULES = {
    "base": "Base: script extender and unofficial patch",
    "stability": "Stability and performance",
    "interface": "Interface",
    "gameplay": "Gameplay overhaul and enemies",
    "brotherhood": "Brotherhood of Steel",
    "minutemen": "Minutemen",
    "institute": "The Institute",
    "railroad": "The Railroad",
    "raiders": "Raiders and hostile factions",
    "factions": "Factions, endings and starts",
    "settlements": "Settlements",
    "dlc": "DLC",
    "quests": "Quests and locations",
    "weapons-armor": "Weapons and armor",
    "immersion": "Immersion and quality of life",
    "companions": "Companions",
}
TIERS = ["core", "recommended", "optional", "avoid"]


def split(cell):
    return [x for x in (cell or "").split(";") if x]


def size(nexus):
    total = sum(f["size_bytes"] for f in nexus.get("main_files", [])[:1])
    return f"{total / 1e6:.1f} MB" if total >= 1e5 else (f"{total / 1e3:.0f} KB" if total else "")


def row(mod, nexus, names):
    n = nexus.get(mod["nexus_id"], {})
    url = f"https://www.nexusmods.com/fallout4/mods/{mod['nexus_id']}" if mod["nexus_id"] else ""
    img = f'<img src="{n["thumbnail"]}" width="96" alt="">' if n.get("thumbnail") and not n.get("adult") else ""
    title = f"**[{mod['name']}]({url})**" if url else f"**{mod['name']}**"
    meta = " · ".join(x for x in [
        f"by {n['author']}" if n.get("author") else "",
        f"v{n['version']}" if n.get("version") else "",
        f"updated {n['updated']}" if n.get("updated") else "",
        f"{n['endorsements']:,} endorsements" if n.get("endorsements") else "",
        size(n),
    ] if x)
    fit = [f"`{mod['tier']}`"]
    fit.append({"yes": "1.11.240: yes", "plugin-only": "1.11.240: plugin only", "no": "1.11.240: **no**"}.get(mod["runtime_1_11_240"], "1.11.240: unknown"))
    if mod["f4se_dll"] == "yes":
        fit.append("F4SE DLL")
    if mod["ending_lock"] not in ("", "none"):
        fit.append(f"locks ending: {mod['ending_lock']}")
    if mod["lunar"] in ("patch", "conflict"):
        fit.append(f"Lunar: {mod['lunar']}")
    if mod["ss2"] in ("patch", "conflict"):
        fit.append(f"SS2: {mod['ss2']}")
    cost = [f"perf {mod['perf']}"]
    if mod["scripts"] not in ("", "none"):
        cost.append(f"scripts {mod['scripts']}")
    if mod["npcs"] not in ("", "none"):
        cost.append(f"NPCs {mod['npcs']}")
    slots = f"{mod['plugins_full'] or 0} full / {mod['plugins_light'] or 0} light"
    if slots != "0 full / 0 light":
        cost.append(slots)
    if mod["precombines"] == "breaks":
        cost.append("**breaks precombines**")
    links = []
    for label, key in (("needs", "requires"), ("patches", "patches"), ("conflicts", "conflicts")):
        ids = split(mod[key])
        if ids:
            links.append(f"{label}: " + ", ".join(names.get(i, i) for i in ids))
    what = mod["summary"] + (f"<br>*{mod['notes']}*" if mod["notes"] else "")
    return f"| {img} | {title}<br><sub>{meta}</sub> | {what} | {'<br>'.join(fit)} | {'<br>'.join(cost)} | {'<br>'.join(links)} |"


def node(mod_id):
    return mod_id.replace("-", "_")  # Mermaid reads "-" in an id as part of an arrow


def graph(mods, names):
    nodes, edges = set(), []
    for m in mods:
        for dep in split(m["requires"]):
            nodes |= {m["id"], dep}
            edges.append(f'  {node(m["id"])} --> {node(dep)}')
        for p in split(m["patches"]):
            nodes |= {m["id"], p}
            edges.append(f'  {node(p)} -. patches .-> {node(m["id"])}')
    if not edges:
        return ""
    lines = ["```mermaid", "graph LR"]
    lines += [f'  {node(n)}["{names.get(n, n)}"]' for n in sorted(nodes)]
    lines += edges + ["```"]
    return "\n".join(lines)


def block(mods, nexus, names):
    if not mods:
        return "No mods in this module yet."
    counts = ", ".join(f"{sum(m['tier'] == t for m in mods)} {t}" for t in TIERS if any(m["tier"] == t for m in mods))
    full = sum(int(m["plugins_full"] or 0) for m in mods if m["tier"] != "avoid")
    out = [f"{len(mods)} mods: {counts}. Plugin slots if you take everything not marked avoid: {full} full.", ""]
    for tier in TIERS:
        group = [m for m in mods if m["tier"] == tier]
        if not group:
            continue
        out += [f"### {tier.capitalize()}", "", "| | Mod | What it does | Fit | Cost | Links |", "| --- | --- | --- | --- | --- | --- |"]
        out += [row(m, nexus, names) for m in sorted(group, key=lambda m: (int(m["load_group"] or 0), m["name"]))]
        out.append("")
    g = graph(mods, names)
    if g:
        out += ["### Dependencies and patches", "", g, ""]
    return "\n".join(out).rstrip()


def write_page(path, title, generated):
    text = path.read_text() if path.exists() else f"# {title}\n\n{BEGIN}\n{END}\n"
    head, _, rest = text.partition(BEGIN)
    _, _, tail = rest.partition(END)
    path.write_text(f"{head}{BEGIN}\n{generated}\n{END}{tail}")


def main():
    mods = list(csv.DictReader(open(ROOT / "data/mods.csv", newline="")))
    nexus = json.loads((ROOT / "data/nexus.json").read_text())
    names = {m["id"]: m["name"] for m in mods}
    unknown = {m["module"] for m in mods} - MODULES.keys()
    assert not unknown, f"unknown modules in mods.csv: {unknown}"
    CATALOG.mkdir(parents=True, exist_ok=True)
    index = ["| Module | Mods | Core | Recommended |", "| --- | --- | --- | --- |"]
    for key, title in MODULES.items():
        group = [m for m in mods if m["module"] == key]
        if not group:
            continue
        write_page(CATALOG / f"{key}.md", title, block(group, nexus, names))
        index.append(f"| [{title}]({key}.md) | {len(group)} | {sum(m['tier'] == 'core' for m in group)} | {sum(m['tier'] == 'recommended' for m in group)} |")
    write_page(CATALOG / "README.md", "Mod catalogue", "\n".join(index))


if __name__ == "__main__":
    main()
