---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local-First Unification Naming Protocol"
section_id: "F.18:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__005_forces.md"
commit_sha: "9a9a42e4d154021ca3f7415e0009a4214832f65f"
heading_path:
  - "F.18 — Local-First Unification Naming Protocol"
  - "F.18:3 — Forces"
line_start: 95345
line_end: 95354
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.6.RSIR"
  - "B.3"
  - "C.2.1"
  - "E.10"
  - "E.10.ARCH"
  - "E.24.PUB"
  - "F.0.1"
  - "F.1"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.8"
  - "F.9"
  - "G.10"
  - "G.2"
  - "G.6"
keywords:
---

### F.18:3 - Forces

| Force | Naming tension |
| --- | --- |
| Local sense and reuse across different semantic-context projections | A name must be interpretable under one effective by-value `U.ReferenceScheme` while remaining bridgeable to a different `<ReferenceScheme, LocalSenseClaim>` projection without spelling-based identity. The projections can differ under one scheme. |
| Brevity and ontology recovery | A short label helps conversation, but the `NameCard` must keep governed kind, effective reference scheme, local sense, governing pattern, and intended use recoverable. |
| Continuity and correction | Readers need stable public names, while authors must be able to rename, split, merge, or retire names without erasing earlier uses. |
| Familiarity and precision | Familiar words are easier to adopt, but some familiar words import wrong prototypes from another discipline. |
| Role recognition and role explosion | Role morphology is useful for `U.Role` values, but it must not absorb holder assignment, capability, method, work, evidence, or status claims. |

