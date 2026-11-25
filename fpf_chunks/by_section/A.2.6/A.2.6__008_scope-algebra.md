---
chunk_kind: "child"
pattern_id: "A.2.6"
pattern_title: "Unified Scope Mechanism (USM): Test Scope Membership and Combine Scopes"
section_id: "A.2.6:7"
section_title: "Scope Algebra"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.6/A.2.6__008_scope-algebra.md"
commit_sha: "423f9d3fef92bafec7b092b910e8ce056a0f607d"
heading_path:
  - "A.2.6 — Unified Scope Mechanism (USM): Test Scope Membership and Combine Scopes"
  - "A.2.6:7 — Scope Algebra"
line_start: 7355
line_end: 7458
dependencies:
  - "A.1.1"
  - "A.15.1"
  - "A.2.2"
  - "A.22"
  - "A.6.0"
  - "A.6.1"
  - "A.7"
  - "C.2.1"
  - "C.2.2"
  - "C.2.3"
  - "C.29"
  - "C.3"
  - "E.24.UK"
  - "F.9"
keywords:
  - "alone"
---

### A.2.6:7 - Scope Algebra

#### A.2.6:7.1 - Membership and coverage

For exact slice `x` and scope `S`, evaluate `member(x, S)`.

* `true`: the slice is included and the scope condition for the attempted use passes;
* `false`: the slice is excluded and that use stops or selects another scope;
* `unknown`: the available evaluation cannot decide; the guard abstains or follows an explicitly governed reliance policy without asserting exclusion.

For a finite target set `T : ContextSliceSet`, `coversSet(S,T)` abbreviates `for every x in T, member(x,S)`. Scope-to-scope `scopeSubset(S1,S2)` instead means `for every x, member(x,S1) implies member(x,S2)`. A target set is neither a scope nor a substitute for one. There is no “close enough” membership and no implicit widening.

Membership evaluation work, its inputs and A.6.1 bindings, an optional C.2.1 result episteme, and a C.29 table remain neighboring objects.

#### A.2.6:7.2 - Serial Composition (Intersection)

**Rule S‑INT (serial).** Identify the original slice and what the chain must deliver. When each essential condition `Ci` is already expressed on that same slice, all must hold there. The scope defined by these conditions is

```
Scope_serial = ⋂_{i=1..k} Scope(Ci)
```

When a stage takes the preceding stage’s output as its input, trace the reachable intermediate outcomes for the original slice. To establish conditional compatibility, show that the downstream stage can use the outputs covered by the claim. To establish feasibility, show that an allowed execution can reach the promised result. To guarantee delivery, justify a way of operating the whole chain that the responsible participants can follow with their authority and the information available at each choice. Under that way of operating, every history allowed by the stated conditions must reach the required result, by the deadline if there is one. Include admissible waits, failures and retries. A chain can produce compatible data whenever it finishes and still fail to finish on time. If the order and choices are prescribed, test that order directly. An empty input scope supplies no slice for using the chain.

**Monotonicity.** Adding a necessary condition to the same chain and expressing it on the same original slices can only narrow the scope or leave it unchanged. Inserting a stage that transforms an intermediate result changes the chain. Recompute which original slices can now reach the promised result and under what conditions. A converter may admit an input that the original chain could not handle.

#### A.2.6:7.3 - Parallel Support (SpanUnion)

To establish where the same claim holds, find the slices on which each argument warrants it. The claim holds throughout the union of those supported areas because each included slice is covered by at least one argument. If two cases depend on one calibration, that premise must be justified everywhere the proof uses it. Retain that dependency when the calibration is challenged. Different areas of application do not by themselves give independent evidence for an overlapping case.

**Rule P‑UNION (parallel).** To claim independently supported areas for the **same** claim or capability, establish the required independence of lines `L₁,…,Lₙ` in addition to their respective scopes `S_i`. The publisher may then declare

```
Scope_published = SpanUnion({S_i})  =  ⋃_{i=1..n} S_i
```

**Constraints.**

