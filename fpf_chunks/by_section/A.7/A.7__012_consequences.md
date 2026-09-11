---
chunk_kind: "child"
pattern_id: "A.7"
pattern_title: "Strict Distinction (Clarity Lattice)"
section_id: "A.7:10"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.7/A.7__012_consequences.md"
commit_sha: "ef9ded2cb965193aa2484c84f06d65770439cef8"
heading_path:
  - "A.7 — Strict Distinction (Clarity Lattice)"
  - "A.7:10 — Consequences"
line_start: 21835
line_end: 21851
dependencies:
  - "A.1"
  - "A.10"
  - "A.13"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.21"
  - "A.3"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "E.10"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.9"
keywords:
  - "EntityOfConcern ≠ Description episteme"
  - "MethodDescription ≠ Method ≠ Capability ≠ Work"
  - "category error"
  - "system-role kind and assignment ≠ Work"
---

### A.7:10 - Consequences

| Benefit                      | Why it matters                                    | Trade‑off / Mitigation                             |
| ---------------------------- | ------------------------------------------------- | -------------------------------------------------- |
| **Category safety at scale** | Makes category slips in claims across holarchies easier to recognize and correct. | Slight explicitness; mitigate by keeping ordinary System-and-action wording and adding assignment, kind, Method, Capability, Work, carrier, or evidence detail only when a receiving inference needs it. |
| **Trustworthy evidence**     | Claim-relative evidence use and the applicable A.10 provenance, carrier, and source-currentness relations make the audit basis inspectable. | Requires discipline → provide checklists.          |
| **Operator determinism**     | Correct Γ‑flavour selection preserves invariants. | A bit more modelling → reusable templates.         |
| **On‑ramp for managers**     | Canonical rewrites give immediate phrasing fixes. | Team training → this pattern is the training page. |

#### A.7:10.1 - EntityOfConcern and publication-boundary consequences

| Benefits | Trade‑offs / Mitigations |
|---------|---------------------------|
| **Category-error detection and correction.** Clear separation of System and Episteme, `EntityOfConcern` and Description-episteme boundary, specification use or refinement, and publication availability helps expose recurring modeling defects. | Name publication face, form, unit, carrier, and rendering uses when the distinction matters; E.8 supplies publication-face guidance. |
| **Audit and pedagogy align.** References distinguish the evidence episteme, its target claim, a carrier, and any current source-currentness claim; Normative face houses checklists; Plain face teaches; Tech face types. | Slight increase in pattern length; offset by predictable navigation and machine-checkable CC. |
| **Cross-context and plane safety.** Faces expose an obtaining F.9 Bridge only for two exact local senses and keep its bounded-use claim and optional `CL` separate; cross-plane use exposes its applicable plane relation. | Authors must name only current relations and policies; tooling may assist, but no penalty follows automatically from context, plane, Bridge, or `CL`. |

