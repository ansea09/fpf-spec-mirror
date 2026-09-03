---
chunk_kind: "child"
pattern_id: "A.19"
pattern_title: "CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
section_id: "A.19:5"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19/A.19__007_solution.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "A.19 — CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
  - "A.19:5 — Solution"
line_start: 29837
line_end: 30042
dependencies:
  - "A.10"
  - "A.15"
  - "A.17"
  - "A.18"
  - "A.19.CHR"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.19.UNM"
  - "A.2.6"
  - "A.6.5"
  - "B.1"
  - "C.16"
  - "C.2.1"
  - "E.24"
  - "F.17"
  - "F.9"
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
  - "state trajectories"
  - "structural overlays"
  - "subspace"
  - "system-role–Method–Work assertions stay outside A.19"
---

### A.19:5 - Solution

#### A.19:5.1 - `U.CharacteristicSpace`

##### A.19:5.1.1 - Type signature

Each slot `i` names one `U.Characteristic` and one chosen `Scale`:

> `slot_i = (Characteristic_i, Scale_i)`.

The Characteristic supplies its subject/input signature: the entity kinds and roles required when it is assigned a value. For a relation Characteristic the signature also gives the role order, or states that the relation is symmetric. A use of the slot binds that participant tuple separately. The tuple is not the Coordinate; the Coordinate is a value on the chosen Scale. C.16 uses the same separation between measurand or subject tuple and measured Coordinate.

The **CharacteristicSpace** is the Cartesian product of the slots' genuine Scale value sets:

> `CS = product_i ValueSet(Scale_i)`.

A point `x` in `CS` supplies one Coordinate `x(i)` from `ValueSet(Scale_i)` for every slot. Using that point for a subject separately binds a conforming subject/input tuple `b_i` and states or evaluates the characteristic assignment between `b_i` and `x(i)`. For example, the distance Characteristic may bind `(Machine-A, Machine-B)` while its Coordinate is `3.5 m`.

A complete state is total over the selected basis. An observation or evaluation input may instead be partial: it supplies Coordinates only for a subset of slots and records `missing`, `censored`, `unknown`, or another observation status separately. A consumer applies its own applicability and tri-state or error rule before treating such input as a state. `not-applicable` is normally an applicability fact, not a Scale value; a domain may use it as a genuine value only when the Scale explicitly defines that meaning.

Any `U.Dynamics.stateSpace` refers to a declared `CharacteristicSpace`, and its states and trajectories use points in that space. A.3.3 supplies the dynamic law, time base, observation relation, and prediction-use conditions.

##### A.19:5.1.2 - Slot discipline (invariants)

To ensure consistency and comparability, a CharacteristicSpace must obey the following invariants:

-   **A19-CS-1 (Exactly one per slot).** Each slot **binds exactly one** Characteristic to **exactly one** Scale (including a specific Unit or kind, if applicable). This mirrors the CSLC clause of “one aspect – one scale”: there are no ambiguous or compound mappings in a single slot. (If a Characteristic can be measured on multiple scales, only one is chosen for a given space; others would require separate slots or a different space.)

- **A19-CS-2 (Named basis).** A CharacteristicSpace declaration contains an ordered basis of slots. Each slot has a stable technical name and makes its Characteristic, Scale, position, and the Characteristic's subject/input signature recoverable. Plain-language aliases may aid recognition but do not change the basis.

- **A19-CS-3 (Stable meaning).** Do not silently change a slot's Characteristic, Scale, or position while claiming the same space. Declare the changed space and an explicit mapping from the earlier space. Call that mapping an embedding only when it is point-injective and preserves every named structure; use a lossy normalization or projection for deliberate coarse-graining.

- **A19-CS-4 (Arity preservation).** A slot for an entity Characteristic binds one subject. A slot for a relation Characteristic binds the exact ordered or unordered subject/input tuple required by that Characteristic. Direction and symmetry belong to this signature. In either case the Coordinate remains one value on the declared Scale; the participant tuple never substitutes for it.

