---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
section_id: "C.3.4:4"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__006_forces.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
  - "C.3.4:4 — Forces"
line_start: 46084
line_end: 46094
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
| Expressivity vs determinism | Real constraints must remain reproducibly checkable. |
| Applicability vs uncertainty | Candidate/slice mismatch stops before the judgment; missing facts preserve `unknown`. |
| Scope vs candidate constraints | Conditions on ClaimScope stay under A.2.6; conditions on the candidate enter classification. |
| Reuse vs proliferation | Stable conceptual distinctions may warrant a separately identified kind, but declaration reuse alone does not. |
| Locality vs identity | A changed locality prompts comparison of membership distinctions, not automatic bridging. |

