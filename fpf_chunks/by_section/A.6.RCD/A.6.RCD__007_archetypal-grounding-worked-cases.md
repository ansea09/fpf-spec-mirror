---
chunk_kind: "child"
pattern_id: "A.6.RCD"
pattern_title: "Needed Relation Claim Derivation and Relation-Kind Admission"
section_id: "A.6.RCD:5"
section_title: "Archetypal Grounding — Worked Cases"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.RCD/A.6.RCD__007_archetypal-grounding-worked-cases.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "A.6.RCD — Needed Relation Claim Derivation and Relation-Kind Admission"
  - "A.6.RCD:5 — Archetypal Grounding — Worked Cases"
line_start: 17212
line_end: 17275
dependencies:
  - "A.11"
  - "A.6.0"
  - "A.6.5"
  - "A.6.P"
  - "A.6.REL"
  - "B.3"
  - "C.2.1"
  - "C.29"
  - "E.24"
  - "E.24.UK"
  - "F.17"
  - "F.18"
  - "F.9"
  - "G.11"
  - "U.Signature"
keywords:
---

### A.6.RCD:5 - Archetypal Grounding — Worked Cases

#### A.6.RCD:5.1 - Promise-content fulfilment: use the existing direct A.2.3 predicate

**Situation.** `PromiseContent_Housing42_v3` says that exact housing `Housing_42` must be delivered to `AssemblyCell_B` during `Interval_42`, satisfy `OutcomeSpec_Housing42_v3`, and satisfy the acceptance predicate in `AcceptanceSpec_Housing42_v3`. The actual delivery work is the independently identified `U.Work` occurrence `Work_DeliverHousing42`; it is not the delivered entity, the post-delivery state, the evaluation, or the acceptance result.

**A.2.3 predicate and required subset.** A.2.3 already supplies the direct predicate `fulfilsPromiseContent(W, SC)`, so disposition 1 is available. For this exact promise-content edition, the necessary and sufficient world-side subset is:

1. `PromiseContentUse(Work_DeliverHousing42, PromiseContent_Housing42_v3, Interval_42)` obtains;
2. `PromisedOutcomeDeliveryRelation(Work_DeliverHousing42, OutcomeSpec_Housing42_v3)` obtains because the selected work facts, exact delivered entity `Housing_42`, and its post-delivery state satisfy that OutcomeSpec; and
3. the acceptance predicate in `AcceptanceSpec_Housing42_v3` is satisfied for those exact facts and states.

No production or entity-inception claim is current because `Housing_42` already existed before this delivery work. This edition requires no additional generic transfer or institutional-acceptance relation beyond the two A.2.3 relations and its acceptance predicate. If another edition requires one, it must name that exact direct relation and its participants rather than adding a `delivery work` bundle.

**Evaluation, result, and evidence.** Separate evaluation work `Work_InspectHousing42` applies the declared acceptance method. Its exact operation-result binding carries the verdict value; optional episteme `InspectionVerdict_Housing42` states that evaluation result. An A.10 evidence-use relation may support reliance on the affirmative fulfilment assertion. The evaluation work, result binding, verdict episteme, and evidence-use relation neither become parts of `Work_DeliverHousing42` nor make `PromiseContentFulfilmentRelation` obtain. The three world-side conditions above make the direct relation obtain; evaluation and evidence only support an assertion about it.

**Positive case.** All three required conditions above are satisfied, so the direct predicate is satisfied and a claim-bearing episteme may state `fulfilsPromiseContent(Work_DeliverHousing42, PromiseContent_Housing42_v3)` without creating the occurrence.

**Discriminating failures.** `Work_DeliverHousing42` can occur and `Housing_42` can be in the target post-state while `PromiseContentUse` is absent or concerns another promise edition; then `PromisedOutcomeDeliveryRelation` for this promised outcome does not obtain and the promise is not fulfilled. Or the delivery relation can obtain while one acceptance condition is false; an `accepted` label or report cannot repair that failure. Missing evidence leaves reliance on the assertion unresolved; it creates neither fulfilment nor non-fulfilment.

**Disposition and stop.** Stop at disposition 1 under A.2.3. No new compound-law episteme, predicate definition, relation kind, or `RelationSignature` is needed. Use A.6.REL only if a later use must distinguish this fulfilment occurrence from another occurrence of the same admitted relation.

#### A.6.RCD:5.2 - System-role assignment and performed Work: recover A.13 and A.15.1 first, then use F.6 directly when attribution is current

**Situation.** A work record needs the readable claim that one actual system performed one exact Work occurrence under one exact assignment to a system role.

**Base and direct result.** Recover `S : U.System` as the exact actual performer through A.13 and let A.15.1 independently admit exact `W : U.Work`. When the work record expressly needs the under-assignment claim, reuse the same obtaining A.13 assignment `RA`, apply F.6 to the direct predicate `performedUnderAssignment(W, RA)`, and compare `RA.HolderSystemSlot` with the already recovered `S`. F.6 identifies neither assignment nor performer. A C.2.1 episteme may assert that result for the receiving use. The system performs the Work; the assignment supplies its holder and assigned-kind projection but neither acts nor creates another participation relation. If F.6 is missing or fails, retain the Work and remove only the under-assignment claim.

