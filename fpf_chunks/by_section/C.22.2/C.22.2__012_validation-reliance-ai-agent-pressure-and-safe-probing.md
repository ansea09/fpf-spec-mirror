---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard@Context"
section_id: "C.22.2:11"
section_title: "Validation, Reliance, AI-Agent Pressure, and Safe Probing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__012_validation-reliance-ai-agent-pressure-and-safe-probing.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "C.22.2 — ProblemCard@Context"
  - "C.22.2:11 — Validation, Reliance, AI-Agent Pressure, and Safe Probing"
line_start: 44697
line_end: 44717
dependencies:
  - "A.10"
  - "A.15"
  - "A.19"
  - "A.21"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.Q"
  - "C.18"
  - "C.19"
  - "C.2.P"
  - "C.22"
  - "C.22.1"
  - "C.24"
  - "C.25"
  - "C.27"
  - "C.28"
  - "C.29"
  - "E.10"
  - "E.16"
  - "E.17"
  - "E.17.ID.CR"
  - "E.18"
  - "E.18.1"
  - "E.2"
  - "E.9"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
  - "P2W-ready"
  - "Thin problem card"
  - "first-principles cue"
  - "freshness and unknown disposition"
  - "problem card"
  - "problem signal"
  - "problem-side record"
  - "safe-probe-needed"
  - "setContextRef"
  - "support posture"
  - "validation boundary"
---

### C.22.2:11 - Validation, Reliance, AI-Agent Pressure, and Safe Probing

`ProblemCard@Context` exposes three local fields for downstream use:

- problem-formulation next-move reason: why this formulation is worth keeping, reviewing, discriminating, or moving onward now;
- validation boundary: what has been checked for the current next move, what may be used now, and which use needs another pattern;
- risk condition: the monitored risk, cost-of-error concern, or containment concern that may change the safe next move.

Use these fields to state a local reliance disposition, not to authorize downstream action.

| Card-use condition | Local disposition | Next pattern application |
|---|---|---|
| The current reason supports the named reversible P2W use. | `RelianceDisposition=pass` for that named use, with validation boundary, context, window, and stop condition. | Apply measurement, evidence, temporal, refresh, representation, gate, autonomy, work, or assurance patterns only when those claims are part of the use. |
| The reason is useful but narrower than the attempted use. | `RelianceDisposition=degrade`; name the narrowed use, non-admissible attempted use, and stop condition. | Apply the governing pattern for the missing claim, relation, or boundary. |
| Source, validation, or currentness is stale, conflicted, uncalibrated, or untied to the live relation. | `RelianceDisposition=abstain`, `evidence-needed`, `refresh`, or `reopen`; name the missing relation and decision point. | Use `A.10`, `G.6`, `B.3`, `C.16`, `C.27`, `G.11`, `A.6.3.RT`, `A.6.4`, `E.17`, `F.9`, or `E.18` according to the reopened relation. |
| The proposed next move can affect the world, spend resources, call tools, delegate to agents, change operational state, or make safety/release/gate/work claims. | `RelianceDisposition=safety-case-required`, `no-current-admissible-use`, or the relation named by value label. | Apply `B.3`, `A.21`, `E.16`, `A.15`, `A.10`, `G.6`, or `B.2.5` when the corresponding controlled-object relation is live. |

Cause-theory cues may focus problem formulation inside `ProblemCard@Context`. Association, intervention, counterfactual, responsibility, expected-effect, or causal-evidence claims are governed by `C.28` plus evidence, provenance, or assurance patterns when those claims are being made.

Environment design and safe probing may appear as source signal reference, validation boundary, risk condition, or governing-pattern cue. If the next move can affect a controlled object, the card names the probe need plus the claim kind named by value that blocks local action; it does not authorize the probe locally.

