---
chunk_kind: "child"
pattern_id: "C.16"
pattern_title: "Measurement & Metrics Characterization (MM‑CHR)"
section_id: "C.16:3.1"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16/C.16__005_problem.md"
commit_sha: "1f413fcd23f4ea26956a45d67dde57bb233f6ad9"
heading_path:
  - "C.16 — Measurement & Metrics Characterization (MM‑CHR)"
  - "C.16:3.1 — Problem"
line_start: 46732
line_end: 46735
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "B.3"
  - "C.26"
  - "C.26.1"
keywords:
  - "CSLC"
  - "U.DHCMethod(Ref)"
  - "U.EvidenceStub"
  - "U.Measure"
  - "U.Unit"
  - "direct comparability"
  - "measurement"
  - "measurement template"
  - "polarity"
  - "probe-changing-state"
  - "scoring method disclosure"
  - "shared-frame check"
---

### C.16:3.1 - Problem

Across FPF patterns, people say “score”, “metric”, “rating”, “property”. Without a shared substrate, numbers drift: *42 of what? on which scale? comparable to whom?* C.16 eliminates drift by requiring every metric notion to **bind** to **one** Characteristic and **one** Scale, and by **separating** Characteristic/template bindings from descriptions and ScoringMethods. The result is **portable meaning**: a measure is always readable as a **Coordinate on a declared Scale of a named Characteristic**, with a principled path to evidence.

