---
chunk_kind: "child"
pattern_id: "E.10.MOVE"
pattern_title: "Move and Readiness Wording Precision Restoration"
section_id: "E.10.MOVE:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.MOVE/E.10.MOVE__001_intro.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "E.10.MOVE — Move and Readiness Wording Precision Restoration"
  - "E.10.MOVE:intro — Intro"
line_start: 76861
line_end: 76876
dependencies:
  - "A.1.STM"
  - "A.10"
  - "A.15"
  - "A.15.2"
  - "A.15.5"
  - "A.16.0"
  - "A.21"
  - "A.22.CGUS"
  - "A.3.3"
  - "A.3.4"
  - "A.3.4.P"
  - "B.4"
  - "C.11"
  - "C.17"
  - "C.19"
  - "C.22.2"
  - "C.24"
  - "C.27.TA"
  - "C.29"
  - "C.30"
  - "C.36"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.DEV"
  - "E.11.PUA"
  - "E.11.PUR"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.23"
  - "E.24"
  - "F.17"
  - "F.18"
  - "F.19"
  - "G.11"
keywords:
---

## E.10.MOVE - Move and Readiness Wording Precision Restoration

> **Type:** Part E precision-restoration pattern
> **Status:** Stable
> **Normativity:** Normative for move-like, movement-like, readiness-like, route-like, path-like, and trajectory-like wording-use restoration.

**At a glance.** `E.10.MOVE` restores the exact FPF value or relation hidden by move-like, movement-like, readiness-like, route-like, path-like, or trajectory-like wording. Its branches cover demonstrated continuation, prediction, readiness, and trajectory use. Recover the subject, posture, ordering, and representation needed to reach the direct owner; the pattern admits no generic Move or Trajectory head.

**Use this when.** After the normal `F.19` reading and compact `E.10` routing, use this pattern only while move-like, movement-like, readiness-like, route-like, path-like, or trajectory-like wording still hides the governed claim—for example, a demonstrated continuation, a prediction, readiness for a named Work, or an actual, planned, or modelled trajectory.

**Primary EntityOfConcern.** One wording-use restoration over a bounded text span whose move-like, movement-like, readiness-like, route-like, path-like, or trajectory-like wording has an FPF-governed use.

**First output.** Repaired wording, a truthful split, or a blocker. When later replay relies on the repair, use a temporary `MoveAndReadinessWordingRepairNote` that names the governed span, claim, object under repair, wording-use disposition, subject pattern, exact governed value and kind, relation signature when applicable, repaired wording or blocker, and remaining admissible reader use. A grounded non-use boundary is optional under `F.19`; it is not a required repair field.

**Not this pattern when.** Use `A.3.4.P` first when the wording is primarily about a transformation or change situation. Use `E.10.DEV` first when *development* or *evolution* still hides the changed subject, continuity or membership, or direction or value claim; continue here only if an independent trajectory, route, ordering, posture, or representation ambiguity remains. Use `F.19` and the direct subject pattern immediately when the current object is already known. Generic *process*, *workflow*, *loop*, or *flow* wording stays outside unless it independently carries one of the governed move, readiness, route, path, or trajectory claims.

