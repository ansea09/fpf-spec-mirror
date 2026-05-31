---
chunk_kind: "child"
pattern_id: "A.19"
pattern_title: "CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
section_id: "A.19:0"
section_title: "Reading path for engineer-managers"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19/A.19__002_reading-path-for-engineer-managers.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "A.19 — CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
  - "A.19:0 — Reading path for engineer-managers"
line_start: 22218
line_end: 22293
dependencies:
  - "A.17"
  - "A.18"
  - "A.19.CHR"
  - "A.19.CN"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.19.SOURCE-SET-SPACE-SUBSTRATE"
  - "A.2.5"
  - "A.3.3"
  - "C.16"
  - "E.18"
  - "G.0"
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

### A.19:0 - Reading path for engineer-managers

> **Informative (navigation only).** This subsection is a didactic index for human readers. It introduces no new norms and does not change governing-pattern assignment.

**When to use this path.** You need to review a CHR-enabled plan or audit, or coordinate engineering work across teams, without deep-diving every CHR mechanism up front.

**Step 1 — Measurement vocabulary: what is measured, and what “comparable” can mean.**

* **A.17** — canonizes the technical anchor **Characteristic** (and retires near-synonyms such as “axis/dimension/feature/property/metric” from normative Tech register).
* **A.18** — CSLC discipline (**Characteristic / Scale / Level / Coordinate**) as the metrology of interpretability, comparability, and admissible aggregation.
* **C.16 (MM‑CHR)** — the measurement substrate (`U.DHCMethodRef`, `U.Measure`, `U.Unit`, `U.EvidenceStub`) and the conservative baseline of **direct comparability** (“same template”). C.16 makes coordinates auditable; it does not define CHR mechanisms. Use `C.16.P` first when the wording itself still hides whether the live object is a characteristic, scale, coordinate, score, metric label, quality-term repair, or another receiving object.

**Step 2 — Ontology and governing spec refs the CHR suite operates on.**

* This pattern **A.19** — `U.CharacteristicSpace` and the dynamics hook: the base ontology of measurable coordinates and their spaces.
* **A.19.CN** — CN‑frame / **CN‑Spec**: the governance card for normalization and comparability routing, indicator policy, aggregation routing, and acceptance; it explicitly points to **C.16** for evidence/backing and to **G.0** for legality gates.

**Step 3 — Legality gates and mechanism shape (what to check when numbers appear).**

* **G.0 (CG‑Spec)** — the legality gate for numeric operations and comparisons (SCP, ComparatorSet, MinimalEvidence, Γ_fold, crossings/plane pins). CHR mechanisms cite CG‑Spec; they do not duplicate it.
* **A.6.1 and A.6.5** — the mechanism norm‑form (`U.Mechanism.Intension`) and slot discipline. Read once so the structure of each mechanism-governing pattern (slots, operators, laws, admissibility guards, audit anchors) is predictable.

**Step 4 — The CHR suite boundary and the P2W seam.**

* **A.19.CHR (CHRMechanismSuite)** — focus on:
  * `A.19.CHR:4.1` (published objects),
  * `A.19.CHR:4.2.1` (CHR SlotKind lexicon),
  * `A.19.CHR:4.2.2` (canonical mechanism targets),
  * `A.19.CHR:4.5` (suite protocols — order/optionality live here, not in `mechanisms[]`),
  * `A.19.CHR:4.6–4.7.2` (P2W planned-baseline hook and the plan-item shape),
  * `A.19.CHR:7` (suite conformance checklist).
* **A.15.3** — `SlotFillingsPlanItem` (planned baseline discipline: planning vs enactment).
* **E.18 (E.TGA)** — how to express the actual pipeline/flow graph (including crossings) while keeping suite and plan artefacts refs‑only.

**Step 5 — The six CHR mechanism-governing patterns (read one at a time).**

Each mechanism-governing pattern below publishes its `U.Mechanism.Intension` card and assumes the measurement-admissibility base from **A.17/A.18** and **C.16**.

1. **A.19.UNM** — normalization (CV→NCV, `≡_UNM`, `TransportRegistryΦ`).
2. **A.19.UINDM** — indicatorization (policy-bound indicator selection; no “NCV ⇒ indicator” shortcut).
3. **A.19.USCM** — scoring (SCP-first; no implicit UNM).
4. **A.19.ULSAM** — admissible aggregation (explicit `Γ_fold`; ordinals are not averaged).
5. **A.19.CPM** — comparison (set-valued outcomes; no silent scalarisation/totalisation).
6. **A.19.SelectorMechanism** — selection kernel (set-returning; dominance/`PortfolioMode` defaults are policy-bound).

