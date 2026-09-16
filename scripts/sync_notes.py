#!/usr/bin/env python3
"""Sync Obsidian course notes into content/notes and static/notes.

Usage: python3 scripts/sync_notes.py [--dry-run] [--report] [--only CODE ...]
                                     [--no-excalidraw] [--force-render] [--check]
                                     [--allow-no-denylist] [--verbose]
The vault is never written to.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from notesync import config as cfglib  # noqa: E402
from notesync import vault as vaultlib  # noqa: E402
from notesync.report import Report  # noqa: E402


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true", help="discover and render but write nothing")
    ap.add_argument("--report", action="store_true", help="print the full report")
    ap.add_argument("--only", action="append", default=[], help="course slug or code (repeatable)")
    ap.add_argument("--no-excalidraw", action="store_true", help="skip rendering; reuse cached SVGs only")
    ap.add_argument("--force-render", action="store_true", help="re-render every Excalidraw drawing")
    ap.add_argument("--check", action="store_true", help="exit non-zero if a sync would change files")
    ap.add_argument("--allow-no-denylist", action="store_true")
    ap.add_argument("--verbose", "-v", action="store_true")
    args = ap.parse_args(argv)

    cfg = cfglib.load()
    report = Report()
    only = {o.lower() for o in args.only} or None
    vault = vaultlib.discover(cfg, only)
    for w in vault.warnings:
        report.add("warnings", w)
    for e in vault.exclusions:
        report.add("excluded", e)
    report.bump("notes discovered", len(vault.notes))
    for n in vault.notes:
        report.bump(f"kind:{n.kind}")

    try:
        from notesync import pipeline
    except ImportError:
        pipeline = None
    if pipeline is None:
        print("(pipeline not available yet: discovery only)")
    else:
        rc = pipeline.run(cfg, vault, report, args)
        if rc:
            print(report.render(args.report or args.verbose))
            return rc

    if args.report or args.verbose or args.dry_run:
        print(report.render(args.report or args.verbose))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
