#!/usr/bin/env python3
"""Render a paper-style figure with gpt-image-2 using the bundled prompt template."""

from __future__ import annotations

import argparse
import base64
import json
import os
from pathlib import Path
import sys
from typing import Any, Dict, List, Optional
from urllib.request import urlopen


DEFAULT_MODEL = "gpt-image-2"
DEFAULT_QUALITY = "high"
DEFAULT_OUTPUT_FORMAT = "png"
DEFAULT_ENV_FILE = ".env"
DEFAULT_PROVIDER_API_URL: Optional[str] = None
DEFAULT_PROVIDER_API_KEY: Optional[str] = None

FIGURE_TYPES = ("architecture", "schema", "chart", "tracks", "generic")

DEFAULT_SIZE_BY_TYPE = {
    "architecture": "2048x1152",
    "schema": "1024x1536",
    "chart": "2048x1152",
    "tracks": "2048x1152",
    "generic": "1536x1024",
}

DEFAULT_ASPECT_BY_TYPE = {
    "architecture": "wide landscape, around 3:2 or 16:9, dense but readable",
    "schema": "portrait card or square schema layout",
    "chart": "landscape chart layout, around 4:3 or 3:2",
    "tracks": "landscape or square two-lane method diagram",
    "generic": "balanced paper-figure layout",
}

LAYOUT_GUIDANCE = {
    "architecture": (
        "Use a left-to-right pipeline with large stage cards, compact substeps, "
        "thin connectors, a visible final artifact, and any cross-cutting method lines "
        "drawn as separate tracks."
    ),
    "schema": (
        "Use a compact card-like schema diagram with a clear header, stacked fields, "
        "small pills/tags, generous padding, and no decorative clutter."
    ),
    "chart": (
        "Use a clean academic chart with readable axes, light grid, clear legend, "
        "balanced margins, and subtle markers."
    ),
    "tracks": (
        "Use two or more clean horizontal lanes/tracks with labeled nodes and small "
        "functional icons. Make the independence and coupling between lines easy to read."
    ),
    "generic": (
        "Use a concise explanatory paper-figure composition with clear hierarchy, "
        "functional icons, and tidy labels."
    ),
}

DEFAULT_AVOID = (
    "watermarks; illegible tiny text; overlapping labels; thick tangled arrows; "
    "numbered badges; unexplained abbreviations; decorative clutter; "
    "photorealism; 3D; bokeh; giant gradient blobs"
)


def die(message: str, code: int = 1) -> None:
    print(f"Error: {message}", file=sys.stderr)
    raise SystemExit(code)


def read_text_arg(value: Optional[str], file_value: Optional[str], label: str) -> str:
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


def default_template_path() -> Path:
    return Path(__file__).resolve().parents[1] / "references" / "template-prompt.md"


def parse_env_file(path: Path) -> Dict[str, str]:
    values: Dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            continue
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        values[key] = value
    return values


def resolve_env_file(explicit_env_file: Optional[str]) -> Optional[Path]:
    if explicit_env_file:
        path = Path(explicit_env_file)
        if not path.exists():
            die(f"Env file not found: {path}")
        return path

    env_override = os.getenv("PAPER_FIGURE_IMAGEGEN_ENV_FILE")
    if env_override:
        path = Path(env_override)
        if not path.exists():
            die(f"Env file not found: {path}")
        return path

    cwd_env = Path.cwd() / DEFAULT_ENV_FILE
    if cwd_env.exists():
        return cwd_env
    return None


def pick_setting(
    *,
    explicit: Optional[str],
    env_names: List[str],
    file_values: Dict[str, str],
    default: Optional[str] = None,
    explicit_source: str,
) -> Dict[str, Optional[str]]:
    if explicit:
        return {"value": explicit, "source": explicit_source}

    for name in env_names:
        value = os.getenv(name)
        if value:
            return {"value": value, "source": f"env:{name}"}

    for name in env_names:
        value = file_values.get(name)
        if value:
            return {"value": value, "source": f"file:{name}"}

    return {"value": default, "source": "default" if default is not None else None}


def output_paths(out: Path, count: int, output_format: str) -> List[Path]:
    suffix = out.suffix or f".{output_format}"
    normalized_suffix = suffix.lower().lstrip(".")
    allowed_suffixes = {output_format}
    if output_format == "jpeg":
        allowed_suffixes.add("jpg")
    if normalized_suffix not in allowed_suffixes:
        die(f"Output suffix {suffix} does not match --output-format {output_format}.")
    if count == 1:
        return [out if out.suffix else out.with_suffix(suffix)]
    stem_path = out if out.suffix else out.with_suffix(suffix)
    return [
        stem_path.with_name(f"{stem_path.stem}_{idx}{stem_path.suffix}")
        for idx in range(1, count + 1)
    ]


def prompt_copy_path(out: Path, explicit: Optional[str]) -> Path:
    if explicit:
        return Path(explicit)
    stem_path = out if out.suffix else out.with_suffix(f".{DEFAULT_OUTPUT_FORMAT}")
    return stem_path.with_name(f"{stem_path.stem}_prompt.md")


def render_template(template: str, context: Dict[str, str]) -> str:
    rendered = template
    for key, value in context.items():
        rendered = rendered.replace("{{" + key + "}}", value)
    return rendered.strip() + "\n"


