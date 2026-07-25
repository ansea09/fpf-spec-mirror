---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "RoleMask — Contextual Adaptation of Kinds (without cloning)"
section_id: "C.3.4:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__001_intro.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "C.3.4 — RoleMask — Contextual Adaptation of Kinds (without cloning)"
  - "C.3.4:intro — Intro"
line_start: 44524
line_end: 44543
dependencies:
  - "C.2.1"
  - "C.3.1"
  - "C.3.2"
  - "C.3.3"
  - "C.3.A"
keywords:
  - "RoleMask declaration episteme"
  - "candidate-feature constraint"
  - "masked judgment"
  - "stable-refinement review"
  - "vocabulary binding"
---

## C.3.4 - RoleMask — Contextual Adaptation of Kinds (without cloning)

> **One-line summary.** Defines **`RoleMask`** as a C.2.1 declaration episteme for one named local use of an exact base kind. Its content pins the base `KindSignature` edition, additional candidate-feature constraints, vocabulary bindings, intended guard use, and definedness. Applying it yields an exact `true`/`false`/`unknown` masked judgment; it creates neither a new kind nor a direct membership relation. Cross-context use requires an obtaining KindBridge relation, a target declaration, and a separate MaskAdapter declaration when constraints or bindings change. Formality remains on declaration epistemes; guard refusal remains separate from `unknown`.

**Status.** Normative in **Part C**. Identifier **C.3.4**.
**Audience.** Engineering managers, architects, reviewers, editors.

**Depends on.**

* **C.3.1 — U.Kind & SubkindOf (Core):** kinds are intensional; `⊑` is a partial order; kinds **carry no Scope**.
* **C.3.2 — Kind intent, judgment, and extension:** `KindSignature` is a declaration episteme; the exact four-input judgment is three-valued; any extension is a pinned-edition representation of true candidates.
* **C.3.3 — KindBridge & CL^k:** Cross‑context kind mapping; `CL^k` penalties → **R** only.
* **A.2.6 — USM (Context slices & Scopes):** Claim/Work scope (**G**) over `U.ContextSlice`; bridges and **CL** for scope.
* **C.2.2 — F–G–R; C.2.3 — U.Formality (F).**

**Non‑goals.**
— No repository/notation mandates; conceptual only.
— RoleMask is **not** a governance tier, data policy, or “mini‑type system.”
— RoleMask does **not** redefine Scope; context conditions belong to **USM**.

