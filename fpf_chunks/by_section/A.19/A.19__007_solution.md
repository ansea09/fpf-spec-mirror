---
chunk_kind: "child"
pattern_id: "A.19"
pattern_title: "CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
section_id: "A.19:5"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19/A.19__007_solution.md"
commit_sha: "308edacfa2bdb2c60d07e4e10c0deb1f260a6a31"
heading_path:
  - "A.19 — CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
  - "A.19:5 — Solution"
line_start: 28469
line_end: 28669
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19.CHR"
  - "A.19.CN"
  - "A.19.CPM"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.19.SOURCE-SET-SPACE-SUBSTRATE"
  - "A.19.SelectorMechanism"
  - "A.2.5"
  - "A.2.6"
  - "A.3.3"
  - "A.6.5"
  - "C.16"
  - "C.2.1"
  - "E.18"
  - "E.24"
  - "F.9"
  - "G.0"
  - "G.11"
  - "G.4"
  - "U.ClaimScope"
  - "U.ContextSlice"
keywords:
  - "CharacteristicSpace"
  - "U.Dynamics.stateSpace"
  - "coordinatewise comparability"
  - "declared Characteristics and Scales"
  - "embedding"
  - "product"
  - "role-specific space refs stay outside A.19"
  - "state trajectories"
  - "structural overlays"
  - "subspace"
---

### A.19:5 - Solution

#### A.19:5.1 - `U.CharacteristicSpace`

##### A.19:5.1.1 - Type signature

Let **I** be a finite index set labeling a collection of **slots**. Each **slot** _i_ (for _i ∈ I_) is defined as a pair:

> **`slot_i = (Characteristic_i, Scale_i)`**,

where:

-   `Characteristic_i` is a `U.Characteristic` (with an explicit arity, i.e. either an entity-Characteristic or a relation-Characteristic as defined in A.17), and

-   `Scale_i` is a chosen **Scale** for that Characteristic (with a specified scale type and unit, per A.18 and the MM‑CHR rules).

Then a **CharacteristicSpace** (CS) is formally the Cartesian product of all slot **value sets**:

$\mathbf{CS} = \prod_{i \in I} \mathrm{ValueSet}(\mathrm{slot}_i)\,.$

In other words, a point (state) in the space consists of one coordinate value for each slot. A **state** _x_ in CS can be seen as a total function _x(i)_ that picks a value from each slot’s **ValueSet** (for every _i ∈ I_, _x(i) ∈ ValueSet(slot\_i)_). By kernel mandate, any `U.Dynamics.stateSpace` **SHALL** be bound to some instance of `CharacteristicSpace`, and all states or trajectories described by that dynamics model **MUST** lie within that space’s **value set**. (The actual dynamic **laws** and time progression are handled in A.3.3; A.19 only defines the state‑space container and its properties.)

##### A.19:5.1.2 - Slot discipline (invariants)

To ensure consistency and comparability, a CharacteristicSpace must obey the following invariants:

-   **A19-CS-1 (Exactly one per slot).** Each slot **binds exactly one** Characteristic to **exactly one** Scale (including a specific Unit or kind, if applicable). This mirrors the CSLC clause of “one aspect – one scale”: there are no ambiguous or compound mappings in a single slot. (If a Characteristic can be measured on multiple scales, only one is chosen for a given space; others would require separate slots or a different space.)

-   **A19-CS-2 (Named basis).** A CharacteristicSpace **SHALL** publish an ordered list of its slots as its **basis**. Each slot in the basis has a stable identifier that can be used in technical notations or data structures. These basis names should be treated as stable technical tokens (identifier-like); any human-friendly alias or description for a slot should be provided only in the Plain register as a non-normative aid (per E.10). In short, the identity and order of slots in the space are explicit and stable.

-   **A19-CS-3 (Immutability of meaning).** Once a space is in use, the meaning of each slot is fixed. A slot’s `(Characteristic, Scale)` pair **MUST NOT** be retroactively altered. If requirements change (e.g. a different scale or a revised definition of the Characteristic), one **MUST** define a new version of the space (or a new slot) rather than silently changing the existing one. When a space is versioned or a slot replaced, an explicit **embedding** (mapping from the old space to the new space) should be published to relate historical states to the new coordinates. This ensures past data remains interpretable and prevents semantic drift.