def build_prompt(args: argparse.Namespace) -> str:
    request = read_text_arg(args.prompt, args.prompt_file, "prompt")
    if args.no_template:
        return request + "\n"

    template_path = Path(args.template) if args.template else default_template_path()
    if not template_path.exists():
        die(f"Template not found: {template_path}")

    figure_type = args.figure_type
    required_text = "\n".join(f"- {item}" for item in args.text) if args.text else (
        "Use only the labels required by the figure request. Keep all text short, exact, and readable."
    )
    context = {
        "figure_request": request,
        "figure_title": args.title or "Use a short descriptive title only if it helps the figure.",
        "figure_type": figure_type,
        "layout_guidance": args.layout or LAYOUT_GUIDANCE[figure_type],
        "required_text": required_text,
        "aspect_ratio": args.aspect_ratio or DEFAULT_ASPECT_BY_TYPE[figure_type],
        "avoid": args.avoid or DEFAULT_AVOID,
        "style_notes": args.style_notes or "Keep the style consistent across figures in the same paper.",
    }
    return render_template(template_path.read_text(encoding="utf-8"), context)


def item_to_dict(item: Any) -> Dict[str, Any]:
    if isinstance(item, dict):
        return item
    if hasattr(item, "model_dump"):
        return item.model_dump()
    data: Dict[str, Any] = {}
    for key in ("b64_json", "url"):
        value = getattr(item, key, None)
        if value:
            data[key] = value
    return data


def image_bytes(item: Any) -> bytes:
    data = item_to_dict(item)
    if data.get("b64_json"):
        return base64.b64decode(data["b64_json"])
    if data.get("url"):
        with urlopen(data["url"], timeout=120) as response:
            return response.read()
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
        die("openai SDK is not installed. Install it in the active environment, for example: uv pip install openai")

    kwargs: Dict[str, str] = {"api_key": api_key}
    if base_url:
        kwargs["base_url"] = base_url
    return OpenAI(**kwargs)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a consistent paper-style figure with gpt-image-2."
    )
    prompt_group = parser.add_mutually_exclusive_group(required=True)
    prompt_group.add_argument("--prompt", help="Figure request text.")
    prompt_group.add_argument("--prompt-file", help="Path to a file containing the figure request.")

    parser.add_argument("--api-key", help="API key. Prefer OPENAI_API_KEY for normal use.")
    parser.add_argument("--base-url", help="API base URL. Defaults to OPENAI_BASE_URL or OpenAI default.")
    parser.add_argument("--env-file", help="Path to a .env file to load before reading environment variables.")
    parser.add_argument("--model", help="Image model. Defaults to gpt-image-2.")
    parser.add_argument("--out", default="fig/paper_figure.png")
    parser.add_argument("--n", type=int, default=1)
    parser.add_argument("--size")
    parser.add_argument("--quality", default=DEFAULT_QUALITY, choices=("low", "medium", "high", "auto"))
    parser.add_argument("--output-format", default=DEFAULT_OUTPUT_FORMAT, choices=("png", "jpeg", "webp"))
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true")

    parser.add_argument("--figure-type", default="generic", choices=FIGURE_TYPES)
    parser.add_argument("--title")
    parser.add_argument("--layout")
    parser.add_argument("--aspect-ratio")
    parser.add_argument("--text", action="append", default=[], help="Exact in-figure text. Repeatable.")
    parser.add_argument("--avoid")
    parser.add_argument("--style-notes")
    parser.add_argument("--template", help="Custom template path.")
    parser.add_argument("--no-template", action="store_true")
    parser.add_argument("--prompt-copy", help="Where to save the final composed prompt.")
    parser.add_argument("--no-save-prompt", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.n < 1 or args.n > 10:
        die("--n must be between 1 and 10.")

    env_file = resolve_env_file(args.env_file)
    file_values = parse_env_file(env_file) if env_file else {}

    api_key_pick = pick_setting(
        explicit=args.api_key,
        env_names=["OPENAI_API_KEY", "PAPER_FIGURE_IMAGEGEN_API_KEY"],
        file_values=file_values,
        default=DEFAULT_PROVIDER_API_KEY,
        explicit_source="arg:api-key",
    )
    base_url_pick = pick_setting(
        explicit=args.base_url,
        env_names=["OPENAI_BASE_URL", "PAPER_FIGURE_IMAGEGEN_BASE_URL"],
        file_values=file_values,
        default=DEFAULT_PROVIDER_API_URL,
        explicit_source="arg:base-url",
    )
    model_pick = pick_setting(
        explicit=args.model,
        env_names=["PAPER_FIGURE_IMAGEGEN_MODEL"],
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
        print(
            json.dumps(
                {
                    "runtime": {
                        "env_file": str(env_file) if env_file else None,
                        "api_key_available": bool(api_key_pick["value"]),
                        "api_key_source": api_key_pick["source"],
                        "base_url": base_url_pick["value"],
                        "base_url_source": base_url_pick["source"],
                        "model": payload["model"],
                        "model_source": model_pick["source"],
                    },
                    "outputs": [str(path) for path in paths],
                    **payload,
                },
                indent=2,
                ensure_ascii=False,
            )
        )
        return 0

    api_key = api_key_pick["value"]
    if not api_key:
        die(
            "Missing API key. Set OPENAI_API_KEY, PAPER_FIGURE_IMAGEGEN_API_KEY, or place one in "
            "the current .env file. You can also pass --api-key."
        )
    base_url = base_url_pick["value"]

    if not args.no_save_prompt:
        copy_path = prompt_copy_path(out, args.prompt_copy)
        if copy_path.exists() and not args.force:
            die(f"Prompt copy already exists: {copy_path} (use --force to overwrite)")
        copy_path.parent.mkdir(parents=True, exist_ok=True)
        copy_path.write_text(prompt, encoding="utf-8")
        print(f"Wrote {copy_path}")

    client = create_client(api_key, base_url)
    print("Calling Image API. This can take a couple of minutes.", file=sys.stderr)
    result = client.images.generate(**payload)
    write_outputs(result, paths, args.force)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