- **A19-CS-5 (No hidden normalization, preference, or aggregation).** A `CharacteristicSpace` carries no implicit normalization, polarity preference, threshold, formula, or aggregation. A `CharacteristicSpacePredicate` may declare polarity, operator semantics, and a cut or band over that space. Normalizing, indicatorizing, scoring, folding, comparing, and selecting remain explicit operations under their subject patterns; the space declaration itself performs none of them. A.19.UNM governs normalization semantics and admissibility; C.16 governs relied-on measurement and calibration claims.
- **A19-CS-6 (Value and absence discipline).** Each slot declares its admissible Scale domain. Missing, censored, unknown, and inapplicable input states stay with the observation, record, or evaluation use rather than entering the ontic Scale value set. `not-applicable` is a Scale value only when that domain explicitly gives it a subject-side meaning.

- **A19-CS-7 (Space-versus-consumer boundary).** A `CharacteristicSpace` declaration contains only its basis, optional overlays, and typing hooks. A consumer separately declares references to the space, relation positions, source use, views, publication details, applicability, partial-input handling, and evaluation results.

##### A.19:5.1.3 - Minimal structure hooks (optional overlays)

A CharacteristicSpace has no default order, topology, or distance. Declare only the structure that a real use needs:

- **Order overlay.** `OrderOverlay = (D, preceq, laws, applicability)`, where `D` is a stated subset of `CS`, `preceq` is a typed binary relation on `D`, and `laws` say whether it is a preorder, partial order, or another named order. The declaration explains how the relation respects each participating Scale.
- **Topology overlay.** `TopologyOverlay = (D, tau, construction, applicability)`, where `tau` is a topology on `D`. The construction may cite a product topology or give another basis; the name alone supplies no continuity claim.
- **Distance overlay.** `DistanceOverlay = (D, d, distanceLaws, parameters, applicability)`, where `d : D x D -> nonnegative values`. `distanceLaws` states exactly which separation, symmetry, direction, and triangle conditions hold; parameters include any weights, units, normalization basis, and validity conditions.

The declaration of every overlay is optional. Once a consumer relies on one, however, it names the exact overlay and stays within its domain and applicability conditions; any claimed order preservation, continuity, convergence, sensitivity, robustness, or stability must satisfy the laws of that overlay. An overlay adds analysis structure and cannot redefine a slot's Characteristic, Scale, admissible operations, or Coordinate meaning.

Here **distance** means a mathematical distance function, not a performance measure or a C.16 measurement method. Use `U.DHCMethod` or `U.DHCMethodRef` for measurement templates.

##### A.19:5.1.4 - Dynamics hook (typing only)

Any model of change or dynamics in FPF must declare the state space it operates over. Formally, `U.Dynamics.stateSpace` **SHALL** be specified as a reference to a `CharacteristicSpace`. This creates a typing requirement: the dynamic model can only produce states and trajectories of states that belong to the given space. All predicates or predictions in such a dynamics model are understood to **quantify over** sequences of points in that CharacteristicSpace (with time semantics governed by A.3.3’s time base and laws). **Note:** A.19 defines only the structure of the state space; it deliberately **does not** fix any time base or dynamic law. Those remain the responsibility of the dynamics pattern (A.3.3). A.19 simply ensures there is a well-defined space in which states are located, so that dynamics are decoupled from any narrative “stage” and instead treat evolution as movement through this space.

##### A.19:5.1.5 - Lexical discipline (Normative)

In all **normative references, definitions, and identifiers** related to this pattern, the specification uses the canonical measurement terminology: **Characteristic**, **Scale**, **Level**, **Coordinate**, **CharacteristicSpace**, **slot**, **basis**. Legacy terms like “axis”, “dimension”, or “point” are **forbidden** in Technical and Formal registers of the spec (per A.17’s lexical rules). They may appear _at most once_ in explanatory **Plain** language as mapped aliases to aid understanding (and if used, must be explicitly identified as equivalent to the official terms). In this pattern, we consistently use “slot” or “basis element” (never “axis”) to refer to a component of a space, and “Characteristic” (never “dimension”) to refer to the measured aspect. This lexical discipline ensures clarity and consistency across the framework (see A.17 and C.16 L-rules for the formal policy on terminology).

