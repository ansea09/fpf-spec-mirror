---
chunk_kind: "child"
pattern_id: "E.19"
pattern_title: "Pattern Quality Gates: Review and Refresh Profiles"
section_id: "E.19:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.19/E.19__005_problem-frame.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "E.19 — Pattern Quality Gates: Review and Refresh Profiles"
  - "E.19:1 — Problem frame"
line_start: 76366
line_end: 76375
dependencies:
  - "A.6.P"
  - "C.2.P"
  - "E.10"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9"
  - "F.18"
  - "F.19"
keywords:
  - "(see H-8)"
  - "MUST NOT modify modeled-world entities (e.g"
  - "and (if needed) reference them from CC items"
  - "inside the predicate)"
  - "where a non-deontic Invariant: predicate is required)"
  - "“Earth”"
  - "“RoleAssignment”"
  - "“Role”"
  - "“holon”) — express those as Invariant: / Well‑formedness constraint: predicates instead"
---

### E.19:1 - Problem frame

FPF evolves by adding and revising patterns. Over time, the framework accumulates two kinds of risk:

1. **Admission risk** — a newly authored pattern can be structurally compliant yet still fail on ontology, semantics, terminology conflicts and vagueness, scope, SoTA in related disciplines, or cross-context hygiene.

2. **Staleness risk** — older patterns can remain internally consistent while drifting away from contemporary practice and newer parts of FPF, current internal vocabulary, or updated related governing patterns. The result is “quiet decay”: the pattern still appears clear, but becomes misleading, incomplete, or incompatible.

FPF already contains many checklists and constraints, but they are distributed across patterns and suites. Authors and reviewers therefore lack a single, repeatable way to answer: *What should be checked, and how deep, before a pattern is admitted or kept?*

