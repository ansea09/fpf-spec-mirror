---
chunk_kind: "child"
pattern_id: "G.4"
pattern_title: "CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
section_id: "G.4:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/G.4/G.4__011_rationale.md"
commit_sha: "421266f0a37ab295b1ffd9e214ace6541e21f5be"
heading_path:
  - "G.4 — CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
  - "G.4:10 — Rationale"
line_start: 103300
line_end: 103312
dependencies:
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.18"
  - "A.19"
  - "A.2.1"
  - "A.2.6"
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
  - "U.ClaimScope"
keywords:
  - "CAL Pack@CG-Frame"
  - "Context charter"
  - "acceptance clause"
  - "legal flow"
  - "pass \\"
  - "typed operator card"
---

### G.4:10 - Rationale

CAL sits at the boundary where typed measurement becomes actionable choice. Making CAL a published, typed, and testable artifact reduces semantic drift and prevents “shadow legality gates” from emerging in tools or in downstream prose.

The design separates concerns:

* CHR governs measurement typing and legality guard macros,
* CG‑Spec and CN‑Spec govern the legality gate and governance card, respectively,
* `G.Core` governs Part‑G invariants and trigger/default discipline,
* `G.4` governs the CAL kit: authoring objects, publication surface, and handoff manifest.

This yields modularity (one governing definition per invariant or default), auditability (pins/ids and proof refs), and extensibility (method families attach through explicit extension modules).

