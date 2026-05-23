---
chunk_kind: "child"
pattern_id: "C.25"
pattern_title: "Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
section_id: "C.25:18"
section_title: "Bundle Decomposition and Comparison Law"
source_path: "FPF-Spec.md"
output_path: "by_section/C.25/C.25__019_bundle-decomposition-and-comparison-law.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "C.25 — Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
  - "C.25:18 — Bundle Decomposition and Comparison Law"
line_start: 43520
line_end: 43530
dependencies:
  - "A.15"
  - "A.16.0"
  - "A.18"
  - "A.2.6"
  - "A.6.1"
  - "A.6.Q"
  - "B.3"
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.2.2a"
  - "C.26.3"
  - "F.9"
  - "F.9.1"
keywords:
  - "admissible quality-family use"
  - "characteristic plus scope"
  - "endpoint classification"
  - "failure mode"
  - "ility"
  - "mechanism/status slots"
  - "proxy metric"
  - "quality bundle"
  - "quality family"
  - "viability envelope"
---

### C.25:18 - Bundle Decomposition and Comparison Law

#### C.25:18.1 - Local decomposition rule
A family label may remain stable while its internal slots differ materially across contexts. Conforming comparison therefore starts by aligning the bundle decomposition: scope slots with scope slots, measure slots with measure slots, mechanism/status slots with their own kinds, and evidence/window slots with their own kinds. Comparing one bundle's measure directly to another bundle's mechanism claim is a category error even if both sit under the same family label.

#### C.25:18.2 - Narrow slice versus whole family
A context may admissibly extract one narrow slice from a broader Q-Bundle and publish that slice as a single CHR characteristic, but the publication should say that the slice is only one member of the broader family. What is not admissible is to report the slice as though it exhausted the entire family claim.

#### C.25:18.3 - Cross-context family comparison
Cross-context comparison of quality families should proceed through explicit bundle alignment and, where needed, `F.9` bridge discipline on the relevant heads or slots. The bundle ontology stays in `C.25`; bridge loss, translation-relation adequacy, and cross-context penalties remain outside the bundle itself.

