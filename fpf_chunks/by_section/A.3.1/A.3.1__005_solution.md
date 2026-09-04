---
chunk_kind: "child"
pattern_id: "A.3.1"
pattern_title: "U.Method: Reusable Way of Doing with Explicit Applicability"
section_id: "A.3.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.1/A.3.1__005_solution.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "A.3.1 — U.Method: Reusable Way of Doing with Explicit Applicability"
  - "A.3.1:4 — Solution"
line_start: 8004
line_end: 8248
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.15.1"
  - "A.15.2"
  - "A.22"
  - "A.3"
  - "A.3.2"
  - "A.6.1"
  - "A.6.5"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.1.5"
  - "C.2.1"
  - "C.2.P.DR"
  - "C.3.1"
  - "C.3.2"
  - "E.18"
  - "E.18.1"
  - "E.20"
  - "F.9"
  - "G.5"
keywords:
---

### A.3.1:4 - Solution

`U.Method` is the **reusable semantic way of doing under stated applicability**.

**Local method mantra.** *Name the reusable way; say who or what it is for and when; state the intended result or preserved condition and any applicable limit or stop condition; add an effective reference scheme or a selected structure only if changing it would change the method identification or the next decision; keep descriptions, plans, Work occurrences, and mechanisms separate.* Use this as an attention aid.

It is a non-agentive holon kind. Part methods can be selected, bounded, ordered, joined, adapted, and hidden or exposed through method interfaces to form a whole method with whole-level preconditions, effects, invariants, constraints, and assurance hooks. The whole method may then be used as a part method in a larger method.

A `U.Method` is:

* **semantically local**: its identity uses the declared participant meanings, applicability, conditions, intended effects or preserved conditions, and bounds; add an effective reference scheme and local senses only when a meaning difference would change the method identification or a stated comparison;
* **semantic**: it is the way of doing that descriptions denote and work may enact;
* **concern-explicit**: it states what a future enactment is intended to do or decide and its intended effect or preserved condition;
* **description-independent**: one method may be described by several `U.MethodDescription` epistemes;
* **run-independent**: one method may be enacted by many Work occurrences admitted under `U.Work`;
* **assignment-independent**: Method admission conditions may name local system-role kinds or capability-fit conditions, but named holders and obtaining assignments belong elsewhere;
* **participant-semantic**: it may state generic participant meanings and method-side applicability without declaring `RelationSignature` SlotSpecs, `OperationAlgebra` argument or result positions, planned fillers, or actual participants.

Do not begin by replacing *method* or *practice* with a preferred technical word. First finish the ordinary sentence, "Here the text is trying to name or assert `___`." Then use this table:


| If the text is really about... | Govern it as... |
| --- | --- |
| semantic way of doing | `A.3.1 U.Method` |
| relation or composition among methods, method families, method-description epistemes, or local method expressions | `C.2.1` or the exact comparison/direct-relation pattern for an actual relation among description epistemes; `A.22` only for a selected structure whose constituent relations already obtain; `G.5` and `A.19` for family selection; `A.15.1` for `enactsMethod`; `B.1.5` for order-sensitive method composition; `C.29` for graph or algebraic representation |
| description of that way of doing: SOP, program, proof script, solver model, protocol, diagram, process model, recipe text | `A.3.2 U.MethodDescription` |
| source phrase such as *practice*, *technique*, *school*, *tradition*, or a local method label whose claim is unclear | leave it unresolved until the sentence identifies a reusable way, description, discipline or tradition, or model-use boundary; use `A.1.1` for the bounded-context or model-use claim and `C.36.P` for the cultural-evolution, tradition, style, canon, recognition, selection, or mediation claim |
| selected formal declaration or mathematical lens | `A.6.0` for the declaration; `C.29` when a stated use applies the mathematical lens |
| mechanism declaration or realization relation | `A.6.1` and `E.20` |
| system-role assignment, relation among exact system-role kinds, direct responsibility relation, or holder eligibility hidden under a practice or Method phrase | `A.2`, `A.2.1`, `A.2.7`, `A.6.RCD`, and `A.15` as applicable |
| planned dated work or authorization to prepare work | `A.15.2 U.WorkPlan` plus the relevant gate, authority, or commitment pattern |
| dated work occurrence or run; trace, log, or result record | Use `A.15.1` for the dated Work. Route a separate record or result by what it asserts—measurement, evaluation, production, delivery, acceptance, or evidence—and link it to Work only through a relation whose predicate and participants are defined by its direct pattern or declaration. |
| field, bounded-context or model-use, discipline or tradition, recognition or selection, mediation, variant, or cultural-evolution claim | Use `A.1.1` for a bounded-context or model-use claim; `C.20`, `C.36`, or `C.36.P` for a discipline, tradition, canon, or cultural-evolution claim; and `F.17`, `F.18`, `F.9`, `C.18`, `C.19`, `G.5`, or `G.11` only after the sentence names its sense, recognition, mediation, variant, selection, or currentness claim. |
| evidence or provenance relation for a claim | `A.10` |
| graph path, query, table, dashboard, publication face, or pattern relation made to prescribe action by its layout | apply `C.2.P.DR`, then state the actual method, Work, gate, or authority claim—or stop when none is present |

