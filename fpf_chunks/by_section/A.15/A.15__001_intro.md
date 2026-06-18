---
chunk_kind: "child"
pattern_id: "A.15"
pattern_title: "Role–Method–Work Alignment (Contextual Enactment)"
section_id: "A.15:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15/A.15__001_intro.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "A.15 — Role–Method–Work Alignment (Contextual Enactment)"
  - "A.15:intro — Intro"
line_start: 20336
line_end: 20396
dependencies:
  - "A.10"
  - "A.12"
  - "A.15"
  - "A.15.1-A.15.4"
  - "A.15.4"
  - "A.2"
  - "A.20"
  - "A.21"
  - "A.4"
  - "A.6"
  - "A.6.B"
  - "A.6.C"
  - "B.3"
  - "C.24"
  - "C.26.2"
  - "C.28"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.16"
  - "E.17"
  - "E.17.EFP"
  - "E.18.1"
keywords:
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.WorkPlan"
  - "actual U.Work"
  - "contextual enactment"
  - "coordinated-work evidence"
  - "role-method-work distinction"
  - "source-restoration boundary"
  - "work admission display"
---

## A.15 - Role–Method–Work Alignment (Contextual Enactment)

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** This pattern is the enactment-alignment pattern for engineer-managers when the real confusion is not "what component is this" but `who is responsible`, `how the work is supposed to happen`, `when the plan applies`, and `what actually happened`.

**Use this when.** Use this pattern when the real job is to separate role, method, plan, capability, and actual work before a team treats one cue, one schedule, one display, one copied or generated statement, or one document as if it already counted as the role assignment, the method, the work plan, execution evidence, or the work itself.

**Start here when.** The dominant ambiguity is role vs method vs schedule vs actual run, and the team keeps arguing over a source-side "process" cue without separating recipe, plan, capability, and executed work.

**First output.** One explicit separation of `U.Role`, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work`, plus the shortest traceable chain that already exists from `U.RoleAssignment` through the governing `U.Method` and its method-description source to the intended `U.WorkPlan` or actual `U.Work` occurrence, or an explicit source gap that blocks admission of the claim.

**Working enactment-alignment spine.** Role, method, plan, and work confusion -> separate role, holder, bounded context, method description, intended `U.WorkPlan`, and actual `U.Work` -> choose proceed, plan, bounded probe, narrow, apply the direct governing pattern for any non-A.15 claim, or stop -> output the smallest alignment frame needed for the next project move -> use `A.15.4` only when an encountered episteme publication, display, credential view, explanation, copied statement, provenance mark, dashboard tile, schema wording, API wording, or composed source chain begins to carry or justify a work claim or reliance claim.

**Working application moves.**
1. Name the role, holder, and context distinction under repair.
2. Name the method or method description that is meant to govern the work.
3. Name the intended `U.WorkPlan` or actual `U.Work` occurrence being claimed.
4. Choose the next move: proceed inside the recovered relation, plan, run a bounded reversible probe, narrow scope, apply the governing FPF pattern and project-side FPF kind and reference named by value for the claim or effect being made, or stop.
5. If an encountered source candidate or display is being used by appearance for a work claim, reliance claim, or source-restoration claim, apply `A.15.4 Work-Relevant Source Restoration` to that source-restoration claim; keep `A.15` only for the `U.Role`, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work` separation.

**Action-pattern protection.** This pattern is not about classifying encountered publications, displays, or cues. It keeps role, method, plan, capability, and actual work distinct so the acting engineer-manager can choose the next admissible project move. Work-relevant source restoration is handled by the related `A.15.4` cluster member.

**Minimum sufficient next move.** Choose the minimum sufficient next move, recover only the project-side FPF kind and reference named by value needed for that move, and do not raise the claim beyond that recovered relation, source, or admissible-use boundary.

**Recovered-source ready condition.** If the required project-side FPF kind and reference named by value is present and its scope and window match the role, method, plan, or work move under repair, proceed inside that recovered scope and window. If not, narrow scope, run a bounded reversible probe, source-find, or create only the smallest source-restoration request, decision-request record, prospective work-plan entry, source-gap note, or missing-source admission block needed for the next move.

**Ordinary use.** If the team only needs to separate role, method, plan, capability, and actual work for orientation or planning, one separation sentence or small working card is enough.

