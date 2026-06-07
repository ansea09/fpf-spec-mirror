---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "GateProfilization: OperationalGate(profile) (GateFit core)"
section_id: "A.21:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__005_solution.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "A.21 — GateProfilization: OperationalGate(profile) (GateFit core)"
  - "A.21:4 — Solution"
line_start: 28082
line_end: 28270
dependencies:
  - "A.19"
  - "A.2.6"
  - "A.20"
  - "A.7"
  - "C.18"
  - "C.19"
  - "E.17"
  - "E.18"
  - "E.TGA"
  - "F.17"
  - "F.9"
  - "G.0"
  - "G.11"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
  - "CV⇒GF"
  - "DecisionLog"
  - "EquivalenceWitness"
  - "GateChecks"
  - "GateDecision"
  - "GateFit"
  - "GateProfile"
  - "LaunchGate"
  - "OperationalGate"
  - "join-semilattice"
---

### A.21:4 - Solution

#### A.21:4.1 - Gate = microkernel of checks

> **Note (guards are not GateChecks).** `USM.CompareGuard` and `USM.LaunchGuard` are **not** `GateCheckKind`s; they may emit `GuardFail` events which are aggregated by the gate referenced by the existing aggregation-assignment field `GuardOwnerGateId` under the active profile (`degrade|block`) and recorded in `DecisionLog`. Guard vocabulary is received through `A.2.6`; gate aggregation remains here.
`OperationalGate(profile)` is treated as a microkernel: checks are **pluggable** `GateCheck`s; the gate core **aggregates** their outputs **conceptually**, without procedural semantics and without mutating the transduction graph.

#### A.21:4.2 - Publication lexemes and register discipline

**Per-check reference lexeme.**
`GateCheckRef := { aspect, kind, edition, scope }`, where:
* `aspect ∈ {ConstraintValidity, GateFit}`,
* `scope ∈ {lane|locus|subflow|profile}`.

**Short-form shorthand (not publication-valid).**
If a local short form `{ kind, edition, scope }` appears in prose, it is interpreted only as a projection of the normative record with `aspect` supplied explicitly at the point of publication. Any published face or `DecisionLog` entry MUST use the full `GateCheckRef` with `aspect`.

**Decision terminology separation.**

* `GateDecision` is the published lattice value.
* `GateDecisionRationale` is the minimal structured support of that decision (check outcomes, folds, witness refs).
* `GateDecisionExplanation` is optional, human-readable, derived from the rationale; it **does not carry decision status** and MUST NOT be used as one.

**Register discipline.** Tech labels are ASCII and twin-labeled where the plain form uses symbolic notation.
(Example: use `CLPlane` / “CL^plane”, `CLKind` / “CL^k”, `UNM.TransportRegistryPhi` / “UNM.TransportRegistryΦ”, `GammaTimeRule` / “Γ_timeRule”.)

#### A.21:4.3 - CV⇒GF activation predicate (counterfactual boundary)

GateFit checks are *defined* as inactive unless `CV.Status=pass`:
* Let `CV.Status` be the join-aggregate of all `GateCheckRef` with `aspect=ConstraintValidity`.
* For any `GateCheckRef` with `aspect=GateFit`:
  **If `CV.Status ≠ pass`, the GateFit check outcome is `abstain`.**
* While `CV.Status ≠ pass` **(or the active profile suppresses narratives)**, any GateFit-oriented `GateDecisionExplanation` **does not apply**.

This keeps the boundary crisp: CV explains internal validity; GF explains profile-fit **only in the counterfactual world where `CV.Status=pass` holds**.

**LaunchGate pre‑run barrier (work‑boundary special case).**

For the unique `LaunchGate` at the entry of each `U.Work`/`U.WorkEnactment`, let `Prev.CV.Status` denote the aggregate over the declared ingress predecessor set or ingress cut-set for the addressed `PathSlice`. In a linear path this may be one predecessor; where graph or fan-in semantics are live, it is not reduced to one immediately preceding step.

* If `Prev.CV.Status ≠ pass`, then (i) all GateFit-scoped LaunchGate checks return `abstain` by activation, and (ii) the **overall LaunchGate** decision is forced to `block` (pre‑run barrier). The rationale MUST record the predecessor CV status and the forced-block rule in `DecisionLog`.

