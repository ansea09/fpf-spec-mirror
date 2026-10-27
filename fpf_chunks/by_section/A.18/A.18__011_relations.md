---
chunk_kind: "child"
pattern_id: "A.18"
pattern_title: "Minimal CSLC in Kernel (Characteristic ⟷ Scale ⟷ Level ⟷ Coordinate) (A.CSLC‑KERNEL)"
section_id: "A.18:10"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/A.18/A.18__011_relations.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "A.18 — Minimal CSLC in Kernel (Characteristic ⟷ Scale ⟷ Level ⟷ Coordinate) (A.CSLC‑KERNEL)"
  - "A.18:10 — Relations"
line_start: 34420
line_end: 34431
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

### A.18:10 - Relations

- **Extends A.17:** uses its Characteristic vocabulary and entity/relation arity distinction, then binds each template to a Scale and its reported values. A.17 supplies the participant and naming rules; A.18 supplies the CSLC structure.

- **Used by C.16 and A.19:** C.16 supplies measurement methods, models, conditions and uncertainty; A.19 and A.19.CHR use Characteristic and Scale meanings in spaces and characterization templates. CSLC is the shared value structure, not a storage or computation implementation.

- **Supports dynamic reasoning:** A.3.3 uses Characteristics and Scales to specify state variables. Linking a five-level performance rating to a probability needs a justified model or correspondence between their meanings. A ScoringMethod is appropriate when the result is an evaluative Score.

- **Coordinates with assurance patterns:** A receiving assurance or trust claim may use measurements or Scores whose Characteristic, Scale, model conditions and uncertainty are recoverable. CSLC conformance does not establish comparability merely because values share a 0–1 or percentage encoding. Apply B.3 to the named assurance claim; a cross-domain comparison, normalization or aggregation additionally needs its own declared rule and applicable evidence.

- **Lexical and external correspondence:** E.10 governs the measurement vocabulary; A.18 applies A.17's distinction between measurement interpretation and use-dependent preference to CSLC templates. Defined scale types and units make the terms used in quantity measurement recoverable for an F.9 correspondence with external measurement standards.

