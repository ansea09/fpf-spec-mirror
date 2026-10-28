---
chunk_kind: "child"
pattern_id: "B.2"
pattern_title: "Meta-Holon Transition - Whole Reidentification"
section_id: "B.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2/B.2__006_solution.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "B.2 — Meta-Holon Transition - Whole Reidentification"
  - "B.2:4 — Solution"
line_start: 43246
line_end: 43376
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.19"
  - "A.3.1"
  - "A.3.4"
  - "B.1"
  - "B.1.2"
  - "B.2"
  - "B.2.2"
  - "B.2.3"
  - "B.2.4"
  - "B.2.5"
  - "B.2.P"
  - "B.3"
  - "C.13"
  - "C.16"
  - "C.2.1"
  - "C.29"
  - "C.30.ILC"
  - "C.32.P2S"
  - "E.24.UK"
  - "G.11"
  - "U.Episteme"
keywords:
---

### B.2:4 - Solution

Use B.2 as a world-side whole-reidentification pattern. Start with the actual wholes and the facts governed by their direct patterns; add records only when a receiving use needs them.

Name what the receiving work needs from a whole: for example, a system bearing an operational capability or an episteme supporting a particular conclusion. Establish which prior whole, if any, is being compared. For a first constitution, obtain the construction facts under the applicable subject pattern and then apply A.1. For a first recognition of an existing whole, apply A.1 to the facts already obtaining; the recognition date does not establish when the whole came into existence. If the prior identity grounds are unavailable, leave that question unresolved. None of these situations supplies a prior holon for `existingWholeRef` by itself.

With an established prior whole:

1. Name the receiving claim or use, the exact existing whole, its admitted kind, and its identity or reidentification rule.
2. Recover each changed delimitation, constituent, constructive part relation, assembly, supervision, objective, capability, characteristic, or temporal fact under its direct pattern. A cue word, profile field, measurement, or graph edge does not make the fact obtain.
3. Test whether those facts can be explained as a change of the same whole using :4.2. If repair, maintenance, changed characteristics, phase coverage, method or work correction, measurement, or architecture-view correction is enough under the existing reidentification rule, keep that whole and stop B.2. If the comparison is unresolved, identify the deciding fact or rule still needed instead of declaring a new whole necessary.
4. When the comparison establishes that the existing whole is insufficient, designate the proposed new whole as an exact `U.Entity` and execute the complete A.1 criterion. Recover its constituents, obtaining constructive relations, assembly, reidentification rule, and composition-grounded whole characteristic. Also show that the candidate's actual boundary, interfaces, relevant characteristics, and identity-preservation conditions satisfy the applicability and compatibility conditions of at least one governed larger-assembly construction method or rule under which it can remain a constituent. Then name its already admitted holon kind and satisfy the direct kind-specific criterion. If a required condition fails, the candidate fails the corresponding recognition test; if missing evidence or an unavailable dependency prevents a determination, evaluation returns `unknown`.
5. State the whole-reidentification claim: why the receiving use cannot retain the existing whole and how the recognized new whole meets that use. A positive classification alone does not establish this comparison. The prior whole may continue to exist and retain a narrower use; reidentification does not require its destruction. This comparison does not itself create, admit, or classify either whole.
6. Materialize a trigger profile, optional explanation-result episteme, reidentification assertion, or record only when a named receiving use must inspect, cite, compare, or preserve that claim.

The optional `MHTTriggerProfile`, `ExistingWholeExplanationResult`, and `HolonReidentificationRecord` are ordinary C.2.1 epistemes. Their content can designate exact wholes, facts, claims, and relation occurrences; the content fields are not world-side participants and supply no substitute for the preceding move.

#### B.2:4.1 - MHTTriggerProfile

`MHTTriggerProfile` is a `U.Episteme` whose EntityOfConcern is the exact existing whole already recognized under an admitted holon kind. It collects exact current cues and support for asking whether whole reidentification is live. It is not MHT itself, and its content fields do not declare another relation.

