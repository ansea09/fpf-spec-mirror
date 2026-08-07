---
chunk_kind: "child"
pattern_id: "A.19"
pattern_title: "CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
section_id: "A.19:6"
section_title: "Conformance Checklist (normative) — CC‑A19"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19/A.19__010_conformance-checklist-normative-cc-a19.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "A.19 — CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
  - "A.19:6 — Conformance Checklist (normative) — CC‑A19"
line_start: 28738
line_end: 28791
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

### A.19:6 - Conformance Checklist (normative) — **CC‑A19**

**Formality references and operational segregation (normative).** A.19 aligns with **C.2.3 Unified Formality Characteristic (F)**. Use **F** directly instead of tier labels such as **T0**, **T1**, and **T2**, and treat operations separately (see **E.10** for registers).
— **F-Declaration baseline (recommended F ≥ F3).** Obligations are **declarability** and **arguability**: the author can **name** the CharacteristicSpace (basis and slots as *(Characteristic, Scale)* pairs), **state** the comparability regime (coordinatewise or normalization-based), and **express** a state’s checklist in observable coordinates. No persistence formats, identifiers, or operational provenance are required.
— **F-Predicates (F ≥ F4 when predicate-like).** As above, plus **explicit slot and NormalizationMethod names** and **stated overlays** (order or metric). When acceptance conditions are written as **typed predicates over coordinates**, declare **F ≥ F4**. Remains **notation-neutral** and **persistence-agnostic**.
— **Operational bindings (not part of F).** When automatic checking or assurance is required, use **A.19.CN**, **C.16**, and **B.3** for identifiers, validity windows, waivers, and logs. These raise **R** and **TA** in the trust calculus and **do not change F** unless the **expression form** changes (see C.2.3 orthogonality).

The following checklist summarizes the normative requirements introduced by Pattern A.19. An implementation or model **conforms** to A.19 if and only if all these conditions are met:

**Spaces & mappings**
**CC‑A19.1.** Any defined **Subspace**, **Embedding**, or **Product** of CharacteristicSpaces **MUST** explicitly list the involved slots and their metadata (scale type, unit, polarity). No comparability or merging is allowed purely by matching names or assuming correspondence – it must be declared.
**CC‑A19.2.** Every **Embedding** `ι: CS₁ ↦ CS₂` **MUST** cite a well‑defined `NormalizationMethodInstance` (per **A.19.UNM**) for each slot where `CS₁`’s slot differs in scale or unit from `CS₂`’s. The cited instances MUST satisfy the admissibility and declaration obligations governed by **A.19.UNM** (including monotonicity w.r.t. polarity, validity window, and method-class token). When the embedding is used for gating or assurance, **C.16** and the governing gate or assurance pattern own the evidence-backed claim. (Identity suffices where scales are identical.)
**CC‑A19.2a.** **Scale‑class guard (by reference).** The scale‑class requirements for admissible normalizations are governed by **A.19.UNM** (and must remain CSLC‑consistent per **A.18**). This checklist item is satisfied by citing a `NormalizationMethodInstance` whose declared class token meets those requirements; do not restate the taxonomy here.

**Comparability**
**CC‑A19.3.** **Coordinatewise comparability** (`≼_coord`) is **permitted only** when the states being compared share the **same CharacteristicSpace**, with **identical scale metadata** on each compared slot, and using the **same state definition criteria**. If these conditions aren’t fully satisfied, an implementation **MUST NOT** attempt direct coordinatewise comparison; it should either apply a **normalization‑based** method or report the items as **incomparable**.
**CC‑A19.3a.** Use of **Indicators** in any checklist or assertion **MUST** cite an **IndicatorChoicePolicy** edition. Treating any **NCV** as an Indicator **without** a declared policy is **forbidden**.

**CC‑A19.4.** **Normalization‑based comparability** (`≼_normalization`) **MUST** be done by first normalizing all relevant coordinates of the source state into the target state’s space via declared admissible `NormalizationMethodInstance`(s) (see **A.19.UNM**), and **only then** comparing in that common space. In other words, two states can be compared under `≼_normalization` only by producing an image of one in the other’s space (`N(x)`) and using `≼_coord` on the result. No implicit or “on the fly” conversions are permitted.
**CC-A19.5.** Any cross-reference-scheme or cross-plane comparison cites an F.9 Bridge with exact endpoints, preserved and lost meaning, direction, applicable use, and CL where current. CPM separately declares comparison scope and evaluation window; neither a matching label nor an optional structure supplies them.

**Neighboring certification references**
**CC-A19.6.** A consumer of a `CharacteristicSpacePredicate` separately states the subject or input projection, one `U.ClaimScope`, relevant `U.ContextSlice` membership, effective reference scheme and plane, application or evaluation window, and any Bridge. These use bindings do not become predicate identity components.

