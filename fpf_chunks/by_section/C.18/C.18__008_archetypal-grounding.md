---
chunk_kind: "child"
pattern_id: "C.18"
pattern_title: "Open-Ended Search Archive and Front Stewardship"
section_id: "C.18:6"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.18/C.18__008_archetypal-grounding.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "C.18 — Open-Ended Search Archive and Front Stewardship"
  - "C.18:6 — Archetypal Grounding"
line_start: 60469
line_end: 60488
dependencies:
  - "A.15"
  - "A.19"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "C.11"
  - "C.11.CRC"
  - "C.16"
  - "C.19"
  - "C.28"
  - "C.30"
  - "C.32"
  - "C.32.P2S"
  - "C.35"
  - "C.36"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.23"
  - "E.24.PUB"
  - "F.17"
  - "F.18"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "currentness"
  - "descriptors"
  - "exploration archive"
  - "generation"
  - "lineage"
  - "non-dominated front"
  - "open-ended search"
  - "refresh"
  - "retained exploration value"
  - "telemetry"
---

### C.18:6 - Archetypal Grounding

**System-facing case.** A robotics team generates gait variants. The front records non-dominated speed and energy relations under declared measures. The archive retains diverse coordination patterns because some are stepping stones for new terrain. Telemetry reports coverage. A selected-set result may later be declared through `G.5`. If it must be available to an audience, use `E.17` for its source-backed publication face and return to source and `E.24.PUB` for the publication occurrence and availability. Performed test runs use A.15.

**Architecture case.** A cooling-module project keeps an archive of modular layout variants and a front over maintainability and energy use. C.18 records descriptors, archive policy, front relation, and telemetry. Use C.30 to name the selected structure and affected architecture characteristic, then decide whether to make an architecture move with a retained variant.

**Cultural case.** A dance-lab project generates movement variants around several source labels. C.18 records generated variants, descriptors, archive membership, front relation, and lineage. Use C.36 to determine whether the lab is deliberately changing the cultural practice; use F.17/F.9 when an actual label correspondence is needed and F.18 when the work needs a durable new name.

**Completed front/archive comparison.** Suppose three eligible cooling-module candidates have comparable readings for energy per operating cycle and time for the same service operation. Both quantities are minimized under the declared comparator.

| Candidate | Energy per cycle | Service-operation time |
| --- | --- | --- |
| A | 8 kWh | 20 min |
| B | 10 kWh | 25 min |
| C | 12 kWh | 15 min |

A dominates B because both readings are lower. A and C are incomparable: A uses less energy, while C takes less service time. The front is therefore `{A, C}`. The project's archive policy also retains one representative of every admitted connector family for later recombination. B is the only available representative of family J, so the archive retains B even though B is absent from the front. That retention is a coverage decision under the stated policy, not evidence that B performs better or will produce a successful later design.

“Front `{A, C}`; retain B in the archive as the family-J representative” answers this question. No selected-set declaration or design choice follows automatically. If another J-family variant arrives, reconsider retention under the same policy; if the comparator or measurement basis changes, recompute the affected front relations.