#### A.3.1:4.0a - Strategy wording by claim position

Treat `strategy` as ordinary source wording until the sentence's claim position is clear. Do not mint `U.Strategy`.

When the wording names a reusable way of deciding or acting under stated applicability, it identifies a `U.Method`. A clinical treatment strategy, manufacturing setup strategy, search strategy, or negotiation strategy qualifies only when it states the reusable action, participant meanings, preconditions, intended result, and bounds.

When a protocol, playbook, program, diagram, or prose passage describes that way, that episteme may be a `U.MethodDescription`. Reusable strategizing can itself be a `U.Method`; a dated strategy workshop, search episode, or planning session is a Work individual only when its A.15.1 occurrence basis is grounded.

When the sentence is about choosing among candidates, use `A.19.SelectorMechanism` and G.5 for the actual criteria, policy, and selector outcome. The label *strategy* does not replace those objects or prove that a reusable method has been stated.

Leave quoted or explanatory *strategy* wording alone when it carries no FPF claim. The repair is complete when a reader can say what the sentence asserts and which pattern contains the defining content for that assertion, not when every occurrence has been replaced.

#### A.3.1:4.1 - Thin first-use method identification

Start with the least apparatus that lets another reader recognize the same method:

1. **Ordinary use.** State the reusable way of doing, the kinds of participants it is for, when it applies, what it is meant to achieve or preserve, and any applicable use limits or stop conditions. If that sentence is enough for the decision at hand, stop.
2. **Later comparison or reliance.** Use the needed entries in the Plain aid below when the ordinary statement is insufficient for another person to distinguish same-named methods, compare descriptions or variants, cite one edition in a plan, or audit why this method was selected.
3. **Organization of several methods or uses.** Open `A.22`, `B.1.5`, or another direct composition pattern only when the question is about the organization itself—for example, which methods were composed, selected, used as fallbacks, or enacted in the reviewed work.

Moving to a heavier level must solve one of those concrete problems.

The following is a Plain identification aid, not a record kind, ontic, serialization, or mandatory form. Omit every optional line that the stated decision does not use.

```text
Method identification aid:
  MethodRef:
  SemanticBasisIfMeaningVaries:
  Applicability:
  GenericParticipantMeanings:
  MethodConcern:
  Preconditions:
  IntendedResultOrPreservedCondition:
  MethodDescriptionIfReliedOn:
  WorkRelationIfReliedOn:
  SelectedStructureOrModelUseIfReliedOn:
  RelationsThatMustObtain:
  RelianceWindow:
  ReviewIf:
  NotEstablished (ClaimBoundary):
```

