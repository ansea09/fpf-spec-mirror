---
chunk_kind: "child"
pattern_id: "C.2.2"
pattern_title: "Reliability R in the F–G–R triad"
section_id: "C.2.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.2/C.2.2__005_solution.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "C.2.2 — Reliability R in the F–G–R triad"
  - "C.2.2:4 — Solution"
line_start: 44044
line_end: 44198
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.2.6"
  - "A.21"
  - "A.6.3.RT"
  - "B.1.3"
  - "B.3"
  - "B.3.3"
  - "B.3.4"
  - "C.16"
  - "C.2"
  - "C.2.3"
  - "C.21"
  - "C.29"
  - "C.3"
  - "C.3.3"
  - "C.3.A"
  - "E.14"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.9"
  - "G.2"
  - "G.6"
  - "G.7"
keywords:
  - "ClaimScope (G)"
  - "Congruence Level (CL / CL^k / CL^plane)"
  - "F–G–R"
  - "Reliability (R)"
  - "TA/VA/LA lanes"
  - "direct relation"
  - "evidence-bound"
  - "no implicit averaging"
  - "pathwise justification (PathId)"
  - "warrant"
  - "weakest-link"
---

### C.2.2:4 - Solution

#### C.2.2:4.1 - Canonical triad relation

**Definition DEF‑C2.2‑1 (Epistemic location).**
An epistemic location for a claim `c` is the tuple:

`Loc(c) = ⟨F(c), G(c), R_eff(c)⟩`

where:

* `F(c)` is Formality (C.2.3), treated as an **ordinal**.
* `G(c)` is Claim scope (A.2.6), treated as a **set-like scope object**.
* `R_eff(c)` names the effective warrant for this claim and use. Its meaning and scale come from the B.3 receiving model, not from the letter R. A probability-like or ratio-scale value in `[0,1]` needs that model; an ordinal proxy keeps its declared ordinal meaning.
  If no common quantitative model is justified, report R as unquantified with the separate support and bounded conclusion, rather than substitute zero or invent a score. When a guard consumes a path-specific value, identify the actual PathId and its model (§4.8.A / G.6); a declared policy name alone does not warrant collapsing paths into one scalar.

A location always concerns one exact claim. `G` carries its `U.ClaimScope`; any stance, reference plane, effective scheme, model-use basis, working situation, evidence basis, or validity window is stated separately when it changes interpretation or use:
* No generic `K` or Context value is part of epistemic-location identity; the exact subject-specific values above remain independently governed.
* `S ∈ {design, run}` is the claim’s stance value; keep design-time and run-time assurance separate.
* `ReferencePlane` is declared where applicable; plane crossings apply `CL^plane` and penalize **R only**.
* When the claim is published on the Working‑Model surface, the author also declares `validationMode ∈ {postulate, inferential, axiomatic}` (E.14 / B.3).

**Mode-to-lane hint (informative).** `validationMode` sets the *default expectation* for which assurance lane carries the initial support load (B.3.3 or B.3.5).
It does **not** add a new characteristic and does **not** change the meaning of `R`:
* `axiomatic` → VA-dominant (constructive grounding or proof carriers); if `ReferencePlane=world`, LA may still be required.
* `inferential` → VA+TA-dominant (reasoned chain + typing/alignment assurance); LA is optional and scope-bound.
* `postulate` → LA-dominant (empirical validation with freshness/decay); VA is optional.
In all modes, **R remains warrant**, not ontological truth; “proof ⇒ R=1 in the world” is a category error.

**Formal-input rule.** Empirical R may be N/A for a strictly axiomatic claim. Preserve the proof and its conclusion under the stated axioms; **do not set `R_proxy := F` for an R fold**. The tag `line=formal`, a postulative mode, or rescaling F into [0,1] supplies no conversion model. A declared F-derived ordinal proxy is valid only for its own ordinal meaning. Any F-derived value used as another quantity needs a receiving model establishing its meaning, scale, conversion, assumptions, and warranted application; in particular, checkability alone does not establish a probability about a real system.

`⟨F,G,R⟩` is an **assurance tuple**, not a `U.CharacteristicSpace`; do not draw “trajectories” in `⟨F,G,R⟩`.

#### C.2.2:4.2 - What Reliability R means in KD‑CAL

**Definition DEF‑C2.2‑2 (Reliability as warrant).**
`R` is a conservative, evidence-bound indicator of how strongly the claim "holds as stated" under its declared `U.ClaimScope` and the separately named evidence and use conditions. It is interpreted as *warrant strength*, not as truth.

