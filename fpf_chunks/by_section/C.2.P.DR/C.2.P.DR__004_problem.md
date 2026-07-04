---
chunk_kind: "child"
pattern_id: "C.2.P.DR"
pattern_title: "Declarative Representation Precision Restoration"
section_id: "C.2.P.DR:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.P.DR/C.2.P.DR__004_problem.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "C.2.P.DR — Declarative Representation Precision Restoration"
  - "C.2.P.DR:2 — Problem"
line_start: 40299
line_end: 40309
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.15.4"
  - "A.19.SPR"
  - "A.20"
  - "A.21"
  - "A.3.1"
  - "A.3.2"
  - "A.6.0"
  - "A.6.1"
  - "A.7"
  - "B.3"
  - "C.2.P"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.20"
  - "E.8"
  - "F.19"
keywords:
---

### C.2.P.DR:2 - Problem

Without this repair:

1. **Graph path becomes work route.** A path or path slice in `E.18` is treated as an ordered work narrative, even when no work occurrence, work plan, or method description is current.
2. **Evidence path becomes permission.** An evidence relation or provenance relation is treated as approval, gate passage, release, safety, or authority rather than as evidence for a named claim or effect.
3. **Query becomes method.** A query, access path, query plan, or dashboard is treated as the semantic way of doing, rather than as a representation, method description, evidence relation, source relation, or ordinary source wording.
4. **Pattern relation overread as dispatch.** Pattern application prose starts saying that one pattern exits to, routes to, calls, invokes, receives, owns, or dispatches another, hiding declarative pattern relations and direct governing-pattern selection.
5. **Programming-paradigm label becomes ontology.** Imperative, functional, logical, constraint, object-centric event, effect-handler, pipeline, orchestration, or workflow wording is treated as the FPF kind rather than as one representation style or source label.
6. **Mechanism, method, and work collapse.** A method-like expression is repaired to `method` or `mechanism` by vocabulary rather than by the current claim: way of doing, description, formal substrate, law-governed mechanism, plan, occurrence, evidence, or quote-only wording.

