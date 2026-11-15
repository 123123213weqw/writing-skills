#!/usr/bin/env python3
"""Randomly sample master paragraphs (style-diverse) to imitate this session.

Usage: python3 scripts/sample.py [--n 5] [--seed N]
Prints N entries, each from a different author, tags non-repeating where possible.
"""
import argparse, json, random, re
from pathlib import Path

POOL = Path(__file__).resolve().parent.parent / "assets" / "style-pool.md"

def load():
    entries = []
    cur = None
    for line in POOL.read_text(encoding="utf-8").splitlines():
        m = re.match(r"## \[(.+?)·(\d+)赞\] (.+?) \| 标签:(.+)$", line)
        if m:
            cur = {"author": m.group(1), "votes": int(m.group(2)),
                   "scene": m.group(3), "tags": m.group(4).split("/")}
        elif line.startswith("> ") and cur:
            cur["text"] = line[2:]
            entries.append(cur); cur = None
    return entries

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=5)
    ap.add_argument("--seed", type=int, default=None)
    args = ap.parse_args()
    if args.seed is not None:
        random.seed(args.seed)
    pool = load()
    picked, used_authors, used_tags = [], set(), set()
    random.shuffle(pool)
    for e in pool:
        if len(picked) >= args.n: break
        if e["author"] in used_authors: continue
        if set(e["tags"]) & used_tags: continue
        picked.append(e); used_authors.add(e["author"]); used_tags.update(e["tags"])
    for e in picked:
        print(f"[{e['author']}·{e['votes']}赞 | {e['scene']} | {'/'.join(e['tags'])}]")
        print(f"  {e['text']}\n")

if __name__ == "__main__":
    main()
