---
chunk_kind: "child"
pattern_id: "E.17.EFP"
pattern_title: "ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces"
section_id: "E.17.EFP:11"
section_title: "SoTA Alignment: Adopted And Adapted Invariants And Rejected Shortcuts"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.EFP/E.17.EFP__012_sota-alignment-adopted-and-adapted-invariants-and-rejected-shortcuts.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "E.17.EFP — ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces"
  - "E.17.EFP:11 — SoTA Alignment: Adopted And Adapted Invariants And Rejected Shortcuts"
line_start: 76603
line_end: 76625
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.20"
  - "A.21"
  - "A.6.3.CSC"
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

### E.17.EFP:11 - SoTA Alignment: Adopted And Adapted Invariants And Rejected Shortcuts

**SoTA alignment rule.** Read each row here as source idea -> local FPF invariant -> practical local test -> popular shortcut rejected. A source citation governs nothing by reputation; it counts only when the cited idea is translated into the Solution, conformance checks, boundary rules, worked slices, and Relations of this pattern.

**Traditions covered.** This profile binds itself to architecture-description governance, explainability and reliability guidance, and faithfulness evaluation for natural-language explanations.

| Claim need | Source idea and current source | Current source section or reference | Local FPF invariant and practical local test | Adopted, adapted, or rejected shortcut |
|---|---|---|---|---|
| Explanation renderings remain subordinate to governed views, source `U.Episteme` or source `U.EpistemePublication`, source pins, and provenance references rather than quietly becoming a second semantic track. | Architecture-description practice keeps views, viewpoints, correspondences, and architecture descriptions explicit instead of letting reader-help prose replace governed source. | Joint ISO, IEC, and IEEE 42010:2022; source status = stable standard | `E.17.EFP` adopts this by keeping explanation on existing MVPK faces, tying class assignment to the source `U.Episteme` or source `U.EpistemePublication`, and rejecting a second face family or second semantic rule track. | **Adopt.** |
| Explanation quality is use- and audience-sensitive and keeps knowledge limits visible rather than collapsing all explanations into one generic mode. | Explainable-AI guidance distinguishes explanation obligations by user, purpose, and stated limits instead of one universal explanation class. | Phillips et al. (2021), *Four Principles of Explainable Artificial Intelligence*; source status = current government guidance | `E.17.EFP` adapts this into explicit explanation classes, bounded faces, and forbidden downstream uses, while keeping the `E.17` face system unchanged. | **Adopt and adapt.** |
| Faithfulness is not the same as plausibility; explanation evaluation stays tethered to the underlying source or decision source relation. | Faithfulness work in interpretable NLP treats explanation as source-sensitive and warns against equating persuasive prose with faithful interpretation. | Jacovi & Goldberg (2020), *Towards Faithfully Interpretable NLP Systems*; source status = research paper used for evaluation-use support | `E.17.EFP` adopts this by requiring source relation, `E.17:5.1b` source-relation class, evidence relation, pins, provenance, and class-per-rendering review rather than fluency alone. | **Adopt.** |
| Natural-language explanation needs explicit checking for faithfulness or self-consistency rather than trust in stylistic coherence. | Recent evaluation work treats natural-language explanation as a review problem with explicit faithfulness or self-consistency checks, not just readability. | Parcalabescu & Frank (2024), *On Measuring Faithfulness or Self-consistency of Natural Language Explanations*; source status = research paper used for evaluation-use support | `E.17.EFP` adapts this into bounded-use review, class downgrade, and reopen duties when source relation, evidence relation, or face assumptions no longer hold. | **Adapt.** |
| Retrieval-augmented generated explanations and source-linked generated explanations need separate checks for retrieved context, answer faithfulness, answer relevance, and source-relation quality. | RAG evaluation practice distinguishes context relevance for retrieval, answer faithfulness, answer relevance, and source-use dimensions instead of treating a retrieved context or citation-like link as reliability by itself. | Es et al. (2023), `RAGAS`; Saad-Falcon et al. (2023), `ARES`; source status = evaluation-method input, conditional on retrieval-facing explanation use. | `E.17.EFP` adapts this through `E.17:5.1b` distinctions such as `source-retrieved`, `source-used`, `source-faithful`, `claim-recoverable-from-source`, and `claim-plausible-only`; the practical test is that retrieved source, source-use relation, and operative claim recoverability remain separate before any explanation guides reliance. | **Adapt conditionally.** Use only when retrieval-facing explanation behavior or source-link behavior is present; reject making RAG metrics an FPF ontology or `authoritySourceRef` target. |
| Interactive explanations create extra interaction and source-relation demands: repeated queries, changing models and data, traceability, responsiveness, and reader-action boundaries. | Interactive-explanation work treats explanation as an information-systems architecture problem connecting reader interaction demands with system capabilities; source status = emerging arXiv preprint, not settled standard. | Labarta et al. (2026), *X-SYS: A Reference Architecture for Interactive Explanation Systems*, arXiv:2602.12748v3. | `E.17.EFP` adapts this narrowly through `targetUserModel`, `interactionMode`, `contrastiveQuestion`, `boundedReaderUse`, and `overreadRisk` when reader interaction is present, while full interactive explanation systems remain outside this profile. | **Adapt with source-status note.** Use as emerging source material for interaction-sensitive fields; reject treating it as a normative standard or as authority that static explanation prose is enough. |

**Architecture-description governance tradition.** `E.17.EFP` adopts the rule that reader-helpful renderings stay subordinate to the already governed source `U.Episteme` or source `U.EpistemePublication` rather than replacing it. Explanation therefore remains on existing faces and is judged against source claims, pins, and provenance references.

**Explainability and reliability traditions.** `E.17.EFP` adopts the distinction between source-bound explanation and merely plausible explanation prose. It rejects the still-popular shortcut in which fluent or pedagogically useful language is treated as sufficient evidence of explanation faithfulness.

**Local stance.** Best-known current practice points to a narrow rule: explanation renderings carry bounded use only when their class, source relation, evidence relation, bounded faces, and forbidden downstream uses remain visible enough that reader help does not become a second semantic rule track.

Action result from the explanation-faithfulness and retrieval-evaluation source set: fluent, source-linked, generated, retrieved, didactic, or pedagogically useful explanations do not become evidence, assurance, approval, gate passage, release reliance, work authority, or operative-claim-source relation by fluency, plausibility, citation-like wording, or retrieved context. The local E.17.EFP result is explanation class, source reference, bounded explanation use or source-finding state, blocked downstream use, and operative-claim mapping to `A.10` or another pattern governing the recovered claim only when reliance use is being made. Reopen the explanation-use result when the source claim set, pins, provenance, retrieved context, generated rendering, bounded face, use escalation, or source relation for an operative claim changes.

