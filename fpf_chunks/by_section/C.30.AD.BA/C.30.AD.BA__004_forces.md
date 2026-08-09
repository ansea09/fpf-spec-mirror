---
chunk_kind: "child"
pattern_id: "C.30.AD.BA"
pattern_title: "Built-Asset Architecture Description and Reference Designation"
section_id: "C.30.AD.BA:1.1"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD.BA/C.30.AD.BA__004_forces.md"
commit_sha: "036c056e98c38522172c6b7b3ad08214281cc4e4"
heading_path:
  - "C.30.AD.BA — Built-Asset Architecture Description and Reference Designation"
  - "C.30.AD.BA:1.1 — Forces"
line_start: 60683
line_end: 60693
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.5"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.3.4"
  - "A.6.F"
  - "A.6.M"
  - "A.6.P"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.2.1"
  - "C.27"
  - "C.27.TA"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.TFS-REL"
  - "E.17"
  - "E.17.0"
  - "E.24.PUB"
  - "F.18"
  - "G.11"
keywords:
---

### C.30.AD.BA:1.1 - Forces

| Force | Tension |
| --- | --- |
| Long asset life vs changing descriptions | The built asset can retain identity while descriptions, model editions, sensor systems, representations, publications, and information uses change. |
| Many useful structures vs exact description identity | Spatial, functional, flow, module, interface, placement, control, and information structures can all matter, but every description still has one exact C.2.1 EntityOfConcern and every selected structure keeps its own A.22 identity. |
| Exchange interoperability vs FPF relation meaning | IFC and related exchange formats carry explicit object and relation data, but exchange content is source description until actual subject relations and selected structures are recovered under their direct owners. |
| Designation stability vs aspect dependence | A reference designation can make an object retrievable across descriptions while still depending on a declared structuring aspect, designation scheme, exact referent, and qualification window. |
| Auxiliary-view usefulness vs direct claim ownership | Cost, schedule, operation, maintenance, sustainability, and energy views can guide architecture work; their characteristic measurement, Work, temporal-claim adequacy, causal use, evidence, assurance, and currentness claims still require `C.16`, `A.15`, `C.27`, `C.28`, `A.10`, `B.3`, and `G.11`. |
| Live coupling vs currentness | Telemetry and simulations can update a digital-twin description rapidly; freshness and fidelity still bound each claim made from it and do not create physical change. |

