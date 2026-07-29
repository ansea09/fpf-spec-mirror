---
chunk_kind: "child"
pattern_id: "A.6.9"
pattern_title: "Cross-Context Sameness Disambiguation - Repairing cross-context \"same\", \"equivalent\", and \"align\" via explicit Bridges (RPR-XCTX)"
section_id: "A.6.9:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.9/A.6.9__006_solution.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "A.6.9 — Cross-Context Sameness Disambiguation - Repairing cross-context \"same\", \"equivalent\", and \"align\" via explicit Bridges (RPR-XCTX)"
  - "A.6.9:4 — Solution"
line_start: 20323
line_end: 20460
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.1"
  - "A.2.6"
  - "A.22"
  - "A.6.3.RT"
  - "A.6.6"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.2.1"
  - "C.29"
  - "C.3.3"
  - "E.17"
  - "E.19"
  - "F.0.1"
  - "F.17"
  - "F.18"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "A.10/B.3 reliance"
  - "LocalSenseClaim> projections"
  - "actual receiving object"
  - "ambiguous sameness"
  - "different <ReferenceScheme"
  - "direct-owner dispatch"
  - "exact F.17 SchemeSenseCell endpoints"
  - "explicit stop"
  - "relation-only F.9 Bridge"
  - "separate C.2.1 bounded-use claim"
---

### A.6.9:4 - Solution

Treat an umbrella sameness sentence as a **dispatch trigger**, not as an automatic Bridge and not as a demand for a card. Recover the concrete subject and action first. Then choose the smallest truthful branch:

1. **Ordinary designation inside one semantic context.** If both expressions resolve under the same `<ReferenceScheme, LocalSenseClaim>` projection and the current action needs only the governed designation, rewrite with that designation and stop. No F.9 Bridge is current.
2. **Lane or reference-plane repair.** If the sentence confuses Object, Description, Carrier, or `CHR:ReferencePlane`, restore the exact kinds under A.7 or the governing plane rule.
3. **Identification or indexing.** If the sentence means same id, key, code, or index target, use A.6.6. Identifier equality does not establish meaning correspondence.
4. **Claim-scope operation.** Use A.2.6 `widen`, `narrow`, or `refit` inside one semantic context. A `translate` operation may consume an independently obtaining Bridge and a separate affirmative claim for that translation.
5. **Representation transition.** Route an actual source-to-receiving representation change to A.6.3.RT. A Bridge neither performs the Work nor creates the transition.
6. **Structure comparison or crossing.** Recover each exact A.22 structure and its organizing relations. A sense Bridge between names does not relate the structures by itself.
7. **Cross-local semantic relation.** Resolve two exact F.17 cells, declare the F.9 relation-semantic profile, and cite a Bridge only when its predicate obtains.
8. **Proposed use of an obtaining Bridge.** In a second sentence, name action `u`, direction `d`, use-specific rule `r`, tolerated loss `t`, and claim polarity under C.2.1. Recover A.10 or B.3 reliance for that same use.
9. **Explanation or unresolved proposal.** Say plainly what remains unestablished. A candidate or negative card carries no positive occurrence reference.
10. **Claim that the use happened.** Name the actual receiving object and open its direct governor; the use role inside the C.2.1 claim is not that object.

For A.6.9, **semantic context** is Plain shorthand for the bounded interpretation basis derived from one exact cell's `<ReferenceScheme, LocalSenseClaim>` projection. It is not a `U.BoundedContext`, entity, ref, project, scope, selected model-use structure, viewpoint, description, designator, or publication.

#### A.6.9:4.0 - Trigger and endpoint recovery

Open the dispatch when **same**, **identical**, **equivalent**, **align**, **map**, **match**, **correspond**, *treat as*, *reuse*, *share*, *unify*, *canonical source*, *synced*, *normalized*, *one-to-one*, *same ID*, or *mirrors* could hide the current object or action. Apply equivalent triggers in any language.

Resolve the actual endpoints before choosing the semantic branch. Each candidate endpoint must be a `SenseCellAddressRef` resolving one exact F.17 `SchemeSenseCell`; a string, system, table, class name, file, context label, card, or id cannot stand in for it. If a token is metonymic — *the system*, *the model*, *the service*, *that table* — enumerate the plausible governed objects and recover the intended local expression and claim. If either endpoint remains unresolved, keep the sentence explanatory and return `unresolved SenseCell endpoint`.

Pin the endpoint reference-scheme and local-sense-claim editions, or an exact as-of basis, when the correspondence can change with a canon or model edition. `Γ_time` may be used as a compact card label for that basis. It is not a participant. It contributes to profile identity only when it states the profile's exact applicability or as-of basis.

Before testing a Bridge, check ontological strata. Kind or classification transfer remains with C.3.3; value normalization with the measurement owner; role assignment with A.2.1; performed-Work attribution with F.6; publication with E.17; representation transition with A.6.3.RT. F.9 can supply a semantic premise needed by one of those claims but cannot make that neighboring object obtain.

