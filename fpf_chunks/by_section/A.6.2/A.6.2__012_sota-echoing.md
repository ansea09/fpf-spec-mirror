---
chunk_kind: "child"
pattern_id: "A.6.2"
pattern_title: "Effect-free episteme morphing"
section_id: "A.6.2:10.1"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.2/A.6.2__012_sota-echoing.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "A.6.2 — Effect-free episteme morphing"
  - "A.6.2:10.1 — SoTA-Echoing"
line_start: 13401
line_end: 13413
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

| Source or practice | Contribution used here | Limit and disposition | A.6.2 locus changed |
| --- | --- | --- | --- |
| [Zhao et al., *KBX: Verified Model Synchronization via Formal Bidirectional Transformation* (2024)](https://arxiv.org/abs/2404.18771) | Separates formal BX definitions, generated synchronization, and consistency verification. | **Adapt.** Supports the declaration, arrow, application, and use-claim split. Its formal synchronizer does not make every arrow effect-free or idempotent in FPF. | Sections 4.1, 4.2, P1, and CC-EFEM.1-5. |
| [He and Zan, *BIT: A template-based approach to incremental and bidirectional model-to-text transformation* (2024)](https://doi.org/10.1016/j.jss.2024.112148) | Separates a user-facing surface language, formal core semantics, printer/parser execution, round-trip properties, and empirical cases; it also treats some computational effects explicitly. | **Adapt.** Supports a readable first route and explicit effect boundary. BIT's round-trip laws are construction-specific, not a universal EFEM idempotence law. | P1, P3-P4, examples, and CC-EFEM.3-5. |
| Category, optic, fibration, cospan, and BX traditions | Supply durable mathematical lineage for arrows, identities, composition, views, and correspondences. | **Retain as lineage.** Use only through a declared C.29/FormalSubstrate lens. Reject automatic F.9 Bridge, EntityOfConcern decision, or idempotence. | P0-P5 and Relations. |
| Current FPF C.2.1, C.29, A.6.3.RT, and A.6.4 | Separate episteme identity, mathematical representation, same-entity representation change, and changed-entity retargeting with a use-specific claim. | **Adopt.** These are the direct FPF boundaries. | P0-P2, the Fourier branch, and the worked cases. |

The thin EFEM arrow class is a bounded FPF synthesis. Reopen it if a current transformation practice needs a different arrow identity or effect boundary, or if a concrete composition cannot be stated without collapsing the declaration, application, or correctness claim.

