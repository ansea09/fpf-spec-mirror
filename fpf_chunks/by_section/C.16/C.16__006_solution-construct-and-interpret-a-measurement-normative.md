---
chunk_kind: "child"
pattern_id: "C.16"
pattern_title: "Measurement & Metrics Characterization (MM‑CHR)"
section_id: "C.16:5"
section_title: "Solution - Construct and interpret a measurement (Normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16/C.16__006_solution-construct-and-interpret-a-measurement-normative.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "C.16 — Measurement & Metrics Characterization (MM‑CHR)"
  - "C.16:5 — Solution - Construct and interpret a measurement (Normative)"
line_start: 49935
line_end: 50018
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.6.1"
  - "B.1.6"
  - "B.3"
  - "C.11"
  - "C.16.P"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "G.11"
  - "G.4"
  - "G.6"
keywords:
  - "C.2.1 result episteme"
  - "Characteristic"
  - "Level/Coordinate"
  - "Scale"
  - "Scale order"
  - "Unit"
  - "actual bindings"
  - "bounded later use"
  - "calibration"
  - "comparability"
  - "dated measurement work"
  - "indication-producing procedure"
  - "input/output quantities"
  - "measurand"
  - "measurement result"
  - "measurement subject"
  - "measurement-model construction"
  - "method"
  - "model"
  - "provenance"
  - "uncertainty"
---

### C.16:5 - Solution - Construct and interpret a measurement (Normative)

To develop a measurement model, begin with §§5.1-5.4. A proposed relation can supply a conditional calculation or expose an ambiguity before any measurement is performed. An existing model that answers the question can be used directly.

When interpreting a performed measurement, recover one ordinary direct sentence:

> Dated measurement work `W` applied method `M` to measurand `x`, using model `f`, calibration basis `K`, and actual input bindings `X`, and obtained output quantity value `y` with stated uncertainty `u`; episteme `E` states that measurement result under its declared Characteristic, Scale, unit, time stance, and interpretation basis.

If a fact needed for that interpretation is unavailable, state which conclusion remains undetermined and what information could resolve it.

#### C.16:5.1 - Name the measurand and measurement subject

**M‑SUB‑1.** Name the measurand: the quantity or characteristic intended to be measured. When FPF uses a non-quantity Characteristic, name the exact subject and the Characteristic whose Scale position is being attributed.

**M‑SUB‑2.** Preserve arity. An entity Characteristic has one subject; a relation Characteristic has the exact ordered tuple required by A.17. A relation reading is not silently rewritten as a unary property of one participant.

**M‑SUB‑3.** Distinguish the measurand from the actual subject state. A measurement result attributes values under a method and model; it does not make the physical, social, architectural, or epistemic state identical to the result episteme.

#### C.16:5.2 - Fix Characteristic, Scale, unit and time stance

**M‑CSLC‑1.** One `U.DHCMethod` binds exactly one Characteristic to exactly one Scale. A discrete reading names its Level; another reading names its Coordinate or value on that Scale.

**M‑CSLC‑2.** When units apply, name the quantity kind and presentation Unit. Conversions are admissible only when they preserve the quantity kind and the Scale supports the operation. Nominal and ordinal labels do not acquire interval or ratio arithmetic by being encoded as numbers.

**M‑CSLC‑3.** Use the Scale's order to interpret the Characteristic: a higher temperature value means hotter. When a later evaluation asks which value is preferable, state its preference under A.17/A.18. A measurement or magnitude comparison needs no preferred direction.

**M‑CSLC‑4.** State the time stance: instantaneous or as-observed at `T`, aggregated over window `W`, or another exact temporal basis. A later value does not silently replace an earlier result.

#### C.16:5.3 - Separate method, description, model, calibration, and work

**M‑METH‑1.** `MeasurementMethod` is one exact `U.Method`. Its `U.MethodDescription` may state generic participants, parameters, effects, and measurement conditions; it contains no actual-participant slots and does not claim that measurement occurred.

**M‑MODEL‑1.** `MeasurementModel` relates input values and relevant influences to the values attributed to the measurand. In quantity measurement, these are input, influence and output quantities. Identify the model version, assumptions, corrections and domain of validity. Recover what its formula, software function or other expression represents. Section :5.3.1 supplies the construction when that relation is missing or unsuitable.

**M‑CAL‑1.** Name the calibration basis required for the use: reference standard or comparison basis, dated calibration work and result when current, calibration coefficients or corrections, applicable interval, and uncertainty contribution. A calibration certificate or ledger row cites these facts; it does not establish them by being stored.

**M‑WORK‑1.** `MeasurementWork` is one exact dated `U.Work`. First recover every actual performer's A.13 core for the measurement action, including the same obtaining assignment; then independently admit the Work under A.15.1 from its performance history, at least one obtaining `enactsMethod` relation, temporal extent, and at least one obtaining locally declared containing-system relation. Add F.6 afterward only when the measurement claim also needs precise assignment-bound attribution. Name the exact measurand through its direct subject relation or an A.6.1 operation-application binding. Name another enacted Method, resource, or concrete participant only when the measurement claim uses its independently obtaining relation or binding. A plan, compatible signature, method description, instrument type, or retained reference establishes none of those actual facts.

##### C.16:5.3.1 - Construct the measurement relation

