---
chunk_kind: "child"
pattern_id: "A.19.CPM"
pattern_title: "Compare Admitted Profiles under a Declared Comparator (CPM)"
section_id: "A.19.CPM:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CPM/A.19.CPM__009_conformance-checklist.md"
commit_sha: "7bba05916e6e8ad42f868ed3aad0a7644fe0c354"
heading_path:
  - "A.19.CPM — Compare Admitted Profiles under a Declared Comparator (CPM)"
  - "A.19.CPM:7 — Conformance Checklist"
line_start: 36291
line_end: 36314
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

Apply the declaration checks to a CPM publication and the application checks to an actual use, together with the applicable A.6.1 checks and, for CHR membership, `A.19.CHR:4.3`. Replay always requires the actual application and its local bindings. Neighboring Work, evidence-use, reliance, currentness and result-episteme checks apply only when the account asserts those objects or the receiving use consumes them:

| Check Id | Requirement (normative) | Notes (didactic and evidence) |
| :--- | :--- | :--- |
| **CC-A19CPM-0** | **Mechanism declaration completeness.** One `U.Mechanism` episteme, its exact comparison-operation-family `EntityOfConcernRef`, effective `U.ReferenceScheme`, operation-local argument/result declarations, `OperationAlgebra`, `LawSet`, `AdmissibilityConditions`, Applicability, and optional `SignatureManifest` are recoverable. | An obtaining F.9 `Bridge`, its separate C.2.1 bounded-use claim when consumed, any applicable ReferencePlane relation and policy, dated `U.Work`, actual operation application and result binding, any result episteme, A.10 evidence-provenance, G.11 currentness, and G.9 parity objects remain separate. |
| **CC‑A19CPM‑1** | **Single governing pattern.** The canonical CPM intension is governed here (`A.19.CPM:4.1`); other descriptions cite this section rather than restating the kernel law. | Prevents near-duplicate comparison semantics from drifting. |
| **CC‑A19CPM‑2** | **Suite stage alignment.** `Compare` is the canonical stage‑op for CHR stage `compare`; ordering and optionality are taken only from `A.19.CHR:4.5`. | Never infer order from `mechanisms[]`. |
| **CC‑A19CPM‑3** | **SlotKind discipline.** SlotKind tokens follow the suite lexicon (`A.19.CHR:4.2.1`). | No SlotKind drift across specializations and wiring. |
| **CC‑A19CPM‑4** | **Comparator admissibility gate.** `ComparatorSpecSlot ∈ CGSpecSlot.ComparatorSet` is enforced (fail-closed otherwise). | Admissibility is declared, not improvised. |
| **CC‑A19CPM‑5** | **Scale admissibility.** Any numeric operations implied by the comparator are admissible under `CGSpecSlot.SCP` and CSLC-admissible. | “Weighted sum” etc must be explicitly admissible. |
| **CC‑A19CPM‑6** | **Set‑valued semantics.** Outputs remain set‑valued; no silent scalarization or totalization is introduced. | Incomparability and ties are first‑class outcomes. |
| **CC‑A19CPM‑7** | **Tri‑state admissibility (fail‑closed).** `CompareEligibility(...) → {pass|degrade|abstain}` exists and does not return `pass` on missing admissibility and evidence. | Unknown never coerces to `pass`. |
| **CC‑A19CPM‑8** | **MinimalEvidence defaulting is explicit.** If `MinimalEvidenceSlot?` is absent, the effective evidence policy is `CGSpecSlot.MinimalEvidence` by explicit rule. | Avoid “implicit evidence policy.” |
| **CC‑A19CPM‑9** | **Gate and guard separation + lexeme discipline.** CPM does not publish `GateDecision` nor `DecisionLog`; mechanism predicates use `…Eligibility` (not reserved gate `…Guard`). | Aligns with suite obligations (`gate_decision_separation`, `guard_lexeme_reservations`). |
| **CC-A19CPM-10** | **Bridge and reference-plane discipline.** A comparison that relies on a semantic relation between two exact F.17 `SchemeSenseCell` values cites an obtaining F.9 `Bridge` under a satisfied `BridgePredicateProfile` and a separate C.2.1 bounded-use claim; a plane-only crossing cites the applicable ReferencePlane relation and policy; both are stated when both facts are current. | `CL` is optional. CPM supplies no default assurance penalty, fold, or `R_eff`; a local `R_eff` is admissible only for an actual named assurance claim under its declared domain model and calculation. These neighboring facts are not CPM declaration content. |
| **CC-A19CPM-11** | **Replay basis completeness.** The actual `Compare` application and its profile, comparator, `U.ClaimScope`, selected A.2.6 context-slice, optional A.19 predicate, reference-scheme and plane, evaluation-window, policy, eligibility and returned `ComparisonResultSlot` bindings (or explicit absence) are recoverable. | If asserted or consumed, independently recover dated comparison Work under A.15.1, evidence use under A.2.4, reliance and provenance under A.10, currentness under G.11 and a result episteme under C.2.1. These facts remain outside the output value. |
| **CC-A19CPM-12** | **Planned-filling separation.** An A.15.2 baseline selects intended editions and policies; A.15.3 typed filling applies only to independently declared positions. Actual Compare applications carry their effective argument and result bindings. | A dated comparison Work and any relied-on A.10 provenance remain separately established. |
| **CC-A19CPM-13** | **No implicit UNM.** CPM uses the explicit upstream directed result and preservation/loss basis. A class-level comparison also passes its query/operation conditions under A.19.UNM; a reference or equal normalized numeral alone is insufficient. Unsupported comparisons follow `abstain` or the declared narrower `degrade` use. | Keeps compare-on-invariants explicit. |
| **CC-A19CPM-14** | **Comparison-scope completeness.** Every actual application binds one exact profile pair, `U.ClaimScope`, selected A.2.6 context slices, optional A.19 predicate, effective reference scheme and plane, and explicit evaluation point or interval. | No generic context input, optional model-use structure, or label supplies these values. |
| **CC-A19CPM-15** | **Outcome separation.** `ComparisonResultSlot` contains only the by-value set of relation or poset tokens; `GuardDecision` remains the separate eligibility value, and abstention fabricates no output token. | Comparator, scope, plane, window, evidence, provenance, currentness, result episteme, and selection remain separate. |
| **CC-A19CPM-16** | **No generic result relation.** The actual A.6.1 operation application binds the output; C.2.1 governs a durable result episteme when needed; direct subject patterns govern any other result relation. | CPM mints no universal comparison-result or work-result link. |

