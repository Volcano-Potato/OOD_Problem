#!/usr/bin/env python3

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "outputs" / "run_manifest.csv"
DEFAULT_AGENT_VARIANT = "benchmark_isolated"
NEW_FIELD = "agent_variant"
INSERT_AFTER = "agent_name"


def main() -> None:
    with MANIFEST.open(newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        fieldnames = list(reader.fieldnames or [])

    if NEW_FIELD in fieldnames:
        print(f"{NEW_FIELD} already present in {MANIFEST}")
        return

    try:
        insert_at = fieldnames.index(INSERT_AFTER) + 1
    except ValueError as exc:
        raise SystemExit(f"Could not find {INSERT_AFTER} in manifest header") from exc

    fieldnames.insert(insert_at, NEW_FIELD)
    for row in rows:
        row[NEW_FIELD] = DEFAULT_AGENT_VARIANT

    with MANIFEST.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    print(f"Backfilled {NEW_FIELD} for {len(rows)} manifest rows in {MANIFEST}")


if __name__ == "__main__":
    main()
