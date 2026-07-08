---
chunk_kind: "child"
pattern_id: "A.2.6"
pattern_title: "Unified Scope Mechanism (USM): Context Slices & Scopes"
section_id: "A.2.6:0.1"
section_title: "Kind Settlement"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.6/A.2.6__002_kind-settlement.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "A.2.6 — Unified Scope Mechanism (USM): Context Slices & Scopes"
  - "A.2.6:0.1 — Kind Settlement"
line_start: 4137
line_end: 4163
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

### A.2.6:0.1 - Kind Settlement

`U.ContextSlice` and `U.Scope` are the durable USM values for scope work. `U.ClaimScope`, `U.WorkScope`, and `U.PublicationScope` are C.3-governed scope specializations under `U.Scope`, not independent root ontics. `ContextSliceSet` is the set-valued scope value over addressable `U.ContextSlice`s, not an independent root kind. `GammaTimePolicy`, work-measure target sets, qualification-window policies, formality thresholds, detail values, abstraction-tier values, scope profiles, coverage metrics, guards, reports, and publication views remain policy values, characteristic values, non-U records, lenses, guard facets, or publication forms unless a direct governing pattern admits them. Dotted forms such as `U.Mechanism.Intension` name the intension slot or intension form governed by `U.Mechanism` and A.6.1; they do not admit a separate structural U-kind.

> **One-line summary.** Introduces a single, context-local **scope mechanism** for all holons: **`U.ContextSlice`** (where we reason and measure) and a family of **set-valued scope types** (**USM scope objects, `U.Scope`**), specialized as **`U.ClaimScope`** for epistemes (**G** in **F–G–R**), **`U.WorkScope`** for system capabilities, and **`U.PublicationScope`** for publication carriers; with one algebra (intersection, SpanUnion, translate, widen, narrow, and refit) and uniform Cross-context handling through Bridge and CL.

**Use this pattern when** a project must decide where a claim holds, where a capability can deliver work, or where a publication surface is admissible across concrete context slices.
**What goes wrong if missed.** Applicability, envelope, generality, validity, capability envelope, and publication applicability start acting like separate mechanisms; teams widen scope by wording, compose unsupported slices, or move claims across contexts without Bridge and CL loss.

**What this buys.** Scope becomes one set-valued mechanism over addressable `U.ContextSlice`s, with carrier-specific specializations for claims, work, and publications and one algebra for intersection, SpanUnion, translation, widening, narrowing, and refit.

**Vocabulary boundary.** Use these scope names in live FPF wording:


* For epistemes, the only **scope type** is **`U.ClaimScope`** (nick **G** in F–G–R).
* For system capabilities, the only **scope type** is **`U.WorkScope`**.
* For publication carriers (views, cards, and lanes), the only **scope type** is **`U.PublicationScope`**.
* The abstract architectural notion is **`U.Scope`** — a **set-valued USM object** over `ContextSliceSet` with its own algebra: intersection, SpanUnion, translate, widen, narrow, and refit. It is **not** a `U.Characteristic` and MUST NOT appear in any `CharacteristicSpace`.

Source words such as *applicability*, *envelope*, *generality*, and *capability envelope* may appear only as explanatory aliases in non-normative notes.

**Cross‑references.**
— **C.2.3** (Unified Formality **F**) and **C.2.2** (F–G–R): this pattern **defines G** as `U.ClaimScope`.
— **A.2.2** (Capabilities): capability gating now **SHALL** use `U.WorkScope`.
— **Part B** (Bridges and CL): Cross‑context transfers **MUST** declare a Bridge with **CL**; CL affects **R**, not **F/G**.
— **Part E** (Publication discipline; e.g., **E.17 MVPK**): publication views, cards, and lanes MAY declare `U.PublicationScope` to bound **where** a publication is admissible; `U.PublicationScope` MUST NOT widen the underlying `U.ClaimScope`/`U.WorkScope`. (USM supplies the scope calculus; Part E supplies publication discipline.)

