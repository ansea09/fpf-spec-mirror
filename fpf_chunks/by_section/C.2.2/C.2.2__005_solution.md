---
chunk_kind: "child"
pattern_id: "C.2.2"
pattern_title: "Reliability R in the F–G–R triad"
section_id: "C.2.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.2/C.2.2__005_solution.md"
commit_sha: "3f6714ae3235e0d771dce32835be7696f626d2ee"
heading_path:
  - "C.2.2 — Reliability R in the F–G–R triad"
  - "C.2.2:4 — Solution"
line_start: 42165
line_end: 42358
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
* `R_eff(c)` is Effective reliability for `c`, treated as a **ratio-scale** scalar in `[0,1]` (or an **ordinal proxy** at **[M‑0/M‑1]**; see §4.5.A).
  `R_eff` is computed **pathwise** (DEF‑C2.2‑3): when more than one admissible justification path exists, publish multiple path records (PathId rows) and cite which PathId(s) a guard/decision consumed (see §4.8.A / G.6). Any collapse to a single scalar is an explicitly declared Γ‑policy (no implicit averaging).

A location always concerns one exact claim. `G` carries its `U.ClaimScope`; any stance, reference plane, effective scheme, model-use basis, working situation, evidence basis, or validity window is stated separately when it changes interpretation or use:
* No generic `K` or Context value is part of epistemic-location identity; the exact subject-specific values above remain independently governed.
* `S ∈ {design, run}` is the claim’s stance carrier (no DesignRunTag chimeras).
* `ReferencePlane` is declared where applicable; plane crossings apply `CL^plane` and penalize **R only**.
* When the claim is published on the Working‑Model surface, the author also declares `validationMode ∈ {postulate, inferential, axiomatic}` (E.14 / B.3).

**Mode-to-lane hint (informative).** `validationMode` sets the *default expectation* for which assurance lane carries the initial support load (B.3.3 or B.3.5).
It does **not** add a new characteristic and does **not** change the meaning of `R`:
* `axiomatic` → VA-dominant (constructive grounding or proof carriers); if `ReferencePlane=world`, LA may still be required.
* `inferential` → VA+TA-dominant (reasoned chain + typing/alignment assurance); LA is optional and scope-bound.
* `postulate` → LA-dominant (empirical validation with freshness/decay); VA is optional.
In all modes, **R remains warrant**, not ontological truth; “proof ⇒ R=1 in the world” is a category error.

**Profile note (informative; fold compatibility).** Some profiles treat empirical `R` as N/A for strictly **axiomatic** lines and use a tagged proxy `R_proxy := F` (`line=formal`) for folding, as an explicit proxy rather than an implicit “F⇒R” rule (B.1.3).

`⟨F,G,R⟩` is an **assurance tuple**, not a `U.CharacteristicSpace`; do not draw “trajectories” in `⟨F,G,R⟩`.

#### C.2.2:4.2 - What Reliability R means in KD‑CAL

**Definition DEF‑C2.2‑2 (Reliability as warrant).**
`R` is a conservative, evidence-bound indicator of how strongly the claim "holds as stated" under its declared `U.ClaimScope` and the separately named evidence and use conditions. It is interpreted as *warrant strength*, not as truth.

**Prophylactic clarification.**

* A higher `R` means “the evidence and its relevance supports relying on this claim under this scope.”
* A higher `F` means “the claim’s form is amenable to higher-formality checking and wider reuse,” but does not itself imply the claim is warranted.
* A larger `G` means “the claim applies to more cases,” but does not itself imply the claim is warranted in those cases.

#### C.2.2:4.3 - Pathwise weakest-link propagation (series vs parallel)

KD‑CAL’s default Γ‑fold is **weakest‑link** on the *entailment spine* (the premises/lemmas actually needed), computed per justification path. It is conservative, monotone, and auditable.

**Definition DEF‑C2.2‑3 (Pathwise weakest-link fold).**
Let `P` be a justification path for claim `c`. Let `SpineClaims(P)` be the required supports on the entailment spine, and let `SpineRelations(P)` be the exact scope, kind, plane, notation, source-local, model-use, or evidence-reuse relations actually traversed on that spine.

Define the raw warrant of the path as:

`R_raw(P) = min_{i ∈ SpineClaims(P)} R_eff(i)`

and compute the effective warrant of the path by applying congruence penalties (see §4.5 for policy shape):

`R_eff(P) = Π(R_raw(P); Φ(CL_min(P)), Ψ(CL^k_min(P)), Φ_plane(CL^plane_min(P)))`

**Spine discipline.** The `min` is taken over the *entailment spine* only (no satellites, no “nice-to-have” citations).

This matches the KD‑CAL propagation rule (C.2:4.3) and the Trust & Assurance skeleton (B.3): weakest-link on the spine, penalize only by the worst (lowest) congruence encountered on the path (no averaging).

**Parallel support (optional, declared).**
If the same claim `c` has multiple **independent** justification paths `{P_j}` (OR‑style support), the default is:

