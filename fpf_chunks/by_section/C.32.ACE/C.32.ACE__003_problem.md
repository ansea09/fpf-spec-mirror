---
chunk_kind: "child"
pattern_id: "C.32.ACE"
pattern_title: "Architecture Characteristic Eval Programs"
section_id: "C.32.ACE:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACE/C.32.ACE__003_problem.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "C.32.ACE — Architecture Characteristic Eval Programs"
  - "C.32.ACE:2 — Problem"
line_start: 64743
line_end: 64750
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

### C.32.ACE:2 - Problem

Architecture synthesis is an optimization and learning activity under competing characteristics. It needs evals: deliberate measurement, simulation, benchmark, scenario, review, or monitoring runs that say how a current architecture or candidate architecture reads against declared criteria.

Testing for errors is a neighboring use. A test asks whether an expectation is violated. An eval asks how variants compare, how a candidate changes the trade-off front, which constraint is hit, or whether the next synthesis pass should open. A candidate that loses the eval is not automatically an error; it may be a deliberate probe that improves the architecture team's knowledge of the solution space.

Evolutionary-architecture sources often say "fitness function". In FPF that is source-side wording. The recoverable FPF object is an eval program over declared architecture-characteristic rows, Q-Bundle slots, candidate structures, and a parity frame. Some eval programs can be automated tests or monitors, but automation does not change the kind.

