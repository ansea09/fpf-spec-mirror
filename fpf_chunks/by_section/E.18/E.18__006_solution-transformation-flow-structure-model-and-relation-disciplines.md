---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transformation Flow Structure"
section_id: "E.18:5"
section_title: "Solution - Transformation-flow structure model and relation disciplines"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__006_solution-transformation-flow-structure-model-and-relation-disciplines.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "E.18 — Transformation Flow Structure"
  - "E.18:5 — Solution - Transformation-flow structure model and relation disciplines"
line_start: 84086
line_end: 84418
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
**Dominant Solution uses.** In ordinary E.18 use, keep five structure uses primary: name one selected transformation-flow structure; distinguish the selected structure from a flow valuation and from its mathematical descriptions; place gates only on crossings or on a pre-run work-entry claim; preserve normalize-before-compare and set-return discipline; and keep cycles under budget plus `PathSlice` refresh. A gate may authorize or block an intended entry, but it neither creates a future Work occurrence nor fills fields in one. S12 viewpoint mapping remains conditional viewpoint-mapping input when engineering or publication viewpoint mapping is current.

#### E.18:5.1 - S1 - Selected Structure (conceptual)

Define a **typed, editioned transformation-flow structure**
`TransformationFlowStructure := (Loci, Transfer, tau_L, tau_Transfer, Gamma_time, CrossingRefs, TransportRegistryRefs)`
with:

* **Loci:** structure positions or bindings to independently defined or constrained FPF values (open world). Common specialisations **include but are not limited to** one first-principles P2W example: an independently identified actual bounded `U.Transformation`, `U.Signature(profile=FormalSubstrate)`, `U.PrincipleFrame`, `U.Mechanism`, `U.ContextNormalization (UNM)`, a selector relation that satisfies the current selector and comparator definitions or tests, `A.15.2 U.WorkPlan` or a plan-item relation, one exact Work individual admitted under `U.Work`, and current evaluation or currentness relations. This list is **illustrative**, not exhaustive, and none of its entries is mandatory for general P2W. A structure position may be expressed by a morphism, graph vertex, tuple position, or category-theoretic object under a mathematical lens when that lens is current, but E.18 does not make every position a `U.Morphism`, graph vertex, or `U.Transformation`. Selection into the same structure, path adjacency, shared work, or a common affected referent supplies neither the `A.3.4` actuality basis nor the facts, predicate, and identity rule needed for a transformation-composition claim.
* **Transfer relation:** a **single relation kind `U.Transfer`** (typed) carrying carrier refs and token refs inside one selected TFS. Raw transfer preserves `CtxState`. Every actual change to a locality, plane, edition, or design/run binding is represented by one `GateCrossing` at an `OperationalGate(profile)` and has one local per-binding account that separates from/to values, establishing facts or claims, applicable declarations or rules, and current applications. An exact A.6.4 retargeting with unchanged `CtxState` follows the limited `StructuralReinterpretation` route in CC-E18-06-EX instead of becoming a crossing. Transport conversions cite the exact registry entry, conversion rule, and applicable policy. E.18 defines neither a generic semantic Bridge nor a generic penalty policy.
* **Scopes:** `Gamma_time` (budgets, horizons), `PublicationScope` for faces (E.17), and **slice ids** for refresh (G.11).

 **CtxState (PS‑projection; closed slots):** `CtxState = ⟨L, P, E⃗, D⟩` is the **projection of E.17 Publication Scope**.
 **Slot definitions and changed-binding account boundary (normative):**
  • `L := Locus` — one exact `U.ContextSlice` value identified under `A.2.6`; any scope-membership or translated-scope claim remains with A.2.6 and its current F.9/C.2.1/A.10-or-B.3 premises when semantic translation is actually required.
  • `P := ReferencePlane` — a ref-only binding to the exact plane and units declaration used by the current case. E.18 supplies no generic plane conversion. Cite the current declaration and applicable conversion rule by value. Return `missing-governor` only when no current conversion predicate or rule can state the attempted crossing; return `missing-information` when the needed declaration or case values are unavailable; when the rule and facts are current, state its positive, negative, or inapplicable result rather than a generic blocker.
  • `E⃗ := Edition vector` — a partial map `edition_key ↦ EditionId` whose members cite each versioned value, its exact edition, and the registry or declaration that assigns that edition; `G.11` defines the edition-bump and refresh records, while `E.17` defines publication of the refs.
  • `D := DesignRunTag` — `design(T^D)` or `run(T^R)` only as consumed by the exact `A.21` gate and, at work entry, the `A.15.5` readiness claim; the tag does not identify or create Work.
 **Invariants.** Raw `U.Transfer` preserves `CtxState` (`⟨L,P,E⃗,D⟩`): it does **not** write or update any CtxState slot; any CtxState write or update, including a design-to-run tag change for a pre-run work-entry claim, occurs at `OperationalGate(profile)`. The gate changes the claim or decision state, not the ontic identity of a Work occurrence or any independently obtaining relation involving it.
 **Extension discipline.** A conforming use registers any extra slot beyond ⟨L,P,E⃗,D⟩ in the **E.17 publication discipline and the E.18 LEX “CtxState Extension Registry”** with slot‑id, intent, partial‑order rule (neutral or absorbing), and SquareLaw compatibility; unregistered extensions are non‑conformant.
 **Data-shape location.** E.18 names the structure and valuation obligations for `PathId`, `PathSliceId`, Gamma pins, and lineage: flow is a valuation over `U.Transfer`, raw transfer preserves `CtxState`, and path or slice evidence is carried through this pattern plus `A.20`, with `G.6` for evidence-provenance path visibility and `G.11` for refresh wiring. These are the current structure loci for path and slice currentness.

 * **Locus kinds:** `Transformation`, `Signature`, `Mechanism`, `WorkPlanning`, `Work`, `Check`, and `StructuralReinterpretation` are the current minimal structure-positioned locus baseline. Domain-specific species are open-world and non-exhaustive, but each species binds to one of the locus kinds or requires an explicit E.18 update. These are positioned loci in the selected structure, not a local taxonomy of new FPF kinds.
  **Exact identification (no local ontology):**
  — `Transformation` **≡** **A.3.4** `U.Transformation` only when the structure locus binds one independently identified actual bounded change with its exact changed referent, extent or ordering boundary, boundary conditions, actual change facts, and continuity or reidentification rule. Desired, intended, planned, modeled, selected, described, evaluated, published, or transferred change content remains under the definition or test for that exact claim; it is not a `Transformation` binding merely because it occupies the selected structure. Current-resolution identification establishes neither finer parts nor partlessness. A positive transformation-composition, `TransformationPartOfRelation`, composite-transformation identity, or transformation-holonhood claim stops under D14.16 with the exact A.6.RCD result: `TC-MWH missing-governor` only when no current predicate, applicability condition, or occurrence rule states the required contribution, compatibility, parthood, or whole-identity claim; `TC-MWH factually unsupported` when the governor exists and the available case basis is sufficient to apply its positive test but that test fails; and `TC-MWH missing-information` when a fact needed to decide the test is unavailable. A negative needs its own applicable non-obtaining criterion or complete closure basis and satisfying facts. E.18 retains the independently identified transformations and supplies no provisional contribution, compatibility, parthood, or whole-change architecture; it does not preselect whether a later settlement uses a generic derived relation, subject-specific relations, local compound claims, or non-admission.
  — `Signature` **≡** **A.6.0** `U.Signature` (universal, law-governed declaration).
  — `Mechanism` **≡** **A.6.1** `U.Mechanism` (law-governed application over a SubjectKind and RangedValueKind), with placement and stabilization relations in `E.20` when current.
  — `WorkPlanning` **≡** **A.15.2** `U.WorkPlan` or its current plan-item relation when that plan or relation occupies the structure position.
  — `Work` **≡** an exact dated Work individual admitted under **A.15.1 `U.Work`**. A structure locus may point to that occurrence after it exists; before execution it points only to a `U.WorkPlan`, A.15.5 readiness relation, or another exact work-entry claim. No second enactment kind is introduced.
  — `Check` **≡** `OperationalGate(profile)` (universal **gate**; `A.20` supplies the CV test when internal step validity is current, and `A.21` defines gate profile, check aggregation, decision, and publication minima when gate fit or gate decision is current).
  — `StructuralReinterpretation` is only the E.18 position of an exact retargeting that satisfies the `A.6.4` definition and test; it is not a new retargeting kind. E.18 records source and receiving EntityOfConcern refs, preserved invariant, path-slice locality, and the A.6.4 witness. A semantic F.9 Bridge is additional and current only when two exact F.17 cells and the F.9 predicate are independently established; any suitability for this retargeting is a separate C.2.1 bounded-use claim with current A.10 or B.3 reliance when relied on. The legacy A.6.4 `KindBridge`/`CL` consumer wording remains parked under D14.17.3, so a case that requires that absent rule returns `missing-governor` rather than borrowing it here.
  `OperationalGate` is the E.18 check locus with DecisionLog aggregation. A check-locus label names only the current gate or check value that the selected structure positions: `A.20` supplies the internal-constraint-validity test when that claim is current, `A.21` defines gate profile, aggregation, decision, and publication minima when gate fit or gate decision is current, and `A.3.4` defines and tests the bounded transformation claim that the check constrains.
  E.18 adds only a structure-local placement rule: when the exact A.6.4 retargeting is current and `CtxState` is unchanged, record its witness and `PathSliceId` without calling it a GateCrossing. If any `CtxState` binding changes, the path uses a GateCrossing and states the changed binding's from/to values, establishing basis, and any applicable declaration, rule, and current application. A Bridge, card, UTS row, `CL`, witness publication, gate decision, or permission claim neither creates the retargeting nor establishes the underlying binding change.
