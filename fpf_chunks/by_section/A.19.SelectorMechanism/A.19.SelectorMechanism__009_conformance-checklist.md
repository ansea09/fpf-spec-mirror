---
chunk_kind: "child"
pattern_id: "A.19.SelectorMechanism"
pattern_title: "Unified Selection Kernel, SelectorMechanism"
section_id: "A.19.SelectorMechanism:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SelectorMechanism/A.19.SelectorMechanism__009_conformance-checklist.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "A.19.SelectorMechanism — Unified Selection Kernel, SelectorMechanism"
  - "A.19.SelectorMechanism:7 — Conformance Checklist"
line_start: 33372
line_end: 33395
dependencies:
keywords:
  - "SelectEligibility"
  - "selected set"
  - "selection kernel"
  - "set-returning selection"
  - "tri-state guard (pass"
---

### A.19.SelectorMechanism:7 - Conformance Checklist

| ID | Requirement |
|----|-------------|
| **CC-A19SelectorMechanism-0** | **Mechanism declaration completeness:** one `U.Mechanism` episteme, its exact selection-operation-family `EntityOfConcernRef`, its effective `U.ReferenceScheme`, the direct signature components, SlotSpecs, `OperationAlgebra`, `LawSet`, `AdmissibilityConditions`, and Applicability are recoverable under A.6.1. |
| **CC‑A19SelectorMechanism‑1** | **Single governing pattern:** the canonical SelectorMechanism `U.Mechanism.Intension` is governed by `A.19.SelectorMechanism:4.1`; other descriptions cite this section rather than restating the kernel law. |
| **CC‑A19SelectorMechanism‑2** | **Set‑return default:** a conformant `Select` MUST be set‑returning by default; it MUST NOT silently collapse partial orders or incomparabilities to a single winner. |
| **CC‑A19SelectorMechanism‑3** | **No hidden thresholds or constants:** a conformant SelectorMechanism publication MUST NOT smuggle thresholds, weights, dominance rules, tie‑breakers, or default `PortfolioMode` fields. Selection‑level commitments MUST be explicit in `CriteriaSlot` and explicit policy defaults when used (e.g., via `TaskSignatureSlot`). Acceptance thresholds remain governed by `AcceptanceClauses`, `TaskSignature`, or `GateProfile` records and MUST be applied only via `SelectEligibility`. |
| **CC‑A19SelectorMechanism‑4** | **No hidden scalarization:** if `ComparisonResultSlot` is set‑valued or partial, a conformant publication MUST consume it as such; scalar summaries are report‑only unless explicitly promoted by policy outside suite closure. |
| **CC-A19SelectorMechanism-5** | **Evidence gating:** `SelectEligibility` returns `pass`, `degrade`, or `abstain`; missing or unknown evidence never yields `pass`. Candidate exclusion or restricted use is explicit in current criteria or policy and recorded by dated selection work rather than hidden in the mechanism declaration. |
| **CC‑A19SelectorMechanism‑6** | **SlotKind discipline:** SlotKind tokens used in the SelectorMechanism intension MUST come from the CHR SlotKind lexicon (`A.19.CHR:4.2.1`). New SlotKinds require lexicon extension first. |
| **CC-A19SelectorMechanism-7** | **Bridge and reference-plane discipline:** cross-reference-scheme or cross-plane selection states an F.9 bridge with exact endpoints, preserved and lost meaning, applicable use, CL value, and any `R_eff` penalty. The bridge remains outside selector-declaration content. |
| **CC-A19SelectorMechanism-8** | **Replay basis completeness:** dated selection `U.Work`, the actual `Select` application, its candidate set, required binary comparisons, every exact upstream CPM application with pair, eligibility and own output binding or absence, token-to-producer trace, criteria and policy, `U.ClaimScope`, selected A.2.6 context slices, predicate basis, reference plane, evaluation window, derived token union, and `SelectionSlot` binding, plus direct evidence-use, provenance, and currentness relations, are recoverable. The outputs carry none of this metadata. |
| **CC-A19SelectorMechanism-9** | **Planned-filling separation:** `SlotFillingsPlanItem` rows carry planned editions and policy pins; dated selection `U.Work` remains the occurrence; the actual operation application carries effective argument and result bindings; and A.10 supplies evidence provenance when relied on. |
| **CC‑A19SelectorMechanism‑10** | **Specialisation-chain discipline:** any `⊑` or `⊑⁺` specialization of SelectorMechanism MUST satisfy `A.6.1:4.2.1`, especially SlotKind invariance and “no new mandatory inputs” to inherited `Select`. |
| **CC-A19SelectorMechanism-11** | **Guard and gate separation:** `SelectorMechanism` publishes neither `GateDecision` nor `DecisionLog`; `SelectEligibility` returns `pass`, `degrade`, or `abstain` separately from the selected set. |
| **CC-A19SelectorMechanism-12** | **Selection-condition completeness:** `CriteriaSlot`, effective selector policies and defaults, and any `degrade` failure behavior are explicit and bound by the actual application; acceptance and admission predicates remain separate. |
| **CC-A19SelectorMechanism-13** | **Selection-scope completeness:** every actual application binds candidate universe, finite exact binary CPM application basis, required comparison coverage, token-to-producer trace, `U.ClaimScope`, selected A.2.6 context slices, A.19 predicate basis, effective reference scheme and plane, and explicit evaluation point or interval. No generic context input, optional structure, batch result, or label supplies them. |
| **CC-A19SelectorMechanism-14** | **Output separation:** `SelectionSlot` contains only the by-value selected candidate set. On `abstain` no output is fabricated; a reduced set under `degrade` requires explicit current policy. |
| **CC-A19SelectorMechanism-15** | **Comparison continuity:** selection cites the finite exact basis of binary CPM applications and may not silently change its membership, required coverage, member pairs, eligibility or output bindings, predicate basis, scope, selected slices, plane, or window. A justified change is a new application and may require recomparison. |
| **CC-A19SelectorMechanism-16** | **No generic result relation:** the A.6.1 operation application binds `SelectionSlot`; C.2.1 governs a durable selected-set episteme when needed; direct subject patterns govern other result relations. |
| **CC-A19SelectorMechanism-17** | **Finite comparison-basis coverage:** selection conditions derive the required binary comparisons; each is discharged by an exact CPM application, and every consumed relation token traces to its producing member output. A missing pair, untraceable token, or required member that abstains forces selector abstention rather than a fabricated batch result. |
---

