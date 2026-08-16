---
chunk_kind: "child"
pattern_id: "C.17"
pattern_title: "Characterising Generative Novelty and Value"
section_id: "C.17:14"
section_title: "SoTA-Echoing and source use"
source_path: "FPF-Spec.md"
output_path: "by_section/C.17/C.17__016_sota-echoing-and-source-use.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "C.17 — Characterising Generative Novelty and Value"
  - "C.17:14 — SoTA-Echoing and source use"
line_start: 48860
line_end: 48872
dependencies:
  - "A.0"
  - "A.1.1"
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.15.2"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.ECS"
  - "A.3.1"
  - "A.3.2"
  - "A.6.1"
  - "B.1.6"
  - "B.3"
  - "B.4"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "F.18"
  - "F.6"
  - "F.9"
  - "G.11"
  - "G.5"
  - "U.Mechanism"
keywords:
  - "ConstraintFit"
  - "Novelty"
  - "Use-Value"
  - "bounded quantitative result"
  - "evidence"
  - "incomparability"
  - "named comparison basis"
  - "qualitative-first evaluation"
  - "uncertainty"
---

### C.17:14 - SoTA-Echoing and source use

**Source-currentness boundary (reviewed through 2026-08-15).** The sources below were selected because they change what a C.17 user inspects or reports. They do not install one creativity theory, automated judge, metric, or search algorithm as the FPF default. Reopen this source-use judgement when a cited source is corrected, retracted, or materially superseded; when new cross-domain evidence overturns one of the stated consequences; or when a proposal would make one automated metric, corpus, encoder, QD descriptor, or proxy score normative. Use `G.11` for that refresh.

| Current practice and source | Source-use decision | Concrete C.17 consequence |
| --- | --- | --- |
| Judge novelty and usefulness as distinct, context-dependent questions. Harvey and Berry, `Toward a Meta-Theory of Creativity Forms: How Novelty and Usefulness Shape Creativity`, *Academy of Management Review* 48(3):504-529 (2023), DOI `10.5465/amr.2020.0110`; Sen et al., `Automated Creativity Evaluation of Language Models Across Open-Ended Tasks`, ACL 2026, DOI `10.18653/v1/2026.acl-long.1061`. | **Adopt** the separation of creative breadth from task fulfilment and the dependence of usefulness on the practical situation. **Adapt** it by using the named comparison basis, Use-Value, and ConstraintFit already defined here. **Reject** a context-free creativity score and the cited paper's particular semantic-entropy or automated-judge machinery as universal FPF measures. | The first move names both what the bearer differs from and which objective or must-criterion matters. Approval-facing use cannot substitute Novelty for Use-Value or ConstraintFit; `CC-C17-1`, `CC-C17-5`, and `CC-C17-8` test that boundary. |
| Preserve a collection of different locally strong alternatives when the question needs coverage rather than one winner. Qin et al., `A survey on Quality-Diversity optimization: Approaches, applications, and challenges`, *Swarm and Evolutionary Computation* 100:102240 (2026), DOI `10.1016/j.swevo.2025.102240`. | **Adopt** the quality-diversity and illumination insight that coverage and local quality can matter together. **Adapt** it as `Diversity_P`, Illumination, or another declared retained-set reading. **Reject** MAP-Elites, a QD score, feature descriptor, container, or quota as a default C.17 method or selection rule. | A set reading stays telemetry with its bearer, rule, Scale, and evidence. Use `C.18` for Archive and Front maintenance, `C.19` for pool treatment, and `G.5` for selector-facing declarations; `CC-C17-9` and `CC-C17-10` keep these moves separate. |
| Test whether a result survives reasonable corpus, metric, and representation choices. Lu et al., `Rethinking Creativity Evaluation: A Critical Analysis of Existing Creativity Evaluations`, EACL 2026, DOI `10.18653/v1/2026.eacl-long.297`; Stein et al., `Exposing Flaws of Generative Model Evaluation Metrics and Their Unfair Treatment of Diffusion Models`, NeurIPS 2023, DOI `10.52202/075280-0165`. | **Adopt** sensitivity checking and comparison with evidence suited to the receiving domain. **Adapt** it by making the corpus, inclusion rule, Method, model or encoder, distance, calibration, and uncertainty part of the claim. **Reject** transfer of one metric across domains, minor prompt or implementation stability as validity, and leaderboard standing as evidence of the bearer characteristic. | For a load-bearing value, inspect neighbours and run the applicable corpus/Method sensitivity or invariance probe. If the conclusion changes, report that dependence or incomparability instead of hiding it in one score; `CC-C17-4` and `CC-C17-11` make this visible. |
| Check whether optimizing a proxy stops improving the result that matters. Gao, Schulman, and Hilton, `Scaling Laws for Reward Model Overoptimization`, ICML 2023, PMLR 202:10835-10866, `https://proceedings.mlr.press/v202/gao23h.html`. | **Adopt** the warning that further proxy optimization can reduce performance under a separate target judgement. **Adapt** it by retaining primitive coordinates, gates, evidence, and held-out or delayed observations and by giving the local result a stop or reopen condition. **Reject** the reward-model setting or its fitted scaling law as a universal degradation model, and reject a rising proxy score as evidence that the bearer improved. | The design and policy cases keep tooling and legal or equity gates visible even when another value improves. Scalarization never erases the primitive coordinates; later target evidence can reopen only the claims that relied on the proxy. |

These decisions reinforce the existing route rather than add another assurance layer. In the pump case, inspect the admitted design set and tooling constraint; in the hospital case, keep the held-out result separate from unsupported transfer; in the policy case, keep the missing subgroup evidence as an eligibility gap. The source record therefore changes the comparison and robustness work already required by the cases and checklist, not the practitioner-first entry.

