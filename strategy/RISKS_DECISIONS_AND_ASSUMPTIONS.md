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
No formulation recommender should be promoted until `objective -> formulation -> process -> observation -> test -> decision -> next hypothesis` is machine-readable and testable.

### D-008 — Factory integration depth is a moat metric
Measure how deeply each AI event is connected to process variables, operator actions, QC decisions and downstream test outcomes.

### D-009 — Action authority is explicit provenance
Every AI event must state whether the system may observe, recommend, require human approval, or is prohibited from autonomous action.

### D-010 — Supply resilience is part of materials intelligence
Supplier origin, substitution class, criticality, lead time, regulatory status and geopolitical exposure belong beside technical performance.

### D-011 — Agent context is bounded before execution
Before any industrial agent accesses tools or executes workflows, define approved sources, retrieval scope, tools, permission boundary, evidence links, action authority and human owner.

### D-012 — Zero-shot/VLM anomaly detection is benchmark-only
Zero-shot anomaly methods may enter the frozen benchmark but cannot receive autonomous production authority without low-false-alarm factory validation.

### D-013 — Materials recommendations must be interpretable
Future materials recommendations must expose influential drivers, uncertainty/confidence, constraints and linked experimental evidence.

## Top risks

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---:|---:|---|
| R-001 | Historical data are incomplete or inconsistent | High | High | Knowledge Capture Gatekeeper, identifier normalisation and data-quality scoring |
| R-002 | QC labels are subjective | High | High | Inspector-agreement study and severity ontology |
| R-003 | Vision model overfits one fabric or lighting setup | High | High | Product-wise splits, cross-scenario tests and shadow deployment |
| R-004 | Unknown defects are forced into known classes | High | High | Open-world/anomaly/zero-shot benchmark and human review |
| R-005 | False alarms create production resistance | High | High | Severity grading and false alarms per 1,000 metres KPI |
| R-006 | External model, cloud or accelerator lock-in | Medium | High | Adapter layer, dual-runtime benchmark and dependency inventory |
| R-007 | AI Act evidence is incomplete or retrospective | Medium | High | System cards, provider/deployer role assessment and continuous audit evidence |
| R-008 | Intelligence repository receives confidential data | Medium | Critical | Public-intelligence-only policy and repository boundary review |
| R-009 | Gulf expansion begins before evidence | Medium | Medium | German proof gate and partner-readiness checklist |
| R-010 | Weekly report grows without improving decisions | Medium | Medium | Monthly consolidation, duplicate removal and action tracking |
| R-011 | Scientific-AI enthusiasm causes premature autonomous R&D | Medium | High | Experiment-contract gate, interpretable recommendations and human review |
| R-012 | AI system is accurate but weakly integrated into factory decisions | Medium | High | Integration-depth KPI and workflow acceptance tests |
| R-013 | Full-stack physical-AI vendors create hidden switching costs | Medium | High | Modular interfaces, exportable evidence and dual-runtime validation |
| R-014 | AI recommends technically strong but supply-fragile materials | Medium | High | Supplier-risk ontology and resilience-adjusted criteria |
| R-015 | Action permissions are ambiguous or drift during deployment | Medium | Critical | Versioned `action_authority`, enforcement tests and human approval gates |
| R-016 | Agent retrieves or acts outside intended context | Medium | Critical | Versioned `agent_context_contract`, least privilege, tool allowlist, revocation and logs |
| R-017 | Zero-shot/VLM model appears strong on benchmarks but creates excessive factory false alarms | Medium | High | Frozen textile evaluation set and identical low-FPR acceptance threshold |
| R-018 | Materials AI recommendation is persuasive but opaque | Medium | High | Require interpretable drivers, uncertainty and evidence before lab testing |

## Critical assumptions to validate

1. Existing inspection images can be legally and technically used for model development.
2. Defects can be linked to trustworthy QC dispositions.
3. Production timestamps and line positions can be aligned across systems.
4. At least one defect category has enough examples for a supervised baseline.
5. Unknown/anomaly/zero-shot routing produces operational value beyond existing alarms.
6. The factory accepts a non-controlling shadow pilot.
7. SmartCoat can demonstrate value without exposing confidential data to external model providers.
8. A frozen benchmark can be reproduced on at least two inference runtime paths.
9. Laboratory experiments can be represented with a stable machine-readable lineage contract.
10. Supplier criticality and substitution attributes can be maintained with sufficient quality.
11. Agent context and permissions can be made explicit enough to test and audit.

## Monthly decision questions

- Did any new evidence change the Germany-first sequence?
- Has a competitor entered technical-textile materials intelligence?
- Are open-world or zero-shot inspection methods production-ready enough to change the pilot architecture?
- Which funding programmes now match a defined pilot?
- Which assumptions have moved from unknown to validated or rejected?
- Is factory integration depth increasing, or are only benchmark metrics improving?
- Are action-authority and agent-context rules still correct after every workflow change?
- Is supplier resilience changing the ranking of any candidate material?

## Escalation triggers

Immediately update this register when a major inspection vendor launches a competing open-world/VLM textile product; EU guidance changes likely SmartCoat obligations; a pilot shows unacceptable critical-defect misses; a partner requests ownership of data/ontology; a major funding deadline is within 60 days; a materials platform enters polymers/coatings/textiles; a full-stack vendor blocks evidence export; an agent requests broader tools or context than its contract allows; or a critical raw material becomes constrained, sanctioned, discontinued or materially more expensive.