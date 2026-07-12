---
chunk_kind: "child"
pattern_id: "D.4"
pattern_title: "Ethical Mediation and Decision Use"
section_id: "D.4:2"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/D.4/D.4__005_solution.md"
commit_sha: "44dd88188a07646ef23aca32627a3f670525853f"
heading_path:
  - "D.4 — Ethical Mediation and Decision Use"
  - "D.4:2 — Solution"
line_start: 64606
line_end: 64631
dependencies:
  - "A.10"
  - "A.20"
  - "A.21"
  - "B.3"
  - "C.11"
  - "C.28"
  - "C.29"
  - "C.30.ILC"
  - "D.1"
  - "D.2"
  - "D.3"
  - "D.5"
keywords:
---

### D.4:2 - Solution

Record an `EthicalMediationDecisionUse@Context`:

```text
EthicalMediationDecisionUse@Context:
  conflictStructureRef
  boundedContextRef
  valueFrameRefs
  decisionQuestionRef?
  optionRefs
  proposedMediationRefs?
  refusalOrStopCondition?
  evidenceDemandRefs?
  causalReturnRefs?
  assuranceReturnRefs?
  architectureResidualReturnRefs?
  acceptedResidualRefs?
  decisionRecordRefs?
  admissibleUse
  inadmissibleOverread
  strongerSourceReturnCondition
```

The record names the current ethical use of the conflict: mediate, refuse, continue under explicit residual, demand evidence, ask a causal question, ask for assurance, return to architecture, or make a bounded decision.

