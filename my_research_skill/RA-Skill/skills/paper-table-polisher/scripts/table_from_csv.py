#!/usr/bin/env python3
"""Convert a CSV/Markdown table into a paper-grade LaTeX table.

No external services. Stdlib only.

Examples:
    python table_from_csv.py results.csv --type comparison \
        --best-col-mode max --second-best --label tab:main \
        --caption "Main Results on <Benchmark>." \
        --ours-row 4 --out tab/main.tex
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path
from typing import List, Optional, Tuple


TABLE_TYPES = ("comparison", "ablation", "dataset-stat", "case-taxonomy", "human-eval", "generic")


def die(msg: str, code: int = 1) -> None:
    print(f"Error: {msg}", file=sys.stderr)
    raise SystemExit(code)


def read_csv_rows(path: Path) -> List[List[str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return [row for row in csv.reader(f)]


def read_md_rows(path: Path) -> List[List[str]]:
    rows: List[List[str]] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line.startswith("|"):
            continue
        if re.fullmatch(r"\|[\s\-:|]+\|", line):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        rows.append(cells)
    return rows


def is_number(s: str) -> bool:
    s = s.strip().lstrip("-+")
    if not s:
        return False
    try:
        float(s)
        return True
    except ValueError:
        return False


def col_dtype(rows: List[List[str]], col: int) -> str:
    has_any = False
    all_num = True
    for r in rows[1:]:
        if col >= len(r):
            continue
        v = r[col].strip()
        if not v:
            continue
        has_any = True
        if not is_number(v):
            all_num = False
            break
    return "S" if (has_any and all_num) else "l"


def build_colspec(rows: List[List[str]]) -> str:
    if not rows:
        return "l"
    n = len(rows[0])
    parts: List[str] = []
    for c in range(n):
        parts.append("l" if c == 0 else col_dtype(rows, c))
    return " ".join(parts)


def best_indices(values: List[str], mode: str) -> Tuple[Optional[int], Optional[int]]:
    """Return (best_idx, second_idx). Ties: best=first match, second=next distinct value."""
    nums = [(i, float(v)) for i, v in enumerate(values) if v and is_number(v)]
    if not nums:
        return None, None
    reverse = (mode == "max")
    nums.sort(key=lambda p: p[1], reverse=reverse)
    best_v = nums[0][1]
    best_idx = nums[0][0]
    second_idx: Optional[int] = None
    for idx, val in nums[1:]:
        if val != best_v:
            second_idx = idx
            break
    return best_idx, second_idx


def latex_escape(s: str) -> str:
    return (
        s.replace("\\", r"\textbackslash{}")
         .replace("&", r"\&")
         .replace("%", r"\%")
         .replace("$", r"\$")
         .replace("#", r"\#")
         .replace("_", r"\_")
         .replace("{", r"\{")
         .replace("}", r"\}")
         .replace("~", r"\textasciitilde{}")
         .replace("^", r"\textasciicircum{}")
    )


def cell(value: str, dtype: str, escape: bool) -> str:
    v = value.strip()
    if dtype == "S" and is_number(v):
        return v
    return latex_escape(v) if escape else v


def render_latex(
    rows: List[List[str]],
    *,
    table_type: str,
    label: str,
    caption: str,
    best_col_mode: Optional[str],
    second_best: bool,
    ours_row: Optional[int],
    note: Optional[str],
    escape_text: bool,
) -> str:
    if not rows:
        die("Empty table.")
    header = rows[0]
    body = rows[1:]
    n_cols = len(header)
    colspec = build_colspec(rows)
    dtypes = colspec.split()

    rendered_rows: List[str] = []

    # Header.
    header_cells = [cell(h, "l", escape_text) for h in header]
    rendered_rows.append(" & ".join(header_cells) + r" \\")
    rendered_rows.append(r"\midrule")

    # Compute best/second per numeric column.
    marks_best = [None] * n_cols
    marks_second = [None] * n_cols
    if best_col_mode in ("max", "min"):
        for c in range(n_cols):
            if dtypes[c] != "S":
                continue
            col_values = [r[c] if c < len(r) else "" for r in body]
            b, s = best_indices(col_values, best_col_mode)
            marks_best[c] = b
            marks_second[c] = s if second_best else None

    for r_idx, r in enumerate(body):
        is_ours = ours_row is not None and r_idx == ours_row
        cells_out: List[str] = []
        for c_idx in range(n_cols):
            raw = r[c_idx] if c_idx < len(r) else ""
            v = cell(raw, dtypes[c_idx], escape_text)
            if marks_best[c_idx] == r_idx:
                v = r"\best{" + v + "}"
            elif marks_second[c_idx] == r_idx:
                v = r"\second{" + v + "}"
            cells_out.append(v)
        prefix = r"\rowcolor{RAAccent!12} " if is_ours else ""
        rendered_rows.append(prefix + " & ".join(cells_out) + r" \\")

    rendered_rows.append(r"\bottomrule")

    body_block = "\n    ".join(rendered_rows)
    note_block = f"\n  \\tabnote{{{note}}}" if note else ""

    return (
        "% Generated by paper-table-polisher (table_from_csv.py)\n"
        "% Requires: \\usepackage{booktabs, siunitx, ra-table-style}\n"
        f"\\begin{{table}}[t]\n"
        f"  \\centering\n"
        f"  \\caption{{{caption}}}\n"
        f"  \\label{{{label}}}\n"
        f"  \\begin{{tabular}}{{{colspec}}}\n"
        f"    \\toprule\n"
        f"    {body_block}\n"
        f"  \\end{{tabular}}{note_block}\n"
        f"\\end{{table}}\n"
    )


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Convert CSV/Markdown to a publication-grade LaTeX table.")
    p.add_argument("input", help="Input CSV or Markdown table file.")
    p.add_argument("--type", default="generic", choices=TABLE_TYPES)
    p.add_argument("--label", required=True, help="LaTeX label, e.g. tab:main.")
    p.add_argument("--caption", required=True, help="Caption text.")
    p.add_argument("--best-col-mode", default=None, choices=("max", "min"),
                   help="Highlight best per numeric column. Omit to disable.")
    p.add_argument("--second-best", action="store_true",
                   help="Also mark second-best per numeric column.")
    p.add_argument("--ours-row", type=int, default=None,
                   help="Zero-based body row index for 'Ours'; gets accent tint.")
    p.add_argument("--note", default=None, help="Optional table note (becomes \\tabnote).")
    p.add_argument("--no-escape", action="store_true",
                   help="Disable LaTeX-escaping of text cells (use when input already has LaTeX).")
    p.add_argument("--out", default=None, help="Write to file. Default: stdout.")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    path = Path(args.input)
    if not path.exists():
        die(f"Input not found: {path}")
    if path.suffix.lower() in {".md", ".markdown"}:
        rows = read_md_rows(path)
    else:
        rows = read_csv_rows(path)
    if not rows:
        die("No rows parsed from input.")

    out = render_latex(
        rows,
        table_type=args.type,
        label=args.label,
        caption=args.caption,
        best_col_mode=args.best_col_mode,
        second_best=args.second_best,
        ours_row=args.ours_row,
        note=args.note,
        escape_text=not args.no_escape,
    )
    if args.out:
        outp = Path(args.out)
        outp.parent.mkdir(parents=True, exist_ok=True)
        outp.write_text(out, encoding="utf-8")
        print(f"Wrote {outp}")
    else:
        sys.stdout.write(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