This is a publication-safety invariant: it constrains what may be admitted at the work boundary without specifying evaluation order or execution scheduling. Actual launch values and work occurrences remain governed by `A.15`.

#### A.21:4.4 - Decision algebra: join-semilattice (“worst wins”)

A.21 adopts order-independent aggregation, not a universal policy language or a one-size-fits-all safety rule. The gate core does not define the domain truth of checks; it aggregates declared check outcomes under the active profile.

**Decision domain.** `GateDecision ∈ {abstain, pass, degrade, block}`.

**Aggregation rule.** Aggregation over all applicable checks is the **idempotent, commutative, associative join** on
`GateDecision` values `abstain <= pass <= degrade <= block`, with **neutral = `abstain`** and **absorbing = `block`**.

Publications carry only:

1. the aggregated `GateDecision`, and
2. its `GateDecisionRationale` recorded in the `DecisionLog`.

#### A.21:4.5 - Profile-bound folds for `error|timeout|unknown`
A check may encounter `error`, `timeout`, or evidence-scoped `unknown`. These do **not** become new decision values; they are folded into the decision lattice **by profile and check policy**.
**Normative minimum folds (tri-state).**

> **Naming note.** Some conformance tables use **Lean** as a label for the `GateProfile=Lite` gating posture. Treat this as an alias only, and do not confuse it with `PublishMode=Lite` (a publication-face reduction mode).

| Active `GateProfile` | `error` fold | `timeout` fold | `unknown` fold (evidence-scoped) |
| -------------------- | -----------: | -------------: | ------------------------------: |
| `Lite`               |    `degrade` |      `degrade` | per `GateCheck` policy (`abstain` or `degrade`) |
| `Core`               |    `degrade` |      `degrade` | per `GateCheck` policy (`abstain` or `degrade`) |
| `SafetyCritical`     |      `block` |        `block` | per `GateCheck` policy (safety-default: `degrade`) |
| `RegulatedX`         |      `block` |        `block` | per `GateCheck` policy (safety-default: `degrade`); X identity and edition are recorded in `DecisionLog` |

Where a `GateCheck` declares an evidence-scoped `unknown` strategy, that strategy is part of the check’s intensional definition; the fold applied and its justification are recorded in `DecisionLog`.

#### A.21:4.6 - GateProfiles: current binding and minimum profile semantics

A.21 binds the following *functional role* of `GateProfile`:

> **Terminology (avoid `Lite`/`Lean` confusion).** `GateProfile=Lite|Core|SafetyCritical|RegulatedX` is the **gating posture** that determines the effective GateCheck set and fold policies. `PublishMode=Lite` is a **publication-face reduction mode** (AssuranceLane‑Lite / TechCard‑Lite) and MUST NOT be interpreted as a reduced-obligation `GateProfile`.

* A `GateProfile` is an attribute of a **branch or `PathSlice`**; the default is `Core`.
* Local overrides may change the active profile for the current GateCrossing and its subordinate scope **but cannot reduce** the already-effective set of `GateCheckKind`s; only additions are allowed. Weakening SHALL use a new `PathSlice` via sentinel.
* `PublishMode=Lite` changes *face reduction only* and does **not** weaken the check set or aggregation rule.

#### A.21:4.7 - Scope and merge semantics (`lane|locus|subflow|profile`)

* Each `GateCheckRef` declares its scope; `subflow` scope is bounded by a sentinel bridge (restart / refresh boundary).
* The effective check set is formed by **union across all declared scopes**; duplicates by `kind` merge by the same join rule (“worst wins”), and **all rationales are preserved** in `DecisionLog`.
  * For `RegulatedConformance(X)`, the identity of **X** and its rule/edition reference are part of the rationale record; multiple `RegulatedConformance(X{…})` may coexist in one gate.
* A check outside its scope reports `abstain`.

#### A.21:4.8 - Publication repeatability, caching, and re-aggregation triggers
**Repeatability (publication).** Gate decisions MUST be replayable from declared pins/refs: no implicit “latest/now”. Any time basis is made explicit via `Γ_time` (or a `Γ_timeRule` that resolves to a concrete basis), and the resolved basis is recorded in `DecisionLog`.

