---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Trust and Assurance Calculus (F-G-R with Congruence)"
section_id: "B.3:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__002_problem-frame.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "B.3 — Trust and Assurance Calculus (F-G-R with Congruence)"
  - "B.3:1 — Problem frame"
line_start: 38503
line_end: 38522
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.4"
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.6"
  - "A.6.1"
  - "B.1"
  - "B.1.1"
  - "B.3"
  - "B.3.5"
  - "B.4"
  - "C.13"
  - "C.16"
  - "C.16.Q"
  - "C.2.1"
  - "C.26"
  - "C.26.1"
  - "C.26.2"
  - "C.26.3"
  - "C.28"
  - "C.29"
  - "D.4"
  - "E.14"
  - "E.17"
  - "E.17.EFP"
  - "E.24.PUB"
  - "F.10"
  - "F.9"
  - "G.11"
  - "G.6"
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

When a non-trivial result in FPF—*a composed system is safe*, *a model is credible*, *a conclusion holds*—is reused for a consequential assurance purpose, the assurance-result claim must expose the exact result claim and the basis on which that use is warranted.

* For a claim whose EntityOfConcern is a **U.System** holon, assurance evaluates the exact capability, constraint, safety, or reliability claim under stated conditions; it is not a new system state.
* For a claim whose EntityOfConcern is a **U.Episteme** holon, assurance evaluates the exact content or model claim and its warrant for `U_A`; it is not an intrinsic quality conferred on the episteme by a citation or evidence item.

To make such claims comparable and auditable across domains, B.3 introduces a **Trust and Assurance Calculus** that:

* uses a **small typed assurance tuple** (F-G-R: `F` and `R` as characteristics plus `G` as scope value) governed by conservative propagation rules; this tuple is **not** a state space,
* accounts for **integration quality** via **Congruence Level (CL)** along the edges of a `DependencyGraph` (B.1.1, A.14),
* and composes these values only through current governing composition, transformation, temporal, and work operators while respecting their declared invariants.

B.3 is **conceptual and normative**: it defines *which assurance components must be published and how they propagate*. How those components improve (for example by formalizing, replicating, reconciling, or widening or narrowing scope under declared operation rules) is handled by KD-CAL improvement moves; those knowledge-dynamics references are descriptive, not required to read here.

**Mechanism linkage.** For law-governed operation families (for example **USM** and **UNM**) authored as **mechanisms**, use A.6.1 — U.Mechanism to publish **OperationAlgebra**, **LawSet**, **AdmissibilityConditions**, and the **Transport** clause (Bridge-only; `CL`, `CL^k`, and `CL^plane`). All such penalties reduce `R_eff` only; `F` and `G` remain invariant.

**Working-Model handshake (alignment with E.14, B.3.5, and C.13).**
Assurance consumes two inputs declared in the **Working-Model** assertion layer (CT2R-LOG, B.3.5): the **justification declaration** `validationMode ∈ {postulate, inferential, axiomatic}` and, where present, the **grounding link** `tv:groundedBy`. Structural claims that aspire to the strongest guarantees rely on **Constructive** grounding as a constructive-composition narrative referenced via `tv:groundedBy`. No assurance record or publication **defines** Working-Model wording or layout; dependence remains downward-only under E.14.

