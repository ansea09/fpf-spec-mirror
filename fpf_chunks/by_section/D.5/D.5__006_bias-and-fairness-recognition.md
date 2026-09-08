---
chunk_kind: "child"
pattern_id: "D.5"
pattern_title: "Bias Audit and Ethical Assurance"
section_id: "D.5:3"
section_title: "Bias and Fairness Recognition"
source_path: "FPF-Spec.md"
output_path: "by_section/D.5/D.5__006_bias-and-fairness-recognition.md"
commit_sha: "f6ee315e560a523f6381f264c03f46bcd3c7bdc0"
heading_path:
  - "D.5 — Bias Audit and Ethical Assurance"
  - "D.5:3 — Bias and Fairness Recognition"
line_start: 69673
line_end: 69721
dependencies:
  - "A.10"
  - "B.3"
  - "C.11.DUA"
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
| "This intervention makes outcomes fair." | Declare the causal fairness use, C.28 support components and causal-use support result. | `C.28` |
| "The model is unbiased." | Name represented and missing groups, data-generation limits, model-use limits, and evidence. | `A.10`, `C.16`, `D.5` |
| "The release is ethically assured." | Separate audit findings, mitigations, accepted residuals, and the assurance or evidence relation. | `B.3`, `D.5` |
| "The policy is acceptable because it helps the whole." | Check whether a multilevel conflict is live. | `D.2`, `D.3`, `D.4` |

#### D.5:3.1 - Optional Audit Records And Depth

D.5 may use a compact `BiasRegister@Context` when the live need is to keep concerns visible during ordinary work:

```text
BiasRegister@Context:
  auditedEntityOfConcernRef
  intendedUseRef
  claimScopeRef?: U.ClaimScope
  qualificationWindowRef?
  affectedPopulationRefs?
  affectedSystemRefs?
  biasConcernCode
  evidenceRefs
  mitigationOrConstraintRef?
  acceptedResidualRef?
  nextReviewTrigger?
```

Choose depth from the claim and consequence that the recipient needs to judge. A bounded finding, corrected metric statement, or identified conflict can complete the present use, including when it concerns an affected group or appears in a publication. Retain the limitation that prevents that result from being read as a wider fairness or assurance claim.

Use a fuller `BiasAuditReport@Context` when the receiving decision needs to inspect the combined evidence, mitigations, and residuals behind an audit or assurance conclusion. A consequential or reusable causal-fairness audit retains this report and the C.28 support it consumes. A release that relies on a particular protective claim needs the evidence and audit account required to support that claim. Reuse a matching existing account; after a material change, reopen the claims whose basis or use changed. The report is a Description episteme or publication-use object, with scope and depth set by that reliance.

A concrete indication of harm, a missing basis for an intended claim, or an applicable assurance requirement can make further investigation necessary before that use. Name what its result could change, who can obtain it, and whether its contribution warrants its full cost and delay; use `C.11.DUA` when this appraisal is unresolved. If the needed basis remains unavailable, state which intended claim remains unsupported and give any feasible narrower use, mitigation, or stop with its conditions. Neither a short record nor a large report supplies missing evidence.

Exposure, repetition, automation, publication, and changed populations are cues to examine the actual use and consequence. They do not by themselves prescribe a full audit or a separate explanation for omitting one. When a protective or documentation requirement is disputed, use `C.11.DUA` to examine its hazard, threshold basis, protective contribution, feasibility, and distributed burden, while keeping its current force and amendment authority explicit.

#### D.5:3.2 - Compact Bias Concern Taxonomy

| Code | Concern | Typical question |
| --- | --- | --- |
| REP | Representation, coverage, sampling, proxy choice, missing group, or shifted population. | Who or what is missing, over-weighted, proxied, or moved out of scope? |
| ALG | Algorithmic, modeling, objective, ranking, optimization, or threshold behavior. | Which model or optimization choice changes outcomes for whom? |
| VIS | Visibility, interface, dashboard, presentation, or publication framing. | What becomes easy to see, hard to see, or too authoritative by display? |
| MET | Metric, measurement, scale, comparator, normalization, or threshold. | What does the metric count, hide, compare, or turn into a pass or fail claim? |
| LNG | Language, naming, category, definition, group label, or claim wording. | Which words change what can be asserted, counted, blamed, or done? |

The codes are only concern locators. They do not replace the governed object, affected people or groups, intended use, evidence, mitigation, or accepted residual.

