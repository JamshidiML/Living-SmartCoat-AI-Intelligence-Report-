from __future__ import annotations

from html import escape
from pathlib import Path
import re

import markdown
import yaml
from weasyprint import CSS, HTML

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "report" / "report_manifest.yaml"
STYLE = ROOT / "styles" / "report.css"
OUTPUT_DIR = ROOT / "dist"
OUTPUT = OUTPUT_DIR / "SmartCoat_AI_Intelligence_Report_2026.pdf"
ARABIC_SCRIPT = re.compile(r"[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]")


def split_front_matter(text: str) -> tuple[dict[str, str], str]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, flags=re.DOTALL)
    if not match:
        return {}, text
    metadata = yaml.safe_load(match.group(1)) or {}
    return metadata, match.group(2)


def read_manifest() -> dict:
    if not MANIFEST.exists():
        raise FileNotFoundError(f"Missing report manifest: {MANIFEST}")
    manifest = yaml.safe_load(MANIFEST.read_text(encoding="utf-8")) or {}
    sources = list(manifest.get("sources", []))
    appendices = list(manifest.get("appendices", []))
    if not sources:
        raise ValueError("Report manifest must define at least one source.")
    manifest["ordered_sources"] = sources + appendices
    return manifest


def read_sources(manifest: dict) -> tuple[dict[str, str], str]:
    metadata: dict[str, str] = {}
    bodies: list[str] = []

    for index, relative_path in enumerate(manifest["ordered_sources"]):
        path = ROOT / relative_path
        if not path.exists():
            raise FileNotFoundError(f"Manifest source does not exist: {relative_path}")
        source_metadata, body = split_front_matter(path.read_text(encoding="utf-8"))
        if index == 0:
            metadata = source_metadata
            bodies.append(body.strip())
            bodies.append('\n<div class="page-break"></div>\n# Table of Contents\n[TOC]')
        else:
            bodies.append(f'\n<div class="page-break"></div>\n{body.strip()}')

    return metadata, "\n\n".join(bodies)


def apply_rtl_direction(html: str) -> str:
    def add_direction(match: re.Match[str]) -> str:
        tag = match.group(1)
        attrs = match.group(2) or ""
        content = match.group(3)
        if ARABIC_SCRIPT.search(re.sub(r"<[^>]+>", "", content)):
            if "dir=" not in attrs:
                attrs += ' dir="rtl" class="persian"'
        return f"<{tag}{attrs}>{content}</{tag}>"

    return re.sub(
        r"<(p|li)([^>]*)>(.*?)</\1>",
        add_direction,
        html,
        flags=re.DOTALL | re.IGNORECASE,
    )


def build_html(metadata: dict[str, str], body_markdown: str) -> str:
    body = markdown.markdown(
        body_markdown,
        extensions=["extra", "toc", "sane_lists", "tables"],
        extension_configs={"toc": {"permalink": False, "toc_depth": "1-3"}},
        output_format="html5",
    )
    body = apply_rtl_direction(body)

    title = escape(str(metadata.get("title", "SmartCoat AI Intelligence Report 2026")))
    subtitle = escape(str(metadata.get("subtitle", "")))
    version = escape(str(metadata.get("version", "unversioned")))
    updated = escape(str(metadata.get("updated", "")))
    status = escape(str(metadata.get("status", "")))

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{title}</title>
</head>
<body>
  <section class="cover">
    <div class="eyebrow">LIVING STRATEGIC INTELLIGENCE OFFICE</div>
    <h1>{title}</h1>
    <h2>{subtitle}</h2>
    <div class="cover-meta">
      <p><strong>Version:</strong> {version}</p>
      <p><strong>Updated:</strong> {updated}</p>
      <p><strong>Status:</strong> {status}</p>
    </div>
    <p class="cover-note">Independent public-source intelligence repository. Separate from the SmartCoat product codebase.</p>
  </section>
  <section class="report-body">{body}</section>
</body>
</html>"""


def main() -> None:
    if not STYLE.exists():
        raise FileNotFoundError(f"Missing report stylesheet: {STYLE}")

    manifest = read_manifest()
    metadata, body_markdown = read_sources(manifest)
    html = build_html(metadata, body_markdown)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    HTML(string=html, base_url=str(ROOT)).write_pdf(
        str(OUTPUT),
        stylesheets=[CSS(filename=str(STYLE))],
    )
    print(
        f"Built {OUTPUT.relative_to(ROOT)} from "
        f"{len(manifest['ordered_sources'])} managed source files."
    )


if __name__ == "__main__":
    main()
