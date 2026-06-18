---
chunk_kind: "child"
pattern_id: "A.2.6"
pattern_title: "Unified Scope Mechanism (USM): Context Slices & Scopes"
section_id: "A.2.6:section-001"
section_title: "E.24.UK settlement"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.6/A.2.6__002_e-24-uk-settlement.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "A.2.6 — Unified Scope Mechanism (USM): Context Slices & Scopes"
  - "A.2.6:section-001 — E.24.UK settlement"
line_start: 3944
line_end: 3965
dependencies:
  - "A.1.1"
  - "A.2.2"
  - "A.2.3"
  - "B.3"
keywords:
  - "& guard style)"
  - "ClaimScope (G)"
  - "WorkScope"
  - "applicability"
  - "scope"
  - "set-valued"
---

### E.24.UK settlement

`U.ContextSlice` and `U.Scope` are retained as root durable USM values under this scope settlement. `U.ClaimScope`, `U.WorkScope`, and `U.PublicationScope` are retained as C.3-governed scope specializations under `U.Scope`, not as independent root ontics. `ContextSliceSet` is the set-valued scope value over addressable `U.ContextSlice`s, not an independent root kind. `GammaTimePolicy`, work-measure target sets, qualification-window policies, formality thresholds, detail values, abstraction-tier values, scope profiles, coverage metrics, guards, reports, and publication views remain policy values, characteristic values, non-U records, lenses, guard facets, or publication forms unless a direct governing pattern admits them. Dotted forms such as `U.Mechanism.Intension` name the intension slot/form governed by `U.Mechanism` and A.6.1; they do not admit a separate structural U-kind.

> **One-line summary.** Introduces a single, context-local **scope mechanism** for all holons: **`U.ContextSlice`** (where we reason and measure) and a family of **set-valued scope types** (**USM scope objects, `U.Scope`**), specialized as **`U.ClaimScope`** for epistemes (**G** in **F–G–R**), **`U.WorkScope`** for system capabilities, and **`U.PublicationScope`** for publication carriers; with one algebra (∩ / SpanUnion / translate / widen / narrow / refit) and uniform Cross-context handling (Bridge + CL).

**Replaces and deprecates.**
This pattern **supersedes** the scattered use of labels *applicability*, *envelope*, *generality*, *universality* and *capability envelope* where they tried to stand in for the one scope mechanism. From now on:

* For epistemes, the only **scope type** is **`U.ClaimScope`** (nick **G** in F–G–R).
* For system capabilities, the only **scope type** is **`U.WorkScope`**.
* For publication carriers (views, cards, and lanes), the only **scope type** is **`U.PublicationScope`**.
* The abstract architectural notion is **`U.Scope`** — a **set-valued USM object** over `ContextSliceSet` with its own algebra (∩ / SpanUnion / translate / widen / narrow / refit); it is **not** a `U.Characteristic` and MUST NOT appear in any `CharacteristicSpace`.

Older source words (*applicability*, *envelope*, *generality*, and *capability envelope*) MAY appear **only** as explanatory aliases in non-normative notes.

**Cross‑references.**
— **C.2.3** (Unified Formality **F**) and **C.2.2** (F–G–R): this pattern **defines G** as `U.ClaimScope`.
— **A.2.2** (Capabilities): capability gating now **SHALL** use `U.WorkScope`.
— **Part B** (Bridges & CL): Cross‑context transfers **MUST** declare a Bridge with **CL**; CL affects **R**, not **F/G**.
— **Part E** (Publication discipline; e.g., **E.17 MVPK**): publication views, cards, and lanes MAY declare `U.PublicationScope` to bound **where** a publication is admissible; `U.PublicationScope` MUST NOT widen the underlying `U.ClaimScope`/`U.WorkScope`. (USM supplies the scope calculus; Part E supplies publication discipline.)

