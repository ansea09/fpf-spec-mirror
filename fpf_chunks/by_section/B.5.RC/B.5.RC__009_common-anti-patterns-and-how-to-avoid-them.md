---
chunk_kind: "child"
pattern_id: "B.5.RC"
pattern_title: "Recover a Construction from Its Description"
section_id: "B.5.RC:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.RC/B.5.RC__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "B.5.RC — Recover a Construction from Its Description"
  - "B.5.RC:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 41952
line_end: 41961
dependencies:
  - "A.6.3.RT"
  - "B.5"
  - "B.5.RA"
  - "C.29.1"
  - "C.29.2"
  - "C.39"
keywords:
---

### B.5.RC:8 - Common Anti-Patterns and How to Avoid Them

| Failure in the working situation | Repair |
| --- | --- |
| Repeating “construct an object with property P” when the obtaining operation is missing | Recover the last producing operation and trace its prerequisites to available inputs. |
| Flattening a construction into a list that loses a shared object or a joint condition | Preserve those dependencies and perform each operation only when its inputs are available together. |
| Filling an omitted operation with a plausible guess and attributing it to the source | Name the addition and establish how it works, or return to the source for the missing operation. |
| Treating a successful small case as a result for all inputs | Recover which conditions carry the general argument and which belong only to the trial. |
| Continuing source reconstruction after the intended use is already possible | Use the recovered construction; reopen only for a further question that requires more. |

