---
chunk_kind: "child"
pattern_id: "B.1.2"
pattern_title: "System Aggregation and Holon Delimitation"
section_id: "B.1.2:7"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.2/B.1.2__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "B.1.2 — System Aggregation and Holon Delimitation"
  - "B.1.2:7 — Common Anti-Patterns and How to Avoid Them"
line_start: 36896
line_end: 36905
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.19"
  - "A.22"
  - "A.3.4"
  - "A.6.F"
  - "A.6.M"
  - "B.1"
  - "B.2"
  - "B.3"
  - "C.11"
  - "C.13"
  - "C.16"
  - "C.2.1"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.AD.BA"
  - "C.32.PAD"
  - "E.17"
keywords:
---

### B.1.2:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Box as boundary | A diagram rectangle determines system membership. | Recover system identity and every obtaining part and crossing relation; stop if those facts answer the question. If a distinct use-relative boundary choice remains, name the applicable C.11 `ChoiceResult`, C.32.PAD `ArchitectureDecisionRelation@Project`, or another explicitly admitted direct result; otherwise stop with the missing-governor blocker. Add a C.2.1 episteme only when that claim must persist; use an A.22 selected structure only when its four discriminators are independently grounded. |
| Supplier as component | External supplier or grid is treated as part of the system. | Recover the exact supply, commitment, evidence, source-use, or other crossing relation under its subject pattern; infer no parthood. |
| Function block as module | A functional block is treated as a physical component. | Recover the exact functional element, proposed bearer, allocation or correspondence, and any obtaining part relation separately. |
| Digital twin as part | A model or dashboard appears inside the system aggregate. | Use description, representation, publication, evidence, source-use, and naming patterns; add parthood only if its direct predicate independently obtains. |
| Redundancy as arithmetic | Redundancy is averaged into a better system score. | Check characteristic scale and existing-whole explanation; use B.2 when the whole must be reidentified. |

