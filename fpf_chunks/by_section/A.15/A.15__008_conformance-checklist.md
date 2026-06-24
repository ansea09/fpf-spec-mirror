---
chunk_kind: "child"
pattern_id: "A.15"
pattern_title: "Role–Method–Work Alignment (Contextual Enactment)"
section_id: "A.15:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15/A.15__008_conformance-checklist.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "A.15 — Role–Method–Work Alignment (Contextual Enactment)"
  - "A.15:7 — Conformance Checklist"
line_start: 21132
line_end: 21153
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
  - "work-entry readiness"
---

### A.15:7 - Conformance Checklist

To preserve role-method-work modeling, check the following predicates.

| ID | Predicate | Purpose and rationale |
| :--- | :--- | :--- |
| **CC-A15-1 (Entity Distinction)** | Keep `U.Role`, `U.Method`, `U.MethodDescription`, `U.Capability`, `U.WorkPlan`, and `U.Work` as distinct values. | This is the core use of A.7 strict distinction for role-method-work alignment. |
| **CC-A15-1a (Work target and kind predicate)** | A `U.Work` record satisfies `A15-WF-1`: `primaryTarget` and `kind` are present. Missing target or kind lowers the work-record conformance claim. | Keeps target and work kind enforceable as work-record predicates without RFC deontic prose. |
| **CC-A15-2 (Temporal Scope)** | `U.Method`, `U.MethodDescription`, and `U.WorkPlan` are design-time or plan-side values; `U.Work` is the dated performed occurrence. Operational events do not mutate method descriptions or work plans. | Preserves design-time and run-time separation. |
| **CC-A15-3 (RoleAssignment link)** | A `U.Work` record links through `performedBy` to a `U.RoleAssignment` satisfying the governing role, holder, bounded-context, and window constraints. | Gives every work occurrence a context-bound actor without making the role act by itself. |
| **CC-A15-4 (Traceability Chain)** | Each `U.Work` occurrence can be traced through `Work -performedBy-> RoleAssignment`, `Work -enactsMethod-> Method`, and, when a description or source is used to identify or constrain the method, `Method -isDescribedBy-> MethodDescription` or `methodDescriptionRef`. Capability checks are evaluated against the holder at run time. | Keeps auditability from occurrence back to method and the method-description source when that source is used. |
| **CC-A15-5 (No Roles in Mereology)** | Do not place `U.Role` or `U.Capability` in a mereological `partOf` hierarchy. | Blocks role-as-part and capability-as-part mistakes. |
| **CC-A15-6 (Resource Honesty)** | Associate resource consumption with `U.Work`, not with `U.MethodDescription`, `U.WorkPlan`, or `U.Capability`. | Keeps costs tied to actual occurrences rather than recipes, plans, or abilities. |
| **CC-A15-7 (Plan and Run Split)** | Represent schedules and calendars as `U.WorkPlan` under A.15.2. Do not use a `U.WorkPlan` as evidence that execution occurred; only `U.Work` carries actuals. | Preserves plan-side and run-time separation and prevents schedule-as-actual drift. |
| **CC-A15-8 (Source-cue resolution)** | Interpret unqualified "process", "workflow", "activity", or "schedule" source cues through `E.10` and `E.10.ARCH`: recover whether the cue points to `U.Method`, `U.MethodDescription`, `U.WorkPlan`, `U.Work`, or another direct governing pattern. | Keeps source vocabulary auditable without creating a generic process object. |
| **CC-A15-9 (Enactment)** | A `U.Work` record enacts a `U.Method` under a `U.RoleAssignment`; a `MethodDescription` is the source episteme or method-description reference when the method is identified, constrained, or justified by a source. Spontaneous physical evolution without role-method-work alignment is modeled as `U.Dynamics`, not as `U.Work`. | Prevents background dynamics and recipe documents from being miscast as governed work. |
| **CC-A15-10 (Gate split)** | A speech act that institutes a role, authorization, or gate-relevant effect is a distinct communicative `U.Work` occurrence when the act itself is being modeled. It may create a gate-relevant condition for later operational work, but it is not that operational work. | Preserves communicative effects as distinct acts. |
| **CC-A15-11 (Kind fit)** | A `performedBy` relation uses a `U.RoleAssignment` whose role fits the `U.Work` kind and context, such as an approver role for communicative approval work or deployer role for operational deployment work. | Prevents kind-mismatched role attribution. |
| **CC-A15-12 (Causal-use work boundary)** | Intervention assignment, counterfactual randomization, target-trial emulation, causal evidence collection, and realized counterfactual-sampling work may be represented here only as `U.Method`, `U.MethodDescription`, `U.WorkPlan`, `U.Work`, and role-assigned execution structure. Any causal-use admissibility claim cites `C.28` for causal-use question, `CausalityLadderRung`, causal estimand, `CausalEvidenceSupportBasis`, `CausalUseSupportVerdict`, supported use, and unsupported use. | Prevents method, plan, or occurrence structure from being mistaken for causal-use authority. |
| **CC-A15-13 (A.15.4 boundary)** | If an encountered source candidate or display is being used for a work relation or reliance relation by appearance, use `A.15.4` for the source-restoration question and keep only the role, method, method-description, work-plan, and work separation here. | Prevents the A.15 kernel from absorbing source-restoration claims. |
| **CC-A15-14 (P2W publication boundary)** | Do not treat a principle scheme, functional diagram, scenario, screen, or explanation that makes an `E.18.1` P2W carry-through structure recoverable as the selected method, `U.WorkPlan`, performed `U.Work`, work-result record, result measurement, or non-A.15 claim by publication alone. | The project use names the selected A.15 object by value; any non-A.15 claim uses its governing pattern or `A.15.4` source restoration. |

