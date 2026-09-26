---
chunk_kind: "child"
pattern_id: "A.19.USCM"
pattern_title: "Unified Scoring Mechanism, USCM"
section_id: "A.19.USCM:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.USCM/A.19.USCM__006_solution.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "A.19.USCM — Unified Scoring Mechanism, USCM"
  - "A.19.USCM:4 — Solution"
line_start: 35451
line_end: 35573
dependencies:
keywords:
  - "CG-Spec.MinimalEvidence"
  - "CSLC-lawful transforms"
  - "ScaleComplianceProfile (SCP)"
  - "ScoringMethodDescription"
  - "score profile"
  - "scoring"
  - "tri-state admissibility (pass"
---

### A.19.USCM:4 - Solution

USCM is the **canonical scoring mechanism** in the CHR suite. It defines:

* a stable **mechanism boundary** (`score` is its own stage with a canonical `Score` operation and a tri‑state eligibility predicate),
* a stable **SlotKind surface** (via the suite lexicon),
* an admissibility‑first **LawSet** anchored in `CG‑Spec.SCP` and CSLC,
* an explicit **anti‑smuggling rule** (no implicit normalization), and
* an **audit minimum** (the evaluated bearer and input profile, exact editions, criteria, scope and window, comparison basis, evidence used, effective evidence policy, result use, and any relation actually used).

USCM preserves the suite obligations by construction: it does not embed GateDecision/GateLog, it does not perform publish/telemetry steps, and it cites relation pins only when the score or its receiving use actually depends on an obtaining relation; supported loss stays in `R_eff`.

Method semantics (“how to score”) remain out of suite core: they belong in SoTA packs (`G.2`) and wiring‑only extension modules (`GPatternExtension` blocks), while USCM remains the stable conceptual mechanism boundary.

#### A.19.USCM:4.1 - Operation declaration

`USCM.IntensionRef` cites the exact A.6.1 U.Mechanism declaration episteme here. The CHR score stage resolves to its local Score operation. Selecting a changed argument, scoring law or guard requires selecting that changed declaration explicitly; another realizer of the same declaration changes no suite member.

* **Scope note:** A.6.1 governs the operation and its actual argument/result bindings below. The planned baseline selects method and specification editions; independently declared receiving positions may use A.15.3 typed filling. Score returns a score profile, while eligibility and Audit retain their own meanings. GateDecision/GateLog remain outside this declaration.

* **IntensionHeader:** `id = USCM`, `version = 1.0.0`, `status = stable`.

* **IntensionRef:** `USCM.IntensionRef` (canonical target for the suite member named in `A.19.CHR:4.2`).

* **SignatureManifest (optional; importability):** if a USCM publication is intended to be imported/reused, it SHOULD publish a `SignatureManifest` (A.6.0:4.5 and A.6.1; A.6.0 checklist item 10 with `SM-1` through `SM-4`) consistent with `IntensionHeader`/`Imports`, explicitly exposing the stable SlotKind surface (including `ScoringMethodDescriptionSlot`) and any declared scalarization commitment.

* **Tell.** **SCP‑first** scoring: produce score measures from admitted profiles without violating CSLC / scale lawfulness.

* **Purpose:** **SCP‑first** scoring: produce score measures from admitted profiles without violating CSLC / scale lawfulness.

* **Imports:** `G.0 (CG‑Spec.SCP, CG‑Spec.MinimalEvidence)`, `A.18 (CSLC)`, `C.16 (measurement constitution and scale-lawful operations when measurement is claimed)`, `A.19.CN (comparability.mode + normalization routing)`, `A.19.CHR:4.2.1 (CHR SlotKind Lexicon)`.

