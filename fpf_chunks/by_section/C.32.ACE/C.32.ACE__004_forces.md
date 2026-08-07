---
chunk_kind: "child"
pattern_id: "C.32.ACE"
pattern_title: "Architecture Characteristic Eval Programs"
section_id: "C.32.ACE:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACE/C.32.ACE__004_forces.md"
commit_sha: "1602a8d0a6934a99a79ead914610b070cedd86d2"
heading_path:
  - "C.32.ACE — Architecture Characteristic Eval Programs"
  - "C.32.ACE:3 — Forces"
line_start: 65517
line_end: 65527
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.19"
  - "A.19.CPM"
  - "A.2.6"
  - "A.3.1"
  - "A.3.2"
  - "A.6.1"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.25"
  - "C.32"
  - "C.32.ACS"
  - "C.32.HCS"
  - "C.32.MLAO"
  - "C.32.PAD"
  - "E.13"
  - "E.22"
  - "E.23"
  - "G.5"
keywords:
  - "architecture-characteristic eval program"
  - "comparison input"
  - "eval result"
  - "measurement boundary"
  - "missing-data policy"
  - "parity frame"
  - "proxy risk"
---

### C.32.ACE:3 - Forces

| Force | Tension |
|---|---|
| Variant learning | Candidate architectures may be valuable even when they lose the selection being made. |
| Fair comparison | Eval results are useful only when context, budgets, windows, units, and missing-data treatment are explicit. |
| Trade-off pressure | Improving one architecture characteristic can worsen another. |
| Automation value | Frequent automated evals reveal drift early, but their results can be overread. |
| Error prevention | Some eval operations are tests, yet error checking must not replace variant comparison. |
| Evolution | A useful eval can expire when the source-currentness relation, environment, declared holon-level ref, or scale window changes. |

