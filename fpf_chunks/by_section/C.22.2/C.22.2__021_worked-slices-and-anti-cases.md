---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard@Context"
section_id: "C.22.2:20"
section_title: "Worked Slices and Anti-Cases"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__021_worked-slices-and-anti-cases.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "C.22.2 — ProblemCard@Context"
  - "C.22.2:20 — Worked Slices and Anti-Cases"
line_start: 44412
line_end: 44462
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

### C.22.2:20 - Worked Slices and Anti-Cases

These worked slices and anti-cases provide local use-quality validation checks. They are not a benchmark suite, scorecard, or completeness test; they test entry findability, wrong-pattern boundary, and admissible stop for a `C.22.2` result.

#### C.22.2:20.1 - Five-Case Worked Slices

Five messy source signals serve as worked slices for use-quality validation, not as a benchmark suite: AI and human task rework, musical mastery tempo drift, problem set or Goldilocks selection, customer-service escalation after a policy or interface change, and literature-synthesis anomaly before method selection.

Thin card slices:

| Micro-slice | Problem signal | Context and scope cut | Not-wish or not-preselected-work reason | Improvement check or acceptance probe |
|---|---|---|---|---|
| AI and human task transfer rework | Repeated AI-agent task rework after transfer between human and agent. | Development or review setting where transfer produces avoidable rework; outside scope is selecting the agentic call plan, tool policy, or performed work. | The signal is not "ask the agent again" or "implement X"; the problem may be unclear task framing, missing candidate acceptance criterion, unsafe delegation, or stale context. | The next task transfer is better only if the problem signal, context, acceptance probe, and safe-call or work-authority exit are recoverable. |
| Musical mastery tempo drift | Practice tempo drifts away from the intended mastery band. | Skill-development setting where tempo, recovery, rhythm, or learning rate changes the next move; outside scope is certifying a training method. | The signal is not "play faster" as a wish; the problem may be an untyped temporal claim, unsuitable acceptance probe, or missing recovery boundary. | The formulation improves only if the temporal claim, practice context, acceptance probe, and `C.27` exit are named when live. |
| Problem set or Goldilocks selection | A candidate problem is selected from an archive, pool, front, shortlist, selected set, or portfolio because it appears to fit a Goldilocks interpretation. | Problem-selection setting with retained candidates and possible stepping stones; outside scope is redefining QD or OEE semantics or selected-set semantics. | The signal is not a priority score or task queue item; the problem remains tied to `setContextRef`, source-set form, and selection or retention criterion. | The card is usable only if `setContextRef`, characteristic or Q-bundle relation, partial-order or set-return cue, and non-scalar next move are recoverable. |
| Customer-service escalation after a policy or interface change | Service escalation volume rises after the change. | Product or operations setting where a changed promise, interface path, policy, or service script may have changed user behavior; outside scope is choosing the fix, staffing plan, or release decision. | The signal is not "reduce escalations" as a wish; the problem may be unclear interface promise, changed user path, stale service documentation, wrong acceptance probe, or a causal-use claim that needs another pattern. | The next revision is better only if the cause cue, acceptance probe, risk boundary, measurement or characterization exit, and evidence or causal-use exit are recoverable when live. |
| Literature-synthesis anomaly before method selection | A repeated anomaly in a literature synthesis does not fit the current category labels. | Named research or review context; outside scope is accepting a new theory, choosing a research method, or settling evidence sufficiency. | The signal is not "explain the anomaly" as a ready task, proof, or theory change; the problem may be an unstable EntityOfConcern, rival frame, evidence need, or bridge or representation boundary. | The formulation improves only if `rivalProblemFormulationRef`, EntityOfConcern, evidence need, and bridge, representation, or mathematical-structure exits are recoverable when live. |

Next move and tempting wrong-pattern check:

| Micro-slice | Honest next move | Tempting wrong pattern |
|---|---|---|
| AI and human task transfer rework | Stabilize the problem-side record; if agentic call planning or world-affecting action is live, exit to `C.24`, `E.16`, `A.21`, `A.15`, `A.10`, `G.6`, or `B.3` before action. | Treat repeated rework as a work item, a prompt retry instruction, or permission to delegate again. |
| Musical mastery tempo drift | Name the temporal claim and exit to `C.27` when tempo, rhythm, recovery, lead time, or learning rate changes the next move. | Treat drift or a trend line as an intervention model, method success, or evidence of mastery. |
| Problem set or Goldilocks selection | Preserve `setContextRef`; send set, parity, refresh, or set-return questions to `C.18`, `C.19`, `G.5`, `G.9`, `G.11`, `A.6.P:7a`, or `C.16.Q` when live. | Treat Goldilocks as one readiness score, priority rank, or local selected-set authority. |
| Customer-service escalation after a policy or interface change | Stabilize the problem-side record; characterize the signal through `C.16` and `A.19`, and exit to `C.28` if the card claims causal use. | Treat escalation volume as an automatic fix request, staffing plan, release rollback, or evidence that the policy was wrong. |
| Literature-synthesis anomaly before method selection | Preserve `rivalProblemFormulationRef` when rival frames remain live; exit to `A.10`, `B.3`, `F.9`, `E.18`, or `C.29` when evidence, assurance, bridge, representation, or mathematical structure is live. | Treat the anomaly as proof for a new theory, an accepted research task, or a selected method. |

