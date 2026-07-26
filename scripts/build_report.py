from __future__ import annotations

from pathlib import Path
import re

import markdown
import yaml
from weasyprint import CSS, HTML

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "report" / "SmartCoat_AI_Intelligence_Report_2026.md"
STYLE = ROOT / "styles" / "report.css"
OUTPUT_DIR = ROOT / "dist"
OUTPUT = OUTPUT_DIR / "SmartCoat_AI_Intelligence_Report_2026.pdf"


def split_front_matter(text: str) -> tuple[dict[str, str], str]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, flags=re.DOTALL)
    if not match:
        return {}, text
    metadata = yaml.safe_load(match.group(1)) or {}
    return metadata, match.group(2)


def build_html(metadata: dict[str, str], body_markdown: str) -> str:
    body = markdown.markdown(
        body_markdown,
        extensions=["extra", "toc", "sane_lists", "tables"],
        output_format="html5",
    )
    title = metadata.get("title", "SmartCoat AI Intelligence Report 2026")
    subtitle = metadata.get("subtitle", "")
    version = metadata.get("version", "unversioned")
    updated = metadata.get("updated", "")
    status = metadata.get("status", "")

    return f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\">
  <title>{title}</title>
</head>
<body>
  <section class=\"cover\">
    <div class=\"eyebrow\">LIVING INTELLIGENCE SYSTEM</div>
    <h1>{title}</h1>
    <h2>{subtitle}</h2>
    <div class=\"cover-meta\">
      <p><strong>Version:</strong> {version}</p>
      <p><strong>Updated:</strong> {updated}</p>
      <p><strong>Status:</strong> {status}</p>
    </div>
    <p class=\"cover-note\">A continuously maintained strategic knowledge base for SmartCoat.</p>
  </section>
  <section class=\"report-body\">{body}</section>
</body>
</html>"""


def main() -> None:
    if not SOURCE.exists():
        raise FileNotFoundError(f"Missing report source: {SOURCE}")
    if not STYLE.exists():
        raise FileNotFoundError(f"Missing report stylesheet: {STYLE}")

    metadata, body_markdown = split_front_matter(SOURCE.read_text(encoding="utf-8"))
    html = build_html(metadata, body_markdown)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    HTML(string=html, base_url=str(ROOT)).write_pdf(
        str(OUTPUT),
        stylesheets=[CSS(filename=str(STYLE))],
    )
    print(f"Built {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