Use `NotEstablished` only for a stronger reading that passes F.19:4's plausible-reader guard test. State the smallest clear correction; omit the entry when the positive identification suffices. Use the FPF term `ClaimBoundary` when a named neighboring subject assertion depends on that boundary.

Add `SemanticBasisIfMeaningVaries` only when the same words have different meanings under another effective reference scheme or set of local senses. Add a claim scope, context slice, selected structure, or model-use relation only when its own predicate obtains and changing it would change the method identification or the later decision.

For every relied-on relation, name its participants, the relation that must obtain, and the pattern that defines or constrains it. A generic `source`, `support`, `evidence`, or `current use` entry is not a replay basis. `RelianceWindow` says which variant, time, or description edition the comparison relies on. `ReviewIf` names the concrete change that would make that comparison unsafe.

#### A.3.1:4.1a - Closure and bounded non-use

Close positively when a reader can write the reusable action, generic participant meanings, applicability, preconditions, intended result or preserved condition, and any use limit or stop condition that changes the identification or decision. Resolve an effective reference scheme and local senses only when a meaning difference changes that answer. Cite a method description, selected structure, model-use relation, or Work relation only when the next decision actually reads that relation.

If the project also claims an actual change, finish the method identification first. Then open A.3.4 for the actual changed referent, temporal boundary, subject facts, and transformation identity.

Close by non-use when the source is only a description, plan, dated Work occurrence, mechanism declaration, selector result, system-role-kind relation, another direct relation, evidence relation, publication use, or quoted wording. If the material does not distinguish those positions, retain the source phrase as an unresolved cue and stop rather than inferring `U.Method`.

#### A.3.1:4.2 - Method and mechanism settlement

Do not decide from words such as *method*, *algorithm*, *process*, or *mechanism*. First ask what the sentence lets the project assert:

| Plain question | Answer and pattern to use |
| --- | --- |
| What reusable way of observing, deciding, deriving, changing, or preserving is meant? | State the `U.Method` under A.3.1: participants, applicability, conditions, intended result or preserved condition, and boundary. |
| What reusable family of operations and laws is declared? | State the separate `U.Mechanism` declaration under A.6.1: its concern, subject and range meanings, operation algebra, laws, admissibility conditions, and Applicability. |
| What happened on this dated occasion? | Recover every exact actual performer and its obtaining system-role assignment through A.13, then identify the dated Work occurrence independently under A.15.1. Its enacted Method, extent, containing System, bindings, and resources are occurrence-side facts. Add F.6 attribution through that same assignment only when the receiving claim expressly consumes precise assignment-bound attribution; missing or failed F.6 attribution does not erase the independently admitted Work. |
| What correspondence, realization, or support claim is being made around those objects? | Name the relation, its participants, exact predicate, current facts, and subject-pattern locator. If no such predicate is defined, keep the objects separate and stop rather than implying the relation. |

A method statement may cite a mechanism episteme whose content declares operations used by that method. A shared concern or operation name does not make the two values identical. A selector may choose a method, and an A.6.1 application may bind a method as an actual value. State that use only when the selector outcome, application binding, or another admitted direct relation is present; otherwise keep the method and neighboring object separate.

Keep the nearby relation families distinct once, here. An F.9 Bridge between two exact F.17 `SchemeSenseCell` values states a cross-context sense correspondence; it does not change an effective reference scheme or establish identity. A claim that this Bridge suits one named use remains a separate C.2.1 bounded-use claim, and A.10 or B.3 governs reliance on that claim. An A.6.1 realization relation connects a mechanism declaration to a realizer; it is not the mechanism content. C.29 governs a mathematical preservation or representation claim. E.20 governs where mechanism meaning is maintained. Evaluation, measurement, and evidence-use patterns support their own claims; they do not add content to the method or mechanism.

When neither the reusable way nor the reusable operation declaration can be stated, keep the source wording unresolved. Replacing it with a more technical noun is not a repair.

#### A.3.1:4.3 - Method, MethodDescription, WorkPlan, Work

Keep the four positions separate.

