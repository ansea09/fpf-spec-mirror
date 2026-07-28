---
chunk_kind: "child"
pattern_id: "B.1.2"
pattern_title: "System Aggregation and Holon Delimitation"
section_id: "B.1.2:7"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.2/B.1.2__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "B.1.2 — System Aggregation and Holon Delimitation"
  - "B.1.2:7 — Common Anti-Patterns and How to Avoid Them"
line_start: 35606
line_end: 35615
dependencies:
  - "A.1"
  - "A.12"
  - "A.14"
  - "A.15.1"
  - "A.19"
  - "A.22"
  - "A.3.4"
  - "A.6.5"
  - "A.6.F"
  - "A.6.M"
  - "B.1"
  - "C.13"
  - "C.16"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.AD.BA"
keywords:
---

### B.1.2:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Box as boundary | A diagram rectangle determines system membership. | Name holon delimitation, identity rule, and part relations. |
| Supplier as component | External supplier or grid is treated as part of the system. | Use boundary-crossing relation, supply relation, commitment relation, A.6.C contract-language unpacking, evidence relation, or source-use relation. |
| Function block as module | A functional block is treated as a physical component. | Recover functional element, candidate bearer, and allocation relation separately. |
| Digital twin as part | Model or dashboard appears inside the system aggregate. | Use architecture-description, publication, evidence, or source-use owners. |
| Redundancy as arithmetic | Redundancy is averaged into a better system score. | Check characteristic scale and existing-whole explanation; use B.2 when the whole must be reidentified. |