#### A.6.9:4.1 - Stable lens: relation, use claim, reliance, and receiving object

Keep these objects distinct:

1. **Bridge occurrence.** The direct relation has exactly two F.17 cell participants and obtains under one exact F.9 profile.
2. **BridgePredicateProfile.** It contains only Bridge kind, kind-defined symmetry or orientation, endpoint-sense readings, relation-specific correspondence or difference condition, applicability and as-of basis, Boolean truth condition, and stop dependencies.
3. **Bounded-use claim.** An ordinary C.2.1 claim says whether the exact obtaining Bridge is suitable for `<u,d,r,t>`. Its EntityOfConcern is the Bridge; its ClaimGraph designates the use, direction, rule, tolerance, and polarity; its effective scheme interprets them.
4. **Optional Bridge Card.** It packages claims and evidence when durable reuse pays. It neither creates the relation nor grants the use.
5. **Separately governed receiving object.** If the use happened, its Work, assertion, publication, direct relation, operation application, or other object keeps its own participants, obtaining or performance condition, and identity.

```text
Bridge(SourceSenseCell, ReceivingSenseCell; BridgePredicateProfile)
```

Use that notation only after the F.9 predicate passes. For a proposal, write `candidate Bridge(...)` or use a candidate card with no positive occurrence reference.

Changing `u`, `d`, `r`, or `t` changes the bounded-use claim, not the Bridge. Changing evidence, an A.10 relation or local `RelianceDisposition`, or a B.3 claim, record, or disposition reopens reliance without reidentifying either fixed object. A changed endpoint or relation-semantic profile identifies another Bridge candidate.

#### A.6.9:4.2 - Explicit claim skeleton

| Item | When required | Meaning and stop |
| --- | ---: | --- |
| `SourceSenseCellRef`, `ReceivingSenseCellRef` | every Bridge candidate | Exact F.17 addresses; unresolved endpoints stop the semantic branch. |
| semantic-context projections | every Bridge candidate | Derived `<ReferenceScheme, LocalSenseClaim>` pairs; they must differ for F.9. |
| `BridgePredicateProfile` | every Bridge candidate | Exact by-value relation semantics only; a label or id is insufficient. |
| `BridgeKind` and relation orientation | profile and readable explanation | What semantic correspondence or difference is claimed; not a use licence. |
| applicability / `Γ_time`, truth condition, dependencies | profile | When and how the direct predicate is tested; missing dependencies stop without inventing an occurrence. |
| action `u` | every proposed use | What the reader proposes to compare, substitute, translate, publish, or otherwise do. |
| direction `d` | every proposed use | Exact use-source to use-receiving order; relation symmetry supplies no direction by implication. |
| rule `r` | every proposed use | The correspondence rule the action will follow. |
| tolerance `t` | every proposed use | Which semantic loss is acceptable for this action; observed loss remains evidence. |
| polarity and effective ReferenceScheme | every bounded-use claim | Whether the claim is affirmative or negative and how its designations are interpreted. |
| A.10 or B.3 branch | when someone will rely on the claim | The exact evidence-provenance relation plus local disposition, or the B.3 claim or explicit disposition selected by its trigger. |
| authorization claim | only when permission is required | Separate policy or deontic governor; semantic suitability and assurance are insufficient. |
| receiving-object ref | only when the use is said to have happened | Exact Work, assertion, publication, relation, application, or other object under its owner. |
| `ClaimMode` and card EntityOfConcern | only when a card pays | Actual card concerns the obtaining Bridge; candidate or negative card concerns the admitted F.9 Bridge relation kind and carries proposed endpoints and profile in its ClaimGraph. |

Only the two endpoint cells fill the direct relation's participant slots. Use content is ClaimGraph content, not another relation participant or profile component.

#### A.6.9:4.3 - Judgement and change

Choose the least-committing truthful Bridge kind: `Equivalence`, `Narrower-than`, `Broader-than`, `Partial-overlap`, `Disjoint`, or one declared cross-family relation kind. The kind settles relation semantics only.

Then judge the proposed use:

* `Partial-overlap` can support an affirmative label-use claim when its exact rule preserves the named differences; the Bridge does not grant that use automatically.
* `Disjoint` can support a contrastive explanation; a proposed substitution receives negative polarity.
* `Equivalence` is symmetric, but `A -> B` and `B -> A` are different use claims.
* `Narrower-than` and `Broader-than` orient the semantic relation. Narrower-to-broader is usually easier to warrant, but every use direction still needs its own rule, tolerance, polarity, and reliance.
* A broader-to-narrower proposal normally requires refined cells and a separately tested Bridge. Another profile over the same broad endpoints cannot make an unsafe use safe by declaration.
* Type-structure reuse requires a separate claim naming the structural rule and loss tolerance. Matched invariants can support that claim; no `CL` number grants it.

`CL` may remain optional evidence shorthand: `0` contradicted, `1` weakly comparable, `2` bounded support with counterexamples, `3` matched stated invariants with no current material counterexample. It is neither profile identity nor a suitability threshold.

