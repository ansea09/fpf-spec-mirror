---
chunk_kind: "child"
pattern_id: "A.12"
pattern_title: "Acting-Side Externalization and Reflexive Split"
section_id: "A.12:7"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.12/A.12__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "A.12 — Acting-Side Externalization and Reflexive Split"
  - "A.12:7 — Common Anti-Patterns and How to Avoid Them"
line_start: 23411
line_end: 23421
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2.1"
  - "A.2.6"
  - "A.2.7"
  - "A.3.4"
  - "A.6.RCD"
  - "A.7"
  - "B.2.5"
  - "C.13"
  - "C.2.1"
  - "E.17"
  - "E.24.PUB"
  - "F.6"
keywords:
---

### A.12:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Self-action literalism | "The system fixed itself" is accepted as one undivided claim. | Use `ReflexiveSplit@Context` and recover acting and changed positions. |
| Transformer kind inflation | The acting side is modeled as `U.Transformer`, as a special system kind, or as a provisional phrase placed in a `U.System` slot. | Before recognition retain the exact `U.Entity` and A.1 disposition or blocker and leave `actingSystemRef` unfilled. After recognition use the exact `U.System`; keep `TransformerSystemRole@Context` only when its local system-role-kind identity and the exact acting-side participation or assignment are current. |
| Boundary as object by word | Boundary or interaction words become durable root objects. | Recover the actual holon delimitation, boundary-crossing predicate, transformation, signal, evidence relation, source-use relation, or publication-use relation, and cite the pattern whose ClaimGraph defines or tests that claim. |
| Work success by action | Because a system acted, the work is treated as successful. | Use A.15.1 and evidence-use patterns for performed work and success. |
| Evidence by producer | The acting system's own output is accepted as enough evidence. | Use A.10 or stronger evidence-use and assurance patterns. |
| Manufacturing as containment | A tool or teacher changing another holon is treated as its containing whole. | Keep transformation and part-whole claims separate. |

