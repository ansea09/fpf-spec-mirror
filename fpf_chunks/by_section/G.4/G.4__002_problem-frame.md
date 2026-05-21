---
chunk_kind: "child"
pattern_id: "G.4"
pattern_title: "CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
section_id: "G.4:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/G.4/G.4__002_problem-frame.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "G.4 — CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
  - "G.4:1 — Problem frame"
line_start: 69601
line_end: 69616
dependencies:
  - "A.10"
  - "A.18"
  - "A.19"
  - "A.21"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.23"
  - "E.17"
  - "E.18"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.0"
  - "G.1"
  - "G.10"
  - "G.11"
  - "G.2"
  - "G.3"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.8"
  - "G.9"
  - "G.Core"
keywords:
  - "CAL authoring"
  - "RSCRTriggerKindId"
  - "acceptance clauses"
  - "edition pins"
  - "evidence profiles"
  - "legality gates"
  - "operators"
  - "tri-state admissibility"
  - "Γ-fold hooks"
  - "Φ/Ψ/Φ_plane policy pins"
---

### G.4:1 - Problem frame

A CG‑Frame has:

* a declared `CG-FrameContext` (scope, described entity, plane),
* a plurality of method traditions and claims (SoTA inputs), and
* CHR‑typed measurement constructs (`Characteristic/Scale/Coordinate` + legality guard macros).

Before any run‑time selection, comparison, aggregation, or selected-set formation is executed downstream, the CG‑Frame needs an explicit, auditable **CAL Pack** that:

1. defines *what operators exist* and what they are allowed to do over CHR types,
2. externalizes *fit‑for‑purpose acceptance* as typed predicates (with Context‑local thresholds), and
3. binds these choices to an evidence wiring surface (lanes, provenance anchors, policy pins, and refresh triggers) so that downstream selection, logging, parity, and shipping can cite *stable ids* rather than re‑inventing semantics.

This pattern provides the design‑time authoring kit and the publication surface for CAL artifacts, while delegating Part‑G‑wide invariants to `G.Core` and CN-Spec and CG-Spec legality to `CG‑Spec`/`CN‑Spec`.