> **MVPK integration (import).** Every locus with an external publication face is published via **MVPK** faces (`PlainView`, `TechCard`, `AssuranceLane`, `InteropCard`) under a declared **PublicationScope** (E.17). E.18 **reuses** MVPK's publication rules (pins, declared-order discipline, "no new numeric claims and no re-listing of inputs and outputs") and only adds structure-scope constraints in S3 and **CC-E18-09 and CC-E18-10**; it does **not** define a second, local publication semantics.

**GateCrossing (normative)**

**Definition.** A `GateCrossing` is E.18's structure-local transition from one exact `<FlowPositionRef, CtxState>` binding to another at one exact `OperationalGate(profile)`. It is selected only when at least one `CtxState` binding changes. It is not a `U.Relation`, an F.9 `Bridge`, a gate decision, a plane conversion, a retargeting occurrence, a penalty, or a publication occurrence.

**Per-binding account.** For an ordinary local crossing, one sentence or table row is enough: name the changed binding, its from and to values, the facts or claims that establish those values for this case, and any declaration or rule whose application is current. No record is required. When a named downstream use needs replay, the same distinctions may be packaged in this local E.18 block:

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

| Changed binding | Basis to distinguish, or honest stop |
| --- | --- |
| `L : U.ContextSlice` | From/to slice values; exact A.2.6 slice identity and current scope-membership facts or claims; the applicable membership predicate and its application only when that use depends on them. |
| `P : ReferencePlane` or units | From/to plane or unit values; their exact declarations; the applicable conversion rule and its current application when conversion is claimed. If the needed declaration, rule, application, or case fact is absent, name that missing item and stop. |
| member of `E⃗` | From/to versioned values and editions; any currentness or refresh claim under G.11. E.17 contributes only a separate publication relation when the ref is published. |
| `D : DesignRunTag` | From/to tag values and the facts that establish them. Keep the A.21 gate decision and any A.15.5 prospective work-entry result as separate values. |
| EntityOfConcern or kind retargeting | From/to subjects or kinds, one exact A.6.4 retargeting occurrence and witness, and any separately applicable rule/application. A legacy `KindBridge`/`CL` dependency remains the D14.17.3 stop. |

`A.20` may supply a current CV or SquareLaw witness; `A.21` supplies GateProfile, check aggregation, GateDecision, and DecisionLog. Neither one supplies the changed locality, plane, edition, tag, retargeting fact, rule application, or permission claim.

**Canonical reference.** `CrossingRef := ⟨TFSRef, GateId, FromPositionRef, ToPositionRef, FromCtxStateRef, ToCtxStateRef, ChangedBindingIds, PathSliceId⟩`. A DecisionLog or downstream use that depends on the crossing cites this ref and the required per-binding accounts.

**CrossingBundle publication block.** Materialize a CrossingBundle only when a named selector, acceptance, audit, replay, or other downstream use relies on durable crossing evidence. The bundle is publication packaging under `E.17`, not a constituent of the crossing or gate decision. It contains the `CrossingRef`, `ChangedBindingAccountRefs[]`, `GateId`, `GateProfileRef`, any current `GateDecisionRef` and `DecisionLogRef`, optional separately current `PermissionClaimEpistemeRefs[]`, `PublicationScopeId`, `PathSliceId`, and any current witness refs.
When that downstream use also relies on cross-semantic correspondence, add a separate F.9 block: the two exact `SchemeSenseCell` endpoints, the obtaining Bridge and its exact profile, the C.2.1 claim that says whether the Bridge suits this named structural use in the named direction under its rule and tolerance, and the current A.10 or B.3 reliance branch if reliance is claimed. A Bridge Card remains optional packaging and `CL` remains optional evidence shorthand; neither makes the structural crossing obtain, makes the gate pass, or grants the use.

