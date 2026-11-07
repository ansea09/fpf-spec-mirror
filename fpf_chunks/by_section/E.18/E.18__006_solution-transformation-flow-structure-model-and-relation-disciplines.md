---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transformation Flow Structure"
section_id: "E.18:5"
section_title: "Solution - Transformation-flow structure model and relation disciplines"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__006_solution-transformation-flow-structure-model-and-relation-disciplines.md"
commit_sha: "870fb0c2a5dcfe1e0165a111fdf2cf8659c85a54"
heading_path:
  - "E.18 — Transformation Flow Structure"
  - "E.18:5 — Solution - Transformation-flow structure model and relation disciplines"
line_start: 110288
line_end: 110601
dependencies:
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.6.RCD"
  - "A.7"
  - "C.29"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.17"
  - "E.18.1"
  - "E.18.2"
  - "E.18.NET"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.18:5 - Solution - Transformation-flow structure model and relation disciplines
**Dominant Solution uses.** In ordinary E.18 use, keep five structure uses primary: name one selected transformation-flow structure; distinguish the selected structure from a flow valuation and from its mathematical descriptions; place gates only on crossings or on a pre-run work-entry claim; preserve the comparison’s required common basis, normalize when needed, and retain declared set returns; and keep cycles under budget plus `PathSlice` refresh. A gate may authorize or block an intended entry, but it neither creates a future Work occurrence nor fills fields in one. S12 viewpoint mapping remains conditional viewpoint-mapping input when engineering or publication viewpoint mapping is current.

#### E.18:5.1 - S1 - Selected Structure (conceptual)

Select S under A.22 by four discriminators:

- O: the exact independently identified constituents;
- R: the exact selected obtaining relation occurrences, with their direct predicates, participant meanings and occurrence-identity rules;
- C: the semantic constraint claims actually applied in selecting the organization; and
- F: the named use question, admissible action and stop or return condition.

This selection identifies an organization; it does not create its participants or make a proposed relation obtain. Include the complete participants of each selected occurrence, including participants that a compact drawing leaves off its main line. An occurrence may itself be a constituent participating in another relation. An exact scope or budget contributes to S through C when it is an applied selection constraint; a record, diagram, selecting system or valuation is not an extra identity discriminator.

A.6.1:4.5 supplies actual application and declaration-local argument/result bindings. Use the subject's direct rules for physical transfer, Work, actual Transformation, production, causation, source use or other participation. A local compound claim can state what follows from established base relations without becoming an additional relation occurrence in R. If the required governor is absent, return missing-governor; if a deciding fact is unavailable, return missing-information; if sufficient facts fail the positive test, return factually unsupported. A negative requires its own applicable non-obtaining criterion. A proposed arrangement can remain useful as a description or model while the stronger selected-structure claim is unresolved.

**Locate the selected participants and relations.** Let Pos_S be the set of participant positions, with beta(p) resolving each position to its exact constituent x in O. A localFlowPositionId designates that position within S and must not silently be rebound to another constituent. Several visible copies may designate the same position. Participant roles are distinguished by their incidences.

Let Conn_S contain exactly one connection position q = <S, r> for each selected occurrence r in R. The resolution rho(q) = r is one-to-one. An incidence <q, participantDesignator> resolves to the position of that participant of r, preserving the role meaning, required order and repeated participation of the same object under different meanings. Where the predicate uses an unordered participant distinction, retain that distinction; a display order does not add semantics. A drawing with three lines for one ternary relation still represents one q and one r.

Pos_S, Conn_S and incidences are local addresses in a representation of the selected organization, not new FPF kinds or additional subject relations. In the complete incidence representation, use a participant node for each position and a relation node for each q. If r is itself in O, its participant position and its relation node resolve to the same occurrence and are identified in the path representation. This is the explicit connection that lets a path pass from an operation to its result-binding occurrence and on to an operation that actually uses that occurrence. It creates no extra transfer relation.

Keep three bindings distinct: beta resolves a structural position; an A.6.1 operation-application binding establishes actual participation or return; a CtxState binding assigns the independently established values for one particular position-use. A stored reference or compatible type does not establish the actual operation binding.

S remains the same only while O/R/C/F remain the same. A new valuation, alias, path, description or publication can preserve that identity. A new actual application or selected relation occurrence must first pass its own identity rule and then A.22; calling it another valuation does not preserve S. A changed use annotation or policy does not change C unless its content is actually applied in selecting the structure.