**Caching constraint (publication).** A gate decision may be cached **only** per
`{PathSliceId, GateProfile, GateChecks.editions, editions{…}}`, where `GateChecks.editions` denotes the canonicalized, order-independent listing of the **effective** `GateCheckRef{aspect,kind,edition,scope}` (including their `edition`s) for this gate instance. Cache reuse is valid only while the declared freshness/evidence window remains valid under the active profile.

**Re-aggregation triggers (non-exhaustive, normative).** Re-aggregation is required if any of the following changes (slice-local; no execution method implied):

* any component of `editions{…}` changes (any `edition_key ↦ EditionId` bump),
* any `GateCheckRef.edition` changes (including regulator X editions for `RegulatedConformance(X)`),
* the declared `Γ_time` basis changes or resolves differently,
* a relevant `FreshnessTicket` expires/changes or TOCTOU window constraints change,
* a sentinel-bounded `subflow` refresh adds an SCR/RSCR carrier to the `DecisionLog` rationale-anchor set,

* any input breaks the declared `A.21` equivalence witness.

Decision stability is under the `A.21` equivalence relation; a witness is recorded on the `DecisionLog` (see §4.10). A.21 constrains equivalence + invalidation conditions but does not fix key formats.

#### A.21:4.9 - MVPK faces for `OperationalGate(profile)` (minimum pins)

The gate publishes faces to record **what is declared**, not “how it executes”. Faces remain **pins + refs** (no new numeric claims; no I/O re-listing).

**Minimum pins (PlainView / TechCard / AssuranceLane where applicable).**

* View scope: `PublicationScopeId` (with MVPK profile: `Min|Lite|SetReady|Max`)
* Identity: `GateId`, `BridgeId`, `PathId`, `PathSliceId`
* Temporal: `DesignRunTagFrom`, `DesignRunTagTo`
* Profile: `GateProfile` (`PublishMode` changes only face reduction)

* Checks: list of `GateCheckRef` (`aspect`, `kind`, `edition`, `scope`)
* CV: aggregated `ConstraintValidityStatus` and optional `ConstraintValidityWitnessRef` (refs only)
* Editions: `editions{…}` vector + `EditionPins{CGSpec, ComparatorSet, UNM.TransportRegistryPhi}`
  * **Gate-requirement on edition refs.** Any face that cites `CGSpec`, `ComparatorSet`, or `UNM.TransportRegistryPhi` editions also includes `BridgeCard + UTS row` through `F.9`, `F.17`, `E.17`, and `E.18`; otherwise downstream consumption is non-conformant.
* ReferencePlane and CL: source `ReferencePlane` pins and target `ReferencePlane` pins; `CLPlane` / “CL^plane” (for non-crossings `CL^plane = none` is allowed, but pins are still explicit); any Φ penalties are published as rule refs and appear in the **R-channel only**
* Freshness: declared `GammaTime` / “Γ_time” pin and presence/absence of `FreshnessTicket` (refs)
* Evidence: SCR/RSCR carrier anchors (refs) + VALATA (VA/LA/TA) presence on AssuranceLane
* Guards: `USM.CompareGuard` / `USM.LaunchGuard` applicability pins (presence-only; GuardFail uses the `A.2.6` guard vocabulary and is aggregated here by the gate referenced by the existing aggregation-assignment field `GuardOwnerGateId`)
* Decision: aggregated `GateDecision` and `DecisionLogRef`

**Lean face (PublishMode=Lite).** It MAY fold to `GateProfile / GateChecks / EditionPins / GateDecision + DecisionLogRef`, but:

* it MUST keep `GateProfile` and `DecisionLogRef`,
* it MUST not weaken GateChecks or the aggregation algebra, and
* if `EditionPins` are present, it still includes `BridgeCard + UTS row` through `F.9`, `F.17`, `E.17`, and `E.18` and preserves the crossing boundaries (explicit `ReferencePlane`, `CLPlane`, and Φ -> R-channel only).