**Step 6 — Specialization and reuse.**
* **A.19.ECS** — how to construct an object-under-improvement evaluation `CharacteristicSpace` for the object being improved: `A.19` says how the space is structured; `A.19.ECS` says how to make one useful for a declared object kind under improvement, use, contrast cases, scale set, value meanings, trade-offs, and stop or reopen condition.

* **E.20** — how to use specializations of mechanisms (`⊑` / `⊑⁺`) without breaking SlotKind meaning or introducing hidden inputs; consult this whenever you see project‑ or domain‑specific variants of the CHR mechanisms.

**Fast review entry points.**

* If you are reviewing a plan: start from **A.19.CHR:4.6–4.7.2** (planned baseline hook + plan item shape) and **A.15.3** (what a planned baseline may/may not contain).
* If you are reviewing semantic drift: start from **A.19.CHR:4.2.2** (canonical targets), then use **E.10** (suffix discipline) and **F.18** (alias docking) to preserve public continuity while fixing terminology.
* If you are reviewing conformance: start from **A.19.CHR:7** (suite checklist), then consult the relevant **A.19.<MechId>** checklist(s) for mechanism-level conformance; use **E.19** for the review protocol.

**Non‑duplication note.** This pattern defines `U.CharacteristicSpace` and the typing hook `U.Dynamics.stateSpace`. It reuses the canonical measurement concepts (`U.Characteristic`, **CSLC** terms) from **A.17/A.18** and remains notation‑neutral about storage/IDs.
This pattern is intentionally **not** a second governing pattern for CHR mechanisms: it may *use* CHR‑mechanism terms when talking about comparability and certification, but it does so strictly by *Tell + Cite* to the corresponding `A.19.<MechId>` mechanism-governing patterns.

**Governing-pattern rule (Normalization & CHR mechanisms referenced here).** This pattern **MUST NOT** be a second governing pattern for CHR‑mechanism vocabulary.
- **Normalization vocabulary + admissibility** (UNM vocabulary items: `UNM`, `NormalizationMethod`, `NormalizationMethodDescription`, `NormalizationMethodInstance`, **NCV**, **≡_UNM**, `NormalizationFix`; κ-retirement; “map vs Map” lexical guard) are governed normatively by **A.19.UNM**.
- **Indicatorization vocabulary + admissibility** (UINDM vocabulary items: `IndicatorChoicePolicy`, `Indicator`, `IndicatorSet`, indicatorization as a policy step; “NCV ⇒ indicator” prohibition) are governed normatively by **A.19.UINDM**.
- **Other CHR mechanism vocabulary referenced here** (e.g., scoring, aggregation, comparison, and selection terms) is governed normatively by the corresponding mechanism-governing pattern in the `A.19.<MechId>` family (e.g., `A.19.USCM`, `A.19.ULSAM`, `A.19.CPM`, `A.19.SelectorMechanism`).
- **Evidence/calibration backing** for normalization is governed by **C.16 (MM‑CHR)**.
- **CN‑Spec field/ref bindings** (`CN_Spec.normalization`, `CN_Spec.comparability.*`) are governed by **A.19.CN (CN‑Spec)**.
- **Vocabulary extension rule.** If this pattern needs a new term for normalization, indicatorization, scoring, aggregation, comparison, or selection, it SHALL be introduced in the corresponding mechanism-governing pattern first, then cited here (*Tell + Cite*). A.19 SHALL NOT mint new CHR‑mechanism vocabulary.

**Terminology pointer (informative; do not duplicate).** When A.19 uses normalization or indicatorization terms below, it uses them *by reference* to **A.19.UNM** and **A.19.UINDM** and **C.16**. This pattern only constrains how such normalization method instances or declarations are **cited** when doing state‑space comparability, embeddings, and certification.

**Reader guide (informative).**
* If you need the **meaning** of `UNM`, `NCV`, `≡_UNM`, or `NormalizationFix` or `NormalizationFixSpec`: see **A.19.UNM**.
* If you need the **meaning** of `IndicatorChoicePolicy` / indicatorization: see **A.19.UINDM**.
* If you need the **CN‑Spec field/ref bindings** (`CN_Spec.normalization`, `CN_Spec.comparability.*`): see **A.19.CN**.
* If you need **evidence/calibration backing** for normalization or scoring legality: see **C.16 (MM‑CHR)**.
* If you need **cross‑context alignment mechanics**: see **F.9 (Alignment Bridge)** and the `Transport` discipline (A.6.1).