| Position | What it means | Common mistaken substitutes |
| --- | --- | --- |
| `U.Method` | how in principle, for stated participants, applicability, conditions, effects, and bounds | code, SOP, graph, solver model, proof script, workflow diagram |
| `U.MethodDescription` | an episteme that describes a method in a representation | method semantics, actual run, authority to work |
| `U.WorkPlan` | planned dated work or work preparation | timeless method, generic recipe, proof that work happened |
| `U.Work` | admitted kind for dated Work occurrences; one Work individual is one world-side occurrence | method, plan, result interpretation, evidence relation, or record about the occurrence |

The same solver model, repository, protocol, diagram, or run packet may figure in several claims, so say what each sentence is about. The solver-model episteme may describe a method; its mathematical representation may expose a C.29 formal substrate; a dated solver run may be Work; and a measurement or evaluation result may support another claim through its evidence relation.

#### A.3.1:4.4 - Method statement fields

A useful `U.Method` statement can usually answer these questions in ordinary project language:

| Field | What to name |
| --- | --- |
| Method name | the reusable semantic way of doing |
| Semantic basis when needed | the effective reference scheme and local senses whose variation would change the method meaning |
| Applicability | the candidate family, conditions, limits, and qualification window under which the way of doing applies |
| Method concern | what future enactments are intended to change, observe, compare, classify, evaluate, communicate, select, derive, prove, control, produce, or preserve; this is reusable semantic content, not an actual occurrence |
| Preconditions | states already in effect for the method to be applicable |
| Effects or postconditions | what successful enactment is meant to produce or preserve |
| Generic participant and boundary meanings | the kinds of entities, resources, conditions, interfaces, and Method-side local system-role-kind or capability-fit conditions that a future enactment may involve, without declaring `RelationSignature` SlotSpecs, `OperationAlgebra` positions, planned fillers, or actual participants |
| Capability acceptance conditions | thresholds or envelopes evaluated against a holder's capability, not baked into the method identity |
| Failure and stop conditions | when the method cannot be used, when a description no longer states it accurately, and when planned Work must not enter its gate |
| Method-description membership | which epistemes, if any, meet A.3.2 membership for this exact Method; any comparison or plan must separately name the edition and claims it uses |
| Work relation | what Work occurrences admitted under `U.Work` may enact the method and how their separate records cite the description used |

This table is a recognition checklist, not a data schema. Start with the ordinary method sentence. Use A.6.1 for a reusable operation declaration, A.6.5 for a reusable direct-relation declaration, A.15.2 for planned use, and the exact direct relation or A.6.1 application binding for actual participation.

#### A.3.1:4.5 - Representation and programming-paradigm discipline

A `U.Method` need not be written as an imperative sequence. A way of doing may be described or represented through code, rules, constraints, process diagrams, SQL queries, proof scripts, optimization models, or functional or effect-handler programs.

Choose by the claim being made:

* If the sentence states the reusable action, participants, applicability, intended result, and boundary, use A.3.1.
* If it points to code, prose, a protocol, diagram, solver model, or other episteme that describes the method, use A.3.2. Use A.6.0 or C.29 when the claim is instead about a formal declaration or mathematical representation.
* If it declares a law-governed operation family or asks where that declaration is maintained, use A.6.1 or E.20.
* If it schedules future work or reports a dated occurrence, use A.15.2 or A.15.1.
* If it claims evidence, provenance, or support, use A.10 and the direct evaluation or measurement pattern. If a representation's form or layout is being treated as sufficient to prescribe or authorize action, apply C.2.P.DR before choosing the pattern for that claim.

Keep cross-context and application claims separate from those five choices. F.9 governs a Bridge between two exact F.17 `SchemeSenseCell` values. A claim that this Bridge suits one named use remains separate under C.2.1, and A.10 or B.3 governs reliance on that claim. C.2.1, A.6.3, A.6.3.RT, A.6.4, or A.1.1 governs an actual change of episteme edition, reference scheme, representation scheme, retargeting, or model-use relation. A.6.1 governs a mechanism realization or application binding. State one of these only when its participants and predicate are present; otherwise stop at the source objects without asserting the relation.

