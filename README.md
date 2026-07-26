# Living SmartCoat AI Intelligence Report

A continuously maintained intelligence system for SmartCoat covering:

- AI for materials discovery
- Computer vision and industrial inspection
- Technical textiles and advanced materials
- Industrial AI, digital twins, knowledge graphs and agents
- Startups, venture capital, acquisitions and partnerships
- Research papers and implementation opportunities
- SmartCoat-specific strategic insights and roadmap actions

## Canonical outputs

- Editable source: `report/SmartCoat_AI_Intelligence_Report_2026.md`
- Living PDF: `dist/SmartCoat_AI_Intelligence_Report_2026.pdf`
- Version history: `report/CHANGELOG.md`
- Watch list: `data/watchlist.yaml`

The report is updated as one coherent knowledge base. Existing entries are revised when facts change, duplicates are consolidated, stale items are corrected or retired, and every release records what changed.

## Build locally

```bash
python -m pip install -r requirements.txt
python scripts/build_report.py
```

## Governance

Every factual entry should include:

1. Publication/event date
2. Source title and URL
3. Region and category
4. English summary
5. Persian summary
6. Why it matters for SmartCoat
7. Recommended action
8. Confidence/status marker

Generated PDFs should not be edited manually. Update the Markdown source and rebuild.
