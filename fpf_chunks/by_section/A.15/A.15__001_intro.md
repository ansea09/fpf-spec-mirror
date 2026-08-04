---
chunk_kind: "child"
pattern_id: "A.15"
pattern_title: "Role–Method–Work Alignment"
section_id: "A.15:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15/A.15__001_intro.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "A.15 — Role–Method–Work Alignment"
  - "A.15:intro — Intro"
line_start: 23972
line_end: 24032
dependencies:
  - "A.10"
  - "A.12"
  - "A.15"
  - "A.15.1-A.15.5"
  - "A.15.4"
  - "A.15.5"
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
  - "C.32.P2S"
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
  - "appearance-based reliance boundary"
  - "contextual enactment"
  - "coordinated-work evidence"
  - "role-method-work distinction"
  - "work admission display"
  - "work-entry readiness"
---

## A.15 - Role–Method–Work Alignment

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** This pattern is the enactment-alignment pattern for engineer-managers when the real confusion is not "what component is this" but `who is responsible`, `how the work is supposed to happen`, `when the plan applies`, and `what actually happened`.

**Use this when.** Use this pattern when the real job is to separate role, method, plan, holder `U.Capability` instance, any capability statement or currentness assessment relied on, capability-fit checks, and performed work before a team treats one cue, one schedule, one display, one copied or generated statement, or one document as if it already counted as the role assignment, the method, the work plan, execution evidence, or the work itself.

**Start here when.** The dominant ambiguity is role vs method vs schedule vs performed work occurrence, and the team keeps arguing over encountered "process" wording without separating recipe, plan, capability, and executed work.

**First output.** One explicit separation of `U.Role`, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, `U.Work` as the admitted kind, one dated Work occurrence admitted under that kind, and any separate assertion or description about it, plus the shortest traceable chain that already exists from `U.RoleAssignment` through the governing `U.Method` and its `methodDescriptionRef` or `U.MethodDescription` reference to the intended `U.WorkPlan` or actual Work occurrence, or an explicit source-relation gap that blocks admission of the claim.

**Working enactment-alignment sequence.** Role, method, plan, and work confusion -> separate the role, holder, role-taxonomy episteme, effective reference scheme, method description, intended `U.WorkPlan`, `U.Work` kind, actual dated Work occurrence, and any record about it -> choose proceed, plan, bounded probe, narrow, apply the direct governing pattern for any non-A.15 claim, or stop -> output the smallest alignment frame needed for the next work-family use -> use `A.15.4` only when an encountered episteme publication, display, credential view, explanation, copied statement, provenance mark, dashboard tile, schema wording, API wording, or composed source-relation chain begins to carry or justify a work claim or reliance claim.

**Working alignment applications.**
1. Name the role, holder, exact role-taxonomy episteme, and effective reference scheme under repair.
2. Name the method or method description that is meant to govern the work.
3. Name the intended `U.WorkPlan`, or identify the actual dated Work occurrence admitted under `U.Work` and keep any assertion or record about it separate.
4. Choose the next governed use: proceed inside the recovered relation, plan, run a bounded reversible probe, narrow scope, apply the governing FPF pattern and project-side FPF kind and reference named by value for the claim or effect being made, or stop.
5. If a reliance appearance such as a display, credential view, copied approval, generated explanation, publication face, or cue is being used by appearance for a work claim or reliance claim before the governing pattern position is named, apply `A.15.4` work-relevant appearance-based reliance repair to that claim; keep `A.15` only for the separation among `U.Role`, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, `U.Work` as the admitted kind, each actual Work individual admitted under it, and every separate episteme about such an occurrence.

**Action-pattern protection.** This pattern is not about classifying encountered publications, displays, or cues. It keeps role, method, plan, holder `U.Capability` instance, separately governed capability-support records and relations, capability-fit checks, and performed work distinct so the acting engineer-manager can choose the next admissible work-family or reliance use. Work-relevant appearance-based reliance repair is handled by the related `A.15.4` cluster member.

**Minimum sufficient governed use.** Choose the minimum sufficient governed use, recover only the project-side FPF kind and reference named by value needed for that use, and do not raise the claim beyond that recovered relation, source, or admissible-use boundary.

**Recovered governing-reference sufficiency condition.** If the required project-side FPF kind and reference named by value is present and its scope and window match the role, method, plan, or work-family claim under repair, proceed inside that recovered scope and window. If not, narrow scope, run a bounded reversible probe, find the missing source relation, or create only the smallest `A.15.4` repair request, decision-request record, prospective work-plan entry, missing-source-relation note, or missing-source admission block needed for the next governed use.

**Ordinary use.** If the team only needs to separate role, method, plan, holder `U.Capability` instance, capability-fit checks, and performed work for orientation or planning, one separation sentence or small working card is enough.

**Reliance-bearing use.** Use the fuller alignment frame when a reliance appearance is about to guide planned work, performed work, role attribution, role-state attribution, release reliance, disputed responsibility, or use under another role taxonomy or reference scheme. Use `A.15.4` when the issue under repair is whether that appearance exposes the project-side FPF kind and reference named by value required for that work claim or reliance claim.

