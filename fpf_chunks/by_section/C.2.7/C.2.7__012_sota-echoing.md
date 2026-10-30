---
chunk_kind: "child"
pattern_id: "C.2.7"
pattern_title: "LanguageStateRepresentationFactorBundle — How Is the Representation Organized?"
section_id: "C.2.7:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.7/C.2.7__012_sota-echoing.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "C.2.7 — LanguageStateRepresentationFactorBundle — How Is the Representation Organized?"
  - "C.2.7:11 — SoTA-Echoing"
line_start: 53987
line_end: 53994
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.18"
  - "A.19"
  - "B.4.1"
  - "B.5.2.0"
  - "C.2.2a"
  - "C.2.6"
  - "C.2.LS"
  - "F.9"
  - "F.9.1"
keywords:
  - "factor bundle"
  - "locality"
  - "representation factors"
  - "representation organization"
  - "sparsity"
  - "symbolicity"
---

### C.2.7:11 - SoTA-Echoing
The triple is an FPF starting choice for :4.1.1, with bounded external comparisons:

| Source and status | Contribution and boundary |
|---|---|
| [Elhage et al., *Toy Models of Superposition* (2022)](https://transformer-circuits.pub/2022/toy_model/toy_model.pdf), pp.1–5, historical research basis | Feature directions can differ from neuron basis directions. This supports identifying the units and basis before interpreting locality or sparsity; the toy models do not establish the FPF triple for all representations. |
| [Fraser-Taliente et al., *Natural Language Autoencoders* (2026)](https://transformer-circuits.pub/2026/nla/index.html), Method and Discussion | The method maps activations to text and reconstructs activations from that text. Reconstruction and the interpretation of the explanation require their own assessment. This is a current case for selecting task-specific Characteristics alongside, or instead of, starter factors. |

