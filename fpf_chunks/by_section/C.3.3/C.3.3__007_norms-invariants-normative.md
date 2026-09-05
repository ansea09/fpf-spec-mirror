---
chunk_kind: "child"
pattern_id: "C.3.3"
pattern_title: "KindBridge and CL^k — Cross-local Correspondence between Distinct Kinds"
section_id: "C.3.3:6"
section_title: "Norms & Invariants (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.3/C.3.3__007_norms-invariants-normative.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "C.3.3 — KindBridge and CL^k — Cross-local Correspondence between Distinct Kinds"
  - "C.3.3:6 — Norms & Invariants (normative)"
line_start: 45898
line_end: 45938
dependencies:
  - "A.2.6"
  - "A.6.REL"
  - "C.2.1"
  - "C.2.2"
  - "C.3.1"
  - "C.3.2"
  - "F.9"
keywords:
---

### C.3.3:6 - Norms & Invariants (normative)

> The **KB‑01…KB‑12** rules below govern kind correspondence.

#### C.3.3:6.1 - Direct Relation Subject and Scope

**KB-01 (Distinct participants and obtaining).** One `KindBridge` occurrence has exactly two ordered participants: an independently identified source kind and an independently identified distinct target kind. It obtains only when its directional correspondence predicate holds within declared definedness. A different locality, label, scheme, or extension supplies no bridge. Signatures, assertions, evidence, `CL^k`, loss notes, and slices are not participants.

**KB-02 (No Scope or sense substitution).** A `KindBridge` maps neither Claim/Work scope nor local wording. Scope translation uses A.2.6 when the receiving claim actually consumes it. An F.9 relation is added only for a current distinct-sense use. Neither channel is required merely because a kind bridge exists.

**No blended score.** Scope congruence, sense-relation loss, and kind congruence remain separate. Do not aggregate them into one interoperability score.

#### C.3.3:6.2 - Settlement, Assertion, and Identity

**KB-03 (Direct settlement).** The C.3.3 settlement SHALL make recoverable:

1. exact ordered source-kind and target-kind participants and the proof that they are distinct;
2. the directional correspondence predicate, applicability, and definedness; and
3. participant-determined occurrence identity for that ordered pair.

The separate bridge assertion states whether obtaining is affirmed, denied, or unresolved; only an affirmative assertion may designate an obtaining occurrence. It also names the declaration and scheme editions used to interpret the predicate, selected source and target subkind facts, preservation/collapse/non-preservation/unknown results, `CL^k`, loss, evidence, and admitted use. Another assertion, mapping expression, card, signature, scheme edition, or publication does not create another relation occurrence. A changed interpretation prompts a renewed obtaining test. If the same ordered participants and correspondence continue, the same relation continues; if not, the prior obtaining claim is no longer current.

**KB-04 (Fresh receiving classification).** With fixed receiving candidate, signature edition, and slice, check admissibility first. `not-applicable` forms no classification judgment. An admissible request is evaluated reproducibly as `true`, `false`, or `unknown`. A source judgment or bridge assertion may support reliance but is never copied into the receiving result. An unavailable bridge dependency blocks that bridge use without rewriting an independently evaluated receiving result.

#### C.3.3:6.3 - Order & Monotonicity

**KB-05 (Monotone order).** If a bridge assertion states that source order fact `SubkindOfObtains(k1, k2; sourceRS)` is preserved, it SHALL designate exact target kinds `k1'` and `k2'`, the respective obtaining `KindBridge` relations from `k1` to `k1'` and from `k2` to `k2'`, and the basis on which `SubkindOfObtains(k1', k2'; targetRS)` holds. Identify a target `R_sub : U.SubkindOf` occurrence only when a receiving use needs occurrence identity.
**KB-06 (No inversions).** A bridge assertion MUST NOT state preservation when the mapped target order is inverted. If `SubkindOfObtains(k2', k1'; targetRS)` holds for distinct mapped kinds and the required forward fact `SubkindOfObtains(k1', k2'; targetRS)` is established not to hold, state non-preservation and the exact loss. If the required target order cannot be settled, state `unknown`; do not turn non-settlement into either preservation or inversion.
**KB-07 (Collapse semantics).** A bridge assertion may classify selected source subkind distinctions as collapsed when several source kinds correspond to one target kind. The assertion SHALL designate the affected obtaining `U.SubkindOf` relations and state the lost properties; the direct bridge relation does not alter either local order.

#### C.3.3:6.4 - Congruence & Assurance

**KB-08 (Anchor reuse and AT neutrality).** `CL^k` reuses the ordinal anchor semantics of CL but assesses the declared bridge use over kind intent and order. The bridge-assertion episteme labels it kind-congruence. KindAT remains editorial under C.3.5 and independent of `CL^k`.
**KB-09 (Effect on R only).** After receiving admissibility has been checked and an admissible candidate has received a fresh target judgment, a claim that relies on both that result and an obtaining KindBridge may apply only the bridge assertion's justified monotone `Ψ(CL^k)` consequence to R, alongside any independently established scope-relation consequence. A `not-applicable` candidate forms no judgment; `unknown` stays `unknown`; F and G do not change.
**KB‑10 (Chaining).** For a chain of bridges, **effective `CL^k` = min** of the links (weakest‑link).

#### C.3.3:6.5 - Loss Notes & Definedness

**KB-11 (Loss notes).** The bridge-assertion episteme SHALL state which `KindSignature` invariants are not preserved, which obtaining source `U.SubkindOf` relations are collapsed or not preserved, and any higher-equality caveats. These claims do not rewrite the source or target kinds.
**KB-12 (Definedness and guard use).** The bridge predicate and assertion SHALL state definedness. Outside it, a receiving guard declines that bridge use. Independently, receiving classification keeps `not-applicable` or its admissible `true`, `false`, or `unknown` result; bridge inapplicability rewrites none of them.

