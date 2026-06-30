---
chunk_kind: "child"
pattern_id: "A.15"
pattern_title: "Role–Method–Work Alignment (Contextual Enactment)"
section_id: "A.15:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15/A.15__006_archetypal-grounding.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "A.15 — Role–Method–Work Alignment (Contextual Enactment)"
  - "A.15:5 — Archetypal Grounding"
line_start: 21452
line_end: 21492
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
  - "contextual enactment"
  - "coordinated-work evidence"
  - "role-method-work distinction"
  - "source-restoration boundary"
  - "work admission display"
  - "work-entry readiness"
---

### A.15:5 - Archetypal Grounding

The role-method-work alignment applies whenever the question under repair is holder-in-role, method description, intended plan, or performed work. Physical engineering, knowledge work, and socio-technical cases can all use the same distinction without turning A.15 into a universal process ontology.

| Archetype | **`U.System` Archetype (Manufacturing)** | **`U.Episteme` Archetype (Scientific Peer Review)** |
| :--- | :--- | :--- |
| **`BoundedContext`** | `FactoryFloor:ProductionLine_B` | `Journal:PhysicsLetters_A` |
| **`Role`** | `WeldingRobotRole` | `PeerReviewRole` |
| **`Holder`** | `ABB_Robot_Model_IRB_6700` (`U.System`) | `Dr_Alice_Smith` (modeled as a `U.System`) |
| **`U.RoleAssignment`** | assignment with holder slot `ABB_Robot_Model_IRB_6700`, role slot `WeldingRobotRole`, context slot `Line_B`, and current-window slots and source-reference slots when they matter | assignment with holder slot `Dr_Alice_Smith`, role slot `PeerReviewRole`, context slot `PhysicsLetters_A`, and current-window slots and source-reference slots when they matter |
| **`MethodDescription` (`U.Episteme`)** | `Welding_Procedure_WP-28A.pdf` (SOP) | `Peer_Review_Guidelines_v3.docx` |
| **`Capability` (Attribute of Holder)** | `executeWeldingSeam(Type: 3F)` | `evaluateManuscript(Field: QuantumOptics)` |
| **`Work` (`Occurrence`)** | Manufacturing Work: `Weld_Job_#78345` (15:32-15:34 UTC, consumed 1.2 kWh, 5g Argon) - **enactsMethod** `WeldingMethod`, with `methodDescriptionRef = Welding_Procedure_WP-28A.pdf` | Peer-review Work: `Review_of_Manuscript_#PL-2025-018` (Completed 2025-08-15, took 4 hours) - **enactsMethod** `PeerReviewMethod`, with `methodDescriptionRef = Peer_Review_Guidelines_v3.docx` |

**Key takeaway from grounding:**
This side-by-side comparison reveals the power of the framework. A seemingly different activity like welding a car chassis and reviewing a scientific paper are shown to have the same underlying enactment structure. Both involve a `Holder` (a system) acting in a `Role` within a `Context`, using a `Capability` to enact a `U.Method`, citing a `MethodDescription` when a recipe or source is used to identify or constrain the method, and producing a specific, auditable instance of `Work`. This universality is what allows FPF to compare and align disparate domains without collapsing their local structure.

#### A.15:5.1.a - Briefing guides orientation, not execution

**Source set.** A release team has one deployment method description, one current work plan, one approval or decision record when required, and the evidence records and evidence relations used to decide whether the rollout may proceed. A short rollout briefing is prepared for the daily stand-up.

**Briefing slice.** `Status briefing only: rollback procedure appears verified in the current source bundle. Execution remains tied to the deployment method, work plan, required approval or decision record, and evidence relation.`

This briefing may orient the team and cue attention. If the team wants to execute from the briefing alone, use `A.15.4` or the evidence, gate, decision, or assurance pattern governing the claim to recover the missing project-side kind and reference. Inside `A.15`, keep only the role, method, plan, and work-occurrence separation.

#### A.15:5.1.b - P2W principle-scheme publication guides planning, not occurrence

**Source set.** A team has a principle scheme that shows an `E.18.1` P2W carry-through structure for a fabrication task: signature or principle episteme, method-family selection, selected method, `U.WorkPlan`, performed `U.Work`, work-result record, and result measurement.

**Published slice.** `For this batch family, method M-2 is selected from the declared method family; prepare work plan WP-17 before any run is recorded.`

This publication may guide method inspection and work-planning preparation under `A.15`. A conforming use keeps selected method, `U.WorkPlan`, actual `U.Work`, work-result record, and result measurement distinct. If the publication is used for evidence, provenance, engineering justification, gate or constraint decision, material carrier, screen, export, OCR behavior, or publication-use, apply the governing pattern for that claim being made. If no project-side kind and reference named by value exists, create only a source-restoration request, decision-request record for the next decision, prospective work-plan entry, or explicit source-gap note.

#### A.15:5.1.c - Scenario guides method selection, not performed work

**Source set.** A method-selection scenario says that material X is below threshold T, resource window W is available, and the fabrication cell is under setup condition S. The scenario is the source episteme or source publication for choosing between method families.

**Published slice.** `Under scenario S, method family MF-2 is admissible for planning; choose the selected method and prepare the work plan before execution.`

The scenario can guide method-family selection and work-planning preparation. Once the team selects a method or prepares a plan, record that project choice or plan as the selected `A.15` selected-method, work-plan, or work-occurrence record named by value. If the scenario is used for evidence, gate, or engineering-justification reliance, first recover the project evidence relation, gate or constraint decision, or engineering-justification record named by value under `A.10`, `A.20`, `A.21`, or `B.3`; otherwise record only a source-restoration request, decision-request record, prospective work-plan entry, or source-gap note.

