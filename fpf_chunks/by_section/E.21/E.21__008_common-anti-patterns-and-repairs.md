---
chunk_kind: "child"
pattern_id: "E.21"
pattern_title: "FPF Pattern-Quality Evaluation CharacteristicSpace"
section_id: "E.21:7"
section_title: "Common anti-patterns and repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/E.21/E.21__008_common-anti-patterns-and-repairs.md"
commit_sha: "eaafd3a43b9173706e1f8388a3bc94c6445397e4"
heading_path:
  - "E.21 — FPF Pattern-Quality Evaluation CharacteristicSpace"
  - "E.21:7 — Common anti-patterns and repairs"
line_start: 67533
line_end: 67546
dependencies:
  - "A.17-A.19"
  - "A.19.ECS"
  - "A.6.P"
  - "C.16"
  - "C.2.P"
  - "C.25"
  - "E.10"
  - "E.19"
  - "E.2.DA"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9.DA"
  - "F.18"
  - "J.4"
keywords:
---

### E.21:7 - Common anti-patterns and repairs

| Anti-pattern | Repair |
|---|---|
| **Score illusion.** `Pattern quality = 87/100`. | Use ordinal coordinate values; no arithmetic aggregation. |
| **Two-column table.** Coordinate/value table has no rationale. | Add `ShortRationale` for every coordinate. |
| **Floor as omission.** A floor evaluation omits maturity, SoTA, formal, corpus, or evolution coordinates. | Keep floor low if needed; evaluate all coordinates. |
| **Administrative proxy.** "4 because landed" or "3 because not externally reviewed". | Evaluate pattern content. |
| **Comparator-free or locus-free maturity.** `MaturePatternParity... = 4` by impression, comparator IDs only, or category list such as "frame, first move, exits, CC, SoTA, relations". | Name mature comparison patterns and use the maturity-discharge payload: comparator, selected ingredient, current locus, and missing/lowering item. Without that payload, cap at `3`. |
| **Omission account as maturity.** A note explaining absence raises the value. | Add content to body/exact neighbour, lower value, or narrow use. |
| **Semio-biased maturity.** Non-semio pattern is judged by episteme/publication exemplars only. | Include non-epistemic mature comparators and score action on the primary `EntityOfConcern`. |
| **Apparatus maximalism.** Every pattern gets evidence cards, telemetry, archives, and companions. | Keep evidence compact unless it changes value, status, stop, or candidate comparison. |
| **Quality veto theatre.** "Not ready" has no exact E.21 locus, evidence, status effect, and repair. | Rewrite as an `E.21` finding or remove the veto. |

