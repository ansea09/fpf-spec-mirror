---
chunk_kind: "child"
pattern_id: "C.17"
pattern_title: "Characterising Generative Novelty & Value (Creativity‑CHR)"
section_id: "C.17:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.17/C.17__001_intro.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "C.17 — Characterising Generative Novelty & Value (Creativity‑CHR)"
  - "C.17:intro — Intro"
line_start: 44643
line_end: 44681
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.2"
  - "A.2.6"
  - "B.1"
  - "B.3"
  - "B.4"
  - "B.5.2.1"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.9"
  - "D.1-D.5"
  - "E.5"
  - "F.18"
  - "F.5"
  - "F.6"
keywords:
  - "ConstraintFit"
  - "Creativity-CHR"
  - "Diversity_P"
  - "MM-CHR measurement templates"
  - "Novelty@context"
  - "Originality"
  - "ReferenceBase"
  - "ResourceEfficiency"
  - "Surprise"
  - "Use-Value and ValueGain"
  - "evidence"
  - "portfolio composition"
---

## C.17 - Characterising Generative Novelty & Value (Creativity‑CHR)

**Status.** Mechanism specification (**CHR**) — normative where stated.
**Depends on.** A‑kernel (A.1–A.15), **A.17/A.18/A.19** characteristic-space discipline, **MM‑CHR** measurement infrastructure (C.16), **KD‑CAL** and **Sys‑CAL** for carriers and holons, **Decsn‑CAL** (utility), and declared must-constraint owners such as E.5, D.1-D.5, or service-acceptance patterns.
**Coordinates with.** **B.5.2.1 NQD** (abductive generator) for search instrumentation, **C.9 Agency Characteristic Profile** for agential capacity, B-cluster trust/assurance (B.3), Canonical Evolution Loop (B.4), Role Assignment & Enactment Cycle (Six-Step) (F.6) and Naming Discipline for U-kinds, role names, and local term sheets (F.5).
**Guard‑rails.** Obeys E‑cluster authoring rules (Notational Independence; DevOps Lexical Firewall; Unidirectional Dependency).

**What this pattern provides (exports):**

This pattern exports **Characteristics** and measurement templates **only**. It **does not** export any Γ\_\* operators, retained-set composition rules, `Front`/`Archive`/`Shortlist` heads, or selection/scalarization policies; those live in **C.18 NQD-CAL**, **C.19 E/E-LOG**, and **G.5** (or **Decsn-CAL** for decision lenses). A Context _publishes_ the measurement space and admissible policies; later choice using that space is attributed to a declared `DecisionSubject` at explicit `DecisionSubjectGranularity` under a named lens.

* **`U.CreativitySpace`** — a **CharacteristicSpace** (CHR) with named **Characteristics** and scale metadata for evaluating creative work/outcomes **inside a `U.BoundedContext`**.
* **`U.CreativityProfile`** — a vector of coordinates in `U.CreativitySpace` attached by a **`U.Evaluation`** to a specific **Outcome** (usually an `U.Episteme` produced by `U.Work`).
* **Core Characteristics (kernel nucleus; Context‑extensible):**
1. **`Novelty@context`** — distance from a **`ReferenceBase`** in the current Context/time window; ∈ \[0, 1].
2. **`Use‑Value`** *(alias: `ValueGain`)* — measured or predicted improvement against a **declared objective**; interval/ratio scale per Context.
3. **`Surprise`** — negative log‑likelihood under a **GenerativePrior**; bits or nats.
4. **`ConstraintFit`** — degree of **must‑constraint** satisfaction under the declared constraint owner or service-acceptance policy; ∈ \[0, 1].
5. **Diversity_P (declared retained-set / portfolio-level)** — coverage/dispersion (set-level). **Illumination** is a **report-metric over Diversity_P** (coverage/QD-score summaries). It is **report-only** and **never** part of the primary dominance test.
6. **`AttributionIntegrity`** — provenance/licensing discipline for lawful, transparent recombination; ∈ \[0, 1].
7. **`FamilyCoverage`** — (count, polarity ↑, scope=declared retained set or portfolio, unit=families, provenance: F1‑Card)
8. **`MinInterFamilyDistance`** — (ratio [0,1] or metric units, polarity ↑, scope=declared retained set or portfolio, DistanceDef@F1‑Card)
9. **`AliasRisk`** —  (ratio [0,1], polarity ↓, diagnostic; drop if dSig ≥3/5 characteristics collide)
10. **`U.DomainDiversitySignature (dSig)`** — 5‑tuple over discrete characteristics **[Sector, Function, Archetype, Regime, MetricFamily]**  attached to each `U.BoundedContext`. Used for **Near‑Duplicate** diagnostics and `AliasRisk`. Policy: flag as Near‑Duplicate when ≥3 characteristics match; see F.1 invariants and SCR‑F1‑S08..S09.
11. **Note (AliasRisk binding).** `AliasRisk` MAY be computed using `dSig` collision diagnostics; a Context MUST declare the collision rule and policy id in DescriptorMap provenance when AliasRisk is reported.

* **Supporting types (linking points):**

  * **`U.ReferenceBase`** — the domain‑local corpus (by Context & time window) used to compute `Novelty@context`.
  * **`U.SimilarityKernel`** — a declared similarity metric class for the Context (text/image/design/code/etc.), with invariance notes.
  * **`U.GenerativePrior`** — a predictive model over the Context’s artifacts/behaviours used to compute `Surprise`.
  * **`U.CreativeEvaluation`** — a specialisation of `U.Evaluation` that yields a `U.CreativityProfile` and the Evidence Graph Ref.
  * **`EffortCost`** *(advisory)* — resource outlay to achieve the outcome; from WorkLedger (Resrc‑CAL). *(For normalization and planning; not itself “creativity.”)*

* **Operators (first tranche):** `composeProfiles` (set → declared retained-set profile), `dominates` (partial order in space), `frontier` (Pareto set), `normaliseByEffort`. *(Formal laws introduced in Quarter 2.)*
* **Relations (informative; not exported):** dominance relation (partial order in the space), frontier predicate (Pareto set), retained-set composition view. *C.17 exports no operators and does not mint public set-result family heads; these are mathematical relations only.*
*
> **Scope note.** This pattern **does not** define who is “a creative person.” It characterises **creative outcomes and episodes** as **observed in Work** and **expressed as Epistemes**. Agency (capacity to originate) is measured through **C.9 Agency Characteristic Profile**; here we measure **what came out** and **how it scores** against stated goals and references.  A **Context publishes** the measurement space and admissible policies; later choice is attributed to a declared `DecisionSubject` at explicit `DecisionSubjectGranularity`, using a named lens within that space. CHR exports **no Γ‑operators** and **no team workflow rules**.