**CC‑A19.7.** If a Green-Gate or enactment rule uses coordinates from a `CharacteristicSpace`, the gate pattern and role-method-work pattern govern permission to act; A.19 only requires that any translated state or coordinate claim cite declared Embeddings and Bridges rather than untracked inferences.
**CC-A19.8.** Predicate and checklist definitions use declared coordinates and explicit logical composition. If temporal order or a multi-step procedure matters, use direct method and work patterns rather than hiding the procedure inside the space or predicate. Indicators require an `IndicatorChoicePolicy`; an NCV is not automatically an indicator.

**Anti‑drift**
**CC‑A19.9.** If a **NormalizationMethod** or **UNM** declaration, space overlay, or state checklist is updated or calibrated differently in a new version, previous StateAssertions are not retroactively modified by A.19. The governing assertion or record pattern closes or versions those claims; A.19 requires only that the old and new space-facing referents remain inspectable.
**CC‑A19.10.** If any **critical slot** in a comparison lacks an **admissible** `NormalizationMethodInstanceId` (per **A.19.UNM**) to translate that slot between the relevant spaces (within the declared validity window), then the comparison **MUST** be reported as **incomparable**. The model must not attempt unofficial workarounds (e.g., name‑matching, silent dropping of the slot, or ad‑hoc coercions). This rule applies even if all other slots have admissible normalization instances, unless a policy explicitly accepts the loss via a declared Bridge with stated limitations.

**Quotients & Normalization‑fix (QNT)**
**CC‑A19.11.** Equality checks and joins across spaces **MUST** target invariant forms (on a **quotient** or declared **NormalizationFixed** chart), not raw coordinates.
**CC‑A19.12.** If a checklist predicates on a normalization‑variant property, it **MUST** name the **NormalizationFix** (which UNM.NormalizationMethod or chart is assumed).
**CC-A19.13.** Every cited normalization method-class token is recoverable from the effective A.19.UNM declaration and reference scheme. A local glossary or model-use structure may aid retrieval but does not supply normalization, scope, predicate, or comparison semantics.

**Metric discipline & calibration (MET)**
**CC‑A19.14.** If a distance overlay is used, acceptance predicates or KPIs over a CS **SHALL** be **non-expansive** (Lipschitz ≤ 1) w.r.t. the published `d` on the declared domain (raw coordinates or NCVs), or declare a compensating margin; otherwise they **SHALL** be isotone w.r.t. the declared product order.
**CC‑A19.15.** Any distance used in state or acceptance checks **MUST** carry max tolerated error and, where claimed, a **Lipschitz bound** for the **NormalizationMethod** composition in use.
**CC-A19.16.** Cross-reference-scheme or cross-plane inputs name the normalization and F.9 Bridge plus their validity conditions. An expired mapping is invalid for the current use unless the direct consumer records an admissible waiver.

**Dynamics and time**
**CC-A19.17.** `CharacteristicSpacePredicate` contains no predicate window. Each consumer binds its own applicability or evaluation interval; observation, evidence, and source-currentness intervals remain with their direct claims and may not reidentify the predicate.
**CC‑A19.18.** Any dynamics map `Φ_{Δt}` used in comparison or gating **MUST** be **non-expansive** (Lipschitz ≤ 1) under the declared distance overlay **and** commute with **NormalizationFix**; otherwise **observation** is required.

**Neighboring certification use**
**CC‑A19.19.** StateAssertions that use a `CharacteristicSpace` must name the current **NormalizationMethod** or **UNM** declaration and overlay definitions used; assertion validity, waiver speech acts, evidence kind, and gate validity are governed by the assertion, evidence, waiver, and gate patterns. A.19 imposes no requirement on identifiers or persistence formats.
**CC‑A19.20.** The space-facing references in a neighboring certification use - normalization declaration, quotient or fixed chart, overlay, and coordinate predicate - are logically distinct and must be reconstructable in the argument or review. The neighboring consumer pattern owns evaluation, assertion, gate, assurance, and decision semantics.

**Operators (OP)**
**CC-A19.21.** Use of `Align_B` declares the exact Bridge. The comparison, gate, or assurance owner retains its own scope, window, result, and CL consequence. A.19 imposes no persistence-identifier requirement.
**CC-A19.22.** Every `CharacteristicSpacePredicate` is recoverable by value from its space, coordinate and scale bindings, normalization or Bridge basis, operator or comparator semantics, cut or band, logical composition, and polarity. It is not a U-kind, description edition, relation occurrence, or evaluation result.
**CC-A19.23.** A predicate use identifies the actual input value or governed projection from its condition or subject. An arbitrary relation occurrence, stored record, or matching label is not automatically a point in the predicate's space.

