---
chunk_kind: "child"
pattern_id: "E.17.EFP"
pattern_title: "ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces"
section_id: "E.17.EFP:5"
section_title: "Archetypal grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.EFP/E.17.EFP__006_archetypal-grounding.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "E.17.EFP — ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces"
  - "E.17.EFP:5 — Archetypal grounding"
line_start: 64178
line_end: 64262
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.20"
  - "A.21"
  - "A.6.3.CSC"
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

**`TechCard` rendering.** `D-14 remains source-pinned to T-44 and E-17; this rendering only shortens and reorders the claim.`

This stays within `SourcePinnedExplanation` because the rendering changes readability, not the semantic load.

#### E.17.EFP:5.2 - Source-linked reconstruction
**Source slice.** `Claims D-14 and D-18 jointly constrain the safe operating window, but the relation is left implicit in the original note.`

**Published reconstruction.** `Claims D-14 and D-18 jointly bound the safe operating window; see the pinned source notes for the original wording and evidence anchors.`

This stays within `SourceLinkedExplanationReconstruction` if the connective prose remains bounded and does not add new claims.

A minimal `addedLinkPolicy` for this slice would say:
- `addedLinkKind = relation-explication only`;
- `sourceReferenceSet = {D-14, D-18}`;
- `boundednessReason = makes an already implied joint constraint explicit without adding a new mechanism, policy conclusion, or unsupported modality lift`;
- `forbiddenLinkClass = design-scope robustness or gate-sufficiency claim`.

#### E.17.EFP:5.2.b - Selected-method explanation

**Source slice.** `The method-selection note chooses method M-2 because the material stays below threshold T and resource window W is available. The same source says that work plan WP-17 and result measurement RM-4 are still required before and after execution.`

**Published explanation.** `Method M-2 is selected here because the material condition and resource window match the declared method family. Use WP-17 for planning and RM-4 for result measurement.`

This may stay within `SourceLinkedExplanationReconstruction` when the explanation keeps its source references visible and only makes the already source-recoverable selection relation easier to inspect. It is admissible for interpretation, source-finding, and selected-method inspection. It is not evidence that work occurred, not a gate decision, and not engineering justification. Evidence or provenance use requires a project evidence path governed by `A.10`; engineering-justification use requires an engineering-justification record governed by `B.3`; method-selection use requires project `U.Method`, work-plan use requires `U.WorkPlan` under `A.15`, and work-occurrence use requires a dated `U.Work` occurrence under `A.15.1`; gate use requires the project gate or constraint decision governed by `A.20` or `A.21`.

#### E.17.EFP:5.2.a - Mixed-face bundle with different explanation classes
**Source slice.** `Claim D-31 and trace set T-8 jointly show that the reserve path remains available during the short overload interval.`

**`PlainView` rendering.** `The reserve path stays available during the short overload interval. Source pins: D-31, T-8.`

**`TechCard` rendering.** `D-31 and T-8 jointly evidence availability of the reserve path during the short overload interval; this rendering adds bounded connective prose to make the source relation explicit.`

The `PlainView` rendering may stay `SourcePinnedExplanation` while the `TechCard` rendering is `SourceLinkedExplanationReconstruction`. The bundle is admissible only if that class difference is stated rather than hidden under one blanket label.

#### E.17.EFP:5.3 - Didactic retelling
**Source slice.** `The pressure-control condition is satisfied whenever the reserve valve opens within 80 ms.`

**Didactic rendering.** `For onboarding: the system stays safe here because the reserve valve opens quickly enough; the threshold and source claim named by value remain in the pinned technical note.`

This stays in `DidacticRetelling` only if it is kept off `TechCard` or `AssuranceLane` faces where it could be mistaken for canonical semantics.

#### E.17.EFP:5.4 - Speculative retelling
**Source slice.** `The pinned source notes record the observed recovery, but they do not explain why the recovery was so rapid.`

**Speculative rendering.** `One possible reading is that a temporary coupling effect accelerated recovery, but this is a reflective aid for discussion, not a source-backed claim.`

This is admissible only as a clearly marked exploratory or didactic use on an existing face; it must not appear as policy-bearing, gate-bearing, or assurance-bearing claim material.

#### E.17.EFP:5.4.a - Anti-example: explanation that quietly becomes a new claim
**Source slice.** `The pinned source claims show the reserve path remained available during the short overload interval.`

**Overreaching rendering.** `The reserve-path design is therefore robust against short overloads.`

This no longer stays inside explanation-use discipline. The rendering introduces a design-scope commitment that the pinned source does not state, so the case must reopen the appropriate source `U.Episteme`, source `U.EpistemePublication`, project record whose governing FPF kind is named, or apply the neighboring pattern that governs that commitment instead of hiding inside a face-local explanation label.

#### E.17.EFP:5.4.b - Anti-example: reader help that quietly becomes policy-bearing use
**Source slice.** `The onboarding note explains, in simplified prose, that the reserve valve usually opens quickly enough to keep the local pressure condition inside the tolerated window.`

**Overreaching rendering on an `AssuranceLane`-facing use.** `Operators may rely on this explanation as sufficient assurance that short overloads stay inside the tolerated window.`

This also leaves the profile. The rendering is no longer only reader help over existing claims; it starts acting like policy-bearing or assurance-bearing guidance. The case must reopen, drop the explanation class, or use the neighboring pattern and project-side FPF kind and reference named by value that govern that guidance rather than staying on an explanation face.

#### E.17.EFP:5.4.c - Boundary to lighter explanatory note with source-bearing return
**Source slice.** `The technical incident note says the reserve path remained available during the measured load band, but it also keeps one unresolved ambiguity about recovery latency.`

**Lighter explanatory rendering.** `In plain terms: the reserve path stayed available during overload recovery.`

This does **not** remain ordinary explanation profiling. The lighter note suppresses the load-band condition and the unresolved ambiguity, so it can stay honest only through narrower admissible claim or effect, non-admissible downstream claim or effect, and return to the source `U.Episteme` or source `U.EpistemePublication`. Once those narrowed-claim conditions become primary, the case must leave ordinary explanation-use discipline and be governed as a coarsened rendering rather than as ordinary reader help.

#### E.17.EFP:5.5 - Class-specific reopen cues in the worked slices
- **`SourcePinnedExplanation`** reopens when the pinned source claim set, source pins, or admissible-face assumptions change so that the rendering can no longer remain omission-only and visibly source-bound.
- **`SourceLinkedExplanationReconstruction`** reopens when the connective prose begins carrying an unsupported relation, or when the source claim set changes enough that the bounded reconstruction is no longer plainly source-linked.
- **`DidacticRetelling`** reopens when the rendering moves onto `TechCard` or `AssuranceLane`-facing use, or when reader-help prose starts functioning as policy-bearing, design-bearing, or gate-bearing guidance.
- **`SpeculativeRetelling`** reopens when source binding becomes available, or when the rendering starts to behave like canonical explanation rather than clearly bounded exploratory help.

#### E.17.EFP:5.6 - Boundary to interpretation and world or gate use
If the rendering starts generating one bounded comparative review case, rival interpretations, bridge-mediated comparative claims, new hypotheses, world consequences, gate consequences, assurance claims, or engineering-justification claims, it must leave this profile and apply the neighboring FPF pattern and project-side FPF kind and reference named by value that govern the claim or effect (`E.17.ID.CR`, `F.9.1`, `B.5.2`, `A.6.4`, `A.15`, `B.3`, `A.20`, `A.21`).

