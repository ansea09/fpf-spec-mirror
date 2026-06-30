---
chunk_kind: "child"
pattern_id: "E.24.CD"
pattern_title: "Ontic Candidate Detection"
section_id: "E.24.CD:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.CD/E.24.CD__012_rationale.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "E.24.CD — Ontic Candidate Detection"
  - "E.24.CD:10 — Rationale"
line_start: 79850
line_end: 79857
dependencies:
  - "A.19"
  - "A.19.ECS"
  - "A.6.5"
  - "C.2.1"
  - "E.10"
  - "E.10.ARCH"
  - "E.2.DA"
  - "E.21"
  - "E.24"
  - "E.24.PUB"
  - "E.24.UK"
  - "E.9.DA"
  - "F.18"
  - "F.19"
  - "U.CharacteristicSpace"
keywords:
---

### E.24.CD:10 - Rationale

FPF needs E.24.CD because ontic candidates are rarely visible as pure ontology. They show up as forms that people use: project tables, cards, schemas, diagrams, source packets, draft pattern rows, examples, and repeated words. Those forms are important because they reveal project concerns, but they are unreliable as ontology decisions.

The pattern therefore uses a small detection cluster rather than a score sheet. A cluster is enough to recover the concern, values, possible relation, and next disposition. A score sheet would make candidate discovery look like a maturity test and invite Goodhart-style optimization of the candidate record instead of ontology settlement.

This also preserves the distinction among EoC, description, and publication. A card can describe an episteme, a table can publish a filled characteristic-space evaluation, and a schema can carry source-side data. None of those forms is automatically the ontic. Conversely, the fact that a concern appears through several forms may be a strong signal that an ontic is needed.

