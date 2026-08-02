---
chunk_kind: "child"
pattern_id: "C.32.ACE"
pattern_title: "Architecture Characteristic Eval Programs"
section_id: "C.32.ACE:5"
section_title: "Worked slices"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACE/C.32.ACE__006_worked-slices.md"
commit_sha: "9a9a42e4d154021ca3f7415e0009a4214832f65f"
heading_path:
  - "C.32.ACE — Architecture Characteristic Eval Programs"
  - "C.32.ACE:5 — Worked slices"
line_start: 65286
line_end: 65297
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

### C.32.ACE:5 - Worked slices

**Latency candidate.** A service candidate promises latency under 100 ms and an eval reads 240 ms. If the 100 ms band is a hard constraint, the candidate is inadmissible for this cycle. If the project is still exploring a trade-off front, the candidate is a losing variant with useful evidence about resource placement, interface burden, or control separation. Treat it as an error only when the project used that expectation to plan work and unplanned rework follows.

**BIM digital twin.** A built-asset team compares architecture candidates that combine placement, schedule, use-phase, maintenance, and cost structures. ACE does not treat the number of dimensions as the evaluation. The practitioner defines a parity frame and evals the ACS rows declared for the project, such as access, source-return cost, observability, and maintenance reach, then records results with the parity-frame and result-form fields needed by `A.19.CPM`.

**Method-family architecture.** A review-method family has ACS rows for evidence reuse, change reach, and role substitutability, plus a C.25 teachability bundle. ACE defines a batch eval over three method variants. One variant loses on teachability but reveals a reusable evidence relation; C.32 may use it as a stepping stone.

**AI-agent workflow.** A model-supported workflow has candidates with different function graphs and tool boundaries. ACE evaluates latency, evidence refresh, policy controllability, and rollback under the same task set and evidence window. A benchmark score is not the architecture decision; it supplies one eval reading inside the parity frame.

**Role-team escalation.** A hospital escalation team has ACS rows for decision latency, accountability clarity, evidence custody, and role continuity. ACE evaluates two role-boundary variants under the same incident scenarios and handoff evidence window. The result can feed comparison or the next synthesis pass; staffing choice remains with the receiving decision pattern.

