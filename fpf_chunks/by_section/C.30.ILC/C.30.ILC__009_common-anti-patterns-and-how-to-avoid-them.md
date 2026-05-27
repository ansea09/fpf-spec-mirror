---
chunk_kind: "child"
pattern_id: "C.30.ILC"
pattern_title: "Cross-Scope Architecture Residual Triage"
section_id: "C.30.ILC:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.ILC/C.30.ILC__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "C.30.ILC — Cross-Scope Architecture Residual Triage"
  - "C.30.ILC:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 52456
line_end: 52466
dependencies:
  - "A.10"
  - "A.22"
  - "A.6.F"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.LCA"
  - "C.30.TGA-FLOW-REL"
  - "D.3"
  - "D.4"
  - "G.5"
  - "G.6"
keywords:
  - "cross-scope residual"
  - "declared scope"
  - "frustration"
  - "interlevel conflict"
  - "local repair"
  - "source return"
  - "structure kind"
---

### C.30.ILC:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| Generic complexity bucket | Everything becomes `complexity` or `interlevel conflict`. | Name declared scopes, structure kinds, residual, and first architecture move. |
| Measurement-first conflict | The team starts measuring before declaring what is in conflict. | Run ILC triage first; open `C.16` or an admitted characteristic/measurement receiving pattern only when the measured characteristic is live. |
| Risk color as cross-scope decision | A red, yellow, or green risk cell, risk matrix, or maturity score decides the cross-scope architecture move or resource-allocation priority. | Recover declared scopes, live structure kinds, the residual, the loss, hazard, or threat path, selected support reading, characteristic scale, comparator, gate pattern, and first admissible architecture move; do not treat ordinal risk color as architecture adequacy, evidence sufficiency, causal proof, assurance proof, resource-allocation priority, or gate passage. |
| Stakeholder-only conflict | A structural residual is sent to mediation with no architecture move. | Use `D.3`/`D.4` only when values, stakeholder negotiation, or ethical mediation is live. |
| Hidden candidate generation | The residual immediately spawns many designs. | State the first admissible move; open `G.5` or an admitted candidate-generation receiving pattern only when candidate generation is live. |
| Scope word without scope record | The text says `level`, `layer`, `scale`, or `scope` without a declared field. | Recover the exact declared scope or demote the phrase to ordinary recognition. |