-   **A19-CS-4 (Arity preservation).** If a `Characteristic_i` is defined as a **relation** (multi-entity characteristic), then slot _i_ represents a relationship among multiple entities. The coordinate value at such a slot is a **tuple** (with the appropriate entity types) rather than a simple scalar. The slot’s declaration **SHALL** indicate the relation’s symmetry or directionality as part of its meaning (this should align with how the Characteristic was originally defined in its template). In essence, relational Characteristics retain their arity in the space, so that we don’t confuse, say, “Coupling between X and Y” with an intrinsic property of X or Y alone.

- **A19-CS-5 (No hidden normalization, preference, or aggregation).** A `CharacteristicSpace` carries no implicit normalization, polarity preference, threshold, formula, or aggregation. A `CharacteristicSpacePredicate` may declare polarity, operator semantics, and a cut or band over that space. Normalizing, indicatorizing, scoring, folding, comparing, and selecting remain explicit operations under their governing patterns; the space declaration itself performs none of them. A.19.UNM governs normalization semantics and admissibility; C.16 governs relied-on measurement and calibration claims.
 - **A19-CS-6 (Slot meta completeness).** Where applicable, each slot **SHALL** declare `admissible_domain` and **missingness semantics** (e.g., codes for *missing*, *censored*, *not-applicable*), consistent with the Characteristic’s Scale and with MM‑CHR. This prevents silent domain drift and clarifies how absent values participate in predicates and comparisons.

 - **A19-CS-7 (Space-vs-consumer boundary).** A `CharacteristicSpace` publishes only its own slot basis, optional overlays, and typing hooks. Ref-typed consumer fields that point to a declared space, explicit relation kinds between such refs, source-set wiring, interpretive-view organization, and publication metadata are **outside** the space object and **MUST** be declared in the consumer pattern or consumer declaration that uses the space. This prevents `CharacteristicSpace` from being silently widened into ref-position semantics, selector semantics, source-set semantics, publication-form semantics, or interpretive-view semantics.

##### A.19:5.1.3 - Minimal structure hooks (optional overlays)

By default, a CharacteristicSpace has no assumed ordering or metric structure – it is just a Cartesian product of value sets. However, a space **MAY** declare certain structural attributes _as opt-in metadata_ (i.e. informative annotations that patterns can rely on, but not enforced by the kernel). These optional **overlays** include:

-   **Product topology.** A **topology** on the space, typically the product topology when slots that are quantitative (interval or ratio scales) need continuity considerations. Declaring a topology is useful if continuity or convergence arguments are relevant (e.g. to say a sequence of states approaches a limit state). By default, without declaration, no topological structure is assumed on the space.

_Lexical note:_ Here **“distance metric”** strictly means a mathematical distance function (or a generalized distance such as a **pseudometric** or **quasi-metric**) on the state space. This is **not** to be confused with *metrics* as performance measures in MM-CHR. In the **Tech** register, avoid the noun **metric**; refer to **`U.DHCMethod` or `U.DHCMethodRef`** for measurement templates (see **C.16**). Any distance overlay on a CharacteristicSpace must not conflict with scale semantics; it is an additional analysis structure, not a redefinition of measurement meaning.

These overlays are entirely **optional** and have no effect on the core meaning of the space - they exist only to enable particular reasoning such as **dominance**, **continuity**, or **distance** reasoning in models that require it. If needed, they should be added deliberately by an architectural theory rather than assumed. This way, any ordering or metric properties of states are made **explicit** instead of relying on hidden or default arithmetic. _(Rationale:_ The CSLC and MM‑CHR rules already govern what operations are allowed on each scale; A.19’s approach is to let neighboring theories add an order, topology, or metric when appropriate, so nothing is taken for granted tacitly in multi-dimensional arithmetic._)_

##### A.19:5.1.4 - Dynamics hook (typing only)

