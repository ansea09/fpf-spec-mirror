---
chunk_kind: "child"
pattern_id: "A.6.2"
pattern_title: "Effect-Free Episteme Morphing: Laws for Mathematical Relations Between Epistemes"
section_id: "A.6.2:10.1"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.2/A.6.2__012_sota-echoing.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "A.6.2 — Effect-Free Episteme Morphing: Laws for Mathematical Relations Between Epistemes"
  - "A.6.2:10.1 — SoTA-Echoing"
line_start: 17381
line_end: 17391
dependencies:
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "F.9"
  - "U.Mechanism"
  - "U.Signature"
keywords:
---

### A.6.2:10.1 - SoTA-Echoing

**Practice question.** How can reusable transformation definitions and composition remain separate from execution and correctness evidence, and which repeat laws do they support?

| Source or practice | Contribution used here | Use boundary |
| --- | --- | --- |
| [Zhao et al., *KBX: Verified Model Synchronization via Formal Bidirectional Transformation* (2024)](https://arxiv.org/abs/2404.18771) | Separates formal BX definitions, generated synchronization and consistency verification. | This supports the declaration, arrow, application and use-claim distinction. The synchronizer's laws do not establish purity or idempotence for every FPF arrow. |
| [He and Zan, *BIT: A template-based approach to incremental and bidirectional model-to-text transformation* (2024)](https://doi.org/10.1016/j.jss.2024.112148) | Separates a surface language, formal core semantics, printer/parser execution, round-trip properties and empirical cases; some computational effects are explicit. | Its round-trip laws belong to that construction. They supply no universal EFEM idempotence law. |
| Category, optic, fibration, cospan and BX traditions | Supply mathematical lineage for arrows, identities, composition, views and correspondences. | The selected FormalSubstrate supplies the local mathematical theory. C.29 governs a mathematical-lens use; F.9 correspondence, EntityOfConcern identity and repeat laws retain their independent conditions. |
| FPF C.2.1, C.29, A.6.3.RT and A.6.4 | Separate episteme identity, mathematical-lens use, same-entity representation change and changed-entity retargeting with a use-specific claim. | These patterns govern the corresponding FPF objects and uses. |

