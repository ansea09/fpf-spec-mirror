---
chunk_kind: "child"
pattern_id: "C.25"
pattern_title: "Q-Bundle: Express a Quality Claim as One Characteristic or a Structured Bundle"
section_id: "C.25:20a"
section_title: "Viability-envelope, quantum-like, and temporal-claim relation note"
source_path: "FPF-Spec.md"
output_path: "by_section/C.25/C.25__022_viability-envelope-quantum-like-and-temporal-claim-relation-note.md"
commit_sha: "4e277189a17b8f9bd3dcdda5df58623d9085ede9"
heading_path:
  - "C.25 — Q-Bundle: Express a Quality Claim as One Characteristic or a Structured Bundle"
  - "C.25:20a — Viability-envelope, quantum-like, and temporal-claim relation note"
line_start: 65353
line_end: 65378
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

Use `C.25` for the quality-family decomposition needed by a quality claim, proxy metric, trade-off, gate, or report. A viability claim should not become quantum-like merely because it involves uncertainty, feedback, several qualities, or changing operating conditions; a temporal claim should not become a Q-Bundle merely because the working phrase mentions speed, cadence, rhythm, or recovery.

Practical reading:

1. Decide whether one Characteristic answers the quality question; if it does, stop there.
2. If several differently typed contributors are load-bearing, identify the bearer and include only those measures, scopes, windows, mechanisms, statuses, or evidence anchors.
3. If one proxy or this proportional bundle answers the receiving question, stay in `C.25`.
4. Open `C.26.3` when several conditions must hold together under a disturbance and the question is whether the viable region is retained, violated or unresolved, or how a proposed change could restore it.
5. Open `C.27` only when a temporal claim is being used to change action—for example, when rate-change, effort, window, resistance, recovery, or cadence changes that action.

For an envelope question, use `C.26.3:4.5` to recover the exact bearer and protected work or result, derive the relevant conditions from ways that work can fail, and obtain bounds from the receiving requirements and actual provision. Keep each bound's subject explicit. Compare the available observations with those bounds under the disturbance. A supported diagnosis can finish the use: a known violation establishes failure of the conjunction even while another condition is unknown; a positive viability claim needs all required conditions supported.

For proposed regulation, identify the intervention and which constraint each predicted effect concerns. Retain the grounds, unknown effects, displaced work, trade-offs and adaptation costs needed to judge that proposal. Recover needed authority or execution conditions for the proposed action. Unknown acceptability limits remain a requirement question or an explicit scenario assumption; observed averages do not supply normative bounds. These conditions are part of the claim and its use, not a compulsory envelope form.

Useful outputs:

- one `C.2.1` quality-claim episteme with Q-Bundle-shaped content when the issue is quality decomposition;
- a `C.26.3` supported envelope diagnosis or conditional regulation proposal, with the grounds required by that result;
- a `C.27` temporal-claim adequacy card when a claim used to change action says that an intervention changes a rate, recovery, or cadence; state its effort, window, and resistance where load-bearing;

#### C.25:20b - Architecture-decision Q-Bundle boundary

`C.32.P2S`, `C.32.PAD`, and `C.32.ADA` may cite exact C.25 quality-claim epistemes or ClaimAddresses as architecture-characteristic inputs, accepted-loss structure, guardrail rows, feedback concerns, or adequacy concerns. C.25 keeps their Q-Bundle claim content, bearer, scope, measures, mechanisms, qualification window, and evidence distinct from the problem-to-structure architecturing flow, project architecture decision relation, and ADR-like publication projection.

