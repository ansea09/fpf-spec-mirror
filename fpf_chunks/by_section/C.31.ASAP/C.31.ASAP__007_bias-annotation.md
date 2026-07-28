---
chunk_kind: "child"
pattern_id: "C.31.ASAP"
pattern_title: "Architecture Scale-Amenability Preference"
section_id: "C.31.ASAP:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31.ASAP/C.31.ASAP__007_bias-annotation.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "C.31.ASAP — Architecture Scale-Amenability Preference"
  - "C.31.ASAP:6 — Bias-Annotation"
line_start: 63199
line_end: 63208
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
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
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
  - "RG"
  - "ScaleClaimTriage"
  - "architecture alternatives"
  - "architecture scale preference"
  - "coarse-graining"
  - "platform scale claim"
  - "scale amenability"
  - "scale variable"
  - "scale window"
  - "source-return condition"
  - "waiver reason"
---

### C.31.ASAP:6 - Bias-Annotation

| Bias risk | C.31.ASAP correction |
| --- | --- |
| **Platform label bias** | Platform or product-line wording names a possible source context, not scale-preference evidence. Recover variability slots, extension rules, exception curve, refactor triggers, and source-return condition. |
| **Modularity-means-scalability bias** | A module count, interface count, or reusable-structure share is not a scale preference. Use C.31 and C.31.RSA first, then C.31.ASAP only when scale variable and scale window are named. |
| **Debt inflation bias** | A locally hand-engineered solution is called debt without checking deontic, safety, law-domain, mission, assurance, or scale-probe waiver reasons. |
| **RG proof bias** | RG, coarse-graining, fixed-point, or universality wording is treated as scale-preference proof. Use C.29 for lens recovery and keep scale preference in C.31.ASAP. |
| **Selection laundering** | The scale-preference claim is used as if it selected the architecture. Use `G.5`, `G.9`, or `C.11` for selected-set or choice claims. |

