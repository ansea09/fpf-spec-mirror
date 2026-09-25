---
chunk_kind: "child"
pattern_id: "E.17.EFP"
pattern_title: "ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces"
section_id: "E.17.EFP:5"
section_title: "Archetypal grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.EFP/E.17.EFP__006_archetypal-grounding.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "E.17.EFP — ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces"
  - "E.17.EFP:5 — Archetypal grounding"
line_start: 93139
line_end: 93253
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.6.3.CR"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.B"
  - "A.7"
  - "B.3"
  - "C.2.8"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.ID.CR"
  - "F.18"
  - "F.9"
  - "U.MultiViewDescribing"
keywords:
---

### E.17.EFP:5 - Archetypal grounding

#### E.17.EFP:5.1 - Source-pinned explanation across multiple faces
**Source claim slice.** `Claim D-14: Cooling loop CL-2 maintains the required temperature margin during standard load. Evidence pins: T-44, E-17.`

**`PlainView` rendering.** `Cooling loop CL-2 keeps the required temperature margin during standard load. Source pins: T-44, E-17.`

**`TechCard` rendering.** `D-14 stays source-pinned to T-44 and E-17; this rendering only shortens and reorders the claim.`

This stays within `SourcePinnedExplanation` because the rendering changes readability, not the semantic load.

#### E.17.EFP:5.2 - Genuinely entailed connective

**Source claims under exact thermal scheme `RS_plantThermal`.**

- `D-14: During standard load, CL-2 outlet temperature is at most 65 °C.`
- `D-18: During standard load, inspection criterion IC-7 is satisfied when that same outlet temperature is at most 70 °C.`

**Published reconstruction.** `During standard load, CL-2 outlet temperature satisfies the IC-7 upper-bound criterion stated by D-18.`

The connective is recoverable because both claims concern the same outlet and load context, `RS_plantThermal` supplies the Celsius order, and `65 <= 70`. The compact `addedLinkPolicy` points to `{D-14,D-18}`, `RS_plantThermal.order`, and that one-step derivation. It does not merely call the link implied. This form may be `SourceLinkedExplanationReconstruction` while those exact premises and rules remain current.

#### E.17.EFP:5.2.a - Non-entailed link exits the profile

**Source claim.** `D-21: The reserve path remained available during observed overload interval O-7.`

**Proposed connective.** `Therefore the reserve-path design is robust against every short overload.`

No source premise, effective-scheme rule, or already obtaining robustness relation derives the universal design claim. `addedLinkPolicy` cannot repair that absence. To retain the sentence, constitute exact target episteme `E_robustnessClaim` and apply the direct robustness, comparison, bridge, or B.5.2 hypothesis pattern appropriate to the intended claim. Until that relation obtains, remove the sentence or leave EFP; it is not source-linked reconstruction.

#### E.17.EFP:5.2.b - Selected-method explanation with an explicit source relation

**Source slice.** `The method-selection note chooses method M-2 because the material stays below threshold T and resource window W is available. It also says that work plan WP-17 and result measurement RM-4 remain required before and after execution.`

**Published explanation.** `M-2 is selected here because the material stays below threshold T and resource window W is available. Work plan WP-17 and result measurement RM-4 remain required before and after execution.`

The selection relation and both limits are explicit in the source, so this is ordinary same-ClaimGraph re-expression; it needs no invented `addedLinkPolicy`. It is not evidence that work occurred, a gate decision, or engineering justification. Selection use still concerns exact `U.Method` M-2; planning concerns `U.WorkPlan` WP-17 under A.15.2; any claim that work occurred requires a dated `U.Work` under A.15.1. Evidence, engineering-justification, or gate use remains under A.10, B.3, A.20, or A.21 only when actually raised.

#### E.17.EFP:5.2.c - Partial source expression and a mixed-face bundle

**Source edition.** In this example, `ReservePathDescription-E4` concerns exact path `R-1` and its overload intervals under effective duration scheme `RS_duration`. It contains `D-31: R-1 is configured to remain available for overload intervals no longer than five minutes` and `T-8: Observed interval O-7 lasted two minutes`.

