---
chunk_kind: "child"
pattern_id: "A.19.SelectorMechanism"
pattern_title: "Unified Selection Kernel, SelectorMechanism"
section_id: "A.19.SelectorMechanism:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SelectorMechanism/A.19.SelectorMechanism__014_relations.md"
commit_sha: "7bba05916e6e8ad42f868ed3aad0a7644fe0c354"
heading_path:
  - "A.19.SelectorMechanism — Unified Selection Kernel, SelectorMechanism"
  - "A.19.SelectorMechanism:12 — Relations"
line_start: 36826
line_end: 36852
dependencies:
  - "A.19.CHR"
  - "A.19.CN"
  - "A.19.ULSAM"
  - "A.19.USCM"
  - "A.6.1"
  - "A.6.5"
  - "C.22"
  - "E.18"
  - "G.0"
  - "G.5"
keywords:
  - "ComparisonResultSlot"
  - "SelectEligibility"
  - "SelectorMechanism"
  - "explicit criteria"
  - "finite basis of binary CPM applications"
  - "pass/degrade/abstain"
  - "required comparison coverage"
  - "selected candidate set"
  - "selection kernel"
---

### A.19.SelectorMechanism:12 - Relations

* **Builds on**

  * `A.6.1` and its conformance checklist for mechanism identity, declaration content, applicability, and specialisation-chain discipline.
  * `A.19.CHR` for suite membership, suite protocol closure, SlotKind lexicon, and threshold and default discipline.
  * `G.0` for `CG‑Spec` admissibility and evidence declarations.
  * `A.19` for the exact `CharacteristicSpacePredicate` basis when one governs selection.
  * `A.19.CPM` for every exact binary `Compare` application in the finite basis, its pair, realized eligibility value, and own set-valued output binding.
  * `A.2.6` for `U.ClaimScope` identity and exact `U.ContextSlice` membership.
  * `A.19.CN` for `CN-Spec` governance card used as an explicit input.
  * `C.22` for `TaskSignature` as a policy-reference artifact when used.
  * `A.6.1 §4.2` for operation-local argument/result meanings and their SlotIndex projection; the local extension rule preserves inherited meanings.
  * `A.15.2` for the edition/policy baseline; `A.15.3` plus `A.19.CHR:4.7.2` for typed filling of independently declared positions.
  * `C.27.TA` for the explicit selection-evaluation point or interval.
  * `A.2.4`, `A.10`, and `G.11` for evidence-use scope, provenance, and currentness, separately from selection scope and output.
* **Used by**

  * `A.19.CHR` as the canonical `select` stage in CHR pipelines.
  * `G.5` as the primary conformance and specialization context for selector-based method dispatch and `PortfolioMode` policies.
  * `E.18` when this declaration is used by transformation-flow nodes. A.15.3 governs planned refs only for independently declared receiving positions; actual operation bindings and any dated selection Work retain their direct rules.
* **Coordinates with**

  * `CPM` and other admissible comparison stages as producers of the exact result bindings whose justified-token union fills the Selector's `ComparisonResultSlot` argument.
  * `ULSAM` and other admissible aggregation stages that must remain explicit rather than hidden inside selection.
  * `E.20` governing-pattern discipline and `F.18` naming or alias handling when a source term needs a bridge.