* **SubjectBlock:**

  * **SubjectKind:** `U.Measure`, supplied by the measures in InputProfileSlot; each measure retains its bearer, Characteristic and Scale.
  * **RangedValueKind:** `U.Measure`; Score transforms the admitted profile under the selected method, and ScoreEligibility assesses that proposed transformation.
  * **SliceBasis:** the declared `U.ClaimScope` and selected `U.ContextSlice` members, together with the qualification window and intended result use.
  * **Input qualification:** scoring ranges over the admitted indicator or NCV profile for the exact evaluated bearer, criteria, claim scope and selected slices, qualification window, comparison or reference basis, and intended result use; `CN-Spec.comparability` routes comparison and `CG-Spec.SCP` gates admissibility.
  * Results are declared per operation: the score-measure profile and the eligibility judgment.

**Operation-local argument and result declarations**

Each input meaning is declared separately for Score and ScoreEligibility. ByRef inputs resolve to the stated exact value and edition. Cardinalities shown are for Score. ScoreEligibility may assess an incomplete proposal: each required input then has cardinality 0..1, and an absent value has no binding and triggers the corresponding missing-input rule.

| Direction | Local designator | Meaning and ValueKind | Designation; cardinality |
| --- | --- | --- | --- |
| Argument | InputProfileSlot | Admitted set of U.Measure values to score; each UINDM-derived value retains its exact basis position, Characteristic and Scale | ByValue; 1 profile |
| Argument | CNSpecSlot | CN-Spec used for the bearer, basis, scope/slices, qualification window, intended use and comparability routing | CNSpecRef; 1 |
| Argument | CGSpecSlot | CG-Spec supplying the SCP restrictions and default evidence requirement for this scoring use | CGSpecRef; 1 |
| Argument | ScoringMethodDescriptionSlot | ScoringMethodDescription supplying the selected Coordinate→Score rule, domain, codomain, Scale, polarity and use-required properties | ScoringMethodDescriptionRef; 1 |
| Argument | MinimalEvidenceSlot | MinimalEvidence override used in place of CGSpecSlot.MinimalEvidence | MinimalEvidenceRef; 0..1 |
| Score result | ScoreProfileSlot | Set of U.Measure values actually returned by the declared scoring rule | ByValue; 1 profile on completed admitted scoring, 0 on abstain or termination without a result |
| ScoreEligibility result | GuardDecision | Eligibility judgment under the predicates below: pass, degrade or abstain | ByValue; 1 on completed evaluation |

An argument's **bindingPredicate** holds when this Score or ScoreEligibility application actually uses the resolved value for that row's purpose: the profile supplies the operands, the method supplies the transformation, CN-Spec delimits its use and routing, and CG-Spec plus any override supplies its admission and evidence conditions. Mere inclusion in an Audit record is insufficient. The ScoreProfileSlot **bindingPredicate** holds when that Score application returns the profile obtained by applying the bound method lawfully to those operands, with the declared scalar/vector cardinality. The guard's result binding holds when that ScoreEligibility application returns its evaluated judgment. Each binding follows A.6.1 identity and continuous extent within the application; the result begins to bind at return.

**SlotIndex (derived projection).** Project this table's local designators, ValueKinds, designation modes and cardinalities. Its historical Slot names permit CHR lookup and introduce no separate meanings; A.6.5 relation SlotSpecs do not govern these operation positions. A repeated Characteristic name alone cannot select a profile value whose basis position and Scale matter.

* **OperationAlgebra** (suite stage = `score`, per `A.19.CHR:4.5`; canonical stage‑op = `Score`):

  * `Score(InputProfileSlot, CNSpecSlot, CGSpecSlot, ScoringMethodDescriptionSlot, MinimalEvidenceSlot?) → ScoreProfileSlot`; the cited inputs supply the evaluated bearer and use qualifications.

**ApplicationPredicate.** Score obtains when a calculation actually applies the bound scoring method to the bound input profile under the CN-Spec/CG-Spec conditions. It proceeds on pass or on an explicitly permitted degrade branch and returns the lawful score profile; abstain starts no Score calculation. ScoreEligibility obtains when an evaluation actually assesses the proposal under the eligibility predicates and returns the corresponding judgment. A passing guard or a cached compatible profile does not establish a new Score calculation.

