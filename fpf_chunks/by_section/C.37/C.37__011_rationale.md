---
chunk_kind: "child"
pattern_id: "C.37"
pattern_title: "Use-Bounded Representation Selection and Co-Use"
section_id: "C.37:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.37/C.37__011_rationale.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "C.37 — Use-Bounded Representation Selection and Co-Use"
  - "C.37:10 — Rationale"
line_start: 68201
line_end: 68206
dependencies:
  - "A.10"
  - "A.2.4"
  - "A.22"
  - "A.6.3.RT"
  - "C.11"
  - "C.13"
  - "C.2.1"
  - "C.2.P.DR"
  - "C.29"
  - "E.17.0"
  - "E.24.PUB"
keywords:
---

### C.37:10 - Rationale

The receiving use is the smallest stable boundary shared across domains. Representation kinds, correspondence relations, view predicates, plan claims, Work records, mathematical objects, and decision results do not converge on one ontology, but practitioners repeatedly need the same action sequence over them: recover the direct result, state the relied-on claim and loss, test bounded reliance when material, obtain the receiving result, and select, decline, or stop.

`Co-use` is chosen instead of *composition* because the rows need not form a new whole. The same receiver may use them together while every candidate and relation retains its own identity, predicate, and return condition.

