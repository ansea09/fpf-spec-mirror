---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__001_intro.md"
commit_sha: "17edd955485f60cafb16159c7d90e20f4ad21844"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:intro — Intro"
line_start: 93457
line_end: 93472
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.19.SPR"
  - "A.2"
  - "A.2.1"
  - "A.2.7"
  - "A.22.CGUS"
  - "A.6.5"
  - "A.6.P"
  - "B.3"
  - "C.2.1"
  - "C.2.P"
  - "E.10"
  - "E.10.D2"
  - "E.10.MOVE"
  - "E.11"
  - "E.17"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
  - "G.11"
  - "U.BoundedContext"
keywords:
---

## F.17 - Unified Term Sheet
> **Type:** Lexical publication pattern (F)
> **Status:** Stable

Use this when a term decision is to become reader-facing, durable, public, Core-facing, or cross-context. Use it when a role name, status name, relation name, slot name, FPF kind name, local concept name, or bridgeable term set has outgrown one local repair and publication as one reviewed term row is current.

First useful move: identify the governed term decision, not the wording alone. Name the governed value and its kind, the effective `U.ReferenceScheme` carried by value, the exact local-sense coordinate, and the current direct pattern that owns the underlying value. When the row will compare local senses, compare their semantic-context projections: the `<ReferenceScheme, LocalSenseClaim>` pairs recovered from the exact cells. If those pairs differ, test an F.9 Bridge and, for a proposed row use, state the separate C.2.1 claim and its A.10 or B.3 reliance. A cross-scheme case is only the subset in which the `ReferenceScheme` values differ. Then publish only the term-row facts already governed there. A locality label or selected model-use structure enters only when it changes the naming use; neither is a mandatory sense coordinate.

Primary EntityOfConcern: one durable reader-facing term decision published by one `UnifiedTermRow` in one bounded unification thread. The role, status value, relation, slot kind, local concept, demonstrated row, or other underlying governed value remains the EntityOfConcern of its direct pattern; F.17 publishes its term decision and does not reconstitute that value.

What goes wrong if missed: a public term sheet becomes a global glossary, a row turns into an ontology claim, a block name becomes a subtype, or a familiar label smuggles role, status, evidence, publication, or source authority into reuse.

What this pattern buys: a compact reader-facing row that preserves the governed object, direct pattern, local senses, bridge, selected names, admissible use, blocked use, and currentness condition without redoing the whole unification argument.

Do not use this pattern for one sentence repair, one private glossary note, one local synonym choice, or one attempt to make an object real by putting it into a table. A short local mantra that only keeps one pattern's Solution in attention remains Plain pattern-local wording and needs no UTS row. Use `E.10`, `A.6.P`, `C.2.P`, `F.18`, or the direct domain pattern first when the kind, relation, slot position, admissible use, or name-card decision is still unsettled.

