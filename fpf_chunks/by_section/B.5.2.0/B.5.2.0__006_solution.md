---
chunk_kind: "child"
pattern_id: "B.5.2.0"
pattern_title: "Question Form for Entering Abduction (U.AbductivePrompt)"
section_id: "B.5.2.0:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2.0/B.5.2.0__006_solution.md"
commit_sha: "c3b34de07a6bd2df85c7081a4c367fd09978079c"
heading_path:
  - "B.5.2.0 — Question Form for Entering Abduction (U.AbductivePrompt)"
  - "B.5.2.0:4 — Solution"
line_start: 49657
line_end: 49721
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.6.3.RT"
  - "A.6.A"
  - "A.6.P"
  - "B.4.1"
  - "B.5.2"
  - "B.5.QD"
  - "C.16.Q"
  - "C.2.1"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.9.1"
keywords:
---

### B.5.2.0:4 - Solution
`U.AbductivePrompt` classifies the question accounts used for entry into `B.5.2`. Use `A.16`, `A.16.1` and `B.4.1` when the initiating cue needs preservation, clarification or selection of its next reasoning contribution. Use `A.16.0` only when the cue-to-prompt history itself needs an explicit trajectory account. Publish the account through a suitable form and ordinary MVPK faces; account membership and current entry depend on the content and grounds described below.

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

A prompt is not yet a hypothesis. Prompt admission usually presupposes articulation high enough to publish a stable open question and closure low enough that rival answers remain live; those articulation and closure thresholds remain governed by `C.2.4` and `C.2.5`, typically reached through cue or route provenance from `A.16.1` and `B.4.1`. The published account must satisfy those entry conditions; its layout supplies no additional admission.

##### B.5.2.0:4.2.1 - Identify the explanatory question

Identify the question from what the inquiry asks someone to explain:

- the subject and the fact, contrast or expected effect to be explained;
- the relevant population, conditions and time horizon in `scope`;
- the explanatory demand: what remains unknown and what an answer would have to explain.

Resolve the terms against their intended referents and interpretation. These three elements identify the question together. A change of wording, notation or publication preserves it when those elements retain their meaning. Two questions differ when a change in any element changes what an explanation must answer. A current list of rival hypotheses helps compare answers; it need not exhaust the possible answers and does not identify the question by itself.

Distinguish making an existing condition explicit from changing that condition. Use the earlier expression and its recoverable context to establish which happened. If a table drops an essential condition, first restore the damaged expression. When the earlier question cannot be recovered, leave its continuity unresolved; do not carry an earlier answer across the gap as an answer to the new formulation.

Motivating evidence and `promptSpecies` qualify the entry. Changing them changes the question only when it changes the explanatory demand, subject or relevant scope. A new observation can change the grounds for comparing explanations of the same event. Correcting the reported event can instead remove the reason to seek that explanation or raise a different question. A budget change affects question identity when the question concerns performance under that budget; a change in the resources available to investigate the same event need not do so.

This rule identifies the explanatory content of the question. An occasion on which someone asks it has its own occurrence identity.

##### B.5.2.0:4.2.2 - Identify the prompt account and check its use

A prompt account makes claims about one question identified under §4.2.1: what is being asked, its scope, how it arose and the grounds for treating it as open in the stated inquiry. The question is its exact `EntityOfConcern`. C.2.1 identifies that account as one `U.Episteme` through its claim content, the question and the effective `ReferenceScheme`.

Under `FPFCoreReferenceScheme`, that same episteme is a `U.AbductivePrompt` when its content records one recoverable explanatory question, a declared species with the conditions in §4.1, and the scope and motivating provenance in §4.2, while leaving rival answers open. Thus `U.AbductivePrompt(E)` implies `U.Episteme(E)` for the same individual. This is the same-individual-dependent membership rule. An unfilled layout, an underspecified cue and an account that asserts its preferred answer as settled fail this test for different reasons: no particular account, an unrecoverable question, or an answer-bearing account.

Use §4.2 and §17 to judge whether that account supports entry into B.5.2 now. An account can remain identifiable after its grounds have failed or its question has been answered. Keep it available as the earlier entry and record the warranted continuation; its earlier admission does not authorize a new run without current grounds.

The same question may have several accounts with different claims or effective schemes. Additional evidence changes account identity only when it changes one of C.2.1's identity constituents; adding an evidence relation alone need not do so. A reusable publication form can express different accounts. E.24.PUB governs the selected account's expression and publication; A.6.3.RT governs a prose-to-table transfer when that representation changes. A note containing several questions may express several prompt accounts in the same document.

On return to an earlier abductive inquiry, determine what changed before restarting it:

| Finding | Warranted continuation |
|---|---|
| Same question and account; different support or candidate ranking | Reconsider the affected rivals under B.5.2. |
| Same question; changed claims in its account | Identify the revised account under C.2.1 and reassess entry on its current grounds. |
| Changed explanatory demand, subject or relevant scope | State the new question and its relation to the earlier one; establish its own entry. |
| Several distinct questions were bundled | Separate their accounts and use B.5.2's split return. |
| An expression lost a condition needed to recover the question | Restore the expression before reusing the account or its answers. |
| The initiating ground fails or an adequate answer is already available | Abort or retire the current attempt as appropriate; preserve the earlier account and the reason for stopping. |

#### B.5.2.0:4.3 - Boundary rule
Only a declared prompt species carrying an explanatory question enters B.5.2 through this form. For a choice among available probes, actions or specialist options, use C.11. Use C.38 to develop incomplete alternatives for the same intended result, C.11.DUA to examine an unclear evidence demand, and C.19 when the question is policy over a still-live candidate pool. C.18 records generation and comparison results; C.22.1 describes an adaptation signature. Neither performs the missing choice. An explanatory subquestion arising during planning can still enter B.5.2 on its own grounds.

