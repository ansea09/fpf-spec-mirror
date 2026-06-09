---
chunk_kind: "child"
pattern_id: "G.3"
pattern_title: "CHR Authoring for a CG‑Frame: Characteristics, Scales, Levels, Coordinates"
section_id: "G.3:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/G.3/G.3__003_problem.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "G.3 — CHR Authoring for a CG‑Frame: Characteristics, Scales, Levels, Coordinates"
  - "G.3:2 — Problem"
line_start: 77781
line_end: 77792
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

### G.3:2 - Problem

Without a disciplined CHR authoring layer, teams repeatedly produce “measurable slots” that are *numerically manipulable but semantically unlawful*:

* **Meaning leaks** across contexts (same token, different referent/sense).
* **Illicit arithmetic** (e.g., averaging ordinals, mixing units, laundering polarity).
* **Hidden normalizations** that silently change scale type, polarity, or admissible transforms.
* **Unreproducible comparisons** (missing edition pins for methods/distances/policies; unclear reference plane).
* **Unscoped reuse** (no explicit bridge and loss notes; unclear `entityOfConcern` changes).
* **Un-auditable aggregation** (no explicit legality surface and guard surface; no proof hooks; unclear Γ‑fold governing-definition assignment).
* **Refresh chaos** (changes in names/editions/policies do not map to typed RSCR causes).

