---
chunk_kind: "child"
pattern_id: "C.3"
pattern_title: "Kinds, Intent/Extent, and Typed Reasoning (Kind‑CAL)"
section_id: "C.3:5"
section_title: "Solution — Architectural Decisions (overview)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3/C.3__006_solution-architectural-decisions-overview.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "C.3 — Kinds, Intent/Extent, and Typed Reasoning (Kind‑CAL)"
  - "C.3:5 — Solution — Architectural Decisions (overview)"
line_start: 35788
line_end: 35817
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

### C.3:5 - Solution — Architectural Decisions (overview)

**C.3‑D1 — `U.Kind` is intensional and context‑local.**
Kinds name *what a claim quantifies over*. They form a partial order **`⊑`** (**SubkindOf**). *(See C.3.1.)*

**C.3‑D2 — Separate **intent** and **extent**.**
— **KindSignature(k)**: the intensional content (predicates/invariants/Standards). It carries its **own F** (C.2.3).
— **Extension(k, slice)**/**MemberOf**: which instances belong to `k` **in a given `U.ContextSlice`**. *(See C.3.2.)*

**C.3‑D3 — Kinds do **not** carry Scope.**
**Scope** lives with **claims/capabilities** (USM): a set of **Context slices** where the statement holds. Kinds carry **intent/extent** only. *(USM A.2.6 + C.3.2.)*

**C.3‑D4 — Typed reuse across Contexts is explicit.**
Use a **KindBridge** with **`CL^k`** (type‑congruence) and loss notes. Its effect is **only via R** penalties; **F/G remain unchanged**. *(See C.3.3.)*

**C.3‑D5 — Local adaptation without cloning.**
Use a **RoleMask** to bind a kind to Context‑specific constraints/aliases; promote to a **subkind** if the mask becomes stable and widely reused. *(See C.3.4.)*

**C.3‑D6 — An **informative** “abstraction tier” exists for Kinds (AT: K0…K3).**
A facet (not a Characteristic) that helps plan **ΔF/ΔR** and forecast bridge style; **AT never appears in guards**. *(See C.3.5.)*

**C.3‑D7 — Guard shapes are standardized and fail‑closed.**
Typed compatibility first (same‑Context **`⊑`** or **KindBridge**), then **Scope coverage** (USM), then **R** penalties and freshness. *(See C.3.A.)*

> **Manager’s picture — Two characteristics (keep them separate).**
> – **characteristic 1 (USM, G):** *Where* the claim holds → set of **Context slices**; composed by ∈ (membership) / ∩ (intersection) / **SpanUnion** (union across independent lines) / translate (scope mapping).
> – **characteristic 2 (Kind extent):** *Which instances* in a **given slice** belong to the kind → `MemberOf(e, k, slice)`.
> **Never “widen G” by abstract wording; widen only by ΔG with support.**