Any model of change or dynamics in FPF must declare the state space it operates over. Formally, `U.Dynamics.stateSpace` **SHALL** be specified as a reference to a `CharacteristicSpace`. This creates a typing requirement: the dynamic model can only produce states and trajectories of states that belong to the given space. All predicates or predictions in such a dynamics model are understood to **quantify over** sequences of points in that CharacteristicSpace (with time semantics governed by A.3.3’s time base and laws). **Note:** A.19 defines only the structure of the state space; it deliberately **does not** fix any time base or dynamic law. Those remain the responsibility of the dynamics pattern (A.3.3). A.19 simply ensures there is a well-defined space in which states are located, so that dynamics are decoupled from any narrative “stage” and instead treat evolution as movement through this space.

##### A.19:5.1.5 - Lexical discipline (Normative)

In all **normative references, definitions, and identifiers** related to this pattern, the specification uses the canonical measurement terminology: **Characteristic**, **Scale**, **Level**, **Coordinate**, **CharacteristicSpace**, **slot**, **basis**. Legacy terms like “axis”, “dimension”, or “point” are **forbidden** in Technical and Formal registers of the spec (per A.17’s lexical rules). They may appear _at most once_ in explanatory **Plain** language as mapped aliases to aid understanding (and if used, must be explicitly identified as equivalent to the official terms). In this pattern, we consistently use “slot” or “basis element” (never “axis”) to refer to a component of a space, and “Characteristic” (never “dimension”) to refer to the measured aspect. This lexical discipline ensures clarity and consistency across the framework (see A.17 and C.16 L-rules for the formal policy on terminology).

##### A.19:5.1.6 - Quotients & NormalizationFix (Normative)

**Governing-pattern note.** `≡_UNM` and `NormalizationFix` are defined in **A.19.UNM**. This section constrains only how they are **cited** when used in state‑space reasoning.

**Design rule — read invariants, not labels.** Any checklist, acceptance predicate, equality check, join, or comparability claim over a `CharacteristicSpace` that depends on representation choice (chart, unit, reference plane, normalization choice, or label) **SHALL** be evaluated on **quotients by ≡_UNM** or on explicitly **Normalization‑fixed** charts, not on raw labels.
*Minimal obligations:*
1) **Name the quotient or fix.** If a checklist predicates over a **normalization‑variant** property, it **MUST** name the **NormalizationFix** (including the referenced **UNM** and the relevant `NormalizationMethodInstance`(s), by reference) and thus the **≡_UNM** class.
2) **Declare NormalizationMethod class.** Every normalization used **MUST** name its method‑class token and validity window **as defined in A.19.UNM** (do not restate the class taxonomy here).
3) **Join and equality only on invariants.** Equality checks and joins across spaces **MUST** target invariant forms (the **≡_UNM** quotient or a declared **Normalization-fixed** representation), never raw un-fixed coordinates.

##### A.19:5.1.7 - Metric discipline & calibration (Normative)

Use the **weakest safe structure** required by the argument (pre‑order → semi‑metric → metric).
* **If a distance overlay is declared**, any acceptance predicate or KPI defined over a CharacteristicSpace **SHALL be non‑expansive** (Lipschitz ≤ 1) w.r.t. the published `d` on the **declared domain** (raw coordinates or NCVs, as specified), or else state an explicit margin that absorbs any expansion.
* **If only an order overlay is declared**, any acceptance predicate or KPI **SHALL be isotone** w.r.t. the declared product order.

*Minimal obligations:*
1) **Publish the metric (if used).** If a distance overlay is used, the space **MUST** publish the distance function `d` (including any weights and parameters) and its declared domain of applicability.
2) **Bound expansion.** Any acceptance predicate or KPI that relies on `d` **MUST** be shown **non-expansive** (Lipschitz ≤ 1); otherwise an explicit **expansion bound** and compensating **margin** **MUST** be stated.
3) **State error and commutation.** If a metric is used together with **NormalizationFix**, the specification **MUST** state (a) the maximum tolerated measurement and calibration error and (b) whether `d` **commutes** with the **NormalizationFix** (or provide a disclaimer and additional guard if it does not).

