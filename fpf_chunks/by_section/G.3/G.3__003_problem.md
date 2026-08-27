---
chunk_kind: "child"
pattern_id: "G.3"
pattern_title: "CHR Authoring for a CG‑Frame: Characteristics, Scales, Levels, Coordinates"
section_id: "G.3:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/G.3/G.3__003_problem.md"
commit_sha: "322625be006f38158e4e7d600f662558f03df77a"
heading_path:
  - "G.3 — CHR Authoring for a CG‑Frame: Characteristics, Scales, Levels, Coordinates"
  - "G.3:2 — Problem"
line_start: 100243
line_end: 100254
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

### G.3:2 - Problem

Without a disciplined CHR authoring layer, teams repeatedly produce “measurable slots” that are *numerically manipulable but semantically unlawful*:

* **Meaning leaks** when the same token is reused after its referent or sense, bearer, scope, validity window, evidence basis, or intended use has changed.
* **Illicit arithmetic** (e.g., averaging ordinals, mixing units, laundering polarity).
* **Hidden normalizations** that silently change scale type, polarity, or admissible transforms.
* **Unreproducible comparisons** (missing edition pins for methods/distances/policies; unclear reference plane).
* **Unscoped reuse** (the characteristic or scale lacks an exact edition, bearer, scope and validity window, reference plane, evidence basis, or intended downstream use; any relation needed for reuse is left unstated).
* **Un-auditable aggregation** (no explicit legality surface and guard surface; no proof hooks; unclear Γ‑fold governing-definition assignment).
* **Refresh chaos** (changes in names/editions/policies do not map to typed RSCR causes).