A penalty appears only when one exact current policy applies to this crossing and its rule application to the crossing facts supports that penalty. Cite the policy and `PolicyIdRef`; when the claim also depends on who may issue or enforce it, cite the separately obtaining direct authority relation and its actual participants. E.18 derives no penalty from `CL`, plane difference, edition difference, or Bridge publication. If the policy, applicability, rule application, or any separately required authority fact is absent, make no penalty claim and infer no default.

**Term separation.** **Transfer** denotes the sole relation kind `U.Transfer` in the selected structure. **Transport** denotes Phi-governed conversion **policies and registries** (**`TransportRegistry^Phi`** under UNM). Wording "reuse via Transport" refers to registries and policies, not to an additional transfer relation.

#### E.18:5.2 - S2 - Flows as valuations (paths, state, and guards)
* A **Flow** is a **valuation** `nu` over internal `U.Transfer` occurrences and cut-sets of one exact selected TFS, paired with an **admissible path** `p = v0 -> ... -> vk` in that structure. The valuation maps transfer occurrences or cut-sets to token and state values under `CtxState` and links publication-event records to a declared `PublicationScopeId`; it is not itself the performed work. E.18 specifies the concrete path and slice publication pins and identifiers (`PathId`, `PathSliceId`, Gamma_time on compare and launch faces); apply `A.20` when CV witnesses are current, `G.6` for evidence-provenance path visibility, and `G.11` for refresh wiring. This reflects the "selected structure != flow" norm (flow = valuation), with gates placed exactly on GateCrossings.
* **Several valuations of one TFS.** One `TransformationFlowStructure` may carry several flow valuations only after the use identifies the same exact TFS and its structural boundary for every valuation. For example, nominal-load and emergency-load valuations may differ in state values, paths, slices, or local `DesignRunTag` bindings while still using the same cooling-loop structure and the same internal transfer occurrences. Labels such as development, application, evaluation, refresh, or feedback do not establish that shared identity.
* **Leave E.18 at a member boundary.** `U.Transfer` relates positions only inside that one selected TFS. When candidate flows have independently identified TFS boundaries, separate identified objects or Work occurrences, and a relation across their positions, keep each TFS and its valuations local and use `E.18.NET` with the exact cross-boundary relation predicate and occurrence rule. Do not turn `U.Transfer`, adjacency, a carried product, or a feedback arrow into a universal cross-flow relation.
* **Admissible path (definition).** A path `p` is **admissible** iff:
  (a) locus kinds and transfer relation kinds match the declared `tau_L, tau_Transfer`;
  (b) any write or update to any member of `⟨L,P,E⃗,D⟩` appears at **exactly one** `OperationalGate(profile)`. An exact A.6.4 retargeting with unchanged `CtxState` follows CC-E18-06-EX without a crossing; if that retargeting also changes a `CtxState` binding, the changed binding appears at exactly one gate;
  (c) each GateCrossing on `p` has a **SquareLaw witness** (CC-E18‑23), while an exact A.6.4 retargeting separately carries the direct retargeting witness required by CC-E18‑06‑EX;
  (d) no hidden crossings occur across raw transfers;
  (e) Γ‑pins are present on compare and launch faces;
  (f) `T^D↔T^R` occurs **only** at `LaunchGate`.

* `U.Transfer` preserves `CtxState` (`⟨L,P,E⃗,D⟩`) and carries **Assurance‑operations** only (see S3b); any crossing of locus, plane, edition, or `T^D↔T^R` is placed at `OperationalGate(profile)`.
* A **PathSlice** is a selected portion of one path used to scope refresh and telemetry; faces pin `PathSliceId`; **re‑emission** happens when any pinned edition changes or `SliceRefresh` is triggered by sentinel rules. The slice is not performed work or an execution interval merely because it bounds those observations.

> **Consequences.** One P2W practitioner application, or its optional C.2.1 carry-through note or stop description, may cite one path `p` in a `TransformationFlowStructure` only when the receiving decision or use relies on explicit selected-structure content. E.18.1 describes that carry-through practice and defines the local claim content; it introduces no `ProblemToWorkCarryThroughRelation@Context`, and the path is not such a relation. Each returned method, plan, Work, transformation, evaluation, decision, entity, or relation occurrence keeps its independent identity and uses the pattern that defines or constrains the current claim about it. Other domains, including supply chains, water networks, and neural-network function structures, may instantiate different paths under E.18.
>
**Why "flow = valuation" preserves the ordinary "some state changes" intuition**
There are two complementary perspectives:
* **Lagrangian (intuitive):** track tokens or state changes through a physical, organizational, or computational network.
* **Eulerian (structural):** define a **function on transfer relations** ("which quantity or object is associated with each relation under a given regime"), with gate rules. E.18 deliberately fixes the **Eulerian semantics of flow** at the selected-structure scope: "flow (= valuation) with publication log", while change over time appears as **re-valuation** over a **PathSlice** (the selected path portion whose identifier scopes refresh and republication) under gate rules and the SquareLaw. This yields comparability, reproducibility, and slice-local refresh.

#### E.18:5.2a - Split-and-join structure discipline

Use split and join only as selected-structure relations inside one `TransformationFlowStructure`. A split separates one source locus, variant set, problem-side cue, or candidate family into several identified loci or flow valuations. A join relates several identified loci, selected sets, gates, measurements, or refresh returns back to one current structure position. Neither operation creates a new FPF kind, a new pattern, or a prescribed work procedure.

Minimum split-and-join use names the selected `TransformationFlowStructure`, the exact split or join predicate or policy when membership changes, the set or archive returned by the exact selector relation, the selected-set result declaration when current, the exact publication relation when that value is published, and the smallest refresh scope when currentness changes. Apply the definitions and tests in `A.19.CPM`, `A.19.SelectorMechanism`, `C.18`, `C.19`, and `G.5` when comparator, selector, archive, pool, or result-declaration claims are current; use `E.17` for a source-backed publication face and return to source, `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability, `A.21` for a gate claim, and `G.11` for a refresh claim.

For evolutionary-engineering work, the same selected structure may contain, for example, loci for variant generation, retention, archive or front treatment, comparison, selected-set result declaration, actual publication, architecture-candidate movement, planning, performed work, effect measurement, residual triage, and refresh. E.18 defines only the structure, loci, `U.Transfer`, crossings, valuations, pins, and slice-local refresh. Apply the definitions and tests in `C.18`, `C.19`, and `G.5` when archive, pool, or selected-set result-declaration claims are current; use `E.17` for a source-backed publication face and return to source, `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability, `C.11` and `C.30` for their decision and architecture-candidate claims, the A.15 family for planning and performed Work, and `G.11` for refresh.

