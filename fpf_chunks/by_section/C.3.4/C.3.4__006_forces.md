---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Tailor the Use of an Existing Kind"
section_id: "C.3.4:4"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__006_forces.md"
commit_sha: "55ef163f91d42b48785bd297b50322e072d0a950"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Tailor the Use of an Existing Kind"
  - "C.3.4:4 — Forces"
line_start: 58528
line_end: 58538
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
| Local specialization vs common core | A use needs tailoring without forking the base kind. |
| Expressivity vs determinism | Constraints must remain reproducibly checkable. |
| Applicability vs uncertainty | A candidate or slice outside the declaration receives no judgment. In an admissible case, `unknown` means that the available facts do not settle the combined criterion. |
| Scope vs candidate constraints | Conditions on ClaimScope stay under A.2.6; conditions on the candidate enter classification. |
| Reuse vs proliferation | Stable conceptual distinctions may warrant a separately identified kind, but declaration reuse alone does not. |
| Locality vs identity | A changed locality prompts comparison of membership distinctions, not automatic bridging. |

