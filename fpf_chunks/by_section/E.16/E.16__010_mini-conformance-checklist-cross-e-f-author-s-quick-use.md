---
chunk_kind: "child"
pattern_id: "E.16"
pattern_title: "RoC‑Autonomy Budget & Enforcement"
section_id: "E.16:9"
section_title: "Mini conformance checklist (cross‑E–F; author’s quick use)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.16/E.16__010_mini-conformance-checklist-cross-e-f-author-s-quick-use.md"
commit_sha: "44dd88188a07646ef23aca32627a3f670525853f"
heading_path:
  - "E.16 — RoC‑Autonomy Budget & Enforcement"
  - "E.16:9 — Mini conformance checklist (cross‑E–F; author’s quick use)"
line_start: 74115
line_end: 74124
dependencies:
  - "A.13"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.21"
  - "B.3"
  - "C.16"
  - "C.24"
  - "C.9"
  - "E.10"
  - "E.18"
  - "E.8"
  - "F.15"
  - "F.17"
  - "F.4"
  - "F.6"
  - "F.8"
  - "G.10"
  - "G.4"
  - "G.5"
  - "G.8"
  - "G.9"
keywords:
  - "autonomy budget"
  - "autonomy ledger"
  - "guarded enactment"
  - "override speech act"
  - "scout/probe/commit checkpoint"
---

### E.16:9 - Mini conformance checklist (cross‑E–F; author’s quick use)

1. **Declare** `AutonomyBudgetDecl` (scope, budgets, AdmissibilityConditionsId, overrides).
2. **Gate** steps with `requiresAutonomyBudget`.
3. **Emit** an `AutonomyLedgerEntry` for each admitted Work.
4. **Enforce SoD** on override SpeechActs; **block on depletion**.
5. **Publish** UTS autonomy fields for any autonomy‑bearing Role/Method/Service.

*(These five are sufficient for a working test harness in Part F.)*

