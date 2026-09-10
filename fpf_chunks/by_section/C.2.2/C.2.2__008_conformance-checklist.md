---
chunk_kind: "child"
pattern_id: "C.2.2"
pattern_title: "Reliability R in the F–G–R triad"
section_id: "C.2.2:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.2/C.2.2__008_conformance-checklist.md"
commit_sha: "cc1aef9b8e38dd50889e058fdc56725b9714fd42"
heading_path:
  - "C.2.2 — Reliability R in the F–G–R triad"
  - "C.2.2:7 — Conformance Checklist"
line_start: 43334
line_end: 43350
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
| **CC‑C.2.2‑1 (Triad publication).** | Authors of a KD-CAL location SHALL attach formal basis, G, and warrant to one exact claim. A numerical R requires the receiving model; otherwise identify unquantified support and the bounded conclusion. | Keeps warrant attached to its claim without inventing a score. |
| **CC‑C.2.2‑2 (R-only penalty routing).**      | A conforming implementation of KD‑CAL reuse **SHALL** satisfy **INV‑C2.2‑1**.                                                                                                                                                | Ensures declared relation losses reduce warrant without silently mutating expression or scope. |
| **CC‑C.2.2‑3 (Support composition).** | A conforming composition SHALL satisfy DEF‑C2.2‑3: identify support roles, compatible scales, and dependencies, and use the justified receiving model or a non-aggregate synthesis. There is no default min or max. | Prevents both overstated assurance and loss of useful complementary support. |
| **CC‑C.2.2‑4 (Relation visibility for reuse).** | Authors **SHALL** name every scope-translation, kind, plane, notation, source-local, model-use, or evidence-reuse relation traversed by the path and cite the fit or loss rule that affects `R_eff`.                                      | Makes each actual reuse loss auditable without inventing one crossing kind.   |
| **CC‑C.2.2‑5 (Loss model visibility).** | Any numerical reuse loss SHALL identify its receiving quantity, scale, assumptions, derivation or calibration, and actual functions and versions, including Π where used. | Makes the calculation reproducible and its meaning inspectable. |
| **CC‑C.2.2‑6 (Type before scope).**           | Authors and validators **SHALL** enforce **WFC‑C2.2‑1** for scope composition operations.                                                                                                                                   | Prevents ill-typed scope algebra from creating incoherent reliability claims. |
| **CC‑C.2.2‑7 (Evidence binding).**            | Authors **SHALL** bind any asserted `R_eff` to evidence references that enable TA/VA/LA inspection, consistent with the assurance lane discipline (B.3.3) and evidence decay discipline (B.3.4).                            | Keeps R grounded and updateable.                                              |
| **CC‑C.2.2‑8 (No ordinal arithmetic).** | Validators SHALL reject arithmetic that treats ordinal F, CL, or an ordinal R proxy as ratio-scale values. A receiving conversion model must establish meaning, scale, conversion, and assumptions; a penalty table or rescaling alone is insufficient. Formal validity never supplies empirical reliability by itself. | Preserves scale legality and useful formal conclusions. |
| **CC‑C.2.2‑9 (Interpretation conditions declared).** | Authors **SHALL** distinguish design- and run-time assurance and declare `ReferencePlane`, effective scheme, model-use basis, working situation, and `validationMode` where each changes the claim or use.                               | Makes interpretation auditable without a generic Context identity field.     |
| **CC‑C.2.2‑10 (Dependence and scope).** | Authors SHALL expose actual shared premises, data, assumptions, and biases. Any assumed independence must be justified for the model and use; different path labels do not suffice. Keep distinct scope slices and counterevidence visible; do not fall back to minimum for entangled support. | Prevents double-counting without erasing complementary evidence. |

