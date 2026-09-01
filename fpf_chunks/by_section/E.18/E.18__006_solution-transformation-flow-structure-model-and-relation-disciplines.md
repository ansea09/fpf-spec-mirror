---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transformation Flow Structure"
section_id: "E.18:5"
section_title: "Solution - Transformation-flow structure model and relation disciplines"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__006_solution-transformation-flow-structure-model-and-relation-disciplines.md"
commit_sha: "434e17ec848bb7f49e6da99dfc268effb2b5b9af"
heading_path:
  - "E.18 — Transformation Flow Structure"
  - "E.18:5 — Solution - Transformation-flow structure model and relation disciplines"
line_start: 85277
line_end: 85543
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

* **Loci:** structure positions or bindings to independently defined or constrained FPF values (open world). Common specialisations **include but are not limited to** one first-principles P2W example: an independently identified actual bounded `U.Transformation`, `U.Signature(profile=FormalSubstrate)`, `U.PrincipleFrame`, `U.Mechanism`, `U.ContextNormalization (UNM)`, a selector relation that satisfies the current selector and comparator definitions or tests, one exact `A.15.2 U.WorkPlan` optionally carrying declaration-local A.15.3 planned-filling rows, one exact Work individual admitted under `U.Work`, and current evaluation or currentness relations. This list is **illustrative**, not exhaustive, and none of its entries is mandatory for general P2W. A structure position may be expressed by a morphism, graph vertex, tuple position, or category-theoretic object under a mathematical lens when that lens is current, but E.18 does not make every position a `U.Morphism`, graph vertex, or `U.Transformation`. Selection into the same structure, path adjacency, shared work, or a common affected referent supplies neither the `A.3.4` actuality basis nor the facts, predicate, and identity rule needed for a transformation-composition claim.
* **Transfer relation:** a **single relation kind `U.Transfer`** (typed) carrying carrier refs and token refs inside one selected TFS. Raw transfer preserves `CtxState`. Every actual change to a locality, plane, edition, or design/run binding is represented by one `GateCrossing` at an `OperationalGate(profile)` and has one local per-binding account that separates from/to values, establishing facts or claims, applicable declarations or rules, and current applications. An A.6.4 arrow r, an affirmative bounded-use assertion q, and a current-case judgement of `satisfies`, with unchanged `CtxState`, follow the limited `StructuralReinterpretation` route in CC-E18-06-EX instead of becoming a crossing. Transport conversions cite the exact registry entry, conversion rule, and applicable policy. E.18 defines neither a generic semantic Bridge nor a generic penalty policy.
* **Scopes:** `Gamma_time` (budgets, horizons), `PublicationScope` for faces (E.17), and **slice ids** for refresh (G.11).

 **CtxState (PS‑projection; closed slots):** `CtxState = ⟨L, P, E⃗, D⟩` is the **projection of E.17 Publication Scope**.
 **Slot definitions and changed-binding account boundary (normative):**
  - `L := Locus` — one exact `U.ContextSlice` value identified under `A.2.6`; any scope-membership or translated-scope claim remains with A.2.6 and its current F.9/C.2.1/A.10-or-B.3 premises when semantic translation is actually required.
  - `P := ReferencePlane` — a ref-only binding to the exact plane and units declaration used by the current case. E.18 supplies no generic plane conversion. Cite the current declaration and applicable conversion rule by value. Return `missing-governor` only when no current conversion predicate or rule can state the attempted crossing; return `missing-information` when the needed declaration or case values are unavailable; when the rule and facts are current, state its positive, negative, or inapplicable result rather than a generic blocker.
  - `E⃗ := Edition vector` — a partial map `edition_key ↦ EditionId` whose members cite each versioned value, its exact edition, and the registry or declaration that assigns that edition; `G.11` defines the edition-bump and refresh records, while `E.17` defines publication of the refs.
  - `D := DesignRunTag` — `design(T^D)` or `run(T^R)` only as consumed by the exact `A.21` gate and, at work entry, the `A.15.5` readiness claim; the tag does not identify or create Work.
 **Invariants.** Raw `U.Transfer` preserves `CtxState` (`⟨L,P,E⃗,D⟩`): it does **not** write or update any CtxState slot; any CtxState write or update, including a design-to-run tag change for a pre-run work-entry claim, occurs at `OperationalGate(profile)`. The gate changes the claim or decision state, not the ontic identity of a Work occurrence or any independently obtaining relation involving it.
 **Extension discipline.** A conforming use registers any extra slot beyond ⟨L,P,E⃗,D⟩ in the **E.17 publication discipline and the E.18 LEX “CtxState Extension Registry”** with slot‑id, intent, partial‑order rule (neutral or absorbing), and SquareLaw compatibility; unregistered extensions are non‑conformant.
 **Data-shape location.** E.18 names the structure and valuation obligations for `PathId`, `PathSliceId`, Gamma pins, and lineage: flow is a valuation over `U.Transfer`, raw transfer preserves `CtxState`, and path or slice evidence is carried through this pattern plus `A.20`, with `G.6` for evidence-provenance path visibility and `G.11` for refresh wiring. These are the current structure loci for path and slice currentness.

 * **Locus kinds:** `Transformation`, `Signature`, `Mechanism`, `WorkPlanning`, `Work`, `Check`, and `StructuralReinterpretation` are the current minimal structure-positioned locus baseline. Domain-specific species are open-world and non-exhaustive, but each species binds to one of the locus kinds or requires an explicit E.18 update. These are positioned loci in the selected structure, not a local taxonomy of new FPF kinds.
  **Exact identification (no local ontology):**
  - `Transformation` **≡** **A.3.4** `U.Transformation` only when the structure locus binds one independently identified actual bounded change with its exact changed referent, extent or ordering boundary, boundary conditions, actual change facts, and continuity or reidentification rule. Desired, intended, planned, modeled, selected, described, evaluated, published, or transferred change content remains under the definition or test for that exact claim; it is not a `Transformation` binding merely because it occupies the selected structure. Current-resolution identification establishes neither finer parts nor partlessness. A positive transformation-composition, `TransformationPartOfRelation`, composite-transformation identity, or transformation-holonhood claim stops under D14.16 with the exact A.6.RCD result: `TC-MWH missing-governor` only when no current predicate, applicability condition, or occurrence rule states the required contribution, compatibility, parthood, or whole-identity claim; `TC-MWH factually unsupported` when the governor exists and the available case basis is sufficient to apply its positive test but that test fails; and `TC-MWH missing-information` when a fact needed to decide the test is unavailable. A negative needs its own applicable non-obtaining criterion or complete closure basis and satisfying facts. E.18 retains the independently identified transformations and supplies no provisional contribution, compatibility, parthood, or whole-change architecture; it does not preselect whether a later settlement uses a generic derived relation, subject-specific relations, local compound claims, or non-admission.
  - `Signature` **≡** **A.6.0** `U.Signature` (universal, law-governed declaration).
  - `Mechanism` **≡** **A.6.1** `U.Mechanism` (law-governed application over a SubjectKind and RangedValueKind), with placement and stabilization relations in `E.20` when current.
  - `WorkPlanning` **≡** one exact **A.15.2** `U.WorkPlan` when that plan occupies the structure position. Declaration-local A.15.3 `SlotFillingsPlanItem` rows remain content inside that WorkPlan and do not occupy a locus or identify a relation independently.
  - `Work` **≡** an exact dated Work individual admitted under **A.15.1 `U.Work`**. A structure locus may point to that occurrence after it exists; before execution it points only to a `U.WorkPlan`, A.15.5 readiness relation, or another exact work-entry claim. No second enactment kind is introduced.
  - `Check` **≡** `OperationalGate(profile)` when a gate/check locus is present. A.20 supplies exact internal-constraint results when those constraints are current; A.21 defines the gate profile, independent check retention, result mapping, aggregate decision, and publication minima when a gate decision is current.
  - `StructuralReinterpretation` is only the E.18 position of an independently identified A.6.4 arrow r, bounded-use assertion q, and current-case judgement; it is not a new retargeting kind. E.18 records r and q, the exact case basis and judgement result needed by this placement, and path-slice locality. q's ClaimGraph carries the invariant, visible loss, use, conditions, and affirmative or negative polarity; the judgement separately reports `satisfies`, `fails`, or `cannot decide`. F.9 is additional only when the same case asserts a semantic relation between two exact F.17 local senses and its predicate obtains; its bounded-use claim, optional `CL`, evidence, and reliance remain separate.
