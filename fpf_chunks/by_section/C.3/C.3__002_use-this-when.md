---
chunk_kind: "child"
pattern_id: "C.3"
pattern_title: "Kinds, Intent and Extent, and Typed Reasoning"
section_id: "C.3:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3/C.3__002_use-this-when.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "C.3 — Kinds, Intent and Extent, and Typed Reasoning"
  - "C.3:0 — Use This When"
line_start: 43676
line_end: 43689
dependencies:
  - "A.1"
  - "A.11"
  - "A.2.6"
  - "A.22.CGUS"
  - "A.6.0"
  - "A.7.1"
  - "A.8"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.5"
  - "C.3.A"
  - "E.24.UK"
  - "F.18"
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

Use this pattern when a claim needs a context-local kind, a subkind order, a judgment about whether one exact candidate satisfies one local kind, or an optional representation of the candidates that satisfy it in one exact context slice.

**What goes wrong if missed.** A source type, local category, programming class, schema label, mathematical set, or public `U.*` name starts doing several jobs at once. The kind is confused with its declaration, evidence is treated as membership, an unavailable fact becomes false, a current extension becomes ontology, or claim scope is stored on the kind.

**What this buys.** Typed reasoning stays usable without premature ontology growth. A practitioner can recover the local kind, the declaration used to classify, one three-valued judgment, and any optional extension representation while leaving direct world-side features, evidence, scope, work, and durable U-kind admission with their own governors.

**Primary EntityOfConcern.** One typed-reasoning use under an effective `U.ReferenceScheme`: the exact local `U.Kind` and any `U.SubkindOf` order needed by the claim, together with the C.3.2 classification question that the use actually asks.

**First useful move.** Write the ordinary conclusion first. For example: `Pump #14 counts as a cooling pump in this plant slice because it satisfies the declared cooling-pump criterion.` Add a reusable declaration, explicit judgment details, evidence reference, or extension representation only when a named receiving use needs it.

**Not this pattern when.** Use `E.24.UK` when the question is durable public FPF U-kind admission. Use the direct subject pattern when the question is whether a physical quality, relation, construction, work occurrence, or other world-side feature obtains. Use `A.2.6` for claim, work, or publication scope and `C.29` for a claim-bearing mathematical representation.

