---
chunk_kind: "child"
pattern_id: "C.2.2"
pattern_title: "Reliability R in the F–G–R triad"
section_id: "C.2.2:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.2/C.2.2__008_conformance-checklist.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "C.2.2 — Reliability R in the F–G–R triad"
  - "C.2.2:7 — Conformance Checklist"
line_start: 41505
line_end: 41521
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.2.6"
  - "A.21"
  - "A.6.3.RT"
  - "B.1.3"
  - "B.3"
  - "B.3.3"
  - "B.3.4"
  - "C.16"
  - "C.2"
  - "C.2.3"
  - "C.21"
  - "C.29"
  - "C.3"
  - "C.3.3"
  - "C.3.A"
  - "E.14"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.9"
  - "G.2"
  - "G.6"
  - "G.7"
keywords:
  - "ClaimScope (G)"
  - "Congruence Level (CL / CL^k / CL^plane)"
  - "F–G–R"
  - "Reliability (R)"
  - "TA/VA/LA lanes"
  - "direct relation"
  - "evidence-bound"
  - "no implicit averaging"
  - "pathwise justification (PathId)"
  - "warrant"
  - "weakest-link"
---

### C.2.2:7 - Conformance Checklist

Normative.

| ID                                            | Requirement                                                                                                                                                                                                                 | Purpose                                                                       |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **CC‑C.2.2‑1 (Triad publication).**           | Authors of a KD‑CAL location **SHALL** publish `⟨F,G,R_eff⟩` for one exact claim, rather than publishing `R` alone.                                                                                                      | Keeps the warrant attached to its claim and declared scope.                   |
| **CC‑C.2.2‑2 (R-only penalty routing).**      | A conforming implementation of KD‑CAL reuse **SHALL** satisfy **INV‑C2.2‑1**.                                                                                                                                                | Ensures declared relation losses reduce warrant without silently mutating expression or scope. |
| **CC‑C.2.2‑3 (Weakest-link fold).**           | A conforming implementation of KD‑CAL reliability propagation **SHALL** use **DEF‑C2.2‑3** as the default for required supports, unless an alternative Γ‑fold is explicitly declared and remains monotone and conservative. | Prevents confidence laundering through aggregation.                           |
| **CC‑C.2.2‑4 (Relation visibility for reuse).** | Authors **SHALL** name every scope-translation, kind, plane, notation, source-local, model-use, or evidence-reuse relation traversed by the path and cite the fit or loss rule that affects `R_eff`.                                      | Makes each actual reuse loss auditable without inventing one crossing kind.   |
| **CC‑C.2.2‑5 (Penalty policy visibility).**   | Authors or tooling **SHALL** reference the active policy identifiers used for `Φ`, `Ψ`, `Φ_plane` **and** the penalty aggregation rule `Π` (if not the default) when computing `R_eff`.                                   | Ensures repeatability and prevents hidden policy drift.                       |
| **CC‑C.2.2‑6 (Type before scope).**           | Authors and validators **SHALL** enforce **WFC‑C2.2‑1** for scope composition operations.                                                                                                                                   | Prevents ill-typed scope algebra from creating incoherent reliability claims. |
| **CC‑C.2.2‑7 (Evidence binding).**            | Authors **SHALL** bind any asserted `R_eff` to evidence references that enable TA/VA/LA inspection, consistent with the assurance lane discipline (B.3.3) and evidence decay discipline (B.3.4).                            | Keeps R grounded and updateable.                                              |
| **CC‑C.2.2‑8 (No ordinal arithmetic).**       | Validators **SHALL** reject any computation that treats `F` or `CL` as if they were ratio-scale numbers (e.g., averaging, subtraction), except where explicitly permitted as a policy-defined penalty function on `R`. Validators **SHALL** also reject arithmetic over `R_eff` when it is published as an **ordinal proxy** ([M‑0/M‑1]). | Enforces CSLC legality and prevents silent scalarisation.                     |
| **CC‑C.2.2‑9 (Interpretation conditions declared).** | Authors **SHALL** distinguish design- and run-time assurance and declare `ReferencePlane`, effective scheme, model-use basis, working situation, and `validationMode` where each changes the claim or use.                               | Makes interpretation auditable without a generic Context identity field.     |
| **CC‑C.2.2‑10 (Parallel requires independence).** | Authors **SHALL** treat `max`-composition of support paths as admissible **only** when an explicit independence justification is recorded; otherwise supports are treated as one entangled line and remain weakest-link. | Prevents confidence inflation by double-counting correlated evidence.         |