**Reliance-bearing use.** Use the fuller alignment frame when an encountered source candidate or display is about to guide planned work, actual work, role attribution, status attribution, release reliance, disputed responsibility, or cross-context use. Use `A.15.4` when the issue under repair is whether that source candidate exposes the project-side FPF kind and reference named by value needed for that work claim or reliance claim.

**Stop condition.** Stop once the separation changes no next admissible work move or reliance move and blocks no concrete overclaim about role, method, plan, work, status, approval, evidence, or release.

**Admissible-use examples.**

| Admissible project use | Source-finding or reversible probe | Non-admissible use |
| --- | --- | --- |
| A maintenance team names `PumpInspectorRole`, the inspection method description, the current `U.WorkPlan`, and the dated `U.Work` record that will be created after the inspection. The team may plan and perform the inspection under those distinct records. | A short briefing says the inspection is ready, but the method description or work plan is missing; use the briefing only to find or repair the missing source before planned work proceeds. | A dashboard tile, copied approval, generated explanation, or briefing is used as the source for a work or reliance claim by appearance. Use `A.15.4` for that source-restoration question. |

**Alignment frame in plain terms.** One alignment frame linking `U.Role`, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work` through `U.RoleAssignment`; not a single work occurrence, not a checklist, not a language-style repair pattern, and not a mere cue note.

**First admissible project move in plain terms.** Keep design-time role, method, and work plan distinct from run-time work while making the chain between them inspectable enough for enactment, audit, and source restoration.

**What goes wrong if missed.** Teams collapse role, recipe, plan, capability, and actual run into one fuzzy source-side "process" label, then mistake documentation for execution, capability for evidence, schedule for occurrence, or a narrower briefing for the source that makes work admissible.

**What this buys.** One inspectable enactment frame that lets a team ask who held what role, which method governed, what plan existed, and what work actually occurred before treating follow-on work, blame, or approval as if those distinctions were the same.

**Not this pattern when.** Not this pattern when the honest need is only one dated work occurrence (`A.15.1`), only planning or schedule baseline (`A.15.2`), only a cue note that has not yet become an enactment-alignment question (`A.16` or `A.16.1`), only boundary wording or policy wording without a role-method-work question under repair (`A.6` or `A.6.B`), or work-relevant source restoration for an encountered source candidate or display (`A.15.4`).

**Related project records and governing patterns.** `A.15.1` governs dated execution records, `A.15.2` schedule or baseline planning records, `A.15.3` slot-filling plan items, `A.15.4` work-relevant source restoration, `B.5.1` Explore -> Shape -> Evidence -> Operate for project progression, `F.11` method and work vocabulary alignment across contexts, and `F.17` the human-facing work sheet.

**Causal-use work boundary.** Realized counterfactual-sampling work, counterfactual randomization, intervention assignment, target-trial emulation work, and causal evidence collection remain `U.MethodDescription`, `U.WorkPlan`, and `U.Work` structures here. `A.15` can say who performs which sampling or intervention work under which method and role; it does not make the resulting causal use admissible. `C.28` governs the causal-use question, `CausalityLadderRung`, causal estimand, `CausalEvidenceSupportBasis`, counterfactual sampling realizability, and supported use and unsupported use.

**Related-record mistakes.** If the first honest encountered source cue is still only a cue, keep it under `A.16` or `A.16.1`; if the question under repair is boundary wording, promise, agreement-like service, or policy wording, recover the corresponding `A.6` boundary-claim record; if you only need one executed occurrence rather than the alignment frame, recover the `A.15.1` dated work-occurrence record; if an encountered source candidate or display is being used for a work relation or reliance relation, use `A.15.4`.

**Boundary to coarsened renderings.** A lighter briefing, summary, redacted note, or coarsened rendering may orient work or cue attention. It becomes sufficient for work execution, plan use, approval, gate decision, or execution evidence only when the required method, plan, approval, gate, or evidence source remains explicit and reopenable. Treat the coarsened-rendering relation through `A.6.3.CSC Controlled Semantic Coarsening` when the rendering itself changes what can be relied on.

**Use boundary.** Use `A.15` when the current project question needs role-method-work alignment. If the current claim is one single work occurrence, source-restoration note, wording repair, assurance claim, or source-side "process" label, use the governing pattern for that claim and keep only the A.15 separation that remains needed.