* Independence MUST be justified (different support lines must not rely on the same weakest link).
* The union MUST NOT exceed the union of supported slices.
* Publishers SHOULD annotate coverage density/heterogeneity (informative) to aid R assessment, but numeric “coverage” is not part of G.
* **Independence criterion.** Support lines in a **SpanUnion** MUST be partitioned so that each line has a set of **essential components** disjoint from the others’ essential components (no shared weakest link). The partition (or a certificate thereof) SHALL be referenced in the publication.

#### A.2.6:7.4 - Set-valued scope and scalar reporting

**1) G is not an ordinal scale; it is set-valued.**
Under **USM**, `U.ClaimScope` is a **set‑valued** **USM scope object** over `U.ContextSlice`. The only well‑typed primitives are **membership** and **set operations** (`⊆`, `∩`, `⋃`). Imposing ordinal “levels” such as **G0…Gk** violates the type discipline and produces non‑invariant behavior (the **same set** could be “rated” with different numbers under different heuristics). (See also LEX‑CHR‑STRICT.)

**2) G is a set of slices.**
USM already fixes composition: intersect requirements on common slices, including conditions traced back through intermediate outcomes. Coverage by cases requires grounds throughout the covered areas. Across independently supported lines the publisher may use **SpanUnion**. None of these operations relies on (or preserves) any linear order. An ordinal “G ladder” invites people to take **minimums/averages**, which is **incorrect** for sets and breaks the established algebra.

**3) Identify what an abstraction level compares.**
C.3.5's optional `KindAT` facet describes how a particular kind is intended to be used. Its anchors run from instance-oriented use, such as cataloguing a particular cohort, to treating structures up to isomorphism. To compare the levels of abstraction or refinement of two models, use B.5.MR. To establish where an assertion holds, identify the context slices in its `U.ClaimScope (G)`. These judgements can change independently.

**4) A G ladder breaks locality and Bridge semantics.**
When exact local senses require translation, an obtaining F.9 Bridge establishes their direct semantic relation while a separate C.2.1 claim states the proposed mapping rule and tolerated loss. There is no canonical way to translate an ordinal G level: the mapped area may be narrower or differently factored. USM translates exact sets only through that bounded claim and keeps A.10 or B.3 reliance separate rather than rewriting G.

**5) A G ladder duplicates ESG guards without adding decision power.**
Expression quality and scope coverage answer different questions. C.2.3 governs expression properties. Explicit guards determine scope coverage, include `gammaTime` only when membership varies with time, and check freshness separately when current. A reported G number cannot replace those predicates.

**Normative directive.**
`U.ClaimScope (G)` **SHALL** remain a **set‑valued USM scope object**; **no ordinal or numeric ladder SHALL be defined** for G. If a profile needs scalar reporting, it MAY publish an explicit **report‑only** proxy **`CoverageMetric(G)`**, but **`CoverageMetric(G)` MUST NOT substitute for `G`** in norms, gates, Bridge semantics, bounded-use claims, or reliance decisions. Authoring and gating **SHOULD** use **required expression properties or justified local formality thresholds** (C.2.3) and **explicit guard predicates** (A.2.6) rather than pseudo‑levels of G.

#### A.2.6:7.5 - Translation across exact local senses

Use translation only when ordinary designation resolution cannot settle the exact local senses needed by the target membership predicate. Then proceed in this order:

1. resolve the source and receiving F.17 `SchemeSenseCell` values and name the exact obtaining F.9 Bridge that relates them;
2. state the proposed scope translation separately: name the source scope, target scheme, source-to-receiving direction, scope-correspondence rule, and tolerated loss, then cite the exact current C.2.1 claim with that Bridge as EntityOfConcern and affirmative polarity for this use;
3. before a guard relies on the claim, require the exact A.10 evidence-provenance relation for this bounded use; ordinary reliance requires `RelianceDisposition=pass`; when an actual named assurance claim is current, require its B.3 `AssuranceResult` for that same use with `disposition=supported-for-use`; and
4. use `translate(Bridge, UseClaim, SourceScope, TargetReferenceScheme)` as the C.29 mathematical representation, or invoke `deriveTranslatedScope` with those same four values when one actual calculation and returned scope are needed.