**Scope and use.** Gamma_time supplies the budget or horizon used by the relevant application, PublicationScope constrains the selected publication use under E.17/A.2.6, and PathSlice identifies portions used in telemetry and refresh. Section 5.13 defines how all genuinely dependent portions are covered.

 **CtxState (bindings for one use; closed slots):** `CtxState = ⟨L, P, E⃗, D⟩` contains independently established bindings for one position-use. `P` here denotes the plane/units declaration; `Pos_S` above denotes participant positions. PublicationScope constrains applicability and publication of that use; it does not choose these bindings. A scope containing two slices chooses neither as L, and even a singleton scope supplies no unique plane, edition vector or design/run tag. Resolve the components under the rules below, then check the applicable A.2.6/E.17 membership and publication conditions.
 **Slot definitions and changed-binding account boundary (normative):**
  - `L := Locus` — one exact `U.ContextSlice` value identified under `A.2.6`; any scope-membership or translated-scope claim remains with A.2.6 and its current F.9/C.2.1/A.10-or-B.3 premises when semantic translation is actually required.
  - `P := ReferencePlane` — a ref-only binding to the exact plane and units declaration used by the current case. E.18 supplies no generic plane conversion. Cite the current declaration and applicable conversion rule by value. Return `missing-governor` only when no current conversion predicate or rule can state the attempted crossing; return `missing-information` when the needed declaration or case values are unavailable; when the rule and facts are current, state its positive, negative, or inapplicable result rather than a generic blocker.
  - `E⃗ := Edition vector` — a partial map `edition_key ↦ EditionId` whose members cite each versioned value, its exact edition, and the registry or declaration that assigns that edition; `G.11` defines the edition-bump and refresh records, while `E.17` defines publication of the refs.
  - `D := DesignRunTag` — `design(T^D)` or `run(T^R)` only as consumed by the exact `A.21` gate and, at work entry, the `A.15.5` readiness claim; the tag does not identify or create Work.
 **Invariants.** A raw connection step preserves `CtxState` (`⟨L,P,E⃗,D⟩`). A changed use binding has an explicit from/to account and the basis required for that change. When an applicable A.21 profile governs the transition, represent it as a GateCrossing at `OperationalGate(profile)`. Retain every required check and action consequence; the gate decision remains separate from the facts identifying either binding, a Work occurrence or an obtaining relation.
 **Extension discipline.** A conforming use registers any extra slot beyond ⟨L,P,E⃗,D⟩ in the **E.17 publication discipline and the E.18 LEX “CtxState Extension Registry”** with slot‑id, intent, partial‑order rule (neutral or absorbing), and SquareLaw compatibility; unregistered extensions are non‑conformant.
 **Data-shape location.** E.18 defines the connection/cut valuation domain, `PathId`, `PathSliceId`, Gamma pins and crossing references. `A.20` supplies current internal-constraint claims, `G.6` evidence-provenance path visibility and `G.11` the currentness and dependency rules used by 5.13. Their references retain their own subject meanings.

 * **Locus markers:** Transformation, Signature, Mechanism, WorkPlanning, Work, Check and StructuralReinterpretation name common uses of independently identified values. They are not a closed taxonomy of permitted constituents. An additional position states its direct kind, definition and identity basis; an actual application, binding or result value uses A.6.1 and its own declaration. The following common bindings retain their direct definitions:
  **Exact identification (no local ontology):**
  - `Transformation` **≡** **A.3.4** `U.Transformation` only when the structure locus binds one independently identified actual bounded change with its exact changed referent, extent or ordering boundary, boundary conditions, actual change facts, and continuity or reidentification rule. Desired, intended, planned, modeled, selected, described, evaluated, published, or transferred change content remains under the definition or test for that exact claim; it is not a `Transformation` binding merely because it occupies the selected structure. Current-resolution identification establishes neither finer parts nor partlessness. A positive transformation-composition, `TransformationPartOfRelation`, composite-transformation identity, or transformation-holonhood claim stops under D14.16 with the exact A.6.RCD result: `TC-MWH missing-governor` only when no current predicate, applicability condition, or occurrence rule states the required contribution, compatibility, parthood, or whole-identity claim; `TC-MWH factually unsupported` when the governor exists and the available case basis is sufficient to apply its positive test but that test fails; and `TC-MWH missing-information` when a fact needed to decide the test is unavailable. A negative needs its own applicable non-obtaining criterion or complete closure basis and satisfying facts. E.18 retains the independently identified transformations and supplies no provisional contribution, compatibility, parthood, or whole-change architecture; it does not preselect whether a later settlement uses a generic derived relation, subject-specific relations, local compound claims, or non-admission.
  - `Signature` **≡** **A.6.0** `U.Signature` (universal, law-governed declaration).
  - `Mechanism` **≡** **A.6.1** `U.Mechanism` (law-governed application over a SubjectKind and RangedValueKind), with placement and stabilization relations in `E.20` when current.
  - `WorkPlanning` **≡** one exact **A.15.2** `U.WorkPlan` when that plan occupies the structure position. Declaration-local A.15.3 `SlotFillingsPlanItem` rows remain content inside that WorkPlan and do not occupy a locus or identify a relation independently.
  - `Work` **≡** an exact dated Work individual admitted under **A.15.1 `U.Work`**. A structure locus may point to that occurrence after it exists; before execution it points only to a `U.WorkPlan`, A.15.5 readiness relation, or another exact work-entry claim. No second enactment kind is introduced.
  - `Check` **≡** `OperationalGate(profile)` when a gate/check locus is present. A.20 supplies exact internal-constraint results when those constraints are current; A.21 defines the gate profile, independent check retention, result mapping, aggregate decision, and publication minima when a gate decision is current.
  - `StructuralReinterpretation` is only the E.18 position of an independently identified A.6.4 arrow r, bounded-use assertion q, and current-case judgement; it is not a new retargeting kind. E.18 records r and q, the exact case basis and judgement result needed by this placement, and path-slice locality. q's ClaimGraph carries the invariant, visible loss, named receiving use, conditions, and affirmative or negative polarity; the judgement separately reports `satisfies`, `fails`, or `cannot decide`. A `cannot decide` result names the exact missing fact and reopen condition. F.9 is additional only when the same case asserts a semantic relation between two exact F.17 local senses and its predicate obtains; its bounded-use claim, optional `CL`, evidence, and reliance remain separate.
`OperationalGate` is the E.18 check locus when a gate or check position is present. A.20 supplies an exact internal-constraint result when that claim is current. When a gate decision is current, A.21 supplies the exact profile application, independently identified check-application results, `GateDecisionResult`, and rationale. A `DecisionLog` is added only for a current audit, history, replay, or reuse need.
  E.18 adds a structure-local placement rule: retain the independently identified A.6.4 arrow r, affirmative q, current-case judgement of `satisfies`, their basis and `PathSliceId`. With unchanged `CtxState`, this placement is not a GateCrossing. For a changed binding, state its from/to values, establishing basis and any applicable declaration, rule and current application; add a GateCrossing when an applicable gate profile governs that transition. A Bridge, card, UTS row, optional `CL`, witness publication, gate decision or permission claim supplies neither r, q’s polarity nor the case judgement.
> **MVPK integration (import).** Every locus with an external publication face is published via **MVPK** faces (`PlainView`, `TechCard`, `AssuranceLane`, `InteropCard`) under a declared **PublicationScope** (E.17). E.18 reuses MVPK's source-reference, pin, declared-order, and no-new-claim rules. Input/output non-duplication and functorial publication apply within E.17's optional morphism profile. E.18 adds the structure-scope constraints in S3 and **CC-E18-09 and CC-E18-10**; it does not define a second publication semantics.

**GateCrossing (normative)**

