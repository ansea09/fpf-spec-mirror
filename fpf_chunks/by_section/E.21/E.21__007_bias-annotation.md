---
chunk_kind: "child"
pattern_id: "E.21"
pattern_title: "FPF Pattern-Quality Evaluation CharacteristicSpace"
section_id: "E.21:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/E.21/E.21__007_bias-annotation.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "E.21 — FPF Pattern-Quality Evaluation CharacteristicSpace"
  - "E.21:6 — Bias-Annotation"
line_start: 67962
line_end: 67997
dependencies:
  - "A.17-A.19"
  - "A.19.ECS"
  - "A.6.P"
  - "C.16"
  - "C.2.P"
  - "C.25"
  - "E.10"
  - "E.11"
  - "E.19"
  - "E.2.DA"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9.DA"
  - "F.18"
  - "J.4"
keywords:
  - "and admissibility predicates are not written as duties"
  - "definitions"
  - "invariants"
  - "state agent obligations only"
  - "typing rules"
---

### E.21:6 - Bias-Annotation

`E.21` intentionally biases evaluation away from single scores, reviewer taste, and flat audit grids and toward activation-normalized characteristic spaces. This advances `P-1 Cognitive Elegance`, `P-2 Didactic Primacy`, `P-7 Pragmatic Utility`, `P-10 Open-Ended Evolution`, and `P-11 SoTA Alignment`.

Lens cautions:

| Lens | Bias to watch | Counter-move |
|---|---|---|
| Governance | A quality result may be overread as approval, release, or certification. | Keep `PatternQualityStatus` scoped to FPF pattern quality and name receiving project-side patterns separately. |
| Architecture | The pattern may centralize all quality concerns and steal authority from `E.8`, `E.19`, `C.16`, `C.25`, or `F.18`. | State exact relations and keep each neighbour's primary EntityOfConcern, evaluation claim or bundle, or exact relation intact. |
| Activation | The declared coordinate menu may become a hidden checklist. | Use activation classes and inactive-coordinate non-reading: inactive coordinates are outside the claim, not passes, waivers, or hidden failures. |
| Formal, corpus, and publication coordinates | Formal, corpus, and publication coordinates may become bureaucracy. | Activate them only when the pattern version or candidate edit changes those claims, entry or projection loci, names, relations, retrieval behavior, or corpus ecology. |
| Merged coordinates | A merged coordinate may hide a weak subreading. | A weak live subreading limits the coordinate value; do not average subreadings. |
| Onto/Epist | Quality terms may become generic umbrellas. | Use declared Characteristics, scales, kind-specific coordinates, and exact status values. |
| Pragmatic | The bundle may become too heavy for ordinary pattern drafts. | Keep the one-screen card as default and add telemetry/front/archive only when live. |
| Goodhart | The declared coordinates may become proxy objectives and displace the pattern-use value they were meant to protect. | Activate affordability/apparatus, change-impact, corpus/projection, and proxy-substitution coordinates when their cost changes admissible use; ask what got worse before stopping. |
| Didactic | Pareto/front language may obscure the reader's first move. | Pair every technical construct with the practical question it answers. |

#### E.21:6a - Architectural characteristics preserved by this pattern

| Architectural characteristic | How `E.21` preserves it | Failure to prevent |
|---|---|---|
| Auditability & traceability | `PatternQualityQBundle` pins version, scope, evidence, status, and stop condition; `ClaimJustificationTraceabilityCurrentnessAndReplayability` keeps claim justification replayable when claim justification is live. | Quality claims depending on chat memory, reviewer taste, or placement state. |
| Evolvability | `QualificationWindow`, `refreshNeeded`, bounded non-use, optional telemetry, and `EvolutionFrontAndRefreshDiscipline` reopen only the live locus. | Whole-pattern churn after small source, neighbour, or wording changes. |
| Modularity | `E.21` keeps authoring, review, measurement, naming, evidence, assurance, gate, work, and release claims under exact neighbouring patterns. | Central quality subsystem or shadow authority. |
| Composability | `NeighborAuthorityAndBoundedUseFit` and relation closure keep pattern-quality claims safe to compose with neighbouring patterns. | One pattern-quality read stealing another pattern's primary `EntityOfConcern`. |
| Usability | First-pass slice checks `firstMoveRecoverability`, `WorkingSituationAndUseBoundaryRecognizability`, and `ActionPathGuidance` before heavy apparatus. | Type-correct but inert pattern-quality control. |
| Affordability | `UseAffordabilityAndApparatusProportionality` and activation aspects keep ordinary reads light. | Review bureaucracy masquerading as quality. |
| Measurement integrity | Ordinal coordinate readings reject averages, percentages, and hidden normalization; `FormalClaimLegalityAndLensFit` activates only when formal claim kind or admissible-use boundary is live. | Illegal scalarization of pattern quality. |
| Goodhart resistance | Proxy-substitution checks ask what got worse when visible coordinates improved. | Rubric satisfaction replacing practical pattern-use value. |
| Corpus ecology | `ExternalEntryAndProjectionIntegrity` and `PatternLanguageEcologyFit` activate only when entry, projection, retrieval, name, relation, or corpus loci are changed or overread. | Local quality win that creates entry noise, stale echoes, name collisions, relation fanout, or shadow authority. |
| Scope safety | `PatternQualityStatus` remains scoped to the pattern-quality admissible-use result. | Overread as project assurance, safety/compliance certification, gate, release, or work authority. |
| Checkability | Status payload, `FalsifiabilityAndLoweringCondition`, and `StopCondition` make closure falsifiable for the declared use. | "Looks good enough" without inspectable stop reason. |

This table states which architectural characteristics `E.21` protects; it does not create a separate review process.

