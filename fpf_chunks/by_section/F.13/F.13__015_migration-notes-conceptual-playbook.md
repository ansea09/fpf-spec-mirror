---
chunk_kind: "child"
pattern_id: "F.13"
pattern_title: "Lexical Continuity & Deprecation"
section_id: "F.13:14"
section_title: "Migration notes (conceptual playbook)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.13/F.13__015_migration-notes-conceptual-playbook.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "F.13 — Lexical Continuity & Deprecation"
  - "F.13:14 — Migration notes (conceptual playbook)"
line_start: 95430
line_end: 95440
dependencies:
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "deprecation"
  - "evolution"
  - "merging terms"
  - "renaming"
  - "splitting terms"
---

### F.13:14 - Migration notes (conceptual playbook)

1. **Ask the same‑sense question first.** If the underlying **SenseCell/row** is unchanged, prefer `renames`; else reach for `splits/merges`.
2. **Keep it inside the Context.** If your explanation crosses Contexts, stop—this is **Bridge** territory (F.9), not a rename.
3. **Prefer clarity over fashion.** Rename only when the new label **removes a real ambiguity** (F.5 criteria), not to chase style.
4. **Limit nostalgia.** Admit **one** legacy alias in each register that readers will most likely meet; leave the rest to footnotes in examples.
5. **Deprecate with kindness.** When retiring a label, add a one‑line **pointer note** (e.g., “see `timer event` in BPMN; ‘heartbeat’ in KD‑CAL means sensor liveness”).
6. **Rows before names.** If a rename request coincides with a shift in what the row covers, **refactor rows** (F.7) first, then choose labels.
7. **Edition bumps.** When a canon updates, check labels used in that Context: if definitions shift, it’s a **split/merge**; if not, you may `renames` for style/uniformity.
8. **Teach the delta.** In primers, show a **mini table** with legacy → preferred pairs only where readers will encounter both.