**Definition.** A `GateCrossing` is E.18's structure-local transition from one exact `<FlowPositionRef, CtxState>` binding to another at one exact `OperationalGate(profile)`. It is selected when at least one `CtxState` binding changes and an applicable gate profile governs that transition. It is not a `U.Relation`, an F.9 `Bridge`, a gate decision, a plane conversion, an A.6.4 arrow or use assertion, a penalty, or a publication occurrence.

**Per-binding account.** For an ordinary binding change, one sentence or table row is enough: name the changed binding, its from and to values, the facts or claims that establish those values for this case, and any declaration or rule whose application is current. When a named downstream use needs replay, the same distinctions may be packaged in this local E.18 block:

```text
ChangedBindingAccount:  # local replay block, not an FPF kind or relation
  changedBindingId
  fromValueRef
  toValueRef
  establishingFactRefs[]?
  establishingClaimEpistemeRefs[]?
  applicableDeclarationRefs[]?
  applicableRuleRefs[]?
  ruleApplicationRefs[]?
  honestStop?
```

Facts or claims establish the case values. A declaration or rule supplies only the meaning, admissibility condition, or constraint it actually states; `ruleApplicationRefs` is present only when the current case depends on that rule applying to these values. A gate decision evaluates the crossing under A.21 and does not establish the underlying facts or apply a rule by itself. A permission claim is separate under A.2.8.PER and is cited only when authorization is current. None of those items entails another.

For example, an analytical use can change its unit binding from metres to centimetres using the applicable conversion and the actual source values. Retain those from/to values and the conversion basis. A gate is needed only if a current profile governs that change. A regulated calibration change before launch retains its applicable gate, required checks and any separate authorization; an unavailable case value remains missing information. If no governing rule states the conversion, return missing-governor.

| Changed binding or separately placed retargeting | Basis to distinguish, or honest stop |
| --- | --- |
| `L : U.ContextSlice` | From/to slice values; exact A.2.6 slice identity and current scope-membership facts or claims; the applicable membership predicate and its application only when that use depends on them. |
| `P : ReferencePlane` or units | From/to plane or unit values; their exact declarations; the applicable conversion rule and its current application when conversion is claimed. If the needed declaration, rule, application, or case fact is absent, name that missing item and stop. |
| member of `E⃗` | From/to versioned values and editions; any currentness or refresh claim under G.11. E.17 contributes only a separate publication relation when the ref is published. |
| `D : DesignRunTag` | From/to tag values and the facts that establish them. Keep the A.21 gate decision and any A.15.5 prospective work-entry result as separate values. |
| EntityOfConcern retargeting (outside `ChangedBindingIds`) | Exact endpoint epistemes and EntitiesOfConcern, one exact A.6.4 arrow r, separate q, exact current facts, and a separate current-case judgement. Retargeting is not a `CtxState` binding and creates no GateCrossing; any crossing in the same case rests on a changed `L`, `P`, `E⃗`, or `D` binding. Any operation application, applicable rule, and Work remain separate. A kind difference alone only reopens the C.2.1 identity test. |

`A.20` may supply an exact current constraint-validity result and witness or reason; `A.21` supplies the gate profile, retained check results, mapping, aggregate decision, and decision log. Neither supplies a changed locality, plane, edition, tag, retargeting fact, rule application, or permission claim.

**Canonical reference.** `CrossingRef := ⟨TFSRef, GateId, FromPositionRef, ToPositionRef, FromCtxStateRef, ToCtxStateRef, ChangedBindingIds, PathSliceId⟩`. A DecisionLog or downstream use that depends on the crossing cites this ref and the required per-binding accounts.

**CrossingBundle publication block.** Materialize a CrossingBundle only when a named selector, acceptance, audit, replay, or other downstream use relies on durable crossing evidence. The bundle is publication packaging under `E.17`, not a constituent of the crossing or gate decision. It contains the `CrossingRef`, `ChangedBindingAccountRefs[]`, `GateId`, the current `profileApplicationRef` and `GateDecisionResultRef` when a gate decision exists, an optional current `DecisionLogRef`, optional separately current `PermissionClaimEpistemeRefs[]`, `PublicationScopeId`, `PathSliceId`, and any current witness refs.
When that downstream use also relies on cross-semantic correspondence, add a separate F.9 block: the two exact `SchemeSenseCell` endpoints, the obtaining Bridge and its exact profile, the C.2.1 claim that says whether the Bridge suits this named structural use in the named direction under its rule and tolerance, and the current A.10 or B.3 reliance branch if reliance is claimed. A Bridge Card remains optional packaging and `CL` remains optional evidence shorthand; neither makes the structural crossing obtain, makes the gate pass, or grants the use.

A penalty appears only when one exact current policy applies to this crossing and its rule application to the crossing facts supports that penalty. Cite the policy and `PolicyIdRef`; when the claim also depends on who may issue or enforce it, cite the separately obtaining direct authority relation and its actual participants. E.18 derives no penalty from `CL`, plane difference, edition difference, or Bridge publication. If the policy, applicability, rule application, or any separately required authority fact is absent, make no penalty claim and infer no default.

**Term separation.** An internal connection is the position q of a selected relation occurrence. A subject-specific transfer has its own predicate and episode rule when that claim is needed. Transport denotes the named Phi conversion policies and registries (`TransportRegistry^Phi` under UNM); citing them does not establish an additional subject relation.

#### E.18:5.2 - S2 - Flows as valuations, paths and admissible uses

A flow valuation assigns declared values to connection positions and named cuts of one selected S. Its exact domain is:

```text
Dom_nu(S, B) =
  { connection(q) : q in Conn_S }
  disjoint-union
  { cut(k) : k in B }
```

For each cut k, name S, the path family being cut, its entry and exit boundaries, and the exact crossing incidences with their boundary sides. Retain every full q to which an incidence belongs. The cut must intersect every entry-to-exit path of that family. An empty family permits an empty cut; an incidence cut cannot interrupt a zero-length path between coincident boundaries. Minimality is required only when the declared use asks for it. These are cuts of a representation, not additional world-side relations or wholes.

