---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local-First Unification Naming Protocol"
section_id: "F.18:1"
section_title: "Context"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__003_context.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "F.18 — Local-First Unification Naming Protocol"
  - "F.18:1 — Context"
line_start: 81686
line_end: 81719
dependencies:
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "A.6.RSIR"
  - "C.2.P"
  - "E.10"
  - "F.0.1"
  - "F.1"
  - "F.1-F.17"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.8"
  - "F.9"
  - "G.10"
  - "G.2"
  - "G.6"
keywords:
---

### F.18:1 - Context

Names are handles for use, not creators of ontology. A good name lets people talk about a governed value without smuggling in extra role, capability, method, work, status, evidence, interface, or cross-context claims.

`F.18` supplies the naming discipline for Part F and for any FPF pattern that needs a durable public term. It coordinates with:

- `F.5` for type-name and role-description label form;
- `F.8` for mint-or-reuse decisions;
- `F.9` for cross-context bridges;
- `F.13` for renames, aliases, splits, and merges;
- `F.14` for anti-explosion control;
- `F.17` for public term-row publication;
- `A.6.5` and `A.6.RSIR` when relation, signature, interface, slot, or role wording hides the governed object.

The central EntityOfConcern is the naming relation around a governed value:

```text
NameCard:
  NameCardId
  GovernedValueRef
  GoverningPatternRef
  BoundedContextRef
  LocalSenseRef
  TechLabel
  PlainLabel
  CandidateSetRef
  SelectionRationale
  BridgeRefs?
  UnifiedTermRowRef?
  LineageEntries
```

The `NameCard` describes and governs the name. It does not create the governed value. A `UnifiedTermRow` publishes the selected name for public, Core-facing, durable, or cross-context use; it also does not create the governed value.

