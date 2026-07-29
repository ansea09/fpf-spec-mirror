---
chunk_kind: "child"
pattern_id: "G.4"
pattern_title: "CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
section_id: "G.4:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/G.4/G.4__011_rationale.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "G.4 — CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
  - "G.4:10 — Rationale"
line_start: 97790
line_end: 97802
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

### G.4:10 - Rationale

CAL sits at the boundary where typed measurement becomes actionable choice. Making CAL a published, typed, and testable artifact reduces semantic drift and prevents “shadow legality gates” from emerging in tools or in downstream prose.

The design separates concerns:

* CHR governs measurement typing and legality guard macros,
* CG‑Spec and CN‑Spec govern the legality gate and governance card, respectively,
* `G.Core` governs Part‑G invariants and trigger/default discipline,
* `G.4` governs the CAL kit: authoring objects, publication surface, and handoff manifest.

This yields modularity (one governing definition per invariant or default), auditability (pins/ids and proof refs), and extensibility (method families attach through explicit extension modules).