1. **Start with what is being measured and why.** Specify the subject, Characteristic, conditions and required range of interpretation under §§5.1-5.2. Separate what is already known from values the proposed measurement must resolve.
2. **Follow how the indication is produced.** Describe the procedure connecting the subject to the indication. Recover the measurement principle, applicable calibration relation, or combination of both that connects the quantities. Include intermediate conversions when they change the answer. Physical laws, assessment models and instrument-specific relations come from the relevant subject knowledge; B.5:4.2 helps recover their construction.
3. **Include influential conditions.** Consider how the apparatus interacts with the subject, what it samples or averages, and its resolution and operating range. Include an influence when its omission could change the interpretation needed for this use. Explain a correction through the relation that gives its direction and magnitude. Retain an unknown influential quantity as unknown, using available bounds or distributions when justified.
4. **Determine what the relation resolves.** With actual or proposed indications, derive the compatible sought values and their uncertainty under §5.4. If different sought values can produce the same indication, identify that ambiguity. Work a small case or limiting case to expose an omitted influence, inconsistent units or a failed inversion.
5. **Choose the useful return.** Supply the interpreted value, interval or conditional result when it answers the question. Otherwise identify which change could resolve the remaining ambiguity: refine the relation, change the measurement arrangement, obtain an applicable calibration or narrow the conclusion. Choose further observation by the distinction it can resolve and the work it demands, using C.11.DUA when that choice needs deliberation.

When an observed discrepancy matters, compare its plausible sources in the subject account, measurement relation and actual arrangement. Change the contribution that can alter the answer; sometimes removing an unwanted influence from the arrangement is more useful than modeling it in greater detail. A model-development result states the relation and what it would establish. A claim about a performed measurement also identifies the work and obtained result under §§5.3-5.5.

#### C.16:5.4 - Recover input quantities, output quantity, and uncertainty

**M‑IO‑1.** Name each actual input quantity used by the model, including indications, repeated observations, environmental or other influence quantities, reference values, calibration coefficients, and applied corrections when current. Name the exact output quantity whose value is attributed to the measurand. These are measurement-model roles, not a universal work input-output ontology.

**M‑UNC‑1.** State the uncertainty associated with the attributed value or values whenever it affects interpretation or use. Identify the contributing input uncertainties, correlations or covariance when relevant, propagation method, coverage or interval interpretation, and significant model inadequacy. An uncertainty number without its interpretation is not complete.

**M‑UNC‑2.** Propagation follows the declared measurement model. Linearized propagation, sampling, interval, set-valued, or another method is admissible only under its own assumptions. Combining provenance pointers is not uncertainty propagation, and more cited grounds do not monotonically guarantee lower uncertainty.

#### C.16:5.5 - State one measurement result and one result episteme

**M‑RES‑1.** `MeasurementResult` is the value or set of values attributed to the measurand together with relevant information needed to interpret them. At minimum, recover the measurand, Characteristic, Scale, attributed value or values, Unit when relevant, uncertainty, method, model, calibration basis, time stance, and exact measurement work.

**M‑RES‑2.** `MeasurementResultEpisteme` is one exact C.2.1 episteme. Its ClaimGraph states the C.16 result, subject, interpretation basis, polarity or domain status when current, and uncertainty. `U.Measure` may designate this retained reading claim. The episteme is not the measurand, actual subject state, raw output, indication, diagnosis, or criterion verdict.

**M‑RES‑3.** When exact work and governed actual changes first establish the episteme's identity and that inception matters, A.15.PROD supplies the local entity-identity inception claim. C.16 does not introduce a work-to-result relation.

#### C.16:5.6 - Keep comparability and scoring bounded

**M‑CMP‑1.** Direct comparability is conservative: two readings cite the same `U.DHCMethodRef`, Characteristic, Scale and Unit semantics, compatible model and calibration regime, and a compatible time or population basis. Similar labels or units are insufficient.

**M‑CMP‑2.** Cross-template conversion, normalization, scoring, aggregation, comparison, selection, or cross-context transport names its method, declaration, and loss or uncertainty consequence under the pattern for that operation. Name an F.9 Bridge when cross-context semantic correspondence is required. C.16 does not mint a common scale or corpus-wide migration relation.

**M‑SCORE‑1.** A Score is another declared Scale reading. Its scoring method and actual application remain under their direct Method, Work, and operation-binding patterns. A score does not overwrite its source measurement results.

#### C.16:5.7 - Route provenance and later use outward

`U.EvidenceStub` may carry a type-of-ground and identifier that lead to the exact A.10/G.6 provenance path. The path can cite the method description, model, calibration, work, inputs, output, result episteme, source publications, and transformations. Neither the stub nor a graph edge establishes those objects or their obtaining relations.

A later comparison, diagnosis, criterion evaluation, acceptance action, or decision is separate dated work. It uses the result episteme through an exact premise, reference, operation-argument, decision-use, or other direct relation. Currentness belongs to G.11; bounded reliance to A.10 or B.3 under their entry conditions.

#### C.16:5.8 - Lexical and neighboring-pattern discipline

Use **measurand**, **measurement subject**, **Characteristic**, **Scale**, **Level**, **Coordinate**, **value**, **Unit**, **measurement method**, **measurement model**, **calibration**, **uncertainty**, **measurement work**, and **measurement-result episteme** for their exact jobs. Plain-register *metric*, *reading*, *score*, and *output* are acceptable after first-use mapping. Do not use *measurement result*, *evidence*, *validation*, or *verification* as umbrella terms for several governed objects.

**Key relations.** C.16 uses A.17 and A.18 for Characteristic and Scale legality; A.6.1 for declaration-local positions and operation bindings; A.13 for each actual performer; A.15.1 for independent admission of the dated Work; and F.6 afterward only when precise assignment-bound attribution is needed. If claim-bearing source wording still says only “role,” use E.10.ROLE first, then use A.2 or A.2.1 only when an exact local system-role kind, classification, or assignment has actually been recovered. C.2.1 covers the result episteme; A.10/G.6 provenance; G.11 currentness; B.3 assurance; and the exact pattern for the next diagnosis, acceptance, causality, comparison, selection, or decision question.

