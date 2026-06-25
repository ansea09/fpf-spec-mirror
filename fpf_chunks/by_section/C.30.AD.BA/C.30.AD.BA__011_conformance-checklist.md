---
chunk_kind: "child"
pattern_id: "C.30.AD.BA"
pattern_title: "Built-Asset Architecture Description and Reference Designation"
section_id: "C.30.AD.BA:8"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD.BA/C.30.AD.BA__011_conformance-checklist.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "C.30.AD.BA — Built-Asset Architecture Description and Reference Designation"
  - "C.30.AD.BA:8 — Conformance Checklist"
line_start: 55393
line_end: 55402
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

### C.30.AD.BA:8 - Conformance Checklist

| ID | Check | Why it matters |
| --- | --- | --- |
| CC-BA-1 | The built asset or facility is named as `describedHolonRef`, and the architecture claim is named as `architectureClaimRef`. | Prevents description-as-asset and description-as-architecture collapse. |
| CC-BA-2 | Selected structures or structure kinds are named for each used view. | Prevents BIM or dashboard labels from replacing structure recovery. |
| CC-BA-3 | Reference designations name their scheme, designated entity, aspect or view, correspondence, and admissible use. | Prevents designation codes from becoming identity or parthood proof. |
| CC-BA-4 | Digital-twin, sensor, operation, and maintenance material carries source, currentness, and `DesignRunTag` boundaries when used across design and run material. | Prevents design-side and run-side objects from being silently merged. |
| CC-BA-5 | Evidence, assurance, gate, decision, work, and causal claims are returned to their governing patterns. | Keeps built-asset description useful without overclaiming authority. |

