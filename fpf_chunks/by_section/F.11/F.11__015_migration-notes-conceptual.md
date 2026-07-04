---
chunk_kind: "child"
pattern_id: "F.11"
pattern_title: "Method Quartet Harmonisation"
section_id: "F.11:14"
section_title: "Migration notes (conceptual)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.11/F.11__015_migration-notes-conceptual.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "F.11 — Method Quartet Harmonisation"
  - "F.11:14 — Migration notes (conceptual)"
line_start: 84845
line_end: 84853
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.3"
  - "A.3.1"
  - "A.3.2"
  - "D.CTX"
  - "E.10.D1"
  - "F.1"
  - "F.10"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.9"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Work"
keywords:
  - "Actuation"
  - "Method"
  - "MethodDescription"
  - "Role–Method–Work alignment"
  - "Work"
---

### F.11:14 - Migration notes (conceptual)

1. **Split conflated “process”.** Where a single “process” node stands for both plan and run, refactor into **MethodDescription** (design) and **Work** (run); add a Bridge if the prose relied on identity.
2. **Reassign statuses.** Move any *Approval*-like statuses from Work to MethodDescription; move *Satisfied/Violated* from Spec to clauses about Work within **Windows**.
3. **Expose actuation.** If control outputs are buried in “execution logs,” mint **Actuation** SenseCells and relate them **within** Work.
4. **Version fences.** Past Works keep references to the **version** of MethodDescription they attempted to follow; don’t update those links retroactively.
5. **Name collisions.** Where *task/activity/process* appear with mixed meanings, prefix with Contexts and relabel per **F.5** (Tech/Plain).
6. **Backfill Bridges.** If earlier text implied Cross‑context equivalence, add explicit Bridges (F.7/F.9) declaring **kind/CL/Loss**.

