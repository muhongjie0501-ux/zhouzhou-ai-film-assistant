#!/usr/bin/env python3
"""Local-only age check for the Higgsfield evidence snapshot.

This script performs no network requests and never changes the snapshot.
"""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path


STATE_PATH = Path(__file__).resolve().parents[1] / "references" / "platform-state.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check dated Higgsfield evidence without networking.")
    parser.add_argument(
        "--scope",
        default="all",
        help="all or one source key, for example cli, mcp, ui_3_5, or ui_4_0",
    )
    parser.add_argument(
        "--as-of",
        default=date.today().isoformat(),
        help="Date used for the check in YYYY-MM-DD form.",
    )
    parser.add_argument("--json", action="store_true", help="Return machine-readable JSON.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    as_of = date.fromisoformat(args.as_of)
    interval = int(state["review_interval_days"])
    sources = state["sources"]

    if args.scope != "all":
        if args.scope not in sources:
            raise SystemExit(f"Unknown scope: {args.scope}")
        sources = {args.scope: sources[args.scope]}

    overall_status = state.get("refresh_status", "unknown")
    results = []
    for name, record in sources.items():
        stamp = record.get("verified_at") or record.get("checked_at")
        source_status = record.get("status", "unknown")
        if not stamp:
            results.append(
                {
                    "source": name,
                    "freshness": "due",
                    "source_status": source_status,
                    "due": True,
                    "age_days": None,
                }
            )
            continue
        age = (as_of - date.fromisoformat(stamp)).days
        # A partial overall refresh must not make every independently fresh source due.
        # Each source owns its own verification status and age.
        due = source_status != "complete" or age < 0 or age >= interval
        results.append(
            {
                "source": name,
                "freshness": "due" if due else "fresh",
                "source_status": source_status,
                "due": due,
                "age_days": age,
                "verified_at": stamp,
            }
        )

    payload = {
        "as_of": as_of.isoformat(),
        "review_interval_days": interval,
        "refresh_status": overall_status,
        "refresh_due": any(item["due"] for item in results),
        "network_used": False,
        "state_changed": False,
        "sources": results,
    }
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        overall = "DUE" if payload["refresh_due"] else "FRESH"
        details = ", ".join(
            f"{item['source']}={item['freshness']}/{item['source_status']}({item['age_days']}d)"
            if item["age_days"] is not None
            else f"{item['source']}=due/{item['source_status']}"
            for item in results
        )
        print(f"{overall} | interval={interval}d | {details} | network=false | writes=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
