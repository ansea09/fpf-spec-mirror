---
chunk_kind: "child"
pattern_id: "A.6.1"
pattern_title: "U.Mechanism - Reusable Law-Governed Operation Declaration"
section_id: "A.6.1:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.1/A.6.1__006_archetypal-grounding.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "A.6.1 — U.Mechanism - Reusable Law-Governed Operation Declaration"
  - "A.6.1:5 — Archetypal Grounding"
line_start: 11859
line_end: 11923
dependencies:
  - "A.1"
  - "A.1.1"
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
  - "A.6.REL"
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

A clinical team declares a dose-adjustment mechanism whose operation has separately named drug, patient-mass, renal-function, and current-dose argument declarations and one proposed-dose-range result declaration, each with its exact meaning and ValueKind. The LawSet states dose bounds and preserved unit relations. Admission conditions state which measurements and qualification intervals make one calculation admissible. Applicability names the patient-population `U.ClaimScope`, qualification interval, selected `CHR:ReferencePlane` (normally `world` for the patient-side use claim), and clinical conditions under which the declaration is used.

An exact claim-bearing clinical-protocol episteme is a `U.MethodDescription` only when it describes one admitted `U.Method` and satisfies A.3.2; its publication form and carrier remain separate. One clinician's treatment occurrence is work only when the A.15.1 occurrence basis obtains. Exact laboratory measurement values may be bound as arguments of one admitted calculation application, while the measurement and evidence relations that warrant their use remain separate. The returned dose-range binding does not say that the calculation produced or constituted the patient, prescription, or result episteme. None of those neighboring values becomes the mechanism episteme.

Practical payoff: a changed protocol presentation or one anomalous treatment does not silently rewrite the declared calculation laws.

#### A.6.1:5.3 - Manufacturing: fixture selection

A machining team declares a fixture-selection mechanism. Its operations filter candidate fixtures, compare admissible loading envelopes, and return a non-dominated candidate set. Laws preserve units and the partial order over constraints. The admission predicate evaluates true only when current workpiece geometry, machine envelope, and measurement qualification interval are available.

The machinist's setup method and the dated setup work remain separate. A fixture is a system. A selector implementation may realize the mechanism for a stated scope and interval.

Practical payoff: the team can replace the implementation without turning a scalar convenience score into the declared ordering law.

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

A project repeatedly evaluates the A.1 holon-recognition criterion. Its exact mechanism edition declares operation `recognizeAdmittedHolonCandidate` with these meanings:

| Declaration-local meaning | Exact declaration |
|---|---|
| `candidate` argument | one exact `U.Entity` being evaluated |
| `admittedHolonKind` argument | one already admitted holon-kind value whose direct pattern supplies any kind-specific condition |
| `recognitionCriterion` argument | one exact criterion-bearing `U.Episteme`, designated through a governed reference |
| `criterionParameter` argument, repeated only as declared | one exact value of each criterion-specific ValueKind needed by this operation application |
| `interpretationBasis` argument | one exact separately identified episteme containing the selected interpretation basis, designated through a governed reference |
| `recognitionJudgment` result | one value of the declaration-local finite `RecognitionJudgmentValue = {true, false, unknown}` |

`RecognitionJudgmentValue` is one local finite `U.Kind` under C.3, used here as the operation's RangedValueKind; its membership rule admits exactly the three values shown. It is not a public U-kind, universal claim-status algebra, candidate state, evidence status, episteme-currentness value, or receiving-work disposition. The argument and result rows are A.6.1 declarations, not A.6.5 SlotSpecs.

For one exact application, the candidate binding designates Pump #37, the kind binding designates already admitted `U.System`, the criterion binding resolves to one exact criterion-bearing episteme whose claims contain the current A.1 criterion and `U.System` clause, declared parameter bindings designate the exact installation-compatibility and reidentification values used by the evaluation, and the interpretation-basis binding resolves to the exact separately identified basis used for that application. Suppose an unavailable dependency prevents the currently bound argument values and available governed evidence from determining whether one required fastening relation obtains. The result binding is then the value `unknown`. The application did occur; Pump #37's world-side satisfaction or failure did not change; and `unknown` is not an admission refusal.

Exact dated classification work remains a separate Work occurrence admitted under `U.Work` by A.15.1. Exact `performedBy -> U.RoleAssignment`, actual `enactsMethod -> U.Method`, temporal, `executedWithin -> U.System`, affected-candidate, concrete application-binding, and performed resource-use relations involving that occurrence obtain independently when their claims are current. A separate assertion may designate the Work occurrence and cite `workContinuityPolicyRef`; any materialized classification-assertion or evaluation-result episteme remains under C.2.1. Evidence and assurance support or warrant its claim content through their own relations, and G.11 governs edition currentness. The result binding alone establishes none of work, evidence, warrant, episteme identity, world-side criterion satisfaction, or B.2 whole reidentification.

Practical payoff: another evaluation can reuse the same typed operation while binding another candidate or basis, and evidence loss can change the returned value to `unknown` without rewriting the candidate or criterion.

