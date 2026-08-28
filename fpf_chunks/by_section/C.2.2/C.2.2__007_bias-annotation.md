---
chunk_kind: "child"
pattern_id: "C.2.2"
pattern_title: "Reliability R in the F–G–R triad"
section_id: "C.2.2:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.2/C.2.2__007_bias-annotation.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "C.2.2 — Reliability R in the F–G–R triad"
  - "C.2.2:6 — Bias-Annotation"
line_start: 42461
line_end: 42471
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

### C.2.2:6 - Bias-Annotation

Informative; non-binding.

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal**.

* **Onto/Epist bias:** High formality is often mistaken for high warrant (“proof therefore true in the world”). This pattern mitigates by forcing LA/TA visibility and by routing transport loss into R rather than mutating the claim.
* **Prag bias:** Teams may Goodhart R by narrowing scope or selecting easy tests. This pattern mitigates by requiring explicit scope declaration and by making scope changes first-class (A.2.6).
* **Gov bias:** Overconfident reuse after a changed scope, scheme, model use, evidence basis, kind, or plane is a recurring failure. This pattern requires the actual relation and its declared loss instead of one generic crossing label.
* **Did bias:** A single scalar is seductive; it hides what kind of warrant exists. Lane reporting keeps the scalar honest.

