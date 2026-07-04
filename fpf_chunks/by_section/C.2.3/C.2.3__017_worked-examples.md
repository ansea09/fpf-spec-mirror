---
chunk_kind: "child"
pattern_id: "C.2.3"
pattern_title: "Unified Formality Characteristic F"
section_id: "C.2.3:16"
section_title: "Worked Examples"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.3/C.2.3__017_worked-examples.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "C.2.3 — Unified Formality Characteristic F"
  - "C.2.3:16 — Worked Examples"
line_start: 39213
line_end: 39238
dependencies:
  - "A.16"
  - "A.18"
  - "A.19"
  - "B.3"
  - "C.2"
  - "C.2.2"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "F.9"
keywords:
  - "F-scale"
  - "F0-F9"
  - "Formality"
  - "language-state separation"
  - "proof"
  - "rigor"
  - "specification"
---

### C.2.3:16 - Worked Examples

#### C.2.3:16.1 - Research hypothesis

A short note proposing a new scaling law with one stable reading and explicit acceptance conditions in prose is typically `F3`. Rewriting the acceptance conditions as typed predicates would move it toward `F4`.

#### C.2.3:16.2 - Interface specification

An interface specification with explicit preconditions, postconditions, and invariants is typically `F4`. Adding declared executable semantics in a faithful reference model may move it toward `F5`.

#### C.2.3:16.3 - Safety controller

A controller coupled to a plant model with explicit hybrid obligations is typically `F6`. If key invariants are then machine-checked in a higher-order proof environment, those claims move toward `F7`.

#### C.2.3:16.4 - Decision policy

A decision policy with controlled prose may remain `F3`. If thresholds and conditions are published as typed predicates, it becomes `F4`.

#### C.2.3:16.5 - Proof-bearing algorithm

A dependent-typed algorithm whose central property is carried by the type itself is typically `F8`.

#### C.2.3:16.6 - Executable ML recipe

A fully explicit training-and-evaluation recipe with declared execution semantics is typically `F5`. It does not become `F7` merely because the surrounding execution machinery is sophisticated.

