---
chunk_kind: "child"
pattern_id: "A.19"
pattern_title: "CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
section_id: "A.19:3"
section_title: "Problem (Informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19/A.19__005_problem-informative.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.19 — CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
  - "A.19:3 — Problem (Informative)"
line_start: 22631
line_end: 22643
dependencies:
  - "A.17"
  - "A.18"
  - "A.19.CHR"
  - "A.19.CN"
  - "A.19.SUPPORT-VIEW"
  - "A.19.SURF-SPACE"
  - "A.2.5"
  - "A.3.3"
  - "C.16"
  - "E.18"
  - "G.0"
keywords:
  - "CharacteristicSpace"
  - "U.Dynamics.stateSpace"
  - "coordinatewise comparability"
  - "declared Characteristics and Scales"
  - "embedding"
  - "product"
  - "role-specific space refs stay outside A.19"
  - "state trajectories"
  - "structural overlays"
  - "subspace"
---

### A.19:3 - Problem (Informative)

-   **P1 — “Feature vector” drift.** In practice, teams often assemble state vectors or “feature” lists with implicit or mismatched units and scales. Without a formal space, one coordinate’s value can’t safely be compared or combined with another’s (e.g. mixing degrees Celsius with percentages). **CSLC** guarantees consistency **per Characteristic**, but a bundle of multiple “characteristics” remains under-specified if we lack a unified space definition.

-   **P2 — Lifecycle bias.** Absent a formal state space, system change tends to be described in terms of fixed **stages or phases** (design phases, maturity levels, etc.). This conflicts with FPF’s **open-ended** stance: in FPF a role’s state model (RSG) allows re-entry and refinement of states rather than one-way lifecycle stages with an “end.” We need a space model that treats evolution as continuous movement, not a one-directional sequence.

-   **P3 — Incoherence across CN‑frames.** Different modeling “CN‑frames” (architecture vs. epistemic vs. operational) often choose different sets of qualities to measure (different sets of characteristics). Later, however, we may need to **compose** these models or **project** one into another. Without a kernel notion of how one state space can be a **subspace** of or **embedded** in another, any integration of models will be ad hoc and error-prone.

-   **P4 — Relational measurements.** Some Characteristics are inherently **relational** (e.g. a _Coupling_ between two components, or _Distance_ between points). Naïvely forcing such traits into a single-object feature vector loses critical information (arity, symmetry). The kernel already distinguishes single-entity vs multi-entity Characteristics (A.17); we must preserve that distinction in the state space so that a relational metric isn’t treated as an intrinsic one by mistake.

-   **P5 — The geometry temptation.** When defining a state space, it’s tempting to assume or inject additional structure (ordering of states, topologies for continuity, metrics for distance) as if inherent. But the kernel must remain minimal and domain-neutral: it should not **smuggle in** analysis methods or domain-specific norms under the guise of geometry. Any such structure should be added explicitly by specialized patterns, not baked into the core definition of a space.


