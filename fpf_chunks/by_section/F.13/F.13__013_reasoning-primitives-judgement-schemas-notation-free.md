---
chunk_kind: "child"
pattern_id: "F.13"
pattern_title: "Lexical Continuity & Deprecation"
section_id: "F.13:12"
section_title: "Reasoning primitives (judgement schemas, notation‑free)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.13/F.13__013_reasoning-primitives-judgement-schemas-notation-free.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "F.13 — Lexical Continuity & Deprecation"
  - "F.13:12 — Reasoning primitives (judgement schemas, notation‑free)"
line_start: 106911
line_end: 106956
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

### F.13:12 - Reasoning primitives (judgement schemas, notation‑free)

> Each judgement is a **pure thought**: premises ⇒ safe conclusion. No storage, no workflow, no roles.

Let `meaningOf(ℓ)` recover the exact `<ReferenceScheme, LocalSenseClaim>` projection for one local label use; let `useOf(ℓ)` recover its intended naming use. Where a value is being named, recover it independently under its subject rule. `pref(t)` denotes the preferred expression for that exact naming use, not a global preferred word.

#### F.13:12.1 - Same‑sense & same‑place

Two expressions with the same `meaningOf`, intended use and independently governed value where applicable may receive a rename. A changed `LocalExpression` still changes the exact F.17 cell. An external label change preserves a cell only when the target coordinate itself is unchanged.

#### F.13:12.2 -Local alias

Under the same conditions, a legacy expression may remain a read-path to `pref(t)`. Retain its own exact coordinate and any source basis; aliasing is not cell identity.

#### F.13:12.3 - Split detection

If one label covered several independently recovered local senses or rows, record the split and prefer the precise later labels. Keep the earlier use resolvable through a disambiguation note.

#### F.13:12.4 - Merge admission

Consolidate local labels only after recovering their common semantic projection and use, with the same governed value where applicable. Consolidate comparison-row labels only after establishing duplicate F.7 comparison content. Neither move merges distinct cell coordinates or subject entities.

#### F.13:12.5 - Retirement

Retire a misleading label when no single successor preserves its earlier use. Point historical readers to the relevant meanings or rows.

#### F.13:12.6 - Cross‑context guard

Different `meaningOf` projections do not support a pure rename or alias. A needed semantic correspondence goes to F.9; relation obtaining, a bounded-use claim and reliance are separate questions.

#### F.13:12.7 - Writing discipline

Use the current preferred expression for the exact naming use. Keep aliases for historical reading.

#### F.13:12.8 - Reading resolution

Resolve a legacy label to its earlier meaning and use first, then to any justified present-name read-path. Include an epoch when it changes interpretation. A successor's changed meaning must not replace the old one retroactively.

#### F.13:12.9 - Alias budget

Keep at most one useful legacy alias per register for one naming use.

#### F.13:12.10 - Row‑level continuity

A Concept-Set display label may change while the exact comparison content and receiving use remain unchanged. Recover changed row content under F.7 first. When an F.17 UnifiedTermRow's identity-bearing claims change, retain the earlier and corresponding later epistemes under C.2.1/F.17; a stable row designator is not identity proof.

