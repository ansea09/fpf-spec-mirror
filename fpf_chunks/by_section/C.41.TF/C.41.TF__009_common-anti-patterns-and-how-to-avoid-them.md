---
chunk_kind: "child"
pattern_id: "C.41.TF"
pattern_title: "Construct a Checklist Template That Preserves Its Questions"
section_id: "C.41.TF:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.41.TF/C.41.TF__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "55ef163f91d42b48785bd297b50322e072d0a950"
heading_path:
  - "C.41.TF — Construct a Checklist Template That Preserves Its Questions"
  - "C.41.TF:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 94456
line_end: 94464
dependencies:
  - "C.37"
  - "C.41"
  - "C.41.OF"
  - "C.41.UA"
keywords:
---

### C.41.TF:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| A copied tick survives while its question or edition changes. | Preserve the association or reopen the answer for the new question. |
| Every blank means failure, or every filled cell means success. | Preserve the meanings of absence, unresolved answers and supported negative answers. |
| A timestamp silently becomes attainment time. | Name whether it records observation, entry or an independently observed change. |
| Each heading is treated as a new type or state. | Recover the subject and relation the heading expresses; keep layout as representation. |

