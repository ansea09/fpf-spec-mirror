---
chunk_kind: "child"
pattern_id: "A.15"
pattern_title: "Role–Method–Work Alignment (Contextual Enactment)"
section_id: "A.15:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15/A.15__008_conformance-checklist.md"
commit_sha: "7c617d5d0fa1abf94a21bac2dd909f68ed514249"
heading_path:
  - "A.15 — Role–Method–Work Alignment (Contextual Enactment)"
  - "A.15:7 — Conformance Checklist"
line_start: 20691
line_end: 20712
dependencies:
  - "A.10"
  - "A.12"
  - "A.15.1"
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
  - "E.16"
  - "E.17"
  - "E.17.EFP"
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

### A.15:7 - Conformance Checklist

To preserve role-method-work modeling, a conforming model or use SHALL satisfy the following checks.

| ID | Requirement (Normative Predicate) | Purpose and Rationale |
| :--- | :--- | :--- |
| **CC-A15-1 (Entity Distinction)** | A conforming model SHALL keep `U.Role`, **`U.Method`**, **`U.MethodDescription`**, `U.Capability`, **`U.WorkPlan`**, and `U.Work` as distinct, non-overlapping types. | This is the core enforcement of **Strict Distinction (A.7)**. It prevents the category errors outlined in the "Problem" section. |
| **CC-A15-1a (Work target and kind predicate)** | A conforming `U.Work` record SHALL satisfy `A15-WF-1`; validators SHOULD report missing `primaryTarget` or missing `kind` as a nonconforming `U.Work` record. | Keeps target and work kind enforceable as work-record conformance without stating modeled-world admissibility through a free RFC sentence. |
| **CC-A15-2 (Temporal Scope)** | `U.Method`, `U.MethodDescription`, and `U.WorkPlan` exist in **design-time**; `U.Work` exists in **run-time**. Design-time method descriptions and work plans are not mutated by operational events. | Enforces **Temporal Duality (A.4)**. Blueprints cannot be mutated by operational events. |
| **CC-A15-3 (RoleAssignment Mandate)** | A conforming `U.Work` record SHALL link via `performedBy` to a `U.RoleAssignment` satisfying the governing role, holder, and bounded-context constraints. | Guarantees that every work occurrence has a clearly identified, context-bound actor, ensuring accountability. |
| **CC-A15-4 (Traceability Chain)** | A conforming model SHALL provide an unbroken chain for every `U.Work`: `Work -performedBy-> RoleAssignment`, `Work -enactsMethod-> Method`, and, when a description or source is used to identify or constrain the method, `Method -isDescribedBy-> MethodDescription` or `methodDescriptionRef`. Capability checks are evaluated against the holder at run time. | Ensures end-to-end auditability from a specific work occurrence back to the enacted method and the recipe or source used to identify or constrain it. |
| **CC-A15-5 (No Roles in Mereology)** | A conforming model SHALL NOT place `U.Role` or `U.Capability` in a mereological (`partOf`) hierarchy. | The "Role-as-Part" anti-pattern is a violation. Roles and capabilities are functional, not structural. Enforces **A.14**. |
| **CC-A15-6 (Resource Honesty)** | A conforming model SHALL associate resource consumption (`U.Resource`) only with `U.Work`, never with `U.MethodDescription` or `U.Capability`. | Enforces that costs are tied to actual events, not to plans or potential. Aligns with **Resrc-CAL (C.5)**. |
| **CC-A15-7 (Plan and Run Split)** | A conforming model SHALL represent schedules and calendars as `U.WorkPlan` (A.15.2). A `U.WorkPlan` SHALL NOT be used as evidence of execution; only `U.Work` carries actuals. | Preserves plan and run separation and prevents schedule-as-actual drift. |
| **CC-A15-8 (Source-cue resolution)** | A conforming use SHALL interpret unqualified "process", "workflow", or "schedule" source cues per **L-PROC**, **L-FUNC**, and **L-SCHED**: workflow cue resolves to `U.MethodDescription` unless the abstract way-of-doing itself is being claimed as `U.Method`; schedule cue resolves to `U.WorkPlan`; what happened resolves to `U.Work`. | Keeps source vocabulary auditable and reduces lexical ambiguity without creating a new process object. |
| **CC-A15-9 (Enactment)** | A conforming `U.Work` record enacts a `U.Method` under a `U.RoleAssignment`; a `MethodDescription` is the source episteme or method-description reference when the method must be identified, constrained, or justified. Spontaneous physical evolution without a role-method-work alignment is modeled as `U.Dynamics`, not as `U.Work`. | Prevents background dynamics and recipe documents from being miscast as governed work. |
| **CC-A15-10 (GateSplit)** | A conforming model SHALL represent a SpeechAct that institutes a role, authorization, or gate-relevant effect (e.g., "Approve", "Authorize") as a distinct `U.Work` step (`kind=Communicative`). It may create the Green-Gate condition for a subsequent operational step, but it SHALL NOT be conflated with that step. | Preserves communicative effects as distinct acts. |
| **CC-A15-11 (KindFit)** | A conforming `performedBy` assignment SHALL use a `U.Role` appropriate for the `U.Work` kind (e.g., `ApproverRole` for communicative approvals; `DeployerRole` for operational deployments). | Prevents kind-mismatched role attribution. |
| **CC-A15-12 (Causal-use Work Boundary)** | A conforming causal-use model MAY represent intervention assignment, counterfactual randomization, target-trial emulation, causal evidence collection, and realized counterfactual-sampling work here only as `U.Method`, `U.MethodDescription`, `U.WorkPlan`, `U.Work`, and role-assigned execution structure. Any claim that the resulting causal use is admissible SHALL cite `C.28` for causal-use question, `CausalityLadderRung`, causal estimand, `CausalEvidenceSupportBasis`, `CausalUseSupportVerdict`, and supported use and unsupported use. | Prevents method, work-plan, or work-occurrence structure from being mistaken for causal-use authority. |
| **CC-A15-13 (A.15.4 Boundary)** | If an encountered source-looking carrier or display is being used for a work relation or reliance relation by appearance, a conforming `A.15` use SHALL use `A.15.4` for the source-restoration question and keep only the `U.Role`, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work` separation here. | Prevents the A.15 kernel from absorbing source-restoration claims. |
| **CC-A15-14 (P2W Publication Boundary)** | A conforming use SHALL NOT treat a principle scheme, functional diagram, scenario, screen, or explanation that makes an `E.18.1` P2W carry-through structure recoverable as the selected method, `U.WorkPlan`, performed `U.Work`, work-result record, result measurement, or non-A.15 claim by publication alone. | The project use names the selected `A.15` object named by value; any non-A.15 claim uses its governing pattern or `A.15.4` source restoration. |