##### A.19:5.1.6 - Quotients & NormalizationFix (Normative)

**Subject-pattern note.** `≡_UNM` and `NormalizationFix` are defined in **A.19.UNM**. This section constrains only how they are **cited** when used in state‑space reasoning.

**Design rule — read invariants, not labels.** Any checklist, acceptance predicate, equality check, join, or comparability claim over a `CharacteristicSpace` that depends on representation choice (chart, unit, reference plane, normalization choice, or label) **SHALL** be evaluated on **quotients by ≡_UNM** or on explicitly **Normalization‑fixed** charts, not on raw labels.
*Minimal obligations:*
1) **Name the quotient or fix.** If a checklist predicates over a **normalization‑variant** property, it **MUST** name the **NormalizationFix** (including the referenced **UNM** and the relevant `NormalizationMethodInstance`(s), by reference) and thus the **≡_UNM** class.
2) **Declare NormalizationMethod class.** Every normalization used **MUST** name its method‑class token and validity window **as defined in A.19.UNM** (do not restate the class taxonomy here).
3) **Join and equality only on invariants.** Equality checks and joins across spaces **MUST** target invariant forms (the **≡_UNM** quotient or a declared **Normalization-fixed** representation), never raw un-fixed coordinates.

##### A.19:5.1.7 - Overlay use, sensitivity, and calibration (Normative)

Use the weakest declared overlay that the argument needs. Declaring an order or distance does not make every predicate monotone, every map non-expansive, or either property necessary or sufficient for acceptance. Bands, target regions, and Boolean cuts are valid even when they are not isotone or continuous.

When a consumer makes a sensitivity, robustness, continuity, stability, or prediction-use claim, that consumer states:

1. the exact function, predicate evaluation, or transition map and the overlay it uses;
2. the domain, codomain, applicability conditions, and claimed property;
3. any bound, margin, approximation, uncertainty, or error allowance required by the consumer's policy; and
4. the evidence or argument needed for that use.

A useful bound need not be `Lipschitz <= 1`; its admissible value comes from the named use and policy. Claim isotonicity only when the use depends on order preservation. Claim commutation with normalization only when that exact composition matters. C.16 governs relied-on measurement and calibration claims. A.3.3 governs prediction error, horizon, and model applicability; A.20, A.21, G.4, and the direct authority pattern govern their own constraint, gate, criterion, and decision consequences. Non-expansiveness or commutation alone grants no gate, release, assurance, or work authority.

##### A.19:5.1.8 - `CharacteristicSpacePredicate` (by-value)

A `CharacteristicSpacePredicate` is a typed unary predicate over one declared space:

> `P : D_P -> Boolean`, where `D_P` is a declared subset of `CS`.

Its input variable denotes one state. The predicate declares which coordinates it reads and any projection used to obtain them. Its complete by-value meaning contains:

- the exact `CharacteristicSpace`, input variable, domain, and coordinate projection;
- each read Coordinate's Scale and value interpretation;
- any exact coordinate projection or A.19.UNM normalization instance used to obtain those inputs;
- the operators, cuts, bands, regions, or unary subpredicates used in its Boolean expression; and
- the polarity that says which outcome satisfies the predicate.

Thresholds, bands, and regions are unary predicates of this kind. Compose predicates with logical operators only after their input bindings and domains are aligned; otherwise give the composition an explicit binding that makes the conversion visible. A dominance or other comparison between two states is instead a typed binary comparison relation such as `R : D_left x D_right -> Boolean`, governed by A.19.CPM or another direct comparison pattern. Its comparator application and result are not components of a unary `CharacteristicSpacePredicate`. Use a genuinely n-ary predicate only when its full variable roles, domains, projections, and result type are declared.

