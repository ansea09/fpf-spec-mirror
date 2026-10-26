---
chunk_kind: "child"
pattern_id: "C.31.ASAP"
pattern_title: "Which Architecture Is Preferable Under Scale? (Scale Amenability)"
section_id: "C.31.ASAP:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31.ASAP/C.31.ASAP__007_bias-annotation.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "C.31.ASAP — Which Architecture Is Preferable Under Scale? (Scale Amenability)"
  - "C.31.ASAP:6 — Bias-Annotation"
line_start: 75103
line_end: 75112
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.CPM"
  - "A.2.6"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18.1"
  - "C.19.1"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.31"
  - "C.31.RSA"
  - "C.32"
  - "C.32.ACS"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
  - "architecture alternatives"
  - "architecture scale preference"
  - "coarse-graining"
  - "exception growth"
  - "scale amenability"
  - "scale probe"
  - "scale variable"
  - "scale window"
  - "waiver"
---

### C.31.ASAP:6 - Bias-Annotation

| Bias risk | C.31.ASAP correction |
| --- | --- |
| **Platform label bias** | Platform or product-line wording names a possible source context, not scale-preference evidence. Recover variability slots, extension rules, exception curve, refactor triggers, and source-return condition. |
| **Modularity-means-scalability bias** | A count or reusable share alone does not establish scale preference. Use C.31 or C.31.RSA when the characteristic or accounting meaning remains unresolved; proceed directly to C.31.ASAP when the alternatives, variable, window and relevant grounds are recoverable. |
| **Debt inflation bias** | A locally hand-engineered solution is called debt without checking deontic, safety, law-domain, mission, assurance, or scale-probe waiver reasons. |
| **RG proof bias** | RG, coarse-graining, fixed-point, or universality wording is treated as scale-preference proof. Use C.29 for lens recovery and keep scale preference in C.31.ASAP. |
| **Selection laundering** | The scale-preference claim is used as if it selected the architecture. Use `G.5` for selected-set declaration and `C.11` for local choice; use `G.9` when parity is current. |