`OperationalGate` is the E.18 check locus when a gate or check position is present. A.20 supplies an exact internal-constraint result when that claim is current. When a gate decision is current, A.21 supplies the exact profile application, independently identified check-application results, `GateDecisionResult`, and rationale. A `DecisionLog` is added only for a current audit, history, replay, or reuse need.
  E.18 adds only a structure-local placement rule: when r, an affirmative q, and a current-case judgement of `satisfies` are current and `CtxState` is unchanged, record their basis and `PathSliceId` without calling the placement a GateCrossing. If any `CtxState` binding changes, use a GateCrossing and state the changed binding's from/to values, establishing basis, and any applicable declaration, rule, and current application. A Bridge, card, UTS row, optional `CL`, witness publication, gate decision, or permission claim neither identifies r nor supplies q's polarity or the case judgement.
> **MVPK integration (import).** Every locus with an external publication face is published via **MVPK** faces (`PlainView`, `TechCard`, `AssuranceLane`, `InteropCard`) under a declared **PublicationScope** (E.17). E.18 **reuses** MVPK's publication rules (pins, declared-order discipline, "no new numeric claims and no re-listing of inputs and outputs") and only adds structure-scope constraints in S3 and **CC-E18-09 and CC-E18-10**; it does **not** define a second, local publication semantics.

