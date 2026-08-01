---
chunk_kind: "child"
pattern_id: "A.15"
pattern_title: "Role–Method–Work Alignment"
section_id: "A.15:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15/A.15__008_conformance-checklist.md"
commit_sha: "1eb56cd0cfd6dccad65143e03d28509373bd8dd5"
heading_path:
  - "A.15 — Role–Method–Work Alignment"
  - "A.15:7 — Conformance Checklist"
line_start: 24129
line_end: 24150
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

### A.15:7 - Conformance Checklist

To preserve role-method-work modeling, check the following predicates.

| ID | Predicate | Purpose and rationale |
| :--- | :--- | :--- |
| **CC-A15-1 (Entity Distinction)** | Keep the role value, `U.Method`, `U.MethodDescription` episteme, `U.Capability` instance, `U.WorkPlan` episteme, `U.Work` kind, and each Work individual admitted under it distinct. | This is the core use of A.7 strict distinction for role-method-work alignment. |
| **CC-A15-1a (Work ontic-epistemic boundary)** | `U.Work` is the admitted kind; one Work individual is the world-side dated occurrence; any assertion, description, log, ticket, or performed-work record about it is a separate `U.Episteme`. Actual performer, method, temporal, containing-system, affected-referent, binding, and resource-use relations obtain independently and are not fields stored in the occurrence. | Blocks record-schema fields, appearance, or documentation from constituting Work. |
| **CC-A15-2 (Kind Scope)** | `U.Method` is the semantic way of doing, `U.MethodDescription` is the description episteme, `U.WorkPlan` is the intended-work episteme, `U.Work` is the admitted kind, and one Work individual is a dated performed occurrence. Operational events do not mutate method descriptions or work plans. | Preserves method, description, plan, kind, occurrence, and record separation. |
| **CC-A15-3 (RoleAssignment link)** | One exact Work occurrence admitted under `U.Work` stands through `performedUnderAssignment` to a `U.RoleAssignment` whose generic signature has exactly holder `U.System`, assigned `U.Role`, role-taxonomy episteme, and effective `U.ReferenceScheme`; that admitted holder system actually performs the Work and the assignment's extent covers the attributed extent. A separate assertion may state this relation. | Gives every work occurrence an exact performer and recoverable role meaning without making the assignment act or making a record, planned window, or selected model-use structure a generic participant. |
| **CC-A15-4 (Traceability Chain)** | Each Work occurrence admitted under `U.Work` can be traced through `Work -performedUnderAssignment-> RoleAssignment`, the assignment's `HolderSystemSlot` to the admitted system that performed it, and `Work -enactsMethod-> Method`. When a method-description episteme, `methodDescriptionRef`, source `U.Episteme`, source `U.EpistemePublication`, or source relation is used to identify or constrain that Method, a separate assertion cites it. For a `U.MethodDescription`, the cited episteme's exact `EntityOfConcern` resolves to that Method and its substantive method claims make the A.3.2 membership basis recoverable; no binary description relation is added. Capability-fit checks are evaluated against the holder's `U.Capability` instance and any declared `U.Characteristic` value, Q-Bundle slot, or architecture-characteristic input for that occurrence. | Keeps auditability from occurrence back to actual performer, assignment, method, holder capability instance, and separate descriptive sources when those are used. |
| **CC-A15-5 (No Roles in Mereology)** | Do not place `U.Role`, `U.Capability`, separately governed capability-support records or relations, or capability-fit predicates in a mereological `partOf` hierarchy. | Blocks role-as-part, capability-as-part, support-as-part, and fit-predicate-as-part mistakes. |
| **CC-A15-6 (Resource Honesty)** | Attribute resource consumption through exact obtaining relations to Work individuals admitted under `U.Work`, not to `U.MethodDescription`, `U.WorkPlan`, `U.Capability`, separately governed capability-support records or relations, or capability-fit predicates. A ledger or report about resource use is a separate episteme. | Keeps costs tied to performed occurrences rather than recipes, plans, abilities, statements, or admission checks. |
| **CC-A15-7 (Plan and Occurrence Split)** | Represent schedules and calendars as `U.WorkPlan` under A.15.2. Do not use a `U.WorkPlan` as evidence that execution occurred; actual performed values require an independently identified Work occurrence and its obtaining relations. | Preserves intended-work and performed-work separation and prevents schedule-as-performed-work drift. |
| **CC-A15-8 (Wording-cue resolution)** | Interpret unqualified "process", "workflow", "activity", or "schedule" wording through `E.10` and `E.10.ARCH`: recover whether the wording points to `U.Method`, `U.MethodDescription`, `U.WorkPlan`, the `U.Work` kind, one Work individual admitted under it, or another direct governing pattern. | Keeps project vocabulary auditable without creating a generic process object. |
| **CC-A15-9 (Enactment)** | One Work occurrence admitted under `U.Work` stands in `enactsMethod` to a `U.Method` and in `performedUnderAssignment` to a `U.RoleAssignment`; the assignment's admitted holder system is the actual performer, while a `MethodDescription` and any performed-work record are separate epistemes and admitted source material remains under a separate source-use relation. Spontaneous physical evolution without role-method-work alignment is modeled as `U.Dynamics`, not as Work. | Prevents assignments, background dynamics, records, and recipe documents from being miscast as actors or governed work. |
| **CC-A15-10 (Gate split)** | A speech act that institutes a role, authorization, or gate-relevant effect is a distinct Work occurrence admitted under `U.Work` only when the A.15.1 occurrence basis and exact effect relation obtain. It may create a gate-relevant condition for later operational work, but it is not that operational work. | Preserves communicative effects as distinct acts without defining a local Work subkind by label. |
| **CC-A15-11 (Role fit)** | A `performedUnderAssignment` relation uses a `U.RoleAssignment` whose admitted holder system is the actual performer, whose exact role meaning, role taxonomy, and effective scheme fit the particular Work occurrence, and whose extent covers the attributed work extent. An approver or deployer label does not create a Work subkind or prove performance. | Prevents assignment-as-actor, role mismatch, and kind-by-example classification. |
| **CC-A15-12 (Causal-use work boundary)** | Intervention assignment, counterfactual randomization, target-trial emulation, causal evidence collection, and realized counterfactual-sampling work may be represented here only through exact `U.Method`, `U.MethodDescription`, `U.WorkPlan`, Work individuals admitted under `U.Work`, and their separately obtaining role and method relations. Any causal-use admissibility claim cites `C.28` for causal-use question, `CausalityLadderRung`, causal estimand, `CausalEvidenceSupportBasis`, `CausalUseSupportVerdict`, supported use, and unsupported use. | Prevents method, plan, occurrence, or relation structure from being mistaken for causal-use authority. |
| **CC-A15-13 (A.15.4 boundary)** | If a reliance appearance is being used for a work relation or reliance relation by appearance, use `A.15.4` for appearance-based reliance repair and keep only the role, method, method-description, work-plan, and work separation here. | Prevents the A.15 kernel from absorbing appearance-based reliance claims. |
| **CC-A15-14 (P2W publication boundary)** | Do not treat a principle scheme, functional diagram, scenario, screen, or explanation that makes an `E.18.1` P2W carry-through structure recoverable as the selected method, `U.WorkPlan`, a performed Work occurrence admitted under `U.Work`, work-result record, result measurement, or non-A.15 claim by publication alone. | The project use names the selected A.15 object by value; any non-A.15 claim uses its governing pattern or `A.15.4` appearance-based reliance repair. |

