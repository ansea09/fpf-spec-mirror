---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:26"
section_title: "Bundle and endpoint interaction"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__027_bundle-and-endpoint-interaction.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:26 — Bundle and endpoint interaction"
line_start: 89930
line_end: 89937
dependencies:
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.6.3.CSC"
  - "A.6.5"
  - "A.6.9"
  - "B.3"
  - "C.26"
  - "C.26.1"
  - "C.26.2"
  - "C.29"
  - "E.10.D1"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9.1"
  - "U.BoundedContext"
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

### F.9:26 - Bundle and endpoint interaction

Viewpoint bundles, quality bundles, dashboards, reports, and endpoint bundles may cite Bridges, but they do not absorb bridge semantics. F.9 remains the pattern for cross-context alignment, while the citing bundle keeps its own ontology.

When a quality-family claim crosses contexts, bridge loss and `CL` affect what may be compared or reused, but they do not retype the quality family itself. Any resulting assurance penalty feeds B.3 rather than changing the ontology of the quality bundle.

A `F.9.1` stance overlay may help readers interpret a Bridge, but the Bridge Card remains primary. If the overlay overstates bridge kind, direction, `CL`, Loss Notes, or admitted use, narrow or remove the overlay.