#### E.18:5.2b - Position and parent-relative subflow references

Use a `FlowPositionRef` to point to one structural position inside one exact TFS:

```text
FlowPositionRef := <
  transformationFlowStructureRef,
  localFlowPositionId
>
```

The pair is the complete position-reference identity. If the TFS is reidentified, the same local id resolves to a different position. A `FlowValuation`, `PathId`, `PathSliceId`, actual filling, `DesignRunTag`, value kind, and reference mode may qualify or bind a use of that position; none of them enters its identity.

Use a `SubflowRef` when the practitioner needs to select and revisit a detailed internal portion of one exact parent TFS without pretending that the portion is another structure:

```text
SubflowRef := <
  parentTransformationFlowStructureRef,
  exactIncludedFlowPositionRefs[],
  exactIncludedInternalTransferOccurrenceRefs[],
  exactBoundaryFlowPositionRefs[]
>
```

Every included and boundary position must resolve through `FlowPositionRef` to the same exact parent. Every included transfer must already obtain as an internal `U.Transfer` occurrence in that parent. A boundary position remains a position of the parent; an internal transfer crossing from an included to an excluded parent position marks the return to the parent. This resolution supplies the parent/subflow connection. It does not introduce parthood, containment, embedding, or membership as another world-side relation.

The tuple is the complete `SubflowRef` identity. Replacing the parent, an included position, an included internal transfer occurrence, or a boundary position gives another reference; reidentifying the parent invalidates the old resolution. Changing only a valuation, path or slice, tag, actual filling, graph, mathematical description, publication, or demonstrative view leaves the reference unchanged while the tuple still resolves. Branching, joining, or cycling inside the portion does not make it a network.

**Quick discriminator.** Grinding, dosing, and wetting may be shown as a coffee-preparation subflow while their positions, internal transfers, entry, and exit all remain in one coffee-brewing TFS. If heating instead has its own TFS identity and boundary and an exact relation connects it to preparation, stop using `SubflowRef` and apply `E.18.NET`.

#### E.18:5.3 - S3 - Publication discipline (faces)