| Content field | Value kind and use |
|---|---|
| `existingWholeRef` | `U.HolonRef` resolving to the exact existing whole already recognized under an admitted holon kind. |
| `existingWholeIdentityRuleRef` | `U.EpistemeRef` resolving to the current identity-rule episteme. |
| `currentPartRelationRefs[]` | `U.EntityRef` values, each resolving to one explicitly individuated current part-relation occurrence. |
| `changedDelimitationRelationRefs[]` | References to exact changed delimitation relation occurrences under their direct patterns. |
| `changedPartRelationRefs[]` | References to exact changed part-relation occurrences. |
| `changedSupervisionRelationRefs[]` | References to exact changed supervision relation occurrences. |
| `changedFeedbackClaimRef?` | `U.EpistemeRef` resolving to a B.2.5 compound feedback assertion when the receiving use needs that claim. Its observation and return-influence relations and coupling grounds remain with the assertion. |
| `changedCoordinationRelationRefs[]` | References to exact changed coordination relation occurrences. |
| `changedObjectiveClaimRef?` | `U.EpistemeRef` resolving to the exact objective-change claim. |
| `changedCapabilityClaimRef?` | `U.EpistemeRef` resolving to the exact capability-change claim. |
| `agencyThresholdClaimRef?` | `U.EpistemeRef` resolving to a current characteristic-space threshold claim. |
| `temporalConsolidationClaimRef?` | `U.EpistemeRef` resolving to the exact temporal-consolidation claim. |
| `evidenceRelationRefs[]` | References to exact evidence relation occurrences supporting the trigger claims. |
| `sourceUseRelationRefs[]` | References to exact source-use relation occurrences when a source is relied on. |

The profile's exact ClaimGraph and effective `U.ReferenceScheme`, together with its existing-whole EntityOfConcern, constitute its C.2.1 identity. Any current `U.ClaimScope` and an independently selected model-use structure can qualify this episteme when its receiving use needs them. These identity values and qualifications do not identify either whole, become MHT trigger facts, or make any referenced relation obtain. A single cue warrants attention; it does not establish whole reidentification.

#### B.2:4.2 - Existing-whole comparison and optional result

First perform an ordinary comparison: compare the observed change with direct explanations that preserve the existing whole. Consider better parts, corrected relations, improved measurement, method or Work repair, richer phase coverage, capability change, and architecture-view repair only when their direct patterns make those explanations current. If one explanation is sufficient for the receiving use, keep the existing whole, use that subject pattern, and stop B.2.

For each material explanation, test three things together: whether it covers the change needed by the receiving use, whether the old identity rule permits it, and whether it is compatible with the established facts. When continuity across observations is uncertain, use A.1.RI to construct the possible connections and test them against the subject constraints. A changed part may preserve one whole's identity and defeat another's; the applicable identity rule decides.

| Comparison result | Grounds and next move |
| --- | --- |
| `sufficient` | At least one supported explanation meets the receiving use while preserving the existing whole's identity. Keep that whole and continue under the subject pattern. |
| `insufficient` | An established condition necessary for the receiving use cannot be met while preserving the prior identity; or the governing facts and rules justify a closed set of applicable alternatives and every alternative fails. Proceed to the candidate's A.1 and kind-specific tests. |
| `unknown` | A deciding fact or rule is unavailable, or material alternatives remain that would change whether a new whole is needed. Obtain that missing basis or retain the unresolved comparison. |

An unsuccessful search for an explanation does not establish `insufficient`. A closed comparison needs a reason why its alternatives cover the named question, not an inventory of every imaginable explanation. If all remaining identity alternatives permit the same needed continuation, A.1.RI allows that continuation without settling the unused identity distinction; this does not establish an MHT claim.

When another use must inspect or cite the outcome, identify an optional `ExistingWholeExplanationResult` episteme whose EntityOfConcern is the existing whole:

