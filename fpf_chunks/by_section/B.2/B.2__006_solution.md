---
chunk_kind: "child"
pattern_id: "B.2"
pattern_title: "Meta-Holon Transition - Whole Reidentification"
section_id: "B.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2/B.2__006_solution.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "B.2 — Meta-Holon Transition - Whole Reidentification"
  - "B.2:4 — Solution"
line_start: 36599
line_end: 36705
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.19"
  - "A.3.4"
  - "B.1"
  - "B.2"
  - "B.2.2"
  - "B.2.3"
  - "B.2.4"
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

1. Name the exact existing whole, its admitted kind, and its identity or reidentification rule.
2. Recover each changed delimitation, constituent, constructive part relation, assembly, supervision, objective, capability, characteristic, or temporal fact under its direct pattern. A cue word, profile field, measurement, or graph edge does not make the fact obtain.
3. Test whether those facts can be explained as a change of the same whole. If repair, maintenance, changed characteristics, phase coverage, method or work correction, measurement, or architecture-view correction is enough under the existing reidentification rule, keep that whole and stop B.2.
4. If the existing whole is not enough, identify the exact candidate new whole and execute the complete A.1 criterion. Recover its constituents, obtaining constructive relations, assembly, reidentification rule, and composition-grounded whole characteristic. Also show that the candidate's actual boundary, interfaces, relevant characteristics, and identity-preservation conditions satisfy the applicability and compatibility conditions of at least one governed larger-assembly construction method or rule under which it can remain a constituent. Then name its already admitted holon kind and satisfy the direct kind-specific criterion. If a required condition fails, the candidate fails A.1; if missing evidence or an unavailable dependency prevents a determination, evaluation returns `unknown`.
5. State the whole-reidentification claim: why the existing whole no longer carries the current subject claim and why the candidate new whole is the EntityOfConcern. This comparison does not itself create, admit, or classify either whole.
6. Materialize a trigger profile, explanation check, reidentification assertion, or record only when named receiving work must inspect, cite, compare, or preserve that claim.

The optional `MHTTriggerProfile`, `ExistingWholeExplanationCheck`, and `HolonReidentificationRecord` below are ordinary C.2.1 epistemes. Their content can designate exact wholes, facts, claims, and relation occurrences; the content fields are not world-side participants and supply no substitute for the preceding move.

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
| `changedCoordinationRelationRefs[]` | References to exact changed coordination relation occurrences. |
| `changedObjectiveClaimRef?` | `U.EpistemeRef` resolving to the exact objective-change claim. |
| `changedCapabilityClaimRef?` | `U.EpistemeRef` resolving to the exact capability-change claim. |
| `agencyThresholdClaimRef?` | `U.EpistemeRef` resolving to a current characteristic-space threshold claim. |
| `temporalConsolidationClaimRef?` | `U.EpistemeRef` resolving to the exact temporal-consolidation claim. |
| `evidenceRelationRefs[]` | References to exact evidence relation occurrences supporting the trigger claims. |
| `sourceUseRelationRefs[]` | References to exact source-use relation occurrences when a source is relied on. |

The profile's effective `U.ReferenceScheme`, any current `U.ClaimScope`, and an independently selected model-use structure can qualify this episteme under C.2.1 when its receiving use needs them. They do not identify either whole, become MHT trigger facts, or make any referenced relation obtain. A single cue warrants attention; it does not establish whole reidentification.

#### B.2:4.2 - ExistingWholeExplanationCheck

`ExistingWholeExplanationCheck` is a `U.Episteme` whose EntityOfConcern is the same existing whole. It compares the observed change claim with direct explanations that preserve that whole.

| Content field | Value kind and use |
|---|---|
| `observedChangeClaimRef` | `U.EpistemeRef` resolving to the exact observed-gain or observed-shift claim. |
| `candidateExplanationClaimRefs[]` | References to claims about better parts, corrected relations, measurement, source quality, method, work, temporal coverage, architecture view, capability, or functioning; each claim names its direct EntityOfConcern and governing pattern. |
| `explanationEvidenceRelationRefs[]` | References to the exact evidence relation occurrences supporting or defeating those explanations. |
| `existingWholeSufficiencyVerdictRef` | `U.EpistemeRef` resolving to the evaluation claim that the existing whole is or is not sufficient for the receiving use. |
| `remainingWholeReidentificationQuestionRef?` | `U.EpistemeRef` resolving to the residual question when the verdict is not sufficient. |

If the existing-whole verdict is sufficient, stop B.2 and use the direct governing pattern named by the selected explanation claim. The checklist does not perform the repair and its content fields do not create the referenced claims or relations.

#### B.2:4.3 - HolonReidentificationRecord

`HolonReidentificationRecord` is an optional `U.Episteme` whose EntityOfConcern is the exact new holon. Use it only when receiving work needs a durable account of why that new holon, rather than the prior whole, is the current EntityOfConcern. Candidate classification remains a separately governed judgment.

