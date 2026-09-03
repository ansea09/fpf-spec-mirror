---
chunk_kind: "child"
pattern_id: "A.6.4"
pattern_title: "EntityOfConcern retargeting"
section_id: "A.6.4:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.4/A.6.4__012_sota-echoing.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "A.6.4 — EntityOfConcern retargeting"
  - "A.6.4:11 — SoTA-Echoing"
line_start: 15919
line_end: 15931
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.6.0"
  - "A.6.1"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.5"
  - "A.7"
  - "B.3"
  - "C.2"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "E.10.D2"
  - "E.17"
  - "E.24.PUB"
  - "F.9"
keywords:
---

### A.6.4:11 - SoTA-Echoing

**Practice question.** What current transformation practice helps a reader keep a transformation definition, its execution, and a correctness claim separate—and what, if anything, can that practice say about whether the source and receiving epistemes concern different entities?

| Source or practice | Contribution used here | Limit and disposition | A.6.4 locus changed |
| --- | --- | --- | --- |
| [Zhao et al., *KBX: Verified Model Synchronization via Formal Bidirectional Transformation* (2024)](https://arxiv.org/abs/2404.18771) | KBX separates formal bidirectional-transformation definitions, generation of a synchronizer, and consistency verification. | **Adapt.** This supports the declaration, application, and use-claim split. KBX synchronizes models; it does not decide FPF EntityOfConcern identity or make one bounded use sound. | Sections 4.1-4.3 and checks 2-4 and 7. |
| [He and Zan, *BIT: A template-based approach to incremental and bidirectional model-to-text transformation* (2024)](https://doi.org/10.1016/j.jss.2024.112148) | BIT distinguishes a usable surface language, a formally defined core, executable printer/parser behavior, round-trip properties, and empirical cases. | **Adapt.** This supports keeping readable first use, formal declaration, execution, and well-behavedness evidence distinct. BIT's model/text synchronization does not decide whether two FPF epistemes concern different entities. | Practitioner entry, sections 4.1-4.3, and check 10. |
| Current FPF C.2.1, C.29, and A.6.3.RT | C.2.1 identifies each episteme and EntityOfConcern; C.29 bounds the mathematical lens; A.6.3.RT handles representation change with preserved EntityOfConcern. | **Adopt.** These are the direct identity and routing rules. | `Use this when`, section 4.4, Show 2, and check 8. |
| Fibrations, cospans, Fourier transforms, and data/model mappings | These provide mathematical lineage and stress cases for endpoints, composition, invariants, and loss. | **Retain as lineage; reject as ontology shortcut.** None proves that the EntityOfConcern changed or that a receiving use is sound. | Problem frame, ER-0 to ER-5, and Show 2. |

The A.6.4 split among r, q, and any application occurrence is a bounded FPF synthesis from these distinctions, not an externally established retargeting ontology. Reopen it if a current direct practice supplies a better identity rule, or if a concrete case cannot keep arrow identity stable while suitability changes across uses.

