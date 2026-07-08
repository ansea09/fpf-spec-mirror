---
chunk_kind: "child"
pattern_id: "E.10.MOVE"
pattern_title: "Move and Readiness Wording Precision Restoration"
section_id: "E.10.MOVE:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.MOVE/E.10.MOVE__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "E.10.MOVE — Move and Readiness Wording Precision Restoration"
  - "E.10.MOVE:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 69558
line_end: 69567
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.3"
  - "A.15.4"
  - "A.15.5"
  - "A.16"
  - "A.16.0"
  - "A.21"
  - "A.3.4.P"
  - "B.1.6"
  - "C.24"
  - "C.30"
  - "C.30.AD"
  - "E.10"
  - "E.10.ARCH"
  - "E.11.PUR"
  - "E.17"
  - "E.18.1"
  - "E.24"
  - "G.6"
keywords:
---

### E.10.MOVE:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Better use |
| --- | --- | --- |
| Synonym replacement | "Move" becomes "action" or "use" without recovered kind. | Recover governed text span, claim being made, object under wording repair, relation, and governing pattern first. |
| Imported MOVE kind | TameFlow source wording becomes FPF ontology. | Recover intended work, readiness, gate, preparation work, or performed work. |
| Readiness as gate passage | A ready label becomes `GateDecision=pass`. | Use A.21 only when gate fields are present. |
| Path as work-authorization route | Evidence path or source-reference path becomes a way to authorize work by resemblance. | Recover evidence relation, source relation, graph path, gate relation, work authorization, or deontic permission separately. |
| Local move generalized | A.16, C.24, or C.30 local move wording is generalized to all project work. | Keep local loci local and use the direct governing pattern elsewhere. |