**Prophylactic clarification.**

* A higher `R` means stronger warrant only within the same declared quantity, scale, claim, and receiving model. A number from another model is not automatically comparable.
* A higher `F` means “the claim’s form is amenable to higher-formality checking and wider reuse,” but does not itself imply the claim is warranted.
* A larger `G` means “the claim applies to more cases,” but does not itself imply the claim is warranted in those cases.

#### C.2.2:4.3 - Dependence-sensitive support composition

**Definition DEF‑C2.2‑3 (Support composition).**
For claim `c`, identify the support actually needed by its receiving use. Distinguish indispensable premises, alternative sufficient arguments, complementary evidence for the same question, support for different scope slices, and counterevidence. A source's presence in the graph does not make it an indispensable premise. B.1.3 supplies the synthesis Method and its guidance and controller examples.

Let `SpineClaims(P)` name premises and lemmas actually required by argument `P`; `SpineRelations(P)` names the actual scope, kind, plane, notation, source-local, model-use, and evidence-reuse relations it traverses. Satellite citations are not required premises. Retain each contribution's source, assumptions, scope, and limitations, including shared datasets, duplicated evidence, and common bias.

**Choose the operation from the model.** B.3 requires the target quantity, compatible scales, dependency assumptions, and warranted operation before an aggregate is calculated. An indispensable weak premise can limit an inference, but `min` is not a universal probability or warrant fold. Two necessary independent conditions with probabilities 0.9 each give 0.81 for their conjunction; minimum 0.9 overstates it. Without independence, use the warranted conditional model or leave the joint probability unresolved. Monotonicity and boundedness of a proposed rule are insufficient.

**Alternative and complementary support.** An actually sufficient argument may be usable without the others. A maximum can select the best attested argument value under a model whose result has that meaning; it does not measure combined corroboration. Complementary evidence may strengthen or qualify a conclusion by addressing different rival explanations or limitations, even when neither source is sufficient alone. Count neither publications nor method names as independent confirmation. A shared bias may leave apparent agreement uninformative. There is no universal “never exceed the best source” cap and no entangled-source fallback to minimum.

**Scope and conflict.** Retain different `G_path` slices under A.2.6; do not use maximum to hide unsupported regions. For overlapping-scope `p` and `¬p`, preserve credible contrary evidence. Separate claims only by distinctions established by the sources; otherwise narrow, qualify, or withhold the affected conclusion. An uninformative study, a lack of decisive support, and evidence against the claim are not interchangeable.

**Useful non-aggregate result.** If there is no warranted common model, retain separate support and limitations and give a bounded reasoned synthesis. This may finish the receiving question without a score, penalty table, extra study, or a record merely certifying their omission. The feasibility and worth of further inquiry are separate C.11/C.19.2 questions; their cost does not alter what the current evidence supports.

#### C.2.2:4.4 - Relation-specific congruence penalties route to R only

A reused claim may traverse more than one independently governed relation. Before calculating `R_eff`, state what actually changed and use the rule for that change. A.2.6 owns claim-scope operations; C.3/C.3.3 owns kind relations; F.9 owns a semantic Bridge between exact local-sense cells; notation, reference-plane, model-use, and evidence-reuse relations keep their own definitions. None is a universal crossing relation.

**Invariant INV-C2.2-1 (R-only penalty routing).** For each traversed relation `r` whose rule declares a congruence loss:

`F_out = F_in`
`G_out = translate(r, G_in)` only when `r` is an applicable A.2.6 scope translation; otherwise `G_out = G_in`
`R_out ≤ R_in` on the named ordered warrant scale for a loss-only transformation, with any numerical penalty justified by that relation's receiving model

A scope translation may narrow or re-express `G`; it never widens the claim silently. A change in formality is a new episteme or explicit ΔF move, not a transport penalty. A semantic Bridge changes neither kind nor scope by itself. A kind or plane relation supplies no semantic correspondence unless that separate relation also obtains. Evidence reuse changes warrant only through its own evidence-use or reliance claim.

There is no implicit crossing. If a reuse depends on a changed value and its required relation or operation is absent, unresolved, or outside its applicability, the reuse is non-conformant. This keeps guard macros simple: each path records the relations it actually traverses and routes their declared losses to `R`, while every other coordinate changes only under its own rule.

#### C.2.2:4.4.A - Worked micro-example: scope revision and evidence reuse

