---
chunk_kind: "child"
pattern_id: "A.15.7"
pattern_title: "Situation-Responsive Work Steering and Next-Action Selection"
section_id: "A.15.7:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.7/A.15.7__002_problem-frame.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "A.15.7 — Situation-Responsive Work Steering and Next-Action Selection"
  - "A.15.7:1 — Problem frame"
line_start: 27014
line_end: 27048
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

**First useful result.** Give a short answer with three visible parts:

1. **Decision now:** take this next action because this current fact and the Method's limits make it the best supported choice.
2. **Performer:** name the System that will perform it. If another System made the choice, name the chooser separately.
3. **Stop and feedback:** say when to stop, fall back, or look again, and which resulting observation can inform the next choice.

For a reversible local choice, ordinary project language is enough. Create a durable claim-bearing episteme only when another use needs to cite, compare, audit, or rely on the answer. The answer does not itself perform or predict the action, and this pattern adds no universal action, situation, or next-step kind.

**Three recognition cases.**

- A DJ is already performing. The current track is ending, the room response has changed, a promised genre constraint still applies, and several known tracks remain possible. The question is what to play next, who will make the transition, and what cue would make the DJ abandon it.
- A case worker is handling an open case. New evidence may make the displayed case state stale, while policy and authority still bound the allowed response. The question is whether to refresh, take the safe fallback, compare several live actions, or stop.
- A robotic maintenance system receives a recommendation during inspection. A sensor state has changed since the recommendation was produced. The question is whether the recommendation remains usable, needs refresh, or must give way to a safe response.

**What goes wrong if missed.** A plan, policy, score, case file, recommender, dashboard, trace, or pattern body is treated as the chooser. Every cue is forced into a heavy decision record, or every adjustment is called improvisation. The team may also invent an option set after the real issue has become stale information, missing authority, missing capability, or no current Work at all.

**What this buys.** The user gets one practical next action without losing the domain Method, current Work, deciding System, performer, authority, and stop or feedback condition. Familiar recognition, quick adaptation, explicit comparison, candidate generation, and tool-call planning remain different branches rather than one universal procedure.

**Not this pattern when.** Use the nearest applicable pattern instead:

- Before Work exists, use `A.15.2` for intended-work content and `A.15.5` for work-entry readiness.
- When ongoing Work is blocked because an exact performer, support, or continuation-state relation is missing or unsupported—not because known candidates need choosing—use the actual-Work branch of `A.15.8` to repair that configuration or stop, then return here.
- For a settled short procedure with no material branch, use the applicable domain Method; consult its `A.3.2` MethodDescription when a description is needed.
- For a choice outside current Work when the chooser and `OptionSet` are already known, use `C.11`.
- For missing action candidates, use a subject-specific generation Method; use `C.18` only for an actual open-ended candidate archive and front.
- After the action is fixed, use `C.24` only if calls to tools or services must be planned.
- For a plan revision before Work, use `A.15.2`.
- For retrospective Method recovery, use `A.3.1.MR`.

**When a DPF reuses this pattern.** A DPF uses it only for a live next-action question that passes this entry. Reuse supplies the general steering Method; the DPF still names any domain-specific problem, facts, authority, vocabulary, result, and return that change what its practitioner does. If no such use-changing contribution remains, cite this pattern rather than copying it.

