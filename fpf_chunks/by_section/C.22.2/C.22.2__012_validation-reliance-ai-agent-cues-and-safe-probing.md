---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard"
section_id: "C.22.2:11"
section_title: "Validation, Reliance, AI-Agent Cues, and Safe Probing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__012_validation-reliance-ai-agent-cues-and-safe-probing.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "C.22.2 — ProblemCard"
  - "C.22.2:11 — Validation, Reliance, AI-Agent Cues, and Safe Probing"
line_start: 63613
line_end: 63633
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.5"
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
  - "C.2.1"
  - "C.2.P"
  - "C.22"
  - "C.22.1"
  - "C.22.PFR"
  - "C.24"
  - "C.25"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.32.P2S"
  - "E.10"
  - "E.10.MOVE"
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
---

### C.22.2:11 - Validation, Reliance, AI-Agent Cues, and Safe Probing

`ProblemCard` exposes three local fields for downstream use:

- problem-formulation follow-up reason: why this formulation is worth keeping, reviewing, discriminating, or moving onward now;
- validation boundary: what has been checked for the current next use, what may be used now, and which use is governed by another pattern;
- risk condition: the monitored risk, cost-of-error concern, or containment concern that may change the safe next action.

Use these fields to state a local reliance disposition, not to authorize downstream action.

| Card-use condition | Local disposition | Next pattern application |
|---|---|---|
| The current reason is sufficient for the named reversible P2W use. | `P2W-ready` only for that named use, with effective ReferenceScheme, ClaimScope, qualification window, validation boundary, and stop condition. | Apply measurement, evidence, temporal, refresh, representation, gate, autonomy, Work, or assurance patterns only when those claims are part of the use. |
| The reason is useful but narrower than the attempted use. | Narrow the attempted use; name the narrowed use, blocked attempted use, and stop condition. | Apply the subject pattern for the missing claim, relation, or boundary. |
| Source material, source relation, validation, or currentness is stale, conflicted, uncalibrated, or untied to the current relation. | Choose `abstainOrNoChange`, `refresh`, or `reopen`; name the missing relation, evidence-needed cue when current, and decision point. | Use `A.10`, `G.6`, `B.3`, `C.16`, `C.27`, `G.11`, `A.6.3.RT`, `A.6.4`, `E.17`, `F.9`, or `E.18` according to the reopened relation. |
| The proposed next action requires a safety, release, gate, autonomy or Work basis beyond the card. | Use the independently applicable grounds or authorization; if missing, block only the dependent action and retain the usable problem-side claim. | Apply `B.3`, `A.21`, `E.16`, `A.15`, `A.10`, `G.6`, or `B.2.5` when its governed claim is current. |

Cause-theory cues may focus problem formulation inside `ProblemCard`. Association, intervention, counterfactual, responsibility, expected-effect, or causal-evidence claims are governed by `C.28` plus evidence, provenance, or assurance patterns when those claims are being made.

Environment design and safe probing may appear as problem signal reference, validation boundary, risk condition, or subject-pattern cue. For a probe affecting a controlled EntityOfConcern, identify the applicable safety or authorization condition. Existing adequate grounds may permit the action; the card itself supplies no missing permission, release authorization or gate result.

