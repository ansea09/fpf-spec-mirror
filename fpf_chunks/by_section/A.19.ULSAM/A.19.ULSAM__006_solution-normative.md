---
chunk_kind: "child"
pattern_id: "A.19.ULSAM"
pattern_title: "Unified Lawful Scale Aggregation Mechanism (ULSAM)"
section_id: "A.19.ULSAM:4"
section_title: "Solution (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.ULSAM/A.19.ULSAM__006_solution-normative.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "A.19.ULSAM — Unified Lawful Scale Aggregation Mechanism (ULSAM)"
  - "A.19.ULSAM:4 — Solution (normative)"
line_start: 33621
line_end: 33706
dependencies:
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.19.UINDM"
  - "A.19.ULSAM"
  - "A.19.USCM"
keywords:
  - "CG-Spec.SCP"
  - "CG-Spec.Γ_fold"
  - "MinimalEvidence"
  - "fold_Γ?"
  - "lawful aggregation"
  - "scale-lawful fold"
  - "tri-state guard (pass"
  - "ΓFoldRef"
---

### A.19.ULSAM:4 - Solution (normative)

ULSAM is the **canonical scale‑aggregation mechanism** in the CHR suite. It defines:
* a stable **mechanism boundary** (`fold_Γ?` is a stage with its own operation and eligibility predicate),
* a stable **SlotKind surface** (via the suite lexicon),
* a **tri‑state admissibility guard** (fail‑closed on missing admissibility/evidence),
* and an **audit minimum** (admitted set and membership basis, fold and policy editions, scope and window, evidence, contributors, result, and any relation actually used).

Method semantics (“which aggregation family to use”) remain out of suite core: they belong in SoTA packs (`G.2`) and wiring‑only extension modules (`GPatternExtension` blocks), while ULSAM remains the stable mechanism boundary.

#### A.19.ULSAM:4.1 - Mechanism.Intension (canonical; normative)

Archetypal Grounding — **Mechanism.Intension** (normative).

This is the canonical `U.Mechanism.Intension` for `ULSAM.IntensionRef` and is intended to be cited by CHR suite publications and by any wiring layers.

* **Scope note:** this intension is an **instance** authored to the `U.Mechanism.Intension` shape governed by `A.6.1`. It defines only the mechanism’s semantic surface (slots/ops/laws/guards/audit). It does **not** bind project‑specific pins (P2W), and it does **not** emit GateDecision/GateLog or publish/telemetry steps; it emits `Audit` pins and a tri‑state guard only.

* **IntensionHeader:** `id = ULSAM`, `version = 1.0.0`, `status = stable`.
* **IntensionRef:** `ULSAM.IntensionRef` (canonical target for the suite member named in `A.19.CHR:4.2`).
* **Tell.** Explicit **Γ‑fold** over admitted measures — no hidden aggregation inside scoring/comparison/selection.
* **Purpose:** explicit **Γ‑fold** (and, when declared, time‑fold) over admitted measures — no hidden aggregation inside scoring/selection.
* **Imports:** `G.0 (CG‑Spec.Γ_fold, CG‑Spec.SCP, CG‑Spec.MinimalEvidence)`, `A.18 (CSLC)`, `A.19.CN (CN‑Spec.acceptance + aggregation routing)`, `A.6.5 (slot discipline)`, `B.3 (Γ‑fold defaults for R_eff, incl. WLNK)`, `A.19.CHR:4.2.1 (CHR SlotKind Lexicon)`.

* **SubjectBlock:**
  * **SubjectKind:** `ScaleAggregation` (Γ‑fold).
  * **GovernedValueDomain:** `U.Measure`.
  * **SliceBasis:** the declared `U.ClaimScope` and selected `U.ContextSlice` members, together with the qualification window and intended result use.
  * **ExtentRule:** aggregation ranges over the admitted measure set and its declared grouping or membership basis, scope and window, evidence basis, contributors, and intended result; `CNSpecSlot.acceptance` routes admission while `CG-Spec.Γ_fold` and `CG-Spec.SCP` govern admissibility.
  * **ResultKind?:** `U.Measure`.