A materials-lab claim says:

> `c_lab:` "Adhesive X retains ≥85% tensile strength on Al6061 for 2 h at 120–150 °C."

Its declared scope is `G_lab := {substrate=Al6061, temp∈[120,150]°C, dwell≤2h, evidenceWindow=1y, rig=Calib-v3}`. A plant engineer proposes a narrower claim for Plant B. Two different moves are required.

1. **State the plant claim and its scope.** Here `temp` in `G_lab` is actual adhesive temperature. For this illustration, assume the plant calibration rule supplies a worst-case error bound `|T_actual − T_reported| ≤ 2 °C` throughout the declared use (C.16). Under A.2.6 the engineer retains `G_lab` and adds the condition `T_reported∈[122,148]°C`: under that bound, actual temperature is within `[120,150]°C`. This changes `G`; it is not an F.9 semantic Bridge and is not inferred from the words "lab" and "plant".
2. **Judge reuse of the lab evidence.** The exact A.10 or B.3 evidence-use and reliance claim names the lab evidence, plant claim, calibration edition, validity window, and intended use. A declared fit `CL=2` records the relation's fit, not a probability decrement. State the actual reuse limitation. Calculate a numerical `R_eff` only if a receiving model establishes the R quantity and this loss; otherwise keep the separate support and qualified plant conclusion. This judgement does not perform the scope edit.

If lab and plant use distinct local meanings for a material term, F.9 separately tests a Bridge between their exact F.17 cells. Its semantic loss is not the calibration correction or the evidence-reuse result. A further safety narrowing of that reported-temperature interval to `[125,145]°C` is another explicit A.2.6 ΔG− decision.

The example therefore preserves one simple rule: name each changed value and relation once, change `G` only through the scope rule, and reduce `R` only through the loss rule that actually applies.

#### C.2.2:4.5 - Effective reliability under reuse: a justified loss model

**Definition DEF‑C2.2‑4 (Effective reliability under reuse).**
A relied-on relation may introduce loss in the support for the receiving claim. Name that relation and its scope, semantic, notation, model-use, evidence-reuse, kind, or reference-plane rule. The corresponding `CL`, `CL^k`, or `CL^plane` is an ordinal summary belonging to that relation family; the ranks are not amounts to subtract from R.

A quantitative loss model names the receiving quantity and scale, input meanings, dependencies, loss interpretation, derivation or calibration, and applicability assumptions under B.3. If the model uses functions `Φ`, `Ψ`, `Φ_plane`, and a combining operation `Π`, cite their actual definitions and versions. A policy identifier, table, monotonicity, boundedness, or clipping to [0,1] does not by itself justify any of them.

For a loss-only interpretation on an ordered scale, worsening fit cannot by itself count as an improvement in warrant. The model must justify any pathwise CL minimum, repeated-loss treatment, or neutral term for an absent relation. Preserve separately justified ordinal chain-congruence operations in C.3.3; they do not provide a numerical R penalty.

**Positive quantitative illustration, not a default.** Suppose a receiving claim requires events A and B. An applicable model and evidence establish `P(A) ≥ 0.82` and `P(¬B) ≤ 0.15` for the same use. The probability bound `P(A ∩ B) ≥ max(0, 0.82 − 0.15) = 0.67` follows without an independence assumption. Here 0.67 is a lower bound, not a point estimate or a generic confidence score. The 0.15 term comes from the stated bound on failure of B, not a CL rank. If those event meanings or bounds are unavailable, the calculation is unavailable.

**Reuse conditions.** Apply a relation's justified admissibility or protection condition to the named use before relying on it; neither this pattern nor a bare CL rung creates a universal waiver obligation. If the condition is unsupported, limit or stop that reliance while retaining any independently supported source conclusion.

#### C.2.2:4.5.A - Formality and scale discipline

* Ordinal F, CL, and ordinal R proxies permit only operations justified for their ordered meanings, not arithmetic pretending they are ratio-scale measurements.
* A numerical R requires a justified receiving model even at high formality. A complete formal proof remains useful with empirical R marked N/A; a missing empirical score does not demote the theorem.
* When support has no common numerical model, publish its separate contributions, limitations, and the bounded conclusion. Use validity windows, empirical reproducibility information, and B.3.4 decay only where the claim actually consumes them.

#### C.2.2:4.6 - Evidence lanes are not new characteristics

KD‑CAL does not add new global coordinates beyond F–G–R. Instead, it requires that reliability be *explainable* via **assurance lanes** (B.3.3):

