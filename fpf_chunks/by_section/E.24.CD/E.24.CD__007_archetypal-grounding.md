---
chunk_kind: "child"
pattern_id: "E.24.CD"
pattern_title: "Ontic Candidate Detection and First-Use Disposition"
section_id: "E.24.CD:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.CD/E.24.CD__007_archetypal-grounding.md"
commit_sha: "17edd955485f60cafb16159c7d90e20f4ad21844"
heading_path:
  - "E.24.CD — Ontic Candidate Detection and First-Use Disposition"
  - "E.24.CD:5 — Archetypal Grounding"
line_start: 86676
line_end: 86772
dependencies:
  - "A.1"
  - "A.14"
  - "A.15.1"
  - "A.19"
  - "A.19.ECS"
  - "A.3.4"
  - "A.6.0"
  - "A.6.5"
  - "A.6.F"
  - "A.6.P"
  - "A.6.RCD"
  - "A.6.RSIR"
  - "B.1"
  - "B.2"
  - "C.13"
  - "C.2.1"
  - "C.2.P.DR"
  - "C.22.2"
  - "C.22.PFR"
  - "C.28"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.2"
  - "E.10"
  - "E.10.ARCH"
  - "E.17.0"
  - "E.18.1"
  - "E.23"
  - "E.24"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.18"
  - "U.CharacteristicSpace"
keywords:
---

### E.24.CD:5 - Archetypal Grounding

#### E.24.CD:5.1 - A candidate that genuinely opens E.24

Before `C.2.1`, “description”, “view”, “claim set”, and “publication” repeatedly pointed to a claim-bearing object used across many patterns. The practical need was stable claim identity across description, evaluation, reference, and publication work. Existing patterns could not supply that shared identity and relation set independently.

That case opens E.24. E.24 then decides the durable ontic; C.2.1 governs the resulting `U.Episteme`; E.17.0, E.24.PUB, F.18, and C.29 keep viewpoint conformance, publication, naming, and representation separate. Cards and files do not become the episteme.

#### E.24.CD:5.2 - Local cooling-pump classification

A maintenance team repeatedly asks whether Pump #14 counts as a cooling pump in plant slice S-14. Pump #14 and its flow, heat-transfer, and operating-state features already have direct governors. The needed outputs are a reusable local criterion and a candidate judgment, not a durable ontology unit.

Apply C.3.2. A `KindSignature` may declare the criterion for repeated use; the judgment can be `true`, `false`, or `unknown`; a current extension is materialized only for a named set-consuming use. A measurement supports a claim about Pump #14's features but does not create its membership.

#### E.24.CD:5.3 - Problem card

A `ProblemCard@Context` under `C.22.2` is a problem-side episteme. It may carry a signal, hypothesis, forecast, scenario, anticipated-condition claim, affected-entity reference, evidence cue, constraint, proposed direction, assignment cue, source reference, or gate cue without creating an actual Problem.

An actual Problem is one obtaining `ProblematicForRelation` under `C.22.PFR`. A card may assert that exact predicate, but it may designate a current Problem occurrence only after C.22.PFR independently establishes the actual-condition relation, criterion-applicability relation, adverse truth, and occurrence identity. Signals, hypotheses, forecasts, scenarios, anticipated conditions, and reviewable formulations remain under `C.22.2` or their exact forecast, scenario, temporal, or causal governor.

For a repair decision, keep the affected entity, evidence-use relation, role assignment or other responsibility relation, source-use relation, and gate or decision claim under their direct governing patterns. Apply `E.18.1`, `E.23`, and the exact work, search, evaluation, or continuation pattern when repeated problematization or later action is current. Neither the card nor its acceptance or publication creates or ends an actual Problem. Open `E.24` only if a different reusable subject-identity or relation gap remains after these direct claims are recovered; do not rediscover the actual Problem as a new ontic.

#### E.24.CD:5.4 - Record-shaped false candidate

A project schema contains:

```text
ChangeItem:
  status:
  owner:
  method:
  mechanism:
  evidence:
  result:
  target:
  source:
```

Treat the schema as source material, not as an ontology. A proposal episteme, method, mechanism declaration, work plan, intended-work claim, performed-work occurrence, holder system, state claim, evidence item, result, affected referent, and source remain different objects. Recover only those that the meeting actually uses:

| Field cue | Object and relation to recover |
| --- | --- |
| `owner` | Identify an admitted holder `U.System`, then state the exact `U.RoleAssignment`, responsibility, commitment, or authority relation only if its predicate obtains. The field neither assigns the holder nor grants authority. |
| `status` | Name the exact bearer and the governed state or status value, claim, gate disposition, decision result, or other current relation. Field presence implies no readiness, validity, gate passage, work authorization, or release. |
| `method` and `mechanism` | Keep an admitted `U.Method` and any qualifying `U.MethodDescription` distinct from the A.6.1 `U.Mechanism` declaration episteme and its declared operation family. If the field concerns one use, identify the exact operation application and only its declaration-local argument or result bindings that obtain. If it concerns realization, identify the realizing entity and the obtaining mechanism-realization relation. Apply `A.6.1` when the row does not yet distinguish these readings. Shared wording identifies none of them. |
| plan, intended work, and actual work | Keep a `U.WorkPlan` or intended-work claim under `A.15.2`. Add a `U.Work` under `A.15.1` only for an independently grounded performed occurrence, whether ongoing with an open end or completed. A proposal, row, trace, or completion label does not make work occur. |
| `evidence` | First identify what the field points to; do not rename it to fit a pattern. Keep its direct kind: an episteme or evidence record, a carrier, the work that produced or interpreted evidence, a currentness relation, or a provenance relation. If it is an episteme and the meeting asks only about its bounded evidence-use or status-use for the claim, use `A.2.4` first. Use `A.10` when the evidence path must be retraceable; include only the record, carrier, work, currentness relation, and provenance relation needed for this claim. Use `B.3` only when a separate assurance claim is current. The field proves neither the claim nor the row's status. |
| `result` | Identify the result entity, value, or result episteme independently, then state the exact production, measurement, evaluation, decision, delivery, acceptance, or other result relation actually claimed. A result label creates no generic result object or relation. |
| `target` | Identify the affected referent and state an exact work-to-referent, change, effect, or other subject relation only when current. The field does not make the referent a work participant or changed entity. |
| `source` | Identify the source episteme or expression and the exact source-use relation. Source presence is not evidence, authority, or currentness by itself. |

