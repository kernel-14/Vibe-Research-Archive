#!/usr/bin/env python3
"""Render a paper-style figure using a layered prompt template + style preset.

This script ships with NO hardcoded provider URL or API key. Configure via:

    OPENAI_API_KEY=...
    OPENAI_BASE_URL=...           # optional, only when using a custom endpoint
    PAPER_FIGURE_STUDIO_MODEL=... # optional, defaults to gpt-image-2

Or supply a project-local `.env`. Or pass --api-key/--base-url at the CLI.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.request import urlopen


DEFAULT_MODEL = "gpt-image-2"
DEFAULT_QUALITY = "high"
DEFAULT_OUTPUT_FORMAT = "png"
DEFAULT_ENV_FILE = ".env"
SKILL_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = SKILL_ROOT / "assets" / "templates"
STYLE_DIR = SKILL_ROOT / "assets" / "styles"

FIGURE_TYPES = ("architecture", "roadmap", "schema", "chart", "tracks", "generic")

DEFAULT_SIZE_BY_TYPE = {
    "architecture": "2048x1152",
    "roadmap": "2048x1152",
    "schema": "1024x1536",
    "chart": "2048x1152",
    "tracks": "2048x1152",
    "generic": "1536x1024",
}

DEFAULT_ASPECT_BY_TYPE = {
    "architecture": "wide landscape, around 16:9",
    "roadmap": "wide landscape, around 16:9",
    "schema": "portrait card or square schema layout",
    "chart": "landscape chart, around 4:3",
    "tracks": "wide landscape, around 16:9",
    "generic": "balanced 3:2 landscape",
}

DEFAULT_AVOID = (
    "watermarks; illegible tiny text; overlapping labels; thick tangled arrows; "
    "unexplained abbreviations; decorative clutter; photorealism; 3D; bokeh; "
    "giant gradient blobs"
)


def die(msg: str, code: int = 1) -> None:
    print(f"Error: {msg}", file=sys.stderr)
    raise SystemExit(code)


def read_text(value: Optional[str], file_value: Optional[str], label: str) -> str:
    if value and file_value:
        die(f"Use --{label} or --{label}-file, not both.")
    if file_value:
        path = Path(file_value)
        if not path.exists():
            die(f"{label} file not found: {path}")
        return path.read_text(encoding="utf-8").strip()
    if value:
        return value.strip()
    die(f"Missing --{label} or --{label}-file.")
    return ""


def parse_env_file(path: Path) -> Dict[str, str]:
    out: Dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        if "=" not in line:
            continue
        k, v = line.split("=", 1)
        k, v = k.strip(), v.strip()
        if not k:
            continue
        if len(v) >= 2 and v[0] == v[-1] and v[0] in {"'", '"'}:
            v = v[1:-1]
        out[k] = v
    return out


def resolve_env_file(explicit: Optional[str]) -> Optional[Path]:
    if explicit:
        p = Path(explicit)
        if not p.exists():
            die(f"Env file not found: {p}")
        return p
    env_override = os.getenv("PAPER_FIGURE_STUDIO_ENV_FILE")
    if env_override:
        p = Path(env_override)
        if not p.exists():
            die(f"Env file not found: {p}")
        return p
    cwd = Path.cwd() / DEFAULT_ENV_FILE
    return cwd if cwd.exists() else None


def pick(
    *,
    explicit: Optional[str],
    env_names: List[str],
    file_values: Dict[str, str],
    default: Optional[str] = None,
    explicit_source: str,
) -> Dict[str, Optional[str]]:
    if explicit:
        return {"value": explicit, "source": explicit_source}
    for n in env_names:
        v = os.getenv(n)
        if v:
            return {"value": v, "source": f"env:{n}"}
    for n in env_names:
        v = file_values.get(n)
        if v:
            return {"value": v, "source": f"file:{n}"}
    return {"value": default, "source": "default" if default is not None else None}


def output_paths(out: Path, count: int, fmt: str) -> List[Path]:
    suffix = out.suffix or f".{fmt}"
    norm = suffix.lower().lstrip(".")
    allowed = {fmt} | ({"jpg"} if fmt == "jpeg" else set())
    if norm not in allowed:
        die(f"Output suffix {suffix} does not match --output-format {fmt}.")
    if count == 1:
        return [out if out.suffix else out.with_suffix(suffix)]
    base = out if out.suffix else out.with_suffix(suffix)
    return [base.with_name(f"{base.stem}_{i}{base.suffix}") for i in range(1, count + 1)]


def prompt_copy_path(out: Path, explicit: Optional[str]) -> Path:
    if explicit:
        return Path(explicit)
    base = out if out.suffix else out.with_suffix(f".{DEFAULT_OUTPUT_FORMAT}")
    return base.with_name(f"{base.stem}_prompt.md")


def load_style(style: str) -> Dict[str, Any]:
    path = STYLE_DIR / f"{style}.yaml"
    if not path.exists():
        die(f"Style preset not found: {path}")
    try:
        import yaml  # type: ignore
    except ImportError:
        die("PyYAML is required. Install with: pip install pyyaml")
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def render_style_block(style: Dict[str, Any], font_override: Optional[str], palette_override: Optional[str]) -> str:
    palette = style.get("palette", {})
    font = style.get("font", {})
    line = style.get("line", {})
    icon = style.get("icon", "flat")
    bg = style.get("background", "clean")
    label_font = font_override or font.get("label", "Inter")
    accents = ", ".join(f"{k}={v}" for k, v in palette.items())
    if palette_override:
        accents = f"{palette_override} (override). " + accents
    return (
        f"- Palette accents: {accents}\n"
        f"- Label font: {label_font} (fallback: {font.get('fallback', 'Arial')})\n"
        f"- Line weight: {line.get('weight', 'thin')}; arrow style: {line.get('arrow', 'thin')}\n"
        f"- Icon style: {icon}\n"
        f"- Background: {bg}\n"
        f"- Motion: {style.get('motion', 'none')}\n"
        f"- Notes: {style.get('notes', '')}"
    )


def render_template(template: str, ctx: Dict[str, str]) -> str:
    out = template
    for k, v in ctx.items():
        out = out.replace("{{" + k + "}}", v)
    return out.strip() + "\n"


def build_prompt(args: argparse.Namespace) -> str:
    request = read_text(args.prompt, args.prompt_file, "prompt")
    if args.no_template:
        return request + "\n"

    base_path = TEMPLATE_DIR / "figure-base.md"
    type_path = TEMPLATE_DIR / f"{args.figure_type}.md"
    if not base_path.exists():
        die(f"Base template missing: {base_path}")
    if not type_path.exists():
        die(f"Figure-type template missing: {type_path}")

    layout = args.layout or type_path.read_text(encoding="utf-8").strip()
    style = load_style(args.style)
    style_block = render_style_block(style, args.font, args.palette)

    required_lines = []
    for item in args.text or []:
        required_lines.append(f"- {item}")
    if args.text_file:
        for line in Path(args.text_file).read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line:
                required_lines.append(f"- {line}")
    required_text = "\n".join(required_lines) or (
        "Use only the labels required by the figure request. Keep all text short, exact, and readable."
    )

    avoid = args.avoid or DEFAULT_AVOID
    if args.forbid_text:
        forbid = "; ".join(args.forbid_text)
        avoid = f"{avoid}; do NOT render the following strings anywhere in the figure: {forbid}"

    ctx = {
        "figure_request": request,
        "figure_title": args.title or "Use a short descriptive title only if it helps the figure.",
        "figure_type": args.figure_type,
        "layout_guidance": layout,
        "required_text": required_text,
        "aspect_ratio": args.aspect_ratio or DEFAULT_ASPECT_BY_TYPE[args.figure_type],
        "avoid": avoid,
        "style_notes": args.style_notes or "Keep the style consistent across figures in the same paper.",
        "style_block": style_block,
    }
    return render_template(base_path.read_text(encoding="utf-8"), ctx)


def item_to_dict(item: Any) -> Dict[str, Any]:
    if isinstance(item, dict):
        return item
    if hasattr(item, "model_dump"):
        return item.model_dump()
    out: Dict[str, Any] = {}
    for k in ("b64_json", "url"):
        v = getattr(item, k, None)
        if v:
            out[k] = v
    return out


def image_bytes(item: Any) -> bytes:
    d = item_to_dict(item)
    if d.get("b64_json"):
        return base64.b64decode(d["b64_json"])
    if d.get("url"):
        with urlopen(d["url"], timeout=120) as resp:
            return resp.read()
    die("Image response did not contain b64_json or url.")
    return b""


def write_outputs(result: Any, paths: List[Path], force: bool) -> None:
    data = getattr(result, "data", None)
    if data is None and isinstance(result, dict):
        data = result.get("data")
    if not data:
        die("Image response did not contain data.")
    if len(data) < len(paths):
        die(f"Expected {len(paths)} image(s), got {len(data)}.")
    for item, path in zip(data, paths):
        if path.exists() and not force:
            die(f"Output already exists: {path} (use --force to overwrite)")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(image_bytes(item))
        print(f"Wrote {path}")


def create_client(api_key: str, base_url: Optional[str]) -> Any:
    try:
        from openai import OpenAI
    except ImportError:
        die("openai SDK not installed. Try: pip install openai")
    kwargs: Dict[str, str] = {"api_key": api_key}
    if base_url:
        kwargs["base_url"] = base_url
    return OpenAI(**kwargs)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Render a paper figure with a layered prompt + style preset.")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--prompt", help="Figure request text.")
    g.add_argument("--prompt-file", help="Path to a file containing the figure request.")

    p.add_argument("--api-key", help="API key. Prefer OPENAI_API_KEY env var.")
    p.add_argument("--base-url", help="API base URL. Prefer OPENAI_BASE_URL env var.")
    p.add_argument("--env-file", help="Custom .env path.")
    p.add_argument("--model", help=f"Image model. Defaults to {DEFAULT_MODEL}.")
    p.add_argument("--out", default="fig/paper_figure.png")
    p.add_argument("--n", type=int, default=1)
    p.add_argument("--size")
    p.add_argument("--quality", default=DEFAULT_QUALITY, choices=("low", "medium", "high", "auto"))
    p.add_argument("--output-format", default=DEFAULT_OUTPUT_FORMAT, choices=("png", "jpeg", "webp"))
    p.add_argument("--force", action="store_true")
    p.add_argument("--dry-run", action="store_true")

    p.add_argument("--figure-type", default="generic", choices=FIGURE_TYPES)
    p.add_argument("--style", default="default", help="Style preset key under assets/styles/")
    p.add_argument("--palette", help="Palette key (free-form note for the model)")
    p.add_argument("--font", help="Override label font, e.g. 'Comic Sans MS'")
    p.add_argument("--title")
    p.add_argument("--layout", help="Override layout guidance for this run.")
    p.add_argument("--aspect-ratio")
    p.add_argument("--text", action="append", default=[], help="Required in-figure text. Repeatable.")
    p.add_argument("--text-file", help="File containing required text, one per line.")
    p.add_argument("--forbid-text", action="append", default=[], help="Strings the model must NOT render.")
    p.add_argument("--avoid", help="Override the generic 'avoid' block.")
    p.add_argument("--style-notes")
    p.add_argument("--no-template", action="store_true")
    p.add_argument("--prompt-copy", help="Where to save the final composed prompt.")
    p.add_argument("--no-save-prompt", action="store_true")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    if args.n < 1 or args.n > 10:
        die("--n must be between 1 and 10.")

    env_file = resolve_env_file(args.env_file)
    file_values = parse_env_file(env_file) if env_file else {}

    api_key_pick = pick(
        explicit=args.api_key,
        env_names=["OPENAI_API_KEY", "PAPER_FIGURE_STUDIO_API_KEY"],
        file_values=file_values,
        default=None,
        explicit_source="arg:api-key",
    )
    base_url_pick = pick(
        explicit=args.base_url,
        env_names=["OPENAI_BASE_URL", "PAPER_FIGURE_STUDIO_BASE_URL"],
        file_values=file_values,
        default=None,
        explicit_source="arg:base-url",
    )
    model_pick = pick(
        explicit=args.model,
        env_names=["PAPER_FIGURE_STUDIO_MODEL"],
        file_values=file_values,
        default=DEFAULT_MODEL,
        explicit_source="arg:model",
    )

    size = args.size or DEFAULT_SIZE_BY_TYPE[args.figure_type]
    out = Path(args.out)
    paths = output_paths(out, args.n, args.output_format)
    prompt = build_prompt(args)

    payload = {
        "model": model_pick["value"] or DEFAULT_MODEL,
        "prompt": prompt,
        "n": args.n,
        "size": size,
        "quality": args.quality,
        "output_format": args.output_format,
    }

    if args.dry_run:
        print(json.dumps({
            "runtime": {
                "env_file": str(env_file) if env_file else None,
                "api_key_available": bool(api_key_pick["value"]),
                "api_key_source": api_key_pick["source"],
                "base_url_available": bool(base_url_pick["value"]),
                "base_url_source": base_url_pick["source"],
                "model": payload["model"],
                "model_source": model_pick["source"],
                "style": args.style,
            },
            "outputs": [str(p) for p in paths],
            "prompt_preview_first_400": prompt[:400],
        }, indent=2, ensure_ascii=False))
        return 0

    api_key = api_key_pick["value"]
    if not api_key:
        die("Missing API key. Set OPENAI_API_KEY or PAPER_FIGURE_STUDIO_API_KEY, or pass --api-key.")
    base_url = base_url_pick["value"]

    if not args.no_save_prompt:
        cp = prompt_copy_path(out, args.prompt_copy)
        if cp.exists() and not args.force:
            die(f"Prompt copy already exists: {cp} (use --force to overwrite)")
        cp.parent.mkdir(parents=True, exist_ok=True)
        cp.write_text(prompt, encoding="utf-8")
        print(f"Wrote {cp}")

    client = create_client(api_key, base_url)
    print("Calling Image API. This can take a couple of minutes.", file=sys.stderr)
    result = client.images.generate(**payload)
    write_outputs(result, paths, args.force)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