**GateCrossing (normative)**

**Definition.** A `GateCrossing` is E.18's structure-local transition from one exact `<FlowPositionRef, CtxState>` binding to another at one exact `OperationalGate(profile)`. It is selected only when at least one `CtxState` binding changes. It is not a `U.Relation`, an F.9 `Bridge`, a gate decision, a plane conversion, an A.6.4 arrow or use assertion, a penalty, or a publication occurrence.

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
| EntityOfConcern retargeting | From/to exact epistemes and EntitiesOfConcern, one exact A.6.4 arrow r, and separate q for the current use. Any operation application, applicable rule, and Work remain separate. A kind difference alone is only a cue to repeat the C.2.1 identity test. |

`A.20` may supply an exact current constraint-validity result and witness or reason; `A.21` supplies the gate profile, retained check results, mapping, aggregate decision, and decision log. Neither supplies a changed locality, plane, edition, tag, retargeting fact, rule application, or permission claim.

**Canonical reference.** `CrossingRef := ⟨TFSRef, GateId, FromPositionRef, ToPositionRef, FromCtxStateRef, ToCtxStateRef, ChangedBindingIds, PathSliceId⟩`. A DecisionLog or downstream use that depends on the crossing cites this ref and the required per-binding accounts.

**CrossingBundle publication block.** Materialize a CrossingBundle only when a named selector, acceptance, audit, replay, or other downstream use relies on durable crossing evidence. The bundle is publication packaging under `E.17`, not a constituent of the crossing or gate decision. It contains the `CrossingRef`, `ChangedBindingAccountRefs[]`, `GateId`, the current `profileApplicationRef` and `GateDecisionResultRef` when a gate decision exists, an optional current `DecisionLogRef`, optional separately current `PermissionClaimEpistemeRefs[]`, `PublicationScopeId`, `PathSliceId`, and any current witness refs.
When that downstream use also relies on cross-semantic correspondence, add a separate F.9 block: the two exact `SchemeSenseCell` endpoints, the obtaining Bridge and its exact profile, the C.2.1 claim that says whether the Bridge suits this named structural use in the named direction under its rule and tolerance, and the current A.10 or B.3 reliance branch if reliance is claimed. A Bridge Card remains optional packaging and `CL` remains optional evidence shorthand; neither makes the structural crossing obtain, makes the gate pass, or grants the use.

A penalty appears only when one exact current policy applies to this crossing and its rule application to the crossing facts supports that penalty. Cite the policy and `PolicyIdRef`; when the claim also depends on who may issue or enforce it, cite the separately obtaining direct authority relation and its actual participants. E.18 derives no penalty from `CL`, plane difference, edition difference, or Bridge publication. If the policy, applicability, rule application, or any separately required authority fact is absent, make no penalty claim and infer no default.

**Term separation.** **Transfer** denotes the sole relation kind `U.Transfer` in the selected structure. **Transport** denotes Phi-governed conversion **policies and registries** (**`TransportRegistry^Phi`** under UNM). Wording "reuse via Transport" refers to registries and policies, not to an additional transfer relation.

