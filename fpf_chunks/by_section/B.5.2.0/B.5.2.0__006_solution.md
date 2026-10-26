---
chunk_kind: "child"
pattern_id: "B.5.2.0"
pattern_title: "Question Form for Entering Abduction (U.AbductivePrompt)"
section_id: "B.5.2.0:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2.0/B.5.2.0__006_solution.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "B.5.2.0 — Question Form for Entering Abduction (U.AbductivePrompt)"
  - "B.5.2.0:4 — Solution"
line_start: 49422
line_end: 49449
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.6.A"
  - "A.6.P"
  - "B.4.1"
  - "B.5.2"
  - "C.16.Q"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "F.9.1"
keywords:
---

### B.5.2.0:4 - Solution
`U.AbductivePrompt` covers the prompt forms that may seed `B.5.2`. Use `A.16`, `A.16.1` and `B.4.1` when the initiating cue needs preservation, clarification or selection of its next reasoning contribution. Use `A.16.0` only when the cue-to-prompt history itself needs an explicit trajectory account. A prompt uses ordinary MVPK faces; its prompt status belongs to the publication form and remains distinct from its face.

#### B.5.2.0:4.1 - Starter canonical species and conditional extension species
- starter canonical species:
  - `AnomalyStatement`
  - `ProblemCuePrompt`
  - `OpportunityCuePrompt`
  - `ProbeCuePrompt`
- conditional extension species:
  - `TaskFamilySpecializationPrompt`
  - `AdaptationProbePrompt`
  - `NonHumanUtilityPrompt`
  - `SubstrateDiversificationPrompt`

##### B.5.2.0:4.1.1 - Specialization-sensitive prompt species
These extension species are admissible only when cue provenance or trajectory account already carries the bounded-specialization evidence requirement by value; they are not the starter canonical entry set for ordinary abduction.

`TaskFamilySpecializationPrompt` asks what explains a performance difference within the declared task family. `AdaptationProbePrompt` asks which rival explanations predict whether a proposed adaptation can reach the stated threshold. `NonHumanUtilityPrompt` asks what could explain the indicated utility advantage of a low-human-overlap approach. `SubstrateDiversificationPrompt` asks what explains the indicated limitation of the current substrate. In each species, B.5.2 returns qualified explanatory conjectures; task family, utility target, threshold, budget and motivating evidence qualify that question.

#### B.5.2.0:4.2 - Core shape
A conforming abductive prompt makes `promptSpecies`, its explanatory `openQuestion`, `scope` and motivating provenance explicit. The provenance may be carried by `motivatingCueRef`, `witnessRefs` or `routeProvenance`; include the applicable basis even when no routing history exists. A rendering may additionally include `contrastSet` and `GammaTime`.

A prompt is not yet a hypothesis. Prompt admission usually presupposes articulation high enough to publish a stable open question and closure low enough that rival answers remain live; those articulation and closure thresholds remain governed by `C.2.4` and `C.2.5`, typically reached through cue or route provenance from `A.16.1` and `B.4.1`. It is the initiating publication form that licenses entry into the abductive loop.

#### B.5.2.0:4.3 - Boundary rule
Only a declared prompt species carrying an explanatory question enters B.5.2 through this form. For a choice among available probes, actions or specialist options, use C.11. Use C.38 to develop incomplete alternatives for the same intended result, C.11.DUA to examine an unclear evidence demand, and C.19 when the question is policy over a still-live candidate pool. C.18 records generation and comparison results; C.22.1 describes an adaptation signature. Neither performs the missing choice. An explanatory subquestion arising during planning can still enter B.5.2 on its own grounds.