P2W-ready disposition check:

| Micro-slice | P2W-ready disposition | Why |
|---|---|---|
| AI and human task transfer rework | Not P2W-ready until the acceptance probe and any agentic, work, safety, evidence, provenance, assurance, or gate exit are named. | The signal may still be a prompt retry, work-authority question, or unsafe delegation cue rather than a reviewable problem for downstream task typing. |
| Musical mastery tempo drift | Not P2W-ready while the temporal claim is untyped; exit to `C.27` when the tempo, rhythm, recovery, or learning-rate claim changes action. | A drift observation does not by itself state effort, window, resistance, relation, or reopen discipline. |
| Problem set or Goldilocks selection | Conditionally P2W-ready only when `setContextRef`, selection or retention criterion, characteristic or Q-bundle relation, and non-scalar next move are present. | Without those fields, the case collapses into priority ranking, selected-set authority, or local QD or OEE vocabulary. |
| Customer-service escalation after a policy or interface change | Not P2W-ready until scope, affected user path, acceptance probe, risk boundary, and measurement or causal-use exits are explicit. | Escalation volume alone may reflect documentation, interface promise, staffing, policy, causal evidence, or measurement changes rather than one ready downstream task. |
| Literature-synthesis anomaly before method selection | Not P2W-ready until EntityOfConcern, rival formulations, evidence need, and bridge, representation, or mathematical-structure exits are explicit when live. | An anomaly in synthesis may still be a cue, an abductive prompt, a bridge problem, or a representation problem rather than one ready downstream task. |

Additional validation cases:

| Validation case | What it checks | Expected result |
|---|---|---|
| Wish-to-problem | A wish-like input such as "I want to improve X" is not yet a reviewable problem for P2W. | The card requires a problem signal, improvement check or acceptance probe, and mandatory constraints before P2W readiness can be claimed. |
| Preselected work item | An input such as "implement X" may be a solution-shaped task rather than a problem. | The card blocks P2W readiness until a problem-side signal, context, scope, and candidate acceptance criterion are stated. |
| Set-derived problem | A problem comes from an archive, pool, front, shortlist, selected set, or portfolio. | The card preserves `setContextRef` and the selection or retention criterion, cites the receiving set pattern when live, and does not create a local portfolio or archive kind. |
| Agentic safe probe | An agentic next move may affect the world, spend resources, call tools, delegate to agents, or change operational state while authority is unclear. | The card names the risk or probe cue and exits to `C.24`, `E.16`, `A.21`, `A.15`, or the needed evidence, provenance, or assurance pattern; it does not authorize the probe locally. |
| Useful first-principles or mathematical cue | A first-principles or mathematical structure cue changes the problem formulation instead of merely decorating the card. | The card records the formulation payoff, preserved and lost structure when live, problem-formulation next-move reason, stop condition, and `C.29` exit. |
| Citation misuse | A later practitioner cites the card as proof, gate passage, safety acceptance, work authorization, or autonomy permission. | The citation is admissible only as cue, reference, or exit; gate passage needs `A.21`, evidence, provenance, or assurance needs `A.10`, `G.6`, or `B.3`, autonomy needs `E.16`, and work authority needs `A.15`. |
| Backlog-intake overread | Every ticket, idea, service request, or backlog item is forced through a full `ProblemCard@Context` before ordinary local work can continue. | Use `C.22.2` only when the signal must become reviewable before P2W, task typing, method-family selection, evidence use, gate passage, autonomy control, set-return handling, or first-principles or mathematical-lens use; the Thin form is sufficient when it gives the honest next move. |
| Already-solved or stale | The signal is stale, duplicate, already solved, already absorbed, unnecessary, or not currently worth downstream work. | A successful result may be refresh, retire, archive, `abstain/no-change`, bounded use under authority, or another named neighboring exit; the card must not silently remain `P2W-ready`. |

