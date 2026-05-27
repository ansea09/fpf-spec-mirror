---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard@Context"
section_id: "C.22.2:11"
section_title: "Support, Validation, AI-Agent Pressure, and Safe Probing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__012_support-validation-ai-agent-pressure-and-safe-probing.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "C.22.2 — ProblemCard@Context"
  - "C.22.2:11 — Support, Validation, AI-Agent Pressure, and Safe Probing"
line_start: 43670
line_end: 43740
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

Reliance-disposition rule for P2W receiving use:

Use this rule when support posture or validation boundary may enter P2W as evidence-like, confidence-like, conformance-like, proxy-like, safety-looking, redress-bearing, or currentness-bearing support. The first C.22.2 move is to keep the result problem-side: name the P2W receiving use, unsupported use, and any live receiving-pattern exit. This rule does not add a default field family to `ProblemCard@Context`. If the Thin card already gives an honest next move and live exits, no additional reliance record is required.

Support role: the disposition table below is a local P2W-reliance recognition and minimum local record aid, and the worked P2W reliance slices are regression/review slices. They are not card field lists, project checklists, or hidden SEMIO state machines. Use them only to state the supported P2W receiving use, unsupported use, and receiving-pattern exit when support posture or validation boundary is actually being relied on. This local section returns the attempted P2W use to the C.22.2 problem-side relation and named receiving-pattern exits; it does not create an extra SEMIO authority or cross-pattern relation vocabulary.

Affordability card: orientation, discussion, or source-finding can remain an ordinary problem-side cue; bounded P2W reliance states the supported receiving use, unsupported use, window, and exit; threshold reliance names the receiving evidence, assurance, gate, autonomy, control, work, temporal, or representation relation instead of making the card larger. Plain wording remains ordinary unless it changes admissible use, support, evidence, gate, assurance, work, decision, or neighboring-pattern exit.

Common wrong first reading: `P2W-ready` means proof, safety acceptance, gate passage, method selection, work authorization, or release permission. First honest entry: keep the result problem-side; name the P2W receiving use and any exact evidence, assurance, gate, autonomy, control, work, temporal, or representation exit when live.

| Attempted P2W use | Local card move | Receiving-pattern exit when live | Forbidden overread |
| --- | --- | --- | --- |
| Support posture is enough for the next P2W receiving use | State `RelianceDisposition=pass` only for the named P2W receiving use, unsupported attempted P2W use, support posture, validation boundary, context, and window. | Open `A.10`, `B.3`, `A.21`, `C.16`, `C.27`, `G.11`, `A.6.3.RT`, or `A.6.4` only when that relation carries part of the support. | Treating `P2W-ready` as proof, safety acceptance, gate passage, method selection, work authorization, portfolio authority, or release permission. |
| Support is useful but narrower than the attempted P2W use | State `RelianceDisposition=degrade`, the narrowed P2W use, the unsupported attempted use, and the stop condition. | Open measurement, evidence, temporal, refresh, representation, or assurance loci only for the live dependency. | Quietly broadening a weak support posture into full P2W readiness. |
| Source, confidence, or validation is stale, conflicted, uncalibrated, or not tied to the live relation | State `RelianceDisposition=abstain` or `RelianceDisposition=evidence-needed`, plus the missing evidence kind or receiving relation and the decision point. | `A.10` for evidence/currentness, `C.16` for measurement or marker support, `C.27`/`G.11` for time, expiry, refresh, or monitoring. | Letting uncertainty become indefinite delay or silent permission to continue. |
| Contest, redress request, changed representation, retargeting, or changed described entity defeats support inheritance | State `RelianceDisposition=reopen`, the relation being reopened, and the card use that is no longer supported. | `A.6.3.RT`, `A.6.4`, `E.17`, `F.9`, `E.18`, `A.10`, `B.3`, or another exact relation when the represented problem, evidence path, or support source changed. | Treating an older card as still current merely because its text was preserved. |
| Safety-looking, release-looking, compliance-looking, public-behavior, resource, people/status, autonomy, gate, or control-bearing use is attempted from the card | State `RelianceDisposition=safety-case-required`, `RelianceDisposition=no-supported-current-use`, or a named exit; do not authorize the use locally. | `B.3` for assurance and the minimum reliance safety support record, `A.21` for gate decision, `E.16` for autonomy, `A.15` for work, `B.2.5` only when a controlled object is regulated through a feedback channel, evidence channel, cadence, window, or supervisory/control relation, `A.10`/`G.6` for evidence/provenance. | Reading a problem-side card as safety acceptance, tool-call permission, delegated-agent authority, release permission, work plan, performed work, or control authority. |