* **TA** (Typing assurance): semantic/type alignment sufficient for transport and composition.
* **VA** (Verification assurance): logical/algorithmic checking, proof, model checking, static guarantees.
* **LA** (Validation assurance): empirical adequacy under declared conditions, tests, benchmarks, telemetry.

Lane reporting is how KD-CAL supports the common research distinction between logical soundness and empirical adequacy **without introducing new global characteristics**.
Lanes remain **separable** in SCR/Notes; they are not averaged into a “single tradition score”.

#### C.2.2:4.7 - Scope operations are kind-safe (and use the ClaimScope algebra)

Reliability is meaningless if scope operations are applied to ill-typed entities.

**Well-formedness constraint WFC‑C2.2‑1 (Type before scope).**
Let `G1` and `G2` be claim scopes for claims about entities of kinds `K1` and `K2`. A scope operation that combines them—such as `G1 ∩ G2` for serial intersection or `SpanUnion({G_i})` for parallel coverage—is defined only if:

* `K1 = K2`; or
* an exact C.3/C.3.3 kind relation or cast makes the operation well typed for these participants and this direction.

An A.2.6 scope translation changes `G` only under its own rule. A kind relation does not translate scope. If distinct source-local meanings also matter, an actual F.9 Bridge and its bounded-use claim are separate; neither repairs an ill-typed scope operation.
This constraint prevents “type-by-scope” anti-patterns where scope manipulation is used to hide type mismatch.

#### C.2.2:4.8 - Minimal authoring recipe

A minimal, conforming KD‑CAL authoring flow for reliability is:

1. **Fix the typed claim.** State the claim as a typed proposition about an EntityOfConcern (Kind‑CAL, C.3).
2. **Declare claim scope.** Write `G` explicitly using A.2.6 operators; avoid scope-by-wording.
3. **Declare interpretation conditions.** State design or run stance, `ReferencePlane`, effective scheme, model-use basis, working situation, and `validationMode ∈ {postulate, inferential, axiomatic}` only where each changes this claim or its use. `G` already carries claim scope; do not add a generic Context identifier.
4. **Bind evidence.** Attach evidence stubs and lane tags (TA/VA/LA) and validity windows / decay policy where applicable (B.3.3, B.3.4).
5. **Identify support roles and dependence.** Distinguish required premises, sufficient alternatives, complementary support, scope slices, and counterevidence. Identify duplicated data, shared assumptions, and plausible common biases.
6. **Choose a justified calculation or a non-aggregate synthesis.** Name the receiving quantity, compatible scales, assumptions, and model before any numerical fold. Otherwise retain separate support and a reasoned bounded conclusion; do not substitute a universal min or max.
7. **Name actual relations on reuse.** Use A.2.6 for an applicable scope translation, C.3/C.3.3 for a kind relation, F.9 for a semantic relation between exact local-sense cells, and the direct pattern for notation, plane, model-use, or evidence reuse. Record the fit or loss declared by each traversed relation. If a required relation is absent or unresolved, stop that reuse; a generic cross-context Bridge cannot substitute for it.
8. **Return the usable result.** State F, G, and the supported conclusion with its warrant and limitations. Publish R numerically only under the justified receiving model, with the actual calculation and relied-on loss definitions. A formal conclusion does not require an empirical score. Inquiry or action choice, if needed, remains separate.


#### C.2.2:4.8.A - Authoring template: claim-local support summary

When publishing a path-specific R for a guard or decision, include enough of the support summary to identify its actual quantity, model, inputs, and use. G.6 PathId references can carry this information; no new Core type or mandatory table is introduced.

| PathId | Receiving claim and support | Quantity and model | R result | Fit and limitations | Lane tags | Validity |
| --- | --- | --- | --- | --- | --- | --- |
| P-1 | A ∩ B; the two bounds in §4.5 | Probability lower bound; union-bound argument for the stated events | ≥0.67, not a point estimate | No numerical penalty follows from a CL rank; both input bounds must apply to this same use | Applicable TA/VA/LA references | Intersection of the actual input-bound validity conditions |

Retain actual CL summaries where their relation uses them; any chain minimum needs that relation's ordinal meaning. Empirical time limits and the fixed theory version of a proof remain different conditions. If several paths are consumed, retain their distinct scopes and models and cite the actual PathId(s). A non-aggregate synthesis may instead give its separate contributions and limitations in ordinary prose.