An arbitrary condition relation is not automatically a state or Coordinate. A use binds either a direct characteristic assignment or an explicit governed projection from its subject/input tuple to the predicate input. When the affected entity differs from the condition participants, the consumer also states that direct relation. An F.9 Bridge relates two exact local senses; it is not this subject-to-input binding.

The predicate carries no applicability, assessment, observation, evidence, or evaluation window. A consumer separately binds the exact `U.ClaimScope`, relevant `U.ContextSlice` membership, effective reference scheme and plane, application or evaluation window, available input, and evaluation operation. An evaluation may return `unknown`, `not-applicable`, or `error` when input or applicability is unresolved; those consumer results do not enlarge the predicate's Boolean codomain or the space's Scale value sets. A dated evaluation is `U.Work`; its operation application and result remain separate from the predicate.

Predicate identity changes when one of these semantic components changes. Wording, notation, carrier, publication, identifier, or description-edition changes alone do not create another predicate. A consumer may evaluate the same predicate in another scope or window, but may not silently change its space, projection, Scale, normalization, expression, cut, band, composition, or polarity. An obtaining semantic Bridge or plane relation may be cited by one consumer use without becoming part of predicate identity.

**Minimally viable case.** In a pump space with `batteryVoltage` on the volt Scale, `batteryReady(x) := x.batteryVoltage >= 24 V` is a unary predicate with Boolean result. A maintenance check separately binds Pump #37, its current measured input and window, and the evaluation result. Comparing two pumps by voltage would be a separate binary comparison relation, not a second reading of `batteryReady`.

#### A.19:5.2 - State Spaces & Comparability

> **Memory hook:** Compare only values already in the same declared space or carried into one common space through an exact coordinate mapping. Reusing a predicate also requires the same semantic predicate. If the use also claims a relation between two exact F.17 local senses, cite an F.9 Bridge only after its predicate obtains and state the bounded-use claim and reliance separately. If the ReferencePlane changes, cite the applicable plane relation. Scope and window remain separate in either case.

This section supplies space projection, embedding, product, and two coordinate-comparability regimes. It does not perform a CPM comparison or a SelectorMechanism selection. A consumer that names a state or category cites the declared space and predicate, then keeps its own scope, evaluation, result, evidence, and work relations.

A CharacteristicSpace may be written abstractly as `CS = ⟨I, basis⟩`, where `I` indexes slots and `basis` is the ordered set of `(Characteristic, Scale)` bindings. A consumer-specific label for a space does not create another A.19 kind; the consumer instead states the exact use or relation position, entity, claim scope, context-slice membership, effective reference scheme and plane, and predicate relevant to that use.

##### A.19:5.2.1 - CS Operators (notation-neutral, reference-scheme-local)

To enable model composition, define operations on CharacteristicSpaces independently of notation. Every operation states its effective `U.ReferenceScheme` and reference plane. Those values locate the operation but create no correspondence. When a use relates two exact F.17 local senses, test the direct F.9 predicate and cite the Bridge only when it obtains; state the bounded-use claim and any reliance separately. A ReferencePlane crossing cites its applicable plane relation. A scheme or plane difference alone establishes neither relation.

###### A.19:5.2.1.1 - Subspace — projection

For a space `CS_I` with basis `I` and a subset `S`, the projection `pi_S^I : CS_I -> CS_S` keeps the Coordinates in `S` and discards the others. The type-correct laws are `pi_I^I = identity_CS_I` and, for `T subseteq S subseteq I`, `pi_T^S after pi_S^I = pi_T^I`. A projection preserves an order, topology, or other structure only when that fact follows from the named overlays; projection alone makes no such promise.

###### A.19:5.2.1.2 - Embedding and lossy mapping

