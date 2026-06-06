---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment & Bridge across Contexts"
section_id: "F.9:25"
section_title: "Bundle and Endpoint Interaction Law"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__027_bundle-and-endpoint-interaction-law.md"
commit_sha: "e3fedf42dc7cb5d12905913b5a0b0e951ed7d254"
heading_path:
  - "F.9 — Alignment & Bridge across Contexts"
  - "F.9:25 — Bundle and Endpoint Interaction Law"
line_start: 71310
line_end: 71320
dependencies:
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.9"
  - "B.3"
  - "C.16.Q"
  - "C.25"
  - "C.26"
  - "C.26.1"
  - "E.10.D1"
  - "E.17.1"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.7"
  - "F.8"
  - "F.9.1"
  - "U.BoundedContext"
  - "U.Mechanism"
keywords:
  - "Bridge-supported use"
  - "CL"
  - "bridge"
  - "bridge reading"
  - "cross-context alignment"
  - "direction"
  - "loss notes"
  - "state export"
  - "weakest-link scope"
---

### F.9:25 - Bundle and Endpoint Interaction Law

#### F.9:25.1 - Viewpoint and bundle interaction
Viewpoint bundles, quality bundles, and other endpoint bundles may cite Bridges, but they do not absorb bridge semantics. `F.9` remains the pattern for cross-context alignment, while the citing bundle keeps its own ontology.

#### F.9:25.2 - Quality-family interaction
When a quality family claim crosses contexts, bridge loss and `CL` affect what may be compared or reused, but they do not retype the quality family itself. Any resulting assurance penalty feeds `R` rather than changing the ontology of `F`, `G`, or the Q-Bundle head.

#### F.9:25.3 - Overlay interaction rule
A `F.9.1` stance overlay may help readers interpret a bridge, but the bridge card remains primary. If the overlay overstates the bridge kind, direction, `CL`, or Loss Notes, the card wins and the overlay should be narrowed or removed.