nu is a typed partial mapping from this tagged domain to declared value channels under a named regime. State each consumed channel's ValueKind, units and Scale when applicable, any observation or assessment window required by that channel or receiving use, and interpretation basis. Distinguish actual observation, model estimate and counterfactual. A returned value, a rate, an uncertainty assessment and a source reference need different channel meanings. Unknown belongs only to a result domain that declares it; unresolved input, out-of-range value, inapplicability, notRun and error keep their different conditions.

A value on connection(q) concerns rho(q). It can report the value actually returned by a result binding or assess the present suitability of relying on that binding. It does not replace any participant of the occurrence. A counterfactual 42 assigned for a model calculation does not change a historical return of 40. A new assessment can be another valuation of the same S; replacing a selected actual result binding reopens R and S.

A cut value has its own rule. A role-indexed tuple may preserve all incident values and their multiplicity. A sum, minimum, probability or total physical flow requires its applicable aggregation law, including shared participants, dependence, duplicate counting and the empty case. Several drawn arms of one q are not several independent inputs.

**Construct a path.** A path is a finite sequence of compatible oriented incidence steps through the complete representation in 5.1. Use the direct predicate or use rule for a dependency direction. At every visited q retain the full occurrence and all required participants, including side inputs. A relation used as a participant retains the node identification stated in 5.1. Repeating a visit to q records another visit to the same place, not another actual episode.

Mathematical path composition concatenates sequences with matching endpoints and compatible interface designations. The empty path is an identity and concatenation is associative. These laws do not establish causal transitivity, actual Work order or composition of Transformations. E.18.2 may use another formalism with an explicit mapping and its own laws.

**Decide whether the path is admissible for this use.** Check its complete resolution and typing; all required n-ary inputs; compatible channels, regimes, units and source editions; the applicable comparison and aggregation conditions; and the budget or cycle rule. The conditions of a concatenation must be checked even if its two paths were individually admissible. A join that requires A and B cannot be enabled by a path from A with B omitted. Their applicable joint rule, rather than two binary arrows, determines the continuation.

For each relevant position-use, recover CtxState sigma = <L, P, Evec, D> under 5.1. A raw connection step preserves these use bindings; it does not assert equality of the physical states of all participants. Account explicitly for each changed binding. Where an applicable profile governs the transition, represent it at one OperationalGate by its GateCrossing. Retain SquareLaw evidence when the crossing rule requires it, Gamma pins on compare and launch faces, and any applicable LaunchGate condition for design/run changes. StructuralReinterpretation retains the separately established r, q and current-case judgement under CC-E18-06-EX.

A FlowValuation use therefore names S, the declared domain and value channels, nu and its regime, the relevant position-use bindings and any admissible path used by the claim. PublicationScopeId and PathSliceId are included when publication or slice-addressed use requires them. A PathSlice is a selected portion of a path; it does not become performed Work or an execution interval. Published slice uses pin PathSliceId; a changed relied-on premise or applicable sentinel trigger reopens the affected uses under 5.13. Re-emit faces whose current claim or required publication status changes; retain supported historical and unaffected uses. Section 5.13 extends the set of addressed slices to cover the complete actual dependency closure.

**Several valuations, a subflow or a network.** State, regime, path, slice and local tag differences alone do not reidentify S. Verify its four A.22 discriminators before treating nominal-load and emergency-load values as valuations of one organization. A parent-relative internal portion uses 5.2b. When separately identified TFS members and an obtaining cross-boundary relation are needed, preserve their identities and use E.18.NET; a connection position q is not a universal cross-member relation.

**What “flow = valuation” contributes.** This Eulerian account assigns a quantity or object to a declared place in an identified organization under a given regime. Revaluation makes changed assessments and values comparable without pretending that the description creates a new actual event. When the question instead depends on a particular delivery, receipt, displacement, possession or causal episode, retain the domain's complete transfer predicate, participants, applicability, extent and recurrence rule in R. Equal payloads can belong to different episodes; two descriptions can concern one episode. For an operation's actual use of an earlier result, exact A.6.1 bindings can already provide the needed distinction. A common arrow style supplies neither additional fact.


#### E.18:5.2a - Split-and-join structure discipline

Use split and join only as selected-structure relations inside one `TransformationFlowStructure`. A split separates one source locus, variant set, problem-side cue, or candidate family into several identified loci or flow valuations. A join relates several identified loci, selected sets, gates, measurements, or refresh returns back to one current structure position. Neither operation creates a new FPF kind, a new pattern, or a prescribed work procedure.

Minimum split-and-join use names the selected `TransformationFlowStructure`, the actual split or join predicate and its complete participants, any applicable membership-change policy, the obtaining selector relation and its returned set or archive when a selector is involved, the selected-set result declaration when current, the exact publication relation when that value is published, and all slices needed for the actual dependency closure when currentness changes (5.13). Apply the definitions and tests in `A.19.CPM`, `A.19.SelectorMechanism`, `C.18`, `C.19`, and `G.5` when comparator, selector, archive, pool, or result-declaration claims are current; use `E.17` for a source-backed publication face and return to source, `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability, `A.21` for a gate claim, and `G.11` for a refresh claim.

For evolutionary-engineering work, the same selected structure may contain, for example, loci for variant generation, retention, archive or front treatment, comparison, selected-set result declaration, actual publication, architecture-candidate movement, planning, performed work, effect measurement, residual triage, and refresh. E.18 defines the selected organization, its position and occurrence resolution, crossings, valuations, pins and dependency-addressed refresh. Apply the definitions and tests in `C.18`, `C.19`, and `G.5` when archive, pool, or selected-set result-declaration claims are current; use `E.17` for a source-backed publication face and return to source, `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability, `C.11` and `C.30` for their decision and architecture-candidate claims, the A.15 family for planning and performed Work, and `G.11` for refresh.

#### E.18:5.2b - Position and parent-relative subflow references

Use a `FlowPositionRef` to point to one structural position inside one exact TFS:

```text
FlowPositionRef := <
  transformationFlowStructureRef,
  localFlowPositionId
>
```

