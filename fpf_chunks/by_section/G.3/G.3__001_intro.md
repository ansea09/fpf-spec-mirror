---
chunk_kind: "child"
pattern_id: "G.3"
pattern_title: "CHR Authoring for a CG‑Frame: Characteristics, Scales, Levels, Coordinates"
section_id: "G.3:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/G.3/G.3__001_intro.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "G.3 — CHR Authoring for a CG‑Frame: Characteristics, Scales, Levels, Coordinates"
  - "G.3:intro — Intro"
line_start: 69146
line_end: 69153
dependencies:
  - "A.10"
  - "A.15.3"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.CHR"
  - "B.3"
  - "B.3.4"
  - "C.16"
  - "C.18"
  - "C.19"
  - "E.10"
  - "E.5.1"
  - "E.5.3"
  - "F.1"
  - "F.17"
  - "F.9"
  - "G.0"
  - "G.1"
  - "G.10"
  - "G.11"
  - "G.2"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.Core"
keywords:
  - "CHR Pack@CG-Frame"
  - "CHR authoring"
  - "CSLC legality"
  - "RSCRTriggerKindId"
  - "ReferencePlane"
  - "characteristics"
  - "coordinates"
  - "edition pins"
  - "levels"
  - "scales"
  - "typed measurement"
  - "Φ/CL policy pins"
---

## G.3 - CHR Authoring for a CG‑Frame: Characteristics, Scales, Levels, Coordinates

**Tag.** Architectural pattern (CHR kit; publishes lawful measurement primitives; constrains CAL authoring and selector/dispatch use)
**Stage.** *design‑time* (authoring & publication; enables admissible run-time consumption by `G.4` / `G.5`)
**Primary output.** `CHR Pack@CG‑Frame` — a notation‑independent, UTS‑published CHR bundle that provides: typed Characteristics/Scales/Levels/Coordinates, legality + guard surfaces, aggregation/comparison specs, RSCR hooks/tests, and provenance pins.
**Primary hooks.** `G.1` (CG‑FrameContext), `G.2` (SoTA synthesis inputs), `A.19.CHR` (CHRMechanismSuite boundary + pins), `A.15.3` (SlotFillingsPlanItem baseline), `A.18/C.16` (MM‑CHR legality), `F.1–F.9` (Contexts/UTS/Bridges), `B.3` / `B.3.4` (trust, freshness/decay), `A.10` (provenance anchors/carriers), `G.6` (EvidenceGraph/Path citation), optional `C.18 and C.19` (QD/OEE wiring), `G.11` (refresh orchestration).
**Non‑duplication note.** Universal Part‑G invariants (bridge‑only crossings, tri‑state semantics, penalties→`R_eff`‑only, set‑return semantics, P2W split, typed RSCR triggers + alias docking, defaults with one governing definition, linkage discipline) are governed by `G.Core`. This pattern cites them via `G.3:4.1` and delegates where needed.

