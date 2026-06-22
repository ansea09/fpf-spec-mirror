---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Trust and Assurance Calculus (F-G-R with Congruence)"
section_id: "B.3:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__002_problem-frame.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "B.3 — Trust and Assurance Calculus (F-G-R with Congruence)"
  - "B.3:1 — Problem frame"
line_start: 33792
line_end: 33811
dependencies:
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.6"
  - "A.7"
  - "B.1"
  - "B.1.1"
  - "B.3"
  - "B.3.5"
  - "B.3.x"
  - "B.4"
  - "C.13"
  - "C.16"
  - "C.26"
  - "C.26.1"
  - "C.26.2"
  - "C.26.3"
  - "C.28"
  - "D.4"
  - "E.14"
  - "E.17.EFP"
  - "F.9"
keywords:
  - "F-G-R"
  - "assurance"
  - "authority-looking labels"
  - "claim-support posture"
  - "congruence"
  - "dashboard tiles"
  - "evidence"
  - "formality"
  - "probe/distributed/export/causal assurance"
  - "reliability"
  - "scope"
  - "trust"
---

### B.3:1 - Problem frame

Every non‑trivial result in FPF—*a composed system is safe*, *a model is credible*, *a conclusion holds*—is a **claim** that rests on **composed evidence**.

* For **U.System** holons, assurance is about *capabilities and constraints* under stated conditions.
* For **U.Episteme** holons, assurance is about the *quality of evidence relation* for a statement or model.

To make such claims comparable and auditable across domains, B.3 introduces a **Trust and Assurance Calculus** that:

* uses a **small typed assurance tuple** (F-G-R: `F` and `R` as characteristics plus `G` as scope value) governed by conservative propagation rules; this tuple is **not** a state space,
* accounts for **integration quality** via **Congruence Level (CL)** along the edges of a `DependencyGraph` (B.1.1, A.14),
* and composes these values only through current governing composition, transformation, temporal, and work operators while respecting their declared invariants.

B.3 is **conceptual and normative**: it defines *which assurance components must be published and how they propagate*. How those components improve (for example by formalizing, replicating, reconciling, or widening or narrowing scope under declared operation rules) is handled by KD-CAL improvement moves; those knowledge-dynamics references are descriptive, not required to read here.

**Mechanism linkage.** For law-governed operation families (for example **USM** and **UNM**) authored as **mechanisms**, use A.6.1 — U.Mechanism to publish **OperationAlgebra**, **LawSet**, **AdmissibilityConditions**, and the **Transport** clause (Bridge-only; `CL`, `CL^k`, and `CL^plane`). All such penalties reduce `R_eff` only; `F` and `G` remain invariant.

**Working-Model handshake (alignment with E.14, B.3.5, and C.13).**
Assurance consumes two inputs declared in the **Working-Model** assertion layer (CT2R-LOG, B.3.5): the **justification declaration** `validationMode ∈ {postulate, inferential, axiomatic}` and, where present, the **grounding link** `tv:groundedBy`. Structural claims that aspire to the strongest guarantees rely on **Constructive** grounding as a constructive-composition narrative referenced via `tv:groundedBy`. No assurance record or publication **defines** Working-Model wording or layout; dependence remains downward-only under E.14.