The pair is the complete position-reference identity. If the TFS is reidentified, the same local id resolves to a different position. A `FlowValuation`, `PathId`, `PathSliceId`, actual filling, `DesignRunTag`, value kind, and reference mode may qualify or bind a use of that position; none of them enters its identity. These use annotations do not override A.22: replacing a selected constituent or relation occurrence requires reidentification before reusing the reference.

Use a `SubflowRef` when the practitioner needs to select and revisit a detailed internal portion of one exact parent TFS without pretending that the portion is another structure:

```text
SubflowRef := <
  parentTransformationFlowStructureRef,
  exactIncludedFlowPositionRefs[],
  exactIncludedInternalRelationOccurrenceRefs[],
  exactBoundaryFlowPositionRefs[]
>
```

Every included and boundary position must resolve through `FlowPositionRef` in the same parent S. Each included occurrence is selected in that parent's R and resolves through its q without losing participant meanings or arity. A participant outside the included internal portion remains explicitly resolved at its parent boundary. If the required participants cannot resolve in that parent, the proposed portion is not an internal subflow. This parent-relative selection adds no world-side parthood, containment or membership relation.

The tuple is the complete `SubflowRef` identity. Replacing the parent, an included position, an included internal relation occurrence, or a boundary position gives another reference; reidentifying the parent invalidates the old resolution. Changing only a valuation, path or slice, tag, actual filling, graph, mathematical description, publication, or demonstrative view leaves the reference unchanged while the tuple still resolves. Branching, joining, or cycling inside the portion does not make it a network.

**Quick discriminator.** Grinding, dosing, and wetting may be shown as a coffee-preparation subflow while their positions, internal relation occurrences, entry, and exit all remain in one coffee-brewing TFS. If heating instead has its own TFS identity and boundary and an exact relation connects it to preparation, stop using `SubflowRef` and apply `E.18.NET`.

#### E.18:5.3 - S3 - Publication discipline (faces)

