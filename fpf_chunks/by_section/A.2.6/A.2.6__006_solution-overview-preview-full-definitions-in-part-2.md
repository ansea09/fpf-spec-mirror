---
chunk_kind: "child"
pattern_id: "A.2.6"
pattern_title: "Unified Scope Mechanism (USM): Context Slices & Scopes"
section_id: "A.2.6:5"
section_title: "Solution — Overview (preview; full definitions in Part 2)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.6/A.2.6__006_solution-overview-preview-full-definitions-in-part-2.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "A.2.6 — Unified Scope Mechanism (USM): Context Slices & Scopes"
  - "A.2.6:5 — Solution — Overview (preview; full definitions in Part 2)"
line_start: 4087
line_end: 4102
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

### A.2.6:5 - Solution — Overview (preview; full definitions in Part 2)

**USM** introduces:

* **`U.ContextSlice`** — an addressable **slice of a bounded context** (terminology, parameter ranges, versions/Standards, and a mandatory **Γ\_time** selector). All scope checks are performed **on slices**.
* **`U.Scope`** — the abstract **set‑valued scope object** over `U.ContextSlice`.
* **Specializations:**
  **`U.ClaimScope`** (nick **G**) on `U.Episteme` (“**where the claim holds**”),
  **`U.WorkScope`** on `U.Capability` (“**where the capability can deliver Work at declared measures within qualification windows**”), and
  **`U.PublicationScope`** on publication carriers (“**where the publication surface is admissible**”).
* **One algebra:** serial **intersection**, parallel **SpanUnion** (only where independently supported), **translate** via Bridge (CL affects **R**, not **F/G**), and **widen / narrow / refit** operations for scope evolution.

**Lexical commitments (normative):**
— In normative text and guards, use **Claim scope (G)**, **Work scope**, and **Publication scope**.
— Do **not** name the characteristic “applicability/envelope/generality/capability envelope/**publication applicability**/validity.” Those words are permitted only as explanatory aliases in notes.