| Content field | Value kind and use |
| --- | --- |
| `observedChangeClaimRef` | `U.EpistemeRef` resolving to the exact observed-gain or observed-shift claim. |
| `candidateExplanationClaimRefs[]` | Exact claims under their direct subject patterns. |
| `explanationEvidenceRelationRefs[]` | Evidence relations actually used to assess those explanations. |
| `existingWholeSufficiencyVerdict` | `sufficient`, `insufficient`, or `unknown` for the named receiving use. |
| `remainingWholeReidentificationQuestionRef?` | The exact residual question when the result is `insufficient` or `unknown`. |

The practitioner performs the comparison; the optional episteme records its outcome. Identity and relation claims still depend on the facts and rules used in that comparison.

#### B.2:4.3 - HolonReidentificationRecord
`HolonReidentificationRecord` is an optional `U.Episteme` whose EntityOfConcern is the established new holon. Use it only when a person or system performing later work needs a durable account of why the receiving use requires that new holon rather than the prior whole. Candidate classification remains a separately governed judgment.

| Content field | Value kind and use |
|---|---|
| `existingWholeRef` | `U.HolonRef` resolving to the exact prior whole already recognized under an admitted holon kind. |
| `selectedTriggerProfileRef` | `U.EpistemeRef` resolving to the selected `MHTTriggerProfile`. |
| `existingWholeExplanationResultRef?` | `U.EpistemeRef` resolving to the optional `ExistingWholeExplanationResult`; omit it when the ordinary comparison sentence is enough. |
| `resultHolonRef` | `U.HolonRef` resolving to the established new whole. |
| `resultHolonKindRef` | `U.KindRef` resolving to its exact admitted holon kind. |
| `resultHolonClassificationAssertionRef?` | `U.EpistemeRef` resolving, only when a person or system performing later work must inspect or cite the judgment, to a C.2.1 classification judgment about whether the candidate new whole satisfies the A.1 criterion under the stated admitted holon kind. |
| `wholeReidentificationClaimRef` | `U.EpistemeRef` resolving to the claim that the candidate new whole, rather than the prior whole, now carries the subject claim. |
| `changedClaimPatternLocators[]` | `U.EpistemeRef` values resolving to the direct patterns for each changed claim used in the rationale. |
| `evidenceRelationRefs[]` | References to exact evidence relation occurrences supporting the reidentification claim. |
| `sourceUseRelationRefs[]` | References to exact source-use relation occurrences when sources are relied on. |
| `mathLensUseOutputRefs[]?` | `MathLensUseOutputRef` values resolving to C.29 outputs whose mathematical results bear on the claim. |

A referenced C.29 output retains its correspondence, assumptions, omitted detail or loss, and limits on reliance. Select the output under C.29:4.4: a conditional explanation or diagnosis may remain a MiniCard, while reliance on the result as an adequate model of the phenomenon requires the FullCard account. Reuse an adequate existing account. Ordinary local mathematics need not produce a C.29 output, and an output reference does not assert a lens-use relation occurrence.

The record does not make the A.1 criterion true, admit a public kind, or create the candidate new holon. `E.24.UK` is the pattern for public-kind admission; A.1 is the pattern for world-side recognition; C.2.1 is the pattern for the optional classification assertion. Recognition requires the relevant construction and identity grounds. When evidence is relied on, retain the evidence relations supporting the particular claim.

Use B.3 when the receiving question asks whether support is adequate for a named claim and use, or when a binding requirement calls for that assurance. Supply B.3's minimum qualified result, adding Work, performer, or replay information only when that use requires it. Storing an optional classification assertion alone creates no separate assurance duty. Check whether existing support applies to the result claim; adequate support can be reused, while assurance for parts does not automatically transfer to the whole. Publication of the record is another relation under the publication patterns.

#### B.2:4.4 - Candidate New Whole Reference And Kind

