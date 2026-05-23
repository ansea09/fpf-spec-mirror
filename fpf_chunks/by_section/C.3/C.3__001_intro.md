---
chunk_kind: "child"
pattern_id: "C.3"
pattern_title: "Kinds, Intent/Extent, and Typed Reasoning (Kind‑CAL)"
section_id: "C.3:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3/C.3__001_intro.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "C.3 — Kinds, Intent/Extent, and Typed Reasoning (Kind‑CAL)"
  - "C.3:intro — Intro"
line_start: 35718
line_end: 35746
dependencies:
  - "A.1"
  - "A.2.6"
keywords:
  - "classification"
  - "extension"
  - "intension"
  - "kind"
  - "subkind"
  - "type"
  - "typed reasoning"
  - "vocabulary"
---

## C.3 - Kinds, Intent/Extent, and Typed Reasoning (Kind‑CAL)

> **One‑line summary.** Establishes **`U.Kind`** as the **minimal, context‑local intensional carrier** of “what a statement is about,” separates **intent** (KindSignature + its own **F**) from **extent** (*which* instances belong to the kind **in a given Context slice**), and situates **typed reasoning** alongside **USM Scope (G)** and **F–G–R** without conflation. Details of the core objects and operations live in **C.3.1–C.3.5**; guard shapes are standardized in **C.3.A**.

**Status.** Normative in **Part C**. Identifier **C.3**. This pattern lays the **architectural invariant** and manager‑level guidance. The **mechanics** are defined by its child patterns.

**Readers.** Engineering managers, architects, and assurance leads who must reason about *typed claims* across Contexts without mixing up **describedEntity** (Kinds), **applicability** (**G**), and **assurance** (**R**).

**Depends on.**
— **A.2.6 USM** (Context slices & Scopes): **`U.ClaimScope` = G**, **`U.WorkScope`**, ∈/∩/**SpanUnion**/translate, **Γ\_time** policy, Bridges + **CL** (scope).
— **C.2.2 F–G–R**: weakest‑link composition; penalties to **R** for Cross‑context congruence (CL).
— **C.2.3 Unified Formality F**: F0…F9 as an **ordinal Characteristic** (expression rigor).

**Sub‑patterns (normative unless noted).**
— **C.3.1** - `U.Kind` & `U.SubkindOf` (partial order).
— **C.3.2** - `KindSignature` (**intent**, with **F**) & `Extension/MemberOf` (**extent** in a slice).
— **C.3.3** - **KindBridge** & **`CL^k`** (type‑congruence; penalties route to **R**).
— **C.3.4** - **RoleMask** (context‑local adaptation without cloning kinds).
— **C.3.5** - **KindAT** (K0…K3, **informative facet**, not a Characteristic).
— **C.3.A** - **Typed Guard Macros** (annex): admit/compose, masks, Cross‑context reuse; AT is **forbidden** in guards.

**Deprecations.**
— “**Generality ladder**” for **G**; **G is Scope** only (set‑valued over `U.ContextSlice`).
— Any “**Kind scope**” characteristic (Kinds carry **intent/extent**, not Scope).
— **Mark as legacy** any uses of **‘validity’ as a Characteristic** or **‘operation’ as a Scope‑like Characteristic**; **redirect** to **`U.ClaimScope`** / **`U.WorkScope`** (A.2.6) for applicability. Editors SHOULD add glossary redirects in Part E.

**Editorial note (cut‑over).** Content formerly in C.3 that defined guard shapes, decision trees, and macro anti‑patterns now resides in **C.3.A**. Membership **evaluation obligations** live in **C.3.2** with `MemberOf`.


