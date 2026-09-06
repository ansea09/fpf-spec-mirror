---
chunk_kind: "child"
pattern_id: "C.3.A"
pattern_title: "Typed Guard Macros for Kinds + USM (Annex)"
section_id: "C.3.A:4"
section_title: "Normative guard macros"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.A/C.3.A__005_normative-guard-macros.md"
commit_sha: "43c46859c3926a371fa60cfb1c76aefa19f9eaf9"
heading_path:
  - "C.3.A — Typed Guard Macros for Kinds + USM (Annex)"
  - "C.3.A:4 — Normative guard macros"
line_start: 46458
line_end: 46555
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.2.6"
  - "C.2.2"
  - "C.2.3"
  - "C.3"
  - "C.3.1-C.3.5"
keywords:
  - "ESG"
  - "Method-Work"
  - "assurance"
  - "declaration compatibility"
  - "exact candidate judgment"
  - "guard refusal"
  - "regulatory"
  - "true/false/unknown"
---

### C.3.A:4 - Normative guard macros

Names such as `Guard_TypedClaim` are editorial handles. A context may alias them only when the same objects, values, and refusal distinctions remain recoverable.

#### C.3.A:4.1 - Guard_TypedClaim — declaration-level admission

**Intent.** Decide whether claim `C`, quantified over local kind `k_claim`, may enter a receiving use restricted to kind `k_receive` in `TargetSlice`, without claiming anything yet about an unnamed candidate.

`Guard_TypedClaim(C, k_claim, claimSignatureEdition, k_receive, receiveSignatureEdition, TargetSlice, thresholds?)` SHALL:

1. recover the exact `KindSignature` declaration episteme editions whose respective `EntityOfConcern` values are `k_claim` and `k_receive`, and whose evaluation domains and effective reference schemes cover the declared use; when both roles use the same kind and edition, state that identity rather than duplicating the declaration;
2. establish declaration-level kind compatibility:
   - the kinds are identical or `SubkindOfObtains(k_receive, k_claim; effectiveReferenceScheme)` holds under C.3.1, with an identified `R_sub : U.SubkindOf` occurrence only when occurrence identity is needed; or
   - for a required directional correspondence between independently identified distinct kinds, an obtaining KindBridge relates exact source `k_claim` and target `k_receive` under the paired source and target `KindSignature` editions, and a separate current bridge assertion states the mapping, applicability, loss, `CL^k`, evidence, and admitted receiving use;
3. require `U.ClaimScope(C)` to cover the exact `TargetSlice` and require an explicit `Gamma_time` selector;
4. apply only the justified bridge consequences to R;
5. check evidence freshness separately when the admission implies reliance; and
6. check a policy-required formality threshold on the exact claim or declaration episteme that owns the value.

The subkind direction above is contravariant only for restricting a universally quantified claim: a claim over `Vehicle` may enter a `PassengerCar`-restricted use when `PassengerCar` is a subkind of `Vehicle`. It is not a generic compatibility direction for producer outputs, operation arguments, mutable positions, or arbitrary typed slots; each such use states its own variance rule. This guard MUST NOT invent an anonymous candidate or infer a candidate classification from declaration compatibility.

#### C.3.A:4.2 - Guard_CandidateUse — apply a typed claim to an exact candidate

**Intent.** Decide whether claim `C`, quantified over `k_claim`, may be used for exact target-side candidate `candidate` in a receiving use restricted to `k_receive`.

`Guard_CandidateUse(C, candidate, k_claim, claimSignatureEdition, k_receive, receiveSignatureEdition, TargetSlice)` SHALL:

1. identify the candidate under its direct governor before classification;
2. satisfy `Guard_TypedClaim` for the same claim-kind and receiving-kind editions and slice;
3. evaluate `J(candidate, k_receive, receiveSignatureEdition, TargetSlice)`;
4. continue candidate-bearing use only on `true`: for a proper subkind, the already established `SubkindOfObtains(k_receive, k_claim; RS)` supplies the monotone claim-kind consequence; for a bridged use, rely only through the obtaining KindBridge and its current assertion, without inventing a source-context candidate judgment;
5. refuse on known `false` while retaining that value; and
6. refuse on `unknown` while retaining the missing dependency or unavailable support reason.

Evidence may support a classification assertion, but record presence, bridge presence, or guard invocation MUST NOT make the candidate satisfy the receiving criterion. When `k_claim` and `k_receive` are identical under one declaration edition, record that identity and evaluate the candidate once.

#### C.3.A:4.3 - Guard_TypedJoin — compose typed producers and consumers

**Intent.** Compose producer `A`, which declares output kind `k_A`, with consumer `B`, which expects input kind `k_B`.