* **SlotIndex** (derived projection from `SlotSpecs` / guard SlotSpecs; uses `A.19.CHR:4.2.1` SlotKind tokens; no independent semantics):
  * `MeasureSetSlot : ⟨ValueKind = U.Set (of U.Measure), refMode = ByValue⟩`,
  * `CNSpecSlot : ⟨ValueKind = CN‑Spec, refMode = CNSpecRef⟩`,
  * `CGSpecSlot : ⟨ValueKind = CG‑Spec, refMode = CGSpecRef⟩`,
  * `GammaFoldSlot : ⟨ValueKind = ΓFold, refMode = ΓFoldRef⟩`,
  * no generic `ContextSlot`: the measure set, CN-Spec, CG-Spec, and Γ-fold declaration resolve the grouping or membership basis, scope and window, evidence, contributors, and intended result,
  * `MinimalEvidenceSlot? : ⟨ValueKind = MinimalEvidence, refMode = MinimalEvidenceRef⟩` (optional override; otherwise cite `CGSpecSlot.MinimalEvidence`),
  * `AggregatedMeasureSlot : ⟨ValueKind = U.Measure, refMode = ByValue⟩`,
  * `ContributorSetSlot? : ⟨ValueKind = U.Set (of U.Measure), refMode = ByValue⟩` (optional but recommended for auditability).

* **OperationAlgebra** (suite stage = `fold_Γ?`, per `A.19.CHR:4.5`; canonical stage‑op = `Fold_Γ`):
  * `Fold_Γ(MeasureSetSlot, CNSpecSlot, CGSpecSlot, GammaFoldSlot, MinimalEvidenceSlot?) → (AggregatedMeasureSlot, ContributorSetSlot?)`; the cited inputs supply the set, grouping and use qualifications.

* **LawSet** (minimum; explicit, scale‑lawful folding only):
  1. **No hidden aggregation:** any Γ‑fold MUST be explicit as `Fold_Γ` (no folding hidden inside `Score/Compare/Select`).
  2. **Scale‑lawfulness:** aggregation MUST be CSLC‑lawful and admissible under `CGSpecSlot.SCP`; ordinal arithmetic (e.g., means on ordinal ranks) is forbidden unless explicitly allowed by the relevant CSLC fragment.
  3. **Γ‑fold admissibility:** `GammaFoldSlot` MUST resolve to either `CGSpecSlot.Γ_fold` or an explicitly pinned override (CAL policy) -- never an implicit "implementation default".
  4. **Evidence‑gated folding:** if evidence is insufficient/unknown, folding MUST follow tri‑state guard behavior and MUST NOT silently coerce.
  5. **Contributor accountability (when produced):** when `ContributorSetSlot?` is produced, it MUST be a subset of the admitted portion of `MeasureSetSlot`, and `AggregatedMeasureSlot` MUST be the result of applying the effective Γ‑fold to that contributor subset (no “hidden contributors”).
  6. **No implicit UNM:** ULSAM MUST NOT silently normalize/rescale to “force comparability.” If establishing a compare‑on‑invariants surface requires UNM for the measures being folded, UNM MUST appear as an explicit stage (Uses + pins) upstream; ULSAM itself remains folding‑only.

* **AdmissibilityConditions** (tri‑state guard; fail‑closed on missing admissibility/evidence):
  * `FoldEligibility_Γ(MeasureSetSlot, CNSpecSlot, CGSpecSlot, GammaFoldSlot, MinimalEvidenceSlot?) → GuardDecision ∈ {pass|degrade|abstain}`.
  * `pass` requires: (i) `CGSpecSlot` provides `SCP` and `Γ_fold`, (ii) `GammaFoldSlot` resolves to the admitted fold or an explicit override, (iii) the measure set and its grouping or membership basis are admitted by `CNSpecSlot.acceptance`, (iv) scope, window, evidence, contributors, and intended result are recoverable, and (v) the set is scale-compatible for that fold.
  * Define `EffectiveMinimalEvidence := (MinimalEvidenceSlot if present, else CGSpecSlot.MinimalEvidence)`; the guard MUST evaluate evidence against `EffectiveMinimalEvidence`.
  * If evidence is missing/unknown under `EffectiveMinimalEvidence`, the guard MUST NOT return `pass` (return `degrade` or `abstain` per the effective failure behavior; record the basis in Audit).

