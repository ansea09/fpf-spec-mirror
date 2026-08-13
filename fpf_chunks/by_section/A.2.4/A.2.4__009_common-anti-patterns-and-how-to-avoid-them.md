---
chunk_kind: "child"
pattern_id: "A.2.4"
pattern_title: "Episteme Evidence-Use and Status-Use Relations"
section_id: "A.2.4:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.4/A.2.4__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "A.2.4 — Episteme Evidence-Use and Status-Use Relations"
  - "A.2.4:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 4546
line_end: 4556
dependencies:
  - "A.10"
  - "A.2"
  - "A.2.1"
  - "A.6.5"
  - "A.6.RSIR"
  - "B.3"
  - "C.2.1"
  - "C.28"
  - "E.10.D2"
  - "E.10.ROLE"
  - "E.17"
  - "F.10"
  - "G.11"
  - "G.6"
  - "U.SystemRoleAssignment"
keywords:
  - "claim"
  - "episteme"
  - "evidence-use relation"
  - "provenance"
  - "role-shaped source phrase"
  - "source-use wording"
  - "status-use relation"
---

### A.2.4:8 - Common Anti-Patterns and How to Avoid Them

| Source wording | Failure | Repair |
| --- | --- | --- |
| "The report has EvidenceRole for Claim A." | Treats a source label as a system-role kind or assignment without recovering the actual relation. | Use an evidence-use relation with `EvidenceEpistemeSlot`, `EvidenceTargetClaimSlot`, scope, polarity, window, and provenance constraints when current. |
| "Dataset X proves safety." | Treats dataset presence as proof, assurance, and safety claim. | Use `A.10` for evidence, `B.3` for assurance or safety assurance, and name unsupported attempted use. |
| "The standard has normative role." | Role word hides standard-use, requirement-use, source-use, or publication-use. | Recover the relation governed by the current claim and apply `E.10.D2`, `E.17`, `F.10`, or the direct requirement pattern. |
| "The badge is current, so release is allowed." | Status display becomes gate passage or permission. | Use status-use relation plus gate or release subject pattern; dashboard display alone is not a decision. |
| "Simulation output is counterfactual evidence." | Simulation-only output is promoted to realized or interventional causal evidence. | Use `C.28`; keep `simulationOnlyCounterfactualOutputBasis` distinct unless an exact causal-use predicate and current assertion establish another value. |
| "The work run is the evidence role." | Work occurrence, local result, result episteme, and later evidence-use are collapsed. | Use A.15.1/A.6.1 for dated work and bindings, the domain pattern for the local result, C.2.1 for its episteme, A.10/G.6 for provenance, and A.2.4 only for first-use classification. |

