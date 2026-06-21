---
chunk_kind: "child"
pattern_id: "A.6.0"
pattern_title: "U.Signature - Universal, law-governed declaration for a SubjectKind over a RangedValueKind"
section_id: "A.6.0:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.0/A.6.0__003_problem-frame.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "A.6.0 — U.Signature - Universal, law-governed declaration for a SubjectKind over a RangedValueKind"
  - "A.6.0:1 — Problem frame"
line_start: 10003
line_end: 10011
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

### A.6.0:1 - Problem frame

FPF already uses “signatures” to stabilise public promises of **reusable extension vocabularies** and, via **A.6.1**, of **mechanisms**. But declaration publishers also need stable, minimal declarations for **theories**, **methods** (operational families), and **disciplines** (regulated vocabularies). Without **one** universal notion of signature:
* similar constructs proliferate under incompatible names;
* practitioners cannot tell what is **declared** (EntityOfConcern kind and laws) versus what is **realized** or admitted for specification use;
* cross-context reuse lacks a canonical place to state **applicability** and **declared admissible vocabularies**.

E.8 demands one publication voice and section order; E.10 demands lexical discipline across strata. A.6.0 provides the common kernel shape these patterns presuppose.