#### E.18:5.2 - S2 - Flows as valuations (paths, state, and guards)
* A **Flow** is a **valuation** `nu` over internal `U.Transfer` occurrences and cut-sets of one exact selected TFS, paired with an **admissible path** `p = v0 -> ... -> vk` in that structure. The valuation maps transfer occurrences or cut-sets to token and state values under `CtxState` and links publication-event records to a declared `PublicationScopeId`; it is not itself the performed work. E.18 specifies the concrete path and slice publication pins and identifiers (`PathId`, `PathSliceId`, Gamma_time on compare and launch faces); apply `A.20` when exact internal-constraint results are current, `G.6` for evidence-provenance path visibility, and `G.11` for refresh wiring. This reflects the "selected structure != flow" norm (flow = valuation), with gates placed exactly on GateCrossings.
* **Several valuations of one TFS.** One `TransformationFlowStructure` may carry several flow valuations only after the use identifies the same exact TFS and its structural boundary for every valuation. For example, nominal-load and emergency-load valuations may differ in state values, paths, slices, or local `DesignRunTag` bindings while still using the same cooling-loop structure and the same internal transfer occurrences. Labels such as development, application, evaluation, refresh, or feedback do not establish that shared identity.
* **Leave E.18 at a member boundary.** `U.Transfer` relates positions only inside that one selected TFS. When candidate flows have independently identified TFS boundaries, separate identified objects or Work occurrences, and a relation across their positions, keep each TFS and its valuations local and use `E.18.NET` with the exact cross-boundary relation predicate and occurrence rule. Do not turn `U.Transfer`, adjacency, a carried product, or a feedback arrow into a universal cross-flow relation.
* **Admissible path (definition).** A path `p` is **admissible** iff:
  (a) locus kinds and transfer relation kinds match the declared `tau_L, tau_Transfer`;
  (b) any write or update to any member of `⟨L,P,E⃗,D⟩` appears at **exactly one** `OperationalGate(profile)`. A current A.6.4 arrow r, affirmative q, and current-case judgement of `satisfies` with unchanged `CtxState` follow CC-E18-06-EX without a crossing; if the same case changes a `CtxState` binding, the changed binding appears at exactly one gate;
  (c) each GateCrossing on `p` carries the **SquareLaw witness** required by its exact current crossing rule, if that rule requires one (CC-E18-23), while the support cited by q remains on the use-claim side and does not identify r;
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
* **Eulerian (structural):** define a **function on transfer relations** ("which quantity or object is associated with each relation under a given regime"), with gate rules. E.18 deliberately fixes the **Eulerian semantics of flow** at the selected-structure scope: "flow (= valuation) with publication log", while change over time appears as **re-valuation** over a **PathSlice** (the selected path portion whose identifier scopes refresh and republication). A SquareLaw condition enters only where an exact current crossing rule requires it. This yields comparability, reproducibility, and slice-local refresh.

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

1. **Crossings on faces.** When a face publishes a GateCrossing, it cites the `CrossingRef`, `ChangedBindingAccountRefs[]`, `GateId`, and any current `GateDecisionResult`, optional `DecisionLog`, policy-application, or permission-claim refs. An F.9 Bridge block appears only for a separately established cross-semantic use; its optional card and `CL` do not replace those refs.
2. **Edition refs on faces.** A face that cites `CG-Spec`, `ComparatorSet`, `UNM.TransportRegistryPhi`, or another versioned value cites that exact value and edition. Edition citation alone requires no Bridge Card, UTS row, or semantic Bridge.
3. **ComparatorSet and set returns (structure-scope).** Any `ComparatorSet` and `SetSemanticsRef` used along a transformation-flow path carries **edition identifiers**; affected faces are **re-emitted** on edition change; faces with comparison **return sets and declared partial orders** (no hidden scalarization), reusing MVPK's declared-order discipline.
4. **Gamma_time on compare and launch faces.** Every current compare or launch publication face on an E.18 path pins `Gamma_time`; implicit *latest* is not admissible. A.21 cites the exact current profile application and qualification window. **CHR avoids acceptance thresholds** (*NoThresholdsInCHR*); gate and threshold claims are carried by A.21 and Part G, while actual performed facts are established through independently obtaining relations involving exact Work occurrences under A.15.1. A source `unknown`, `notRun`, or error remains explicit before the current profile rule maps it to a gate decision.

