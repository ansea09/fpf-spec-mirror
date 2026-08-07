---
chunk_kind: "child"
pattern_id: "A.6.1"
pattern_title: "U.Mechanism - Reusable Law-Governed Operation Declaration"
section_id: "A.6.1:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.1/A.6.1__006_archetypal-grounding.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "A.6.1 — U.Mechanism - Reusable Law-Governed Operation Declaration"
  - "A.6.1:5 — Archetypal Grounding"
line_start: 12460
line_end: 12565
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.19"
  - "A.2.6"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.1"
  - "A.3.2"
  - "A.6.0"
  - "A.6.5"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.3"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "E.10"
  - "E.10.ARCH"
  - "E.20"
  - "E.24.PUB"
  - "F.18"
  - "F.9"
  - "G.11"
keywords:
  - "AdmissibilityConditions"
  - "LawSet"
  - "OperationAlgebra"
  - "U.Mechanism"
  - "application binding"
  - "operation application"
  - "operation declaration"
  - "realization"
---

### A.6.1:5 - Archetypal Grounding

#### A.6.1:5.1 - Physical modeling: thermal connector operations

A physical-modeling team repeatedly uses a thermal connector operation family. The mechanism episteme declares named temperature and heat-flow argument and result meanings with their exact ValueKinds, connection operations, equality and conservation laws, application identity and extent rules, and admission conditions for unit compatibility and steady-state conduction. Applicability names a `U.ClaimScope` over the modeled systems, the use interval, selected `CHR:ReferencePlane = conceptual` for these model-side connector claims, and the steady-state conduction condition; a component port is a modeled participant or locus, not a `CHR:ReferencePlane` value.

One equation-based model can realize that declaration for simulation use. The modeled heater and pipe remain physical systems. Solver work, validation measurements, and a connection diagram remain work, evidence, and representation under their own patterns.

Practical payoff: another model can be compared against the same operation and law declaration without treating equation order, solver choice, or a diagram as mechanism identity.

#### A.6.1:5.2 - Clinical work: dose-adjustment operations

A clinical team declares a dose-adjustment mechanism over one common patient subject and one common dose-value domain. The headline fields and the heterogeneous operation positions connect as follows; every named ValueKind must already resolve under the effective reference scheme, and this example admits no new U-kind.

| Declaration locus | Filled value and connection |
|---|---|
| `SubjectKind` | `Patient`; required argument `patient` has `ValueKind = Patient` and identifies the patient for whom one calculation is proposed. |
| `RangedValueKind` | `DoseValue`; required argument `currentDose` has `ValueKind = DoseValue`, and the LawSet states the dose bounds and unit-preserving rules over that domain. |
| optional `ResultKind` | `DoseRange`; result `proposedDoseRange` has `ValueKind = DoseRange`. This field is present because the returned range is not one `DoseValue`. If the operation instead returned one `DoseValue`, omit the separate `ResultKind`; if several operations returned unrelated local kinds, keep those kinds in their own result declarations rather than forming a union. |
| other operation-local arguments | `drug : Drug`, `patientMass : MassValue`, and `renalFunction : RenalFunctionMeasure`; these exact ValueKinds constrain this operation but do not replace or widen the family-level subject and range. |

Admission conditions state which measurements and qualification intervals make one calculation admissible. Applicability names the patient-population `U.ClaimScope`, qualification interval, selected `CHR:ReferencePlane` (normally `world` for the patient-side use claim), and clinical conditions under which the declaration is used.

An exact claim-bearing clinical-protocol episteme is a `U.MethodDescription` only when it describes one admitted `U.Method` and satisfies A.3.2; its publication form and carrier remain separate. One clinician's treatment occurrence is work only when the A.15.1 occurrence basis obtains. Exact laboratory measurement values may be bound as arguments of one admitted calculation application, while the measurement and evidence relations that warrant their use remain separate. The returned dose-range binding does not say that the calculation produced or constituted the patient, prescription, or result episteme. None of those neighboring values becomes the mechanism episteme.

Practical payoff: a changed protocol presentation or one anomalous treatment does not silently rewrite the declared calculation laws.

#### A.6.1:5.3 - Manufacturing: fixture selection

A machining team declares a fixture-selection mechanism. Its operations filter candidate fixtures, compare admissible loading envelopes, and return a non-dominated candidate set. Laws preserve units and the partial order over constraints. The admission predicate evaluates true only when current workpiece geometry, machine envelope, and measurement qualification interval are available.

The machinist's setup method and the dated setup work remain separate. A fixture is a system. A selector implementation may realize the mechanism for a stated scope and interval.

**Positive realization in plain terms.** `FixtureSelectorRuntime-12-E3` realizes exact mechanism episteme `FixtureSelectionMechanism-E3` for `Cell7FixtureSelection-Q3` during `[2026-07-01T08:00Z, 2026-07-19T14:32Z)`. During that interval the independently identified runtime provided `filterCandidates`, `compareLoadingEnvelopes`, and `returnNonDominatedSet`; every admitted use required current workpiece geometry, the current machine envelope, and a current measurement-qualification interval; and its results preserved the declared unit and constraint-partial-order laws.

