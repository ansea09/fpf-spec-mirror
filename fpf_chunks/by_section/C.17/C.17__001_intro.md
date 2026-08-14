---
chunk_kind: "child"
pattern_id: "C.17"
pattern_title: "Characterising Generative Novelty & Value (Creativity‑CHR)"
section_id: "C.17:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.17/C.17__001_intro.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "C.17 — Characterising Generative Novelty & Value (Creativity‑CHR)"
  - "C.17:intro — Intro"
line_start: 48780
line_end: 48820
dependencies:
  - "A.1"
  - "A.10"
  - "A.13"
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
**Depends on.** A‑kernel (A.1–A.15), **A.17/A.18/A.19** characteristic-space discipline, **MM‑CHR** measurement infrastructure (C.16), **KD‑CAL** and **Sys‑CAL** for carriers and holons, **Decsn‑CAL** (utility), and declared must-constraint predicates and their source patterns, such as E.5, D.1-D.5, or service-acceptance patterns.
**Coordinates with.** **B.5.2.1 NQD** (abductive generator) for search instrumentation, A.13 for agential participation and the A.17/A.18/A.19/C.16/A.10 stack for measured characteristics and evidence, planned **C.9 Agency Characteristic Profile** only as future consolidation, B-cluster trust and assurance (B.3), Canonical Evolution Loop (B.4), SystemRoleAssignment and Performed-Work Attribution Check (F.6), and Naming Discipline for U-kind Names and SystemRoleKindDescription Labels (F.5).
**Guard‑rails.** Obeys E‑cluster authoring rules (Notational Independence; DevOps Lexical Firewall; Unidirectional Dependency).

**What this pattern provides (exports):**

This pattern exports **Characteristics** and measurement templates **only**. It **does not** export any Γ\_\* operators, retained-set composition rules, `Front`/`Archive`/`Shortlist` heads, or selection/scalarization policies; those live in **C.18 NQD-CAL**, **C.19 E/E-LOG**, and **G.5** (or **Decsn-CAL** for decision lenses). A Context _publishes_ the measurement space and admissible policies; later choice using that space is attributed to a declared `DecisionSubject` at explicit `DecisionSubjectGranularity` under a named lens.

* **`U.CreativitySpace`** — a **CharacteristicSpace** (CHR) with named **Characteristics** and scale metadata for evaluating creative work/outcomes **inside a `U.BoundedContext`**.
* **`U.CreativityProfile`** — a vector of coordinates in `U.CreativitySpace` attached by a **`U.Evaluation`** to a specific **Outcome** (usually an `U.Episteme` produced by `U.Work`).
* **Core Characteristics (kernel nucleus; Context-extensible):**
1. **`Novelty@context`** — distance from a **`ReferenceBase`** in the current Context/time window; ∈ \[0, 1].
2. **`Use-Value`** *(alias: `ValueGain`)* — measured or predicted improvement against a **declared objective**; interval/ratio scale per Context.
3. **`Surprise`** — negative log-likelihood under a **GenerativePrior**; bits or nats.
4. **`ConstraintFit`** — degree of **must-constraint** satisfaction under the declared constraint predicate and source or service-acceptance policy; ∈ \[0, 1].
5. **Diversity_P (declared retained-set / portfolio-level)** — coverage/dispersion (set-level). **Illumination** is a **report-metric over Diversity_P** (coverage/QD-score summaries). It is **report-only** and **never** part of the primary dominance test.
6. **`AttributionIntegrity`** — provenance/licensing discipline for lawful, transparent recombination; ∈ \[0, 1].

* **Optional local retained-set Characteristics:**
7. **`FamilyCoverage`** — count or other declared coverage reading over one retained set, under a named `RetainedSetMeasurementPolicyRef` and `ScaleRef`.
8. **`MinInterFamilyDistance`** — minimum inter-family distance for one retained set, under a named `DescriptorMapRef.edition`, `DistanceDefRef.edition`, measurement policy, and scale.
9. **`AliasRisk`** — a context-local near-duplicate or alias diagnostic under a named `CollisionPolicyRef`, measurement policy, and scale.
10. **`DescriptorVector`** — an optional local descriptor record used by the named measurement policy; its dimensions and taxonomy or corpus edition are explicit.
11. **Admission boundary.** These Characteristics describe one retained set or portfolio. They do not admit or exclude sources, widen a method's applicability, establish universality, or replace the selection rule that produced the set.

* **Supporting types (linking points):**

  * **`U.ReferenceBase`** — the domain‑local corpus (by Context & time window) used to compute `Novelty@context`.
  * **`U.SimilarityKernel`** — a declared similarity metric class for the Context (text/image/design/code/etc.), with invariance notes.
  * **`U.GenerativePrior`** — a predictive model over the Context’s artifacts/behaviours used to compute `Surprise`.
  * **`U.CreativeEvaluation`** — a specialisation of `U.Evaluation` that yields a `U.CreativityProfile` and the Evidence Graph Ref.
  * **`EffortCost`** *(advisory)* — resource outlay to achieve the outcome; from a work/resource ledger whose dated Work, aggregation, measurement, and provenance follow **A.15.1**, **B.1.6**, **C.16**, and **A.10**; planned values remain **A.15.2** WorkPlan content. *(For normalization and planning; not itself “creativity.”)*

* **Operators (first tranche):** `composeProfiles` (set → declared retained-set profile), `dominates` (partial order in space), `frontier` (Pareto set), `normaliseByEffort`. *(Formal laws introduced in Quarter 2.)*
* **Relations (informative; not exported):** dominance relation (partial order in the space), frontier predicate (Pareto set), retained-set composition view. *C.17 exports no operators and does not mint public set-result family heads; these are mathematical relations only.*
*
> **Scope note.** This pattern **does not** define who is “a creative person.” It characterises **creative outcomes and episodes** as **observed in Work** and **expressed as Epistemes**. Agency (capacity to originate) is identified under A.13 and measured through A.17/A.18/A.19/C.16/A.10; planned **C.9 Agency Characteristic Profile** may later consolidate that profile but supplies no current governing force. Here we measure **what came out** and **how it scores** against stated goals and references. A **Context publishes** the measurement space and admissible policies; later choice is attributed to a declared `DecisionSubject` at explicit `DecisionSubjectGranularity`, using a named lens within that space. CHR exports **no Γ‑operators** and **no team workflow rules**.