Thus *algorithm* and *practice* remain source cues. “The SQL query is the method” fails unless the project can state the reusable way of querying, its admissible inputs, intended result, and stop independently of that query text. “Our review practice is the method” fails when the sentence is actually about a team assignment, dated review, discipline, tradition, evidence record, or publication.

#### A.3.1:4.6 - Constructor and process-theory settlement

When a method concerns change, its statement says what change a future enactment is meant to achieve; it does not assert that any referent changed. The same identification rule applies to methods for other concerns, such as observation, comparison, classification, evaluation, communication, selection, proof, and preservation.

The constructor-theory and process-theory source line supports this separation but does not supply a universal method ontology. FPF uses it as follows:

* An exact actual performer first has the A.13 core; A.15.1 then independently identifies the dated Work, at least one obtaining `enactsMethod` relation, time, and at least one obtaining locally declared containing-system relation. Another enactment relation is named only when the receiving claim relies on it. F.6 enters only when that claim also consumes precise assignment-bound attribution through the same obtaining A.13 assignment; missing or failed F.6 leaves the Work intact. The System's classification and the obtaining assignment remain separate claims.
* The `U.Method` is the reusable way under stated participant meanings, applicability, conditions, intended result or preserved condition, and bounds. A `U.MethodDescription` is an episteme that describes it.
* A formal substrate or mathematical lens can make the method analyzable, and a `U.Mechanism` can declare the relevant operation family and laws.
* A cross-context Bridge, changed reference or model-use relation, mechanism realization, evaluation, or evidence-use claim remains a separately stated relation with its own participants.
* A `U.WorkPlan` prepares or schedules dated Work; a Work individual is the occurrence that actually happened.

For example, “the etch method changed `Wafer-22`” contains at least two claims. A.3.1 identifies the reusable etch method. Only if an actual bounded change of `Wafer-22` is independently grounded does A.3.4 identify that transformation; any claim connecting the Work and transformation additionally needs its own predicate or an honest missing-governor result.

Apply the same distinction across physical, informational, organizational, and mathematical work.

#### A.3.1:4.7 - Semantic identity and variants

Two `U.MethodDescription` epistemes may describe the same `U.Method` when the later comparison or reuse decision relies on the same method bases:

* effective reference scheme and local senses, when a meaning difference matters;
* generic participant meanings and declared applicability;
* compatible preconditions;
* compatible intended effects or preserved conditions;
* compatible safety and other non-functional bounds;
* accepted nondeterminism or search behavior; and
* the same work-facing acceptance relation, when that relation is part of the comparison.

Different control flow, proof notation, programming paradigm, diagram notation, or prose does not by itself make a different method. The converse also holds: the same name, repository, supplier label, or diagram family does not prove identity.

Keep one method across parameter ranges, equipment envelopes, or representation variants only when its declared applicability and the bases used by the comparison admit that variation. A changed intended result, participant meaning, safety bound, semantic basis, or acceptance criterion requires a stated refinement, substitution, or distinct-method decision.

**Same-name locality replay.** An emergency-department `Triage` method applies to patient presentations awaiting clinical assessment; a clinician enacting it uses clinical signs to assign urgency, escalates unsafe cases, and stops when the evidence cannot support that assignment. A software-defect `Triage` method applies to defect reports awaiting product handling; a product team enacting it uses reproduction evidence, severity, and ownership to choose routing and release impact, and stops when the report cannot support that choice. The shared label identifies neither method. Their participants, applicability, local senses, intended results, and stops distinguish them without a generic context object.

**No-extra-locality replay.** `EuclideanGCD` over positive integers closes as one method when the integer meanings, division-with-remainder rule, positivity precondition, decreasing-remainder invariant, and greatest-common-divisor result are stated. If those facts answer the comparison, add no claim scope, context slice, model-use structure, or other locality object.

