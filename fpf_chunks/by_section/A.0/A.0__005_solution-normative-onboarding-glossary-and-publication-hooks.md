---
chunk_kind: "child"
pattern_id: "A.0"
pattern_title: "Onboarding Glossary (NQD & E/E‑LOG)"
section_id: "A.0:4"
section_title: "Solution - Normative onboarding glossary and publication hooks"
source_path: "FPF-Spec.md"
output_path: "by_section/A.0/A.0__005_solution-normative-onboarding-glossary-and-publication-hooks.md"
commit_sha: "ce6fcc3b99b10e42f4b258f84091355b2ee5ab24"
heading_path:
  - "A.0 — Onboarding Glossary (NQD & E/E‑LOG)"
  - "A.0:4 — Solution - Normative onboarding glossary and publication hooks"
line_start: 1319
line_end: 1350
dependencies:
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.19.SOURCE-SET-SPACE-SUBSTRATE"
  - "A.5"
  - "B.5"
  - "B.5.2.1"
  - "C.17"
  - "C.17-C.19"
  - "C.19"
  - "E.10"
  - "E.2"
  - "E.7"
  - "E.8"
  - "F.17"
  - "G.12"
  - "G.5"
  - "G.9"
  - "G.9-G.12"
keywords:
  - "& queries. novelty"
  - "BLP"
  - "CL^plane"
  - "DeclaredSubstrateInterpretiveView"
  - "OutcomeSpaceRef"
  - "ParetoOnly default"
  - "ReferencePlane"
  - "SearchSpaceRef"
  - "TypedSetViews"
  - "comparability"
  - "declared set result"
  - "explore/exploit (E/E-LOG)"
  - "explore/exploit (E/E‑LOG)"
  - "illumination map (report‑only telemetry)"
  - "novelty"
  - "parity run"
  - "quality-diversity (NQD)"
  - "quality‑diversity (NQD)"
  - "scale-probe"
  - "typed portfolio publication"
---

### A.0:4 - Solution - Normative onboarding glossary and publication hooks

#### 4.1 Plain one‑liners (normative on‑ramp; formal anchors in C.17–C.19)

| Term                      | Plain definition (on‑ramp)                                                                                                                                   | See        |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **Novelty (N)**           | How unlike the known set a candidate is in your declared **CharacteristicSpace**. **Compute admissibly** (declared `DescriptorMapRef` + `DistanceDefRef`; no ad-hoc normalisation). | C.17, C.18 |
| **Use‑Value (U / ValueGain)** | What the candidate helps you achieve now under your **CG‑Frame**; tie to acceptance/tests; **publish units, scale kind, polarity, ReferencePlane**.                   | C.17, C.18 |
| **Constraint‑Fit (C)**    | *Satisfies must‑constraints (Resource/Risk/Ethics)*; legality via **CG‑Spec**; **unknowns propagate** (never coerce to zero).                                | C.18, G.4  |
| **Diversity_P (declared retained set)** | Coverage or dispersion of the declared retained set under a named measurement policy; declare **ReferencePlane**. Its change on adding one candidate is **DeltaDiversity_P**. | C.17, C.18 |
| **E/E‑LOG**               | *Named, versioned **explore↔exploit** policy*; governs when to widen space vs refine candidates; **policy‑id is published**.                                   | C.19       |
| **ReferencePlane**        | *Where a value lives:* **world** (system), **concept** (definition), **episteme** (about a claim). **Plane‑crossings add CL^plane** (penalties to **R only**); cite policy‑id. | F.9, G.6   |
| **Scale Variables (S)**  | *The **monotone knobs** along which improvement is expected* (e.g., parameterisation breadth, data exposure, iteration budget, resolution). **Declare S** for any generator/selector claimed to scale. | C.18.1       |
| **Scale Elasticity (χ)** | *Qualitative class of improvement when moving along S* (e.g., **rising**, **knee**, **flat** in the declared window). Used as a **selection lens**; numeric laws live in domain contexts.              | C.18.1       |
| **BLP (Bitter‑Lesson Preference)** | A preference supported by a comparable, uncertainty-qualified scale comparison; begin with a **cheap scale-claim probe**. **No scale claim yet** or **no scale-based preference** are valid results. A local generality policy is a separate declared basis. | C.19.1, C.24 |
| **Iso‑Scale Parity**  | *Fair comparison across candidates at equalised **scale budgets** along S*; may also include **scale‑probes** (two points) to test elasticity.                                                         | G.9, C.18.1  |

*(Registers & forbidden forms per **LEX‑BUNDLE**; avoid “axis/dimension/validity/process” for measurement and scope.)*

#### 4.2 Publication & telemetry duties (where these terms **show up**)

1. **UTS surface (Part F).** When a **UTS row describes a generator, selector, typed portfolio publication, or set-return publication surface**, it **MUST** surface **N, U, C, Diversity_P, E/E‑LOG `policy‑id`, `ReferencePlane`**, with **units, scale, and polarity** typed under **MM‑CHR** and **CG‑Spec**, and admissible references to `DescriptorMapRef` and `DistanceDefRef`. *(Row schema: F.17; shipping via G.10.)*
2. **Parity & edition pins (Part G).** When QD/OEE is in scope, **pin** `DescriptorMapRef.edition` and `DistanceDefRef.edition` (and, where applicable, `CharacteristicSpaceRef.edition`, `TransferRulesRef.edition`) and record `policy‑id` + `PathSliceId`. Treat **illumination/coverage as report‑only telemetry**; publish an **Illumination Map** where G‑kit mandates parity records. **Declare S** (Scale Variables) and run at least one **scale‑probe** (two points along S) when claiming **scale‑amenability**. **Dominance policy defaults to `ParetoOnly`;** including illumination in dominance **MUST** cite a CAL policy‑id.
3. **Tell‑Show‑Show (E.7/E.8).** Any architectural pattern that claims generative behaviour **MUST** embed **both** a **U.System** and a **U.Episteme** illustration using this glossary (manager‑first didactics).

#### 4.3 Minimal first-day construction
1) Declare **CG‑Frame** (what “quality” means; admissible units and scales) and **ReferencePlane**.
2) Pick 2–4 **Q components** + a simple **DescriptorMap** (≥2 dims) for N/D; publish **editions**.
3) Choose an **E/E‑LOG policy** (explore↔exploit budget); record **policy‑id**.
4) Apply **G.5** selection/dispatch with parity pins. Keep any consumed `Front` or `Archive` identified as the source set. For a set outcome, return `Shortlist` or `RankedShortlist` for retained alternatives, or `JointUseSet` when all named members are included for one named use. Return a handoff, abstain, or escalation when that is the actual G.5 outcome.
5) Keep the actual **G.5 outcome**'s required content and basis pins. **Publish that result only when the receiving use calls for publication**, with its applicable **PathIds/PathSliceId**. Add a **UTS row** for a named governed value only when **F.17**'s independent naming and reuse conditions hold; otherwise reuse its existing designation. Follow the outcome's continuation or stop. An **Illumination Map** remains **report‑only telemetry** by default.

