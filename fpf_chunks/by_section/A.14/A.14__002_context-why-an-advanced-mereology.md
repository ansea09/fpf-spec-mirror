---
chunk_kind: "child"
pattern_id: "A.14"
pattern_title: "Advanced Mereology: Components, Portions, Aspects & Phases"
section_id: "A.14:1"
section_title: "Context — why an advanced mereology?"
source_path: "FPF-Spec.md"
output_path: "by_section/A.14/A.14__002_context-why-an-advanced-mereology.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "A.14 — Advanced Mereology: Components, Portions, Aspects & Phases"
  - "A.14:1 — Context — why an advanced mereology?"
line_start: 19163
line_end: 19179
dependencies:
  - "A.1"
  - "B.1.1"
keywords:
  - "ComponentOf"
  - "PhaseOf"
  - "PortionOf"
  - "composition"
  - "mereology"
  - "part-of"
---

### A.14:1 - Context — why an advanced mereology?

FPF’s holonic modelling relies on **part–whole** relations to build *structural* and *conceptual* holarchies (systems and epistemes). But `U.Holon` is **not** synonymous with “mereological whole”: some holons (notably **Roles** and **Methods**) are bounded identity‑bearing objects whose primary composition is handled by other algebras (A.2 role algebra; A.15 method/description graphs), not by `partOf`. Early drafts distinguished structural vs. conceptual parthood (e.g., **ComponentOf**, **ConstituentOf**) but practical modelling kept hitting two recurrent gaps:

1. **Quantities vs. parts.** Engineers routinely need “some of the fuel”, “the first 10 pages”, “a 30% subset of data”. This is not a component; it is a **portion** of a stuff‑like whole, governed by measures and conservation.

2. **Change vs. replacement.** Authors need to say “the prototype **before calibration**”, “v2 of the spec”, “shift 1 vs. shift 2 of the same run”. That is not a new whole; it is a **phase** of the same carrier across time.

This section introduces two **normative** sub‑relations of `partOf` that close those gaps and lock them to the rest of the kernel:

* **PortionOf** — metrical, measure‑preserving parthood of stuffs and other measurables.
* **PhaseOf** — temporal parthood of the *same* carrier across an interval.

It also restates guard‑rails that keep **Roles** and **Methods** (as intensional masks/ways‑of‑doing) outside mereology (A.15), while allowing their **describing epistemes** (e.g., `U.MethodDescription`, `U.WorkPlan`) to use ordinary episteme parthood and versioning like any other `U.Episteme`. It also clarifies how **MemberOf** fits (preview: **collections** are grounded constructively in **C.13 Compose‑CAL** via `Γ_m.set`; collective agency/composition is handled outside A.14 via **B.1.7 Γ_collective** and **A.15**, not via `partOf`).

**Publication note (Working‑Model first).** Read A.14 together with **E.14 Human‑Centric Working‑Model** and **B.3.5 CT2R‑LOG**: publish relations on the **Working‑Model** surface; when assurance is sought, **ground downward**. For structural claims that require extensional identity, use the **Constructive** shoulder via **Compose‑CAL Γ_m (sum | set | slice)**; order/time stay outside mereology (Γ_time / Γ_method).

