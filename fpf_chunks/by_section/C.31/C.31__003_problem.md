---
chunk_kind: "child"
pattern_id: "C.31"
pattern_title: "Modularity and Reusable Structure Characteristics"
section_id: "C.31:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31/C.31__003_problem.md"
commit_sha: "1f413fcd23f4ea26956a45d67dde57bb233f6ad9"
heading_path:
  - "C.31 — Modularity and Reusable Structure Characteristics"
  - "C.31:2 — Problem"
line_start: 62177
line_end: 62184
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.31"
  - "C.31.ASAP"
  - "C.31.RSA"
  - "C.32"
  - "C.32.P2S"
  - "G.5"
keywords:
  - "ModularityVectorLite"
  - "bespoke residue"
  - "cohesion"
  - "coupling"
  - "evidence reuse"
  - "interface variation"
  - "modularity characteristics"
  - "reusable-structure characteristics"
  - "substitutability"
---

### C.31:2 - Problem

Architecture work often asks for more modularity, better reuse, lower coupling, more explicit interfaces, cleaner allocation, or less bespoke residue. These phrases point to real engineering work, but they do not name one scalar property.

Modularity can improve along one characteristic while worsening another. A design can reduce external coupling and increase interface alphabet size. A platform can standardize interfaces and create unhelpful rigidity. Evidence reuse can improve while functional-to-module allocation remains tangled. A report can show a high reuse share while hiding source-return work or residual uncertainty.

C.31 turns modularity talk into a small characteristic vector plus repair direction. It does not promise that every characteristic is measurable now, comparable across cases, causal, admissible for decision use, or evidence-backed.

