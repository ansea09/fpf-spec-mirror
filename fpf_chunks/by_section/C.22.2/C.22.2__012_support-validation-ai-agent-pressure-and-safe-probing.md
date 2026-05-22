---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard@Context"
section_id: "C.22.2:11"
section_title: "Support, Validation, AI-Agent Pressure, and Safe Probing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__012_support-validation-ai-agent-pressure-and-safe-probing.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "C.22.2 — ProblemCard@Context"
  - "C.22.2:11 — Support, Validation, AI-Agent Pressure, and Safe Probing"
line_start: 42142
line_end: 42183
dependencies:
  - "A.10"
  - "A.15"
  - "A.19"
  - "A.21"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.P"
  - "A.6.Q"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22"
  - "C.22.1"
  - "C.24"
  - "C.25"
  - "C.27"
  - "C.28"
  - "C.29"
  - "E.10"
  - "E.10.SEMIO"
  - "E.16"
  - "E.17"
  - "E.17.ID.CR"
  - "E.18"
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

### C.22.2:11 - Support, Validation, AI-Agent Pressure, and Safe Probing

`ProblemCard@Context` exposes support posture and validation boundary; it does not certify evidence, assurance, gate passage, safety, or autonomy control.

Plain definition: support posture names the current reason this problem formulation is worth keeping, reviewing, discriminating, or moving onward now. Typical bases include an observed signal, stakeholder cost or risk, repeated rework, violated constraint, stale or changed environment, selected-set retention basis, cheap probe value, first-principles structure that changes formulation, or stale but still useful archive or refresh cue. It is not evidence sufficiency, proof, confidence, provenance, assurance, gate passage, safety-case acceptance, release permission, autonomy permission, or work authority.

Plain definition: validation boundary states what has and has not been checked for the current next move, what the current problem formulation may be used for now, what it cannot yet support, and where any validation, evidence, assurance, gate, autonomy, or work claim beyond this local boundary is assigned. It is not an assurance claim, safety-case acceptance, release permission, or work authorization.

Plain definition: risk posture names the monitored risk, risk condition, cost-of-error concern, or containment concern that may change the safe next move. It is not the validation boundary, not the support reason, not evidence of danger by itself, and not permission to probe, delegate, or act.

Local-label boundary: `support posture`, `validation boundary`, and `risk posture` are local problem-card field labels unless a separate accepted FPF decision assigns a different governing kind. When mathematical-lens support is live, cite `C.29` and do not read local support posture as `LensSupportPosture`. When assurance, evidence, or provenance support is live, exit to `B.3`, `A.10`, or `G.6` as applicable.

Detector, check, and optimization-target discriminator:

- symptom detector: what revealed the possible problem; not an acceptance criterion.
- improvement check: what would show that the problem formulation became better.
- acceptance probe: what downstream acceptance may need to inspect; not local acceptance authority.
- optimization target: what a later selector may improve under comparison-governance or selection-governance patterns; not a local method choice.
- monitored risk signal: what may worsen, distort value, or change the safe next move; not proof by itself.
- acceptance authority: carried by `G.4` or another receiving acceptance pattern, not by `C.22.2`.










A cause-theory cue may focus problem formulation inside `ProblemCard@Context`. If that cue is used to claim association, intervention, counterfactual, responsibility, expected effect, or causal evidence, the relation exits to `C.28` plus `A.10`, `G.6`, or `B.3` when support, provenance, or assurance is live.

The AI-agent and autonomy material from the source material is received as neighboring pressure:

- autonomy budget and delegated-agent control exit to `E.16`;
- gate decisions and gate logs exit to `A.21`;
- method selection and work execution exit to `G.5` and `A.15`;
- evidence, provenance, and assurance exit to `A.10`, `G.6`, and `B.3`;
- freshness, monitoring, decay, and update triggers exit to `G.11`.

Environment design and safe probing may appear as source signal basis, validation boundary, risk posture, or neighboring-pattern exit. When the next move requires probe planning, autonomy control, gate authority, evidence, assurance, or work authority, an honest card may record `safe-probe-needed` and name `C.24`, `E.16`, `A.21`, or another live receiving pattern; this records a probe need and receiving-pattern relation, not local probe authorization. `C.22.2` does not create a separate problem-environment pattern. If the next move may affect the world, spend resources, call tools, delegate to agents, change an operational state, or require agentic tool-call scouting, tool-call plan selection, checkpoint return, or bounded call plan, `ProblemCard@Context` may only name the probe need. The authority to probe or act exits to `C.24`, `E.16`, `A.21`, `A.15`, `A.10`, `G.6`, or `B.3` when those relations are live.