* **Applicability:**
  * Intended to be used only when a fold is explicitly required (and never as a hidden sub‑step of scoring/comparison/selection).
  * Applicable only when `CGSpecSlot` provides the admissibility surface (`Γ_fold` and `SCP`) (fail‑closed otherwise).
  * If comparability routing for the measures being folded is UNM‑based, applicability presumes an explicit upstream UNM stage; ULSAM does not “make measures comparable” by itself.

* **Relation boundary:** folding creates no transfer relation. If the admitted set or receiving use relies on an F.9 Bridge, kind relation, aggregation or membership relation, or plane relation, cite the exact obtaining relation, its direction and loss; supported penalties route to **`R_eff` only**.
* **Γ_timePolicy:** `point` by default; time‑fold requires explicit windowing policy (if an explicit operator is needed, introduce `FoldTime_Γ` as an `⊑⁺` extension using `GammaTimeRuleSlot` from the CHR SlotKind Lexicon).
* **PlaneRegime:** each contributor and aggregated measure keeps its declared reference plane; ULSAM introduces no plane crossing. When a result depends on a relation between planes, cite that relation, its direction and loss, and keep the receiving use separate.

* **Audit:**
  * MUST record: the admitted measure set and grouping or membership basis; `CNSpecRef.edition`, `CGSpecRef.edition`, and effective `ΓFoldRef`; claim scope and selected slices, qualification window, intended result, and the aggregated measure.
  * MUST record the evidence refs used to admit the measure set and evaluate `FoldEligibility_Γ`.
  * If `GammaFoldSlot` resolves via an explicit override, SHOULD record the override’s `policy-id` (or its stable ref) alongside `ΓFoldRef`.
  * When `MinimalEvidenceSlot?` is present, MUST record `MinimalEvidenceRef`; otherwise MUST cite `CGSpecSlot.MinimalEvidence` as the effective evidence policy.
  * When `ContributorSetSlot?` is produced, SHOULD record it (or an id reference) as an auditable explanation surface.
  * SHOULD record: any explicit UNM invocation ids/pins when folding presumes a compare‑on‑invariants surface established by UNM.
  * SHOULD record: an F.9 Bridge, kind relation, aggregation or membership relation, or plane relation only when the fold or receiving use actually relies on that obtaining relation.
  * SHOULD record: the evaluated `GuardDecision` (especially when not `pass`) and, when applicable, the effective evidence policy / failure behavior reference used to justify `degrade|abstain`.

#### A.19.ULSAM:4.2 - Interpretation notes (didactic, informative)

- **Γ‑fold is a declared governing spec ref, not an implementation choice.** In FPF terms, “how we fold” is a **policy-level commitment**: `GammaFoldSlot` MUST be resolvable to `CGSpecSlot.Γ_fold` routing or an explicit pinned override. If you cannot cite it, you do not have a fold — you have a hidden default.
- **ULSAM is not normalization.** ULSAM does not establish comparability by itself: it does not normalize, rescale, or “align units” as a hidden convenience. If a compare‑on‑invariants surface is required, invoke UNM explicitly upstream and cite the effective pins in Audit.
- **Prefer vector semantics when possible.** If you do not strictly need one aggregated measure, keep measures separate and let `CPM` + `SelectorMechanism` operate on a partial order (set-return semantics). A fold is a lossy compression; treat it as such.
- **Contributor surfaces are not “nice-to-have” in practice.** `ContributorSetSlot?` is optional in the signature, but operationally it is the simplest way to prevent “mystery rollups” and to preserve an explanation surface.
- **Time-fold is a specialization, not a loophole.** The base ULSAM declares `Γ_timePolicy` and allows time-fold only via explicit windowing policy. If a project needs an explicit `FoldTime_Γ` operator, introduce it as an `⊑⁺` extension consistent with `A.6.1:4.2.1` (no mutation of inherited ops; no SlotKind drift).
  - Use the suite lexicon token `GammaTimeRuleSlot` for the additional windowing rule input; do not overload `GammaFoldSlot` or invent a generic context input to carry time semantics.

