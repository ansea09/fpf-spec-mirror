---
chunk_kind: "child"
pattern_id: "C.3"
pattern_title: "Kinds, Intent and Extent, and Typed Reasoning"
section_id: "C.3:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3/C.3__002_use-this-when.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "C.3 — Kinds, Intent and Extent, and Typed Reasoning"
  - "C.3:0 — Use This When"
line_start: 44636
line_end: 44649
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
  - "C.3.2"
  - "C.3.3"
  - "C.3.5"
  - "C.3.A"
  - "E.24.UK"
  - "F.18"
  - "F.8"
  - "F.9"
keywords:
  - "KindBridge"
  - "SubkindOf"
  - "bounded-context local kind"
  - "effective ReferenceScheme"
  - "intent-bearing KindSignature"
  - "optional slice-indexed extension"
  - "three-valued candidate judgment"
---

### C.3:0 - Use This When

Use this pattern when a claim needs a context-local kind, a subkind order, a judgment about whether one exact candidate satisfies one local kind, or an optional representation of the candidates that satisfy it in one exact context slice.

**What goes wrong if missed.** A source type, local category, programming class, schema label, mathematical set, or public `U.*` name starts doing several jobs at once. The kind is confused with its declaration, evidence is treated as membership, an unavailable fact becomes false, a current extension becomes ontology, or claim scope is stored on the kind.

**What this buys.** Typed reasoning stays usable without premature ontology growth. A practitioner can recover the local kind, the declaration used to classify, one three-valued judgment, and any optional extension representation while leaving direct world-side features, evidence, scope, work, and durable U-kind admission with their own governors.

**Primary EntityOfConcern.** One typed-reasoning question: the exact context-local `U.Kind`, any `U.SubkindOf` order needed by the claim, and the C.3.2 classification question the use actually asks. The exact `KindSignature` edition used for that question carries the effective `U.ReferenceScheme` in its claim content; the scheme is not stored on the kind.

**First useful move.** Write the ordinary conclusion first. For example: `Pump #14 counts as a cooling pump in this plant slice because it satisfies the declared cooling-pump criterion.` Add a reusable declaration, explicit judgment details, evidence reference, or extension representation only when a named receiving use needs it.

**Not this pattern when.** Use `E.24.UK` when the question is durable public FPF U-kind admission. Use the direct subject pattern when the question is whether a physical quality, relation, construction, work occurrence, or other world-side feature obtains. Use `A.2.6` for claim, work, or publication scope and `C.29` for a claim-bearing mathematical representation.