#### A.3.1:4.8 - Method relations, composition, and Work enactment

Start with the practical question, not a graph or the umbrella word *specialization*. Ask what must be decided now.

| Current question | First useful result |
| --- | --- |
| Does this reusable way meet one or more Method-kind criteria? | Use `C.3.2` for the admissibility check and a `true`, `false`, or `unknown` judgment. An out-of-scope request is `not-applicable` and forms no judgment. |
| Does one Method kind have several broader kinds? | Check each broader-kind claim under `C.3.1`. |
| Does one Method contribute to several larger Methods? | Use `B.1.5` for every part–whole pair and every whole construction. Each whole keeps its own action, boundary, interfaces, and reidentification rule. |
| Are two Methods being compared for refinement or replacement? | First identify both Methods and the use that needs the comparison. State the direction, what remains, what changes, and the material guards or losses. A sentence or local claim is often enough for one use. |
| Is this another question—for example, parameter variation, family grouping, fallback, dispatch, a description, a selected structure, performed Work, capability, provider contribution, or cultural change? | Use the pattern that defines or tests that claim. The label alone establishes no Method kind, Method part, or relation occurrence. |

Before claiming refinement or replacement, decide whether the changed account still identifies the same Method. If it does, state what was preserved and what changed; do not invent a relation between two Methods. If two Methods are identified, a refinement comparison states its direction and use, the semantics retained from the first Method, what the second narrows or strengthens, and the action or result that changes.

A replacement comparison says which Method may replace which other Method, for what use, under which preconditions, with which intended result or preserved condition, and which bounds, interfaces, losses, and guards must remain visible. Do not infer the reverse direction. Shared kind criteria or similar descriptions do not prove replacement.

A parameter change inside the Method's declared applicability and identity rule is variation of the same Method. A change to a participant meaning, result, bound, interface, or acceptance condition that matters to identity identifies another Method or leaves the identity question unresolved.

A `G.5` family row cites already identified Methods and states why they are grouped for the current use. A fallback can belong to a `B.1.5` whole construction, a `G.5` selector rule or result, or a local relation-bearing claim. A dispatch rule says which selector branch applies; state the current branch and its basis.

When FPF has no admitted predicate for refinement, replacement, fallback, or another relation-bearing claim, use `A.6.RCD` to choose the lightest sufficient result. For one use, a local claim may be enough; repeated use of the same rule may justify a reusable predicate definition. Continue through `E.24` and `E.24.UK` only when a named later use must treat the relation occurrences themselves as stable objects. A local claim or predicate definition cannot become an `A.22` edge.

**Short positive.** `ChangeImpactReview` can meet two Method-kind criteria and also be required by the independent constructions of `ApproveControlSoftwareRelease` and `InvestigateFieldIncident`. Those judgments and two `methodPartOf` facts remain separate.

**Selector anti-case.** A `RapidRecoveryMethods` row groups `RollbackRelease`, `DisableFeatureFlag`, and `ShiftTraffic` for one selector. Its stated grouping basis and fallback policy may support a `G.5` result, but they do not establish a Method kind, one composite Method, or a refinement or replacement relation. If the fallback condition is incomplete, return the missing fact instead of drawing an edge.

`MethodRelationStructure` is only a local name for an `A.22` structure selected from independently identified constituents and relations that already obtain. It is not a durable kind, Method holon, or relation type. Composition, refinement, replacement, parameter variation, family grouping, fallback, dispatch, and enactment are recognition cues; the cue does not decide the claim.

**Filled A.22 basis — enacted-method review.** For this one-off review, a practitioner selects only two A.15.1 `enactsMethod` occurrences. No durable selection judgment is asserted.

