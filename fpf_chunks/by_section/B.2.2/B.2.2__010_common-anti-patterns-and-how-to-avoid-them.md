---
chunk_kind: "child"
pattern_id: "B.2.2"
pattern_title: "Meta-System Transition - System Specialization of MHT"
section_id: "B.2.2:7"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.2/B.2.2__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "B.2.2 — Meta-System Transition - System Specialization of MHT"
  - "B.2.2:7 — Common Anti-Patterns and How to Avoid Them"
line_start: 37758
line_end: 37767
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2.1"
  - "A.2.2"
  - "A.22"
  - "A.3.4"
  - "A.6.F"
  - "B.1.2"
  - "B.2"
  - "B.2.4"
  - "B.2.5"
  - "B.3"
  - "B.3.5"
  - "C.13"
  - "C.16"
  - "C.27"
  - "C.30"
  - "C.30.ASV"
  - "C.30.TFS-REL"
  - "E.24.UK"
keywords:
---

### B.2.2:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Named aggregate as system | "The platform" or "the fleet" is treated as a system because it has a name. | Identify one exact candidate and apply the complete A.1 and direct `U.System` criteria; return to the old whole if either fails. |
| Component certificate transfer | Individual part certificates are used as result-system assurance. | Re-base assurance through B.2.2:4.5 and evidence owners. |
| Controller as containing whole | A controller or external system is treated as the new whole because it changes the parts. | Use A.12, A.3.4, B.2.5, and part-whole owners separately. |
| Dashboard as system | A monitoring model is treated as the operating system. | Use episteme, publication, source-use, C.30.AD, or digital-twin description owners. |
| Capability jump as system MHT | A metric improves and the result is called a new system. | Use B.2's `ExistingWholeExplanationCheck`; return to capability, characteristic, method, work, or architecture owners if the existing whole remains sufficient. |

