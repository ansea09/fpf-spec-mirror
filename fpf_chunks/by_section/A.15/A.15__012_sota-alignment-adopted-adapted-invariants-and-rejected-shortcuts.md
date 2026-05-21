---
chunk_kind: "child"
pattern_id: "A.15"
pattern_title: "Role–Method–Work Alignment (Contextual Enactment)"
section_id: "A.15:11"
section_title: "SoTA Alignment: Adopted/Adapted Invariants And Rejected Shortcuts"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15/A.15__012_sota-alignment-adopted-adapted-invariants-and-rejected-shortcuts.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "A.15 — Role–Method–Work Alignment (Contextual Enactment)"
  - "A.15:11 — SoTA Alignment: Adopted/Adapted Invariants And Rejected Shortcuts"
line_start: 19757
line_end: 19790
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

### A.15:11 - SoTA Alignment: Adopted/Adapted Invariants And Rejected Shortcuts

**SoTA alignment rule.** Read each row here as source idea -> local FPF invariant -> practical local test -> popular shortcut rejected. A source citation governs nothing by reputation; it counts only when the cited idea is translated into the Solution, conformance checks, boundary rules, worked slices, and Relations of this pattern.


**Claim 1.** Best-known current workflow, digital-thread, and service-operations practice keeps recipe, plan, and execution separate.

**Practice source, local alignment, and adoption decision.** Contemporary process modeling, service operations, and auditability practice after 2015 separates procedure, schedule, and executed occurrence because otherwise paper compliance becomes indistinguishable from completed work. In the manufacturing and peer-review slices above, this means a procedure or calendar never counts as the weld or the review itself. This pattern **adopts** that separation, **adapts** it through `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work`, and **rejects** the shortcut where one undifferentiated "process" object carries all three loads.

**Claim 2.** Best-known current accountability practice keeps actor-in-context explicit rather than attributing work to a role label or a document.

**Practice source, local alignment, and adoption decision.** Contemporary governance, service delivery, and incident practice distinguishes accountable assignee, governing procedure, and actual run record because post-hoc review depends on knowing who acted, under what role, and under which method. In the slices above, that is why the robot or reviewer acts under `U.RoleAssignment` rather than the role or guideline acting on its own. This pattern **adopts** explicit actor-in-context attribution through `U.RoleAssignment`, **adapts** it to bounded-context semantics, and **rejects** anonymous work logs and role-as-part modeling.

**Claim 3.** Best-known current approval and execution practice treats communicative gate acts and operational acts as distinct kinds of work.

**Practice source, local alignment, and adoption decision.** Contemporary release, compliance, and safety-critical practice separates approval, authorization, and review acts from the operational steps they permit because authority change and world change are not the same event. In the examples above, that means an approval is not the same work as a deployment or a weld. This pattern **adopts** that split, **adapts** it through communicative versus operational `U.Work` kinds, and **rejects** the collapse of approval into the thing being approved.

**Local stance.** The load-bearing SoTA claim for this pattern is practical and narrow: contextual enactment remains reviewable only when role, method, plan, and work stay distinct enough that audits can tell whether the problem was in the assignment, the recipe, the schedule, the capability, or the run itself.

**Claim 4.** Best-known current agentic work practice treats fast bounded specialization as a checkpointed scout/probe discipline rather than as a naked winner claim.

**Practice source, local alignment, and adoption decision.** Contemporary agentic tool-use, adaptive workflow, and human-in-the-loop governance practice separates bounded exploration from committed rollout because a successful probe is not yet an admissible committed approach. In the working moment above, that is why the pair returns one `CheckpointReturn` with candidate approaches, evidence, burned and residual budget, and a commit trigger rather than only a winner label. This pattern **adopts** checkpointed scout/probe discipline, **adapts** it through the dyad-local roles and `CheckpointReturn`, and **rejects** the shortcut where an early probe silently becomes a committed rollout.
| Claim need | Source idea and current source | Current source reference | Local FPF invariant and practical local test | Adopted invariant, adapted invariant, and rejected shortcut |
| --- | --- | --- | --- | --- |
| Recipe, plan, case, decision, and executed occurrence must stay separable. | Case-management, decision-modeling, and service-change practice distinguish discretionary case work, decision logic, planned change support, and the realized service/product change. | OMG CMMN 1.1 (2016); OMG DMN 1.5 (2024); ITIL 4 Practitioner: Change Enablement (2023); source maturity = mature modeling standards plus current practitioner guidance. | The manufacturing, peer-review, and rollout slices keep `U.MethodDescription`, `U.WorkPlan`, approval work, and `U.Work` separate so a calendar or procedure never counts as the weld, review, deployment, or actual run. | **Adopt/Adapt.** Adopt the separation of case, decision, plan, and occurrence; adapt it to FPF's `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work`; reject an undifferentiated "process" object. |
| Architecture and digital-thread practice need traceable views without confusing description, authority, and occurrence. | Architecture-description and model-based systems practice treat descriptions, viewpoints, requirements, behavior, verification, and traceability as explicit review targets. | ISO/IEC/IEEE 42010:2022; OMG SysML v2.0 Language Specification (2025); source maturity = mature standard plus current technical specification. | `A.15` uses actor-in-context, role assignment, method description, and work occurrence so post-hoc review can ask whether the problem was assignment, capability, recipe, plan, approval, or run. | **Adopt/Adapt.** Adopt explicit trace and viewpoint discipline; adapt it to role, method, work-plan, and work-occurrence alignment; reject attributing work to a role label or document alone. |
| Approval and execution are distinct practical acts. | Change-enablement and decision-modeling practice separates risk assessment, authorization, scheduling, decision logic, and the work that realizes change. | ITIL 4 Practitioner: Change Enablement (2023); OMG DMN 1.5 (2024); source maturity = current practitioner guidance plus mature modeling standard. | In the release and gate examples, an approval or authorization changes authorization state; it is not the same work as deployment, welding, or other operational occurrence. | **Adopt.** Adopt the communicative/operational split and reject collapse of approval into the thing approved. |
| Fast bounded exploration must not become committed rollout by convenience. | Contemporary agentic tool-use and adaptive-work practice, including ReAct/Toolformer/Reflexion-style tool-use and self-correction lines, supports bounded probing while preserving explicit transition from option exploration to committed change. | Current agentic tool-use/self-correction practice; ITIL 4 Practitioner: Change Enablement (2023); ISO/IEC/IEEE 42010:2022; OMG SysML v2.0 Language Specification (2025); source maturity = current technical/practitioner guidance plus mature/current modeling standards. | The scout/probe moment returns candidate support, observed result, burned/residual budget posture, and a commit trigger rather than a selected method, `U.WorkPlan`, performed `U.Work`, or rollout authority. | **Adapt/Reject.** Adapt bounded scout/probe discipline to FPF role, method, work-plan, and work-occurrence splits; reject the shortcut where an early probe silently becomes a committed method choice, work plan, or rollout. |


For visible credential, provenance, dashboard, explanation, or composed-source cases that need exact project-side FPF kind and reference before work or reliance, use `A.15.4`. A.15 receives only the returned role, method, plan, and work part of the case.

The nearest recovery anchors are the manufacturing, peer-review, rollout briefing, `CC-A15-7`, `CC-A15-10`, `CC-A15-12`, and the boundary to `A.15.4`. If a SoTA row cannot be recovered through those local checks, do not let the source citation stand in for the local `A.15` rule.

