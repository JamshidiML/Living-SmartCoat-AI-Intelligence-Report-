# Living SmartCoat AI Intelligence Office

An independent, GitHub-backed strategic intelligence system for SmartCoat.

> **Repository boundary:** This repository is intentionally separate from `smartcoat-intelligence`. It contains research, market intelligence, knowledge assets, strategic analysis and generated publications. It must not contain SmartCoat application source code, production data, confidential formulations or factory credentials.

## What ChatGPT maintains

- Global technology and market scouting
- Company and competitor profiles
- Research-paper reviews and implementation assessments
- Germany, EU, United States, UAE, Qatar and Saudi Arabia intelligence
- AI, industrial AI, computer vision, technical textiles and advanced-materials analysis
- Funding, regulation, standards and partnership radars
- SmartCoat opportunity, threat and product-discovery analysis
- Weekly, monthly, quarterly and annual synthesis
- Version history, corrections and evidence traceability

## Repository structure

```text
.
├── governance/             # ChatGPT operating model and editorial controls
├── knowledge/              # Persistent companies, research, technologies, funding, standards
├── intelligence/           # Weekly, monthly and regional intelligence products
├── strategy/               # Opportunities, risks, decisions and action roadmaps
├── data/                   # Structured registries, taxonomy and watch lists
├── templates/              # Reusable analysis templates
├── report/                 # Canonical publication source and manifest
├── scripts/                # Reproducible report build tools
├── styles/                 # PDF styling
└── dist/                   # Generated canonical PDF
```

## Canonical outputs

- Executive source: `report/SmartCoat_AI_Intelligence_Report_2026.md`
- Publication manifest: `report/report_manifest.yaml`
- Living PDF: `dist/SmartCoat_AI_Intelligence_Report_2026.pdf`
- Version history: `report/CHANGELOG.md`
- Structured registry: `data/intelligence_registry.yaml`

## Publication model

ChatGPT updates the evidence-backed Markdown and YAML files. GitHub Actions then builds one coherent PDF from the ordered publication manifest and commits the refreshed PDF to `main`.

```text
Research and verification
        ↓
Knowledge-base updates
        ↓
Strategic synthesis
        ↓
GitHub commit / merge
        ↓
Automated PDF build
        ↓
Canonical living report
```

## Build locally

```bash
python -m pip install -r requirements.txt
python scripts/build_report.py
```

Generated PDFs must not be edited manually. Update the source files and rebuild.