**Stop condition.** Stop once the separation changes no next admissible work-family use or reliance use and blocks no concrete overclaim about role, role-state, method, plan, work, approval, evidence, or release.

**Admissible-use examples.**

| Admissible project use | Source-finding or reversible probe | Non-admissible use |
| --- | --- | --- |
| A maintenance team names `PumpInspectorRole`, the inspection method description, and the current `U.WorkPlan`. After the inspection actually occurs, it identifies the dated Work occurrence admitted under `U.Work` and creates a separate inspection record that designates it. The plan, occurrence, and record remain distinct. | A short briefing says the inspection is ready, but the method description or work plan is missing; use the briefing only to find or repair the missing source before planned work proceeds. | A dashboard tile, copied approval, generated explanation, or briefing is used as the source for a work or reliance claim by appearance. Use `A.15.4` for appearance-based reliance repair. |

**Alignment frame in plain terms.** One alignment frame that keeps `U.Role`, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, `U.Work` as the admitted kind, one actual Work individual admitted under it, and any episteme about that occurrence distinct, while exact `performedUnderAssignment` and `enactsMethod` relations connect the occurrence to its `U.RoleAssignment` and `U.Method`; the admitted holder system is the actual performer under the assignment. This is not a single work occurrence, checklist, language-style repair pattern, or mere cue note.

**First admissible work-family use in plain terms.** Keep role value, holder assignment, semantic method, method-description reference, intended work plan, and dated performed work distinct while making the chain between them inspectable enough for enactment, audit, and source-relation recovery.

**What goes wrong if missed.** Teams collapse role, recipe, plan, capability, and performed work occurrence into one fuzzy "process" label from project material, then mistake documentation for execution, capability for evidence, schedule for occurrence, or a narrower briefing for the relation that makes work admissible.

**What this buys.** One inspectable enactment frame that lets a team ask who held what role, which method governed, what plan existed, and what work actually occurred before treating follow-on work, blame, or approval as if those distinctions were the same.

**Not this pattern when.** Not this pattern when the honest need is only one dated work occurrence (`A.15.1`), only planning or schedule baseline (`A.15.2`), only work-entry readiness or full-kit preparation (`A.15.5`), only a cue note that has not yet become an enactment-alignment question (`A.16` or `A.16.1`), only boundary wording or policy wording without a role-method-work question under repair (`A.6` or `A.6.B`), or work-relevant appearance-based reliance repair for a display, credential view, copied approval, generated explanation, publication face, or similar reliance appearance (`A.15.4`).

**Related project records and governing patterns.** `A.15.1` governs dated Work occurrences admitted under `U.Work` and the boundary to separate assertions or records about them; `A.15.2` governs schedule or baseline planning records, `A.15.3` slot-filling plan items, `A.15.4` work-relevant appearance-based reliance repair, `A.15.5` work-entry readiness and full-kit preparation, `B.5.1` Explore -> Shape -> Evidence -> Operate for project progression, `F.11` method and work vocabulary alignment across contexts, and `F.17` the human-facing work sheet.

**Causal-use work boundary.** Realized counterfactual-sampling work, counterfactual randomization, intervention assignment, target-trial emulation work, and causal evidence collection remain separately represented here as `U.MethodDescription` epistemes, `U.WorkPlan` epistemes, and world-side Work individuals admitted under `U.Work` together with their exact role and method relations. `A.15` can say who performs which sampling or intervention work under which method and role; it does not make the resulting causal use admissible. `C.28` governs the causal-use question, `CausalityLadderRung`, causal estimand, `CausalEvidenceSupportBasis`, counterfactual sampling realizability, and supported use and unsupported use.

**Related-record mistakes.** If the first honest cue is still only a cue, keep it under `A.16` or `A.16.1`; if the question under repair is boundary wording, promise, agreement-like service, or policy wording, recover the corresponding `A.6` boundary-claim record; if you need one executed occurrence rather than the alignment frame, recover the dated Work occurrence under `A.15.1` and create or cite a separate assertion or record only when that episteme is also needed; if a reliance appearance is being used for a work relation or reliance relation, use `A.15.4`.

**Boundary to coarsened renderings.** A lighter briefing, summary, redacted note, or coarsened rendering may orient work or cue attention. It becomes sufficient for work execution, plan use, approval, gate decision, or execution evidence only when the required method, plan, approval, gate, or evidence source remains explicit and reopenable. Treat the coarsened-rendering relation through `A.6.3.CSC Controlled Semantic Coarsening` when the rendering itself changes what can be relied on.

**Use boundary.** Use `A.15` when the current project question needs role-method-work alignment. If the current claim is one single work occurrence, `A.15.4` repair note, wording repair, assurance claim, or encountered "process" label, use the governing pattern for that claim and keep only the A.15 separation that remains needed.

