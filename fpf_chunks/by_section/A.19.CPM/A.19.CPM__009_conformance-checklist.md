---
chunk_kind: "child"
pattern_id: "A.19.CPM"
pattern_title: "Unified Comparison Mechanism (CPM)"
section_id: "A.19.CPM:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CPM/A.19.CPM__009_conformance-checklist.md"
commit_sha: "1eb56cd0cfd6dccad65143e03d28509373bd8dd5"
heading_path:
  - "A.19.CPM — Unified Comparison Mechanism (CPM)"
  - "A.19.CPM:7 — Conformance Checklist"
line_start: 32854
line_end: 32877
dependencies:
keywords:
  - "ComparatorSet"
  - "ComparatorSpecRef"
  - "comparator"
  - "comparison"
  - "partial order"
  - "set-valued comparison outcome"
  - "tri-state admissibility (pass"
---

### A.19.CPM:7 - Conformance Checklist

A CPM publication or use is conformant if it satisfies the checks below together with the A.6.1 mechanism conformance checklist and the CHR suite obligations in `A.19.CHR:4.3`:

| Check Id | Requirement (normative) | Notes (didactic and evidence) |
| :--- | :--- | :--- |
| **CC-A19CPM-0** | **Mechanism declaration completeness.** One `U.Mechanism` episteme, its exact comparison-operation-family `EntityOfConcernRef`, effective `U.ReferenceScheme`, direct signature components, SlotSpecs, `OperationAlgebra`, `LawSet`, `AdmissibilityConditions`, Applicability, and optional `SignatureManifest` are recoverable. | F.9 bridge, dated `U.Work`, actual operation application and result binding, any result episteme, A.10 evidence-provenance, G.11 currentness, and G.9 parity objects remain separate. |
| **CC‑A19CPM‑1** | **Single governing pattern.** The canonical CPM intension is governed here (`A.19.CPM:4.1`); other descriptions cite this section rather than restating the kernel law. | Prevents near-duplicate comparison semantics from drifting. |
| **CC‑A19CPM‑2** | **Suite stage alignment.** `Compare` is the canonical stage‑op for CHR stage `compare`; ordering and optionality are taken only from `A.19.CHR:4.5`. | Never infer order from `mechanisms[]`. |
| **CC‑A19CPM‑3** | **SlotKind discipline.** SlotKind tokens follow the suite lexicon (`A.19.CHR:4.2.1`). | No SlotKind drift across specializations and wiring. |
| **CC‑A19CPM‑4** | **Comparator admissibility gate.** `ComparatorSpecSlot ∈ CGSpecSlot.ComparatorSet` is enforced (fail-closed otherwise). | Admissibility is declared, not improvised. |
| **CC‑A19CPM‑5** | **Scale admissibility.** Any numeric operations implied by the comparator are admissible under `CGSpecSlot.SCP` and CSLC-admissible. | “Weighted sum” etc must be explicitly admissible. |
| **CC‑A19CPM‑6** | **Set‑valued semantics.** Outputs remain set‑valued; no silent scalarization or totalization is introduced. | Incomparability and ties are first‑class outcomes. |
| **CC‑A19CPM‑7** | **Tri‑state admissibility (fail‑closed).** `CompareEligibility(...) → {pass|degrade|abstain}` exists and does not return `pass` on missing admissibility and evidence. | Unknown never coerces to `pass`. |
| **CC‑A19CPM‑8** | **MinimalEvidence defaulting is explicit.** If `MinimalEvidenceSlot?` is absent, the effective evidence policy is `CGSpecSlot.MinimalEvidence` by explicit rule. | Avoid “implicit evidence policy.” |
| **CC‑A19CPM‑9** | **Gate and guard separation + lexeme discipline.** CPM does not publish `GateDecision` nor `DecisionLog`; mechanism predicates use `…Eligibility` (not reserved gate `…Guard`). | Aligns with suite obligations (`gate_decision_separation`, `guard_lexeme_reservations`). |
| **CC-A19CPM-10** | **Bridge and reference-plane discipline.** Cross-reference-scheme or cross-plane use states an F.9 bridge with exact endpoints, preserved and lost meaning, applicable use, CL value, and any `R_eff` penalty. | A bridge relation is not CPM declaration content. |
| **CC-A19CPM-11** | **Replay basis completeness.** Dated comparison `U.Work`, the actual `Compare` application, its profile, comparator, `U.ClaimScope`, selected A.2.6 context-slice, optional A.19 predicate, reference-plane, evaluation-window, policy, and `ComparisonResultSlot` bindings, plus direct evidence-use, provenance, and currentness relations, are recoverable. | The output value does not carry this metadata. |
| **CC-A19CPM-12** | **Planned-filling separation.** Editions and policy ids are planned fillings only in `SlotFillingsPlanItem` rows; the CPM declaration does not fill them, dated comparison `U.Work` remains the occurrence, and the actual operation application carries effective argument and result bindings. | Planned baseline = A.15.3 plus suite PlanItem; A.6.1 governs operation application; A.10 supplies evidence provenance when relied on. |
| **CC-A19CPM-13** | **No implicit UNM.** CPM never performs silent normalization; normalization-based comparability requires explicit upstream UNM refs or returns `abstain` or `degrade`. | Keeps compare-on-invariants explicit. |
| **CC-A19CPM-14** | **Comparison-scope completeness.** Every actual application binds one exact profile pair, `U.ClaimScope`, selected A.2.6 context slices, optional A.19 predicate, effective reference scheme and plane, and explicit evaluation point or interval. | No generic context input, optional model-use structure, or label supplies these values. |
| **CC-A19CPM-15** | **Outcome separation.** `ComparisonResultSlot` contains only the by-value set of relation or poset tokens; `GuardDecision` remains the separate eligibility value, and abstention fabricates no output token. | Comparator, scope, plane, window, evidence, provenance, currentness, result episteme, and selection remain separate. |
| **CC-A19CPM-16** | **No generic result relation.** The actual A.6.1 operation application binds the output; C.2.1 governs a durable result episteme when needed; direct subject patterns govern any other result relation. | CPM mints no universal comparison-result or work-result link. |

