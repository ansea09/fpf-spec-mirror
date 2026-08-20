---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
section_id: "C.3.4:4"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__006_forces.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
  - "C.3.4:4 — Forces"
line_start: 45329
line_end: 45337
dependencies:
  - "A.2.6"
  - "C.2.1"
  - "C.3.1"
  - "C.3.2"
  - "C.3.3"
  - "C.3.A"
  - "F.9"
keywords:
---

### C.3.4:4 - Forces

| Force | Tension to resolve |
| --- | --- |
| Local specialization versus common core | A context needs local tailoring without forking the base kind. |
| Expressivity versus determinism | The declaration must express real constraints and remain reproducibly checkable at guard time. |
| Context versus entity constraints | Conditions over `U.ContextSlice` belong to Scope; conditions over the candidate belong to the classification judgment. |
| Reuse versus proliferation | Reuse is useful, but a stable conceptual distinction may warrant a separately identified local kind and independently obtaining `U.SubkindOf` relation. |