`R_eff(c) = max_j R_eff(P_j)`

Independence is recorded as an explicit note (e.g., separate rigs/datasets/proof lines), per CC‑C.2.2‑10 and the KD‑CAL composition rule (C.2:4.3).
If the “multiple paths” actually cover **different** scope slices, do not use `max` to hide weaker slices; instead publish distinct `G_path` (SpanUnion‑style coverage) and keep per‑path `R_eff` traceable (A.2.6 / C.2:4.3).

**Conflict detection (no averaging).**
If the evidence graph supports both `p` and `¬p` with overlapping scope, do **not** average. Separate the claims by the exact source, scheme, scope, model use, situation, or evidence basis that distinguishes them, or mark the claim **provisional** with explicit conflict edges until resolved.

#### C.2.2:4.4 - Relation-specific congruence penalties route to R only

A reused claim may traverse more than one independently governed relation. Before calculating `R_eff`, state what actually changed and use the rule for that change. A.2.6 owns claim-scope operations; C.3/C.3.3 owns kind relations; F.9 owns a semantic Bridge between exact local-sense cells; notation, reference-plane, model-use, and evidence-reuse relations keep their own definitions. None is a universal crossing relation.

**Invariant INV-C2.2-1 (R-only penalty routing).** For each traversed relation `r` whose rule declares a congruence loss:

`F_out = F_in`
`G_out = translate(r, G_in)` only when `r` is an applicable A.2.6 scope translation; otherwise `G_out = G_in`
`R_out ≤ R_in`, with the exact penalty determined by `r` and the cited policy

A scope translation may narrow or re-express `G`; it never widens the claim silently. A change in formality is a new episteme or explicit ΔF move, not a transport penalty. A semantic Bridge changes neither kind nor scope by itself. A kind or plane relation supplies no semantic correspondence unless that separate relation also obtains. Evidence reuse changes warrant only through its own evidence-use or reliance claim.

There is no implicit crossing. If a reuse depends on a changed value and its required relation or operation is absent, unresolved, or outside its applicability, the reuse is non-conformant. This keeps guard macros simple: each path records the relations it actually traverses and routes their declared losses to `R`, while every other coordinate changes only under its own rule.

#### C.2.2:4.4.A - Worked micro-example: scope revision and evidence reuse

A materials-lab claim says:

> `c_lab:` "Adhesive X retains ≥85% tensile strength on Al6061 for 2 h at 120–150 °C."

Its declared scope is `G_lab := {substrate=Al6061, temp∈[120,150]°C, dwell≤2h, evidenceWindow=1y, rig=Calib-v3}`. A plant engineer proposes a narrower claim for Plant B. Two different moves are required.

1. **State the plant claim and its scope.** Under A.2.6 the engineer explicitly narrows the temperature interval to `[122,148]°C` because the plant calibration rule reports a ±2 °C bias. This changes `G`; it is not an F.9 semantic Bridge and is not inferred from the words "lab" and "plant".
2. **Judge reuse of the lab evidence.** The exact A.10 or B.3 evidence-use and reliance claim names the lab evidence, plant claim, calibration edition, validity window, and intended use. If that relation's declared fit is `CL=2` under policy `Φ_v1`, compute `R_eff := max(0, R_lab − Φ_v1(2))`. The penalty reduces warrant; it does not perform the scope edit.

If lab and plant use distinct local meanings for a material term, F.9 separately tests a Bridge between their exact F.17 cells. Its semantic loss is not the calibration correction or the evidence-reuse result. A further safety narrowing to `[125,145]°C` is another explicit A.2.6 ΔG− decision.

The example therefore preserves one simple rule: name each changed value and relation once, change `G` only through the scope rule, and reduce `R` only through the loss rule that actually applies.

#### C.2.2:4.5 - Effective reliability under transport (policy-defined, monotone, bounded)

When a claim is reused through declared relations, `R_eff` is computed by applying the penalties those relations assign to their congruence levels.

**Definition DEF‑C2.2‑4 (Effective reliability under transport).**
Let:

* `CL` be the congruence level declared by the applicable scope, semantic, notation, model-use, or evidence-reuse relation (B.3 and its direct subject pattern).
* `CL^k` be the congruence level of an applicable kind relation (C.3/C.3.3).
* `CL^plane` be the congruence level of an applicable reference-plane relation (B.3 / plane patterns).

Let `Φ`, `Ψ`, and `Φ_plane` be **policy-defined**, **monotone**, **bounded**, **table-backed** penalty policies applied on the relevant edges:
* `Φ(CL)` — penalty declared for the applicable scope, semantic, notation, model-use, or evidence-reuse relation.
* `Ψ(CL^k)` — penalty declared for an applicable kind relation.
* `Φ_plane(CL^plane)` — plane-crossing penalty when `ReferencePlane` differs.

