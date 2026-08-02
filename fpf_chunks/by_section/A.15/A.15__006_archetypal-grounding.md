---
chunk_kind: "child"
pattern_id: "A.15"
pattern_title: "Role–Method–Work Alignment"
section_id: "A.15:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15/A.15__006_archetypal-grounding.md"
commit_sha: "9a9a42e4d154021ca3f7415e0009a4214832f65f"
heading_path:
  - "A.15 — Role–Method–Work Alignment"
  - "A.15:5 — Archetypal Grounding"
line_start: 24140
line_end: 24182
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

### A.15:5 - Archetypal Grounding

The role-method-work alignment applies whenever the question under repair is holder-in-role, method description, intended plan, or performed work. Physical engineering, knowledge work, and socio-technical cases can all use the same distinction without turning A.15 into a universal process ontology.

| Archetype | **`U.System` Archetype (Manufacturing)** | **`U.Episteme` Archetype (Scientific Peer Review)** |
| :--- | :--- | :--- |
| **Role-taxonomy episteme** | `FactoryProductionRoles-2026` | `PhysicsPeerReviewRoles-2026` |
| **Effective `U.ReferenceScheme`** | `Factory-Line-B-Role-Scheme` | `PhysicsLetters-A-Review-Scheme` |
| **`U.Role`** | `WeldingRobotRole` | `PeerReviewerRole` |
| **Holder** | `ABB_Robot_Model_IRB_6700` (`U.System`) | `Dr_Alice_Smith` (modeled as a `U.System`) |
| **`U.RoleAssignment`** | exact four participants: the robot holder, `WeldingRobotRole`, `FactoryProductionRoles-2026`, and `Factory-Line-B-Role-Scheme`; actual extent is derived from uninterrupted obtaining | exact four participants: Alice as holder, `PeerReviewerRole`, `PhysicsPeerReviewRoles-2026`, and `PhysicsLetters-A-Review-Scheme`; actual extent is derived from uninterrupted obtaining |
| **`U.MethodDescription`** | `Welding_Procedure_WP-28A.pdf` describes `WeldingMethod` | `Peer_Review_Guidelines_v3.docx` describes `PeerReviewMethod` |
| **`U.Capability` instance of holder** | `executeWeldingSeam(Type: 3F)` within declared envelope, measures, and currentness condition | `evaluateManuscript(Field: QuantumOptics)` within declared envelope, measures, and currentness condition |
| **Receiving interpretation use, only if current** | designates the selected factory model-use structure separately from the generic assignment | designates the selected journal review model-use structure separately from the generic assignment |
| **Work occurrence admitted under `U.Work`** | Manufacturing work: `Weld_Job_#78345` is one Work individual; its exact temporal relation covers 15:32-15:34 UTC, separately obtaining resource-use relations connect it to 1.2 kWh and 5g Argon, and exact `enactsMethod` connects it to `WeldingMethod`. A separate assertion may cite `methodDescriptionRef = Welding_Procedure_WP-28A.pdf`. | Peer-review work: `Review_of_Manuscript_#PL-2025-018` is one Work individual; its exact temporal relation ends on 2025-08-15, a separately obtaining resource-use relation connects it to four hours of reviewer time, and exact `enactsMethod` connects it to `PeerReviewMethod`. A separate assertion may cite `methodDescriptionRef = Peer_Review_Guidelines_v3.docx`. |

**Key takeaway from grounding:**
The welding and peer-review cases share one enactment alignment without sharing a domain ontology. Each has a holder `U.System`, a role interpreted by an exact role-taxonomy episteme and effective reference scheme, a four-participant `U.RoleAssignment`, a run-independent `U.Method`, a separate `U.MethodDescription`, a holder capability when reliance on it is current, and a dated Work occurrence admitted under `U.Work`. A selected model-use structure appears only in the receiving interpretation use that needs it. This is enough to compare the alignment while preserving different local structures; any classification beyond `U.Work` remains with its direct owner.

#### A.15:5.1.a - Briefing guides orientation, not execution

**Source set.** A release team has one deployment method description, one current work plan, one approval or decision record when required, and the evidence records and evidence relations used to decide whether the rollout may proceed. A short rollout briefing is prepared for the daily stand-up.

**Briefing slice.** `Status briefing only: rollback procedure appears verified in the current source bundle. Execution remains tied to the deployment method, work plan, required approval or decision record, and evidence relation.`

This briefing may orient the team and cue attention. If the team wants to execute from the briefing alone, use `A.15.4` or the evidence, gate, decision, or assurance pattern governing the claim to recover the missing project-side kind and reference. Inside `A.15`, keep only the role, method, plan, and work-occurrence separation.

#### A.15:5.1.b - P2W principle-scheme publication guides planning, not occurrence

**Source set.** A team has a principle scheme that shows an `E.18.1` P2W carry-through structure for a fabrication task: signature or principle episteme, method-family selection, selected method, `U.WorkPlan`, an actual Work occurrence admitted under `U.Work`, a separate work-result record, and result measurement.

**Published slice.** `For this batch family, method M-2 is selected from the declared method family; prepare work plan WP-17 before any actual Work occurrence exists.`

This publication may guide method inspection and work-planning preparation under `A.15`. A conforming use keeps selected method, `U.WorkPlan`, actual dated Work occurrence, separate assertion or record about it, work-result record, and result measurement distinct. If the publication is used for evidence, provenance, engineering justification, gate or constraint decision, physical medium, screen, export, OCR behavior, or publication-use, apply the governing pattern for that claim being made. If no project-side kind and reference named by value exists, create only an `A.15.4` repair request, decision-request record for the next decision, prospective work-plan entry, or explicit missing-source-relation note.

#### A.15:5.1.c - Scenario guides method selection, not performed work

**Source set.** A method-selection scenario says that material X is below threshold T, resource window W is available, and the fabrication cell is under setup condition S. The scenario is admitted source material, or an episteme publication exposing that source material, for choosing between method families.

**Published slice.** `Under scenario S, method family MF-2 is admissible for planning; choose the selected method and prepare the work plan before execution.`

The scenario can guide method-family selection and work-planning preparation. Once the team selects a method or prepares a plan, state that project choice or plan through its governed episteme. If an actual Work occurrence is later claimed, ground that world-side individual independently under `A.15.1`; a separately governed assertion or performed-work record may designate it but does not become the occurrence. If the scenario is used for evidence, gate, or engineering-justification reliance, first recover the project evidence relation, gate or constraint decision, or engineering-justification record named by value under `A.10`, `A.20`, `A.21`, or `B.3`; otherwise record only an `A.15.4` repair request, decision-request record, prospective work-plan entry, or missing-source-relation note.