##### A.19:5.1.8 - `CharacteristicSpacePredicate` (by-value)

Use a `CharacteristicSpacePredicate` when a threshold, band, region, dominance condition, or composed criterion must remain semantically recoverable and reusable independently of one description or evaluation. Its complete by-value meaning contains:

- the exact `CharacteristicSpace` and the coordinates read from it;
- each coordinate's scale and value interpretation;
- the identity mapping or exact A.19.UNM normalization instances, and any F.9 Bridge with exact endpoints and declared loss when meanings or planes differ;
- the operator or comparator semantics supplied by A.19.CPM, G.4, or another named direct consumer interface;
- the cut value, band, region, or explicitly composed subpredicates; and
- the polarity that determines which side or region satisfies the predicate.

An arbitrary condition relation is not automatically a coordinate tuple. The predicate use must recover either a direct characteristic assignment already governed for that condition or an explicit projection or Bridge from the condition to the predicate input. When the affected entity differs from the condition's participants, the consuming relation or claim must also recover how that entity and use are related to the projected input.

The predicate owns no applicability, assessment, observation, evidence, or evaluation window. A consumer separately binds the exact `U.ClaimScope`, relevant `U.ContextSlice` membership, effective reference scheme and plane, application or evaluation window, input value, and evaluation operation. A dated evaluation is `U.Work`; its actual operation application binds the predicate and input and returns the direct owner's typed result. A criterion-description episteme can express the predicate, and an assertion episteme can claim an evaluation result, but neither episteme nor result is the predicate.

Predicate identity changes only when its semantic components change. Coextensional wording, notation, carrier, publication, identifier, or description-edition change does not by itself create another predicate. A consumer may evaluate the same predicate in another scope or window without changing the predicate; it may not silently change the space, coordinate projection, scale, normalization or Bridge, comparator, cut, band, or polarity while claiming reuse.

**Minimally viable case.** For a pump space with `batteryVoltage` on volts, `batteryReady := batteryVoltage >= 24 V` has the pump space, voltage coordinate and scale, `>=`, `24 V`, and positive polarity as its by-value meaning. A maintenance check separately binds Pump #37, its claim scope and current slice, the evaluation interval, the measured voltage input, and the direct evaluation result. A different projection such as controller supply voltage is inadmissible unless named; a later description edition with the same semantic predicate does not change it.

#### A.19:5.2 - State Spaces & Comparability

> **Memory hook:** Compare only values in the same declared space, or values carried into one common space through an exact mapping or Bridge. Reusing a predicate also requires the same semantic predicate; applying it requires separately stated scope, plane, and window.

This section supplies space projection, embedding, product, and two coordinate-comparability regimes. It does not perform a CPM comparison or a SelectorMechanism selection. A consumer that names a state or category cites the declared space and predicate, then keeps its own scope, evaluation, result, evidence, and work relations.

A CharacteristicSpace may be written abstractly as `CS = ⟨I, basis⟩`, where `I` indexes slots and `basis` is the ordered set of `(Characteristic, Scale)` bindings. A consumer-specific label for a space does not create another A.19 kind; the consumer instead states the exact role, entity, claim scope, context-slice membership, effective reference scheme and plane, and predicate relevant to that use.

##### A.19:5.2.1 - CS Operators (notation-neutral, reference-scheme-local)

To enable model composition, define operations on CharacteristicSpaces independently of notation. Every operation states its effective `U.ReferenceScheme` and reference plane. When an endpoint differs in scheme or plane, use an exact F.9 Bridge; no umbrella context value supplies the correspondence.

###### A.19:5.2.1.1 - Subspace – **Projection** `π_S : CS → CS|_S`.
Given a CharacteristicSpace CS with basis _I_ (slots) and a chosen subset of slot indices $S \subseteq I$, one can form the **subspace** $CS|_S$ which includes only the slots in _S_ and omits all others. The projection map `π_S` takes any state _x_ in the original space and **projects** it onto the coordinates indexed by _S_, effectively discarding the other coordinates. This operation is straightforward: if $S = \{i_1, i_2, … \}$, then $CS|_S$ has those slots, and any state in $CS|_S$ corresponds to a state in CS with the other coordinates ignored.
**Properties:** Projection is **idempotent** (`π_S ∘ π_S = π_S`) and, if an order or other structure is defined solely on the subspace’s slots, `π_S` preserves that structure (e.g. it will reflect any order that depends only on slots in _S_).

