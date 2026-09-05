---
chunk_kind: "child"
pattern_id: "A.6.0"
pattern_title: "U.Signature - Reusable Law-Governed Declaration Episteme"
section_id: "A.6.0:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.0/A.6.0__002_problem-frame.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "A.6.0 — U.Signature - Reusable Law-Governed Declaration Episteme"
  - "A.6.0:1 — Problem frame"
line_start: 12620
line_end: 12641
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
  - "A.6.RCD"
  - "A.6.REL"
  - "A.7"
  - "C.16"
  - "C.2.1"
  - "C.22"
  - "C.29"
  - "C.3"
  - "E.10"
  - "E.18.1"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.19"
  - "F.9"
keywords:
---

### A.6.0:1 - Problem frame

An engineer has a vocabulary and a set of laws that need to remain stable across several dependent epistemes, such as model epistemes, method descriptions, and patterns. For example, a physical-modeling team needs one stable declaration of connector variables and conservation laws; a clinical team may need one stable definition of a dose-response predicate and its applicability without assuming that a dose-response relation kind has been admitted; and a formal-methods team needs one stable declaration of terms, inference forms, and invariants.

Use this pattern only when the thing being written or reused is itself a reusable declaration. A description, rule, policy, work plan, or specification does not qualify merely because it contains terms or constraints that recur elsewhere.

Before opening declaration fields, ask:

> What subject does this declaration cover? What values or results does it speak about? Which terms and laws may another use rely on? Where do those laws apply?

In FPF terms, the declaration is about one exact independently governed `EntityOfConcern`; `SubjectKind` and `RangedValueKind` name its declared subject and value range; `ResultKind` is added when a distinct result kind is current; and `Vocabulary`, `Laws`, and `Applicability` answer the remaining three questions. `U.Signature` is the episteme that carries this declaration. A relation kind opens the `RelationSignature` specialization; a mechanism family or formal calculus opens the corresponding A.6.1 or FormalSubstrate declaration; a method kind remains governed by A.3.1.

**Primary working reader and concern.** The reader is an engineer who authors or reuses a declaration and needs stable meaning, applicability, and typed reuse without authoring declaration or occurrence-identity apparatus beyond what the current use needs.

For the lightest useful declaration, name that subject through `SubjectKind` and `RangedValueKind`, add `ResultKind` when the result has another kind, and state `Vocabulary`, `Laws`, and `Applicability`. Add `SliceSet` and `ExtentRule` only when the same declared kind can have different members at different `U.ContextSlice` values and one named reuse needs that difference. Add A.6.5 SlotSpecs that declare the direct relation's participant meanings only inside a reusable `RelationSignature`; add operation argument and result declarations under A.6.1 when a mechanism declaration needs them. Add dependency declarations only when another signature relies on provided names or laws.

What goes wrong if this pattern is missed: content about later realization, evaluation, and publication accumulates inside the declaration. A later user cannot tell which names and laws are reusable, where they apply, or whether a changed implementation has changed the declaration.

What this buys: one identifiable declaration can be reused while later realizations and uses change under their own subject patterns.

Do not use this pattern merely to state that a direct relation obtains or that one work occurrence produced a result. State that claim directly. A maintenance work plan may reuse the words `connector` and `conservation law` while scheduling tasks; it remains a work plan unless its own claim content performs the reusable declaration job above. Construct a signature only when reusable declaration content is the current object.