An embedding `iota : CS_1 -> CS_2` is point-injective and preserves every structure named by its declaration. It gives an injective slot correspondence and an injective value map for each corresponding slot. Identity maps and exact, reversible unit conversions can support an embedding when they preserve the declared Scale meaning. The declaration states its domain, image, preserved structures, and any A.19.UNM instances used.

A coarse-graining, binning, many-to-one normalization, or dropped-coordinate operation is not an embedding. Declare it as a lossy mapping or projection, state the preserved and lost distinctions, and let each consumer decide whether that loss is admissible for its comparison, prediction, gate, or assurance use. When the use relates two exact F.17 local senses and the F.9 predicate obtains, cite that Bridge and a separate bounded-use claim. A ReferencePlane change instead cites its applicable plane relation. The coordinate mapping, semantic relation, plane relation, and C.16 calibration or measurement backing remain separate.

###### A.19:5.2.1.3 Product – **Combination** `CS₁ ⊗ CS₂ = CS⊗`.

The **product** of two spaces CS₁ and CS₂ is a new space **CS⊗** whose basis is the disjoint union of both bases, so even same-named slots retain their source identity. Its state is a pair `(x₁, x₂)`. For example, a product can combine internal capability Coordinates with external-condition Coordinates for a readiness use. The product does not aggregate them: any cross-slot aggregation uses a declared B.1 `Gamma` fold and any needed A.19.UNM normalization.

##### A.19:5.2.2 - Comparability of **States** (two admissible regimes)

A label such as `Ready`, `Authorized`, or `Degraded` is a consumer-side category, not a space or comparison result. Its subject pattern states the predicate and evaluation use. Comparing two coordinate states depends on the declared spaces, mappings, scales, and comparison scope; A.19 permits only the following two coordinate regimes.

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

If a normalization use also spans different reference schemes or planes, keep the decisions separate. The A.19.UNM instance supplies the coordinate mapping. Cite an F.9 Bridge only when the use relates two exact F.17 local senses and its direct predicate obtains; state the bounded-use claim and reliance separately, with `CL` only as optional evidence shorthand. A ReferencePlane crossing cites its applicable plane relation. CPM supplies the comparison scope and evaluation window, and B.3 enters only for an actual assurance use. None of these relations or consequences follows from the scheme or plane difference alone.

**Inspectability.** Each normalization instance used for comparison is recoverable through its A.19.UNM declaration. C.16 governs measurement and calibration backing. When values differ in scale, reference scheme, or plane, keep the normalization, any independently obtaining semantic Bridge with its separate use claim, any applicable plane relation, and their limitations explicit.

> **Mnemonic:** Never compare before both values are carried into the same well-typed space; never claim the same predicate, scope, plane, or window merely from matching labels.

##### A.19:5.2.3 - Predicate-use and state-assertion boundary

A.19 defines the space and `CharacteristicSpacePredicate`; it does not define a state assertion, applicability relation, dated evaluation work, gate, evidence relation, assurance result, or permission to act.

A consumer use recovers: the exact subject or input; any direct characteristic assignment or projection from that subject; the A.19 space and predicate; one set-valued `U.ClaimScope`; relevant A.2.6 `U.ContextSlice` membership; effective `U.ReferenceScheme` and reference plane; application or evaluation window; and, only when current, any obtaining F.9 Bridge with its separate bounded-use claim and reliance, plus any applicable plane relation. The consumer identifies the exact evaluation-operation application and its typed result under the applicable evaluation or assertion rule. A.10 provenance, G.11 currentness, measurement backing, assurance, and receiving-work disposition remain separate.

For a `Ready` claim requiring temperature below a cut and pressure above a cut, A.19 supplies the two declared coordinates, scales, normalization or coordinate-mapping basis, operators, cuts, polarity, and conjunction. The actual state assertion binds the pump, scope, slice, evaluation interval, inputs, result, and evidence use. Any semantic Bridge or plane relation needed by that use remains separate. Changing the evaluation interval does not change the predicate; changing either cut does.