#### A.21:4.10 - DecisionLog (minimum composition)

`DecisionLog` is an append-only record of reasons and references:

* gate identity + `PathSliceId` (+ `PublicationScopeId` when the log is published via a face bundle)
* each `GateCheckKind`, its `GateCheckRef.edition`, and its folded outcome (`pass|degrade|block|abstain`) including the applied `error|timeout|unknown` fold
* rule anchors / evidence anchors (SCR/RSCR carriers + VALATA bindings); SquareLaw mismatched pins appear only when the crossing check is live

* policy-id dependencies used by checks (as `PolicyIdRef` bundles per F.8:8.1); `Φ(CL)`, `Φ_plane`, and `Ψ(CL^k)` appear only when bridge or crossing is live, while gate-local policy ids appear only when consulted by the active profile

* `GuardFail` events only when guard events exist; if present, they are received from `USM.Guards` and aggregated by the gate referenced by the existing aggregation-assignment field `GuardOwnerGateId` with the applied profile rule (`degrade|block`)

* `EquivalenceWitness` (or `EquivalenceWitnessRef`) as an `A.21` publication item, minimally: `{ keys, E⃗, Γ_time(basis), PathSliceId?, ReturnShapeClass, ComparatorSetRef?, profile }`; use `G.6` or `G.11` where evidence-path visibility or refresh implications are live
* the declared publish reaction for `degrade|block` only when that outcome has a declared publication consequence, including any local “degrade mode” notes when permitted by profile

* for `RegulatedConformance(X)`, only when `RegulatedConformance(X)` is active: the identity of X and the rule/edition references used

#### A.21:4.11 - GateChecks admissibility (GateFit-only catalog boundary)

**Mandatory on LaunchGate.** `FreshnessUpToDate`, `DesignRunTagConsistency`.
**Allowed GateFit checks (non-exhaustive, normative minima).**

* `DesignRunTagConsistency` (mandatory on LaunchGate; may appear elsewhere)
* `FreshnessUpToDate` (mandatory on LaunchGate; may appear elsewhere)
* `ReferencePlaneCrossing`
* `ComparatorConstraintRules (CSLC)`
* `EvidenceCompleteness`
* `SafetyEnvelope`
* `RegulatedConformance(X)` (X identity plus edition and rule refs are recorded in `DecisionLog`)
* `Role/ChannelFit` (roles are Kernel `U.Role` tokens, not alias strings)
* `EquivalencePreservation`
* `OutflowAudit`
* `SnapshotConsistency`

**Receiving-pattern truth examples (informative).** A.21 names and aggregates the check; it does not decide the domain truth condition. `EvidenceCompleteness` returns to `A.10`, `G.6`, or `B.3`; `Role/ChannelFit` returns to `A.2`, `A.15`, or `A.2.6`; `ReferencePlaneCrossing` returns to `E.18`, `F.9`, `F.17`, and UNM; `ComparatorConstraintRules` returns to `A.19`, `G.0`, `G.5`, `C.18`, `C.19`, `G.9`, or `G.11` where comparator, archive, parity, set-return, or refresh claims are live; `SafetyEnvelope` and `RegulatedConformance(X)` return to the safety or regulatory pattern that governs the envelope or rule.

**Forbidden (hard boundary).**

* Modeling CV classes “as GateFit” (CV classes remain CV; GF remains GF).
* Any “LEX gate checks” or lexical pseudo-checking (lexical views do not participate in decisions).

#### A.21:4.12 - SquareLaw compatibility at crossings
For every GateCrossing, the SquareLaw constraint SHALL hold:
`gate_out ∘ transfer = transfer' ∘ gate_in`.

Profile selection/inheritance does not weaken this requirement; inconsistency yields `block|degrade` within the active profile and is recorded in the DecisionLog. LaunchGate is a work-boundary GateCrossing case, so SquareLaw is mandatory there as well.

#### A.21:4.13 - Lexical mediation (optional trace, non-decisional)

A gate MAY publish a `LexicalResolutionRef` / `LexicalView` for traceability of alias resolution, but:

* it does **not** participate in aggregation, and
* it is not a `GateCheck` input and cannot change `GateDecision`.

