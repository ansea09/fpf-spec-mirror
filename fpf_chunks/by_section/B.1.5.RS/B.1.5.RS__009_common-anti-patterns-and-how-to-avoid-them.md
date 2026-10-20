---
chunk_kind: "child"
pattern_id: "B.1.5.RS"
pattern_title: "Evaluate a Constituent Method Replacement in Its Encompassing Uses"
section_id: "B.1.5.RS:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5.RS/B.1.5.RS__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "73e53b7b1a40aae81d6871f327e5bf7b1c495e23"
heading_path:
  - "B.1.5.RS — Evaluate a Constituent Method Replacement in Its Encompassing Uses"
  - "B.1.5.RS:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 43351
line_end: 43360
dependencies:
  - "A.3.1"
  - "B.1.5"
  - "B.1.5.EW"
  - "B.1.5.RS"
  - "C.11.DUA"
  - "C.29"
keywords:
---

### B.1.5.RS:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| One matching output stands in for preserved behavior. | Recover the timing, interaction or property actually used by the whole and test that contribution. |
| Compatibility in one whole is exported to every user. | Separate receiving uses and restrict the conclusion accordingly. |
| Every implementation detail must remain unchanged. | Preserve what the declared use relies on; permit changes outside that dependence. |
| An adapter is omitted from the candidate's cost or failure analysis. | Include the adapter in the candidate arrangement and follow the combined behavior. |
| A successful trial becomes an unconditional guarantee. | State its supported scope and establish stronger claims only when required. |