**Important (direction of monotonicity).** Congruence ladders are “polarity up” (higher CL = better fit). Per **CC‑G0‑Φ** and the Trust & Assurance skeleton, penalty tables are monotone **decreasing** in their CL ladders (if `CL1 < CL2` then `Φ(CL1) ≥ Φ(CL2)`, analogously for `Ψ` and `Φ_plane`) and bounded so that `R_eff` remains within `[0,1]` after clipping. Penalty magnitudes are not required to lie in `[0,1]` (tables may exceed 1 to force `R_eff → 0` under the subtractive default); what matters is monotonicity, boundedness, and published policy identifiers.

Define:

`R_eff(P) = clip_0^1( Π(R_raw(P); Φ(CL_min(P)), Ψ(CL^k_min(P)), Φ_plane(CL^plane_min(P))) )`

where each `*_min(P)` is the **lowest** congruence level encountered on the entailment spine of `P` for that dimension (a bottleneck; no averages), and `clip_0^1(x)` truncates to `[0,1]`.

**Default (safe) instantiation (subtractive).**
When policies are expressed as subtractive penalties, a safe default is:

`R_eff(P) = max(0, R_raw(P) − Φ(CL_min(P)) − Ψ(CL^k_min(P)) − Φ_plane(CL^plane_min(P)) )`

This generalises the B.3 skeleton to multiple congruence ladders (scope vs kind vs plane) without introducing new penalty characteristics. If a dimension is not present on the path, its penalty term is treated as neutral (`0` in the subtractive default).

**Provisional marking.**
Default admissibility thresholds for reuse are set by the relevant relation-calibration profile (e.g., G.7). Typically, `CL=1` requires an explicit waiver to proceed and `CL=0` is inadmissible; this pattern only specifies that such thresholds gate reuse before any numeric penalty is meaningful.

#### C.2.2:4.5.A - Math-by-level gating (B.1.3:4.3)

* **[M‑0/M‑1]** allow **ordinal** comparisons only (no arithmetic on `R_eff`); Φ/Ψ/Φ_plane may be qualitative (“low/med/high”). Publish evidence links + lane tags.
* **[M‑2/L1]** numeric `R_eff` requires referencing numeric, table-backed policy identifiers for Φ/Ψ/Φ_plane (and Π if not default), plus reproducibility tags for empirical legs; otherwise treat the claim as [M‑1] semantics.

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

1. **Fix the typed claim.** State the claim as a typed proposition about a EntityOfConcern (Kind‑CAL, C.3).
2. **Declare claim scope.** Write `G` explicitly using A.2.6 operators; avoid scope-by-wording.
3. **Declare interpretation conditions.** State design or run stance, `ReferencePlane`, effective scheme, model-use basis, working situation, and `validationMode ∈ {postulate, inferential, axiomatic}` only where each changes this claim or its use. `G` already carries claim scope; do not add a generic Context identifier.
4. **Bind evidence.** Attach evidence stubs and lane tags (TA/VA/LA) and validity windows / decay policy where applicable (B.3.3, B.3.4).
5. **Choose Γ-mode.** Declare whether the support is **series** (required) or **parallel** (independent lines to the same claim).
6. **Compute R_raw.** Use the weakest-link fold on the entailment spine; for parallel support, use `max` only with an explicit independence note.
7. **Name actual relations on reuse.** Use A.2.6 for an applicable scope translation, C.3/C.3.3 for a kind relation, F.9 for a semantic relation between exact local-sense cells, and the direct pattern for notation, plane, model-use, or evidence reuse. Record the fit or loss declared by each traversed relation. If a required relation is absent or unresolved, stop that reuse; a generic cross-context Bridge cannot substitute for it.
8. **Compute R_eff.** Apply the declared penalty policies into `R` (never into `F` or `G`), and publish `⟨F,G,R_eff⟩` with traceable references and policy identifiers.

A reliable claim is not a loud claim; it is a claim that can be *carried*.

#### C.2.2:4.8.A - Authoring template: Path summary row (copy/paste)

When publishing `R_eff` for a claim, authors SHOULD include a compact, claim-local **path summary**. This is intentionally shaped so it can be turned into tooling later (EvidenceGraph/PathId in G.6) without introducing new Core types or face-kinds.

| PathId | Entailment spine (required supports) | CL_min | CL^k_min | CL^plane_min | Policy-id(s) (Φ / Ψ / Φ_plane) | R_raw | R_eff | Lane tags (TA/VA/LA) | valid_until |
| ------ | ----------------------------------- | ------ | -------- | ----------- | ------------------------------ | ----- | ----- | --------------------- | ---------- |
| P‑1    | `c ← {c_a, c_b, c_c}`               | 2      | 3        | —           | `Φ=Φ_v1`, `Ψ=Ψ_v2`             | 0.82  | 0.67  | {TA, LA}              | 2026‑09‑30 |

Notes:
* `CL_*_min` values are **bottlenecks** on the relevant path/dimension (no averaging).
* `valid_until` is the **earliest** expiry across empirical legs (or `—` / “fenced to TheoryVersion” for non-decaying proof legs).
* If you publish multiple admissible paths, include multiple rows and cite which PathId(s) your decision/guard consumed.

