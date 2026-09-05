---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "Gate Decisions from Independent Check Results"
section_id: "A.21:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__004_problem.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "A.21 — Gate Decisions from Independent Check Results"
  - "A.21:2 — Problem"
line_start: 35174
line_end: 35184
dependencies:
  - "A.10"
  - "A.15.5"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.20"
  - "B.3"
  - "C.3.2"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.19"
  - "F.6"
  - "F.9"
  - "G.11"
  - "G.6"
keywords:
---

### A.21:2 - Problem

How can one gate decision remain reproducible without:

- losing the identity and result of each check application;
- treating not applicable, not run, unknown, and policy consequence as one value;
- allowing a missing required result to vanish beside a passing result;
- inferring policy selection or weakening from a `PathSlice` boundary;
- requiring semantic-Bridge, publication, replay, crossing, or LaunchGate apparatus for an ordinary local decision; or
- turning a prospective work-entry question into a future Work individual?

