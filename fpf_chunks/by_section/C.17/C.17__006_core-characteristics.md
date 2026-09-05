---
chunk_kind: "child"
pattern_id: "C.17"
pattern_title: "Characterising Generative Novelty and Value"
section_id: "C.17:4"
section_title: "Core characteristics"
source_path: "FPF-Spec.md"
output_path: "by_section/C.17/C.17__006_core-characteristics.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "C.17 — Characterising Generative Novelty and Value"
  - "C.17:4 — Core characteristics"
line_start: 49550
line_end: 49600
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
  - "A.2.1"
  - "A.3.1"
  - "A.3.2"
  - "A.6.1"
  - "B.1.6"
  - "B.3"
  - "B.4"
  - "C.11"
  - "C.11.CRC"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "E.10.LRN"
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

### C.17:4 - Core characteristics

Each selected characteristic has a declared Scale, polarity, admissible operations, missingness rule, and evidence route. An ordinal value is not averaged unless a declared model justifies an interval interpretation.

#### C.17:4.1 - Novelty: unlike which admitted set?

Novelty describes supported difference from a finite comparison corpus under one declared similarity Method. When that Method returns a calibrated similarity result on `[0,1]` for each like-for-like comparison, that source result keeps its declared Similarity Scale. The following transformation defines a bounded value on a corresponding declared Novelty Scale, whose meaning is difference from the corpus and whose positive polarity increases as maximum similarity falls:

`Novelty = 1 - max similarity(bearer, corpus member)`

A declared normalization to `[0,1]` may be part of the Method; state its source Scale and transformation. If the Method uses another similarity or distance Scale, state the lawful coordinate construction and resulting Scale instead of reusing this formula. Subtracting an unrestricted result from one does not make it bounded.

When the Method compares representations or observations rather than the evaluated bearers themselves, name each bearer and the value actually compared, together with the describing, projection, measurement, or other stated relation that lets the comparison support the bearer-level claim. Use a compatible basis for corpus members, or state the mapping and relevant loss. A direct like-for-like comparison of epistemes needs no extra representation relation.

A robust top-k variant is allowed when declared. The result identifies the Novelty Characteristic and Scale editions, corpus and inclusion rule, source editions, comparison window, Method, model or encoder edition, distance definition, invariances, calibration, uncertainty, ClaimScope, evidence, and intended use. Changing any load-bearing element creates a different comparison basis or result edition.
Those identifiers make the result reproducible; they do not by themselves show that the value is robust. When the value materially affects a comparison or pool treatment, use diagnostics suited to the claim. For example, inspect the nearest corpus members and their distances, repeat the reading with a plausible alternative corpus or similarity Method and report the sensitivity, and remove a claimed invariance to see whether it materially changes the result. These are bounded diagnostic examples, not one mandatory algorithm. If no robustness check was performed, report the supported value and uncertainty without calling it robust.

Novelty is neither timeless originality nor a property detached from its comparison basis. A label such as `Novelty@context` is not an executable input and must not substitute for the result chain.

#### C.17:4.2 - Use-Value: useful for which objective?

Use-Value, historically also called `ValueGain`, reports the bearer's supported usefulness or contribution to one declared objective or acceptance criterion. An ordinary usefulness statement may use an ordinal Scale such as `Fail | Partial | Pass`; it does not need a counterfactual merely because the bearer is useful for the stated purpose.

When the result claims an improvement or gain, identify both the baseline and the comparison or counterfactual Method that makes the difference meaningful. One bounded measured construction is `ValueGain = metric_after - metric_before` under a fixed metric and window. An A/B comparison, back-test, or causal-inference Method may provide the comparison when it fits the claim. Cite the before and after measurements and the Work or other evidence on which they rely. A predicted gain identifies its model, error, baseline, and intended later update. Without a baseline and an appropriate comparison Method, say what usefulness is supported; do not report an observed gain.

Use-Value may be one member of a declared Q-set, but it is not the whole Q-set by default. If it stays outside Q, name its actual use as a side condition or tie-breaker. Do not silently promote Novelty, Surprise, `DeltaDiversity_P`, or Illumination into dominance.

#### C.17:4.3 - Surprise: unexpected under which model?

Surprise reports how improbable one declared sample of the bearer is under one generative model. For a discrete probability, a common raw result is `-log p(sample)` in bits or nats. State the modeled sample unit and encoding and how bearer size is handled. Compare bearers only under a justified common extent, a declared per-unit or code-length normalization, or another calibrated rule suited to the model. For a continuous model, identify the measure as well as the representation; a density value alone is not representation-independent. Otherwise keep the raw model result within its exact basis and do not treat it as a comparable Surprise coordinate. Also identify the model episteme and edition, training basis, preprocessing, fit and out-of-distribution checks, calibration, refresh condition, and limits.

Novelty and Surprise answer different questions. A bearer may be unlike the selected corpus yet unsurprising under a broad model, or close to known examples yet surprising under a narrow model. Keep both results visible when both matter.

#### C.17:4.4 - ConstraintFit: which must-criteria hold?

ConstraintFit reports satisfaction of the declared must-constraints under their predicates and source epistemes. Use `E.5`, `D.1`-`D.5`, or a service-acceptance pattern only when it supplies the actual predicate or source for the current must-criterion. A ratio such as `passed declared must-constraints / all declared must-constraints` is allowed when the set and any criticality weights are explicit.

A failing must-constraint makes the bearer ineligible for the affected use unless the receiving constraint or decision pattern recognizes an independently obtaining exception or waiver effect. A waiver speech act alone does not change eligibility. If no pattern defines the needed effect, return the missing relation rather than treating communication as authorization.

#### C.17:4.5 - AttributionIntegrity

AttributionIntegrity reports how completely the applicable provenance, authorship, source, and licence duties are met. First identify the duty set and the source that makes each duty applicable. One bounded local construction is `satisfied required duties / all applicable required duties` on a declared ratio Scale; mark unresolved and inapplicable duties separately rather than treating them as satisfied. Provenance links, licence scans, and acknowledgements are example evidence routes.

When the applicable-duty set is empty, do not compute the ratio. Omit AttributionIntegrity when the receiving use does not need it; when that use needs an explicit disposition, return `not applicable` under the declared Scale and missingness rule. That disposition is not a pass and cannot by itself pass a filter, break a tie, establish legal adequacy, or satisfy a must-constraint. Keep it distinct from an unresolved duty that does apply.

This reading does not by itself establish legal adequacy. It is measurable but not in the default dominance set; an applicable policy may use it as a filter or tie-breaker. When a duty is a must-constraint, its pass or failure belongs in ConstraintFit and affects eligibility there.

#### C.17:4.6 - EffortCost

EffortCost reports actual resource outlay through `A.15.1` dated Work, `B.1.6` resource aggregation, `C.16` measurement, and `A.10` evidence. Planned effort remains `A.15.2` WorkPlan content. Use cost-normalized readings for planning or comparison only under a declared rule; cost is not itself creativity, and a profile does not carry operational actuals.