**`PlainView` form.** `R-1 is configured for overload intervals up to five minutes. Source: ReservePathDescription-E4, D-31. Use: orientation to the configured duration; this form omits the O-7 observation.`

For that use, D-31 is sufficient and the form may be `SourcePinnedExplanation` of the same source edition. It does not assert T-8, observed availability or a guarantee. The omitted T-8 does not constitute another episteme, and the class claims no whole-source coverage.

**`TechCard` form.** `O-7 falls within D-31's configured duration window. Sources: ReservePathDescription-E4, D-31 and T-8.`

That connective follows from `2 min <= 5 min` under `RS_duration`; the form may be `SourceLinkedExplanationReconstruction` with this derivation pointer. The bundle states the class difference. The PlainView form alone cannot answer whether O-7 fits: that use needs the omitted T-8 and must return to it. Neither comparison establishes that the path actually remained available.

**Missing qualification.** Suppose an identified source edition also states `D-32: This availability configuration applies only while the backup supply is energized`. A form giving only the true five-minute duration is insufficient for deciding whether the configuration applies during loss of that supply. Return D-32 and the supply-state facts before that use. This insufficiency creates no target episteme; a separate assertion of unconditional availability would be changed content requiring its own target and relation.

**Equal words, different subject.** The same duration sentence about path `R-2` does not identify the `R-1` source. Likewise, identical displayed duration words interpreted under another effective scheme do not establish the same source identity. Recover the exact concern and scheme and apply the relevant retargeting or scheme-change pattern before claiming a source-to-target relation.

#### E.17.EFP:5.3 - Didactic retelling

**Source episteme claim.** `The pressure-control condition is satisfied whenever the reserve valve opens within 80 ms.`

**Didactic publication form.** `For onboarding: opening the reserve valve within 80 ms is enough to satisfy the pressure-control condition. The exact condition and threshold remain in the pinned source edition.`

The form expresses the same source ClaimGraph; `DidacticRetelling` qualifies only its teaching use. If the text instead says that the whole system is safe, that different safety claim requires its own target episteme, an obtaining source-to-target relation, and the applicable safety relation before publication. A didactic label cannot supply them.

#### E.17.EFP:5.4 - Speculative retelling

**Observed-source episteme.** `The pinned source notes record the observed recovery, but they do not explain why the recovery was so rapid.`

That observation may frame an abductive prompt. If `B.5.2` produces exact hypothesis episteme `E_couplingHypothesis` with claim `A temporary coupling effect may have accelerated recovery`, that claim belongs to the new hypothesis ClaimGraph, not to the observed-source edition.

**Speculative publication form of the hypothesis episteme.** `Exploratory hypothesis: a temporary coupling effect may have accelerated recovery. This is the separately identified L0 hypothesis, not a claim of the incident source.`

`SpeculativeRetelling` qualifies only this form's exploratory explanation use. It neither constitutes `E_couplingHypothesis` nor turns the form into a passive rendering of the observed source.

#### E.17.EFP:5.4.a - Anti-example: explanation that quietly becomes a new claim

**Source episteme claim.** `The reserve path remained available during the observed short overload interval.`

**Overreaching text.** `The reserve-path design is robust against short overloads.`

The second sentence has a different ClaimGraph. To retain it, constitute an exact target episteme under C.2.1, identify an obtaining source-to-target relation, and establish the wider design-robustness claim under its applicable pattern. Until that relation obtains and the wider claim is established, the sentence is unsupported and receives no EFP class; reopening the source or calling the text face-local does not make the claim part of the source edition.

#### E.17.EFP:5.4.b - Anti-example: reader help that quietly becomes policy-bearing use
**Source slice.** `The onboarding note explains, in simplified prose, that the reserve valve usually opens quickly enough to keep the local pressure condition inside the tolerated window.`

**Overreaching rendering on an `AssuranceLane`-facing use.** `This explanation is sufficient assurance that short overloads stay inside the tolerated window.`

