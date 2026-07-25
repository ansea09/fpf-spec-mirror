---
chunk_kind: "child"
pattern_id: "C.31"
pattern_title: "Modularity and Reusable Structure Characteristics"
section_id: "C.31:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31/C.31__007_bias-annotation.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "C.31 — Modularity and Reusable Structure Characteristics"
  - "C.31:6 — Bias-Annotation"
line_start: 62091
line_end: 62101
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

### C.31:6 - Bias-Annotation

| Bias risk | C.31 repair |
| --- | --- |
| Scalar bias | Refuse one modularity score unless scoring method and comparability basis are declared. |
| Measure-first bias | Start with `ModularityVectorLite` and repair direction before C.16-heavy fields. |
| Interface-publication bias | Treat public interfaces as only one possible basis for substantiating substitutability. |
| Proxy bias | Add `ProxyRisk` and `AuditQuestion` to every decision-facing card. |
| Complexity umbrella bias | Keep residual heads claim-scoped and apply scale, RG, or lens governing patterns when those uses are being made. |
| Source-label bias | Treat software, neural-network, chiplet, safety-case, product-line, block, layer, expert, cache, router, and gate labels as source examples until `C.30.STRAT` and the governing pattern recover the FPF characteristic subject, structure, scale, and admissible use. |

