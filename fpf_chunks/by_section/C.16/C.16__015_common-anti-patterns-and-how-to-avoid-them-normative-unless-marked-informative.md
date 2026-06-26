---
chunk_kind: "child"
pattern_id: "C.16"
pattern_title: "Measurement & Metrics Characterization (MM‑CHR)"
section_id: "C.16:11"
section_title: "Common Anti-Patterns and How to Avoid Them (Normative unless marked “Informative”)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16/C.16__015_common-anti-patterns-and-how-to-avoid-them-normative-unless-marked-informative.md"
commit_sha: "f1d0f9319cf1f93129b7691a328a281022252c4e"
heading_path:
  - "C.16 — Measurement & Metrics Characterization (MM‑CHR)"
  - "C.16:11 — Common Anti-Patterns and How to Avoid Them (Normative unless marked “Informative”)"
line_start: 43107
line_end: 43169
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "B.3"
  - "C.26"
  - "C.26.1"
keywords:
  - "CSLC"
  - "U.DHCMethod(Ref)"
  - "U.EvidenceStub"
  - "U.Measure"
  - "U.Unit"
  - "direct comparability"
  - "measurement"
  - "measurement template"
  - "polarity"
  - "probe-changing-state"
  - "scoring method disclosure"
  - "shared-frame check"
---

### C.16:11 - Common Anti-Patterns and How to Avoid Them *(Normative unless marked “Informative”)*

#### C.16:11.1 - Invariants (N‑rules)

**N‑1 — One Characteristic + one Scale per template.**
Every `U.DHCMethodRef` binds *exactly one* **Characteristic** and *exactly one* **Scale** (its type + admissible range or level‑set). This is the CSLC sufficiency condition for interpretability.

**N‑2 — Value validity.**
A `U.Measure` holds a **Value** that is *admissible* for the template’s Scale (numeric range, categorical level); when a **Level** is used, it is among the named levels declared for that Scale.

**N‑3 — Polarity is declared at the template.**
For ordered Scales, the template states the comparison direction (↑ better, ↓ better, or target-is-best). Any **ScoringMethod mapping** to **Score** preserves that monotonic ordering. *(Note: we use “ScoringMethod mapping” instead of the Greek letter used elsewhere in FPF to avoid symbol conflicts.)*
For ordered Scales, the template states the comparison direction (↑ better, ↓ better, or target-is-best). Any scoring method **𝒢** that issues a **Score** is order‑compatible with that declared polarity semantics.

**N‑4 — Unit coherence.**
Within one template there is one *primary* **Unit** of expression (or an explicit level‑set for non‑numeric Scales). Conversions are conceptually valid only where the Scale supports meaningful arithmetic (interval or ratio); nominal/ordinal Scales are not subject to numeric conversions.

**N‑5 — Comparability guard.**
Two Measures are comparable *iff* they share the same template (hence, the same Characteristic, Scale, and Unit) **or** stand in an explicit comparability relation whose governing FPF pattern or specification record is cited (e.g., an F‑cluster Bridge, or a cited characterization mechanism’s declared equivalence). Otherwise, comparability is not presumed.

**N-6 - Evidence as conceptual relation.**
If a template requires it, each Measure includes an **EvidenceStub** that conceptually links the Value to its grounds; absence where required makes the Measure inadmissible for use. *(This is a conceptual obligation; no process mechanics are implied.)*

**N‑7 — Arity clarity.**
If the Characteristic is relational (applies to a pair or tuple), the subject of measurement is the relation itself; the reading must not be re‑described as a unary property of either participant.

**N‑8 — Open‑ended evolution; role-state relation, not lifecycle.**
When MM‑CHR is used in change reasoning, movement happens in a **CharacteristicSpace** and is admitted by current `RoleStateRelation@BoundedContext` state assertions and checklists. There is no lifecycle terminal; revisions may re‑enter earlier framing states as per A.17. *(Conceptual control structure only.)*

#### C.16:11.2 - Anti‑Patterns (A‑rules) — with cures

**A‑1 — Scale drift under the same template.**
*Smell:* the Scale meaning (bounds, categories) shifts while the template ID remains.
*Cure:* version the template; declare the relation in the Unification suite.

**A‑2 — Arithmetic on ordinal.**
*Smell:* averaging “stars” or ranking labels as if they were intervals.
*Cure:* either keep order‑respecting operations only, or introduce a **ScoringMethod** that defines a proper Score range.

**A‑3 — Unit soup.**
*Smell:* mixing milliseconds and seconds for the same template, or “%” and “points” for one Scale.
*Cure:* one primary Unit per template; conversions (when meaningful) are declared conceptually, not ad‑hoc.

**A‑4 — Alias leakage.**
*Smell:* “axis”, “dimension”, “point”, or “ladder” in normative identifiers or headings.
*Cure:* use only canonical tokens in normative prose; narrative labels are valid *solely* in Plain register with first‑mention mapping (A.17).

**A‑5 — Multi‑Characteristic stuffing.**
*Smell:* one template tries to carry a vector of Values for several Characteristics.
*Cure:* separate templates (one Characteristic each) and compose coordinates explicitly when needed.

**A‑6 — Evidence afterthought.**
*Smell:* Measures required to have grounds are introduced without an intelligible EvidenceStub.
*Cure:* treat the EvidenceStub as part of the measurement claim itself, not an accessory.

**A‑7 — Template mutation after Measures exist.**
*Smell:* retro-editing Characteristic, Scale, and Unit of an active template.
*Cure:* immutability of that triad post‑use; publish a successor template if the concept changes.

**A‑8 — Score‑of‑everything.**
*Smell:* collapsing heterogeneous Values into a single “points” Score without declared ScoringMethod and SCP.
*Cure:* retain the Value on its Scale; add an explicit scoring method by reference to its governing method-description episteme or FPF pattern and an explicit admissibility profile governed by the relevant FPF pattern or specification record only when there is a justified need for a Score.

