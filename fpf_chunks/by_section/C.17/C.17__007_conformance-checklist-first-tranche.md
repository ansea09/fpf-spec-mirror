---
chunk_kind: "child"
pattern_id: "C.17"
pattern_title: "Characterising Generative Novelty & Value (Creativity‑CHR)"
section_id: "C.17:6"
section_title: "Conformance Checklist (first tranche)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.17/C.17__007_conformance-checklist-first-tranche.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "C.17 — Characterising Generative Novelty & Value (Creativity‑CHR)"
  - "C.17:6 — Conformance Checklist (first tranche)"
line_start: 49001
line_end: 49014
dependencies:
  - "A.1"
  - "A.10"
  - "A.13"
  - "A.15"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.2"
  - "A.2.6"
  - "B.1"
  - "B.3"
  - "B.4"
  - "B.5.2.1"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.9"
  - "D.1-D.5"
  - "E.5"
  - "F.18"
  - "F.5"
  - "F.6"
keywords:
  - "ConstraintFit"
  - "Creativity-CHR"
  - "Diversity_P"
  - "MM-CHR measurement templates"
  - "Novelty@context"
  - "Originality"
  - "ReferenceBase"
  - "ResourceEfficiency"
  - "Surprise"
  - "Use-Value and ValueGain"
  - "evidence"
  - "portfolio composition"
---

### C.17:6 - Conformance Checklist (first tranche)

| ID                                        | Requirement (normative)                                                                                                                                                                  | Purpose / audit hint                                          |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **CC‑CR‑1 (context‑locality)**               | Every **CreativityProfile** **MUST** name the **`U.BoundedContext`** and the **edition** of `U.CreativitySpace`.                                                                         | Prevents Cross‑context slippage.                                 |
| **CC‑CR‑2 (Declared bases)**              | **Novelty@context** claims **MUST** declare `ReferenceBase`, `SimilarityKernel`, and `TimeWindow`; **Surprise** claims **MUST** declare `GenerativePrior` and its training slice.                 | Makes “new to whom?” and “unexpected under what?” explicit.   |
| **CC‑CR‑3 (Objective anchor)**            | **ValueGain** **MUST** reference the **objective** (KPI/utility) and **counterfactual method** (if predicted, the model).                                                                | Stops free‑form value stories.                                |
| **CC‑CR‑4 (Must‑fit)**                    | If **must** constraints exist, **ConstraintFit** **MUST** be present; enactment decisions **SHALL** treat `ConstraintFit<1` as **fail** unless the current constitutive rule and an independently obtaining direct waiver-effect relation or decision result make that exact exception valid for the receiving constraint. A waiver SpeechAct occurrence alone is insufficient; without the governor, return `missing-governor` and keep the option ineligible. | Keeps safety and ethics non‑negotiable without mistaking communication for institutional effect. |
| **CC‑CR‑5 (Evidence)**                    | Each coordinate **MUST** have Evidence Graph Ref (neighbours, tests, logs, model cards).                                                                                                   | Enables audit & replication.                                  |
| **CC‑CR‑6 (Scopes)**                      | Profiles **MUST** include **USM scopes** (ClaimScope/WorkScope) relevant to measurement; off‑scope claims are advisory.                                                                  | Ties numbers to where they hold.                              |
| **CC‑CR‑7 (No scalarisation by default)** | The pattern **SHALL NOT** force a single scalar “creativity score.” If a Context defines one, it **MUST** publish the weighting and its drift policy.                                   | Keeps decisions on a Pareto frontier unless a policy opts‑in. |
| **CC‑CR‑8 (Bridge discipline)**           | Cross-context comparisons **MUST** use a **Bridge** with **CL** and recorded **losses**; any mapped coordinate **MUST** note penalties in the **R** lane, not silently alter the value.     | Honest portability. |
| **CC‑CR‑9 (Local retained-set measures)** | Every reported `FamilyCoverage`, `MinInterFamilyDistance`, `AliasRisk`, or `DescriptorVector` **MUST** cite its `RetainedSetMeasurementPolicyRef` and `ScaleRef`, plus the applicable `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and `CollisionPolicyRef`. The result **MUST** identify the retained set and **MUST NOT** be used as source-admission or universality evidence. | Keeps optional set characteristics reproducible and separate from selection. |

