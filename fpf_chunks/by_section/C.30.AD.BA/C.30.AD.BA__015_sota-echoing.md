---
chunk_kind: "child"
pattern_id: "C.30.AD.BA"
pattern_title: "Built-Asset Architecture Description and Reference Designation"
section_id: "C.30.AD.BA:10.1"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD.BA/C.30.AD.BA__015_sota-echoing.md"
commit_sha: "9b6d71cff42a9ac45e46a2be2d9450f766868bc4"
heading_path:
  - "C.30.AD.BA — Built-Asset Architecture Description and Reference Designation"
  - "C.30.AD.BA:10.1 — SoTA-Echoing"
line_start: 55130
line_end: 55139
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
  - "A.6.M"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.27"
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
  - "E.17.1"
  - "E.17.2"
  - "E.24.PUB"
  - "F.18"
keywords:
---

### C.30.AD.BA:10.1 - SoTA-Echoing

| Source family | What it contributes | FPF adoption stance | Practitioner implication |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010 architecture-description practice | Separates architecture of an entity from architecture description, views, viewpoints, and correspondence. | Adopt through `C.30.AD` and specialize here for built assets. | Keep built asset, architecture claim, description, view, and publication separate. |
| ISO 19650 information management for built assets | Treats information management across built-asset life as a serious engineering concern. | Adopt as practice discipline, not as FPF ontology. | Asset information needs source, edition, currentness, and admissible-use boundaries. |
| IFC / ISO 16739 and openBIM practice | Provides standardized digital descriptions of built assets, properties, and relations. | Use as exchange and description discipline. | Tool-readable structure is not evidence, assurance, gate passage, or architecture adequacy by itself. |
| ISO/IEC 81346 reference designation | Provides aspect-sensitive reference designation across object descriptions. | Adopt as designation discipline, not as a code-list ontology import. | A designation coordinates views; it does not prove parthood, function, or identity across every use. |
| Digital-twin practice for buildings and manufacturing | Connects BIM, asset metadata, sensors, maintenance, and operations descriptions. | Adopt as source and description discipline with `DesignRunTag` boundaries. | A digital twin may guide action, but the physical asset, description, telemetry, work, and evidence remain distinct. |

