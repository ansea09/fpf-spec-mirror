---
chunk_kind: "child"
pattern_id: "C.32.PAD"
pattern_title: "Project Architecture Decision After Candidate Synthesis"
section_id: "C.32.PAD:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.PAD/C.32.PAD__006_archetypal-grounding.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "C.32.PAD — Project Architecture Decision After Candidate Synthesis"
  - "C.32.PAD:5 — Archetypal Grounding"
line_start: 65775
line_end: 65787
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.21"
  - "B.2"
  - "B.2.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "E.11.PUR"
  - "E.17"
  - "E.24.PUB"
  - "E.8"
  - "G.5"
keywords:
  - "ArchitectureDecisionRelation@Project"
  - "accepted loss"
  - "affected selected structure"
  - "architect-developer split"
  - "architecture-characteristic trade-off"
  - "method-use instruction"
  - "project architecture decision"
  - "reopen condition"
  - "selected architecture option"
---

### C.32.PAD:5 - Archetypal Grounding


**Software service architecture.** A platform team compares synchronous service calls, event-carried integration, and a bounded shared kernel. The selected option is event-carried integration for order events with a bounded exception for payment authorization. C.32.PAD records affected module and information structures, latency and substitutability trade-offs, the method-use instruction for service teams, the event-schema source-return condition, and the reopen trigger when payment volume crosses the declared eval band.

**Manufacturing fixture architecture.** A production architect compares a dedicated fixture per product, a universal fixture with adapters, and a mixed cell layout. The selected option uses a universal fixture only for products inside a scale window. C.32.PAD records module, placement, maintenance, and evidence-structure effects, the accepted setup-time loss, the method instruction for cell design, and the trigger for returning to candidate synthesis when adapter complexity exceeds the guardrail.

**Method-family architecture.** A review-method owner compares role-specialized review, peer rotation, and tool-supported triage. The selected option uses peer rotation plus a tool-supported evidence handoff. C.32.PAD records role, method, evidence, and information structures, the trade-off between teachability and evidence custody, and the developer-owned refinement boundary for local checklists.

**Transformer and transformed holons.** An automation program changes both the toolchain that transforms products and the product architecture being transformed. C.32.CONWAY supplies the correspondence frame. C.32.PAD records which toolchain structure is required to produce the target product structure and which mismatch will reopen the decision.

**Digital-twin structural information loss.** A built-asset team publishes a 6D-style digital-twin decision view for construction planning. The view intentionally hides supplier-contract and temporary-work structures. C.32.PAD records the selected building, placement, schedule, cost, operation, and evidence structures that the decision uses; `C.29` records which hidden structures remain recoverable and which accepted loss reopens the decision. The view count, file, and model do not become the decision authority.

