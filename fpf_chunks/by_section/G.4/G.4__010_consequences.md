---
chunk_kind: "child"
pattern_id: "G.4"
pattern_title: "CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
section_id: "G.4:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/G.4/G.4__010_consequences.md"
commit_sha: "3d19010169827708d0bca36d0551af8323908640"
heading_path:
  - "G.4 — CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
  - "G.4:9 — Consequences"
line_start: 78867
line_end: 78873
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

### G.4:9 - Consequences

* CAL becomes a stable, citable CAL Pack: operator/acceptance semantics are explicit artifacts, not tacit code behavior.
* Legality failures are surfaced as authoring defects (RSCR‑testable) rather than run‑time surprises.
* Downstream patterns (`G.5`, `G.8`, `G.9`, `G.10`, `G.11`) can reference stable ids/pins without redefining acceptance or operator semantics.
* Method pluralism is supported: multiple calculi can coexist as separate operator/flow/acceptance families, wired via Extensions rather than mixed into the core kit.

