---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local‑First Unification Naming Protocol"
section_id: "F.18:17"
section_title: "Migration notes (renames, splits, merges, retirements)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__018_migration-notes-renames-splits-merges-retirements.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "F.18 — Local‑First Unification Naming Protocol"
  - "F.18:17 — Migration notes (renames, splits, merges, retirements)"
line_start: 75608
line_end: 75619
dependencies:
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "C.2.P"
  - "E.10"
  - "F.0.1"
  - "F.1-F.17"
  - "G.10"
  - "G.2"
  - "G.6"
keywords:
---

### F.18:17 - Migration notes (renames, splits, merges, retirements)

**M1 — Start from Contexts, not from the old global word.** When inheriting legacy names, first **re‑harvest** terms inside the chosen Contexts (F.2–F.3). Only then decide whether to **reuse** or **mint** (F.8).

**M2 — Preserve reader muscle memory without duplicating meaning.** Keep the **Plain** label close to familiar speech, but make the **Tech** label precise. If a legacy term is overloaded, publish it as a **deprecated alias** in Annexes, not as a second Tech label. (F.13; Part H “Deprecated Aliases”.)

**M3 — Prefer split‑then‑bridge over vague merges.** If one legacy word covers two distinct concepts, **split** into two rows and add a short **relation note** between them (e.g., “recipe vs run”). Do **not** hide the split under a wide new name. (F.7; F.16.)

**M4 — Keep identifiers stable; move rows between blocks.** When the **Block Plan** evolves, move rows rather than renumbering; record the move in the row’s **Notes** field. (F.17 §16.)

**M5 — Upgrade rationale quality with worked examples.** Every rename or split should be accompanied by a **one‑page example** that shows the new row in action across at least **two Contexts**. (F.16; “tell‑show‑show”.)

