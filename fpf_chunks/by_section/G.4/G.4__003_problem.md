---
chunk_kind: "child"
pattern_id: "G.4"
pattern_title: "CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
section_id: "G.4:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/G.4/G.4__003_problem.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "G.4 — CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
  - "G.4:2 — Problem"
line_start: 100189
line_end: 100198
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.18"
  - "A.19"
  - "A.2.1"
  - "A.21"
  - "A.6.1"
  - "B.3"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "C.23"
  - "E.17"
  - "E.18"
  - "E.8"
  - "F.17"
  - "F.6"
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
  - "CAL Pack@CG-Frame"
  - "Context charter"
  - "acceptance clause"
  - "legal flow"
  - "pass \\"
  - "typed operator card"
---

### G.4:2 - Problem

Teams repeatedly face drift and ambiguity in the CAL Pack that sits between “typed measurements exist” and “a selector/dispatcher runs”:

* **Illicit operations** slip in (implicit cardinalization, unit laundering, ordinal arithmetic).
* **Acceptance is scattered** (thresholds embedded in code or in CHR prose; predicates not typed; unknown handling inconsistent).
* **Evidence wiring is underspecified** (which provenance anchors matter, what policy ids are in force, what is plane‑scoped, what changes must trigger refresh).
* **Cross‑context imports are silent** (hidden reuse of constructs across contexts or planes/editions without published GateCrossings and loss accounting).
* **Tooling artifacts become semantics** (vendor flags or implementation details substitute for a conceptual specification).

