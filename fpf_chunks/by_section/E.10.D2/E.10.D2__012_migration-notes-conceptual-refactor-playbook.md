---
chunk_kind: "child"
pattern_id: "E.10.D2"
pattern_title: "Intension–Description–Specification Discipline (I/D/S)"
section_id: "E.10.D2:11"
section_title: "Migration notes (conceptual refactor playbook)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D2/E.10.D2__012_migration-notes-conceptual-refactor-playbook.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "E.10.D2 — Intension–Description–Specification Discipline (I/D/S)"
  - "E.10.D2:11 — Migration notes (conceptual refactor playbook)"
line_start: 53935
line_end: 53947
dependencies:
  - "A.7"
  - "C.2.1"
  - "C.2.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.10"
  - "F.15"
  - "F.4"
  - "F.5"
  - "F.8"
  - "F.9"
  - "U.BoundedContext"
  - "U.EpistemeSlotGraph"
keywords:
  - "I/D/S"
  - "description"
  - "intension"
  - "specification"
  - "testable"
  - "verifiable"
---

### E.10.D2:11 - Migration notes (conceptual refactor playbook)

> Goal: remove conflations and normalise names without changing underlying models.

1. **Rename by default.** Any `XSpec` lacking a bound acceptance harness becomes **`XDescription`**. Keep content intact; change suffix and preface with a “Description, not Spec” note.
2. **Promote selectively.** For epistemes that *are* testable and declare **F ≥ F4**, add harness links (F.15) and re-label as **`XSpec`** via the Spec-gate.
3. **Fix the verbs.** Rewrite “Role contains RSG/RCS” → “Role is **characterised by** RSG/RCS in RoleDescription”.
4. **Detach carriers.** Replace identity‑by‑file with **`U.Carrier` encodes …Description/Spec** wording.
5. **Add Contexts.** Where a Description drifts globally (“the backlog refinement is…”), prefix with the Context and adjust wording to be **local**.
6. **Split planes.** Move any Evidence/Requirement **statuses** out of role state lists; keep them as roles over **knowledge units**.
7. **Window‑ise verdicts.** Ensure every evaluation statement adds an explicit **window** (instant or interval).
8. **Document maturity.** **Declare each Description’s F** (C.2.3) and track **ΔF** promotions/demotions as part of change notes (no governance implied).

