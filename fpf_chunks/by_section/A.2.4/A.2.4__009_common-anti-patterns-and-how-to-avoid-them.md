---
chunk_kind: "child"
pattern_id: "A.2.4"
pattern_title: "Episteme Evidence-Use and Status-Use Relations"
section_id: "A.2.4:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.4/A.2.4__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "A.2.4 — Episteme Evidence-Use and Status-Use Relations"
  - "A.2.4:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 4359
line_end: 4369
dependencies:
  - "A.10"
  - "A.2"
  - "A.2.1"
  - "A.6.5"
  - "B.3"
  - "C.2.1"
  - "C.28"
  - "E.10.D2"
  - "E.17"
  - "F.10"
  - "G.11"
  - "G.6"
  - "U.Role"
  - "U.RoleAssignment"
keywords:
  - "claim"
  - "episteme"
  - "evidence-use"
  - "provenance"
  - "source-use"
  - "status-use"
---

### A.2.4:8 - Common Anti-Patterns and How to Avoid Them

| Source wording | Failure | Repair |
| --- | --- | --- |
| "The report has EvidenceRole for Claim A." | Puts an episteme into role ontology. | Use an evidence-use relation with `EvidenceEpistemeSlot`, `EvidenceTargetClaimSlot`, scope, polarity, window, and provenance constraints when current. |
| "Dataset X proves safety." | Treats dataset presence as proof, assurance, and safety claim. | Use `A.10` for evidence, `B.3` for assurance or safety assurance, and name unsupported attempted use. |
| "The standard has normative role." | Role word hides standard-use, requirement-use, source-use, or publication-use. | Recover the relation governed by the current claim and apply `E.10.D2`, `E.17`, `F.10`, or the direct requirement pattern. |
| "The badge is current, so release is allowed." | Status display becomes gate passage or permission. | Use status-use relation plus gate or release governing pattern; dashboard display alone is not a decision. |
| "Simulation output is counterfactual evidence." | Simulation-only output is promoted to realized or interventional causal evidence. | Use `C.28`; keep `simulationOnlyCounterfactualOutputBasis` distinct unless the causal-use pattern admits another value. |
| "The work run is the evidence role." | Work occurrence, local result, result episteme, and later evidence-use are collapsed. | Use A.15.1/A.6.1 for dated work and bindings, the domain pattern for the local result, C.2.1 for its episteme, A.10/G.6 for provenance, and A.2.4 only for first-use classification. |