**Positive case.** A.13 has already recovered `S` through the same obtaining `RA`, A.15.1 has independently admitted `W`, `RA` covers `W`, `RA.HolderSystemSlot = S`, and F.6's direct Work-attribution predicate holds for the exact pair. The readable result is “S performed W under RA.” No generic enactment object is needed.

**Discriminating failure.** The assignment obtains, but another system performs the Work, or `S` performs Work outside the assignment's extent. Assignment plus nearby Work is insufficient; capability, responsibility, authority, and a result also remain separate claims.

**Disposition and stop.** Stop at disposition 1 under A.2.1 and F.6. Admit no `RoleEnactment` kind, compound relation, occurrence, or `RelationSignature`. If a later use needs another participation or functioning relation in addition to Work attribution, name its direct predicate or return that exact missing governor instead of generalizing from *enacted*.

#### A.6.RCD:5.3 - Supply-chain reachability: subject-bounded query or reusable predicate definition

**Situation.** One planner asks whether `Supplier_A` can reach `Plant_B` inside `SupplyNetwork_North_2026`. Other planners want the same directed-reachability rule for independently identified supply-network structures.

**Base and derivation.** Name the direct edge-relation kinds, direction, structure parameter, source and target parameters, path or closure rule, zero-length and cycle policies, applicability, and edge-definition editions. A one-off answer is a local compound claim. Repeated queries only about `SupplyNetwork_North_2026` may use a subject-bounded compound-law episteme whose `EntityOfConcern` is that exact structure and whose reuse boundary excludes other structures. When the same parameterized rule is reused across independently identified structures, publish `DirectedReachabilityPredicate_v1` as a predicate-definition episteme whose `EntityOfConcern` is that exact reusable definition. If its claim graph supplies A.6.0's subject and value range, Vocabulary, Laws, and Applicability, it may independently satisfy ordinary `U.Signature` membership without becoming a `RelationSignature`.

**Positive case.** A path exists whose every edge is an obtaining occurrence of the admitted base relation under the selected structure and closure rule.

**Discriminating failure.** A graph representation contains a visual or stored path, but one edge points in the wrong direction, denotes a different base relation, or belongs to a superseded structure edition. Representation connectivity therefore does not satisfy the reachability predicate.

**Disposition and stop.** The one-off query stops at disposition 2. Repeated use confined to one exact structure stops at disposition 3's subject-bounded branch. Cross-structure reuse stops at disposition 3's reusable predicate-definition branch and may add ordinary A.6.0 `U.Signature` membership. If a subject practice later needs reachability occurrences with action-facing identity, recurrence, continuation, or participation in another relation, the A.6.RCD application records a derived reachability-kind candidate plus a proposed direct subject settlement; apply the E.24 and E.24.UK admission tests and the A.11 parsimony test when current. Create a `RelationSignature` only for an admitted relation kind. Path identity, query-result-row identity, predicate-definition identity, subject-structure identity, and relation-occurrence identity are not interchangeable.

#### A.6.RCD:5.4 - Formal and probabilistic result use: preserve separate algebras

**Situation.** One engineering decision-work occurrence consumes one formal result episteme and one probabilistic result episteme.

**Base and derivation.** Keep the formal result in its formal substrate and the probabilistic result in its probability substrate. State the two result-use assertions under their exact predicates in one `C.2.1` episteme whose exact `EntityOfConcern` is the engineering decision-work occurrence. The formal and probabilistic result epistemes remain distinct used results; neither their pair nor a union of nearby objects replaces that concern.

No F.9 Bridge is needed for this case as stated: the two result epistemes enter the decision through separate direct use relations, and no obtaining relation between two exact F.17 cells is claimed. No ReferencePlane crossing is claimed either, so no plane relation or policy is added. Either fact could later become current without creating the other.

**Positive case.** Both direct use relations obtain for the decision-work occurrence under their own applicability, so the decision rationale can cite each result for its admitted use.

**Discriminating failure.** The two results are co-published or mention the same subject, but the decision work has no current direct use relation to one of them. Shared carrier, topic, or notation does not establish decision use.

**Disposition and stop.** The apparent combined need decomposes into two independently stated receiving claims. Each closes under disposition 1 with its exact direct decision-use relation. Do not publish a cross-algebra conjunction predicate merely to join the sentences, and do not infer one composite relation occurrence from a decision record.

#### A.6.RCD:5.5 - Primitive-candidate stop test

A subject practice proposes a primitive relation because all accepted bases preserve co-occurrence and shared participants but lose one independently used subject distinction. The candidate advances only when the subject can name that lost distinction, show a positive and discriminating case, state its own obtaining and recurrence laws, distinguish repeated occurrences, and identify independent receiving uses. If any item is missing, the honest result is a local claim, reusable predicate definition, or exact blocker. This is disposition 4's positive test, not a license to mint a placeholder relation.