E.18 **imports E.17** wholesale **and associates MVPK faces with `PublicationScope` (USM)**.
**MVPK remains the source for:**
* the set of face kinds (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`),
* pin discipline and Publication Characteristics (PC),
* “no new numeric claims, no re‑listing of inputs and outputs, and no Γ‑semantics on faces”.

E.18 **does not re-specify** these rules; it only adds **structure-scope obligations** for faces published over transformation-flow paths:

1. **Crossings on faces.** When a face publishes a GateCrossing, it cites the `CrossingRef`, `ChangedBindingAccountRefs[]`, `GateId`, and any current GateDecision, DecisionLog, policy, or permission-claim refs. An F.9 Bridge block appears only for a separately established cross-semantic use; its optional card and `CL` do not replace those refs.
2. **Edition refs on faces.** A face that cites `CG-Spec`, `ComparatorSet`, `UNM.TransportRegistryPhi`, or another versioned value cites that exact value and edition. Edition citation alone requires no Bridge Card, UTS row, or semantic Bridge.
3. **ComparatorSet and set returns (structure-scope).** Any `ComparatorSet` and `SetSemanticsRef` used along a transformation-flow path carries **edition identifiers**; affected faces are **re-emitted** on edition change; faces with comparison **return sets and declared partial orders** (no hidden scalarization), reusing MVPK's declared-order discipline.
4. **Gamma_time on compare and launch faces.** All compare and launch faces on E.18 paths pin `Gamma_time`; implicit *latest* is not admissible. `A.21` carries current GateProfile binding and minimum profile semantics; E.18 paths include the pin. **CHR avoids acceptance thresholds** (*NoThresholdsInCHR*); gate and threshold claims are carried by `A.21` and Part G, while actual performed facts are established through independently obtaining relations involving exact Work occurrences under A.15.1. Unknowns remain tri-state (`pass|degrade|abstain`) and fold per the active GateProfile (`A.21`).

> **Reminder.** MVPK already bans "signature" on faces, input-output re-listing, arithmetic on faces, and unpinned numeric content (E.17 §5.4-5.5). E.18 **does not weaken or override** those rules; it only constrains how they are used along transformation-flow paths.

**Lean publish‑mode (AssuranceLane‑Lite).** Lean changes **publication faces only** (`PlainView`/`AssuranceLane` minimal), not checks; publication shows `GateProfile`, `GateCheckRef[]`, and `DecisionLogRef`; the underlying GateChecks list remains unchanged.

**Decision stability and idempotency (gate-local).** Gate decisions are stable under a declared equivalence relation over the pins used by `A.21`; the witness is recorded as `DecisionLog` or `EquivalenceWitnessRef`, with `G.6` used for evidence-provenance path visibility and `G.11` for refresh implications. E.18 **does not** prescribe storage formats, key shapes, or hashing schemes.

**Retargeting and semantic-Bridge boundary.**

An `EntityOfConcernRef` or kind change is not admitted by a UTS row, mapping label, card, `CL` value, or GateCrossing. First recover an exact A.6.4 retargeting with its source and receiving subjects, invariant, preserved and withdrawn commitments, applicability, and witness. If the retargeting also needs a semantic relation between different local senses, apply F.9 separately and keep its bounded-use claim and reliance branch separate. A use that requires the parked A.6.4 `KindBridge`/`CL` consumer rule returns the D14.17.3 `missing-governor` stop. For the current A.6.4 test itself, return `factually unsupported` when its governor exists and the available case basis is sufficient to apply the positive test but that test fails; return `missing-information` when a fact needed to decide the test is unavailable. Failure of the positive test alone establishes no negative retargeting claim.

#### E.18:5.4 - S4 - Assurance‑operations on `U.Transfer` (counterfactual admissibility)

On `U.Transfer` relations, an operation is interpreted as a **declarative assurance-operation** **iff** it is one of
`ConstrainTo(rule)`, `CalibrateTo(calibrationReference)`, `CiteEvidence(evidenceRef)`, or `AttributeTo(provenanceReference)`; otherwise this explanation does not apply.
Under this interpretation, `CtxState⟨L,P,E⃗,D⟩` is preserved.
If a claimed assurance operation would change plane or units, this assurance-operation explanation does not apply. Use a GateCrossing only after the exact plane or units declaration and applicable conversion rule are cited. Return `missing-governor` only if no current conversion predicate or rule can state the crossing, and `missing-information` if the declaration or case values needed to apply it are unavailable; otherwise state the rule's positive, negative, or inapplicable result.

If one exact current policy applies and its rule application supports a penalty, cite the policy and `PolicyIdRef` and publish the penalty only in the assurance lane specified by that policy. When the claim also depends on an issuing or enforcing authority, cite the separately obtaining direct authority relation and its actual participants. Otherwise no penalty claim appears here.

#### E.18:5.5 - S5 - Comparability and aggregation (normalize‑then‑compare; counterfactual form)

The comparison explanation applies under the following admissibility conditions:

* If a path segment intends to compare or aggregate, it is admissible as a comparison **only when** UNM precedes it; UNM is **method‑independent**, publishes **TransportRegistry^Phi** and **CG-Spec** references, and faces cite those editions; otherwise this comparison explanation does not apply.
* If the comparator defines a **declared partial order**, then returns are **sets or archives** (Pareto or Archive); if a **total order** is declared, it is the one provided by the comparator; otherwise set semantics apply and covert scalarization is out of scope here.
* If a claim is **ordinal‑only**, then only comparison results are published; arithmetic transforms (e.g., means and z‑scores) are out of scope of this explanation and belong to declared comparators or downstream policy.

**Edition-aware publication records for sets or archives (e.g., QD archives) pin `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and `CharacteristicSpaceRef.edition` when applicable; refresh is slice-local. For current selector, archive, pool, selected-set result-declaration, comparator, or refresh claims, apply the definitions and tests in `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11`. For actual publication, use `E.17` for a source-backed face and return to source and `E.24.PUB` for the occurrence, form, carrier, audience, bounded use, and availability.**

#### E.18:5.6 - S6 - Cycle discipline (Selection ↔ Planning)

* The selected structure may center a loop between the `SelectionAndTuning` locus, whose relation satisfies the named selector and comparator definitions or tests, and the `WorkPlanning` locus, which binds an `A.15.2 U.WorkPlan` or plan-item relation.
* The Selection-Planning loop is represented under local **budget and max_iter** in `Γ_time`; at expiry, the exact selector relation returns its declared current set or archive outcome, such as `CandidateSet`, with the applicable partial-optimality status. If the next step needs changed tuning, a separately identified `U.WorkPlan`, plan-item relation, configuration, or policy carries that tuning; it is not another entity returned by the selector. Further improvement is placed in the **next `PathSlice`** only through that explicit planning, configuration, policy, or refresh continuation.
* **UNM occurs before the loop.** When the normalized basis shows missing or stale measurements, retain the finding returned by the UNM test. A freshness request remains a request. If the receiving use plans measurement refresh, A.15.2 identifies the WorkPlan or plan item; only later dated Work admitted by A.15.1 performs the refresh, with F.6 identifying its performer and assignment. Keep the later measurement and calibration separate. A `RefreshReport@Context` is likewise separate from the request, plan, Work, measurement, and calibration. A publication that states a calibration target cites the calibration reference and any applicable transport-conversion rule. A penalty requires its own current policy, applicability, rule application, and any authority relation actually used; calibration, conversion, registry publication, or a report supplies no penalty by itself.
* **Work-entry claim and actual Work stay distinct.** `workEntryClaimRef` designates one exact `U.WorkPlan`, A.15.5 readiness relation, or other prospective claim consumed by `LaunchGate`. If Work later occurs, each actual launch value is established only through an independently obtaining direct relation or exact A.6.1 application binding of that Work individual. A separate `FinalizeLaunchValues` episteme may then designate the Work occurrence and those facts; it neither performs Work nor fills slots in the occurrence.
> **Refresh orchestration.** Telemetry records and publications that designate an exact Work occurrence are **slice-scoped**, editions re-pinned, and faces **re-emitted**. Telemetry remains a separate episteme and does not constitute the occurrence.

#### E.18:5.7 - S7 - Selector semantics (G.5) and parity harness (G.9)
E.18 keeps set-return, archive preservation, and comparator refs visible along the path. It does not define selector, archive, dominance, or comparator semantics; those remain with `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` for current selector or comparator cases.

* **Selectors return sets.** Default **DominanceRegime** is `ParetoOnly`; **IlluminationSummary** (telemetry summary) and any coverage and regret telemetry quantities are **report-only telemetry** (reported), excluded from dominance **unless** a CAL policy promotes them as declared dominance inputs (policy-id in SCR).

If `PortfolioMode=Archive`, a **QD archive** can be returned; when generation is in scope, pairs `{environment, method}` are managed under declared **EnvironmentValidityRegion** and **TransferRulesRef**; parity records and `PathSliceId` are pinned on publication. For current selector, archive, pool, selected-set result-declaration, comparator, or refresh claims, apply the definitions and tests in `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11`. For actual publication, use `E.17` for a source-backed face and return to source and `E.24.PUB` for the occurrence, form, carrier, audience, bounded use, and availability.

#### E.18:5.8 - S8 - Guard aggregation assignment and handling (USM §1.2)
* **USM.CompareGuard** and **USM.LaunchGuard** publish the guard-gate aggregation assignment field `GuardOwnerGateId`. The legacy field name is read here as a gate-reference assignment, not as an owner relation. Guard failures are **events** aggregated by the declared gate (not GateChecks).
* **Aggregation-assignment rules:** (i) `USM.LaunchGuard.aggregationGate = LaunchGateId(workEntryClaimRef)`, where the ref resolves to the exact prospective claim consumed by the gate and never to a not-yet-existing Work occurrence; (ii) inside a Subflow, `USM.CompareGuard.aggregationGate = OperationalGate(InSentinel)`; join loci cannot be assigned as guard-pin aggregation gates.

**GateProfile data shape (cross-reference).** `A.21` carries the current GateProfile binding and minimum profile semantics. E.18 names the structure only where crossings need it; fuller profile-matrix material has no current authority unless a cited pattern defines and admits that exact object.

**Scope-translation guards (cross-reference).** `A.2.6` defines and tests exact slice and scope membership and any actual translated-scope application. When that translation relies on different local senses, it additionally requires an obtaining F.9 Bridge, a separate affirmative C.2.1 bounded-use claim, and current A.10 or B.3 reliance. Use `A.21` for gate aggregation; no `CL` value or Bridge Card decides the guard.

**Error, timeout, or unknown (profile-bound).** GateCheck errors and timeouts fold to **`degrade`** under `Lean` or `Core` and to **`block`** under `SafetyCritical` or `RegulatedX`; `unknown` follows the declared GateCheck rule (safety-default: `degrade`). The `A.21` DecisionLog record and equivalence witness carry decision stability; E.18 does not define storage or key structures.

#### E.18:5.9 - S9 - Transport and crossings

* A GateCrossing records one selected-structure transition between exact source and receiving positions and `CtxState` bindings at one exact gate whose profile and decision test come from A.21. Cite A.2.6 for locality and scope membership, the current plane or units declaration and conversion rule, each versioned value and exact edition plus G.11 when refresh is current, A.21 for `DesignRunTag` and the gate decision, and A.15.5 for a prospective work-entry boundary. If no current predicate, applicability condition, occurrence rule, conversion rule, or decision test can state a claim on which the crossing depends, return `missing-governor`. If the governor exists and the available case basis is sufficient to apply its positive test but that test fails, return `factually unsupported`; if a fact or declaration needed to decide the test is unavailable, return `missing-information`. State a negative crossing only under an applicable non-obtaining criterion or complete closure basis and satisfying facts.
* A semantic F.9 Bridge is additional, not constitutive. Use it only when the case identifies two exact F.17 `SchemeSenseCell` values from different semantic contexts and the Bridge predicate actually obtains. Keep the proposed structural use in a separate C.2.1 claim, recover current A.10 or B.3 reliance when relied on, and keep any Bridge Card or `CL` optional and non-constitutive.
* An EntityOfConcern or kind change remains with A.6.4. The current A.6.4 legacy `KindBridge`/`CL` branch is parked under D14.17.3; E.18 records no positive substitute. `T^D↔T^R` is handled at the exact A.21 gate with `DesignRunTagFrom` and `DesignRunTagTo` and the current A.15.5 or publication locus, without implying Work occurred.

#### E.18:5.10 - S10 - Non‑mechanism boundary

* Publication is a **typed projection**, not execution. Any build, render, or upload is **Work on carriers**; faces do **not** carry Γ-semantics.

#### E.18:5.11 - S11 - Coordination wording labels (when current)
Coordination wording may be published as **LexicalView** labels over a P2W carry-through flow valuation; it is orientation-only unless an exact structural crossing, work relation, semantic Bridge, or gate decision is independently current. It adds no current structure locus kind, checks, or mechanisms. A published crossing cites `CrossingRef` and `ChangedBindingAccountRefs[]`, with gate-decision and permission-claim refs separate when current; an F.9 block is added only for a separately established semantic Bridge and bounded use.

#### E.18:5.12 - S12 - Exact Viewpoint References To E.18 Constructs (neutral, holonic)

**S12 use.** S12 is secondary mapping input when a current use relates one exact viewpoint episteme to exact E.18 constructs. It is not the ordinary E.18 core for naming a selected structure, flow valuation, path slice, or crossing. One viewpoint mapping may stop after one row.

**Imported interface, not a local viewpoint ontology.**

- `E.17.0` defines how P gains `U.Viewpoint` membership, the `EpistemeViewpointConformanceRelation(E,P)` test between independently identified E and admitted P, and the rule by which E gains `U.View` membership.
- `E.17.1` defines the catalogue form for exact L: the local family-declaration claim block inside `G_L`, its ordinary family designator, exact `U.ViewpointRef` members, subset and omission discipline, and catalogue provenance. It admits no `U.ViewpointBundle` kind.
- `E.17.2` supplies a project-local TEVB authoring template. It ships no current catalogue L, family value, four references, or four P editions. Symbols such as `f_eng`, `r_functional`, and `P_functional` remain variables until one project supplies exact bindings.
- `E.24.PUB` defines publication-form expression, carrier-bearing, publication-occurrence, and recurrence relations. Use `C.29` for a separately claimed representation or correspondence. Neither grants viewpoint or view membership.

**Ordinary first move.** For one current S12 mapping:

1. identify exact catalogue L by the obtaining C.2.1 triple `<G_L, K_L, R_L>`;
2. retrieve one local family declaration by its ordinary `familyDesignator` under `R_L`;
3. name the exact retained subset `Sigma` and any omitted members needed to interpret that subset;
4. select one exact `viewpointRef : U.ViewpointRef` from `Sigma` and resolve it under `R_L` to exact P; and
5. name only the exact E.18 loci, transfer relations, gates, crossings, or valuations used by this mapping.

Stop there unless the current claim also says that an exact candidate episteme E is a view, publishes E, compares semantic contexts, or claims whole-family coverage. Those are separate branches below; family provenance and a familiar `VP.*` spelling establish none of them.

**Catalogue locator and designator discipline.** The legacy S12 pair `<editionId(L), ViewFamilyId>` is only a row spelling of E.17.1's compact retrieval locator `<editionDesignator(L), familyDesignator>`. Both components are ordinary designators interpreted under exact `R_L`; the locator aids retrieval and provenance but does not identify L, a bundle entity, a viewpoint, or a view. A token such as `VP.Functional` may remain as P's ordinary reader-facing designator after exact `viewpointRef -> P` resolution. It is not a `U.ViewpointId`, reference, family member, or conformance result.

**Keep the relation positions separate.**

- **Selected viewpoint.** One singular `viewpointRef` resolves exact P for the current use. Importing a family or subset does not select P by itself.
- **Candidate view.** If the row claims that exact E is a view under P, E is independently constituted under C.2.1 and the exact E/P conformance relation must obtain. The row does not create that relation.
- **Selected transformation-flow structure.** Use E.18 for the selected `TransformationFlowStructure` and its loci, relations, paths, crossings, and valuations. Viewpoint selection does not make any of those objects obtain.
- **Publication.** A publication form expresses the selected episteme for one bounded use; a presentation carrier bears the form; an E.24.PUB occurrence makes the selected episteme available. A form or carrier is never part of a `U.View` merely because it presents that view.
- **Representation or correspondence.** When a form or other expression represents an independently recovered object or relation, cite the exact C.29 relation. A representation relation neither supplies E/P conformance nor makes the represented world-side relation obtain.
- **Cross-context meaning.** Catalogue provenance is only provenance. If comparison crosses semantic contexts, resolve the exact F.17 cells, an obtaining F.9 Bridge, the separate bounded-use claim, and any required reliance branch; otherwise stop at lexical or structural contrast.

**Architecture and described-subject boundary.** E.18 can supply a transformation-flow structure used by an `ArchitectureOf@Context` claim or by another use that selects the same architecture structure. Name that claim or structure and the pattern that defines it or the project relation that selects it. Identify a C.2.1 description episteme, its EntityOfConcern, effective reference scheme, ClaimScope, or `BoundedModelUseStructure` only when the architecture use relies on it. A second-order episteme may concern an architecture-description episteme only when C.2.1 identifies that description as its EntityOfConcern; a mapping row or publication form creates no such identity. E.18 does not define architecture, and a transformation-flow structure is not a functional architecture by default. Use `C.30`, `C.30.ASV`, and the architecture transformation-flow relation pattern when the selected structure participates in an architecture claim. Structural crossings follow E.18 S9 and CC-E18-11 and CC-E18-23. Any penalty also needs a current policy, evidence that it applies, the rule application, `PolicyIdRef`, and any separately needed authority relation with its participants. None of these changes viewpoint semantics.

One project-local TEVB viewpoint may describe an already identified target holon (`U.System` or `U.Episteme`) only after its exact P and target-kind criterion are recovered. That subject remains distinct from any `U.ContextSlice`, claim scope, description episteme, and selected `TransformationFlowStructure`; a mapping row creates no context-holon or context-object identity. A different EntityOfConcern requires one exact A.6.4 retargeting with its source and receiving subjects, source and receiving viewpoint references when current, invariant, applicability, and witness. If the case requires A.6.4's parked legacy `KindBridge`/`CL` rule, return the D14.17.3 `missing-governor` stop.

**Purpose.** Provide a neutral F.18 mapping from one selected project-local engineering viewpoint reference to exact E.18 constructs so that one holon may be described through functional, procedural, allocation-responsibility, or module-interface concerns without turning those labels into viewpoint ids, family entities, publication forms, or view-membership evidence. S12 does not claim that several views share one underlying transformation-flow structure unless that exact structure, each candidate E, each exact P, and the obtaining relations are declared.

**Holon target.** The mapping applies to any admitted holon. When actual Work is current, A.15.1 identifies its performers, Method, time, and containing System; F.6 identifies the assignment under which each performer acted. The System acts and the assignment does not. A compact S12 row may omit identifiers its named receiving use does not need. Merely being a System, view, or structure locus creates no Work. Supervisory and structural hierarchies remain distinct under B.2.5.

**Four project-local TEVB template positions and their E.18 mappings.** The four `r_*` and `P_*` names below are variables. A project may use a row only after its exact local reference resolves exact P. The quoted `VP.*` spellings are optional ordinary designators for reader recognition.

1. **Function-oriented mapping** — selected relation `r_functional` maps to position `P_functional`; optional P designator `VP.Functional`; “what transformation is achieved and, when actual Work is current, which admitted Systems perform it”.
   - **Flow valuation example:** a P2W carry-through valuation through loci `U.Signature(profile=FormalSubstrate) -> U.PrincipleFrame -> U.Mechanism -> U.ContextNormalization (UNM) -> SelectionAndTuning locus -> WorkPlanning locus -> later exact Work occurrence admitted under U.Work -> EvaluatingAndRefreshing locus`, where each illustrative locus label names an independently defined value or relation rather than a new `U.*` kind.
   - **Publication:** any publication uses exact E.24.PUB relations; comparable claims pin `CG-Spec` and `ComparatorSet` editions; a structural crossing publishes `CrossingRef` and `ChangedBindingAccountRefs[]`, with gate-decision and permission-claim refs separate when current. Add an F.9 Bridge branch only for a separately established cross-semantic use.
   - **Checks:** A.20 (CV) inside transformations; A.21 (GateFit) at gates; comparator, set-return, and No-Hidden-Scalarization discipline through `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` for current selector or comparator cases.
   - **Holonic note:** `U.Episteme` does not act; Systems use epistemes while acting on carriers. Actual Work must pass A.15.1 and F.6 for its performers, Method, time, containing System, and assignments.

2. **Procedure-oriented mapping** — selected `r_procedural -> P_procedural`; optional P designator `VP.Procedural`; “what steps occur and when”.
   - **FPF constructs:** `U.WorkPlan` (A.15.2) for intent and schedule; an exact Work occurrence admitted under `U.Work` (A.15.1) for actual performance; and a separate assertion or record when the occurrence is described.
   - **Boundary:** `OperationalGate(profile)` with `USM.LaunchGuard` consumes one exact `workEntryClaimRef` and may authorize or block an attempted run; it does not create or mediate ontic entry into Work. `DesignRunTagFrom` and `DesignRunTagTo` appear only where their exact gate use requires them. If Work occurs, A.15.1 independently grounds its identity and actual relations.
   - **Holonic note:** the target may be one System or a supervised sub-holon cluster. Represent supervision by the B.2.5 relation established for that case. A local system-role kind, classification, assignment, or label does not establish supervision; structural mereology remains separate.

3. **Allocation-responsibility mapping** — selected relation `r_allocation` maps to position `P_allocation`; optional P designator `VP.AllocationResponsibility`; “which Systems, interfaces, constraints, local system-role-kind classifications, assignment occurrences, and separately established responsibility relations are relevant”.
   - **FPF constructs:** module interfaces are `Signature` loci; module realizations are `Mechanism` loci; inter-module dependencies traverse `U.Transfer`, with gates on crossings.
   - **Publication:** forms are typed expressions of selected epistemes, not Work occurrences, performed-work records, execution carriers, or sources of new numeric claims. Constraints and compatibility appear as CV checks under A.20.
   - **Holonic note:** Use Part A for structural mereology. E.18 ties interface and exposure semantics to mathematical-lens expressions and gates only when those are current.
   - **Device-view structural reinterpretation:** the same transformation-flow valuation may be described under a device-oriented concern without changing the selected structure. A real EntityOfConcern change requires exact A.6.4 retargeting; if a `CtxState` binding changes, use a GateCrossing with the local per-binding account. Do not infer a semantic Bridge, use licence, gate result, or permission from the viewpoint change.
   - **Role-word guard:** `TypicalEnactorRoleName` is pedagogical only. When source wording says *role* and the current meaning is unresolved, apply E.10.ROLE. Otherwise the label substitutes for none of these: a local system-role kind, its independently evaluated classification, one A.2.1 assignment occurrence, a B.2.5 supervision relation, a direct responsibility or authority relation, the exact values consumed by a GateFit-scoped `GateCheckRef`, or F.6 Work attribution.

4. **Module-interface mapping** — selected `r_module -> P_module`; optional P designator `VP.ModuleInterface`; “what modules exist and how they specify commitments and constraints across interfaces”.
   - **FPF constructs:** module interfaces are `Signature` loci; module realizations are `Mechanism` loci; inter-module dependencies traverse `U.Transfer`, with gates on crossings.
   - **EntityOfConcern note:** a functional-to-element-structure change follows the device-view rule above: exact A.6.4 retargeting first, then a GateCrossing only for changed `CtxState`; any semantic F.9 Bridge remains a separate relation and bounded-use question.
   - **Holonic note:** the same module can concern several view epistemes under separately resolved P editions; supervisory loops under B.2.5 remain orthogonal to structural composition.

These four positions are one candidate local family shape, not four globally materialized members. Another safety, mission, information, assurance, or domain family is another local declaration inside an exact catalogue episteme L with exact references resolving exact admitted P editions. It is never introduced as a `U.ViewpointBundle` species.

**View-family label discipline for transformation-flow loci (recognition only).** When a current mapping needs familiar wording, a pattern or domain profile may publish `LocusViewFamilyLabels[]` records of the form `{ CatalogueEpistemeRef, EditionDesignator, ViewFamilyDesignator, ViewpointRef, Label }`.

1. `CatalogueEpistemeRef` resolves exact L; `EditionDesignator` and `ViewFamilyDesignator` reproduce the ordinary compact locator under `R_L`; `ViewpointRef` resolves exact P. If those values are absent, `Label` is only local orientation and makes no family or viewpoint mapping claim.
2. Labels are recognition-only: no arithmetic, new claim, check participation, `CtxState` write, `DesignRunTag` change, conformance, or publication-form creation follows from them.
3. A `VP.*` label is P's optional ordinary designator, never a substitute for `ViewpointRef` or P.
4. Twin Tech/Plain registers may be used under E.10 and F.18.
5. Do not name transformation-flow loci by operands or output states; an operation is not its operand or output state.
6. `TypicalEnactorRoleName` may aid pedagogy. If *role* remains unresolved, route it through E.10.ROLE; the label itself fills none of the exact values named by the Role-word guard.
7. ASCII TitleCase remains the local morphology convention; conjunctions use `And`, and composite operation labels use `XingAndYing` or `XAndYing` when grammar calls for it.
8. The illustrative P2W row is informative. It neither defines general P2W nor changes kind, viewpoint, or Work semantics.

**Conditional publication block — `UTS.ViewpointMap`.** Publish this block only when an exact viewpoint-to-E.18 mapping claim is made or consumed. Ordinary E.18 use requires no map.

*Minimum row schema, when current:*

- `CatalogueEpistemeRef` — exact L, recoverable through `<G_L, K_L, R_L>`;
- `CatalogueProvenance{EditionDesignator, ViewFamilyDesignator}` — the E.17.1 compact locator, corresponding to legacy row spellings `editionId(L)` and `ViewFamilyId`, for retrieval and provenance only;
- `ViewpointRef : U.ViewpointRef` — one exact selected member of the declared retained subset;
- `ResolvedViewpointEpistemeRef` — exact P resolved from `ViewpointRef` under `R_L`;
- `ViewpointDesignator?` — optional ordinary reader label such as `VP.Functional`, never an id or reference;
- `CandidateEpistemeRef?` and `EpistemeViewpointConformanceRelationRef?` — present together only when the row claims that exact E is a `U.View` under P;
- `TargetHolonRef` — one admitted `U.System` or `U.Episteme`. A `U.PromiseContent` or `U.MethodFamily` label does not fill this field: recover the actual system or episteme concerned by the promise, method, description, work, or architecture claim, and use E.18 only for the selected transformation-flow structure around that admitted target. If the target is not `U.System`, the row supplies no performer basis for Work;
- `PrimaryE18ConstructRefs[]` — exact loci, transfer relations, gates, paths, crossings, or valuations actually used;
- `Crossings[]{CrossingRef, ChangedBindingAccountRefs[], GateId, GateDecisionRef?, DecisionLogRef?, PermissionClaimEpistemeRefs[]?}` — only crossings actually used by this mapping;
- `EditionPins[]` — only when comparable claims consume exact editions; each pin resolves the exact edition and the independently identified value whose edition it names;
- `SemanticBridgeUse?` — only with two exact F.17 cells, an obtaining F.9 Bridge, the separate bounded-use claim, and any required reliance branch;
- `PublicationUse?{SelectedEpistemeRef, BoundedUseDeclarationRef, PublicationFormRef, PresentationCarrierRef, EpistemePublicationRelationRef}` — only when the selected episteme is actually published; and
- `RepresentationRelationRef?` — only when one expression separately represents an independently recovered E.18 object or relation under C.29.

An optional `PublicationViewpointRef` may select another exact P for a publication-focused use, but it resolves and passes E.17.0 conformance independently. It does not map to the engineering P by label or turn the form or carrier into a view.

**Whole-family coverage is a separate claim.** One row is sufficient for one-viewpoint use. Require four exact rows only when the current use makes one separately identified whole-family coverage claim over the materialized local TEVB declaration. That claim names exact L, the exact declaration, all four retained references, their resolved P editions, the target, and the coverage predicate. Saying “TEVB-like”, using four familiar labels, or importing one member does not make that claim.

**Conformance (S12-scoped, only when `UTS.ViewpointMap` is current).**

1. Every row resolves exact L, its local declaration, the retained subset, one exact `U.ViewpointRef`, and exact P; the locator and any `VP.*` token remain ordinary designators.
2. E.17.0 supplies the membership test for P and the sole E/P conformance test for `U.View` membership. A row without an obtaining E/P conformance relation makes no view claim.
3. One-viewpoint use needs only the selected row. Four rows are required only by an exact whole-family coverage claim satisfying the preceding paragraph.
4. Every E.18 construct resolves to its exact value and every crossing to its exact occurrence. Each `ChangedBindingAccountRef` resolves one binding's from/to values, establishing facts or claims, applicable declarations or rules, and current applications. Each gate resolves to the exact `OperationalGate(profile)` and any current GateDecision or DecisionLog; any permission claim remains a separate A.2.8.PER claim. Each edition pin resolves the independently identified value whose edition it names. The row creates none of them.
5. A Work-related row preserves the Work identity, every performer System, enacted Method, time, and containing System; F.6 identifies the assignment under which each performer acted. A short row may omit identifiers its named receiving use does not need; a gate decision never becomes the Work occurrence.
6. `SemanticBridgeUse` is absent unless its exact endpoint cells, obtaining Bridge, bounded-use claim, and required reliance path are all present. Provenance or equal labels never substitutes for it.
7. A publication branch resolves E.24.PUB expression, bearing, and publication relations. Form and carrier remain distinct from E, P, and `U.View` membership; no correspondence-based part claim is allowed.
8. A C.29 representation branch names its exact relation and makes no represented world-side relation obtain.
9. Additional families are exact local declarations with exact members inside constituted catalogue epistemes, never instances or species of `U.ViewpointBundle`.
10. For an unresolved catalogue, declaration, reference, P, conformance claim, or whole-family coverage basis, return `missing-governor` only when no current predicate, occurrence rule, or test can state the needed claim; return `missing-information` when an exact reference or case fact needed to decide the applicable test is unavailable; and return `factually unsupported` only when the governor exists, the available case basis is sufficient to apply its positive test, and that test fails. If the applicable rule establishes that the case is outside its scope, state the inapplicable result. State a negative only when an applicable non-obtaining criterion or complete closure basis exists and the available facts satisfy it; a failed positive test alone establishes neither. Do not substitute a label for any of those outcomes.