###### A.19:5.2.1.2 Embedding – **Injection** `ι : CS₁ ↪ CS₂`.
An **embedding** is a structure-preserving **injection** from one space CS₁ into another space CS₂. It consists of two parts: (a) an injective **slot correspondence** from CS₁ to CS₂, and (b) (only where needed) cited **normalization instances** that make the correspondence semantically safe. Formally, let CS₁ have basis _I₁_ and CS₂ have _I₂_. An embedding declares an injective function _m: I₁ → I₂_ that identifies each slot of CS₁ with a corresponding slot in CS₂.

For each slot _i ∈ I₁_ where the scale or unit differs from the target slot _m(i)_ in CS₂, the embedding **MUST cite** a `NormalizationMethodInstanceId` (per **A.19.UNM**) that re-expresses values from `ValueSet(slot_i)` into `ValueSet(slot_{m(i)})` within the declared invariants and validity window. The embedding does **not** define normalization semantics; it only references the required instances.

Intuitively, an embedding says: “Any coordinate tuple from CS₁ can be interpreted as a coordinate tuple in CS₂, possibly after converting units or re‑scaling, and without losing any information except what the declared **NormalizationMethods** intentionally **coarse‑grain**.” If there is no loss at all (**NormalizationMethods** are identity or strict conversions), the embedding is essentially an inclusion of one space into a larger one; if there is some information loss (e.g., converting a fine‑grained scale to a coarse one), that loss is explicit in the **NormalizationMethodDescription**. **Locality:**

An embedding whose endpoints share semantic interpretation remains local to their declared reference scheme and plane. A cross-scheme or cross-plane embedding requires an F.9 Bridge with exact endpoints, preserved and lost meaning, applicable use, CL value, and any receiving assurance consequence; the relevant A.6.1 operation application cites that Bridge explicitly.

**Normalization declaration duties (MUST):** Each cited `NormalizationMethodInstanceId` satisfies A.19.UNM declaration and admissibility obligations, including method-class token and validity window. C.16 governs calibration and measurement backing when relied on. Normalization alone does not license a change of reference scheme, plane, predicate, scope, or evaluation window; each changed boundary needs its direct declaration or Bridge.

###### A.19:5.2.1.3 Product – **Combination** `CS₁ ⊗ CS₂ = CS⊗`.
The **product** of two spaces CS₁ and CS₂ is a new space **CS⊗** that effectively contains all slots of CS₁ and all slots of CS₂. If CS₁ has index set _I₁_ and basis slots {slot₁…} and CS₂ has _I₂_, then $CS⊗$ has index set $I\_⊗ = I₁ ⊎ I₂$ (disjoint union) with each slot’s definition carried over from its original space. In practical terms, any state in the product space is a pair _(x₁, x₂)_ where _x₁_ is a state of CS₁ and _x₂_ is a state of CS₂ (assuming the two spaces pertain to possibly different aspects or roles). **Use cases:** Product spaces allow modeling **multi-role scenarios** or bundling an entity’s state with some environmental or contextual state. For example, one might take a space of internal capability metrics and ⊗ with a space of external conditions to form a combined space for “readiness under conditions.” **Note:** When combining scores or coordinates from a product space, one must be mindful of scale incommensurability. Cross‑slot aggregation **SHALL** proceed only via a declared **Γ‑fold** (B.1) and, where needed, explicitly declared **NormalizationMethods**; naïve arithmetic is forbidden. The product operation itself doesn’t perform any aggregation; it only sets the stage.

##### A.19:5.2.2 - Comparability of **States** (two admissible regimes)

A label such as `Ready`, `Authorized`, or `Degraded` is a consumer-side category, not a space or comparison result. Its direct owner states the predicate and evaluation use. Comparing two coordinate states depends on the declared spaces, mappings, scales, and comparison scope; A.19 permits only the following two coordinate regimes.

