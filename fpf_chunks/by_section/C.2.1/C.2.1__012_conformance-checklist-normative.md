---
chunk_kind: "child"
pattern_id: "C.2.1"
pattern_title: "U.Episteme: Constitution, Empirical Grounding, and Edition Relations"
section_id: "C.2.1:11"
section_title: "Conformance Checklist  (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.1/C.2.1__012_conformance-checklist-normative.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "C.2.1 — U.Episteme: Constitution, Empirical Grounding, and Edition Relations"
  - "C.2.1:11 — Conformance Checklist  (normative)"
line_start: 42409
line_end: 42426
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.14"
  - "A.2.6"
  - "A.22"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.0"
  - "A.6.1"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.5"
  - "A.6.REL"
  - "A.7"
  - "B.3"
  - "C.13"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "C.3.2"
  - "E.10.D2"
  - "E.13"
  - "E.17"
  - "E.17.0"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.9"
  - "G.11"
  - "U.Episteme"
  - "U.MethodDescription"
  - "U.Signature"
  - "U.View"
keywords:
---

### C.2.1:11 - Conformance Checklist  *(normative)*

1. **Episteme identity.** Claim content, exact EntityOfConcern, and effective `U.ReferenceScheme` are recoverable, and the text states what changes each discriminator. A dependent episteme kind such as `U.MethodDescription` or `U.View` adds a governed membership judgment for the same individual, not another identity discriminator.
2. **Direct constitution and case judgment.** `EpistemeConstitutionRelation` has its three identified participants, obtaining predicate, and participant-determined occurrence-identity rule. C.2.1 defines that rule; current case facts satisfy or fail the predicate; an assertion states affirmative or negative polarity; and evaluation or evidence use states reliance only when needed. Designate an occurrence only after positive case facts and the identity rule individuate it.
3. **Declaration identity and Slot discipline.** Each of the three named relation declarations is first a C.2.1 episteme whose exact EntityOfConcern is its direct relation kind; the fixed `A.6.0` predicate gives that same individual `U.Signature` membership and `RelationSignature` is its relation-facing use. Its complete declaration carries the direct predicate, occurrence identity, applicability, exact A.6.5 SlotSpecs, and only actual dependencies and provided names. Signature-local SlotKinds never become participants, and a one-off assertion needs no signature or manifest.
4. **Classification discipline.** `A.1` governs recognition under an admitted holon kind, `C.3.2` governs local-kind membership, and `E.24.UK` governs public U-kind admission. A separately current classification assertion is a C.2.1 episteme about the exact candidate; it states affirmative or negative polarity for the exact classification predicate and keeps supported, refuted, or unresolved reliance separately governed. It neither creates the candidate nor changes the kind's admission.
5. **Empirical-grounding discipline.** `GroundingHolonSlot` occurs only inside `EpistemeEmpiricalGroundingRelationSignature`. Each occurrence names one exact nonempty covered claim subgraph and maps every empirical claim in it to the required current direct observation, intervention, measurement, or test relations involving the grounding holon. Unlisted claims receive no grounding from that occurrence. One occurrence is reidentified from the episteme, covered claim subgraph, grounding holon, and maximal continuous interval during which the complete coverage predicate is true; demonstrated coverage failure followed by restoration yields another occurrence. Evaluation counts in the empirical base only when its exact direct relation and use in the test are stated; otherwise evaluation and evidence support or challenge an assertion. Availability or loss of a report, store, or Work log alone neither makes nor unmakes grounding.
6. **Edition discipline.** `EpistemeEditionRelation` has exactly the earlier and later epistemes as participants and is acyclic in that direction. Positive continuity requires exact source use, an applicable edition policy or rule, and preserved and deliberately changed claim, EntityOfConcern, and scheme features satisfying that rule. Fork, translation, retargeting, and independent reconstruction are explicit failure branches. Work, Method, provenance, and change facts supply case facts but no label makes continuity true.
7. **View and neighboring-relation discipline.** C.2.1 identifies epistemes; E.17.0 alone tests the conformance of fixed E to fixed P and the resulting same-individual `U.View` membership. One named describing use may select one exact viewpoint P, but that selection creates no context value, selects no view, and remains separate from A.6.3 source-to-receiving construction. Several views remain a plurality. Recover a C.13 collection only when the use depends on that plurality as a collection, and an A.22 structure only when it depends on their organization. Cross-view claims use the pattern for their direct subject relation or return an exact blocker naming the participants, required predicate, use, and missing defining or constraining pattern. Use E.17 for view or publication form and E.24.PUB for publication occurrence, form, and carrier, not for view membership or correspondence.
8. **Description boundary.** The EntityOfConcern and any Description episteme about it remain distinct, including self-description and episteme-about-episteme cases.
9. **Specification use.** Specification force is admitted only when the E.10.D2 conditions obtain: checkable claims and a named harness or validation relation. A selected viewpoint is preserved or updated only for the named describing use whose reliance depends on it. Naming and appearance do not grant specification force.
10. **Agency, work-result, and identity-inception boundary.** Only systems perform authoring, evaluation, revision, publication, viewing, query, redrawing, and use work. `A.6.1` declares typed argument and result positions; neither a position nor its binding says when the bound entity first existed. When a current claim asks that question, the subject's direct inception pattern must define the predicate and identity rule, and the exact work and change facts must satisfy them. If no such governor exists, return one `missing-governor` blocker naming the entity, facts, required predicate, and receiving use. Otherwise do not open the inception boundary. No morphism, heading, representation, form, bare A.6.1 `result`, generic work result, or universal production relation supplies that fact.
11. **Publication boundary.** Episteme, publication occurrence, publication form, view, and carrier keep separate identities. Plain `published episteme` names a contingent relation use, not another durable kind.
12. **Representation boundary.** Tuple components, graph elements, schema fields, and notation tokens remain representation elements. An explicit correspondence may relate one to an independently recovered object without identifying the two or changing the represented direct relation's participants.
13. **Transformation and Bridge-use boundary.** A morphing, viewing, or retargeting declaration states which C.2.1 identity discriminators are preserved or changed and names the exact correspondence or retargeting relation used. For cross-context sense use, F.9 separately establishes the exact Bridge; one C.2.1 assertion about that Bridge carries `<u,d,r,t>` and polarity; A.10 handles ordinary evidence reliance; B.3 adds a result only when an actual named assurance claim is current; and the direct receiver defines or tests any actual Work, assertion, publication, relation, or operation application. The mathematical morphism performs no work, and none of these objects authorizes another.
14. **Recursive assurance.** Self-reference and meta-description do not form a minimal justification cycle; assurance terminates in independently governed evidence, observation, or formal derivation.
15. **Minimum current object.** Readable prose adds no object beyond the current use's dependency and states the direct relation to an already recoverable object.

