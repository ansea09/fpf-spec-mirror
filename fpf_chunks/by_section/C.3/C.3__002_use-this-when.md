---
chunk_kind: "child"
pattern_id: "C.3"
pattern_title: "Kinds, Intent and Extent, and Typed Reasoning"
section_id: "C.3:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3/C.3__002_use-this-when.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "C.3 — Kinds, Intent and Extent, and Typed Reasoning"
  - "C.3:0 — Use This When"
line_start: 38445
line_end: 38461
dependencies:
  - "A.1"
  - "A.11"
  - "A.2.6"
  - "A.8"
  - "C.2.3"
  - "C.3.1"
  - "C.3.5"
  - "C.3.A"
  - "E.24.UK"
  - "F.5"
  - "F.8"
keywords:
  - "classification"
  - "extension"
  - "intension"
  - "kind"
  - "subkind"
  - "type"
  - "typed reasoning"
  - "vocabulary"
---

### C.3:0 - Use This When

Use this pattern when a claim needs to say what kind of thing it quantifies over, which instances belong to that kind in a context slice, how intent and extent are related, and how typed compatibility affects composition.

Typical moments:

- two claims may be about different kinds of entities;
- scope is being widened by abstract wording instead of supported slices;
- a local kind needs membership, extension, bridge, or subkind reasoning;
- a `U.Kind` or `U.SubkindOf` occurrence must be kept distinct from durable FPF U-kind admission.

**Primary EntityOfConcern.** The EntityOfConcern is the typed reasoning claim: kind, intent, extent, membership, and typed compatibility in a bounded context.

**First useful move.** Ask whether the current question is C.3 typed reasoning or U-kind admission. If it is U-kind admission, use `E.24.UK`. If it is claim quantification, stay in C.3.

When a source ontology, schema, standard, class hierarchy, or top-level ontology supplies type, class, category, or subtype wording, C.3 may govern the local typed-reasoning claim. Use `E.24.UK` only when the source construct is being proposed as a public durable FPF U-kind or as part of an E.24 ontic settlement.

