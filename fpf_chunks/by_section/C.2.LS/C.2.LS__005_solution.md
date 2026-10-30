---
chunk_kind: "child"
pattern_id: "C.2.LS"
pattern_title: "Language-State Facet Profile: Publish Readings and Use Conditions Together"
section_id: "C.2.LS:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.LS/C.2.LS__005_solution.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "C.2.LS — Language-State Facet Profile: Publish Readings and Use Conditions Together"
  - "C.2.LS:4 — Solution"
line_start: 53016
line_end: 53077
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.18"
  - "A.19"
  - "B.4.1"
  - "B.5.2.0"
  - "C.2.1"
  - "C.2.2a"
  - "C.2.3"
  - "C.2.4"
  - "C.2.4-C.2.7"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "E.18"
  - "E.24.PUB"
  - "F.9"
  - "F.9.1"
keywords:
  - "articulation"
  - "closure"
  - "facet profile"
  - "local thresholds"
  - "representation factors"
  - "source and use claims"
---

### C.2.LS:4 - Solution
A language-state facet profile records the selected readings and use conditions about one identified episteme edition. Characteristic readings use the declared language-state chart over `U.CharacteristicSpace`; a separate relation account keeps its own predicates. Use C.2.2a:0 and :4.2–4.5 to select the needed facets, obtain readings and grounds, and identify any conditions used by the receiving action. The profile brings those results together. Its fields can refer to existing readings or to the source and use account supplied by C.2.6. A reading reference makes its Characteristic, Scale, value and assessment scope recoverable; a reference to a source or use claim makes the predicate, participants and grounds recoverable. Select the applicable fields from:

- `formalityRef` -> the expression-property assessment governed by `C.2.3`, including its selected basis and any justified local ordered summary
- `articulationExplicitnessRef` -> the articulation reading governed by `C.2.4`
- `languageStateClosureDegreeRef` -> the closure reading governed by `C.2.5`
- `languageStateAnchoringModeRef` -> the source, evidence, access or action-condition claims selected under `C.2.6`; cite their account or an explicitly defined local summary with its criterion
- `languageStateRepresentationFactorBundleRef` -> the selected representation-factor readings governed by `C.2.7`
- `thresholdRefs?` -> context-local threshold declarations over the named facets
- `routeNotes?` -> informative notes that help interpret routing or reopening decisions

`C.2.LS` therefore defines only the **profile bundle**; it defines neither an individual characteristic nor a trajectory. A formality assessment or representation-factor bundle can contain several Characteristics. If placed in a CharacteristicSpace, each of those Characteristics receives its own declared Scale and slot; the reference to the assessment is not itself a Coordinate. The C.2.6 account is likewise separate from those slots; a local summary needs its own declared Characteristic and Scale before it can supply a Coordinate. `A.18/A.19` supply characteristic semantics, `A.16` defines admissible moves, and `E.18` governs an independently selected TransformationFlowStructure.

#### C.2.LS:4.0a - Kind and profile-bundle boundary

The optional `LanguageStateFacetProfile` form expresses an ordinary C.2.1 assessment account. The episteme edition being assessed is its EntityOfConcern. Its claims give the selected readings under their chart and scope, their grounds, any required source or use conditions, and any thresholds used in the assessment. C.2.1 governs the account's identity; E.24.PUB governs its expression and publication. No additional profile individual or dependent U-kind is needed for this use.

Distinguish the **selection of facets** from the **filled assessment**. A selection identifies the Characteristics and Scales in the A.19 basis and any separate C.2.6 questions needed by the receiving use. The same selection can be used for several assessments, just as the same record form can express them. A filled assessment states readings about its identified episteme edition and scope; changing a reading or a stated relation changes that claim content even if every definition reference stays the same. A threshold predicate has its own by-value identity under A.19:5.1.8. Reusing readings with a different predicate requires a new evaluation of that predicate, while the readings can remain unchanged.

For reuse, recover the assessed edition, chart meanings, scope, readings and relied-on grounds from the profile or its applicable cited source. Recover a threshold or a separate source or action condition and its receiving use when the conclusion relies on it. Saying which of the selection, readings, threshold or whole assessment is being reused prevents an unchanged label from concealing changed content. Rearranging the same claims in a dashboard or table leaves their meanings available under the same account-identity rule.

**Choose direct readings or a shared profile.**

Use direct facet readings when they already provide the inputs for the receiving judgement. A shared profile is useful when several readings and their conditions must be interpreted, compared or reused together: the reader can recover their joint scope and see which of them a local threshold actually uses. This saves reassembling dispersed references. The profile adds no stronger warrant to the readings. Keep it partial when the task needs only part of the facet family, and reuse an existing applicable assessment rather than writing another.

#### C.2.LS:4.1 - Contribution boundary
`C.2.LS` defines only profile composition and requires the language-state facets to remain explicit and non-collapsed. It does **not**:

- redefine `F`;
- invent a universal formality progression or an undeclared local summary;
- redefine the scale semantics of `AE`, `CD` or the representation factors in `C.2.7`, or replace the direct predicates recovered through C.2.6;
- define reopen/backoff moves;
- define endpoint classification or bridge kinds.

#### C.2.LS:4.2 - Threshold publication discipline
Any threshold used to choose a next question, constrain an admissible move, or begin `A.6.P` recovery shall be published on explicit named facets in the profile. Do not describe hidden sub-levels of `F` when the real issue is articulation, closure, a source or use condition, or the representation-factor bundle. A required relation is tested under its direct predicate; only a declared Characteristic reading participates as a slot value in an A.19 threshold.

#### C.2.LS:4.2.a - Local profile-reading witness
For this pattern, a published facet profile is reviewable when:

- the assessed episteme edition, chart, scope, selected refs, readings and any relied-on source or use claims are explicit or recoverable from a cited applicable upstream publication;
- any threshold-bearing use names the facet whose threshold is being invoked;
- route notes or local overlays remain informative and visibly docked to the explicit facet bundle;
- and any claimed move, Bridge, gate state or downstream result retains its own governing definition and test.

A polished label, one strong facet, or one memorable route note does not by itself yield an admissible profile reading. The profile remains conformant only when the named facets stay explicit and decomposable.

#### C.2.LS:4.3 - Composite readings
A language-state judgement may be composite, but the composite shall be decomposable. For example, a cue may be:

- low `AE`,
- medium `CD`,
- derived from an identified trace, with any evidential use separately qualified,
- and representation-wise mixed rather than purely symbolic.

A conforming profile makes this decomposition visible rather than hiding it under one stage label such as "early" or "raw".

#### C.2.LS:4.4 - Corridor map note
`C.2.LS` participates in the current `Language-State & Semantic Routing Corridor`, but contributes only the thin facet-profile bundle. Readers who need one map of the full language-state pattern set should read the corridor note in `C.2.2a`.

That map does not change this boundary: `C.2.LS` still does not define cue preservation, route-bearing publication, prompt entry, or downstream endpoint use.

