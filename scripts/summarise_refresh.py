#!/usr/bin/env python3
"""
Diff two snapshots of the seed dataset and print a human summary.

Used by the refresh workflow to write its job summary, but works anywhere:

    python3 scripts/summarise_refresh.py BEFORE.json [AFTER.json]

Reports, per series, the change in observation count and in coverage end date,
plus series that appeared or disappeared. Exits 0 always — this reports, it
does not gate. scripts/validate_data.py is the gate.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load(p: Path) -> dict:
    if not p.exists():
        print(f"(no snapshot at {p})")
        return {}
    return json.loads(p.read_text(encoding="utf-8")).get("series", {})


def span(s: dict) -> tuple[int, str]:
    obs = [o for o in s.get("observations", []) if o[1] is not None]
    return len(obs), (obs[-1][0] if obs else "-")


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 0
    before = load(Path(sys.argv[1]))
    after = load(Path(sys.argv[2]) if len(sys.argv) > 2
                 else ROOT / "data" / "seed" / "series.json")

    added = sorted(set(after) - set(before))
    dropped = sorted(set(before) - set(after))
    changed = []
    for sid in sorted(set(before) & set(after)):
        nb, eb = span(before[sid])
        na, ea = span(after[sid])
        if (nb, eb) != (na, ea):
            changed.append((sid, nb, eb, na, ea))

    if not (added or dropped or changed):
        print("No change — upstream returned the same values.")
        return 0

    if added:
        print(f"NEW SERIES ({len(added)})")
        for sid in added:
            n, e = span(after[sid])
            print(f"  + {sid:26} {n:>5} obs, through {e}")
        print()
    if changed:
        print(f"UPDATED ({len(changed)})")
        for sid, nb, eb, na, ea in changed:
            arrow = f"{nb:>5} -> {na:<5}"
            tail = f"  through {eb} -> {ea}" if eb != ea else ""
            print(f"  ~ {sid:26} {arrow}{tail}")
        print()
    if dropped:
        print(f"DISAPPEARED ({len(dropped)}) — upstream stopped returning these")
        for sid in dropped:
            n, e = span(before[sid])
            print(f"  - {sid:26} was {n} obs, through {e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
