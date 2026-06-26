---
chunk_kind: "child"
pattern_id: "A.19.SelectorMechanism"
pattern_title: "Unified Selection Kernel, SelectorMechanism"
section_id: "A.19.SelectorMechanism:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SelectorMechanism/A.19.SelectorMechanism__014_relations.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "A.19.SelectorMechanism — Unified Selection Kernel, SelectorMechanism"
  - "A.19.SelectorMechanism:12 — Relations"
line_start: 29422
line_end: 29443
dependencies:
keywords:
  - "SelectEligibility"
  - "selected set"
  - "selection kernel"
  - "set-returning selection"
  - "tri-state guard (pass"
---

### A.19.SelectorMechanism:12 - Relations

* **Builds on**

  * `A.6.1` and `CC‑UM.*` for the mechanism intension shape and specialisation-chain discipline.
  * `A.19.CHR` for suite membership, suite protocol closure, SlotKind lexicon, and threshold and default discipline.
  * `G.0` for `CG‑Spec` admissibility and evidence declarations.
  * `A.19.CN` for `CN‑Spec` governance card used as an explicit input.
  * `C.22` for `TaskSignature` as a policy-reference artifact when used.
  * `A.6.5` for slot discipline (SlotIndex as projection; SlotKind invariance).
  * `A.15.3` + `A.19.CHR:4.7.2` for the planned slot-filling ontic and `SlotFillingsPlanItem` rows carrying edition and policy pins (cited as planned slot fillings, not duplicated in Intension).
* **Used by**

  * `A.19.CHR` as the canonical `select` stage in CHR pipelines.
  * `G.5` as the primary conformance and specialization context for selector-based method dispatch and `PortfolioMode` policies.
  * `E.18` when selector instances are used as transformation-flow structure nodes; planned pins are planned fillers in `SlotFillingsPlanItem` rows, and effective pins appear in `Audit`.
* **Coordinates with**

  * `CPM` and other admissible comparison stages as producers of `ComparisonResultSlot`.
  * `ULSAM` and other admissible aggregation stages that must remain explicit rather than hidden inside selection.
  * `E.20` governing-pattern discipline and `F.18` naming or alias handling when a source term needs a bridge.

