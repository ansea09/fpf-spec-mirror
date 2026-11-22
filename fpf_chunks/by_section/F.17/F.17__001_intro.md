---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Make a Settled Naming Decision Recoverable for Reuse (Unified Term Sheet)"
section_id: "F.17:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__001_intro.md"
commit_sha: "4ee69807f8e5d4fa438e8c9b5de001d91275cc31"
heading_path:
  - "F.17 — Make a Settled Naming Decision Recoverable for Reuse (Unified Term Sheet)"
  - "F.17:intro — Intro"
line_start: 133119
line_end: 133136
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
  - "E.10.LRN"
  - "E.10.MOVE"
  - "E.11"
  - "E.17.0"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
---

## F.17 - Make a Settled Naming Decision Recoverable for Reuse (Unified Term Sheet)
> **Type:** Lexical row pattern (F)
> **Status:** Stable

**Use this when.** An independently governed value has a settled durable name and public, Core-facing, durable, or cross-local reuse needs a reader-facing term row.

**First useful move.** Ask what a later reader will need to cite. If the reader needs a settled name, identify the governed value, its kind, the pattern that defines or constrains it, the intended citation use, the Tech designation and any Plain designation needed there. Apply F.14 to decide whether the reader needs a row. An existing designation, alias or local expression can settle the request.

**Primary working object.** One C.2.1 `UnifiedTermRow` episteme whose exact EntityOfConcern is the independently governed value. Its claim graph cites the separate F.18 naming-settlement episteme and selected designation expressions. Section 5.1 explains the identities and relations needed to recover this decision and distinguish the row from its publication.

**What goes wrong if missed.** A table entry becomes an ontology claim; a stable identifier looks like identity evidence; one source title or file stands in for a local sense; a NameCard automatically creates a cell and row; or a row is mistaken for the publication occurrence that makes it available.

**What this buys.** A compact, durable navigation row through which readers can recover the naming decision and the rules that define or constrain the governed value without letting the row create, merge, prove, or publish that value.

**Not this pattern when.** Keep private wording, local synonyms or aliases, and names already supplied where the value is defined or constrained in their local use. Use F.14 before every naming object, F.8 for one unresolved mint-or-reuse choice, F.18 for the durable naming settlement, F.9 only for an actual relation between exact cells, and E.24.PUB only when a selected row edition must be made available.

For any stronger ontology, obtaining, equivalence, authority, system-role-kind, assignment, relation-position, status, evidence, Work, or subject-use claim, use the pattern that defines or constrains it.

