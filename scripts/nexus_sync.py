#!/usr/bin/env python3
"""Refresh data/nexus.json from the public Nexus Mods GraphQL API (no key needed)."""
import csv
import datetime
import json
import pathlib
import sys
import time
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
API = "https://api.nexusmods.com/v2/graphql"
GAME_ID = "1151"  # Fallout 4

MOD_QUERY = """query($id: String!) { mods(filter: {gameId: [{value: "%s"}], modId: [{value: $id}]}) {
  nodes { name author summary pictureUrl thumbnailUrl version updatedAt endorsements downloads adultContent modCategory { name } } } }""" % GAME_ID
FILES_QUERY = """query($id: ID!) { modFiles(modId: $id, gameId: "%s") { name version category sizeInBytes } }""" % GAME_ID


def gql(query, variables):
    body = json.dumps({"query": query, "variables": variables}).encode()
    req = urllib.request.Request(API, body, {"Content-Type": "application/json", "User-Agent": "fallout4-macos-modding"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.load(resp)
            if "errors" in data:
                raise RuntimeError(data["errors"][0]["message"])
            return data["data"]
        except OSError:
            time.sleep(2 * (attempt + 1))
    raise RuntimeError("Nexus API unreachable")


def fetch(nexus_id):
    nodes = gql(MOD_QUERY, {"id": nexus_id})["mods"]["nodes"]
    if not nodes:
        return None
    m = nodes[0]
    files = gql(FILES_QUERY, {"id": nexus_id})["modFiles"] or []
    return {
        "name": m["name"],
        "author": m["author"],
        "summary": m["summary"],
        "picture": m["pictureUrl"],
        "thumbnail": m["thumbnailUrl"],
        "category": (m["modCategory"] or {}).get("name"),
        "adult": m["adultContent"],
        "version": m["version"],
        "updated": m["updatedAt"][:10],
        "endorsements": m["endorsements"],
        "downloads": m["downloads"],
        "main_files": [
            {"name": f["name"], "version": f["version"], "size_bytes": int(f["sizeInBytes"] or 0)}
            for f in files if f["category"] == "MAIN"
        ],
        "synced_on": datetime.date.today().isoformat(),
    }


def main():
    rows = list(csv.DictReader(open(ROOT / "data/mods.csv", newline="")))
    ids = sorted({r["nexus_id"] for r in rows if r["nexus_id"]}, key=int)
    out_path = ROOT / "data/nexus.json"
    out = json.loads(out_path.read_text()) if out_path.exists() else {}
    today = datetime.date.today().isoformat()
    force = "--force" in sys.argv
    for i, nexus_id in enumerate(ids, 1):
        if not force and out.get(nexus_id, {}).get("synced_on") == today:
            continue
        info = fetch(nexus_id)
        if info:
            out[nexus_id] = info
        else:
            print(f"warning: mod {nexus_id} not found (hidden or removed)", file=sys.stderr)
        print(f"{i}/{len(ids)} {nexus_id}", file=sys.stderr)
        if i % 50 == 0:  # keep progress if the run is interrupted
            out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
        time.sleep(0.3)
    out = {k: out[k] for k in sorted(out, key=int) if k in ids}
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
