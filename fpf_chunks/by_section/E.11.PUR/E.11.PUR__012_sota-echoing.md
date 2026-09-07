---
chunk_kind: "child"
pattern_id: "E.11.PUR"
pattern_title: "Pattern-Use Applicability, Recommendation, and Coordination"
section_id: "E.11.PUR:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PUR/E.11.PUR__012_sota-echoing.md"
commit_sha: "d514a6fcb7908af8e773ed054b9582394f755caf"
heading_path:
  - "E.11.PUR — Pattern-Use Applicability, Recommendation, and Coordination"
  - "E.11.PUR:11 — SoTA-Echoing"
line_start: 80042
line_end: 80057
dependencies:
  - "A.10"
  - "A.15"
  - "A.19"
  - "A.19.CPM"
  - "A.19.ECS"
  - "A.21"
  - "A.6.5"
  - "C.22.PFR"
  - "C.24"
  - "C.30"
  - "E.10.MOVE"
  - "E.11"
  - "E.11.PUA"
  - "E.18"
  - "E.18.1"
  - "G.11"
keywords:
---

### E.11.PUR:11 - SoTA-Echoing

| Source or practice line | Problem-solving move taken here | Adoption and boundary |
| --- | --- | --- |
| Que et al., *LLM-as-a-Judge for Reliable and Explainable Offline Evaluation in Top-K Recommendation*, KDD 2026, arXiv:2606.22961 | Observed feedback and Top-K scores can be biased proxies; pair a judgement with explicit rationale rather than treating the score as self-explanatory. | Adapt the proxy warning and rationale pressure to current candidate fit and expected-result reasoning. Reject the recommender, Top-K, user-profile, and LLM-judge ontology as a model of FPF recommendation authority. |
| Nunes and Jannach, *A Systematic Review and Taxonomy of Explanations in Decision Support and Recommender Systems*, User Modeling and User-Adapted Interaction 27 (2017) | Lineage for separating recommendation explanation functions and making reasons addressable to a receiving decision. | Retain as lineage, not current-best evidence. Candidate and coordination rationales do not prove applicability or authorize action. |
| Jin, Bai, and Oulasvirta, *Modeling Trial-and-Error Navigation With a Sequential Decision Model of Information Scent*, arXiv:2603.11759 (2026) | Preserve bounded search, wrong-turn recovery, and reconsideration under limited attention. | Adapt to candidate reconsideration and return boundaries. The preprint does not decide recommendation authority or record cardinality. |
| Current FPF NQD and OEE lines together with A.19 comparison practice | Preserve plural candidates, non-dominated alternatives, explicit comparison spaces, and dynamic reconsideration. | Adopt the plurality discipline. PUR coordinates pattern uses but does not replace subject-domain candidate evaluation. |
| Current FPF `C.2.1`, `A.10`, and `G.11` result-identity, reliance, and currentness line | Compare the earlier result under its direct subject pattern, then state later reliance and currentness separately. | Adopt the separation. Reuse ends repeated work only when the result's relevant values still match; the branch creates no generic result-reuse relation. |

The practical implication is to recommend a use for its expected result, not for its familiarity or score, to stop on an earlier result that still answers the concern, and to add order only where a real dependency exists.

Que et al. is the current decision-bearing recommender source in this narrow use; Nunes and Jannach supplies lineage. The 2026 navigation preprint supplies bounded reconsideration, while current FPF NQD, OEE, A.19, C.2.1, A.10, and G.11 supply the transdisciplinary candidate, comparison, result-identity, reliance, and currentness basis. These sources change `4.1-4.5`, `5.1.1`, and `5.6`; none decides FPF kinds or recommendation authority.

Reopen the score-proxy adaptation when stronger evaluation evidence shows that the relied-on score tracks current expected-result and receiving-use fit without the identified exposure or rationale loss. Reopen the wrong-turn adaptation when peer review, replication, or use evidence changes the value of reconsideration. Use `G.11` to manage source and telemetry currentness, then revise the affected PUR fit, rationale, recommendation, or return relation.