`Guard_TypedJoin(A, k_A, edition_A; B, k_B, edition_B; TargetSlice)` SHALL:

1. pin both declaration episteme editions;
2. establish output-to-input compatibility in the covariant flow direction:
   - the kinds are identical or `SubkindOfObtains(k_A, k_B; effectiveReferenceScheme)` holds; or
   - for a bridged flow, an obtaining KindBridge maps `k_A` to exact, independently identified distinct target-side kind `k_A'`, its separate assertion carries the current mapping and loss basis, and `k_A'` is identical to `k_B` or `SubkindOfObtains(k_A', k_B; targetReferenceScheme)` holds;
3. compute serial scope as the intersection of the two governed scopes and require coverage of `TargetSlice`;
4. route bridge consequences to R and check freshness separately; and
5. when an actual produced candidate enters B, evaluate `J(candidate, k_B, edition_B, TargetSlice)` and continue only on `true`, preserving `false` and `unknown` separately from refusal.

Declaration compatibility alone MUST NOT classify a future or actual output. Scope widening MUST NOT repair a type mismatch. The universal-claim variance rule in `Guard_TypedClaim` does not reverse this producer-to-consumer direction.

#### C.3.A:4.4 - Guard_MaskedUse — exact RoleMask use

**Intent.** Use exact candidate `candidate` under a named RoleMask declaration in `TargetSlice`.

`Guard_MaskedUse(artifact, candidate, kind, kindSignatureEdition, roleMaskEdition, TargetSlice)` SHALL:

1. recover the exact C.2.1 RoleMask declaration episteme, its base kind, pinned base signature edition, intended use, candidate-feature constraints, bindings, dependencies, and definedness;
2. check artifact scope separately through USM;
3. evaluate `J_mask(candidate, kind, kindSignatureEdition, roleMaskEdition, TargetSlice)`;
4. continue only on `true`, refuse while preserving known `false`, and fail closed while preserving `unknown`;
5. keep context predicates out of the candidate-feature criterion; and
6. for cross-context use, compare base-kind identity and recover target declarations; when this use requires a correspondence between distinct kinds, establish the KindBridge relation and assertion under C.3.3; recover any separate `MaskAdapter` declaration episteme before evaluating the target masked judgment.

A mask name is not a kind synonym. Repeated mask use can trigger review for a separately identified local kind and independently obtaining `U.SubkindOf` relation; no guard or catalog action performs that admission.

#### C.3.A:4.5 - Guard_SpanUnion_Typed — parallel support lines

**Intent.** Publish SpanUnion for the same typed claim supported by independent lines.

For each line, the guard SHALL:

1. recover the same governed claim, quantified kind, and signature edition;
2. satisfy declaration-level typed admission in that line's slice;
3. when a line's evidence is candidate-specific, bind each exact candidate and its exact judgment rather than treating a row label as classification;
4. preserve line-specific bridge consequences and freshness;
5. provide the USM independence justification; and
6. include no slice outside the union of covered line scopes.

If lines quantify over genuinely different kinds, normalize through separately justified kind relations or publish distinct claims; do not hide the difference in SpanUnion.

#### C.3.A:4.6 - Guard_XContext_Typed — cross-context typed reuse

**Intent.** Reuse claim `C` from a source context in target `TargetSlice` while keeping scope translation, kind correspondence, and target classification separate.

`Guard_XContext_Typed(C, sourceKind, sourceSignatureEdition, targetKind, targetSignatureEdition, TargetSlice, candidate?)` SHALL:

1. when the receiving claim requires Scope translation, recover the obtaining Scope Bridge and its applicable congruence assessment, the separate affirmative translation-use claim, and the current reliance branch under A.2.6;
2. compare source and target kind identity and establish the receiving use's declaration-level compatibility under §4.1; if that compatibility relies on a directional correspondence between distinct kinds, recover an obtaining KindBridge relation with exact source/target kind participants and its separate bridge assertion with pinned scheme/signature editions, mapping rule, definedness, `CL^k`, loss, evidence, and admitted use;
3. recover the independently identified target `KindSignature` edition;
4. require Claim scope, translated when needed, to cover `TargetSlice`;
5. when an actual candidate is current, evaluate the fresh target judgment `J(candidate, targetKind, targetSignatureEdition, TargetSlice)` and preserve all three values;
6. apply the justified scope- and kind-bridge consequences to R only; and
7. make the separate allow/refuse decision.

A source judgment may support reliance but MUST NOT be copied as target truth. If no candidate is current, the guard ends at declaration-level compatibility and scope; it does not fabricate one.