The Bridge establishes the direct semantic correspondence. The separate claim selects this translation's direction, rule, and tolerance. A Bridge profile, Bridge Card, reference-scheme difference, project label, or slice designator cannot supply that claim or its reliance basis. A missing or non-obtaining Bridge blocks the semantic branch. A missing or non-affirmative use claim blocks reliance. A non-passing A.10 disposition blocks ordinary reliance; when an actual named assurance claim is current, a B.3 result other than `supported-for-use` stops or narrows the assurance-bearing use. None of these outcomes makes an otherwise obtaining Bridge false.

An A.10 `pass`, or a B.3 `AssuranceResult` with `disposition=supported-for-use`, supports only the named use; neither authorizes it. A direct domain rule may require an assurance claim, but it must be stated separately.

Observed mismatch, calibration error, and counterexamples are evidence about the use claim. The permitted loss is the tolerance inside that claim. If the rule and tolerance permit translation only for part of the source scope, identify that part and return its target image. Neither the Bridge nor the claim supplies direct support for adding a slice, and neither makes membership true. The exact `deriveTranslatedScope` application remains an A.6.1 operation application; the claim and reliance basis do not prove that it occurred.

#### A.2.6:7.6 - Δ‑Operations (Widen, Narrow, Refit)

* **Δ‑G+ (widen).** Monotone expansion: `S proper-subset S-prime`. Every added slice requires direct support under the receiving use; a Bridge and affirmative translation-use claim can define a mapping but supply no such support by themselves.
* **ΔG− (narrow).** Monotone restriction: `S′ ⊂ S`. Often used to remove areas invalidated by new findings.
* **Refit.** A different expression or parameterization designates the same extensional scope after normalization (for example, changing units or factoring common predicates). Refit MUST NOT alter membership and does not create another scope value.

**Refit (normalization).** A refit **MUST preserve membership** exactly: `extension_RS(S_after) = extension_RS(S_before)`, so both expressions designate the same scope value. Any change that alters boundary inclusion through rounding, unit conversion, or discretization is a ΔG± change, not a refit.

**Edition triggers.** A changed extension identifies a different scope value. A changed predicate expression with the same exact extension preserves the scope value but is a content change in the declaration or claim-bearing episteme that carries the expression; its direct governor decides whether another episteme edition is needed.

**Discriminating cases.** Under one effective reference scheme, `20 °C <= temperature <= 30 °C` and the exactly converted `293.15 K <= temperature <= 303.15 K` have the same extension and can be related as a refit while designating the same scope. Replacing the inclusive upper boundary with `temperature < 30 °C` removes every slice exactly at `30 °C`; that one membership-boundary change identifies another scope rather than a refit.

#### A.2.6:7.7 - Invariants

* **I-LOCAL.** Interpret membership under the effective reference scheme and exact local senses current to the declaration. Translate only through an obtaining F.9 Bridge plus the separate affirmative C.2.1 claim for that translation; keep A.10 or B.3 reliance outside membership truth.
* **I‑SERIAL.** Intersect essential conditions expressed on the original slice. Adding a necessary condition to a fixed chain can only preserve or narrow its scope.
* **I‑PARALLEL.** A claim supported throughout each of several cases holds throughout their union under the premises used. The additional `SpanUnion` claim requires the independence established in §7.3.
* **I‑WLNK.** **F** describes the required expression properties of the essential constituents and their connecting inferences under C.2:4.3 and C.2.3:15.1. The composition must preserve those properties; a minimum applies only under a justified rule on a shared local ordered scale. **R** follows the justified support-composition model or non-aggregate synthesis under C.2.2:4.3 and B.3:4.4; dependency paths alone supply no default minimum. **G** follows the set rules in A.2.6:7.2 and A.2.6:7.3.
* **I‑IDS.** Idempotence: Intersecting or unioning a set with itself does not change it.
* **I‑EMPTY.** Empty scope is a first‑class value; guards MUST treat it as “not applicable”.

#### A.2.6:7.8 - Empty & Partial Scopes

* **Empty scope (`∅`).** No slice satisfies the declared predicate. A receiving guard stops.
* **Partial scope.** Publishers SHOULD avoid “global” language when actual scope is thin; instead, publish explicit slices and (informatively) coverage hints to guide R assessment.

