---
chunk_kind: "child"
pattern_id: "A.19.SelectorMechanism"
pattern_title: "Unified Selection Kernel, SelectorMechanism"
section_id: "A.19.SelectorMechanism:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SelectorMechanism/A.19.SelectorMechanism__006_solution.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "A.19.SelectorMechanism — Unified Selection Kernel, SelectorMechanism"
  - "A.19.SelectorMechanism:4 — Solution"
line_start: 32526
line_end: 32635
dependencies:
keywords:
  - "SelectEligibility"
  - "selected set"
  - "selection kernel"
  - "set-returning selection"
  - "tri-state guard (pass"
---

### A.19.SelectorMechanism:4 - Solution

`SelectorMechanism` is the canonical **selection kernel** for CHR and for selector specializations. It provides:

* a stable mechanism boundary for `select`,
* a stable SlotKind field set (via the CHR lexicon),
* a minimum law set that preserves set‑valued semantics and forbids hidden thresholds and hidden scalarization,
* a tri‑state admissibility guard that is fail‑closed under missing admissibility or evidence,
* an audit minimum that records effective editions and policy references.

Method semantics and SoTA algorithm families do not live inside the kernel: they connect via `G.2` SoTA packs and wiring modules, and via admissible specializations `⊑` and `⊑⁺` that obey the specialisation-chain discipline (`A.6.1:4.2.1`).

#### A.19.SelectorMechanism:4.1 - Mechanism.Intension — normative core

Archetypal Grounding — **Mechanism.Intension** (normative).

* **Scope note:** this intension is an **instance** authored to the `U.Mechanism.Intension` shape governed by `A.6.1`. It defines only the mechanism’s semantic boundary: slots, operations, laws, guards, and audit. It does **not** bind project-specific planned pins, and it does **not** emit GateDecision or GateLog; it emits `Audit` pins and a tri-state guard only.
* **Canonicality note:** this is the canonical `U.Mechanism.Intension` for `SelectorMechanism.IntensionRef` and is intended to be cited by CHR suite publications and by any wiring layers; other mentions are **Tell + Cite** only.

* **IntensionHeader:** `id = SelectorMechanism`, `version = 1.0.0`, `status = stable`.

* **IntensionRef:** `SelectorMechanism.IntensionRef` (canonical target for the suite member named in `A.19.CHR:4.2`).

* **Tell.** Universal set‑returning selection kernel over candidates and criteria; defaults remain policy‑bound; **no hidden thresholds**.

* **Purpose:** universal set‑returning selection kernel over candidates and criteria; defaults remain policy‑bound; **no hidden thresholds**.

* **Imports:** `A.6.1:4.2.1 (specialisation relation chains)`, `A.6.5 (slot discipline; SlotIndex as projection)`, `A.19.CN (CN‑Spec governance card)`, `C.22 (TaskSignature as a policy-reference artifact when used)`, `G.5 (selector conformance and default selection policy)`, `G.0 (CG‑Spec admissibility and evidence gates)`, `A.19.CHR:4.2.1 (CHR SlotKind Lexicon)`.

* **SubjectBlock:**

  * **SubjectKind:** `Selection`.
  * **GovernedValueDomain:** candidate set plus admissible comparison-outcome relation token set.
  * **SliceSet:** `U.ContextSliceSet`.
  * **ExtentRule:** selection ranges over admitted candidates in the active context slice, constrained by explicit criteria and policies and by admissible comparison outcomes.
  * **ResultKind?:** `U.Set`.

