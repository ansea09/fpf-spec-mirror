---
chunk_kind: "child"
pattern_id: "D.5"
pattern_title: "Bias Audit and Ethical Assurance"
section_id: "D.5:3"
section_title: "Bias and Fairness Recognition"
source_path: "FPF-Spec.md"
output_path: "by_section/D.5/D.5__006_bias-and-fairness-recognition.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "D.5 — Bias Audit and Ethical Assurance"
  - "D.5:3 — Bias and Fairness Recognition"
line_start: 67554
line_end: 67595
dependencies:
  - "A.10"
  - "B.3"
  - "C.16"
  - "C.28"
  - "D.1"
  - "D.2"
  - "D.3"
  - "D.4"
  - "E.13"
  - "E.17"
  - "E.5.4"
keywords:
---

### D.5:3 - Bias and Fairness Recognition

| Current claim | What D.5 requires | Neighboring owner |
| --- | --- | --- |
| "This metric shows the system is fair." | Distinguish metric disparity, proxy choice, subgroup impact, and intended use. | `C.16` for metric construction |
| "This intervention makes outcomes fair." | Declare the causal fairness use, C.28 evidence value, and causal-use verdict. | `C.28` |
| "The model is unbiased." | Name represented and missing groups, data-generation limits, model-use limits, and evidence. | `A.10`, `C.16`, `D.5` |
| "The release is ethically assured." | Separate audit findings, mitigations, accepted residuals, and the assurance or evidence relation. | `B.3`, `D.5` |
| "The policy is acceptable because it helps the whole." | Check whether a multilevel conflict is live. | `D.2`, `D.3`, `D.4` |

#### D.5:3.1 - Optional Audit Records And Depth

D.5 may use a compact `BiasRegister@Context` when the live need is to keep concerns visible during ordinary work:

```text
BiasRegister@Context:
  auditedEntityOfConcernRef
  intendedUseRef
  affectedPeopleOrGroupRefs?
  biasConcernCode
  evidenceRefs
  mitigationOrConstraintRef?
  acceptedResidualRef?
  nextReviewTrigger?
```

Use a fuller `BiasAuditReport@Context` only when the object is being released, relied on by other work, exposed to affected people or groups, used for assurance, or used after a material source-currentness, population, context, model, metric, or policy change. The report is a Description episteme or publication-use object; it does not make the audited object fair by existing.

Lightweight scan is enough when the intended use is local, reversible, low-impact, and the scan finds no affected group, proxy, metric, representation, causal-use, or publication-use concern. Deeper review is required when the use is consequential, repeated, automated, cross-context, externally published, safety-relevant, regulatorily or deontically constrained, or when an affected group, missing group, proxy variable, threshold, causal fairness claim, accepted residual, or assurance claim is current.

#### D.5:3.2 - Compact Bias Concern Taxonomy

| Code | Concern | Typical question |
| --- | --- | --- |
| REP | Representation, coverage, sampling, proxy choice, missing group, or shifted population. | Who or what is missing, over-weighted, proxied, or moved out of scope? |
| ALG | Algorithmic, modeling, objective, ranking, optimization, or threshold behavior. | Which model or optimization choice changes outcomes for whom? |
| VIS | Visibility, interface, dashboard, presentation, or publication framing. | What becomes easy to see, hard to see, or too authoritative by display? |
| MET | Metric, measurement, scale, comparator, normalization, or threshold. | What does the metric count, hide, compare, or turn into a pass or fail claim? |
| LNG | Language, naming, category, definition, group label, or claim wording. | Which words change what can be asserted, counted, blamed, or done? |

The codes are only concern locators. They do not replace the governed object, affected people or groups, intended use, evidence, mitigation, or accepted residual.