**ApplicationIdentityRule.** One application is one scoring calculation or eligibility evaluation at its calculation locus, from taking up the chosen operands/rules until return or termination. Reidentifying that same invocation preserves identity. A second invocation with identical profile, method, specifications, qualification point and output is a distinct application; changing those arguments for another calculation also makes another application. A record identifier designates an established invocation and cannot create it.

**ApplicationExtentRule.** Score extends from actual use of the input profile under the selected method to the return of its score profile or termination; ScoreEligibility extends from actual proposal assessment to judgment or termination. An unfinished invocation has an open extent and no unreturned result binding. The qualification point or input window identifies what is scored, not when the scoring occurs. Ordinary use of a scoring function does not by itself assert dated U.Work.

For the Celsius example in §4.2, two separate calculations of (20−0)/(40−0) each return 0.5 under the same declared method. Their operand-to-return episodes and result bindings differ. A saved 0.5 can refer to the earlier result when that return is established; numerical agreement and the same method pins cannot establish a second return. The example retains its specified Celsius input and explicit interval endpoints.

* **LawSet** (minimum; admissibility‑first, no hidden scalarization):

  1. **SCP+CSLC lawfulness:** any numeric transform used to produce `ScoreProfileSlot` MUST be admissible under `CGSpecSlot.SCP` and CSLC‑lawful (cites `G.0` + `A.18`).
  2. **ScoringMethod is explicit (no hidden defaults):** `Score` MUST cite `ScoringMethodDescriptionSlot` (edition-pinned via P2W when reproducibility matters; see `A.19.CHR:4.7.2`). Disclose the scoring method **𝒢** (Coordinate→Score), its domain, codomain, Scale, polarity and the properties required by the declared scoring use. Apply C.16 when measurement is claimed and enforce the actual SCP/CSLC restrictions. Boundedness or monotonicity is required only when the selected method or use requires it. USCM MUST NOT rely on an implicit default scoring method.
  3. **No implicit normalization:** `Score` MUST NOT silently perform UNM; if `CNSpecSlot.comparability` requires normalization‑based comparability, the normalization step MUST be explicit in choreography (Uses/pins), not hidden in `Score`.
  4. **Vector scores allowed; scalarization must be explicit:** producing a single scalar score is allowed only if explicitly declared (e.g., by fixing `ScoreProfileSlot` cardinality to 1 and citing the lawful transform); partial‑order semantics MUST NOT be silently reduced to a scalar “tie‑breaker”.
  5. **Unknown is not coerced:** unknown / insufficient evidence MUST NOT be mapped to `0`/`false`; use tri‑state guards and explicit failure behavior.

* **AdmissibilityConditions** (tri‑state guard; fail‑closed on missing admissibility/evidence):

  * `ScoreEligibility(InputProfileSlot, CNSpecSlot, CGSpecSlot, ScoringMethodDescriptionSlot, MinimalEvidenceSlot?) → GuardDecision ∈ {pass|degrade|abstain}`.
  * `pass` requires: (i) `CGSpecSlot.SCP` is present, (ii) the scoring method and edition are explicit, (iii) the input profile is admitted for the exact bearer and criteria, (iv) the cited specs apply to the exact claim scope and selected slices, qualification window, comparison or reference basis, and intended result use, (v) the evidence supporting the admitted profile passes the effective minimum, and (vi) `CN-Spec.comparability` routing is satisfied, including explicit UNM when needed.
  * If `MinimalEvidenceSlot` is absent, the guard MUST evaluate evidence against `CGSpecSlot.MinimalEvidence` (by explicit rule), and MUST NOT return `pass` when evidence is missing/unknown.
  * If `ScoringMethodDescriptionSlot` is missing or unpinned/ambiguous under the active planned baseline, the guard MUST return `abstain` (fail‑closed), not “assume a default”.