Transporting a predicate into another space or transporting an assertion across spaces requires the exact Coordinate correspondence. Use an embedding only for point-injective structure-preserving transport; use a declared lossy mapping or projection when normalization discards distinctions. If the use relates two exact F.17 local senses and the F.9 predicate obtains, cite that Bridge and its separate bounded-use claim. If the ReferencePlane changes, cite the applicable plane relation. A scheme or plane difference alone establishes neither relation. If the required correspondence is absent, the current use is incomparable or unevaluable rather than approximately valid.

##### A.19:5.2.4 - Cross-reference-scheme and cross-plane comparability

A comparison across reference schemes or planes follows the relations the case actually needs. When it relates two exact F.17 local senses and the F.9 predicate obtains, cite that Bridge and a separate bounded-use claim; `CL` is optional evidence shorthand. A plane crossing cites its applicable plane relation. Keep the coordinate mapping and A.19.UNM instances explicit. A context, scheme, or plane difference alone establishes no Bridge or comparison admissibility, and a reverse comparison needs its own justified direction.

A comparison may reuse a predicate only when its complete by-value meaning is unchanged. When a coordinate mapping is needed, it must preserve every predicate component required by this use. If the reuse also relates two exact local senses through an obtaining Bridge, a separate bounded-use claim states that semantic use and any required reliance passes. CPM separately binds comparison scope, comparator, input values, effective reference plane, and evaluation window. The Bridge alone copies neither predicate content, scope, nor time, and a common label establishes none of them.

B.3 or the direct assurance pattern contains the defining content for any confidence or margin consequence. Report the values as incomparable for the use when a critical coordinate lacks an admissible normalization or coordinate mapping; a separately needed semantic Bridge, bounded-use claim, or plane relation is absent; any required reliance does not pass; or the predicate, plane, scope, or window cannot be held fixed.

##### A.19:5.2.5 - Characteristic-Space Reference Chain

When a consumer pattern evaluates a checklist, StateAssertion, gate, assurance argument, or decision through a declared `CharacteristicSpace`, keep the space-related references distinct:

`declared Coordinates -> [normalization or quotient, when used] -> [indicator choice, when used] -> [order, topology, or distance overlay, when used] -> neighboring predicate evaluation, assertion, gate, assurance, or decision claim`

Only the branches actually used are present. A.19 supplies the declared space and any named mapping, quotient, or overlay; the consumer supplies applicability, operation, result, and consequence. Co-implementation in software or records does not collapse these values.

#### A.19:5.3 - Operator library (notation‑neutral)

**Spaces:** `Sub` (projection), `Emb` (embedding), `Prod` (product), `Quot` (quotient by declared equivalence), `NormalizationFix` (fix to a named chart or edition).

**Predicate and assertion transport:** `Pull` transports a predicate through a declared embedding or lossy mapping; `Push` transports an assertion with proof or waiver under its subject pattern; `Indicatorize` applies an `IndicatorChoicePolicy`; and `Fold_Gamma` performs admissible aggregation under its subject pattern. `Align_B` is not a space operator: when retained as a consumer mnemonic, it names only an already obtaining F.9 Bridge between two exact F.17 local senses. A ReferencePlane relation remains separate.

**OP-1 (Normative).** Use `Align_B` only after the direct F.9 predicate obtains. The consumer cites that exact Bridge, a separate bounded-use claim, and the reliance required for the named gate, comparison, or assurance use; `CL` remains optional evidence shorthand. A ReferencePlane crossing cites its applicable plane relation and does not use `Align_B` unless an independently obtaining semantic Bridge is also current. The consumer separately binds scope, evaluation window, and result; any assurance consequence requires a separately current B.3 assurance result.

#### A.19:5.4 - Set-view, comparison, and selection boundary

A view, comparison result, selection, portfolio, distance-based neighborhood, or transition-sensitive interpretation is a consumer value. It may cite an A.19 space, predicate, order, distance, or transition relation, but its identity and result remain with the direct view, comparison, selection, or transition pattern.

