---
chunk_kind: "child"
pattern_id: "G.3"
pattern_title: "CHR Authoring for a CG‑Frame: Characteristics, Scales, Levels, Coordinates"
section_id: "G.3:8"
section_title: "Common Anti‑Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/G.3/G.3__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "G.3 — CHR Authoring for a CG‑Frame: Characteristics, Scales, Levels, Coordinates"
  - "G.3:8 — Common Anti‑Patterns and How to Avoid Them"
line_start: 74389
line_end: 74397
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

### G.3:8 - Common Anti‑Patterns and How to Avoid Them

* **Hidden cardinalization.** Don’t treat ordinal encodings as interval/ratio; do publish coordinate policies that explicitly preserve order‑only invariants and forbid arithmetic upgrades.
* **Unit laundering.** Don’t add or average quantities with incompatible units; do force explicit unit discipline and legality checks via MM‑CHR governing definitions.
* **Polarity drift.** Don’t rely on “higher is better” implicitly; do publish polarity explicitly and make downstream use auditable.
* **Threshold leakage into CHR.** Don’t embed policy cut‑offs in CHR; do keep thresholds in CAL acceptance artefacts.
* **Unpinned semantics.** Don’t cite “the metric” or “the distance” without edition pins; do require edition‑pinned references when semantics affect interpretation.
* **Unscoped reuse.** Don’t reuse CHR terms across contexts without explicit import and loss notes; do keep crossings explicit and auditable (pinned through `G.Core`).

