#!/usr/bin/env python3
"""Compile a LaTeX project and stage build artifacts for log analysis.

This wrapper runs the user's chosen engine (latexmk by default) and copies the
.log into build/ for downstream parsing. It does NOT auto-fix anything.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def die(msg: str, code: int = 1) -> None:
    print(f"Error: {msg}", file=sys.stderr)
    raise SystemExit(code)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Compile a LaTeX project and copy the log to build/.")
    p.add_argument("--root", required=True, help="Path to the main .tex file.")
    p.add_argument("--engine", default="latexmk", choices=("latexmk", "pdflatex", "xelatex"))
    p.add_argument("--build-dir", default="build", help="Where to stage outputs.")
    p.add_argument("--passes", type=int, default=2, help="Compile passes when not using latexmk.")
    p.add_argument("--extra", default="", help="Extra args appended to the engine.")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root)
    if not root.exists():
        die(f"Root tex not found: {root}")
    build = Path(args.build_dir)
    build.mkdir(parents=True, exist_ok=True)

    tex_dir = root.parent
    job = root.stem
    extra = args.extra.split() if args.extra else []

    if args.engine == "latexmk":
        cmd = ["latexmk", "-pdf", "-interaction=nonstopmode",
               f"-output-directory={build.resolve()}", *extra, str(root)]
        rc = subprocess.run(cmd, cwd=tex_dir).returncode
    else:
        cmd_base = [args.engine, "-interaction=nonstopmode",
                    f"-output-directory={build.resolve()}", *extra, str(root)]
        rc = 0
        for _ in range(max(1, args.passes)):
            rc = subprocess.run(cmd_base, cwd=tex_dir).returncode

    log_src = build / f"{job}.log"
    if not log_src.exists():
        # latexmk sometimes places log next to source.
        alt = tex_dir / f"{job}.log"
        if alt.exists():
            shutil.copy2(alt, log_src)
    if not log_src.exists():
        die(f"No log file produced. Engine returned {rc}.")
    print(f"Wrote {log_src}")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