###### A.19:5.2.2.1 Coordinatewise comparability (`≼_coord`)

Two states can be compared **coordinatewise** only under strict conditions. Essentially, we require the states to be expressed in the **same measurement space**, with the **same units and scales**, and using the **same state definitions**. Formally, coordinatewise comparison is allowed **only if all of the following hold**:

-   **Same space.** Both coordinate values lie in the same `CharacteristicSpace` by value. Similar names, shared storage, or a common model-use label are insufficient.

-   **Scale congruence.** For each slot being compared, the scale type, unit, and polarity orientation are **identical**. For example, if comparing temperature values, both must be on the same scale (say, °C on a ratio scale with “higher = hotter” orientation). No unit mismatches or differing interpretations can be present.

-   **Predicate and use congruence.** When comparison depends on a category predicate, both values use the same `CharacteristicSpacePredicate` by value. CPM still states the exact comparison scope, comparator, reference plane, and evaluation window; A.19 does not infer them from matching labels.

When these conditions are met, one can define a **coordinatewise preorder** over states. Common patterns include:

- **Dominance:** For a given set of “higher is better” slots, we say state *x* **≼<sub>coord</sub>** state *y* if and only if for *every relevant slot a*, the coordinate $a(x) \le a(y)$ (**after orienting all slots to the declared polarity for that slot**). In other words, *y* is as good or better on all enforced criteria. This defines a Pareto-like ordering (often partial, not total).

-   **Predicate band inclusion:** If states are defined by satisfying declared predicate bands (e.g. State _Y_ means declared coordinates stay above specific levels), then we might say _x_ **≼<sub>coord</sub>** _y_ if _x_ satisfies every predicate that defines _y_’s state. For instance, if state _y_ = “High Performance” requires speed > 100 and accuracy > 90%, then _x_ is “no less than y” if _x_ also satisfies those predicates.

By default, **no comparability** is assumed unless proven. If any of the above congruence conditions fails, one must **not** fall back to ad-hoc comparisons (like matching by name or normalizing without declaration). Either switch to a **normalization-based regime** or declare the states **incomparable**.

###### A.19:5.2.2.2 Normalization‑based comparability (`≼_normalization`)

When two state vectors do not meet the strict conditions for coordinatewise comparison (e.g. they come from different spaces, or the “same” Characteristics are measured on different scales or units), the only sanctioned way to compare them is: **normalize, then compare**.

Concretely: if we have state _x_ in CS₁ and state _y_ in CS₂, a normalization‑based comparison is permitted only if the model can cite a set of `NormalizationMethodInstanceId`(s) under a chosen **UNM** (per **A.19.UNM**) that lands the relevant coordinates of _x_ into CS₂ (or lands both into a declared common target space). The result is understood as **NCVs** (or an `≡_UNM` quotient class) per A.19.UNM.

**Comparability rule (normalize-then-compare).** We say _x_ **≼<sub>normalization</sub>** _y_ only if, after applying the cited normalization instances to produce a representation of _x_ in CS₂ (or a common target), the mapped state can be compared **coordinatewise** under `≼_coord`. In other words, we never compare raw _x_ and _y_; we compare *after mapping into a common, well-typed space*.

If normalization also crosses reference schemes or planes, the comparison cites an F.9 Bridge with exact endpoints and any CL value, plus the CPM comparison scope and evaluation window. The receiving assurance pattern applies any B.3 consequence; normalization does not silently change meaning or grant comparability.

**Inspectability.** Each normalization instance used for comparison is recoverable through its A.19.UNM declaration. C.16 governs measurement and calibration backing. If values differ in scale, reference scheme, or plane, the normalization and Bridge choices and their limitations remain explicit.

> **Mnemonic:** Never compare before both values are carried into the same well-typed space; never claim the same predicate, scope, plane, or window merely from matching labels.

##### A.19:5.2.3 - Predicate-use and state-assertion boundary

