---
chunk_kind: "child"
pattern_id: "G.4"
pattern_title: "CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
section_id: "G.4:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/G.4/G.4__003_problem.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "G.4 — CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
  - "G.4:2 — Problem"
line_start: 89566
line_end: 89575
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
  - "admissibility gates"
  - "edition pins"
  - "evidence profiles"
  - "operators"
  - "tri-state admissibility"
  - "Γ-fold hooks"
  - "Φ/Ψ/Φ_plane policy pins"
---

### G.4:2 - Problem

Teams repeatedly face drift and ambiguity in the CAL Pack that sits between “typed measurements exist” and “a selector/dispatcher runs”:

* **Illicit operations** slip in (implicit cardinalization, unit laundering, ordinal arithmetic).
* **Acceptance is scattered** (thresholds embedded in code or in CHR prose; predicates not typed; unknown handling inconsistent).
* **Evidence wiring is underspecified** (which provenance anchors matter, what policy ids are in force, what is plane‑scoped, what changes must trigger refresh).
* **Cross‑context imports are silent** (hidden reuse of constructs across contexts or planes/editions without published GateCrossings and loss accounting).
* **Tooling artifacts become semantics** (vendor flags or implementation details substitute for a conceptual specification).

