---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__001_intro.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:intro — Intro"
line_start: 77481
line_end: 77491
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.19.SPR"
  - "A.2"
  - "A.2.1"
  - "A.2.7"
  - "A.6.5"
  - "A.6.P"
  - "B.3"
  - "C.2.P"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "F.1"
  - "F.1-F.12"
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
  - "UTS"
  - "Unified Term Sheet"
  - "glossary"
  - "human-readable output"
  - "publication"
  - "summary table"
---

## F.17 - Unified Term Sheet
> **Status:** Stable

Status: stable pattern.

Use this when a term decision must become reader-facing, durable, public, Core-facing, or cross-context. Use it when a role name, status name, relation name, slot name, FPF kind name, local concept name, or bridgeable term set has outgrown one local repair and must be shown as one reviewed term row.

First useful move: identify the governed term decision, not the wording alone. Name the bounded context, the governed FPF kind or governed object kind, the local senses, the bridge claim if cross-context use is present, and the current direct pattern that owns the underlying object. Then publish only the term-row facts that are already governed there.

Do not use this pattern for one sentence repair, one private glossary note, one local synonym choice, or one attempt to make an object real by putting it into a table. Use `E.10`, `A.6.P`, `C.2.P`, `F.18`, or the direct domain pattern first when the kind, relation, slot position, admissible use, or name-card decision is still unsettled.