A.19 defines the space and `CharacteristicSpacePredicate`; it does not define a state assertion, applicability relation, dated evaluation work, gate, evidence relation, assurance result, or permission to act.

A consumer use recovers: the exact subject or input; any direct characteristic assignment or projection from that subject; the A.19 space and predicate; one set-valued `U.ClaimScope`; relevant A.2.6 `U.ContextSlice` membership; effective `U.ReferenceScheme` and reference plane; application or evaluation window; and any F.9 Bridge. The direct consumer owns the actual evaluation operation and typed result. A.10 provenance, G.11 currentness, measurement backing, assurance, and receiving-work disposition remain separate.

For a `Ready` claim requiring temperature below a cut and pressure above a cut, A.19 supplies the two declared coordinates, scales, normalization or Bridge basis, operators, cuts, polarity, and conjunction. The state-assertion owner binds the pump, scope, slice, evaluation interval, actual inputs, result, and evidence use. Changing the evaluation interval does not change the predicate; changing either cut does.

Pulling a predicate into another space or pushing an assertion through an embedding requires the exact coordinate correspondence, normalization, and Bridge. If an input projection or semantic correspondence is missing, the current use is incomparable or unevaluable rather than approximately valid.

##### A.19:5.2.4 - Cross-reference-scheme and cross-plane comparability

A comparison across reference schemes or planes is admissible only through an F.9 Bridge that states exact source and target endpoints, preserved and lost meaning, direction, applicable use, and CL when current. The coordinate mapping and A.19.UNM instances are explicit. A reverse comparison needs its own justified direction.

The comparison may reuse a predicate only when the Bridge preserves every semantic predicate component. CPM separately binds comparison scope, comparator, input values, effective reference plane, and evaluation window. A Bridge does not copy scope or time, and a common label does not establish predicate equality.

B.3 or the direct assurance pattern owns any confidence or margin consequence. If a critical coordinate lacks an admissible normalization or Bridge, or if the predicate, plane, scope, or window cannot be held fixed, report the values as incomparable for that use.

##### A.19:5.2.5 - Characteristic-Space Reference Chain

When a consumer pattern evaluates a checklist, StateAssertion, gate, assurance argument, or decision through a declared `CharacteristicSpace`, keep the space-related references distinct:

`raw coordinates -> NormalizationMethodInstance -> quotient or NormalizationFix -> optional indicator choice -> optional order or distance overlay -> neighboring checklist, assertion, gate, assurance, or decision claim`

The left side of this chain is A.19-facing: declared space, normalization reference, quotient or fixed chart, and declared overlay. The right side is governed by the consumer pattern. Co-implementation in software or records does not collapse the conceptual references.

#### A.19:5.3 - Operator library (notation‑neutral)

**Spaces:** `Sub` (projection), `Emb` (embedding), `Prod` (product), `Quot` (quotient by declared equivalence), `NormalizationFix` (fix to a named chart or edition).

**Predicate and assertion transport:** `Pull` (pull a predicate through an embedding and declared normalization), `Push` (push an assertion with proof or waiver under its direct owner), `Indicatorize` (apply an `IndicatorChoicePolicy`), `Align_B` (align exact reference-scheme or plane endpoints through a Bridge), and `Fold_Γ` (admissible aggregation under its governing pattern).

**OP-1 (Normative).** If `Align_B` supports a gate, comparison, or assurance claim, cite the exact Bridge and CL where current. The direct consumer owns scope, evaluation window, result, and any B.3 consequence. Silent cross-scheme or cross-plane reuse is forbidden.

#### A.19:5.4 - Set-view, comparison, and selection boundary

A typed view over a set, `ComparisonResultSlot`, `SelectionSlot`, shortlist, archive, portfolio, search-space role, outcome-space role, metric-based neighborhood, and transition-sensitive selection interpretation are consumer objects. They may cite an A.19 space, predicate, order, distance overlay, or transition relation, but A.19 does not define their result, view, comparison, or selection identity. Keep the underlying source set and exact A.19 values recoverable; use A.19.CPM, A.19.SelectorMechanism, the direct view or publication pattern, and the exact transition owner for the consuming claim.

