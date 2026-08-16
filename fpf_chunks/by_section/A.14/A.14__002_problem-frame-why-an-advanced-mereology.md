---
chunk_kind: "child"
pattern_id: "A.14"
pattern_title: "Advanced Mereology: Components, Portions, Aspects & Phases"
section_id: "A.14:1"
section_title: "Problem frame - why an advanced mereology?"
source_path: "FPF-Spec.md"
output_path: "by_section/A.14/A.14__002_problem-frame-why-an-advanced-mereology.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "A.14 — Advanced Mereology: Components, Portions, Aspects & Phases"
  - "A.14:1 — Problem frame - why an advanced mereology?"
line_start: 23622
line_end: 23638
dependencies:
  - "A.1"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.7"
  - "B.1"
  - "B.1.1"
  - "B.2"
  - "B.3.5"
  - "C.13"
keywords:
  - "ComponentOf"
  - "PhaseOf"
  - "PortionOf"
  - "composition"
  - "mereology"
  - "part-of"
---

### A.14:1 - Problem frame - why an advanced mereology?

FPF’s holonic modelling relies on **part–whole** relations to build *structural* and *conceptual* holarchies for admitted holons such as systems, epistemes, work occurrences, bounded contexts, disciplines, and methods. But `U.Holon` is **not** a synonym for every bounded object. A local system-role kind is an exact context-local `U.Kind` whose candidates are `U.System` values; it is neither a public root U-kind nor a holon kind by kind identity. `U.Method` is a non-agentive holon kind, but submethod assembly is handled by method-composition patterns, not by A.14 structural component mereology. `SystemRoleKindRelationStructure`, method relation structures, system-role-kind descriptions, method descriptions, work plans, and work occurrences enter A.14 only through their subject patterns and admitted carriers. Early drafts distinguished structural vs. conceptual parthood (e.g., **ComponentOf**, **ConstituentOf**) but practical modelling kept hitting two recurrent gaps:

1. **Quantities vs. parts.** Engineers routinely need “some of the fuel”, “the first 10 pages”, “a 30% subset of data”. This is not a component; it is a **portion** of a stuff‑like whole, governed by measures and conservation.

2. **Change vs. replacement.** “The prototype **before calibration**” may be a proper temporal restriction of one unchanged pump. By contrast, “v2 of the spec” first opens C.2.1 identity and, for two different epistemes, its independent edition-continuity test; “shift 1 vs. shift 2” first opens A.15.1 Work-part or occurrence law. None of those labels selects `PhaseOf` by itself.

This section introduces two **normative** sub‑relations of `partOf` that close those gaps and lock them to the rest of the kernel:

* **PortionOf** — metrical, measure‑preserving parthood of stuffs and other measurables.
* **PhaseOf** — temporal parthood of the *same* carrier across an interval.

It also restates guard-rails that keep local system-role kinds outside holon mereology by kind identity and keep **method values** outside A.14 structural component mereology, while allowing method holarchy through method patterns such as `A.3.1` and `B.1.5`. Describing epistemes such as `U.MethodDescription` and `U.WorkPlan` keep their C.2.1 identity: content or publication-unit inclusion may use ordinary episteme parthood, a proper interval of one unchanged episteme may use `PhaseOf`, and changed C.2.1 identity discriminators identify another episteme whose historical continuation is tested separately through `EpistemeEditionRelation`. It also clarifies how **MemberOf** fits: membership and collection-as-whole grounding start with A.14, C.13, and B.3.5 as appropriate; acting collective systems require `U.System` admission plus system-role assignment, method, work, and evidence patterns; whole reidentification uses B.2 only when existing-whole explanations fail.

**Publication note (Working-Model first).** Read A.14 together with **E.14 Human-Centric Working-Model** and **B.3.5 CT2R-LOG**: publish the direct relation claim in the **Working-Model** layer and, when assurance is sought for a structural claim, link that assertion downward to one current C.2.1 construction-trace episteme in the **Compose-CAL Γ_m** `sum`, `set`, or `slice` form. The trace reports exact participants, direct relation occurrences, the applicable construction rule, and identity or reidentification conditions. It creates none of them; order and time remain outside mereology.

