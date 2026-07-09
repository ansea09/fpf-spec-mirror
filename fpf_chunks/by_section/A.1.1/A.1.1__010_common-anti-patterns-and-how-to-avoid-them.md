---
chunk_kind: "child"
pattern_id: "A.1.1"
pattern_title: "U.BoundedContext Semantic Frame"
section_id: "A.1.1:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.1/A.1.1__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "A.1.1 — U.BoundedContext Semantic Frame"
  - "A.1.1:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 1938
line_end: 1947
dependencies:
  - "A.1"
  - "A.15"
  - "A.6.5"
  - "C.2.1"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.D1"
  - "E.24"
  - "E.24.PUB"
  - "F.0.1"
  - "F.18"
  - "F.9"
  - "U.Holon"
keywords:
---

### A.1.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Domain as context | "Healthcare" or "physics" is used where local meaning must be decided. | Name a specific bounded context or keep the broad label informative. |
| Same spelling as sameness | A word used in two contexts is treated as equivalent. | Write a bridge relation or keep the meanings separate. |
| Context as storage place | Everything mentioned in one context is treated as part of that context. | Use the appropriate slot relation: interpreted-in, governed-by, described-under, bridged-to, or part-of. |
| Global role | "Owner", "operator", or "reviewer" is used without a context. | Name the role value and the bounded context that defines it. |
| Time as context by reflex | Design-time and run-time become separate contexts even when meaning is unchanged. | Use temporal patterns or window patterns unless the local vocabulary or invariants actually change. |

