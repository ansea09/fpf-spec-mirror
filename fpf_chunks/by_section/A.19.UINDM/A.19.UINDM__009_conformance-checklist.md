---
chunk_kind: "child"
pattern_id: "A.19.UINDM"
pattern_title: "Indicatorization (UINDM): Select Indicators Under a Declared Policy"
section_id: "A.19.UINDM:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UINDM/A.19.UINDM__009_conformance-checklist.md"
commit_sha: "7bba05916e6e8ad42f868ed3aad0a7644fe0c354"
heading_path:
  - "A.19.UINDM — Indicatorization (UINDM): Select Indicators Under a Declared Policy"
  - "A.19.UINDM:7 — Conformance Checklist"
line_start: 35297
line_end: 35322
dependencies:
keywords:
  - "CHR suite stage indicatorize"
  - "CN-Spec.indicator_policy"
  - "IndicatorChoicePolicy"
  - "indicator set"
  - "indicatorization"
  - "tri-state admissibility (pass"
---

### A.19.UINDM:7 - Conformance Checklist

A UINDM publication or use is conformant if it satisfies:

1. **A.6.1 declaration completeness.** Indicatorize and the separately reused IndicatorizeEligibility have local argument/result declarations, obtaining predicates and application identity/extent rules. Their declared selection and guard laws hold; SlotIndex projects those declarations. An actual binding requires the value used or returned by the identified application, not a compatible audit record.

2. **SlotKind discipline.** SlotKind tokens match the CHR SlotKind lexicon for the roles used (`CharacteristicSpaceSlot`, `CNSpecSlot`, `IndicatorChoicePolicySlot`, etc.); no generic `ContextSlot` is introduced. New SlotKinds, if any, first extend the suite lexicon rather than appearing ad hoc in the mechanism.

3. **Selection-only behavior.** `Indicatorize` returns positions in the exact declared basis, retaining their Characteristic, Scale and meaning. A projected state keeps their original relative order. There is no implicit normalization or enlargement. After a basis change, resolve the policy again rather than reuse naked indices.

4. **No NCV shortcut.** “Measurable/NCV” is not treated as sufficient for indicatorhood; indicatorhood arises only via `IndicatorChoicePolicySlot` consistent with `CN‑Spec.indicator_policy`.

5. **Evidence gating is explicit.** When the chosen `IndicatorChoicePolicy` is evidence‑gated, `CGSpecSlot` is present and the effective MinimalEvidence is explicit and auditable
   (`MinimalEvidenceSlot` when provided; otherwise `CGSpecSlot.MinimalEvidence`); insufficient/unknown evidence must yield `degrade/abstain` per the effective failure‑behavior policy, never a silent `pass`.

6. **Reuse is explicit.** Another bearer, scope and window, basis, plane, or intended use gets a fresh eligibility decision; any F.9 Bridge, kind relation, or plane relation is cited only when the conclusion relies on that obtaining relation, with supported loss routed to `R_eff`.

7. **Gate/guard separation + lexeme discipline.** UINDM uses `…Eligibility` returning `GuardDecision ∈ {pass|degrade|abstain}` and does not embed GateDecision/GateLog in suite steps.
   Reserved gate‑lexemes (e.g., `…Guard`) are not used for mechanism‑level predicates; the mechanism stays at the guard/admissibility layer.

8. **Planning and actual use.** An A.15.2 WorkPlan selects the intended editions; A.15.3 governs typed filling only for independently declared positions. Record the actual application and its effective bindings under §4.1, keeping the refs and pins needed for replay in Audit.

9. **Extension discipline (if extended).** A proposed UINDM specialization MUST preserve the inherited SlotKind designators and their meanings, add no mandatory input to Indicatorize, and declare any additional output or operation explicitly (the local extension notation is ⊑⁺). A refinement, conservative-extension or equivalence claim additionally uses its own A.6.1 §4.8 preservation test and exact comparison predicate; those three claims are not interchangeable. Preserve inherited application/binding meanings, identity and extent to the degree required by the claimed comparison, and retain narrowed applicability or stronger conditions explicitly. A missing comparison predicate or substrate returns the applicable A.6.RCD gap.

For example, an extended Indicatorize may add an optional justification result while retaining the original inputs and selected-position result. To claim a conservative extension, establish that every inherited admitted use, result and application/binding rule remains as specified; the new output has its own declaration. Making a new explanation input mandatory fails the local restriction. A label such as ⊑⁺ does not settle the comparison: use the admitted comparison relation or A.6.RCD's case-specific claim branch under A.6.1 §4.8, returning its exact missing-governor/substrate gap if necessary.

