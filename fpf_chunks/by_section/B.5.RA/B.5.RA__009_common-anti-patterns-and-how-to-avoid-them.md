---
chunk_kind: "child"
pattern_id: "B.5.RA"
pattern_title: "Recover an Argument for Its Next Use"
section_id: "B.5.RA:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.RA/B.5.RA__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "B.5.RA — Recover an Argument for Its Next Use"
  - "B.5.RA:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 42138
line_end: 42148
dependencies:
  - "B.5"
  - "B.5.MPC"
  - "B.5.RC"
  - "C.2.8"
  - "C.37"
keywords:
---

### B.5.RA:8 - Common Anti-Patterns and How to Avoid Them

| Failure in the working situation | Repair |
| --- | --- |
| Paraphrasing successive claims while the inference remains missing | Apply the relevant definition, rule or earlier result to the transition's actual premises. |
| Checking local steps while failing to explain why a lemma or construction appears | Recover the difficulty that contribution resolves and connect it to the conclusion. |
| Treating several uses of one premise as several independent grounds | Keep the common prerequisite visible and examine its role in the needed branches. |
| Promoting a temporary assumption to an established premise | Recover the subargument and the conclusion obtained when that assumption is discharged. |
| Using one example to claim that the general statement has been proved | Recover the argument that covers the stated domain; retain the example as an illustration of it. |
| Demanding a complete reproof when the task only needs an established result under its stated conditions | Use that result at the needed level; open its internals when the new question requires them. |