| Realization position or test | Filled value |
|---|---|
| declared mechanism | `FixtureSelectionMechanism-E3 : U.Mechanism`, the exact mechanism episteme containing those operations, laws, admission conditions, and Applicability |
| realizing entity | `FixtureSelectorRuntime-12-E3 : U.System`; the runtime keeps its system kind |
| realization scope | `Cell7FixtureSelection-Q3 : U.ClaimScope`, covering fixture selection for machining cell 7 under the named machine-envelope and qualification conditions |
| realization predicate | the runtime provides all three declared operations, enforces `GeometryCurrent`, `MachineEnvelopeCurrent`, and `MeasurementQualificationCurrent` before an application is admitted, and preserves `UnitPreservationLaw` and `ConstraintPartialOrderLaw` in returned candidate sets |
| derived extent | the maximal continuous interval `[2026-07-01T08:00Z, 2026-07-19T14:32Z)` over which those facts obtain |

This replay needs one occurrence distinguished from its failing successor, so its identity is `<FixtureSelectionMechanism-E3, FixtureSelectorRuntime-12-E3, Cell7FixtureSelection-Q3, [2026-07-01T08:00Z, 2026-07-19T14:32Z)>`. The interval is derived, not a fourth writable participant.

**Nearest failing variant.** `FixtureSelectorRuntime-12-FastPath-E4 : U.System` exposes the same three operation names but accepts a loading-envelope comparison when `MeasurementQualificationCurrent` is false. It therefore bypasses one declared admission condition and does not realize `FixtureSelectionMechanism-E3` for that scope, even if its returned candidate set happens to match E3 in one run. A missing audit-log segment for E3 instead reopens evidence and warrant under A.10. Without demonstrated cessation or bypass, that gap does not make the world-side realization predicate false or split its occurrence, although the project may have to withhold its positive assertion until warrant recovers. Demonstrated cessation followed by later restored conformity would create a later maximal-continuous realization occurrence.

Practical payoff: the team can replace the implementation without turning a scalar convenience score into the declared ordering law, and it can reject a look-alike implementation without rewriting the declaration.

#### A.6.1:5.4 - FPF scope and normalization declarations

A.2.6 scope operations and A.19 normalization operations may use the `U.Mechanism` declaration shape when their direct patterns need reusable operations, laws, admission conditions, and typed results. A.2.6 and A.19 retain their domain semantics. A.6.1 supplies the declaration and realization distinctions; it does not redefine scope or comparison.

Practical payoff: shared mechanism form does not create a second governing locus for scope or normalization meaning.

#### A.6.1:5.5 - Publication operations

E.24.PUB may cite a mechanism declaration for operations that assemble, validate, and expose a publication package. The mechanism episteme declares those operations, laws, and admission conditions. The dated publication work, resulting publication use, information carrier, evidence, and currentness relations remain with their direct patterns.

Practical payoff: reusable publication-operation semantics do not turn a released package or its carrier into the mechanism.

#### A.6.1:5.6 - Reduced ordinary use

An engineer states, "this conversion is admitted only for values in the calibrated interval." No later claim reuses an operation family, compares declarations, identifies an actual application, or refers to a realization occurrence. The direct sentence and its governing characteristic and measurement patterns are enough. No mechanism episteme is opened.

Practical payoff: precision grows only when a receiving use needs reusable mechanism identity or an exact application binding.

#### A.6.1:5.7 - Recognition evaluation: Pump #37

A project repeatedly evaluates the A.1 holon-recognition criterion. In ordinary language, one bounded evaluation act applies the selected criterion to Pump #37 and returns `true`, `false`, or `unknown`. For this replay, resolving `HolonRecognitionMechanism-E1_Ref` under its effective reference scheme returns exact mechanism episteme `HolonRecognitionMechanism-E1`; neither label nor suffix establishes an edition relation. That episteme has `SubjectKind = U.Entity`, `RangedValueKind = RecognitionJudgmentValue`, no separate `ResultKind`, and operation `recognizeAdmittedHolonCandidate`.

The operation declares these meanings:

| Declaration-local meaning | Exact declaration |
|---|---|
| `candidate` argument | one exact `U.Entity` being evaluated |
| `admittedHolonKind` argument | one already admitted holon-kind value whose direct pattern supplies any kind-specific condition |
| `recognitionCriterion` argument | one exact criterion-bearing `U.Episteme`, designated through a governed reference |
| `criterionParameter` argument, repeated only as separately declared | one exact value of the parameter-specific ValueKind needed by this operation application |
| `interpretationBasis` argument | one exact separately identified episteme containing the selected interpretation basis, designated through a governed reference |
| `recognitionJudgment` result | one value of the declaration-local finite `RecognitionJudgmentValue = {true, false, unknown}` |

`RecognitionJudgmentValue` is one local finite `U.Kind` under C.3, used here as the operation's `RangedValueKind`; its membership rule admits exactly the three values shown. It is not a public U-kind, universal claim-status algebra, candidate state, evidence status, episteme-currentness value, or receiving-work disposition. The argument and result rows are A.6.1 declarations, not A.6.5 SlotSpecs.