* **Applicability:**

  * Intended to be used after indicatorization (when indicator profiles are used) and before comparison/selection.
  * Applicable only when admissibility/evidence surfaces are present via `CGSpecSlot` (fail‑closed otherwise).
  * Applicable only when a scoring method is explicitly declared via `ScoringMethodDescriptionSlot` (edition‑pinned when reproducibility matters). A “do nothing / identity scoring” intent (if ever needed) MUST still be declared as an explicit scoring method description, not as an implicit default.

* **Relation boundary:** scoring creates no transfer relation. If the input profile or receiving use relies on an F.9 Bridge, kind relation, or plane relation, cite that exact obtaining relation, its direction and loss; supported penalties route to **`R_eff` only**.

* **Γ_timePolicy:** `point` by default (no implicit “latest”).

* **PlaneRegime:** each admitted input and score keeps its declared reference plane; USCM introduces no plane crossing. When a conclusion depends on a relation between planes, cite that relation, its direction and loss, and keep the receiving use separate.

* **Audit:**

  * MUST record: the exact evaluated bearer and admitted input profile; `CNSpecRef.edition`, `CGSpecRef.edition`, and `ScoringMethodDescriptionRef.edition`; criteria, claim scope and selected slices, qualification window, comparison or reference basis, and intended result use.
  * MUST record the evidence refs used to admit the input profile and evaluate `ScoreEligibility`.
  * MUST record the **effective evidence policy**:
    * if `MinimalEvidenceSlot?` is present → record `MinimalEvidenceRef` as effective;
    * otherwise → cite `CGSpecSlot.MinimalEvidence` as effective.
  * SHOULD record the realized `GuardDecision` for `ScoreEligibility`, and (when `degrade`/`abstain`) the referenced failure behavior / downstream handling policy id (e.g., SoS‑LOG branch id) when such a policy is in scope.
  * SHOULD record: a stable description of `ScoreProfileSlot`; any F.9 Bridge, kind relation, or plane relation only when the score or receiving use actually relies on it; and, when normalization-based comparability was required, the explicit upstream UNM ref or pin.

#### A.19.USCM:4.2 - Interpretation notes — informative

* **Selected-input basis.** Consume the exact UINDM S and space declaration when an indicator profile is used. For CS7 in A.19.UINDM §5.4, the Celsius policy selects i1 and the declared Celsius scoring rule reads 20, giving 0.5. It cannot read the kelvin position's 293.15 under that rule. After a basis change, resolve the selected positions and the scoring method's input requirements again; keep any projection in the original basis order.

* **A score profile is a set of measures.** `ScoreProfileSlot` is a `U.Set (of U.Measure)`. Treat this as “vector scoring by default.” If a project truly needs a single scalar score, declare that explicitly (per LawSet item 4), rather than assuming scalarity.

* **USCM does not order; it scores.** USCM produces score measures. Any ordering, dominance, or set‑valued comparison is performed by CPM and SelectorMechanism (and any optional aggregation is made explicit via ULSAM). Treating the score as “the decision” is a category error in CHR terms.

* **ScoringMethod is explicit (no hidden defaults).** USCM requires `ScoringMethodDescriptionSlot`: the scoring method is a first‑class, auditable choice (typically pinned in planned baseline). This keeps “how we score” evolvable (wired via method packs) without making it implicit or accidental.

* **No implicit UNM is a boundary guard.** This discourages convenience implementations that “just normalize inside scoring.” USCM forbids that: if comparability requires normalization‑based routing, the UNM step is explicit in choreography (Uses/pins) and visible in audit surfaces.

* **Evidence policy is explicit and auditable.** `MinimalEvidenceSlot?` is an optional override; otherwise the effective policy is `CGSpecSlot.MinimalEvidence`. Failures do not disappear; they must show up as `degrade/abstain` and be traceable.

* **Relations are explicit and loss stays in `R_eff`.** When a score or receiving conclusion depends on another source-local meaning, bearer kind, or reference plane, cite the exact obtaining relation and supported loss. A changed bearer, scope, method, basis, or use is not by itself a crossing.