> **Reminder.** MVPK already bans "signature" on faces, input-output re-listing, arithmetic on faces, and unpinned numeric content (E.17 §5.4-5.5). E.18 **does not weaken or override** those rules; it only constrains how they are used along transformation-flow paths.

**Lean publish-mode (AssuranceLane-Lite).** Lean changes publication faces only, not policy or checks. A current face cites the `profileApplicationRef`, identified `GateCheckApplicationResult` refs, and `GateDecisionResultRef`; it cites a `DecisionLogRef` only when an audit, history, replay, or reuse record is current. The underlying check-application results remain unchanged.

**Decision stability and idempotency (gate-local).** A gate decision is recomputed when an input named by A.21 changes. Only a current reuse, cacheability, or stability claim needs an equivalence witness covering the inputs whose equality that claim relies on; an optional `DecisionLog` may cite it. Use G.6 for evidence-provenance path visibility and G.11 for refresh implications. E.18 does not prescribe storage formats, key shapes, or hashing schemes.

**Retargeting and semantic-Bridge boundary.**

An `EntityOfConcernRef` change is not established by a UTS row, mapping label, card, `CL`, or GateCrossing; a kind change alone only reopens the C.2.1 identity test. First recover the exact A.6.4 arrow r from its endpoints, arrow rule or designator, and formal equivalence. Separately recover q, whose claim content states the invariant, visible loss, receiving use, conditions, support, and polarity. Any application occurrence and Work remain separate. If the use also needs a semantic relation between two exact local senses, apply F.9 separately and keep its own bounded-use claim, optional `CL`, evidence, and reliance separate.

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

* The selected structure may center a loop between the `SelectionAndTuning` locus, whose relation satisfies the named selector and comparator definitions or tests, and the `WorkPlanning` locus, which binds one exact `A.15.2 U.WorkPlan`. Any A.15.3 planned-filling row remains declaration-local content inside that WorkPlan.
* The Selection-Planning loop is represented under local **budget and max_iter** in `Γ_time`; at expiry, the exact selector relation returns its declared current set or archive outcome, such as `CandidateSet`, with the applicable partial-optimality status. If the next step needs changed tuning, a separately identified `U.WorkPlan` with any declaration-local A.15.3 planned-filling rows, or a separately identified configuration or policy that passes its own applicable rule, carries that tuning; it is not another entity returned by the selector. Further improvement is placed in the **next `PathSlice`** only through that explicit planning, configuration, policy, or refresh continuation.
* **UNM occurs before the loop.** When the normalized basis shows missing or stale measurements, retain the finding returned by the UNM test. A freshness request remains a request. If the receiving use plans measurement refresh, A.15.2 identifies the exact WorkPlan; when a reusable declaration member must be pinned, A.15.3 adds only a declaration-local row inside that WorkPlan. For later dated refresh Work, recover each exact actual performer through A.13 and let A.15.1 independently admit the occurrence. Add F.6 only when the receiving use also consumes precise assignment-bound attribution; F.6 neither discovers the performer nor supplies classification, and its failure leaves the Work intact. Keep the later measurement and calibration separate. A `RefreshReport@Context` is likewise separate from the request, plan, Work, measurement, and calibration. A publication that states a calibration target cites the calibration reference and any applicable transport-conversion rule. A penalty requires its own current policy, applicability, rule application, and any authority relation actually used; calibration, conversion, registry publication, or a report supplies no penalty by itself.
* **Work-entry claim and actual Work stay distinct.** `workEntryClaimRef` designates one exact `U.WorkPlan`, A.15.5 readiness relation, or other prospective claim consumed by `LaunchGate`. If Work later occurs, each actual launch value is established only through an independently obtaining direct relation or exact A.6.1 application binding of that Work individual. A separate `FinalizeLaunchValues` episteme may then designate the Work occurrence and those facts; it neither performs Work nor fills slots in the occurrence.
> **Refresh orchestration.** Telemetry records and publications that designate an exact Work occurrence are **slice-scoped**, editions re-pinned, and faces **re-emitted**. Telemetry remains a separate episteme and does not constitute the occurrence.