* **SlotIndex:** derived projection from `SlotSpecs` (and any guard‑only SlotSpecs) per slot discipline; uses `A.19.CHR:4.2.1` SlotKind tokens; has no independent semantics.

  * `CandidateSetSlot : ⟨ValueKind = U.Set (candidates), refMode = ByValue⟩`.
  * `ComparisonResultSlot : ⟨ValueKind = U.Set (relation or poset tokens), refMode = ByValue⟩`.
  * `CriteriaSlot : ⟨ValueKind = U.Set (selection criteria or clauses, including explicit tie‑breakers; **acceptance thresholds are not criteria** and remain governed by the cited acceptance declarations and applied only via `SelectEligibility`), refMode = ByValue⟩`.
  * `TaskSignatureSlot? : ⟨ValueKind = TaskSignature, refMode = TaskSignatureRef⟩` optional; when present, SHOULD be the single policy-default slot or ref for selector defaults (e.g., `PortfolioMode` or dominance regime), but it does not replace `CNSpecSlot` or `CGSpecSlot` governing spec refs.
  * `CNSpecSlot : ⟨ValueKind = CN‑Spec, refMode = CNSpecRef⟩`.
  * `CGSpecSlot : ⟨ValueKind = CG‑Spec, refMode = CGSpecRef⟩`.
  * `ContextSlot : ⟨ValueKind = U.BoundedContext, refMode = U.BoundedContextRef⟩`.
  * `MinimalEvidenceSlot? : ⟨ValueKind = MinimalEvidence, refMode = MinimalEvidenceRef⟩` optional override; otherwise the effective evidence policy is `CGSpecSlot.MinimalEvidence`.
  * `SelectionSlot : ⟨ValueKind = U.Set (selected set), refMode = ByValue⟩`.

* **OperationAlgebra** suite stage = `select`, per `A.19.CHR:4.5`; canonical stage op = `Select`

  * `Select(CandidateSetSlot, ComparisonResultSlot, CriteriaSlot, CNSpecSlot, CGSpecSlot, ContextSlot, TaskSignatureSlot?, MinimalEvidenceSlot?) → SelectionSlot`.

* **LawSet** (minimum): the selection kernel is set‑returning and policy‑bound

  1. **Set‑returning by default:** a conformant `Select` MUST return a declared selected set by default. It MUST NOT silently collapse partial orders or incomparabilities to a single winner; if a singleton outcome is required, it MUST be an explicit criterion (or a declared upstream total order).
  2. **No hidden thresholds or constants:** a conformant publication MUST NOT smuggle thresholds, weights, dominance rules, or tie‑breakers. Selection‑level commitments MUST be explicit in `CriteriaSlot` and, where needed, in explicit policy defaults exposed through `TaskSignatureSlot`. Admissibility and acceptance thresholds are applied only via `SelectEligibility` using `CNSpecSlot.acceptance` and the effective evidence policy (`MinimalEvidenceSlot?` or `CGSpecSlot.MinimalEvidence`).
  3. **No hidden scalarization:** a conformant publication MUST consume `ComparisonResultSlot` as set‑valued or partial when it is set‑valued or partial. Scalar summaries (if produced at all) are report‑only unless explicitly promoted by policy outside suite closure.
  4. **Evidence gating is explicit:** when selection depends on evidence, it MUST cite either `MinimalEvidenceSlot` (override) or the effective policy `CGSpecSlot.MinimalEvidence`, and it MUST evaluate the selection with tri‑state guards (no unknown coercion). Any candidate‑level ineligibility handling MUST be explicit (criteria and upstream outputs when used) and auditable (no silent dropping); the kernel MUST NOT invent new evidence thresholds.
  5. **No competing defaults:** `PortfolioMode` and dominance defaults (when relevant) MUST be sourced from their declared governing patterns (typically through `TaskSignatureSlot` and the selector conformance or default rules in `G.5` when used), and MUST NOT be re‑declared inside the kernel.

* **AdmissibilityConditions** (tri‑state guard; fail‑closed on missing admissibility or evidence)

  * `SelectEligibility(CandidateSetSlot, ComparisonResultSlot, CriteriaSlot, CNSpecSlot, CGSpecSlot, ContextSlot, TaskSignatureSlot?, MinimalEvidenceSlot?) → GuardDecision ∈ {pass|degrade|abstain}`.
  * `pass` requires at minimum: (i) `ComparisonResultSlot` is compatible with `CandidateSetSlot` (same candidate universe), (ii) all selection criteria and any tie‑breakers are explicit (via `CriteriaSlot` and `TaskSignatureSlot` when used), (iii) admissibility and acceptance gates (`CNSpecSlot.acceptance`, evidence) do not fail, and (iv) `CNSpecSlot` and `CGSpecSlot` are coherent for the comparison tokens being consumed (no mixed CN-Spec and CG-Spec pairings).
  * If `MinimalEvidenceSlot` is absent, `SelectEligibility` MUST evaluate evidence against `CGSpecSlot.MinimalEvidence` by explicit rule, and missing or unknown evidence MUST NOT yield `pass`.
  * `degrade` is permitted only when an explicit, auditable failure behavior exists (policy‑bound), e.g., “exclude ineligible candidates” or “sandboxed probe only”; `abstain` is used when selection cannot proceed admissibly under the declared criteria and policies.

