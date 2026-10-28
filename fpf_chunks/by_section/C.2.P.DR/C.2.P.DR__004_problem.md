---
chunk_kind: "child"
pattern_id: "C.2.P.DR"
pattern_title: "Repair Claims Based on Declarative Form Alone (Declarative Representation Precision Restoration)"
section_id: "C.2.P.DR:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.P.DR/C.2.P.DR__004_problem.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "C.2.P.DR — Repair Claims Based on Declarative Form Alone (Declarative Representation Precision Restoration)"
  - "C.2.P.DR:2 — Problem"
line_start: 54020
line_end: 54030
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.15.4"
  - "A.19"
  - "A.19.SPR"
  - "A.20"
  - "A.21"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.0"
  - "A.6.1"
  - "A.7"
  - "B.3"
  - "C.16"
  - "C.2.1"
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
4. **Pattern relation overread as dispatch.** A reference to another pattern is treated as an actual call or work occurrence. Ordinary navigation remains adequate when it expresses the intended relation clearly.
5. **Programming-paradigm label becomes ontology.** A label such as functional, declarative or workflow is treated as sufficient to determine an FPF kind.
6. **Mechanism, method, and work collapse.** A method-like expression is repaired to `method` or `mechanism` by vocabulary rather than by the current claim: way of doing, description, formal substrate, law-governed mechanism, plan, occurrence, evidence, or quote-only wording.

