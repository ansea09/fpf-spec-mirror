---
chunk_kind: "child"
pattern_id: "C.31.ASAP"
pattern_title: "Architecture Scale-Amenability Preference"
section_id: "C.31.ASAP:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31.ASAP/C.31.ASAP__012_sota-echoing.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "C.31.ASAP — Architecture Scale-Amenability Preference"
  - "C.31.ASAP:11 — SoTA-Echoing"
line_start: 60353
line_end: 60362
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

### C.31.ASAP:11 - SoTA-Echoing

| Source family | Source-use relation | C.31.ASAP adaptation | Non-admissible overread | Practitioner implication |
| --- | --- | --- | --- | --- |
| Software product-line and variability-management practice (`https://www.sei.cmu.edu/library/variability-in-software-product-lines/`; `https://arxiv.org/abs/2605.21353`) | Mature variability lineage plus current SPLE-review cues. | Adopt variability slots, product-line reuse, exception inventory, and refactor triggers as architecture scale-preference fields. | Product-line label, shared code base, feature model, or platform name is not scale-preference evidence. | Before preferring the product-line alternative, name the scale window, variability slots, exception curve, and source-return condition. |
| Product-platform and modular product-architecture practice (`https://link.springer.com/article/10.1007/s00163-023-00427-1`; `https://arxiv.org/abs/2510.11089`) | Current engineering-design source line for modular product architecture, assembly orientation, product-family reuse, and manufacturing-aware modularity. | Adopt the product-family commonality and variety trade-off as an architecture scale-preference pressure: reusable structure needs declared variation points, interface rules, assembly or realization constraints, exception curve, and source-return condition. | A product-platform name, common-module count, or modular-product label is not scale-preference evidence and does not by itself justify a module-interface or manufacturing claim. | Before preferring a product-platform alternative, state which product-family variation is scaled, which structure remains stable, and which assembly, safety, law-domain, or mission exception is allowed. |
| Platform-engineering maturity practice (`https://tag-app-delivery.cncf.io/fr/whitepapers/platform-eng-maturity-model/`) | Current platform-practice source for platform service set, extension-rule, substitution-policy, and maturity-pressure claims. | Adapt platform practice into extension-rule, substitution-policy, conformance-expectation, and exception-growth checks. | Platform maturity does not by itself select an architecture or prove reusable structure. | Treat platform claims as source cues until the architecture scale variable and exception behavior are declared. |
| C.19.1 BLP in FPF | FPF-local preference discipline for general scale-amenable methods. | Specialize the preference idea to architecture alternatives, selected structures, scale variables, and architecture slope vector. | C.31.ASAP does not replace general method BLP, selector policy, or decision records. | Use C.19.1 for method-family policy; use C.31.ASAP for architecture scale preference. |
| C.29 RG and coarse-graining lens use in FPF | FPF-local mathematical-lens discipline. | Require scale window, coarse-graining rule, preserved structure, lost structure, and source-return condition when RG-like architecture scale reasoning is being claimed. | RG wording is not physical RG, scale proof, causal proof, assurance, or selected architecture. | Use `MLU.Description@RGArchitecture` or `MLU.Description@MultilevelLearningFrustration` only when the lens changes the next admissible use. |

