---
chunk_kind: "child"
pattern_id: "C.18.1"
pattern_title: "Scaling‑Law Lens Binding (SLL)"
section_id: "C.18.1:12.1"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.18.1/C.18.1__014_sota-echoing.md"
commit_sha: "e307edbd91c04c1d85661bd309b9944fac251937"
heading_path:
  - "C.18.1 — Scaling‑Law Lens Binding (SLL)"
  - "C.18.1:12.1 — SoTA-Echoing"
line_start: 61422
line_end: 61427
dependencies:
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.24"
  - "G.10"
  - "G.5"
  - "G.9"
keywords:
  - "DoE (design‑of‑experiments)"
  - "Scale Variables (S)"
  - "ScaleWindow"
  - "UNM/NormalizationMethod‑based mapping"
  - "compute‑elasticity"
  - "data‑elasticity"
  - "diminishing returns"
  - "elasticity class"
  - "iso‑scale parity"
  - "knee"
  - "knee detection"
  - "probe uncertainty"
  - "resolution‑elasticity"
  - "scale variables (S)"
  - "scale‑probe"
  - "scaling law"
  - "segmented regression"
---

### C.18.1:12.1 - SoTA-Echoing

**Which evidence is sufficient for a scale claim?** Retain the distinction in `C.29` between a consequence inside a declared mathematical model and a claim about the modelled phenomenon. The conditional cost equations in `C.19.2:5` establish their break-even horizon from the supplied assumptions; empirical probes would answer whether those assumptions describe actual handoffs. Requiring a probe for the derivation adds work without strengthening that conditional result, while using the derivation as observed performance omits the needed evidence. This pattern therefore limits its probe requirements to empirical scale claims and adapts `C.19.1`'s claim-matched evidence rule: keep real parity and uncertainty conditions, and reuse an adequate account. Reopen when the assertion extends beyond the model conditions, the empirical window or the supported uncertainty.

Scaling-law fits, knee detectors, segmented regressions and experimental-design methods support the scale claim under their own conditions. Keep the measurement, parity and selector-policy grounds required by the use. Apply `C.29` only when a mathematical representation choice, transfer or reliance question remains unresolved.

