---
chunk_kind: "child"
pattern_id: "A.7"
pattern_title: "Strict Distinction: Repair Conflations of FPF Objects (Clarity Lattice)"
section_id: "A.7:10"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.7/A.7__012_consequences.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "A.7 — Strict Distinction: Repair Conflations of FPF Objects (Clarity Lattice)"
  - "A.7:10 — Consequences"
line_start: 25614
line_end: 25630
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
  - "B.1.2"
  - "B.1.4"
  - "B.1.5"
  - "B.1.6"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.24.PUB"
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
| **Inspectable evidence use** | Claim-relative evidence use and the needed A.10 provenance, carrier and source-currentness relations expose the audit basis. | Recover only the relations and facts needed by that use. |
| **Composition rule selection** | The subject determines which Γ rule and premises govern an aggregation claim. | Check the invariant under that rule and its actual premises. |
| **Readable repair examples** | The rewrites show how a recovered distinction changes the sentence. | Establish the teaching case's stipulated facts in a real use before adopting its rewrite. |

#### A.7:10.1 - EntityOfConcern and publication-boundary consequences

| Benefits | Trade‑offs / Mitigations |
|---------|---------------------------|
| **Category-error detection and correction.** Clear separation of System and Episteme, `EntityOfConcern` and Description-episteme boundary, specification use or refinement, and publication availability helps expose recurring modeling defects. | Name publication face, form, unit, carrier, and rendering uses when the distinction matters; E.8 supplies publication-face guidance. |
| **Audit and explanation share referents.** References distinguish the evidence episteme, target claim, carrier and any needed source-currentness claim. Different publication faces can explain or expose those same values. | Add only the face and reference detail the receiving use needs. |
| **Cross-context and plane safety.** Faces expose an obtaining F.9 Bridge only for two exact local senses and keep its bounded-use claim and optional `CL` separate; cross-plane use exposes its applicable plane relation. | Authors must name only current relations and policies; tooling may assist, but no penalty follows automatically from context, plane, Bridge, or `CL`. |

