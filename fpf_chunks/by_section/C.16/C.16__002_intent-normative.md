---
chunk_kind: "child"
pattern_id: "C.16"
pattern_title: "Measurement & Metrics Characterization (MM‑CHR)"
section_id: "C.16:1"
section_title: "Intent (Normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16/C.16__002_intent-normative.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "C.16 — Measurement & Metrics Characterization (MM‑CHR)"
  - "C.16:1 — Intent (Normative)"
line_start: 42799
line_end: 42828
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

### C.16:1 - Intent (Normative)

**Name.** *Measurement & Metrics Characterization (MM‑CHR).* This is a user‑oriented name: in user‑facing narrative we may say *metrics*; in **Tech** register we speak **Characteristic, Scale, Level, Coordinate, Value, Score, Unit, and ScoringMethod**; in **Formal** register we use `U.DHCMethod(Ref)`, `U.Measure`, `U.Unit`, and `U.EvidenceStub`.
**Intent.** Provide a **transdisciplinary substrate for measurement** that any FPF pattern can rely on: a small, stable set of measurement-definition constructs and relations—**`U.DHCMethodRef`**, **`U.Measure`**, **`U.Unit`**, **`U.EvidenceStub`**—disciplined by **CSLC** (*Characteristic, Scale, Level, Coordinate*) so that every recorded value is **interpretable**, and any claim of “comparability” is **auditable** (physics lab time‑of‑flight, figure‑skating judging, architectural modularity, etc.). **C.16** does **not** re‑define **Characteristic** (A.17) nor the CSLC kernel Standard (A.18); instead, it **exports** the measurement substrate that *binds* an FPF pattern’s measurable notions to **one Characteristic and one Scale** and frames a **conceptual link to evidence**. This characterization is **notation‑neutral**, **tool‑agnostic**, and **open‑ended** (no “lifecycle” narrative; state admission and refresh proceed through `RoleStateRelation@BoundedContext` checklists when a role state is current).

**E.24.UK settlement.** C.16 retains a small measurement-value family, not four independent root ontics. `U.DHCMethod` is the durable measurement-template value for a declared Characteristic and Scale reading. `U.Measure` is a dependent durable reading claim that references one `U.DHCMethodRef`. `U.Unit` is a dependent scale or quantity-kind value used when the declared Scale requires unit semantics. `U.EvidenceStub` is a dependent measurement-ground locator attached to a Measure when the template requires grounds. None of these names admits a free-standing `U.Metric`, score-table, dashboard, evidence carrier, storage record, or comparison mechanism; broader scoring, normalization, selection, causal, evidence, assurance, or gate uses stay with their governing patterns.

**One‑minute mental model (didactic; non‑normative).**
* **Template** (`U.DHCMethod`) says what a value *means*: the **Characteristic**, **Scale** (and **Unit** when applicable), plus **polarity** and applicability.
* **Measure claim** (`U.Measure`) says what was claimed about a **subject**: a value on that Scale, with a **time stance** and (when required) an **EvidenceStub**.
* **Direct comparability** is conservative: *same template*; everything else requires a **named and cited** comparability basis governed by the relevant FPF pattern, Bridge, method description, or specification record.

**Boundary to neighboring governing patterns and specification records.** C.16 governs measurement templates, readings, score meanings, scale admissibility, direct comparability, and evidence-stub adequacy. It does **not** govern (i) characterization mechanisms such as normalization, indicatorization, scoring, comparison, or selection, (ii) normalization and equivalence notions such as method tokens, invariant-value notions, or equivalence relations, (iii) claim-use policies such as comparability modes and admission gates, or (iv) suite protocol obligations. Those meanings are governed by their FPF patterns or specification records, such as CN-Spec, CG-Spec, and the CHR mechanism-governing patterns. C.16 may **cite** those patterns or records when motivating evidence or interpretability, but MUST NOT introduce or restate their terminology or laws.

**Use this when.** Use this pattern when a value, score, rating, metric label, QL probe output, dashboard reading, or comparison is being treated as meaningful without a visible characteristic, scale, unit, polarity, comparability basis, or evidence pointer. The action is to rebuild the measurement claim as a typed reading: name the subject, bind one characteristic to one scale, state the coordinate or level, declare unit and polarity when they matter, attach the evidence stub, and keep comparison or scoring claims with broader scope, higher evidence requirement, or release or admission use with the governing pattern or specification record that governs that comparison or scoring claim.

**What goes wrong if missed.** Convenient numbers become free-floating facts: dashboards imply unsupported comparison, scores hide scale changes, ordinal labels are averaged as interval quantities, and measurement outputs are reused as causal, assurance, or admission claims without the pattern that governs those uses.

**What this buys.** A measurement reading that a reader can interpret, compare, and reuse only within its declared measurement basis: subject, characteristic, scale, coordinate or level, unit, polarity, evidence stub, and any governing comparability or scoring basis.

**Not this pattern when.** Not this pattern when the live question is naming a characteristic (`A.17`), scale operations (`A.18`), measurement wording repair before the measurement object is recoverable (`C.16.P`), causal use (`C.28`), assurance (`B.3`), or mathematical-lens adequacy (`C.29`).

Thin precision-restoration pointer: if the current issue is still whether wording such as *metric*, *measure*, *score*, *axis*, *dimension*, *level*, *coordinate*, *quality*, or *stronger/weaker value* names a characteristic, scale, coordinate, score, unit, scoring method, quality-term repair, or application of the pattern governing the recovered claim, use `C.16.P` first. Do not copy the `C.16.P` trigger table here; C.16 resumes after the measurement or characteristic construction is recoverable.
Useful output: a measurement claim that a reader can interpret and compare only within its declared measurement basis, without turning a convenient number into a free-floating fact.

Metric admissibility does not make causal use admissible. If a measured value, score, dashboard reading, or metric disparity reaches `CausalUseActivation` by being used to claim effect, intervention success, causal fairness, policy optimality, counterfactual comparison, or causal method superiority, keep the measurement repair in `C.16` and carry the causal-use question, causal-ladder rung, estimand, support basis, support verdict, admissible causal use, and inadmissible causal use in `C.28`.

**Outcomes.**
(1) A uniform way for FPF patterns to *declare* what is measured and *read* what has been measured; (2) explicit **Characteristic binding** and **Scale typing** per CSLC; (3) principled **comparability** and **polarity** (declared at the template level); (4) **traceability** via conceptual evidence stubs; (5) seamless alignment with cross‑domain quantity notions (ISO 80000, ISO/IEC 25024, QUDT, SOSA/SSN, Verspoor) through Unification rows (Part F).

