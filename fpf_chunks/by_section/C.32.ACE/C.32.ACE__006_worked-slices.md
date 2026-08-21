---
chunk_kind: "child"
pattern_id: "C.32.ACE"
pattern_title: "Architecture Characteristic Eval Programs"
section_id: "C.32.ACE:5"
section_title: "Worked slices"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACE/C.32.ACE__006_worked-slices.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "C.32.ACE — Architecture Characteristic Eval Programs"
  - "C.32.ACE:5 — Worked slices"
line_start: 62470
line_end: 62481
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

**Method-family architecture.** A review-Method family has ACS rows for evidence reuse and change reach. If source wording also says “role substitutability,” use `E.10.ROLE` and `C.32.ACS` to bind the exact recovered subject and predicate—such as substitutability among local system-role kinds under A.2.7, not among holders or assignments—before ACE evaluates it. A separate C.25 bundle covers teachability. ACE defines a batch evaluation over three Method variants. One variant loses on teachability but reveals a reusable evidence relation; C.32 may use it as a stepping stone.

**AI-agent workflow.** A model-supported workflow has candidates with different function graphs and tool boundaries. ACE evaluates latency, evidence refresh, policy controllability, and rollback under the same task set and evidence window. A benchmark score is not the architecture decision; it supplies one eval reading inside the parity frame.

**Hospital escalation.** A hospital escalation team has ACS rows for decision latency, accountability clarity, and evidence custody. Any source “role continuity” or “role-boundary” criterion first goes through `E.10.ROLE` and `C.32.ACS`, which binds the exact subject and predicate—such as continuity of assignment occurrences and their holder Systems, or a boundary among exact participant relations. ACE evaluates two recovered architecture variants under the same incident scenarios and handoff evidence window. The result can feed comparison or the next synthesis pass; staffing choice remains with the receiving decision pattern.

