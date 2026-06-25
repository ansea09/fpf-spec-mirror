---
chunk_kind: "child"
pattern_id: "A.6.0"
pattern_title: "U.Signature - Universal, law-governed declaration for a SubjectKind over a RangedValueKind"
section_id: "A.6.0:7.1"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.0/A.6.0__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "A.6.0 — U.Signature - Universal, law-governed declaration for a SubjectKind over a RangedValueKind"
  - "A.6.0:7.1 — Common Anti-Patterns and How to Avoid Them"
line_start: 10225
line_end: 10233
dependencies:
  - "A.2.6"
  - "A.6.1"
  - "A.6.5"
  - "D.CTX"
  - "E.10"
  - "E.10.D1"
  - "E.5.3"
  - "E.8"
  - "U.Mechanism"
  - "U.RelationSlotDiscipline"
keywords:
  - "RFC 2119"
  - "applicability"
  - "bounded context"
  - "laws"
  - "signature"
  - "vocabulary"
---

### A.6.0:7.1 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Correct action |
|---|---|---|
| Signature as implementation manual | Build steps, CI checks, vendors, or work authorization are placed before the public declaration. | State SubjectKind, RangedValueKind, Vocabulary, Laws, and Applicability first; put realization, tooling, work, and evidence in their governing patterns. |
| Signature as operational gate | Runtime admission predicates are treated as signature laws. | Keep declaration-level constraints in A.6.0 and put operational admissibility conditions in A.6.1 mechanisms. |
| Signature as measurement or bridge proof | Measurement comparability, cross-context transport, or bridge policy is treated as part of the declared law. | Keep the signature declaration stable and use measurement, bridge, evidence, gate, or decision patterns for those relations. |
| Signature as U-kind minting shortcut | A vocabulary symbol is treated as a durable U-kind because it appears in the declaration. | Use C.3, E.24.UK, and the relevant ontic pattern before admitting a durable U-kind. |

