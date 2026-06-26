---
chunk_kind: "child"
pattern_id: "E.10.MOVE"
pattern_title: "Move and Readiness Wording Precision Restoration"
section_id: "E.10.MOVE:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.MOVE/E.10.MOVE__001_intro.md"
commit_sha: "f1d0f9319cf1f93129b7691a328a281022252c4e"
heading_path:
  - "E.10.MOVE — Move and Readiness Wording Precision Restoration"
  - "E.10.MOVE:intro — Intro"
line_start: 68205
line_end: 68220
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.3"
  - "A.15.4"
  - "A.15.5"
  - "A.16"
  - "A.16.0"
  - "A.21"
  - "A.3.4.P"
  - "B.1.6"
  - "C.24"
  - "C.30"
  - "C.30.AD"
  - "E.10"
  - "E.10.ARCH"
  - "E.11.PUR"
  - "E.17"
  - "E.18.1"
  - "E.24"
  - "G.6"
keywords:
---

## E.10.MOVE - Move and Readiness Wording Precision Restoration

> **Type:** Part E precision-restoration pattern
> **Status:** Stable
> **Normativity:** Normative for move-like and readiness-like wording-use restoration.

**At a glance.** `E.10.MOVE` restores the FPF object hidden by wording such as move, step, action, application, solution, next action, work item, work entry, full kit, readiness, TameFlow `MOVE`, route, workflow, and process when that wording is about project concern, pattern-use recommendation, work-entry readiness, or another direct governing pattern.

**Use this when.** Use this pattern when move-like or readiness-like wording helps recognition but starts to hide whether the current value is pattern use, P2W carry-through, WorkPlan, SlotFillingsPlanItem, WorkEntryReadiness, GateDecision, performed Work, transformation, method, publication, source use, language-state move, call plan, or architecture candidate material.

**Primary EntityOfConcern.** One wording-use restoration over a bounded text span whose move-like or readiness-like wording has an FPF-governed use.

**First output.** One `MoveAndReadinessWordingRepair` note naming the project concern, source-use class, recovered relation or value, direct governing pattern, retained plain wording, blocked overread, split if needed, final wording or blocker, and remaining reader use.

**Not this pattern when.** Use `A.3.4.P` first when the wording is primarily about transformation, flow, path, process, workflow, operation, or change as a change-situation label. Use the direct governing pattern immediately when the current object is already known and no move-like or readiness-like wording problem remains.

