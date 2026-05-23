---
chunk_kind: "child"
pattern_id: "A.15"
pattern_title: "Role–Method–Work Alignment (Contextual Enactment)"
section_id: "A.15:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15/A.15__006_archetypal-grounding.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.15 — Role–Method–Work Alignment (Contextual Enactment)"
  - "A.15:5 — Archetypal Grounding"
line_start: 19700
line_end: 19740
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

### A.15:5 - Archetypal Grounding

The Contextual Action Framework is universal. It applies identically to the modeling of physical engineering processes, knowledge work, and socio-technical systems.

| Archetype | **`U.System` Archetype (Manufacturing)** | **`U.Episteme` Archetype (Scientific Peer Review)** |
| :--- | :--- | :--- |
| **`BoundedContext`** | `FactoryFloor:ProductionLine_B` | `Journal:PhysicsLetters_A` |
| **`Role`** | `WeldingRobotRole` | `ReviewerRole` |
| **`Holder`** | `ABB_Robot_Model_IRB_6700` (`U.System`) | `Dr_Alice_Smith` (modeled as a `U.System`) |
| **`U.RoleAssignment`** | `ABB_Robot#WeldingRobotRole:Line_B` | `Dr_Smith#ReviewerRole:PhysicsLetters_A` |
| **`MethodDescription` (`U.Episteme`)** | `Welding_Procedure_WP-28A.pdf` (SOP) | `Peer_Review_Guidelines_v3.docx` |
| **`Capability` (Attribute of Holder)** | `executeWeldingSeam(Type: 3F)` | `evaluateManuscript(Field: QuantumOptics)` |
| **`Work` (`Occurrence`)** | Manufacturing Work: `Weld_Job_#78345` (15:32-15:34 UTC, consumed 1.2 kWh, 5g Argon) - **isExecutionOf** `Welding_Procedure_WP-28A.pdf` | Peer-review Work: `Review_of_Manuscript_#PL-2025-018` (Completed 2025-08-15, took 4 hours) - **isExecutionOf** `Peer_Review_Guidelines_v3.docx` |

**Key takeaway from grounding:**
This side-by-side comparison reveals the power of the framework. A seemingly different activity like welding a car chassis and reviewing a scientific paper are shown to have the **exact same underlying causal structure**. Both involve a `Holder` (a system) acting in a `Role` within a `Context`, using a `Capability` described by a `MethodDescription` to produce a specific, auditable instance of `Work`. This universality is what allows FPF to compare and align disparate domains without collapsing their local structure.

#### A.15:5.1.a - Briefing is not execution authority
**Source set.** A release team has one governing deployment method description, one current work plan, one approval work item, and the evidence carriers and evidence paths used to decide whether the rollout may proceed. A short rollout briefing is prepared for the daily stand-up.

**Briefing slice.** `Status briefing only: rollback path appears verified in the current source bundle. Deployment authority remains with the governing approval record and work plan.`

This briefing may orient the team and cue attention, but it is not the governing execution authority by itself. Work can proceed admissibly only when the underlying method description, current work plan, required approval records, and evidence carriers and evidence paths stay explicit and reopenable. If the team wants to treat the briefing as sufficient to execute, the case leaves simple orientation and must reopen the governing method, plan, approval, or evidence source rather than treating the shortened note as the work-enactment authority.

#### A.15:5.1.b - P2W principle-scheme publication supports planning, not occurrence

**Source set.** A team has a principle scheme that shows the P2W principles-to-work transduction chain for a fabrication task: signature or principle episteme, method-family selection, selected method, `U.WorkPlan`, performed `U.Work`, work-result record, and result measurement.

**Published slice.** `For this batch family, method M-2 is selected from the declared method family; prepare work plan WP-17 before any run is recorded.`

This publication may support method inspection and work-planning preparation under `A.15`. It does not say that the work already occurred, that the batch may pass a gate, that evidence is sufficient, or that engineering justification is complete. A conforming use keeps the selected method, `U.WorkPlan`, actual `U.Work`, work-result record, and result measurement distinct. Evidence or provenance use requires a project evidence path governed by `A.10`; engineering-justification use requires an engineering-justification record governed by `B.3`; gate use requires the project gate or constraint decision governed by `A.20` or `A.21`; carrier, screen, export, or OCR behavior requires the carrier or front-end record governed by `A.7`; publication and readability questions stay with `E.17` and the relevant `A.6.3.*` relation.

#### A.15:5.1.c - Scenario supports method selection, not performed work

**Source set.** A method-selection scenario says that material X is below threshold T, resource window W is available, and the fabrication cell is in setup state S. The scenario is the source episteme or source publication for choosing between method families.

**Published slice.** `Under scenario S, method family MF-2 is admissible for planning; choose the selected method and prepare the work plan before execution.`

The scenario can support method-family selection and work-planning preparation. It is not the selected method by itself, not a `U.WorkPlan`, not performed `U.Work`, and not evidence that the work result was achieved. Once the team selects a method or prepares a plan, record that project choice or plan as the exact `A.15` selected method, work-plan, or work-occurrence record; if the scenario is being used as evidence, gate passage, or engineering justification, first recover the existing project evidence path, gate or constraint decision, or engineering-justification record governed by `A.10`, `A.20`, `A.21`, or `B.3`. If no existing exact project-side FPF kind and reference carries the needed load-bearing claim, create only a prospective repair request, future decision request, prospective work-plan entry, or explicit source-gap note; do not backdate evidence, approval, gate passage, performed `U.Work`, release permission, engineering justification, or assurance for the earlier scenario-based claim.