#### E.18:5.7 - S7 - Selector semantics (G.5) and parity harness (G.9)
E.18 keeps set-return, archive preservation, and comparator refs visible along the path. It does not define selector, archive, dominance, or comparator semantics; those remain with `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` for current selector or comparator cases.

* **Selectors return sets.** Default **DominanceRegime** is `ParetoOnly`; **IlluminationSummary** (telemetry summary) and any coverage and regret telemetry quantities are **report-only telemetry** (reported), excluded from dominance **unless** a CAL policy promotes them as declared dominance inputs (policy-id in SCR).

If `PortfolioMode=Archive`, a **QD archive** can be returned; when generation is in scope, pairs `{environment, method}` are managed under declared **EnvironmentValidityRegion** and **TransferRulesRef**; parity records and `PathSliceId` are pinned on publication. For current selector, archive, pool, selected-set result-declaration, comparator, or refresh claims, apply the definitions and tests in `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11`. For actual publication, use `E.17` for a source-backed face and return to source and `E.24.PUB` for the occurrence, form, carrier, audience, bounded use, and availability.

#### E.18:5.8 - S8 - Guard aggregation assignment and handling (USM §1.2)
* **USM.CompareGuard** and **USM.LaunchGuard** publish the guard-gate aggregation assignment field `GuardOwnerGateId`. The legacy field name is read here as a gate-reference assignment, not as an owner relation. Guard failures are **events** aggregated by the declared gate (not GateChecks).
* **Aggregation-assignment rules:** (i) `USM.LaunchGuard.aggregationGate = LaunchGateId(workEntryClaimRef)`, where the ref resolves to the exact prospective claim consumed by the gate and never to a not-yet-existing Work occurrence; (ii) inside a Subflow, `USM.CompareGuard.aggregationGate = OperationalGate(InSentinel)`; join loci cannot be assigned as guard-pin aggregation gates.

**Profile-application boundary (cross-reference).** A.21 distinguishes a `GateProfile` description from the exact current fact that applies it to one gate, subject, action, scope, and window. E.18 cites that application only where a current gate or crossing needs it; a profile name, matrix, branch, or `PathSlice` supplies no application or authority by itself.

**Scope-translation guards (cross-reference).** `A.2.6` defines and tests exact slice and scope membership and any actual translated-scope application. When that translation relies on different local senses, it additionally requires an obtaining F.9 Bridge, a separate affirmative C.2.1 bounded-use claim, and current A.10 or B.3 reliance. Use `A.21` for gate aggregation; no `CL` value or Bridge Card decides the guard.

**Error, timeout, or unknown (profile-bound).** Keep each source error, timeout, `unknown`, and `notRun` result explicit. The exact current profile application cites the rule and edition that maps that result to `abstain`, `pass`, `degrade`, or `block`; a profile name alone supplies no fixed fold, and no missing or unrun required result maps to `pass` or neutral `abstain`. The `GateDecisionResult` retains the mapping and rationale.

#### E.18:5.9 - S9 - Transport and crossings

* A GateCrossing records one selected-structure transition between exact source and receiving positions and `CtxState` bindings at one exact gate whose profile and decision test come from A.21. Cite A.2.6 for locality and scope membership, the current plane or units declaration and conversion rule, each versioned value and exact edition plus G.11 when refresh is current, A.21 for `DesignRunTag` and the gate decision, and A.15.5 for a prospective work-entry boundary. If no current predicate, applicability condition, occurrence rule, conversion rule, or decision test can state a claim on which the crossing depends, return `missing-governor`. If the governor exists and the available case basis is sufficient to apply its positive test but that test fails, return `factually unsupported`; if a fact or declaration needed to decide the test is unavailable, return `missing-information`. State a negative crossing only under an applicable non-obtaining criterion or complete closure basis and satisfying facts.
* A semantic F.9 Bridge is additional, not constitutive. Use it only when the case identifies two exact F.17 `SchemeSenseCell` values from different semantic contexts and the Bridge predicate actually obtains. Keep the proposed structural use in a separate C.2.1 claim, recover current A.10 or B.3 reliance when relied on, and keep any Bridge Card or `CL` optional and non-constitutive.
* An EntityOfConcern change remains with A.6.4. E.18 may place the independently identified r and q; it creates neither, records no operation application by implication, and supplies no `KindBridge` or mandatory `CL`. `T^D↔T^R` is handled at the exact A.21 gate with `DesignRunTagFrom` and `DesignRunTagTo` and the current A.15.5 or publication locus, without implying Work occurred.

