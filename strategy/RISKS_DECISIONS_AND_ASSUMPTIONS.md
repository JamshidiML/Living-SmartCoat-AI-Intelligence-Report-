# Risks, Decisions and Assumptions

## Confirmed decisions

### D-001 — Repository separation

This intelligence office remains fully separate from `smartcoat-intelligence`.

**Reason:** Different security boundary, lifecycle and purpose. This repository contains public intelligence and strategic analysis; the SmartCoat product repository contains software architecture and implementation.

### D-002 — Germany-first validation

The first production-relevant proof should be executed in Germany before major international expansion outreach.

**Reason:** Direct industrial access, policy fit and stronger credibility for later EU and Gulf partnerships.

### D-003 — Human-supervised inspection

The first vision pilot operates in shadow mode and cannot autonomously stop production.

**Reason:** Safety, label uncertainty, regulation and the need to establish false-alarm and missed-defect performance.

### D-004 — Model and hardware independence

SmartCoat's knowledge, data model and workflows must not depend on one model provider, cloud or accelerator.

### D-005 — Domain data is the moat

The strategic asset is the governed connection among materials, formulations, process conditions, visual evidence, QC decisions and performance tests.

## Top risks

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---:|---:|---|
| R-001 | Historical data are incomplete or inconsistent | High | High | Knowledge Capture Gatekeeper, identifier normalisation and data-quality scoring |
| R-002 | QC labels are subjective | High | High | Inspector-agreement study and severity ontology |
| R-003 | Vision model overfits one fabric or lighting setup | High | High | Product-wise splits, cross-scenario tests and shadow deployment |
| R-004 | Unknown defects are forced into known classes | High | High | Open-world/anomaly routing and human review |
| R-005 | False alarms create production resistance | High | High | Severity grading and false alarms per 1,000 metres KPI |
| R-006 | External model or cloud lock-in | Medium | High | Adapter layer, open-weight evaluation and local deployment option |
| R-007 | AI Act documentation begins too late | Medium | High | System cards and audit evidence from pilot start |
| R-008 | Intelligence repository receives confidential data | Medium | Critical | Public-intelligence-only policy and repository boundary review |
| R-009 | Gulf expansion begins before evidence | Medium | Medium | German proof gate and partner-readiness checklist |
| R-010 | Weekly report grows without improving decisions | Medium | Medium | Monthly consolidation, duplicate removal and action tracking |

## Critical assumptions to validate

1. Existing ELSIS images can be legally and technically exported for model development.
2. Defects can be linked to trustworthy QC dispositions.
3. Production timestamps and line positions can be aligned across systems.
4. At least one defect category has enough examples for a supervised baseline.
5. Unknown/anomaly detection produces operational value beyond existing alarms.
6. The factory accepts a non-controlling shadow pilot.
7. SmartCoat can demonstrate value without ingesting confidential data into external model providers.

## Monthly decision questions

- Did any new evidence change the Germany-first sequence?
- Has a competitor entered technical-textile materials intelligence?
- Are open-world inspection methods production-ready enough to change the pilot architecture?
- Which funding programmes now match a defined pilot rather than a generic vision?
- Which assumptions have moved from unknown to validated or rejected?
- Which recommended actions were completed, delayed or abandoned?

## Escalation triggers

Immediately update this register when:

- A major inspection vendor launches a directly competing open-world textile product.
- EU guidance changes the likely risk classification of SmartCoat use cases.
- A pilot shows unacceptable critical-defect misses.
- A partner requests ownership of data, ontology or derived industrial knowledge.
- A major funding or partnership opportunity has a deadline within 60 days.