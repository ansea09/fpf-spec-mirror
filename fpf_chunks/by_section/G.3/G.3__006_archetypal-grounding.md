---
chunk_kind: "child"
pattern_id: "G.3"
pattern_title: "CHR Authoring for a CG‑Frame: Characteristics, Scales, Levels, Coordinates"
section_id: "G.3:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/G.3/G.3__006_archetypal-grounding.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "G.3 — CHR Authoring for a CG‑Frame: Characteristics, Scales, Levels, Coordinates"
  - "G.3:5 — Archetypal Grounding"
line_start: 89430
line_end: 89457
dependencies:
  - "A.10"
  - "A.15.3"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.CHR"
  - "B.3"
  - "B.3.4"
  - "C.16"
  - "C.18"
  - "C.19"
  - "E.10"
  - "E.5.1"
  - "E.5.3"
  - "F.1"
  - "F.17"
  - "F.9"
  - "G.0"
  - "G.1"
  - "G.10"
  - "G.11"
  - "G.2"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.Core"
keywords:
  - "CHR Pack@CG-Frame"
  - "CHR authoring"
  - "CSLC lawfulness"
  - "RSCRTriggerKindId"
  - "ReferencePlane"
  - "characteristics"
  - "coordinates"
  - "edition pins"
  - "levels"
  - "scales"
  - "typed measurement"
  - "Φ/CL policy pins"
---

### G.3:5 - Archetypal Grounding

**AG‑1 — ML fairness auditing (post‑2015 selective and set‑valued practice).**
*System:* a CG‑Frame for evaluating deployed classifiers across cohorts with explicit abstention/defer behavior.
*CHR authoring:* publish `DemographicParityGap` and `EqualizedOddsGap` as Characteristics with:

* explicit ReferencePlane (deployment population + sampling regime),
* `ObservableOf` (audit protocol + uncertainty model + window),
* interval scale (bounded; zero semantics explicit),
* missingness semantics (cohort sparsity and label noise are typed),
* legality surfaces and guard surfaces that forbid illicit cohort mixing and require explicit proof hooks for aggregation across cohorts.

*Downstream:* CAL acceptance binds thresholds and failure behavior; selector remains set‑returning under partial orders and may treat “defer/abstain” as a first‑class outcome (tri‑state semantics pinned through `G.Core`).

**AG‑2 — Clinical diagnostics (post‑2015 evidence‑aware evaluation).**
*System:* a CG‑Frame for comparing diagnostic pipelines under evolving datasets and protocols.
*CHR authoring:* publish `Sensitivity` and `Specificity` as ratio‑scale, dimensionless Characteristics on `[0,1]`, with:

* explicit `ObservableOf` (trial protocol, inclusion criteria, uncertainty model),
* freshness/decay expectations (protocol drift is modelled as decay),
* legality surfaces that forbid averaging incompatible ordinal labels (e.g., severity grades) and require explicit unit/exposure constraints for any derived rate.

*Downstream:* CAL acceptance governs thresholds and guard‑bands; evidence wiring is cited via Path/PathSlice to make refresh triggers actionable.

**AG‑3 — Quality‑Diversity / Illumination (post‑2015 MAP‑Elites/CMA‑ME lineage).**
*System:* a CG‑Frame where selection returns archives/fronts rather than a single winner.
*CHR authoring:* declare which Characteristics play Q/D/QD‑score roles and pin the metric definitions (descriptor map, distance definition, method editions) so archives are reproducible across runs and refresh can be triggered on edition changes. CHR does not scalarize partial orders; set‑return semantics are pinned through `G.Core`.