Not every row has every listed object, not every filled field is claim-bearing, and co-presence in one row does not constitute a larger subject. The filled row is one C.2.1 episteme only when one exact ClaimGraph forms a claim-bearing whole about one truthful exact EntityOfConcern under one effective ReferenceScheme. Otherwise keep the epistemes separate and state only the exact collection, publication, representation, or meeting-use relation that actually obtains.

The column arrangement is a publication form only when selected to express an identified episteme for the meeting. The form is not a `U.ChangeItem`, and its columns are not ontic slots. If the project later needs a local kind of records for a query, `C.3.2` may classify those records as records. If several FPF patterns later demonstrate a different shared durable subject with its own identity and minimal relation set, that evidence can reopen `E.24`; the schema's shape cannot.

#### E.24.CD:5.5 - Current configuration around a holon

A maintenance review asks about “the current configuration around Pump #14.” Identify Pump #14 under its system governor, then recover only the characteristic or state claims, actual part relations, temporal phase, and other direct relations that the maintenance decision uses. If the work compares a possible configuration, identify the possible-state episteme and its direct state or configuration claims rather than asserting current actuality.

A separate C.2.1 description episteme may provide claim-bearing orientation. Its exact EntityOfConcern and any grounding holon in a separately current `EpistemeEmpiricalGroundingRelation` neither identify Pump #14 nor turn the surrounding claims into one world-side object. The holon and those current relations answer the question; their conjunction is not `U.Situation`.

#### E.24.CD:5.6 - Operating pump with connected parts

Pump #14 is operating while a sensor, valve, and controller are connected. `Operating` first cues a governed state claim; it does not establish `U.Work` or `U.Transformation`. Connectedness does not establish parthood. Identify the pump and connected entities, state the exact connection relations, and use `A.14` only for part relations whose predicates actually obtain.

Add a dated maintenance or control-work occurrence under `A.15.1` only when its performer, assignment, method enactment, temporal extent, and other required facts are independently grounded. Add an actual bounded change under `A.3.4` only when its changed referent, boundary, conditions, and change facts obtain. No bundle of system, state, connection, work, and change becomes a situation entity.

#### E.24.CD:5.7 - Multi-party emergency

An emergency report mentions a leaking vessel, an overheated subsystem, a suppression system, and response teams. Recover each participating system, each independently grounded actual change, and each dated response-work occurrence separately. State temporal relations through their temporal governors and a causal relation through `C.28` only when that causal-use claim is current and supported.

Use a C.2.1 emergency-description episteme only when the receiving work needs claim-bearing orientation across those objects. The emergency word, the record, and the co-presence of several systems and works identify neither `U.IncidentSituation` nor another bundled whole. Stop decomposition once the response decision has the exact subjects and relations it needs.

#### E.24.CD:5.8 - Mathematical inconsistency under a declared formal substrate

Two specification epistemes state constraints that cannot both hold under one declared `FormalSubstrate` and applicability. Identify the exact claims or epistemes, name that formal substrate, and state the exact inconsistency or consequence relation under its direct formal governor. Use `C.29` only when the formalism is also being used as a mathematical lens for another declared use.

The formal relation may guide a later decision or repair-work occurrence, but it establishes no project-world event, work, transformation, causal relation, adverse episode, actual Problem, or situation entity. Formal consequence is not causation. Inconsistent descriptions do not make their world-side subjects inconsistent without a separately governed bridge claim. If the exact relation or substrate cannot be named, leave the formal claim unresolved rather than letting the word `inconsistency` stand for it.

#### E.24.CD:5.9 - Architecture diagram

An architecture diagram may carry claims about selected structures of one holon. If the diagram is selected as one claim-bearing whole, C.2.1 identifies that episteme. The same episteme has `U.View` membership only when E.17.0 conformance obtains; its publication form and carrier use E.24.PUB; selected graphical elements use C.29 only with explicit correspondence to independently recovered objects.

The diagram does not become the architecture, structure, or ontic by being visible. If the current work is simply to correct one architectural claim, apply the architecture and structure patterns directly.

#### E.24.CD:5.10 - Broad source word

A source says that a method “supports” production. If the author can recover a specific required-effect, method-use, work-enactment, capability, evidence-use, or other direct claim, apply its governing pattern. If the source word still compresses several claims, use E.10 and E.10.ARCH to retain it only with its bounded meaning or in quote-only or reduced use.

Do not open E.24 merely because `support` recurs, and do not invent `SupportRelation` as the candidate.

#### E.24.CD:5.11 - Score table and characteristic space

A score table can serve as the publication form of an evaluation-result episteme over a `U.CharacteristicSpace`, or it may be only a local report. Use A.19 when the characteristic space itself must be identified and A.19.ECS when the work is constructing the evaluation characteristics for a contested comparison. Use C.29 when readers calculate, compare, infer, navigate, or inspect through the table's mathematical structure and those available operations matter.

The table does not admit `U.CharacteristicSpace` by appearance and does not require another candidate ontology beside the current A.19 governing pattern.

