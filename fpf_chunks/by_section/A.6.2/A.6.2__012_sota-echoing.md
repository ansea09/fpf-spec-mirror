---
chunk_kind: "child"
pattern_id: "A.6.2"
pattern_title: "Effect-free episteme morphing"
section_id: "A.6.2:10.1"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.2/A.6.2__012_sota-echoing.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "A.6.2 — Effect-free episteme morphing"
  - "A.6.2:10.1 — SoTA-Echoing"
line_start: 14051
line_end: 14063
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

**Practice question.** What current transformation practice supports reusable definitions and composition while keeping execution and correctness evidence separate, and does it justify a universal repeat law?

| Source or practice | Contribution used here | Limit and disposition |
| --- | --- | --- |
| [Zhao et al., *KBX: Verified Model Synchronization via Formal Bidirectional Transformation* (2024)](https://arxiv.org/abs/2404.18771) | Separates formal BX definitions, generated synchronization, and consistency verification. | **Adapt.** Supports the declaration, arrow, application, and use-claim split. Its formal synchronizer does not make every arrow effect-free or idempotent in FPF. |
| [He and Zan, *BIT: A template-based approach to incremental and bidirectional model-to-text transformation* (2024)](https://doi.org/10.1016/j.jss.2024.112148) | Separates a user-facing surface language, formal core semantics, printer/parser execution, round-trip properties, and empirical cases; it also treats some computational effects explicitly. | **Adapt.** Supports a readable first route and explicit effect boundary. BIT's round-trip laws are construction-specific, not a universal EFEM idempotence law. |
| Category, optic, fibration, cospan, and BX traditions | Supply durable mathematical lineage for arrows, identities, composition, views, and correspondences. | **Retain as lineage.** Use the selected FormalSubstrate for the local mathematical theory; apply C.29 when the mathematics is used as a lens. Reject automatic F.9 Bridge, EntityOfConcern decision, or idempotence. |
| Current FPF C.2.1, C.29, A.6.3.RT, and A.6.4 | Separate episteme identity, mathematical-lens use, same-entity representation change, and changed-entity retargeting with a use-specific claim. | **Adopt.** These are the direct FPF boundaries. |

The thin EFEM arrow class is a bounded FPF synthesis.

