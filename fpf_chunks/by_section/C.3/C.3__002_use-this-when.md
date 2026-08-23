---
chunk_kind: "child"
pattern_id: "C.3"
pattern_title: "Kinds, Intent and Extent, and Typed Reasoning"
section_id: "C.3:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3/C.3__002_use-this-when.md"
commit_sha: "7f7c592f4d633e54cdb202d622d6e0e05df41517"
heading_path:
  - "C.3 — Kinds, Intent and Extent, and Typed Reasoning"
  - "C.3:0 — Use This When"
line_start: 43409
line_end: 43422
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
  - "KindSignature"
  - "SubkindOf preorder"
  - "admissibility"
  - "admitted U.Kind individual"
  - "distinct-kind KindBridge"
  - "membership distinction"
  - "optional extension"
  - "true/false/unknown judgment"
---

### C.3:0 - Use This When

Use this pattern when a claim needs a reusable kind, a subkind comparison, a judgment about whether one exact candidate satisfies one kind, or an optional representation of the candidates that satisfy it in one exact context slice. A kind may be used locally without receiving its own public `U.*` name; “local” describes the bounded use, not an identity component.

**What goes wrong if missed.** A source type, practice label, programming class, schema label, mathematical set, or public `U.*` name starts doing several jobs at once. A source boundary splits one unchanged kind; several kinds inside one source collapse; the kind is confused with its declaration; evidence is treated as membership; a non-applicable request becomes `unknown`; or a current extension becomes ontology.

**What this buys.** A practitioner can recover the kind's membership distinction, the declaration used to classify, an admissibility result, one three-valued judgment when admissible, and any optional extension representation while leaving source provenance, direct world-side conditions, evidence, scope, Work, and public naming with their own patterns.

**Primary EntityOfConcern.** One typed-reasoning question: the exact `U.Kind` individual, its intended candidate domain and membership distinction, any `U.SubkindOf` comparison needed by the claim, and the C.3.2 candidate question the use actually asks. The exact `KindSignature` edition carries the effective `U.ReferenceScheme` in its claim content; the scheme and practice/source provenance are not stored on the kind.

**First useful move.** Write the ordinary conclusion first. For example: `Pump #14 counts as a cooling pump in this plant slice because it satisfies the declared cooling-pump condition.` Add a reusable declaration, admissibility detail, explicit judgment, support reference, or extension representation only when a named receiving use needs it.

**Not this pattern when.** Use `E.24.UK` when the question is admission of another durable public FPF U-kind. Use the direct subject pattern when the question is whether a physical quality, relation, registration, certification, publication occurrence, Work, or other governed condition obtains. Use `A.2.6` for claim, work, or publication scope and `C.29` for a claim-bearing mathematical representation.

