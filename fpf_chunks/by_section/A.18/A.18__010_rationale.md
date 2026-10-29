---
chunk_kind: "child"
pattern_id: "A.18"
pattern_title: "Minimal CSLC in Kernel (Characteristic ⟷ Scale ⟷ Level ⟷ Coordinate) (A.CSLC‑KERNEL)"
section_id: "A.18:9"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.18/A.18__010_rationale.md"
commit_sha: "c3b34de07a6bd2df85c7081a4c367fd09978079c"
heading_path:
  - "A.18 — Minimal CSLC in Kernel (Characteristic ⟷ Scale ⟷ Level ⟷ Coordinate) (A.CSLC‑KERNEL)"
  - "A.18:9 — Rationale"
line_start: 34436
line_end: 34449
dependencies:
  - "A.17"
  - "A.19"
  - "A.19.CHR"
  - "A.19.CN"
  - "B.3"
  - "C.16"
  - "G.0"
keywords:
  - "CSLC"
  - "Characteristic"
  - "Coordinate"
  - "Level"
  - "Scale"
  - "lawful comparability"
  - "measurement interpretability"
  - "no illegal averaging"
  - "one-characteristic-one-scale rule"
  - "ordinal vs cardinal scale"
  - "scale order"
  - "use-dependent preference"
---

### A.18:9 - Rationale

Defining a measurement template makes the aspect, Scale and value meaning available for later use. The receiving practitioner can reuse that definition instead of reconstructing it from the reported number. The following choices support that result:

- **Shared structure, distinct domain rules:** a usability rating and a throughput measurement both identify an aspect, Scale and reading. Their common structure exposes the difference rather than supplying a common calculation or evidence rule.

- **Comparability vs. freedom:** Measurement comparison needs a common interpretation of the Characteristic, Scale and measurement conditions. A unit conversion can establish that interpretation across compatible presentations. Preference answers a further question: which result serves the intended use? The same temperature Scale supports identifying the hotter sample, choosing a cooling intervention or maintaining a target. Only the latter uses add a preferred direction or target rule.

- **Preserved information:** an ordinal Scale states order without asserting distances. An interval or ratio model can support further calculations only when its additional assumptions are justified; wanting an average is not a reason to assume such a model.

- **Optional Levels:** named tiers make category boundaries recoverable where the Scale uses them. A continuous measurement needs no Level labels unless an explicit categorization is introduced.

- **Separate structure and method:** the same CSLC structure can describe measurements made through different methods. Domain measurement patterns supply their procedures, applicability and evidence conditions; sharing the template does not make those methods interchangeable.

