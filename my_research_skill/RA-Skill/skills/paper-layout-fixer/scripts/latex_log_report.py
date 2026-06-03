#!/usr/bin/env python3
"""Parse a LaTeX .log into a categorized human-readable layout report.

Usage:
    python latex_log_report.py build/paper.log --format markdown --out build/report.md
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional


CATEGORIES = (
    "overfull-hbox",
    "underfull-hbox",
    "overfull-vbox",
    "float-too-large",
    "undefined-ref",
    "missing-citation",
    "multiply-defined-label",
    "package-conflict",
    "font-shape",
    "cleveref-mismatch",
    "package-warning",
    "other-warning",
)

PATTERNS = [
    ("overfull-hbox",
     re.compile(r"^Overfull \\hbox \(([\d.]+)pt too wide\)(?:.*?lines? (\d+)(?:--(\d+))?)?", re.M)),
    ("underfull-hbox",
     re.compile(r"^Underfull \\hbox \(badness (\d+)\)(?:.*?lines? (\d+)(?:--(\d+))?)?", re.M)),
    ("overfull-vbox",
     re.compile(r"^Overfull \\vbox \(([\d.]+)pt too high\)", re.M)),
    ("float-too-large",
     re.compile(r"Float too large for page by ([\d.]+)pt", re.M)),
    ("undefined-ref",
     re.compile(r"LaTeX Warning: Reference `([^']+)' on page (\d+) undefined", re.M)),
    ("missing-citation",
     re.compile(r"LaTeX Warning: Citation `([^']+)' on page (\d+) undefined", re.M)),
    ("multiply-defined-label",
     re.compile(r"LaTeX Warning: Label `([^']+)' multiply defined", re.M)),
    ("package-conflict",
     re.compile(r"(Option clash for package|LaTeX Error: Option clash|Package \w+ Error)", re.M)),
    ("font-shape",
     re.compile(r"LaTeX Font Warning: ([^\n]+)", re.M)),
    ("cleveref-mismatch",
     re.compile(r"Package cleveref Warning: ([^\n]+)", re.M)),
    ("package-warning",
     re.compile(r"Package (\w+) Warning: ([^\n]+)", re.M)),
]


def parse_log(text: str) -> List[Dict]:
    findings: List[Dict] = []
    for cat, rx in PATTERNS:
        for m in rx.finditer(text):
            findings.append({
                "category": cat,
                "match": m.group(0).strip()[:240],
                "groups": [g for g in m.groups() if g is not None],
                "offset": m.start(),
            })
    findings.sort(key=lambda f: f["offset"])
    for i, f in enumerate(findings, 1):
        f["id"] = i
    return findings


def severity(category: str, groups: List[str]) -> str:
    if category in ("package-conflict", "missing-citation", "undefined-ref",
                    "multiply-defined-label", "float-too-large"):
        return "high"
    if category in ("overfull-hbox", "overfull-vbox"):
        try:
            excess = float(groups[0]) if groups else 0.0
            return "high" if excess >= 10 else ("medium" if excess >= 3 else "low")
        except ValueError:
            return "medium"
    if category == "underfull-hbox":
        try:
            badness = int(groups[0]) if groups else 0
            return "low" if badness < 5000 else "medium"
        except ValueError:
            return "low"
    return "low"


def render_markdown(findings: List[Dict]) -> str:
    if not findings:
        return "# LaTeX Layout Report\n\nNo warnings detected.\n"
    lines = ["# LaTeX Layout Report", ""]
    by_cat: Dict[str, List[Dict]] = {}
    for f in findings:
        by_cat.setdefault(f["category"], []).append(f)
    counts = ", ".join(f"{k}={len(v)}" for k, v in by_cat.items())
    lines.append(f"**Total findings:** {len(findings)} ({counts})")
    lines.append("")
    for cat in CATEGORIES:
        items = by_cat.get(cat, [])
        if not items:
            continue
        lines.append(f"## {cat} ({len(items)})")
        for f in items:
            sev = severity(cat, f.get("groups", []))
            lines.append(f"- **[{sev}]** {f['match']}")
        lines.append("")
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Categorize a LaTeX .log into a layout report.")
    p.add_argument("log", help="Path to the .log file.")
    p.add_argument("--format", default="markdown", choices=("markdown", "json"))
    p.add_argument("--out", help="Write to this path instead of stdout.")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    log_path = Path(args.log)
    if not log_path.exists():
        print(f"Error: log not found: {log_path}", file=sys.stderr)
        return 1
    text = log_path.read_text(encoding="utf-8", errors="replace")
    findings = parse_log(text)

    out_str: str
    if args.format == "json":
        out_str = json.dumps({"findings": findings}, indent=2, ensure_ascii=False)
    else:
        out_str = render_markdown(findings)

    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(out_str, encoding="utf-8")
        print(f"Wrote {args.out}")
    else:
        sys.stdout.write(out_str)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