Narrate changes by the object that changed:

1. `retargetEndpoint` for another source or receiving cell;
2. `replaceBridgeProfile` for changed relation-semantic content;
3. `reviseBoundedUseClaim` for changed `u`, `d`, `r`, `t`, effective scheme, or polarity;
4. `retestObtaining` for changed endpoint facts or dependencies under the fixed profile;
5. `reopenReliance` for changed evidence, currentness, A.10 relation or disposition, or B.3 claim, record, or disposition;
6. `reviseBridgeCard` for changed package content;
7. `publishBridgeCardEdition` for a publication occurrence; and
8. `recoverReceivingObject` when the use is claimed to have happened.

An inverse asymmetric relation and any direct A-to-C relation require their own profiles and tests. Two chained Bridges do not entail a third.

#### A.6.9:4.4 - Lexical guardrails

In normative or decision-carrying prose, replace the umbrella word with a sentence that exposes the action and stop:

| Intended meaning | Plain action | Exact follow-through |
| --- | --- | --- |
| ordinary same-context designation | “Both expressions designate this local sense.” | Cite the common projection and naming owner; no Bridge. |
| interpretation | “Use A to explain B; do not substitute it.” | Test the cross-family Bridge; state a separate affirmative explanation-use claim and its nearest non-use. |
| naming convenience | “Use the label ‘actor’ in this comparison; keep account and customer eligibility distinct.” | Obtaining Bridge plus a C.2.1 claim naming direction, label rule, and zero tolerance for eligibility transfer. |
| directional substitution | “For calculation X, read A as B by rule R within tolerance T; do not reverse it.” | Obtaining Bridge, affirmative claim for `<X,A->B,R,T>`, and current A.10 or B.3 reliance. |
| type-structure reuse | “Reuse this subtype row only while invariants I remain true and loss stays within T.” | Obtaining Bridge plus a separately warranted structural-use claim. |
| contrast | “These senses differ in this stated way; do not substitute them.” | Obtaining `Disjoint` or `Partial-overlap` Bridge plus negative substitution-use polarity. |
| unresolved proposal | “The mapping is available, but the semantic relation is not established.” | Candidate card or plain stop naming the missing endpoint, predicate fact, or dependency. |

Plain teaching prose may retain *same*, *align*, or *map* only when the local sentence also tells the reader what to do, what not to infer, and what result would reopen the claim.

#### A.6.9:4.5 - Disambiguation guide

| Trigger | First question | Default route | Stop |
| --- | --- | --- | --- |
| “A is the same as B” | Same local sense or relation between distinct senses? | designation first; otherwise least-committing F.9 kind | no exact cells or predicate -> explanatory only |
| “Align A and B” | Shared label, comparison, substitution, or structure use? | name the proposed action before selecting a Bridge | mapping score alone establishes neither relation nor use |
| “Map A to B” | Semantic reading or operational transformation? | keep code or ETL as witness; test semantics separately | code direction is not use suitability |
| “Same ID/key/one-to-one” | Identifier relation or meaning relation? | A.6.6 first | collision-free ids do not establish sense identity |
| “B is a view/projection of A” | View membership, representation, or sense reuse? | E.17, C.29, or representation owner first | dropped constraints block stronger use claims |
| “Equivalent” | What relation, action, direction, rule, and tolerance? | test overlap or inclusion before equivalence | symmetry alone grants no use |

#### A.6.9:4.6 - Mapping witnesses are not Bridges

A lookup table, aligner model, transformation function, API, or ETL step is an implementation or evidence object. It may support the claim that a Bridge obtains or that one bounded use is suitable. It does not determine either claim by itself. Code may run `A -> B` while the semantic Bridge is symmetric, oriented the other way, or absent; and even an obtaining Bridge may be unsuitable for that operation's rule or tolerance.

Keep the witness in the A.10 evidence path or optional card. Test the F.9 predicate first, state the C.2.1 bounded-use claim second, and recover reliance third.

#### A.6.9:4.7 - Coordination boundaries

- **Naming:** F.18 selects designations; F.17 publishes exact scheme-based cells and rows. Neither creates a Bridge.
- **Evidence and assurance:** A.10 owns evidence provenance and local reliance; B.3 owns assurance claims, records, and explicit dispositions.
- **Scopes:** A.2.6 owns `widen`, `narrow`, `refit`, and `translate`; translation consumes an obtaining Bridge only together with an affirmative claim for its exact direction, rule, and tolerance.
- **Views, representations, and publications:** E.17, C.29, and A.6.3.RT own their objects and occurrences.
- **Kinds and classifications:** C.3.3 owns classification transfer; F.9 supplies only local-sense correspondence needed by that use.
- **Structures:** A.22 and direct relation owners identify structures and crossings. A sense Bridge cannot substitute for that architecture.
- **Work and roles:** A.2.1, F.6, and A.15.1 own assignments and performed Work; a semantic relation or use claim has no enactment effect.
- **Authorization:** the exact policy or deontic governor owns permission. Neither semantic suitability nor assurance grants it.

