---
chunk_kind: "child"
pattern_id: "A.6.0"
pattern_title: "U.Signature - Universal, law-governed declaration for a SubjectKind over a RangedValueKind"
section_id: "A.6.0:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.0/A.6.0__005_forces.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "A.6.0 — U.Signature - Universal, law-governed declaration for a SubjectKind over a RangedValueKind"
  - "A.6.0:3 — Forces"
line_start: 9999
line_end: 10007
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

### A.6.0:3 - Forces

| Force | Tension |
| --- | --- |
| **Universality vs. fitness** | One shape must fit **Kernel**, **Mechanisms**, **Protocols**, and other specialised signatures, without over‑committing to any one family. |
| **EntityOfConcern vs. specification use** | Signatures declare **the subject kind and laws**, not recipes or test harnesses. |
| **Simplicity vs. expressivity** | Keep the kernel small while allowing family-specific header metadata and usable projections (e.g., `imports` and `provides` DAGs, assurance matrices, transport views). |
| **Locality vs. transport** | Meaning is context‑local (D.CTX); transport must remain explicit and auditable (Part F) without smuggling implementation. |

