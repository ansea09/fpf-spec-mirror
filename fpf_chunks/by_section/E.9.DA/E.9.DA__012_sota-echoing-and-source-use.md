---
chunk_kind: "child"
pattern_id: "E.9.DA"
pattern_title: "DRR Decision-Adequacy Evaluation CharacteristicSpace"
section_id: "E.9.DA:11"
section_title: "SoTA-Echoing and source use"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9.DA/E.9.DA__012_sota-echoing-and-source-use.md"
commit_sha: "c7ac61bbaa8d3c10165b1a5a4a350956c87d77c9"
heading_path:
  - "E.9.DA — DRR Decision-Adequacy Evaluation CharacteristicSpace"
  - "E.9.DA:11 — SoTA-Echoing and source use"
line_start: 72489
line_end: 72501
dependencies:
  - "A.19.ECS"
  - "E.10"
  - "E.19"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9"
  - "F.19"
keywords:
---

### E.9.DA:11 - SoTA-Echoing and source use

| Practice question | Exact source and status | Selected payload and disposition | Changed E.9.DA locus | Qualification and smallest reopen condition |
|---|---|---|---|---|
| How much structure should the first decision result expose? | Nogueira, Silva, and Conte, [*One Size Fits All? An Empirical Comparison of ADR Templates regarding Comprehension, Usability, and Ease of Adoption*](https://arxiv.org/abs/2604.27333), 2026 preprint — current empirical comparator for ADR-form usability. | **Adapt.** The study's controlled comparison favours Nygard's concise and objective form overall, while participant feedback identifies MADR's advantage for structural detail and specific requirements. E.9.DA therefore keeps a short ordinary result and adds detail only for a named reliance. **Reject** one universal record shape or the inference that the longest template is the most adequate decision. | §§4, 4.6, and 5: ordinary result first; reliance-bearing extension second. | Qualified on 2026-08-15 for the reported student experiment and five templates. Reopen these loci if a stronger practitioner study reverses the form trade-off or shows that a named E.9.DA use needs a different minimum. |
| How should a reviewer treat fluent, reconstructed, or generated rationale? | Zhou, Li, Liang, et al., [*Using LLMs in Generating Design Rationale for Software Architecture Decisions*](https://arxiv.org/abs/2504.20781), 2025 preprint — current empirical stress line for rationale completeness and misleading additions. | **Adapt, with a domain boundary.** In the reported 100-problem study, generated rationale had incomplete recall and a small but real share of potentially misleading arguments. E.9.DA does not generalize those rates to all DRRs; it uses the result to reject fluency, source volume, or recovered prose as completeness evidence and to require one bounded search for an important omitted question. | §§4, 4.4, 4.4a, 5, and `CC-E9DA-0b/9`. | Qualified on 2026-08-15 for generated software-architecture rationale, not all human-authored decisions. Reopen if better direct evidence changes the omission/misleading-risk answer or supplies a more effective low-cost completeness test. |
| Which architecture-description distinctions may an architecture-facing DRR reuse? | [ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74393.html), *Software, systems and enterprise — Architecture description* — current-standard reference, not SoTA by official status. | **Adopt narrowly.** Reuse the standard's explicit separation between an entity's architecture and an architecture description, and its boundary that the standard does not define the architecting process or recording medium. **Reject** treating the standard, an architecture description, a viewpoint, or a model as the DRR adequacy method or as the architecture decision itself. | `ArchitectureSourceAndViewLossClosure`, the architecture-impact slice, and Relations. | Qualified to the published 2022 edition checked on 2026-08-15. Reopen only if a relied-on distinction changes; a later edition number alone does not make the standard a better adequacy method. |
| How should an actionable finding connect present condition, desired condition, and next move? | Sadler, [*Formative assessment and the design of instructional systems*](https://doi.org/10.1007/BF00117714), 1989, and Hattie and Timperley, [*The Power of Feedback*](https://doi.org/10.3102/003465430298487), 2007 — retained feedback lineage, with current FPF use carried through E.22 and E.23 rather than claimed as new SoTA. | **Adapt as lineage.** Keep the gap, evidence locus, first repair or drafting action, and reopen condition together so a finding changes the next move. **Reject** praise, a score, or a condition label without an action-changing diagnosis. | §§4.4a, 4.5–4.7, the worked case, and finding-related checks. | Retained because the desired/current/next-action distinction still answers this narrow feedback question and is used by E.22/E.23. Reopen only if a better feedback result changes that action structure, not because the sources are old. |
| How should several adequacy dimensions and trade-offs remain visible? | Qin et al., [*A survey on Quality-Diversity optimization: Approaches, applications, and challenges*](https://doi.org/10.1016/j.swevo.2025.102240), *Swarm and Evolutionary Computation* 100 (2026) 102240 — current multi-dimensional optimization overview; MCDA and Pareto practice remain design lineage. | **Adapt only the preserved-dimension lesson.** E.9.DA keeps distinct coordinates, adjacent-value reasons, and visible trade-offs; it does not average them or import a QD archive, algorithm, fitness function, or selection mechanism into DRR review. The effective-floor rule is noncompensatory. | §§4.3–4.5, calibration, Consequences, and `CC-E9DA-8/10/11`. | Qualified on 2026-08-15 for the current overview's quality-plus-diversity separation. Reopen if the selected dimensions no longer lead to distinct repair questions or a better decision-evaluation practice preserves the same distinctions at lower use cost. |
| What prevents decision-adequacy values from replacing decision usefulness? | Karwowski et al., [*Goodhart's Law in Reinforcement Learning*](https://proceedings.iclr.cc/paper_files/paper/2024/hash/6ad68a54eaa8f9bf6ac698b02ec05048-Abstract-Conference.html), ICLR 2024 — current theoretical and empirical proxy-optimization branch; Goodhart and Campbell remain lineage. | **Adapt.** Treat the ordinal value as an imperfect proxy claim, ask what became worse, and stop value-directed repair when it improves the visible score without strengthening the selected answer or first action. **Reject** all-`5`, `5`-defensible, source-count, or checklist-completion targeting. | Problem failure 9; §§4.4a and 4.7; `CC-E9DA-8/11`; the Goodharted-DRR anti-pattern. | Qualified on 2026-08-15 as a proxy-risk result, not as an assertion that DRR review is reinforcement learning. Reopen if better proxy-risk work changes the early-stop or protected-value answer used here. |

The current-best source set spans empirical decision-document use, rationale-completeness risk, multi-dimensional evaluation, and proxy optimization. ISO/IEC/IEEE 42010 is deliberately kept as a narrow current-standard reference; the feedback, MCDA, Pareto, Goodhart, and Campbell traditions remain lineage where the current rows or neighbouring FPF patterns carry the present answer. A new publication date, official status, citation count, or popular template does not by itself reopen any row.

