---
chunk_kind: "child"
pattern_id: "A.15.8"
pattern_title: "Work-Performance Configuration and Recovery Testing"
section_id: "A.15.8:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.8/A.15.8__002_problem-frame.md"
commit_sha: "6226816d8005a4c8ee3af338bb3752f6732449a9"
heading_path:
  - "A.15.8 — Work-Performance Configuration and Recovery Testing"
  - "A.15.8:1 — Problem frame"
line_start: 33051
line_end: 33075
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
  - "A.2.4"
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

**Use this when.** Use this pattern to assess or design a configuration that must continue or recover a service after interruption, handoff, delay, support loss or replacement. Begin with the service due under the changes the agreement permits. For an actual interruption, establish what happened in its circumstances. Choose the branch for the focus being examined:

- **Actual-Work branch:** start from one dated `U.Work` occurrence already admitted under `A.15.1`. Name actual performers, assignments, and attribution only where the rules governing those claims pass.
- **Present-WorkPlan branch:** start from one present `U.WorkPlan` under `A.15.2`. Intended performers and intended performance remain declaration-local plan content; they are not an existing future `U.Work`, obtaining assignment, or actual attribution.

Start with a sentence appropriate to that branch:

> **Actual Work:** For this admitted Work occurrence, these Systems performed it under the attribution rules; these other Systems or values supported it; this is where the state needed to continue lives; this is what the available evidence establishes about continuation or recovery; continue within the supported conditions, repair the affected relation, or stop as that result warrants.
>
> **Present WorkPlan:** For this present WorkPlan, these Systems are named as intended performers in its declaration-local content; these other Systems or values support the proposed configuration; this is where the state needed for intended performance would be recovered; this is what the plan and applicable evidence establish about the promised service under the specified changes; obtain a needed basis, revise the plan, continue within the supported conditions, or stop as that result warrants.

**First useful result.** Return a short branch-specific account of the Work or WorkPlan focus, required result and receiving decision, performers, supports, continuation state and grounds needed by that decision, the supported, failed or unresolved relation claims, and the warranted next action or stop.

**What changes in practice.** A team can choose the support and state its service needs, identify a loss that defeats the promise or justify continued service under the allowed changes. It can then retain or repair the configuration, investigate an unresolved condition or stop the affected use.

**Cheap non-use.** Do not use this pattern merely because Work uses a tool, a person takes notes, software has state, a bacterium responds to its environment, or several Systems participate.

Stop when current results from domain Work already identify the configuration of the named Work or WorkPlan, continuation state, grounds for recovery under the required conditions, and limits needed by the decision, with the applicable Method and evidence boundary explicit.

If `A.15.5` has established an ordinary full kit and no interruption, handoff, support loss, or configuration ambiguity can change entry, stop there. If the configuration is adequate and only the next action during current Work is open, use `A.15.7`. For ordinary preparation and return after an interruption, use `A.15.10` when the purpose, method or unfinished contribution must be recovered; that use does not require a configuration test.

**Not this pattern when.** Use `A.1` to recognize a proposed System, and `B.2` when changed facts require comparison with an established prior whole; `A.2.2` for capability of one admitted holder; `A.15.1` for Work occurrence identity or resumption segmentation; `A.15.2` for the WorkPlan; `A.15.5` for ordinary entry readiness; `A.15.7` for next-action selection; `A.22` for one selected Structure; `C.30` for architecture; the pattern governing a representation; `A.2.4` for the first evidence-use or status-use classification and `A.10` when the bounded source-to-use account must remain replayable; or the applicable domain Method when only its test, threshold, algorithm, safety rule, or intervention is missing.