* **Applicability:**

  * Intended as the last stage of CHR selection after admissible comparison, producing a selected-set-valued result.
  * Cross‑context selection is allowed only via explicit Transport (Bridge, CL, and ReferencePlane) and cannot bypass CG‑Spec admissibility.

* **Transport:** declarative‑only: no embedded CL, Φ, or Ψ tables and no new transport edges; crossings are via cited Bridge, CL, and ReferencePlane declarations; penalties are assigned to **`R_eff` only**.

* **Γ_timePolicy:** `point` by default, no implicit latest.

* **PlaneRegime:** declarative‑only; does not introduce plane crossings. If selection spans planes, it MUST cite the applicable **ReferencePlane** and **CL^plane** policy; penalties are assigned to **`R_eff` only**.

* **Audit:**

  * Must record: `CNSpecRef.edition`, `CGSpecRef.edition`.
  * If `TaskSignatureSlot?` is present, must record `TaskSignatureRef.edition`.
  * If `MinimalEvidenceSlot?` is present, must record `MinimalEvidenceRef`; otherwise must cite `CGSpecSlot.MinimalEvidence` as the effective evidence policy.
  * SHOULD record: the realized `GuardDecision` (`pass|degrade|abstain`) and, when non‑`pass`, the policy‑bound failure behavior reference that justified it.
  * SHOULD record: a stable identity for `CandidateSetSlot` and `ComparisonResultSlot` **or** a citable upstream `Audit` anchor that already fixes these identities; the goal is traceability without duplicating upstream semantics.
  * MUST record: a stable identity for `SelectionSlot`.
  * SHOULD record: a stable description (or citable reference) for the effective selection criteria record or reference (e.g., criteria record ids when criteria are reference‑backed; `TaskSignatureRef` when used).
  * SHOULD record: the realized policy-relevant selector defaults (e.g., `PortfolioMode` or dominance regime) **when** they are not fully determined by a referenced `TaskSignatureRef` or an explicit selector policy reference; the point is auditability, not re‑declaring defaults.
  * SHOULD record: any Bridge, CL, and ReferencePlane ids when `Transport` was used.

#### A.19.SelectorMechanism:4.2 - Boundary and layering rules

1. **Selection consumes upstream CHR products, it does not invent them.** `ComparisonResultSlot` is an input: the kernel MUST NOT perform normalization (UNM), indicatorization (UINDM), scoring (USCM), folding (ULSAM), or comparison (CPM) inside `Select`. If a scalar “overall score” is desired, it must be declared upstream as an admissible scoring or comparator choice, not invented inside selection.

2. **Threshold discipline (acceptance ≠ selection).** Acceptance and admission thresholds are not selection criteria: they live in `AcceptanceClauses`, `TaskSignature`, or `GateProfile` records per `A.19.CHR:4.3.5` and are applied only via `SelectEligibility`. Selection‑level tie‑breakers, `PortfolioMode`, or selected-set constraints MAY exist, but MUST be explicit and auditable (typically as criteria records or explicit policy references), never as unnamed constants.

3. **Report‑only summaries inside suite closure.** Any scalar summaries, illumination metrics, or auxiliary “why not chosen” telemetry are report‑only unless explicitly promoted by policy, and MUST NOT be used as hidden dominance rules (`A.19.CHR:4.3.3`).
   Publishing and telemetry remain outside suite closure and are handled by established publication forms such as `G.10` or `PTM`, not as hidden tails inside selection.

4. **Specializations are explicit and disciplined.** Any refinement or extension of `SelectorMechanism` must follow `A.6.1:4.2.1`:

   * SlotKind invariance for inherited operations,
   * no new mandatory inputs to inherited `Select`,
   * added capabilities appear as new operations or as `⊑⁺` extensions.

5. **Planned slot filling is preserved.** Planned fillers for `TaskSignatureRef@edition`, `CGSpecRef@edition`, evidence policy overrides, and other pins live in `SlotFillingsPlanItem` rows. Execution visibility is via `Audit`, not by mutating plan objects at run time.

---

