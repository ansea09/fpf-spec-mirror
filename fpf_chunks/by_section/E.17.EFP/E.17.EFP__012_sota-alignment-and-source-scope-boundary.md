---
chunk_kind: "child"
pattern_id: "E.17.EFP"
pattern_title: "ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces"
section_id: "E.17.EFP:11"
section_title: "SoTA Alignment and Source-Scope Boundary"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.EFP/E.17.EFP__012_sota-alignment-and-source-scope-boundary.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "E.17.EFP — ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces"
  - "E.17.EFP:11 — SoTA Alignment and Source-Scope Boundary"
line_start: 83846
line_end: 83866
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.6.3.CR"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.B"
  - "A.7"
  - "B.3"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.ID.CR"
  - "F.18"
  - "F.9"
  - "U.MultiViewDescribing"
keywords:
---

### E.17.EFP:11 - SoTA Alignment and Source-Scope Boundary

**Source-use rule.** A source supports only claims within the problem population and action it actually studies. The external sources below concern AI explanations, NLP/model interpretations, LLM-generated explanations, RAG outputs, or interactive XAI systems. They do not establish a universal architecture for ordinary human-authored engineering notes.

| Claim need | Exact source and actual scope | Local use | Boundary or rejected transfer |
|---|---|---|---|
| Keep claim-bearing episteme, source-to-target relation, publication form, and carrier distinct. | Current FPF `C.2.1`, `A.6.3`, and `E.24.PUB`. | Apply the ClaimGraph identity branch before EFP classification. | This is current internal ontology, not a conclusion imported from an architecture-description standard. |
| Explanations of AI-system results are purpose- and recipient-sensitive and must state knowledge limits. | Phillips et al. (2021), *Four Principles of Explainable Artificial Intelligence*, NISTIR 8312, DOI `10.6028/NIST.IR.8312`; government-guidance lineage. | Adapt bounded reader use and explicit limits when an AI explanation is current. | Do not generalize this XAI guidance into mandatory fields or classes for every technical explanation, and do not present it as the whole current research line. |
| Plausibility and faithfulness of model interpretations are different evaluation questions. | Jacovi & Goldberg (2020), *Towards Faithfully Interpretable NLP Systems*, ACL DOI `10.18653/v1/2020.acl-main.386`; research lineage. | For NLP/model interpretation, do not infer faithfulness from persuasive prose. | The paper studies interpretable NLP systems, not ordinary human engineering exposition; later work further distinguishes self-consistency and intervention-based evaluation. |
| Output-level consistency tests for LLM explanations are not automatically tests of faithfulness to model internals. | Parcalabescu & Frank (2024), *On Measuring Faithfulness or Self-consistency of Natural Language Explanations*, ACL DOI `10.18653/v1/2024.acl-long.329`; later repair of an overclaim in the evaluation line. | Name the actual check as self-consistency when that is what it measures. | Apply only to generated/LLM explanation use; do not require it for human-authored notes. |
| Current LLM-explanation work tests faithfulness through model-behaviour intervention rather than surface plausibility alone. | Chuang et al. (2026), *FaithLM: Towards Faithful Explanations for Large Language Models*, EACL DOI `10.18653/v1/2026.eacl-long.177`; current research line. | Use an intervention-shaped evaluation only when the current task actually asks whether an LLM explanation reflects model decision behaviour. | EFP's source ClaimGraph comparison is not a FaithLM score and does not import model-internal faithfulness into ordinary engineering text. |
| Retrieval quality, answer faithfulness, and answer relevance are distinct RAG evaluation dimensions. | Es et al. (2023), *RAGAS*, arXiv:`2309.15217`; Saad-Falcon et al. (2023), *ARES*, arXiv:`2311.09476`; RAG-evaluation method lineage. | Keep retrieved context, source use, and claim recoverability separate for RAG-generated explanations. | These metrics do not define FPF ontology, do not exhaust current RAG evaluation, and do not apply without a retrieval pipeline. |
| Repeated queries, evolving models/data, responsiveness, and traceability create system-level demands for interactive XAI. | Labarta et al. (2026), *X-SYS: A Reference Architecture for Interactive Explanation Systems*, arXiv:`2602.12748v3`; current emerging preprint. | Use interaction-sensitive prompts only for an actual interactive explanation system. | Do not transfer a five-component XAI system architecture or its fields to a static human-authored note, and do not treat an emerging preprint as settled standard. |
| Decide whether ordinary human-authored engineering explanation needs EFP at all. | No external source in this set establishes EFP's four-class architecture for that population. Local evidence is the two-case task replay in E.17.EFP:5.7. | Prefer a source locator plus one bounded/blocked-use sentence when that performs the task. Use EFP only when class ambiguity changes action. | Present this branch as provisional local design rationale, not current external SoTA. Reopen if exact technical-writing, discourse, or decision-record evidence changes the comparison. |

**Source-grounded branch.** The XAI/NLP/RAG sources justify caution about generated or model-facing explanations: fluency, plausibility, retrieved context, or an `AI summary` label does not establish claim preservation, evidence, or reliance. They support the focused identity and use check only when that population is current.

**Local human-authored branch.** For ordinary human explanation, the architecture is justified only by the concrete local problem and the E.17.EFP:5.7 replay. The default is non-use when a simpler source-linked boundary sentence is equally comprehensible, preserves the claims, costs less, and prevents the same overread.

**Retained result.** Keep only the ClaimGraph identity screen, an explanation class when it changes the next action, the compact bounded/blocked use, and a reopen condition. Add reader-model, trace, provenance, evidence, RAG, self-consistency, or interactive-system details only when their exact source-scoped situation is present.