* **Independently identified constituents.** `InspectPumpSeal@PumpMaintenance-2026` and `ClassifyPumpSealCondition@PumpMaintenance-2026` are two `U.Method` values. `Pump37SealInspectionWork-2026-07-25T0900-0908` and `Pump37SealClassificationWork-2026-07-25T0910-0916` are two admitted A.15.1 Work occurrences.

  `PumpDiagnosticAssignment` is a declared `U.SystemRoleAssignment` species. Under A.2.1 it defines the holder and assigned-kind participant meanings and uses `PumpDiagnosticSystemRoleKindDomain` as the local assigned-kind domain. Occurrence `Pump37DiagnosticAssignment-2026-07-25` has `PumpDiagnosticService-A : U.System` as holder, `PumpDiagnosticSystemRole` as the assigned-kind value admitted by that domain, and an extent covering both Work occurrences. That System performs each Work under the assignment and within `Pump37MaintenanceCell-A`.

  The fixture states no Work-to-`Pump_37` predicate, so neither Work is said to affect or concern the pump merely because its designator contains `Pump37`.
* **Selected obtaining relations.** `enactsMethod(Pump37SealInspectionWork-2026-07-25T0900-0908, InspectPumpSeal@PumpMaintenance-2026)` and `enactsMethod(Pump37SealClassificationWork-2026-07-25T0910-0916, ClassifyPumpSealCondition@PumpMaintenance-2026)` obtain under A.15.1.
* **Applied constraint claims.** `DiagnosticReviewWindowConstraint` states that an eligible `enactsMethod` occurrence must have one of the two independently admitted Work individuals as its Work participant and an extent within 09:00-09:20 on 2026-07-25. `NoCompositionFromEnactmentOrderConstraint` states that their timestamps and order establish no serial, fallback, or whole-method relation.
* **Selection-use frame.** `DiagnosticMethodEnactmentFrame` states the question: which methods did these two Work occurrences enact during the review window? The admissible action is to list the two `enactsMethod` occurrences in that review.

Those four discriminators identify `DiagnosticMethodEnactmentStructure-2026-07-25-0900-0920`, locally designated `MethodRelationStructure` for this use. Reidentify it only from its four constituents, two obtaining relations, two applied constraint claims, and use frame. If the project relies on a persisted selection, separately identify the System that made it, the selection Method and dated Work, the participation relation or A.6.1 binding used by that Work, and the C.2.1 result episteme. Add a C.11 choice claim only if one is asserted. If responsibility for that choice is also claimed, cite its direct domain predicate, actual participants, applicability, and occurrence identity or return the exact missing governor.

**Missing-governor stop.** Suppose a note additionally calls `ClassifyPumpSealCondition@PumpMaintenance-2026` a fallback for `InspectPumpSeal@PumpMaintenance-2026`, but supplies no direct fallback predicate, compatible participant meanings, or occurrence-identity rule. Keep the two methods and the note, omit the fallback relation, and return `missing-governor: fallback relation for <ClassifyPumpSealCondition@PumpMaintenance-2026, InspectPumpSeal@PumpMaintenance-2026>`. If the question is specifically about fallback organization, do not select a positive structure until that relation and all four A.22 discriminators are available.

Method-holon composition is not A.14 component mereology. Source labels such as `SerialStepOf` or `ParallelFactorOf` remain cues until B.1.5 or another subject pattern supplies an admitted relation with participants and an obtaining rule. A method-description node is not a submethod unless the described object is independently identified as a `U.Method`.

Work composition is occurrence-side. Work may interleave, split, retry, or fail differently from the method description. A temporal Work part can enact the same whole method, and an episode can change Work continuity without changing method identity. Call a candidate a submethod only when it has its own reusable action, preconditions, intended result or preserved condition, boundary, and whole-method relation.

**Quick distinction.** A step label, graph node, detector component, event-log segment, telemetry interval, work-plan item, or document section is not a submethod by position. If it states a reusable way with method-level conditions and a relation to the whole method, test it under A.3.1 and B.1.5. If it states what happened, when it happened, what a component did, or what a record shows, use the direct Work, mechanism, evidence, or description pattern instead.

Mathematical or graphical notation may describe the selected structure under C.29 or occur in a `U.MethodDescription`. A registry row lists or describes candidates; state any relation among them separately under its defining pattern.

