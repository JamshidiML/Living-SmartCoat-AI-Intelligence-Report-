# Risks, Decisions and Assumptions

## Confirmed decisions

### D-001 — Repository separation
This intelligence office remains fully separate from `smartcoat-intelligence`.

### D-002 — Germany-first validation
The first production-relevant proof should be executed in Germany before major international expansion outreach.

### D-003 — Human-supervised inspection
The first vision pilot operates in shadow mode and cannot autonomously stop production.

### D-004 — Model, cloud, accelerator and runtime independence
SmartCoat's knowledge, data model and workflows must not depend on one provider or deployment stack.

### D-005 — Domain data is the moat
The strategic asset is the governed connection among materials, formulations, process conditions, visual evidence, QC decisions and performance tests.

### D-006 — Operational compliance evidence
Every AI pilot must generate a versioned, machine-readable system card, decision-boundary record, human-oversight evidence and incident/change log from the start.

### D-007 — Experiment lineage before formulation AI
No formulation recommender should be promoted until the chain `objective -> formulation -> process -> observation -> test -> decision -> next hypothesis` is machine-readable and testable.

### D-008 — Factory integration depth is a moat metric
The project should measure how deeply each AI event is connected to process variables, operator actions, QC decisions and downstream test outcomes.

### D-009 — Action authority is explicit provenance
Every AI event must state whether the system may observe, recommend, require human approval, or is prohibited from autonomous action. Stop-line and reject authority remain prohibited in the first inspection pilot.

### D-010 — Supply resilience is part of materials intelligence
Supplier origin, substitution class, criticality, lead time, regulatory status and geopolitical exposure should be represented alongside technical performance.

## Top risks

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---:|---:|---|
| R-001 | Historical data are incomplete or inconsistent | High | High | Knowledge Capture Gatekeeper, identifier normalisation and data-quality scoring |
| R-002 | QC labels are subjective | High | High | Inspector-agreement study and severity ontology |
| R-003 | Vision model overfits one fabric or lighting setup | High | High | Product-wise splits, cross-scenario tests and shadow deployment |
| R-004 | Unknown defects are forced into known classes | High | High | Open-world/anomaly routing and human review |
| R-005 | False alarms create production resistance | High | High | Severity grading and false alarms per 1,000 metres KPI |
| R-006 | External model, cloud or accelerator lock-in | Medium | High | Adapter layer, dual-runtime acceptance benchmark and local deployment option |
| R-007 | AI Act evidence is incomplete or retrospective | Medium | High | Machine-readable system cards, decision boundaries and continuous audit evidence |
| R-008 | Intelligence repository receives confidential data | Medium | Critical | Public-intelligence-only policy and repository boundary review |
| R-009 | Gulf expansion begins before evidence | Medium | Medium | German proof gate and partner-readiness checklist |
| R-010 | Weekly report grows without improving decisions | Medium | Medium | Monthly consolidation, duplicate removal and action tracking |
| R-011 | Scientific-AI enthusiasm causes premature autonomous R&D | Medium | High | Experiment-contract gate, human review and staged autonomy |
| R-012 | AI system is accurate but weakly integrated into factory decisions | Medium | High | Integration-depth KPI and workflow acceptance tests |
| R-013 | Full-stack physical-AI vendors create hidden switching costs | Medium | High | Modular interfaces, exportable evidence and dual-runtime validation |
| R-014 | AI recommends technically strong but supply-fragile materials | Medium | High | Supplier-risk ontology and resilience-adjusted formulation criteria |
| R-015 | Action permissions are ambiguous or drift during deployment | Medium | Critical | Versioned `action_authority`, enforcement tests and human approval gates |

## Critical assumptions to validate

1. Existing ELSIS images can be legally and technically exported for model development.
2. Defects can be linked to trustworthy QC dispositions.
3. Production timestamps and line positions can be aligned across systems.
4. At least one defect category has enough examples for a supervised baseline.
5. Unknown/anomaly detection produces operational value beyond existing alarms.
6. The factory accepts a non-controlling shadow pilot.
7. SmartCoat can demonstrate value without ingesting confidential data into external model providers.
8. A frozen benchmark can be reproduced on at least two inference runtime paths without unacceptable accuracy or latency loss.
9. Laboratory experiments can be represented with a stable machine-readable lineage contract.
10. Supplier criticality and substitution attributes can be maintained with sufficient quality to influence decisions.

## Monthly decision questions

- Did any new evidence change the Germany-first sequence?
- Has a competitor entered technical-textile materials intelligence?
- Are open-world inspection methods production-ready enough to change the pilot architecture?
- Which funding programmes now match a defined pilot rather than a generic vision?
- Which assumptions have moved from unknown to validated or rejected?
- Which recommended actions were completed, delayed or abandoned?
- Is factory integration depth increasing, or are we only improving benchmark metrics?
- Are action-authority rules still correct and enforced after every model or workflow change?
- Is supplier resilience changing the ranking of any candidate material or formulation?

## Escalation triggers

Immediately update this register when:

- A major inspection vendor launches a directly competing open-world textile product.
- EU guidance changes the likely risk classification or evidence requirements for SmartCoat use cases.
- A pilot shows unacceptable critical-defect misses.
- A partner requests ownership of data, ontology or derived industrial knowledge.
- A major funding or partnership opportunity has a deadline within 60 days.
- A scientific-AI or materials platform enters polymers, coatings or technical-textile workflows.
- A full-stack vendor requires exclusivity or prevents export of model/evidence records.
- A critical raw material becomes constrained, sanctioned, discontinued or materially more expensive.