For this exact mechanism episteme, the declaration-local designation, cardinality, and binding predicates are:

| Member | ValueKind and designation rule | Cardinality | Declaration-local binding predicate |
|---|---|---:|---|
| `candidate` | `U.Entity`; an exact `U.EntityRef` must resolve to the entity | exactly one | `recognitionCandidateBound(P, E)` holds only when application `P` actually evaluates `E` as its candidate |
| `admittedHolonKind` | one already identified C.3 `U.Kind` value, carried by value | exactly one | `recognitionKindBound(P, K)` holds only when `P` evaluates the candidate against admitted kind `K` |
| `recognitionCriterion` | `U.Episteme`; an exact `U.EpistemeRef` must resolve to the selected criterion-bearing episteme | exactly one | `recognitionCriterionBound(P, C)` holds only when `P` applies the claims in `C` as its recognition criterion |
| `criterionParameter[constructionFacts]` | `U.Episteme`; an exact `U.EpistemeRef` resolves to the candidate-facts episteme used by the evaluation | exactly one | `recognitionParameterBound(P, constructionFacts, V)` holds only when `P` uses `V` under that meaning |
| `criterionParameter[reidentificationRule]` | `U.Episteme`; an exact `U.EpistemeRef` resolves to the reidentification-rule episteme used by the evaluation | exactly one | `recognitionParameterBound(P, reidentificationRule, V)` holds only when `P` uses `V` under that meaning |
| `interpretationBasis` | `U.Episteme`; an exact `U.EpistemeRef` must resolve to the selected basis episteme | exactly one | `recognitionBasisBound(P, B)` holds only when `P` uses `B` as its interpretation basis |
| `recognitionJudgment` | `RecognitionJudgmentValue`, carried by value | exactly one | `recognitionJudgmentReturned(P, J)` holds only when `P` returns `J` under this result meaning |

These predicate names are local to `HolonRecognitionMechanism-E1`; they do not admit public binding relation kinds. `Pump_37_Ref` can be type-correct without a binding: the candidate predicate is current only when the exact application actually uses its resolved referent under the `candidate` meaning. The same rule applies to each argument, and a result predicate is current only after the application returns that value.

For this mechanism episteme, `ApplicationPredicate(P)` holds only when bounded evaluation act `P` fixes exactly one value for every required argument above, applies `recognizeAdmittedHolonCandidate` from `HolonRecognitionMechanism-E1`, and returns exactly one `RecognitionJudgmentValue`. Its `ApplicationExtentRule` sets the maximal extent from the moment all required argument bindings are fixed and evaluation begins through the terminal judgment return. Its `ApplicationIdentityRule` reidentifies one application by `<HolonRecognitionMechanism-E1, recognizeAdmittedHolonCandidate, independently grounded evaluation-act locus, maximal application extent>`. A later invocation is another application even with the same bound values. A trace token or reused work label can designate an act but cannot merge the two.

For the worked case, `Pump37RecognitionApplication-2026-07-21T100000Z` designates the evaluation act that began at 10:00:00 and returned at 10:00:04. It used `Pump_37_Ref -> Pump_37 : U.Entity`, admitted kind `U.System`, `A1-Holons-Criterion-E1_Ref`, `Pump37-Construction-Facts-E1_Ref`, `Pump37-Reidentification-Rule-E1_Ref`, and `Pump37-Interpretation-Basis-E1_Ref`. The six argument-binding predicates have maximal continuous extents from 10:00:00 through the terminal return. A required fastening-relation fact could not be resolved during this act, so the bound values could determine neither satisfaction nor failure. The act returned `unknown`; the extent of `recognitionJudgmentReturned(Pump37RecognitionApplication-2026-07-21T100000Z, unknown)` is the terminal return event at 10:00:04 and does not begin earlier. The application did occur; Pump #37's world-side satisfaction or failure did not change; and `unknown` is not an admission refusal.

If the project also claims that dated classification work occurred, identify a separate Work occurrence `W` under A.15.1. Name the admitted System `S` that performed it and the obtaining assignment `RA` under which it performed; verify `S = RA.HolderSystemSlot`, assignment coverage, and F.6 `performedUnderAssignment(W, RA)`, then state the Work temporal extent and the actual `enactsMethod -> U.Method` and `executedWithin -> U.System` relations. The candidate application binding above can establish Pump #37's participation in the application; add a separate work-to-candidate or resource-use claim only when its declared predicate obtains, and add `workContinuityPolicyRef` only when an identity or segmentation question needs it. Any materialized classification-assertion or evaluation-result episteme remains under C.2.1. Evidence and assurance support or warrant its claim content through their own relations, and G.11 governs edition currentness. The result binding alone establishes none of work, evidence, warrant, episteme identity, world-side criterion satisfaction, or B.2 whole reidentification.

Practical payoff: another evaluation can reuse the same typed operation while binding another candidate or basis, and evidence loss can change the returned value to `unknown` without rewriting the candidate or criterion.