#### E.18:5.10 - S10 - Non‑mechanism boundary

* Publication is a **typed projection**, not execution. Any build, render, or upload is **Work on carriers**; faces do **not** carry Γ-semantics.

#### E.18:5.11 - S11 - Coordination wording labels (when current)
Coordination wording may be published as **LexicalView** labels over a P2W carry-through flow valuation; it is orientation-only unless an exact structural crossing, work relation, semantic Bridge, or gate decision is independently current. It adds no current structure locus kind, checks, or mechanisms. A published crossing cites `CrossingRef` and `ChangedBindingAccountRefs[]`, with gate-decision and permission-claim refs separate when current; an F.9 block is added only for a separately established semantic Bridge and bounded use.

#### E.18:5.12 - S12 - Exact viewpoint references to E.18 constructs

**Use this when.** Use S12 only when a current claim maps one exact viewpoint episteme to exact E.18 constructs. Ordinary work with a selected transformation-flow structure, valuation, path slice, or crossing does not open S12, and one mapping may stop after one row.

**Imported interface.** E.17.0 defines viewpoint membership and episteme–viewpoint conformance. E.17.1 defines local catalogue declarations and `U.ViewpointRef` members. E.17.2 provides the project-local TEVB authoring template; it ships no catalogue, reference, or viewpoint episteme value. S12 uses those results and does not copy their catalogue or conformance procedure. E.24.PUB defines publication, and C.29 defines any separately current representation or correspondence.

**First useful move.** Resolve one `viewpointRef : U.ViewpointRef` under the effective reference scheme to the named viewpoint episteme. Then name only the E.18 loci, transfer occurrences, gates, crossings, paths, or valuations used by the mapping claim. The reference is not a relation, the viewpoint episteme is not a template position, and the mapping makes neither the E.18 constructs nor their conformance relation obtain.

Stop there unless the current claim separately needs candidate-view conformance, whole-family coverage, retargeting, cross-context meaning, publication, representation, or actual Work. Follow the defining pattern for that claim rather than reproducing it here. A token such as `VP.Functional` may remain P's ordinary reader-facing designator after resolution; it is not a viewpoint id, reference, family member, or conformance result.

| Project-local TEVB position | Exact reference resolution | E.18-specific mapping contribution |
|---|---|---|
| function-oriented | exact `r_functional : U.ViewpointRef` resolves exact `P_functional` under the effective scheme | Name the exact transformation-flow structure, valuation, transformation or capability-facing loci, gates, crossings, paths, and current comparator or publication pins that the mapping actually consumes. Any actual Work and exact performer are independently established through A.13 and A.15.1. Add F.6 only when the mapping also consumes precise assignment-bound attribution; missing or failed F.6 leaves the Work intact. |
| procedure-oriented | exact `r_procedural : U.ViewpointRef` resolves exact `P_procedural` under the effective scheme | Name the exact `U.WorkPlan`, dated Work, state, transfer, gate, path, or valuation references used by the mapping. A gate may decide attempted entry; it creates no Work occurrence. |
| allocation-responsibility | exact `r_allocation : U.ViewpointRef` resolves exact `P_allocation` under the effective scheme | Name only the exact E.18 interface, locus, transfer, gate, crossing, or valuation references consumed by the mapping. Local system-role kinds, C.3.2 classification judgments, A.2.1 assignments, supervision, and responsibility or authority relations remain separate claims under their defining patterns. |
| module interface | `r_module : U.ViewpointRef` resolves `P_module` under the effective scheme | Name the Signature and Mechanism loci, transfer occurrences, gates, crossings, paths, or valuations used by the module-interface mapping. A different described subject needs A.6.4 retargeting; a changed `CtxState` binding uses the E.18 crossing rule. |

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

**Purpose.** Provide a neutral E.18 mapping from one resolved project-local engineering viewpoint reference to exact E.18 constructs without turning the reference into a relation, P into a template position, or a familiar label into viewpoint, view, family, publication, or conformance evidence.