This assurance sentence has a different ClaimGraph. It requires an exact target episteme under C.2.1 and the applicable A.10/B.3 relations; until those obtain it is unsupported and receives no EFP class. The earlier onboarding form may retain its bounded didactic use, but that class neither carries nor weakens the assurance claim.

#### E.17.EFP:5.4.c - Boundary to lighter explanatory note with source-bearing return
**Source slice.** `The technical incident note says the reserve path remained available during the measured load band, but it also keeps one unresolved ambiguity about recovery latency.`

**Lighter explanatory rendering.** `In plain terms: the reserve path stayed available during overload recovery.`

For a use that needs the measured load band or the unresolved latency qualification, this lighter text is insufficient: return those source conditions. Omission alone does not constitute another episteme. If the text is instead intended to assert availability throughout overload recovery beyond the measured band, it makes a changed claim. Identify that target under C.2.1 and establish its `A.6.3.CSC` or other applicable source-to-target relation before EFP classifies a later target form.

#### E.17.EFP:5.5 - Class-specific reopen cues in the worked slices
- **`SourcePinnedExplanation`** reopens when the pinned source claim set, source pins, or face-use assumptions change so that the rendering can no longer remain claim-preserving and visibly source-bound.
- **`SourceLinkedExplanationReconstruction`** reopens when any source premise, effective-scheme rule, derivation, context identity, source claim about the exact relation occurrence, or that occurrence's obtaining basis changes or disappears.
- **`DidacticRetelling`** reopens when the exact source or target edition connected under A.6.3 changes, or when teaching use starts functioning as policy-bearing, design-bearing, or gate-bearing guidance.
- **`SpeculativeRetelling`** reopens when its exact B.5.2 hypothesis edition, prompt link, or exploratory use changes; it never falls back to being a passive form of the observation source.

#### E.17.EFP:5.6 - Boundary to interpretation and world or gate use

If a text carries a new hypothesis or another changed claim, first constitute its exact target episteme and apply `B.5.2`, A.6.3, or the other direct source-to-target pattern. Comparative review, rival interpretation, bridge, world, gate, assurance, and engineering-justification uses likewise leave to their exact patterns; EFP can only qualify a later published form's explanation use.

#### E.17.EFP:5.7 - Human-authored and generated task replay against the simpler alternative

This is a qualitative task replay for local architecture choice, not an empirical performance study. Each case compares EFP with the least-cost source-linked note on comprehension, semantic preservation, author/check time, and prevention of overread.

| Task and credible simpler alternative | Comprehension | Semantic preservation | Author/check time | Overread prevention | Non-dominated result |
|---|---|---|---|---|---|
| **Human-authored shift note.** An engineer writes two sentences that repeat inspection note N-14 without changing its claims. Simpler alternative: `Reader orientation; source N-14; not an operating procedure.` | The simple sentence is as easy to understand as an EFP class note. | The source locator and unchanged wording preserve the needed tether. | The simple note is shorter to write and check. | `not an operating procedure` blocks the only credible overread. | The simpler note dominates. Do not apply EFP; use the source/publication pattern and stop. |
| **Generated incident explanation.** A generated paragraph restates one observed recovery and adds `therefore the design is robust`. Simpler alternative: attach a source link and label the paragraph `AI summary`. | Both versions are readable. | The simple label misses the widened robustness claim; EFP's identity-and-bounded-sufficiency screen detects another target claim and prevents source identity from being inherited. | EFP adds one focused claim comparison; no full metadata block is needed. | EFP blocks reliance on the widened claim until its target episteme and source-to-target relation exist. | EFP is non-dominated when the generated text will be reviewed, reused, disputed, or relied on. Keep the identity screen, class only after identity, bounded/blocked use, and reopen; add trace or evidence only for the named reliance. |

The human-authored case is the ordinary non-use boundary. The generated case is the source-grounded branch supported by XAI/NLP/generated-explanation literature. A human-authored case may still use EFP when a real source-pinned/reconstructive/didactic/speculative ambiguity changes the next action, but authorship alone never triggers the profile.