Minimum P2W support statement when this rule is live: support posture, validation boundary, `RelianceDisposition`, supported P2W receiving use, unsupported use, currentness or window when relevant, contest or redress path when relevant, and live receiving-pattern exits. Do not copy evidence, gate, assurance, work, autonomy, or control fields into the card unless the card is explicitly naming a live exit to the receiving pattern.

Misuse guard: `RelianceDisposition=abstain` and `RelianceDisposition=degrade` must state the condition for reopening, narrowing, or closing the P2W use; do not use uncertainty to block valid P2W receiving use indefinitely or to hide a full pass behind a narrower label.

False-negative reliance guard: a blocked, abstained, or evidence-needed P2W use is not final if admissible challenge evidence, missing affected-party evidence, changed source, changed representation, or redress can materially change the disposition.

Support-inheritance guard: support does not inherit across representation scheme, episteme-lane view, publication face, described entity, retargeting relation, or source-basis change merely because the same card text, dashboard label, source phrase, support cue, generated explanation, coarsened or redacted rendering, screenshot, or copied approval survived. Use A.6.3.RT, A.6.3.CSC, A.6.4, E.17, F.9, or E.18 only when that relation is live; otherwise keep the local card use bounded.

Positive repaired path: a messy support cue becomes useful when the card states what P2W may receive now, what P2W must not infer, and which exact neighboring pattern carries any evidence, assurance, gate, temporal, representation, autonomy, control, or work relation. A successful result can be `P2W-ready`, degraded P2W use, evidence-needed, refresh, reopen, `abstain/no-change`, or a named neighboring exit; it need not become a bigger card.

Worked P2W reliance slices:

| Slice | Local card move | Boundary |
| --- | --- | --- |
| An archive or portfolio retention cue supports looking at a problem again. | State the support posture, validation boundary, source-set or retention basis, currentness/window, and `RelianceDisposition=degrade`, `RelianceDisposition=evidence-needed`, or `refresh` when the cue is stale or incomplete. | Retention is not proof, safety acceptance, method selection, or work authorization. |
| Confidence-looking support is enough for one reversible exploration step. | State `RelianceDisposition=pass` only for that P2W receiving use, unsupported attempted use, context, window, and stop condition. | The same card does not become full readiness, release permission, or assurance. |
| A problem card is cited as safety acceptance or tool-call permission. | State `RelianceDisposition=safety-case-required`, `RelianceDisposition=no-supported-current-use`, or a named exit to `B.3`, `E.16`, `A.21`, `A.15`, or `A.10`. | `ProblemCard@Context` does not authorize action, autonomy, gate passage, work, or release. |
| A contest, redress request, or changed described entity defeats inherited support. | State `RelianceDisposition=reopen`, the relation being reopened, and which previous P2W use is no longer supported. | Preserved card text does not preserve currentness when representation or evidence changed. |
| A selected-set or portfolio basis is used before P2W. | Keep the set-source, selection, retention, and not-selected disposition as source cues and name the receiving set patterns when live. | The card is not portfolio authority, selected-set proof, or scalar readiness. |

A cause-theory cue may focus problem formulation inside `ProblemCard@Context`. If that cue is used to claim association, intervention, counterfactual, responsibility, expected effect, or causal evidence, the relation exits to `C.28` plus `A.10`, `G.6`, or `B.3` when support, provenance, or assurance is live.

The AI-agent and autonomy material from the source material is received as neighboring pressure:

- autonomy budget and delegated-agent control exit to `E.16`;
- gate decisions and gate logs exit to `A.21`;
- method selection and work execution exit to `G.5` and `A.15`;
- evidence, provenance, and assurance exit to `A.10`, `G.6`, and `B.3`;
- freshness, monitoring, decay, and update triggers exit to `G.11`.

Environment design and safe probing may appear as source signal basis, validation boundary, risk posture, or neighboring-pattern exit. When the next move requires probe planning, autonomy control, gate authority, evidence, assurance, or work authority, an honest card may record `safe-probe-needed` and name `C.24`, `E.16`, `A.21`, or another live receiving pattern; this records a probe need and receiving-pattern relation, not local probe authorization. `C.22.2` does not create a separate problem-environment pattern. If the next move may affect the world, spend resources, call tools, delegate to agents, change an operational state, or require agentic tool-call scouting, tool-call plan selection, checkpoint return, or bounded call plan, `ProblemCard@Context` may only name the probe need. The authority to probe or act exits to `C.24`, `E.16`, `A.21`, `A.15`, `A.10`, `G.6`, or `B.3` when those relations are live.