E.18 **imports E.17** wholesale **and associates MVPK faces with `PublicationScope` (USM)**.
**MVPK remains the source for:**
* the set of face designators (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`),
* pin discipline and Publication Characteristics (PC),
* “no new claims; in the optional morphism profile, no re‑listing of inputs and outputs and no Γ‑semantics on publication morphisms”.

E.18 **does not re-specify** these rules; it only adds **structure-scope obligations** for faces published over transformation-flow paths:

1. **Crossings on faces.** When a face publishes a GateCrossing, it cites the `CrossingRef`, `ChangedBindingAccountRefs[]`, `GateId`, and any current `GateDecisionResult`, optional `DecisionLog`, policy-application, or permission-claim refs. An F.9 Bridge block appears only for a separately established cross-semantic use; its optional card and `CL` do not replace those refs.
2. **Edition refs on faces.** A face that cites `CG-Spec`, `ComparatorSet`, `UNM.TransportRegistryPhi`, or another versioned value cites that exact value and edition. Edition citation alone requires no Bridge Card, UTS row, or semantic Bridge.
3. **ComparatorSet and set returns (structure-scope).** Any `ComparatorSet` and `SetSemanticsRef` used along a transformation-flow path carries **edition identifiers**; affected uses are reconsidered when a relied-on premise changes, and faces are **re-emitted** when the result or an applicable publication rule requires it; faces with comparison **return sets and declared partial orders** (no hidden scalarization), reusing MVPK's declared-order discipline.
4. **Gamma_time on compare and launch faces.** Every current compare or launch publication face on an E.18 path pins `Gamma_time`; implicit *latest* is not admissible. A.21 cites the exact current profile application and qualification window. **CHR avoids acceptance thresholds** (*NoThresholdsInCHR*); gate and threshold claims are carried by A.21 and Part G, while actual performed facts are established through independently obtaining relations involving exact Work occurrences under A.15.1. A source `unknown`, `notRun`, or error remains explicit before the current profile rule maps it to a gate decision.

> **Reminder.** MVPK supplies the "signature" naming rule, the optional morphism profile's input-output rule, arithmetic-visibility rules, and material numeric-pin requirements (E.17 §5.4-5.5). E.18 **does not weaken** those rules; `CC-E18-09` states the additional constraints on faces published along transformation-flow paths.

**Lean publish-mode (AssuranceLane-Lite).** Lean changes publication faces only, not policy or checks. A current face cites the `profileApplicationRef`, identified `GateCheckApplicationResult` refs, and `GateDecisionResultRef`; it cites a `DecisionLogRef` only when an audit, history, replay, or reuse record is current. The underlying check-application results remain unchanged.

**Decision stability and idempotency (gate-local).** A gate decision is recomputed when an input named by A.21 changes. Only a current reuse, cacheability, or stability claim needs an equivalence witness covering the inputs whose equality that claim relies on; an optional `DecisionLog` may cite it. Use G.6 for evidence-provenance path visibility and G.11 for refresh implications. E.18 does not prescribe storage formats, key shapes, or hashing schemes.

**Retargeting and semantic-Bridge boundary.**

An `EntityOfConcernRef` change is not established by a UTS row, mapping label, card, `CL`, or GateCrossing; a kind change alone only reopens the C.2.1 identity test. First recover the exact A.6.4 arrow r from its endpoints, arrow rule or designator, and formal equivalence. Separately recover q, whose ClaimGraph states the invariant, visible loss, named receiving use, conditions, and affirmative or negative polarity. Compare the exact current facts with q and keep the current-case judgement separate: `satisfies`, `fails`, or `cannot decide`; for `cannot decide`, name the exact missing fact and reopen condition. Any application occurrence and Work remain separate. If the use also needs a semantic relation between two exact local senses, apply F.9 separately and keep its own bounded-use claim, optional `CL`, evidence, and reliance separate.

#### E.18:5.4 - S4 - Assurance operations on connection positions

The four declarative assurance operations act on the annotation of connection(q) for a particular flow-use. rho resolves q to the selected occurrence. When the assertion concerns a participant, name that subject as well. The operations preserve CtxState and the identity of r.

| Operation | Useful action | Required subject basis |
| --- | --- | --- |
| ConstrainTo(q, rule) | Restrict the admissible region or policy for this use of the connection | Resolve the rule, applicability and restriction operation. An empty region is a possible result. Recompare S under A.22 only if the new content changes a constraint actually applied in selecting S |
| CalibrateTo(q, calibrationRef, target) | Cite the calibration edition used by the claim about the named measurement, instrument or output | Recover the target, calibration and direct calibration predicate. Attaching the reference does not calibrate an instrument or replace a returned value |
| CiteEvidence(q, evidenceRef, claim) | Cite identified evidence for the specified claim about r or a participant | Retain the direct evidence-use relation and bounded use; the citation does not itself establish truth, warrant or a gate result |
| AttributeTo(q, provenanceRef, subject) | Cite the provenance of the specified result, source or other subject | Retain the actual provenance predicate or the justified compound claim and its base relations; equal values or adjacent records do not establish provenance |

For a cut, identify the affected q values or state a separately governed aggregate-claim rule. Do not silently treat the cut as another subject relation. Declaration-change labels from A.6.6 may describe an edited assertion; they neither replace these operations nor establish their subject relations.

CalibrateTo may cite an edition already compatible with the current Evec binding. A change from C3 to C4 that changes that binding needs its from/to basis and a GateCrossing when an applicable profile governs the transition. The same rule applies to a changed plane, units declaration or locality; the assurance operation preserves the explicit changed-binding account. If the conversion governor is absent, return missing-governor; if required declarations or case values are unavailable, return missing-information; otherwise report the applicable rule’s positive, negative or inapplicable result.

A penalty requires an applicable current policy and its rule application. Cite PolicyIdRef and any separately needed authority relation and participants, and publish the result only in the assurance lane named by that policy. Calibration, a registry entry or CL alone supplies no penalty or gate decision.


#### E.18:5.5 - S5 - Comparability and aggregation

The comparison explanation applies under the following admissibility conditions:

* Use an already adequate common basis directly. Apply A.19.UNM before comparison when the CN-Spec, applicable protocol or receiving use requires re-expression; retain the normalization method, invariants, edition and any transport rule actually used. The comparison and aggregation still require their applicable rule, admissible operands and evidence. A missing compatible basis remains a comparison gap; a normalization label does not supply it.
* If the comparator defines a **declared partial order**, then returns are **sets or archives** (Pareto or Archive); if a **total order** is declared, it is the one provided by the comparator; otherwise set semantics apply and covert scalarization is out of scope here.
* If a claim is **ordinal-only**, publish comparison results under its declared order. Arithmetic transforms such as means and z-scores require a separately governed scoring method and Scale that support them under C.16; naming a comparator or downstream policy does not supply that justification.

**Edition-aware publication records for sets or archives (e.g., QD archives) pin `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and the exact `CharacteristicSpaceRef` with its separate `characteristicSpaceDescriptionRef: U.EpistemeRef` under A.19:5.1.1.1 when applicable; refresh covers all actual dependent uses under 5.13. For current selector, archive, pool, selected-set result-declaration, comparator, or refresh claims, apply the definitions and tests in `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11`. For actual publication, use `E.17` for a source-backed face and return to source and `E.24.PUB` for the occurrence, form, carrier, audience, bounded use, and availability.**

#### E.18:5.6 - S6 - Cycle discipline (Selection ↔ Planning)

* The selected structure may center a loop between the `SelectionAndTuning` locus, whose relation satisfies the named selector and comparator definitions or tests, and the `WorkPlanning` locus, which binds one exact `A.15.2 U.WorkPlan`. Any A.15.3 planned-filling row remains declaration-local content inside that WorkPlan.
* The Selection-Planning loop is represented under local **budget and max_iter** in `Γ_time`; at expiry, the exact selector relation returns its declared current set or archive outcome, such as `CandidateSet`, with the applicable partial-optimality status. If the next step needs changed tuning, a separately identified `U.WorkPlan` with any declaration-local A.15.3 planned-filling rows, or a separately identified configuration or policy that passes its own applicable rule, carries that tuning; it is not another entity returned by the selector. Further improvement is placed in the **next `PathSlice`** only through that explicit planning, configuration, policy, or refresh continuation.
* **Establish the comparison basis before the loop.** Use it directly when adequate; apply UNM when normalization is required. If the applicable measurement, currentness or UNM check finds missing or stale measurements, retain that finding. A freshness request remains a request. If the receiving use plans measurement refresh, A.15.2 identifies the exact WorkPlan; when a reusable declaration member must be pinned, A.15.3 adds only a declaration-local row inside that WorkPlan. For later dated refresh Work, recover each exact actual performer through A.13 and let A.15.1 independently admit the occurrence. Add F.6 only when the receiving use also consumes precise assignment-bound attribution; F.6 neither discovers the performer nor supplies classification, and its failure alone leaves independently admitted Work intact. Keep the later measurement and calibration separate. A `RefreshReport@Context` is likewise separate from the request, plan, Work, measurement, and calibration. A publication that states a calibration target cites the calibration reference and any applicable transport-conversion rule. A penalty requires its own current policy, applicability, rule application, and any authority relation actually used; calibration, conversion, registry publication, or a report supplies no penalty by itself.
* **Work-entry claim and actual Work stay distinct.** `workEntryClaimRef` designates one exact `U.WorkPlan`, A.15.5 readiness relation, or other prospective claim consumed by `LaunchGate`. If Work later occurs, each actual launch value is established only through an independently obtaining direct relation or exact A.6.1 application binding of that Work individual. A separate `FinalizeLaunchValues` episteme may then designate the Work occurrence and those facts; it neither performs Work nor fills slots in the occurrence.
> **Refresh orchestration.** Telemetry records and publications that designate an exact Work occurrence are **slice-scoped**, editions re-pinned, and faces **re-emitted**. Telemetry remains a separate episteme and does not constitute the occurrence.

#### E.18:5.7 - S7 - Selector semantics (G.5) and parity harness (G.9)
E.18 keeps set-return, archive preservation, and comparator refs visible along the path. It does not define selector, archive, dominance, or comparator semantics; those remain with `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` for current selector or comparator cases.

* **Selectors return sets.** Default **DominanceRegime** is `ParetoOnly`; **IlluminationSummary** (telemetry summary) and any coverage and regret telemetry quantities are **report-only telemetry** (reported), excluded from dominance **unless** a CAL policy promotes them as declared dominance inputs (policy-id in SCR).

`PortfolioMode=Archive` retains exploration evidence under G.5:4.4e and CC-G5.23. It neither activates QD nor names the emitted selector outcome. When an actual selector relation constructs or returns a QD archive, retain that archive under its C.18 and ArchiveConfig basis; a G.5 outcome is declared separately under G.5:4.4b–4.4e. When generation is in scope, pairs `{environment, method}` are managed under declared **EnvironmentValidityRegion** and **TransferRulesRef**; parity records and `PathSliceId` are pinned on publication. For current selector, archive, pool, selected-set result-declaration, comparator, or refresh claims, apply the definitions and tests in `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11`. For actual publication, use `E.17` for a source-backed face and return to source and `E.24.PUB` for the occurrence, form, carrier, audience, bounded use, and availability.

#### E.18:5.8 - S8 - Guard aggregation assignment and handling (USM §1.2)
* **USM.CompareGuard** and **USM.LaunchGuard** publish the guard-gate aggregation assignment field `GuardOwnerGateId`. The legacy field name is read here as a gate-reference assignment, not as an owner relation. Guard failures are **events** aggregated by the declared gate (not GateChecks).
* **Aggregation-assignment rules:** (i) `USM.LaunchGuard.aggregationGate = LaunchGateId(workEntryClaimRef)`, where the ref resolves to the exact prospective claim consumed by the gate and never to a not-yet-existing Work occurrence; (ii) inside a Subflow, `USM.CompareGuard.aggregationGate = OperationalGate(InSentinel)`; join loci cannot be assigned as guard-pin aggregation gates.

**Profile-application boundary (cross-reference).** A.21 distinguishes a `GateProfile` description from the exact current fact that applies it to one gate, subject, action, scope, and window. E.18 cites that application only where a current gate or crossing needs it; a profile name, matrix, branch, or `PathSlice` supplies no application or authority by itself.

**Scope-translation guards (cross-reference).** `A.2.6` defines and tests exact slice and scope membership and any actual translated-scope application. When that translation relies on different local senses, it additionally requires an obtaining F.9 Bridge, a separate affirmative C.2.1 bounded-use claim, and current A.10 or B.3 reliance. Use `A.21` for gate aggregation; no `CL` value or Bridge Card decides the guard.

**Error, timeout, or unknown (profile-bound).** Keep each source error, timeout, `unknown`, and `notRun` result explicit. The exact current profile application cites the rule and edition that maps that result to `abstain`, `pass`, `degrade`, or `block`; a profile name alone supplies no fixed fold, and no missing or unrun required result maps to `pass` or neutral `abstain`. The `GateDecisionResult` retains the mapping and rationale.

#### E.18:5.9 - S9 - Transport and crossings

* A GateCrossing records one selected-structure transition between exact source and receiving positions and `CtxState` bindings at one exact gate whose profile and decision test come from A.21. Cite A.2.6 for locality and scope membership, the current plane or units declaration and conversion rule, each versioned value and exact edition plus G.11 when refresh is current, A.21 for `DesignRunTag` and the gate decision, and A.15.5 for a prospective work-entry boundary. If no current predicate, applicability condition, occurrence rule, conversion rule, or decision test can state a claim on which the crossing depends, return `missing-governor`. If the governor exists and the available case basis is sufficient to apply its positive test but that test fails, return `factually unsupported`; if a fact or declaration needed to decide the test is unavailable, return `missing-information`. State a negative crossing only under an applicable non-obtaining criterion or complete closure basis and satisfying facts.
* A semantic F.9 Bridge is additional, not constitutive. Use it only when the case identifies two exact F.17 `SchemeSenseCell` values from different semantic contexts and the Bridge predicate actually obtains. Keep the proposed structural use in a separate C.2.1 claim, recover current A.10 or B.3 reliance when relied on, and keep any Bridge Card or `CL` optional and non-constitutive.
* An EntityOfConcern change remains with A.6.4. E.18 may place the independently identified r, q, and current-case judgement; it creates none of them, records no operation application by implication, and supplies no `KindBridge` or mandatory `CL`. `T^D↔T^R` is handled at the exact A.21 gate with `DesignRunTagFrom` and `DesignRunTagTo` and the current A.15.5 or publication locus, without implying Work occurred.

#### E.18:5.10 - S10 - Non‑mechanism boundary

* Within E.17's optional morphism profile, publication uses typed projections that carry no Γ-semantics. Ordinary publication uses E.24.PUB's form, carrier and publication relations. Building, rendering or uploading is separate work on carriers; a claimed dated Work occurrence still needs its A.15.1 basis.

#### E.18:5.11 - S11 - Coordination wording labels (when current)
Coordination wording may be published as **LexicalView** labels over a P2W carry-through flow valuation; it is orientation-only unless an exact structural crossing, work relation, semantic Bridge, or gate decision is independently current. It adds no current structure locus kind, checks, or mechanisms. A published crossing cites `CrossingRef` and `ChangedBindingAccountRefs[]`, with gate-decision and permission-claim refs separate when current; an F.9 block is added only for a separately established semantic Bridge and bounded use.

#### E.18:5.12 - S12 - Exact viewpoint references to E.18 constructs

**Use this when.** Use S12 only when a current claim maps one exact viewpoint episteme to exact E.18 constructs. Ordinary work with a selected transformation-flow structure, valuation, path slice, or crossing does not open S12, and one mapping may stop after one row.

**Imported interface.** E.17.0 defines viewpoint membership and episteme–viewpoint conformance. E.17.1 defines local catalogue declarations and `U.ViewpointRef` members. E.17.2 provides the project-local TEVB authoring template; it ships no catalogue, reference, or viewpoint episteme value. S12 uses those results and does not copy their catalogue or conformance procedure. E.24.PUB defines publication, and C.29 defines any separately current representation or correspondence.

**First useful move.** Resolve one `viewpointRef : U.ViewpointRef` under the effective reference scheme to the named viewpoint episteme. Then name only the E.18 participant positions, selected internal relation occurrences r, resolved connection positions q, gates, crossings, paths or valuations consumed by the mapping. A relation reference names r under its direct predicate; a connection reference names q with rho(q)=r. The viewpoint reference is not a relation, the viewpoint episteme is not a template position, and the mapping establishes neither the selected subject relations nor episteme–viewpoint conformance.

Stop there unless the current claim separately needs candidate-view conformance, whole-family coverage, retargeting, cross-context meaning, publication, representation, or actual Work. Follow the defining pattern for that claim rather than reproducing it here. A token such as `VP.Functional` may remain P's ordinary reader-facing designator after resolution; it is not a viewpoint id, reference, family member, or conformance result.

| Project-local TEVB position | Exact reference resolution | E.18-specific mapping contribution |
|---|---|---|
| function-oriented | exact `r_functional : U.ViewpointRef` resolves exact `P_functional` under the effective scheme | Name the exact transformation-flow structure, valuation, transformation or capability-facing loci, gates, crossings, paths, and current comparator or publication pins that the mapping actually consumes. Any actual Work and exact performer are independently established through A.13 and A.15.1. Add F.6 only when the mapping also consumes precise assignment-bound attribution; missing or failed F.6 alone leaves independently admitted Work intact, with any invalidated A.13/A.15.1 premise and dependent conclusion rechecked. |
| procedure-oriented | exact `r_procedural : U.ViewpointRef` resolves exact `P_procedural` under the effective scheme | Name the references used by the mapping to `U.WorkPlan`, dated Work, state, selected internal relation occurrences r, resolved connection positions q, gates, paths or valuations. A gate may decide attempted entry; it creates no Work occurrence. |
| allocation-responsibility | exact `r_allocation : U.ViewpointRef` resolves exact `P_allocation` under the effective scheme | Identify only the E.18 interfaces, participant positions, selected internal relation occurrences r, resolved connection positions q, gates, crossings or valuations consumed by the mapping. Local system-role kinds, C.3.2 classification judgments, A.2.1 assignments, supervision, and responsibility or authority relations remain separate claims under their defining patterns. |
| module interface | `r_module : U.ViewpointRef` resolves `P_module` under the effective scheme | Name the Signature and Mechanism loci, selected internal relation occurrences r, resolved connection positions q, gates, crossings, paths or valuations used by the module-interface mapping. A different described subject needs A.6.4 retargeting; a changed `CtxState` binding uses the E.18 crossing rule. |

The four rows use one grammar: an exact reference resolves exact P, and a separately current mapping claim names the E.18 constructs it uses. A project may use one row without materializing the other three. Four rows are required only by a separately identified whole-family coverage claim under E.17.1/E.17.2.

**Conditional map row.** Persist `UTS.ViewpointMap` only when the mapping claim is made or consumed:

```text
UTS.ViewpointMapRow:
  EffectiveReferenceSchemeRef:
  ViewpointRef: exact U.ViewpointRef
  ResolvedViewpointEpistemeRef: exact P
  PrimaryE18ConstructRefs[]:
  MappingClaimEpistemeRef?: when the mapping claim is persisted separately
  CandidateEpistemeRef?: only with an obtaining E/P conformance relation
  EpistemeViewpointConformanceRelationRef?: only with CandidateEpistemeRef
  CrossingRefs[]?: only crossings consumed by the mapping
  GateRefs[]?: only gates consumed by the mapping
  PublicationUseRef?: only an independently current E.24.PUB use
  RepresentationRelationRef?: only an independently current C.29 relation
```

The optional branches carry references to independently established results. They do not repeat the classification, assignment, responsibility, Work, publication, representation, Bridge, or retargeting tests. If a semantic-context comparison is current, use the exact F.17/F.9 path and bounded-use claim; catalogue provenance or equal labels supply none of them.

**S12-scoped checks, only when `UTS.ViewpointMap` is current.**

1. `ViewpointRef` resolves exact P under the stated effective scheme. The row never calls the reference a relation or P a position.
2. Every `PrimaryE18ConstructRef`, crossing, and gate resolves the exact E.18 value or occurrence consumed by the mapping; the row creates none of them.
3. Candidate-view, whole-family, publication, representation, cross-context, retargeting, and Work branches appear only when that separate claim is current and cite its defining pattern's result.
4. One-viewpoint use needs one row. Familiar labels or four unbound template names establish no whole-family coverage.

#### E.18:5.13 - Refresh every actual dependent use

Start with the exact changed source, binding, calibration edition, rule or result. Recover the actual argument-use, premise-use, source-use or other dependence relations that determine which continuations rely on it. The incidence representation helps locate them; graph reachability alone does not establish a dependency.

Apply G.11 to obtain the least closed set containing those direct uses and every further use whose result or admissibility depends on them. Include both dependent branches and their join, and further gate or publication uses. At an n-ary use, recover every operand so that reconsideration is complete; an independently supported operand may be reused. Stop expanding only when no such unresolved dependency remains. A known dependence on an unavailable new value remains in the affected set with its governed unknown or stop.

Use PathSlice identifiers to address the work, and extend the set of addressed slices until it covers that closure. A changed source shared by two slices reopens both and their join. A cross-member dependency follows the exact E.18.NET relation and retains each member's local state. “Slice-local” means that each action is addressed to the affected portion; it does not confine refresh to the slice that first detected the change.

For each affected use, decide whether its direct rule permits current reliance on the old result, requires a new assessment, requires a new application, or stops continuation. A stale judgement does not erase an actual historical occurrence. A new application has its own bindings; selecting those instead of the old occurrences reopens A.22 identity. Reconsidering a use does not automatically require rerunning it.

Join the refreshed branches only when all the inputs required by the join rule are available and compatible, including their relevant editions. When a new gate decision is required, publish it separately under A.21. Re-emit a face when its current claim or required publication status changes. Preserve unaffected results and independently supported uses.


