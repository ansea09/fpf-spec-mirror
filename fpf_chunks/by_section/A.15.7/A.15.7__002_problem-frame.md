---
chunk_kind: "child"
pattern_id: "A.15.7"
pattern_title: "Situation-Responsive Work Steering and Next-Action Selection"
section_id: "A.15.7:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.7/A.15.7__002_problem-frame.md"
commit_sha: "b223469ecafb9735c1d9bac220671e3336618339"
heading_path:
  - "A.15.7 — Situation-Responsive Work Steering and Next-Action Selection"
  - "A.15.7:1 — Problem frame"
line_start: 31520
line_end: 31555
dependencies:
  - "A.10"
  - "A.13"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.15.6"
  - "A.19"
  - "A.3.1"
  - "B.1.5"
  - "C.11"
  - "C.18"
  - "C.24"
  - "F.6"
  - "G.11"
keywords:
---

### A.15.7:1 - Problem frame

**Use this when.** Use this pattern when you are in the middle of Work, current facts can change what should happen next, and a domain Method still sets what is allowed.

**First useful result.** Give a supported next-action answer in ordinary language, with the content needed for its use:

1. **Decision now:** state the selected continuation and its grounds, or the limitation that requires a stop or return to another question.
2. **Performer:** identify the intended System performer when an action is selected. Name the chooser separately when it differs.
3. **Stop and feedback:** retain the stop, fallback, reconsideration or observation condition that the selected continuation or receiving use needs.

For a reversible local choice, ordinary project language is enough. When a use needs to cite, compare, audit, or rely on an identified claim, use an existing sufficient episteme or identify one under C.2.1. Preserve access when later reliance requires it. The answer states the supported result and its grounds.

**Three recognition cases.**

- A DJ is already performing. The current track is ending, the room response has changed, a promised genre constraint still applies, and several known tracks remain possible. The question is what to play next, who will make the transition, and what cue would make the DJ abandon it.
- A case worker is handling an open case. New evidence may make the displayed case state stale, while policy and authority still bound the allowed response. The question is whether to refresh, take the safe fallback, compare several live actions, or stop.
- A robotic maintenance system receives a recommendation during inspection. A sensor state has changed since the recommendation was produced. The question is whether the recommendation remains usable, needs refresh, or must give way to a safe response.

**What goes wrong if missed.** A plan, policy, score, case file, recommender output, dashboard, trace, or pattern body is treated as the chooser. Every cue is forced into a heavy decision record, or every adjustment is called improvisation. The team may also invent an option set after the real issue has become stale information, missing authority, missing capability, or no current Work at all.

**What this buys.** The user gets a supported continuation or a named blocker, with the domain Method, current Work, deciding System, intended performer when one is needed, and applicable authority, stop and feedback conditions clear. Familiar recognition, quick adaptation, explicit comparison, candidate generation, and tool-call planning remain different branches rather than one universal procedure.

**Not this pattern when.** Use the nearest applicable pattern instead:

- Before Work exists, use `A.15.2` for intended-work content and `A.15.5` for work-entry readiness.
- After an interruption, use `A.15.10` when the purpose, governing method or unfinished contribution must be recovered before a useful next action can be selected. If these are already available, continue here.
- When ongoing Work is blocked because an exact performer, support, or continuation-state relation is missing or unsupported—not because known candidates need choosing—use the actual-Work branch of `A.15.8` to repair that configuration or stop, then return here.
- For a settled short procedure with no material branch, use the applicable domain Method; consult its `A.3.2` MethodDescription when a description is needed.
- For a choice outside current Work when the chooser and `OptionSet` are already known, use `C.11`.
- For missing action candidates, use a subject-specific generation Method; use `C.18` only for an actual open-ended candidate archive and front.
- After the action is fixed, use `C.24` if calls to tools or services must be planned. An already prescribed action can enter C.24 directly before Work begins; it needs no A.15.7 decision.
- For intended-work content or plan revision before or during Work, use `A.15.2`; return here when current facts require a next-action choice.
- For retrospective Method recovery, use `A.3.1.MR`.

**Adapt to the domain.** Apply the steering Method to the domain facts, constraints and intended result that can change the next action. For example, a DJ tests a transition against the promised genre and live response; a maintenance practitioner tests an intervention against the equipment state and applicable safety conditions. The same steering operations can yield different actions because their domain premises differ.

