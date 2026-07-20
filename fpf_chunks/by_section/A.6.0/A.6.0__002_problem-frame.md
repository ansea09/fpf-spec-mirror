---
chunk_kind: "child"
pattern_id: "A.6.0"
pattern_title: "U.Signature - Reusable Law-Governed Declaration Episteme"
section_id: "A.6.0:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.0/A.6.0__002_problem-frame.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "A.6.0 — U.Signature - Reusable Law-Governed Declaration Episteme"
  - "A.6.0:1 — Problem frame"
line_start: 10900
line_end: 10919
dependencies:
  - "A.15.1"
  - "A.17"
  - "A.18"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.19.UNM"
  - "A.2.6"
  - "A.3.1"
  - "A.6.0"
  - "A.6.1"
  - "A.6.5"
  - "A.6.REL"
  - "A.7"
  - "C.16"
  - "C.2.1"
  - "C.22"
  - "C.29"
  - "C.3"
  - "E.18.1"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.9"
keywords:
---

### A.6.0:1 - Problem frame

An engineer has a vocabulary and a set of laws that need to remain stable across several dependent epistemes, such as model epistemes, method descriptions, and patterns. For example, a physical-modeling team needs one stable declaration of connector variables and conservation laws; a clinical team needs one stable declaration of a dose-response relation and its applicability; a formal-methods team needs one stable declaration of terms, inference forms, and invariants.

Use this pattern when the working question is:

> What reusable declaration episteme identifies its subject, states the vocabulary entries and specialized typed declarations available for reuse, states the declared laws, and bounds where those claims apply?

The primary `EntityOfConcern` of this pattern is the `U.Signature` episteme. Its declaration identifies one exact `EntityOfConcern`, whose kind remains governed independently. A relation kind opens the `RelationSignature` specialization; a mechanism family or formal calculus opens the corresponding A.6.1 or FormalSubstrate declaration; a method kind remains governed by A.3.1.

**Primary working reader and concern.** The reader is an engineer who authors or reuses a declaration and needs stable meaning, applicability, and typed reuse without authoring declaration or occurrence-identity apparatus beyond what the current use needs.

For the lightest useful declaration, name that subject through `SubjectKind` and `RangedValueKind`, add `ResultKind` when the result has another kind, and state `Vocabulary`, `Laws`, and `Applicability`. Add `SliceSet` and `ExtentRule` only when a receiving use depends on varying extension. Add A.6.5 SlotSpecs that declare the direct relation's participant meanings only inside a reusable `RelationSignature`; add operation argument and result declarations under A.6.1 when a mechanism declaration needs them. Add dependency declarations only when another signature relies on provided names or laws.

What goes wrong if this pattern is missed: content about later realization, evaluation, and publication accumulates inside the declaration. A later user cannot tell which names and laws are reusable, where they apply, or whether a changed implementation has changed the declaration.

What this buys: one identifiable declaration can be reused while later realizations and uses change under their own governing patterns.

Do not use this pattern merely to state that a direct relation obtains or that one work occurrence produced a result. State that claim directly. Construct a signature only when reusable declaration content is the current object.

