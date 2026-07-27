---
chunk_kind: "child"
pattern_id: "G.4"
pattern_title: "CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
section_id: "G.4:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/G.4/G.4__001_intro.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "G.4 — CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
  - "G.4:intro — Intro"
line_start: 96469
line_end: 96484
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

## G.4 - CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring

**Tag.** Architectural pattern (publishes `CAL Pack@CG-Frame`; consumes `CHR Pack@CG-Frame`; constrains selector/dispatcher usage; binds GateCrossing discipline; exposes `ReferencePlane` and penalty/guard policy pins to `SCR`)

**Stage.** design‑time (authoring & publication; enables lawful run‑time evaluation)

**Primary output.** A notation‑independent `CAL Pack@CG-Frame` containing:
`CAL.Charter@Context`, `CAL.Operator[]`, `CAL.Acceptance[]`, `CAL.Flow[]`,
`CAL.EvidenceProfiles`, `CAL.ProofLedger`, **optional** `CAL.NQD[]` (when declared),
UTS entries (Name Cards with twin labels and public-id continuity notes, including deprecations and lexical-continuity notes),
RSCR tests, Worked‑Examples, and a `TaskMap@Context` (`TaskMap`; handoff record consumed by `G.5`).

**Primary hooks.** `G.Core` (Part‑G invariants + RSCR trigger catalogue + Default Governing Definition Index), `G.1` (CG‑FrameContext), `G.2` (SoTA Synthesis Pack), `G.3` (CHR Pack), `G.0` (CG‑Spec legality gate), `A.19` (CN‑Spec), `A.18` (CSLC), `A.10` (provenance anchors), `B.3` (trust / freshness / decay), `E.18` + `A.21` + `F.9`/`F.17`/`E.17` (GateCrossing / CrossingBundle harnesses), `G.6` (EvidenceGraph / PathId / PathSliceId; wired via Extensions), `G.5` (Selector & Dispatch), `G.10` (shipping), `G.11` (refresh orchestration), plus Contexts/UTS/LEX disciplines already fixed elsewhere in the spec.

**Non‑duplication note.** Universal Part‑G invariants (no shadow specs, crossing visibility, tri‑state guard, penalties→`R_eff`‑only, set‑return semantics, P2W split, typed RSCR causes, Default Governing Definition Index, shipping boundary) are governed in `G.Core` and are pulled into `G.4` only through the `G.Core linkage` manifest in **G.4:4.1** (and via explicit delegations in CC).

