---
chunk_kind: "child"
pattern_id: "F.13"
pattern_title: "Lexical Continuity & Deprecation"
section_id: "F.13:6"
section_title: "Solution — Continuity, not “registries”"
source_path: "FPF-Spec.md"
output_path: "by_section/F.13/F.13__007_solution-continuity-not-registries.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "F.13 — Lexical Continuity & Deprecation"
  - "F.13:6 — Solution — Continuity, not “registries”"
line_start: 106773
line_end: 106800
dependencies:
  - "F.1"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "deprecation"
  - "historical reading"
  - "lexical continuity"
  - "local aliases"
  - "renaming labels"
  - "retirement"
  - "splitting and merging labels"
---

### F.13:6 - Solution — Continuity, not “registries”

Use the least-committing continuity relation that tells the truth after recovering the subject's identity or change under its own rule.

#### F.13:6.1 - Continuity relations (normative meanings)

1. **`renames(label_old → label_new)`** — wording changes while meaning and use remain unchanged.
   *Use when:* The effective scheme, local-sense claim and intended use remain the same, and the independently governed value remains the same when one is being named. For an external row or description label, recover its target under F.7, F.4 or F.17 as applicable.
   *Effect:* The legacy label becomes a local read-path to the preferred one. If `LocalExpression` changes, retain both exact F.17 cells; if a NameCard or row ClaimGraph changes, retain the earlier episteme and the corresponding later one. The rename itself proves none of those identities.

2. **`aliases(label_legacy ↔ label_pref)`** — a legacy synonym is kept for reading.
   *Use when:* The two exact label uses have the same scheme, local-sense claim, intended use and, where applicable, governed value.
   *Effect:* Keep a two-way read-path; writing uses `label_pref`. Keep at most one legacy alias per register. Distinct expressions need not be the same SchemeSenseCell.

3. **`splits(label_old ⇒ {label_A, label_B})`** — one earlier label covered several senses or rows that are now distinguished.
   *Use when:* F.3 recovers the distinct local senses, or F.7 establishes the required row refactor.
   *Effect:* Deprecate the old label for new writing and retain a disambiguating read-path. Neither new label is asserted to continue the whole earlier meaning.

4. **`merges({label_A, label_B} ⇒ label_new)`** — several labels are consolidated for one recovered naming use.
   *Use when:* The local label uses have the same scheme, local-sense claim and use, with the same governed value where applicable; or two F.7 rows are duplicate displays of the same named comparison or use, exact entries, independently established relations, losses, basis and receiving-use conclusion.
   *Effect:* Keep the old labels' epoch-qualified read-paths subject to the alias budget. This label or display consolidation does not merge source-local cells, named values or Bridge occurrences.

5. **`retires(label_old)`** — a name is withdrawn without one successor.
   *Use when:* The label misleads and no single successor preserves its earlier use.
   *Effect:* Keep a warning for historical reading and point to the relevant meanings or rows. A known single successor for an unchanged meaning belongs to rename, not retirement.

**Meaning-change boundary.** These five label relations do not exhaust changes to the things being named. For a one-to-one changed criterion, recover the revision or replacement under the subject's rule, preserve the exact earlier claim, and settle the later name under F.18. If the governing continuity decision is unavailable, state that missing decision instead of inventing a split or merge. A needed relation between different semantic projections is a separate F.9 question.

