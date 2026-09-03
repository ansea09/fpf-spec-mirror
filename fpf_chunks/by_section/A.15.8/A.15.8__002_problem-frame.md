---
chunk_kind: "child"
pattern_id: "A.15.8"
pattern_title: "Work-Performance Configuration and Recovery Testing"
section_id: "A.15.8:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.8/A.15.8__002_problem-frame.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "A.15.8 — Work-Performance Configuration and Recovery Testing"
  - "A.15.8:1 — Problem frame"
line_start: 27485
line_end: 27505
dependencies:
  - "A.1"
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.15.2"
  - "A.15.4"
  - "A.15.5"
  - "A.15.7"
  - "A.15.8"
  - "A.2.1"
  - "A.2.2"
  - "A.22"
  - "A.6.RCD"
  - "A.6.REL"
  - "C.11"
  - "C.2.1"
  - "C.2.P.DR"
  - "C.27.TA"
  - "C.30"
  - "E.23.CAE"
  - "E.23.CDI"
  - "F.6"
keywords:
---

### A.15.8:1 - Problem frame

**Use this when.** Use this pattern when a result succeeds in one configuration but may fail after interruption, handoff, delay, support loss, replacement, or changed conditions, and the decision needs to know which exact relation to repair or test. Begin through exactly one lawful branch:

- **Actual-Work branch:** start from one exact dated `U.Work` occurrence already admitted under `A.15.1`. Name actual performers, assignments, and attribution only where their direct rules pass.
- **Present-WorkPlan branch:** start from one exact present `U.WorkPlan` under `A.15.2`. Intended performers and intended performance remain declaration-local plan content; they are not an existing future `U.Work`, obtaining assignment, or actual attribution.

Start with an ordinary branch-exact sentence:

> **Actual Work:** For this admitted Work occurrence, these Systems performed it under the direct attribution rules; these other Systems or values supported it; this is where the state needed to continue lives; this dependency failed under this probe; repair this relation or stop.
>
> **Present WorkPlan:** For this present WorkPlan, these Systems are named only as intended performers in its declaration-local content; these other Systems or values support the proposed configuration; this is where the state needed for intended performance would be recovered; this dependency is unsupported by the current plan or probe claim; repair the plan relation or stop.

**First useful result.** Return a short branch-specific account naming the exact Work or WorkPlan focus, required result and receiving decision, actual or intended performers, supports, continuation-critical state, probe and observation, the direct relation result or exact blocker, and the next repair or stop.

**What changes in practice.** Instead of saying that a person, tool, team, organism, service, or machine must “pay attention”, “remember”, or become one “extended performer”, the practitioner names the exact relation whose loss changes continuation or recovery and challenges that relation under one representative condition. The next move becomes a bounded configuration repair, direct domain test, plan change, or stop.

**Cheap non-use.** Do not use this pattern merely because Work uses a tool, a person takes notes, software has state, a bacterium responds to its environment, or several Systems participate. Stop when current results from directly governed domain Work already identify the actual configuration, continuation state, representative recovery evidence, and limits needed by the decision, with the applicable Method and evidence boundary explicit. If `A.15.5` has established an ordinary full kit and no interruption, handoff, support loss, or configuration ambiguity can change entry, stop there. If the configuration is adequate and only the next action during current Work is open, use `A.15.7`.

**Not this pattern when.** Use `A.1` or `B.2` when the current question is whether a proposed whole is a System or must be reidentified; `A.2.2` for capability of one admitted holder; `A.15.1` for Work occurrence identity or resumption segmentation; `A.15.2` for the WorkPlan; `A.15.5` for ordinary entry readiness; `A.15.7` for next-action selection; `A.22` for one selected Structure; `C.30` for architecture; the direct representation pattern for a representation; `A.10` for evidence reliance; or the applicable domain Method when only its test, threshold, algorithm, safety rule, or intervention is missing.

