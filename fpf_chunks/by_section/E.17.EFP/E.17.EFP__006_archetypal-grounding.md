---
chunk_kind: "child"
pattern_id: "E.17.EFP"
pattern_title: "ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces"
section_id: "E.17.EFP:5"
section_title: "Archetypal grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.EFP/E.17.EFP__006_archetypal-grounding.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "E.17.EFP — ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces"
  - "E.17.EFP:5 — Archetypal grounding"
line_start: 83618
line_end: 83726
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

**`PlainView` rendering.** `Cooling loop CL-2 keeps the required temperature margin in standard operation. Source pins: T-44, E-17.`

**`TechCard` rendering.** `D-14 stays source-pinned to T-44 and E-17; this rendering only shortens and reorders the claim.`

This stays within `SourcePinnedExplanation` because the rendering changes readability, not the semantic load.

#### E.17.EFP:5.2 - Genuinely entailed connective

**Source claims under exact thermal scheme `RS_plantThermal`.**

- `D-14: During standard load, CL-2 outlet temperature is at most 65 °C.`
- `D-18: During standard load, inspection criterion IC-7 is satisfied when that same outlet temperature is at most 70 °C.`

**Published reconstruction.** `During standard load, D-14 satisfies the IC-7 upper-bound criterion stated by D-18.`

The connective is recoverable because both claims concern the same outlet and load context, `RS_plantThermal` supplies the Celsius order, and `65 <= 70`. The compact `addedLinkPolicy` points to `{D-14,D-18}`, `RS_plantThermal.order`, and that one-step derivation. It does not merely call the link implied. This form may be `SourceLinkedExplanationReconstruction` while those exact premises and rules remain current.

#### E.17.EFP:5.2.a - Non-entailed link exits the profile

**Source claim.** `D-21: The reserve path remained available during observed overload interval O-7.`

**Proposed connective.** `Therefore the reserve-path design is robust against every short overload.`

No source premise, effective-scheme rule, or already obtaining robustness relation derives the universal design claim. `addedLinkPolicy` cannot repair that absence. To retain the sentence, constitute exact target episteme `E_robustnessClaim` and apply the direct robustness, comparison, bridge, or B.5.2 hypothesis pattern appropriate to the intended claim. Until that relation obtains, remove the sentence or leave EFP; it is not source-linked reconstruction.

#### E.17.EFP:5.2.b - Selected-method explanation with an explicit source relation

**Source slice.** `The method-selection note chooses method M-2 because the material stays below threshold T and resource window W is available. It also says that work plan WP-17 and result measurement RM-4 remain required before and after execution.`

**Published explanation.** `M-2 is selected here for the stated material condition and resource window. Planning still requires WP-17, and result measurement still requires RM-4.`

The selection relation and both limits are explicit in the source, so this is ordinary same-ClaimGraph re-expression; it needs no invented `addedLinkPolicy`. It is not evidence that work occurred, a gate decision, or engineering justification. Selection use still concerns exact `U.Method` M-2; planning concerns `U.WorkPlan` WP-17 under A.15; any claim that work occurred requires a dated `U.Work` under A.15.1. Evidence, engineering-justification, or gate use remains under A.10, B.3, A.20, or A.21 only when actually raised.

#### E.17.EFP:5.2.c - Mixed-face bundle with one entailed connective

**Source claims.** `D-31: The reserve path is configured to remain available for overload intervals no longer than five minutes.` `T-8: Observed interval O-7 lasted two minutes.` Both use exact duration scheme `RS_duration` and concern the same path and interval class.

**`PlainView` form.** `The reserve path is configured for overload intervals up to five minutes. Source: D-31.`

**`TechCard` form.** `O-7 falls within D-31's configured availability window. Sources: D-31, T-8.`

The `PlainView` form is `SourcePinnedExplanation`. The `TechCard` connective is derivable from `2 min <= 5 min` under `RS_duration` and may be `SourceLinkedExplanationReconstruction` with that derivation pointer. The bundle states the class difference; it does not infer availability beyond D-31's exact condition.

#### E.17.EFP:5.3 - Didactic retelling

**Source episteme claim.** `The pressure-control condition is satisfied whenever the reserve valve opens within 80 ms.`

**Didactic publication form.** `For onboarding: in this stated test, opening the reserve valve within 80 ms is enough to satisfy the pressure-control condition. The exact condition and threshold remain in the pinned source edition.`

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

This does **not** remain ordinary explanation profiling. The lighter text expresses a coarsened ClaimGraph, so it must be identified as an exact target episteme under C.2.1 and related to the source through `A.6.3.CSC`; only a later publication form of that target can receive an EFP class if explanation use remains material.

#### E.17.EFP:5.5 - Class-specific reopen cues in the worked slices
- **`SourcePinnedExplanation`** reopens when the pinned source claim set, source pins, or face-use assumptions change so that the rendering can no longer remain omission-only and visibly source-bound.
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
| **Generated incident explanation.** A generated paragraph restates one observed recovery and adds `therefore the design is robust`. Simpler alternative: attach a source link and label the paragraph `AI summary`. | Both versions are readable. | The simple label misses the widened robustness claim; EFP's ClaimGraph screen detects another target claim and prevents source identity from being inherited. | EFP adds one focused claim comparison; no full metadata block is needed. | EFP blocks reliance on the widened claim until its target episteme and source-to-target relation exist. | EFP is non-dominated when the generated text will be reviewed, reused, disputed, or relied on. Keep the identity screen, class only after identity, bounded/blocked use, and reopen; add trace or evidence only for the named reliance. |

The human-authored case is the ordinary non-use boundary. The generated case is the source-grounded branch supported by XAI/NLP/generated-explanation literature. A human-authored case may still use EFP when a real source-pinned/reconstructive/didactic/speculative ambiguity changes the next action, but authorship alone never triggers the profile.

