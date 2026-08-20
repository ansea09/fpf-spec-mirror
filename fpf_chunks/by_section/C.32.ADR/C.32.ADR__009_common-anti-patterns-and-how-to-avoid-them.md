---
chunk_kind: "child"
pattern_id: "C.32.ADR"
pattern_title: "Architecture Decision Record Projection"
section_id: "C.32.ADR:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ADR/C.32.ADR__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "C.32.ADR — Architecture Decision Record Projection"
  - "C.32.ADR:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 66870
line_end: 66880
dependencies:
  - "A.10"
  - "A.15"
  - "A.21"
  - "B.3"
  - "C.16"
  - "C.25"
  - "C.29"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.32.ADA"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.11.PUR"
  - "E.17"
  - "E.24.PUB"
  - "E.8"
keywords:
  - "ADR projection"
  - "ArchitectureDecisionDescription@Project"
  - "ArchitectureDecisionRecordProjection@Project"
  - "architecture decision record"
  - "consequences"
  - "method-use instruction"
  - "publication boundary"
  - "rationale"
  - "section function"
  - "supersession"
---

### C.32.ADR:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| `BlankTemplateADR` | A template is filled with plausible prose but no PAD relation can be cited. | Draft or recover `ArchitectureDecisionRelation@Project` with `C.32.PAD`; then project it into the record. |
| `ArchitectureDescriptionDump` | The ADR copies diagrams, views, or model text and the decision outcome is hard to find. | Keep the record small; cite architecture-description refs and restore decision outcome, rationale, consequences, and work effects. |
| `OptionsInventedInRecord` | The ADR lists options that were not part of candidate synthesis or accepted decision basis. | Use `C.32`, `A.19.CPM`, or PAD; update the decision relation before updating the record. |
| `MethodInstructionHiddenInRationale` | A decision requires developers to change their practice, but the instruction is buried in rationale prose. | Record the prospective content through the exact plan, policy, commitment, permission, decision, responsibility, authority, or other direct relation that states it, with Method refs, intended Systems, expected structure effect, and readiness or gate exit; otherwise return its exact missing governor. Do not manufacture a current assignment or performed Work. If performance later occurs, point to its complete A.15.1/F.6 basis and add only the other direct relations that independently obtain. |
| `NoConfirmationPath` | Future teams cannot tell whether the decision still holds or has been violated. | Add confirmation, eval, guardrail, source-return, or supersession condition; use the receiving evaluation or governance pattern. |
| `PackageOrderAsGovernance` | The latest file by number is treated as active without explicit status or supersession. | Add package map or status fields; make active, proposed, superseded, and related relations explicit. |

