# SmartCoat 90-Day Strategic Action Roadmap

## Objective

Convert intelligence findings into one measurable German industrial pilot while preserving the separation between this intelligence repository and the SmartCoat software repository.

# Days 0–30 — Define and prepare

## 1. Select the pilot

**Recommended pilot:** Shadow-mode textile surface inspection using existing ELSIS imagery.

**Business question:** Can AI reduce false alarms, route unknown defects and classify operational severity without creating unsafe automated decisions?

**Success metrics:** unknown-defect recall, known-defect macro F1, false alarms per 1,000 metres, missed critical defects, QC severity agreement, inference latency, model footprint, estimated scrap/stop-time effect, integration depth and portability.

## 2. Establish the data contract

Record camera/lighting configuration, product/fabric/coating identifiers, timestamp/line position, alarm and defect labels, QC disposition, final test result, hardware/runtime/model/preprocessing provenance, `action_authority`, data owner and retention rule. No confidential factory data belongs in this intelligence repository.

## 3. Define the defect and severity ontology

Include known defect type, unknown anomaly, informational, monitor, rework, reject and stop-line. Conduct an inspector-agreement exercise before training.

## 4. Operationalise the AI system card

Document intended/excluded use, data provenance, hardware/runtime/model/preprocessing version, decision boundaries, `action_authority`, human review, change process, incident handling, EU AI Act role assessment and AI Pact/sandbox readiness.

## 5. Define the agent context contract

Before any tool-using industrial agent is piloted, define a machine-readable contract covering approved data sources, retrieval scope, tools, credential/permission boundary, evidence links, action authority, human owner, logging and revocation.

## 6. Define the experiment contract

Before any formulation recommender, make this chain machine-readable and traceable:

`objective -> formulation -> process -> observation -> test -> decision -> next hypothesis`

## 7. Extend the supplier/material ontology

Add supplier, origin, lead time, substitution class, material criticality, regulatory status, geopolitical exposure and batch-linked performance. Future materials recommendation records must also contain interpretable drivers, uncertainty and linked evidence.

# Days 31–60 — Benchmark and learn

## 1. Imaging benchmark

Compare raw, difference, flat-field corrected, contrast-normalised and frequency-sensitive preprocessing using the same baseline model.

## 2. Model benchmark

Run all candidates on one frozen evaluation set:

- Closed-set detector baseline
- PaDiM-style or equivalent anomaly-detection baseline
- Open-world/unknown routing
- Zero-shot/VLM anomaly route
- Multi-scale detector
- Edge-optimised inference

The zero-shot/VLM route is research-only until it meets the same low-false-alarm acceptance criteria as other candidates.

## 3. Portability benchmark

Reproduce the frozen pipeline on at least two inference runtime or accelerator paths. Record accuracy delta, latency, memory, energy estimate, packaging effort and vendor-specific dependencies. Maintain an explicit dependency inventory for inference libraries, drivers, accelerator-specific operators and conversion steps.

## 4. Synthetic-data experiment

Generate a small expert-reviewed set of rare defects and compare curated synthetic samples with uncontrolled bulk augmentation.

## 5. Knowledge integration

Connect each defect example to product, material, process state, QC decision and test evidence in the SmartCoat data model—not in this intelligence repository.

# Days 61–90 — Validate and package

## 1. Shadow-mode deployment

Run the selected model without controlling production. Enforce `action_authority=autonomous-prohibited` for stop-line and reject decisions in the first pilot.

## 2. Decision review

Promote the pilot only if critical-defect misses remain below the agreed threshold; false alarms improve measurably; severity grading is reproducible; human override and audit logging work; action-authority rules are enforced; the alternative runtime passes; and consequential recommendations can be reconstructed from evidence.

## 3. Funding and partnership package

Prepare a two-page German pilot result, technical architecture, AI system card/evidence pack, agent-context template, data-governance summary, portability benchmark, supplier-resilience model, ROI estimate, EIC/Horizon/Fraunhofer fit and Gulf expansion hypothesis.

# Ownership model

| Workstream | Primary owner | Intelligence-office contribution |
|---|---|---|
| Factory problem and success criteria | R&D / QC | Market and research benchmark |
| Data access and labelling | Factory stakeholders | Ontology and evidence template |
| Model development | SmartCoat technical project | Research radar and architecture risks |
| Compliance | Product owner / legal support | Regulatory radar and system-card template |
| Funding and partnerships | Founder | Programme and regional intelligence |

# Stop conditions

Pause or redesign the pilot if data cannot be linked to trustworthy QC outcomes; inspector agreement is too low; autonomous stop-line control is expected in phase one; recommendations cannot be reconstructed; the pipeline is locked to one proprietary inference stack without accepted reason; an agent cannot be bounded by a context/tool/permission contract; confidential factory data would enter this intelligence repository; or a vendor requires exclusive ownership of industrial data or knowledge.