---
chunk_kind: "child"
pattern_id: "C.25"
pattern_title: "Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
section_id: "C.25:20a"
section_title: "Viability-envelope, quantum-like, and temporal-claim relation note"
source_path: "FPF-Spec.md"
output_path: "by_section/C.25/C.25__022_viability-envelope-quantum-like-and-temporal-claim-relation-note.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "C.25 — Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
  - "C.25:20a — Viability-envelope, quantum-like, and temporal-claim relation note"
line_start: 53808
line_end: 53844
dependencies:
  - "A.10"
  - "A.15"
  - "A.16.0"
  - "A.18"
  - "A.2.6"
  - "A.6.1"
  - "B.3"
  - "C.16"
  - "C.16.P"
  - "C.16.Q"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.2.2a"
  - "C.26.3"
  - "C.33"
  - "C.34"
  - "C.35"
  - "F.9"
  - "F.9.1"
keywords:
  - "admissible quality-family use"
  - "characteristic plus scope"
  - "endpoint classification"
  - "failure mode"
  - "ility"
  - "mechanism/status slots"
  - "proxy metric"
  - "quality bundle"
  - "quality family"
  - "viability envelope"
---

### C.25:20a - Viability-envelope, quantum-like, and temporal-claim relation note

Use `C.25` when the question under repair is a quality bundle, "-ility" decomposition, proxy metric, trade-off, gate, or report. A viability claim should not become quantum-like merely because it involves uncertainty, feedback, several qualities, or changing operating conditions; a temporal claim should not become a Q-Bundle merely because the working phrase mentions speed, cadence, rhythm, or recovery.

Practical reading:

1. Decide whether one Characteristic answers the quality question; if it does, stop there.
2. If several differently typed contributors are load-bearing, identify the bearer and include only those measures, scopes, windows, mechanisms, statuses, or evidence anchors.
3. If one proxy or this proportional bundle answers the receiving question, stay in `C.25`.
4. Open `C.26.3` only when the current question concerns a viable region, disturbance, boundary condition, intervention, adaptation cost, or failure mode.
5. Open `C.27` only when rate-change under effort, window, resistance, recovery, or cadence changes the admissible use of a temporal claim.
Minimum viability-envelope note:

| Field | Required content |
| --- | --- |
| Bearer | One exact `U.System` under A.1 when that System is the subject; or one exact `A.22` `U.Structure` when selected organization is the subject, with independently identified constituents, selected obtaining relations, applied constraints, and one selection-use frame. A service label, team label, or list of system-role kinds and assignment occurrences does not identify the bearer by itself. |
| Protected promise / function | The promise, function, use, operating regime, or stakeholder value the envelope protects |
| Variables | Which qualities, constraints, resources, risks, or state descriptors define the envelope |
| Viable region / bounds | What counts as inside, near edge, degraded, or outside the envelope for this use |
| Disturbance class | What perturbation, demand shift, environment change, probe, or boundary condition stresses the envelope |
| Actuators | What work, design move, policy, boundary change, sensor change, or resource change can move the bearer |
| Trade-off / loss | What gets worse, hidden, coarsened, delayed, or made more expensive |
| Admissible use | Which action, decision, relation, or triage use the envelope reading can carry |
| Non-admissible use | Which release, audit, assurance, or universal quality claim requiring additional support it does not support |
| Failure mode | What it means to leave the envelope or to mistake one proxy for the envelope |

Useful outputs:

- one `C.2.1` quality-claim episteme with Q-Bundle-shaped content when the issue is quality decomposition;
- a `C.26.3` envelope-regulation note when probes/actuators/boundary conditions change the admissible viability reading;
- a `C.27` temporal-claim adequacy card when rate-change, effort, window, resistance, or cadence changes the admissible use;
- no QL wording when ordinary quality-bundle, proxy, feedback, or control tuning carries the work.

#### C.25:20b - Architecture-decision Q-Bundle boundary

`C.32.P2S`, `C.32.PAD`, and `C.32.ADA` may cite exact C.25 quality-claim epistemes or ClaimAddresses as architecture-characteristic inputs, accepted-loss structure, guardrail rows, feedback concerns, or adequacy concerns. C.25 keeps their Q-Bundle claim content, bearer, scope, measures, mechanisms, qualification window, and evidence distinct from the problem-to-structure architecturing flow, project architecture decision relation, and ADR-like publication projection.