| Content field | Value kind and use |
|---|---|
| `existingWholeRef` | `U.HolonRef` resolving to the exact prior whole already recognized under an admitted holon kind. |
| `selectedTriggerProfileRef` | `U.EpistemeRef` resolving to the selected `MHTTriggerProfile`. |
| `existingWholeExplanationCheckRef` | `U.EpistemeRef` resolving to the completed check. |
| `resultHolonRef` | `U.HolonRef` resolving to the exact candidate new whole. |
| `resultHolonKindRef` | `U.KindRef` resolving to its exact admitted holon kind. |
| `resultHolonClassificationAssertionRef?` | `U.EpistemeRef` resolving, only when downstream work must inspect or cite the judgment, to a C.2.1 assertion that the candidate new whole satisfies the A.1 criterion under the stated admitted holon kind. |
| `wholeReidentificationClaimRef` | `U.EpistemeRef` resolving to the claim that the candidate new whole, rather than the prior whole, now carries the subject claim. |
| `changedClaimGoverningPatternRefs[]` | `U.EpistemeRef` values resolving to the direct patterns for each changed claim used in the rationale. |
| `evidenceRelationRefs[]` | References to exact evidence relation occurrences supporting the reidentification claim. |
| `sourceUseRelationRefs[]` | References to exact source-use relation occurrences when sources are relied on. |
| `mathLensUseRelationRefs[]` | References to exact C.29 lens-use relations when mathematical results bear on the claim. |

The record does not make the A.1 criterion true, admit a public kind, or create the candidate new holon. `E.24.UK` owns public-kind admission; A.1 owns world-side recognition; C.2.1 owns the optional classification assertion; exact evidence and assurance relations own its warrant. Publication of the record is another relation under the publication patterns.

#### B.2:4.4 - Candidate New Whole Reference And Kind

Use one `resultHolonRef : U.HolonRef` for the candidate new whole and one `resultHolonKindRef : U.KindRef` for its kind. `E.24.UK` must already have admitted that public kind, and the candidate new whole must satisfy the A.1 constructive criterion plus any kind-specific membership condition. Neither the references nor the record establish those facts.

When downstream work must inspect or cite the classification judgment, add the optional `resultHolonClassificationAssertionRef`. That C.2.1 assertion may report a governed evaluation of `true`, `false`, or `unknown`; its evidence, warrant, and G.11 currentness stay separate from world-side criterion satisfaction. B.2 still asks a different question: whether the existing whole can continue to carry the subject claim or a new whole must be identified.

Do not use `post*` field names as live governed names. They hide the candidate new whole and its kind and invite temporal shorthand. Name that whole and its admitted public kind; cite a classification assertion only when the receiving use needs that episteme.

#### B.2:4.5 - Agency Threshold

Agency is not a binary status and not a root kind. Treat agency as a characteristic-space threshold for one exact system, predicate, claim scope, and qualification window.

Use `A.13`, `A.19`, and `C.16` for the characteristic-space and threshold claim. Levin-line TAME work can discipline the multi-characteristic framing when agency evidence is relied on for the current claim. B.2 uses agency threshold only as one possible trigger in `MHTTriggerProfile`, and only when crossing the threshold changes closure, supervision, objective, or whole identity.

#### B.2:4.6 - Acting-System Participation

When a source describes a system changing another holon, recover acting-system participation and transformation separately.

Use `A.12` for acting-side externalization, `A.3.4` for bounded transformation, and `A.15.1` for work occurrence. A system changing another holon does not become that holon's super-holon, and no `U.Transformer` kind is created.

#### B.2:4.7 - Mathematical-Lens Separation

Graph, algebra, RG-like, MSPD, benchmark, scaling, and morphism language can bear on MHT recognition only as mathematical or analytical expression.

Use `C.29` when the mathematical lens is relied on for the current claim. Use B.2 only after the holon identity claim is recovered and the existing-whole explanation check leaves a whole-reidentification question.

#### B.2:4.8 - Keep Whole Identity, Evidence, Currentness, And Reliance Separate

Keep five results apart:

- the existing whole and candidate new whole, their constituents, obtaining constructive relations, assemblies, characteristics, and identity rules are world-side objects and facts under their direct patterns;
- a B.2 whole-reidentification assertion is a C.2.1 episteme about those objects;
- evidence and assurance relations support or warrant the assertion's claim content but create neither whole and decide neither identity rule;
- G.11 decides whether the selected assertion or record edition is current for the receiving use;
- receiving work decides whether to rely, decline to rely, defer, or reopen.

Evidence present or missing, and a current or stale record, can change what an evaluation returns and whether receiving work relies. They cannot turn the same whole into a new whole or a new whole into the same one. Whether the existing whole continues or a new whole must be identified follows the direct identity and reidentification rules plus the actual construction facts. A.1 recognition of either candidate supplies no B.2 warrant and does not select B.2.

