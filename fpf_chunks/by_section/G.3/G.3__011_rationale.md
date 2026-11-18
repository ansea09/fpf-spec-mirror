---
chunk_kind: "child"
pattern_id: "G.3"
pattern_title: "CHR Authoring for a CG‑Frame: Characteristics, Scales, Levels, Coordinates"
section_id: "G.3:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/G.3/G.3__011_rationale.md"
commit_sha: "169e3e09c04a4174ce4c26682cf181a0d255b6f7"
heading_path:
  - "G.3 — CHR Authoring for a CG‑Frame: Characteristics, Scales, Levels, Coordinates"
  - "G.3:10 — Rationale"
line_start: 137297
line_end: 137302
dependencies:
  - "A.10"
  - "A.15.2"
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
  - "C.2.1"
  - "E.10"
  - "E.5.1"
  - "E.5.3"
  - "F.0.1"
  - "F.1"
  - "F.17"
  - "F.18"
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
  - "CSLC lawfulness"
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

### G.3:10 - Rationale

CHR authoring states which measurements and operations downstream reasoning may use. By making scale/unit/polarity explicit, publishing legality and guard surfaces, and requiring provenance pins, CHR authoring prevents downstream mechanisms from silently inventing their own legality assumptions.

Using shared rules from `G.Core` keeps tri-state guards, penalty routing, set-return semantics and RSCR trigger kinds consistent across Part G. Its default index points to the pattern that defines each default. CHR defines the frame’s measurement kit.