Before recognition, designate the candidate as an exact `U.Entity` and name the admitted kind under which it is being tested. A known failure of a necessary A.1 or kind-specific condition yields `false`; unavailable deciding grounds yield `unknown`. Neither result proves that the prior whole is sufficient for the receiving use.

For the established result, use one `resultHolonRef : U.HolonRef` and one `resultHolonKindRef : U.KindRef` for its kind. `E.24.UK` must already have admitted that public kind, and the candidate new whole must satisfy the A.1 constructive criterion plus any kind-specific membership condition. Neither the references nor the record establish those facts.

When a person or system performing downstream work must inspect or cite a preliminary, failed, or unresolved evaluation, use the optional classification assertion or result episteme governed by A.1 and C.2.1. Its EntityOfConcern is the candidate being evaluated. After establishing the new holon, a needed `HolonReidentificationRecord` may cite the classification judgment through `resultHolonClassificationAssertionRef`.

That C.2.1 assertion may report a governed evaluation of `true`, `false`, or `unknown`; its evidence, warrant, and G.11 currentness stay separate from world-side criterion satisfaction. A false or unresolved assertion does not become a positive result by being cited in a record. A historical record can be preserved when support later becomes unavailable; present reliance must reflect that loss, which alone does not change the object's historical identity. B.2 still asks a different question: whether the existing whole can continue to carry the subject claim or a new whole must be identified.

#### B.2:4.5 - Agency Threshold

An agency-characteristic threshold is a condition in a characteristic space, not a root kind or a substitute for the A.13 agency claim. State its exact System, predicate, claim scope, and qualification window.

Use `A.13`, `A.19`, and `C.16` for the characteristic-space and threshold claim. Levin-line TAME work can discipline the multi-characteristic framing when agency evidence is relied on for the current claim. B.2 uses agency threshold only as one possible trigger in `MHTTriggerProfile`, and only when crossing the threshold changes closure, supervision, objective, or whole identity.

Recover the admitted System and its agency-relevant characteristic or threshold independently. A System may bear that characteristic while participating passively in the situation. A precise agency claim additionally requires the A.13 core, including the local agential system-role kind, System-classification judgment, and obtaining assignment; a characteristic-only claim does not acquire that additional scope. If claim-bearing source wording still says only “role,” use `E.10.ROLE` rather than presuming classification or assignment.

#### B.2:4.6 - Acting-System Participation

When a source describes a system changing another holon, recover acting-system participation and transformation separately.

Use `A.12` for acting-side externalization, `A.3.4` for bounded transformation, and `A.15.1` for work occurrence. Changing another holon does not establish a part-whole relation between that holon and the acting System.

#### B.2:4.7 - Mathematical-Lens Separation

A mathematical or analytical result, such as an MSPD measure or graph analysis, can contribute to an MHT claim through a justified correspondence with the objects and relations concerned.

Use `C.29` when the mathematical lens is relied on for the current claim. Use B.2 only after the holon identity claim is recovered and the ordinary existing-whole comparison leaves a whole-reidentification question.

#### B.2:4.8 - Keep Whole Identity, Evidence, Currentness, And Reliance Separate

Keep these five distinctions explicit:

- the existing whole and candidate new whole, their constituents, obtaining constructive relations, assemblies, characteristics, and identity rules are world-side objects and facts under their direct patterns;
- a B.2 whole-reidentification assertion is a C.2.1 episteme about those objects;
- evidence and assurance relations support or warrant the assertion's claim content but create neither whole and decide neither identity rule;
- use G.11 to determine whether the selected assertion or record edition is current for the receiving use;
- a person or system performing the receiving work decides whether to rely, decline to rely, defer, or reopen.

Evidence present or missing, and a current or stale record, can change what an evaluation returns and whether a person or system relies while performing receiving work. They cannot turn the same whole into a new whole or a new whole into the same one. Whether the existing whole continues or a new whole must be identified follows the direct identity and reidentification rules plus the actual construction facts. A.1 recognition of either candidate supplies no B.2 warrant and does not select B.2.

