---
chunk_kind: "child"
pattern_id: "C.30.AD.BA"
pattern_title: "Built-Asset Architecture Description and Reference Designation"
section_id: "C.30.AD.BA:6.1"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD.BA/C.30.AD.BA__010_bias-annotation.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "C.30.AD.BA — Built-Asset Architecture Description and Reference Designation"
  - "C.30.AD.BA:6.1 — Bias-Annotation"
line_start: 56031
line_end: 56040
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

### C.30.AD.BA:6.1 - Bias-Annotation

| Bias | How C.30.AD.BA prevents it |
| --- | --- |
| Model-as-asset bias | The BIM model, IFC exchange, dashboard, or digital twin remains an architecture-description, source, publication, or view object, not the physical built asset. |
| Designation-as-identity bias | ISO/IEC 81346-style designation is treated as a designation relation with aspect and admissible-use boundaries, not as universal identity proof. |
| Currentness-as-assurance bias | Sensor freshness or model edition bounds use; evidence, assurance, gate, decision, and release claims keep their direct owners. |
| Design-run collapse | `DesignRunTagRefs` keep design-side model material, run-side telemetry, operation records, maintenance work, and physical transformations distinct. |
| Standard-as-ontology bias | Built-asset standards inform source and exchange discipline without importing their classifications as FPF U-kinds. |

