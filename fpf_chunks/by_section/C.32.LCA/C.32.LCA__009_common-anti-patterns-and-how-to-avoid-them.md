---
chunk_kind: "child"
pattern_id: "C.32.LCA"
pattern_title: "Construct and Compare a Control Architecture"
section_id: "C.32.LCA:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.LCA/C.32.LCA__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "996ae39ce00b4a9c9b59b48a4f1446b2175dcffb"
heading_path:
  - "C.32.LCA — Construct and Compare a Control Architecture"
  - "C.32.LCA:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 77007
line_end: 77018
dependencies:
  - "A.3.3.PI"
  - "B.2.5"
  - "C.30.LCA"
  - "C.32"
  - "C.32.MWA.PP"
keywords:
---

### C.32.LCA:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Why it fails in this use | Repair |
| --- | --- | --- |
| Draw strategy, planning and execution and call the architecture complete | The drawing leaves the connecting information, authority and feasible actions unspecified. | Derive the division from the needed decisions and construct each consequential exchange. |
| Give every local unit the whole resource limit | Simultaneously valid local choices can exceed the shared capacity. | Establish a joint allocation or coordination rule and its timing. |
| Forward every update immediately | Irrelevant changes consume attention; premature preparation can waste or reserve scarce resources. | Identify the receiving action and compare early preparation with waiting. |
| Escalate every exception | A decision can arrive after the last useful action or at a participant without the needed means. | Bound the actual response path or construct a qualified local continuation. |
| Call separate controller stability a whole-system guarantee | Reference changes, delay, estimation and interactions can violate the individual premises. | Derive or obtain the joint behavior under the real interface. |
| Treat a promise or benchmark average as a hard bound | The required availability, tail behavior or operating condition may be unsupported. | Use the warranted bound, uncertainty or conditional claim and change the reliance accordingly. |
| Improve the local rate while weakening the demanded outcome | The comparison changes the task and manufactures a gain. | Hold the receiving demand fixed or make the changed commitment an explicit alternative. |

