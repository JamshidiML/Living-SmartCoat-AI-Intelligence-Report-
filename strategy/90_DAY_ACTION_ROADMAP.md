# SmartCoat 90-Day Strategic Action Roadmap

## Objective

Convert the intelligence findings into one measurable German industrial pilot while preserving the separation between this intelligence repository and the SmartCoat software repository.

# Days 0–30 — Define and prepare

## 1. Select the pilot

**Recommended pilot:** Shadow-mode textile surface inspection using existing ELSIS imagery.

**Business question:** Can AI reduce false alarms and classify the operational severity of defects without creating unsafe automated decisions?

**Success metrics:**

- Unknown-defect recall
- Known-defect macro F1
- False alarms per 1,000 metres
- Missed critical defects
- Agreement with QC severity rating
- Inference latency
- Estimated scrap and stop-time effect
- Integration depth: linked process variables, operator actions, QC outcomes and final tests per visual event
- Portability: acceptance metrics reproduced on a second inference runtime or accelerator path

## 2. Establish the data contract

- Camera and lighting configuration
- Product, fabric and coating identifiers
- Production timestamp and line position
- Existing alarm and defect labels
- QC disposition and final test result
- Hardware/runtime/model/preprocessing provenance for every benchmark
- `action_authority`: observe, recommend, approval-required or autonomous-prohibited
- Data-access owner and retention rule
- No customer or confidential formulation data in the intelligence repository

## 3. Define the defect and severity ontology

- Known defect type
- Unknown anomaly
- Informational
- Monitor
- Rework
- Reject
- Stop-line

Conduct an inspector-agreement exercise before training.

## 4. Operationalise the AI system card

Document intended use, excluded use, data provenance, hardware/runtime/model/preprocessing version, decision boundaries, `action_authority`, human review, change process, incident handling and EU AI Act risk assessment. Generate these records during the pilot rather than retrospectively.

## 5. Define the experiment contract

Before any formulation recommender, make this chain machine-readable and traceable:

`objective -> formulation -> process -> observation -> test -> decision -> next hypothesis`

## 6. Extend the supplier/material ontology

Add fields for supplier, country of origin, lead time, substitution class, material criticality, regulatory status, geopolitical exposure and batch-linked performance. The goal is to make technical performance and supply resilience jointly queryable.

# Days 31–60 — Benchmark and learn

## 1. Imaging benchmark

Compare raw, difference, flat-field corrected, contrast-normalised and frequency-sensitive preprocessing using the same baseline model.

## 2. Model benchmark

- Closed-set detector baseline
- Anomaly-detection baseline
- Open-world/unknown routing
- Multi-scale detector
- Edge-optimised inference

## 3. Portability benchmark

Freeze one evaluation dataset and acceptance threshold. Reproduce the same pipeline on at least two inference runtime or accelerator paths. Record accuracy delta, latency, memory, energy estimate, packaging effort and vendor-specific dependencies.

## 4. Synthetic-data experiment

Generate a small expert-reviewed set of rare defects. Compare curated synthetic samples with uncontrolled bulk augmentation.

## 5. Knowledge integration

Connect each defect example to product, material, process state, QC decision and test evidence in the SmartCoat data model—not in this intelligence repository.

# Days 61–90 — Validate and package

## 1. Shadow-mode deployment

Run the model without controlling production. Compare model recommendations with inspectors and real outcomes. Enforce `action_authority=autonomous-prohibited` for stop-line and reject decisions in the first pilot.

## 2. Decision review

Promote the pilot only if:

- Critical-defect misses remain below the agreed safety threshold.
- False alarms show measurable improvement.
- Severity grading is reproducible.
- Human override and audit logging work.
- Action-authority rules are enforced and auditable.
- The same acceptance dataset passes the alternative runtime test.
- Consequential recommendations can be reconstructed from data, model and human-decision evidence.
- Compute and maintenance costs are acceptable.

## 3. Funding and partnership package

Prepare:

- Two-page German pilot result
- Technical architecture
- AI system card and evidence pack
- Data-governance summary
- Portability benchmark
- Supplier-resilience data model summary
- ROI estimate
- EIC/Horizon/Fraunhofer fit
- UAE/Saudi/Qatar expansion hypothesis

# Ownership model

| Workstream | Primary owner | Intelligence-office contribution |
|---|---|---|
| Factory problem and success criteria | R&D / QC | Market and research benchmark |
| Data access and labelling | Factory stakeholders | Ontology and evidence template |
| Model development | SmartCoat technical project | Research radar and architecture risks |
| Compliance | Product owner / legal support | Regulatory radar and system-card template |
| Funding and partnerships | Founder | Programme and regional intelligence |

# Stop conditions

Pause or redesign the pilot if:

- Data cannot be linked to trustworthy QC outcomes.
- Inspector agreement is too low to create reliable labels.
- The system is expected to make autonomous stop-line decisions in the first phase.
- A model recommendation cannot be reconstructed from evidence and version history.
- The pipeline can run only on one proprietary inference stack without an accepted reason.
- Confidential factory data would be copied into this intelligence repository.
- A vendor requires exclusive ownership of SmartCoat's industrial data or knowledge layer.