---
chunk_kind: "child"
pattern_id: "A.6.4"
pattern_title: "EntityOfConcern Retargeting: Judge a Bounded Use Across Different Entities"
section_id: "A.6.4:5"
section_title: "Archetypal Grounding (Tell-Show-Show)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.4/A.6.4__006_archetypal-grounding-tell-show-show.md"
commit_sha: "c3b34de07a6bd2df85c7081a4c367fd09978079c"
heading_path:
  - "A.6.4 — EntityOfConcern Retargeting: Judge a Bounded Use Across Different Entities"
  - "A.6.4:5 — Archetypal Grounding (Tell-Show-Show)"
line_start: 19737
line_end: 19754
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.6.0"
  - "A.6.1"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.5"
  - "A.7"
  - "B.3"
  - "C.2"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "E.10.D2"
  - "E.17"
  - "E.24.PUB"
  - "F.9"
keywords:
---

### A.6.4:5 - Archetypal Grounding (Tell-Show-Show)

**Tell.** Retargeting means “different EntityOfConcern, one stated invariant, visible loss, one named use, and exact current facts for judging it”.

**Show 1 — Physical cabinet to selected functional structure.** Take `Cab-7` and functional `U.Structure` `Route-A` as independently identified entities. Under an explicit finite-routing scheme, source episteme X states two observations of `Cab-7` in configuration K: input L routed to output 1, and input R routed to output 2. X also identifies cabinet layout `Layout-7` and manufacturer `Maker-7`. A separate definition episteme Z specifies `Route-A` with those pairs and a third pair M→3. Receiving episteme Y concerns `Route-A` and selects only its declared L→1 and R→2 pairs. C.2.1 distinguishes X, Y and Z by their complete claims, concerns and effective schemes.

In the selected finite-table substrate, r relates X to Y by the rule `TestedRowProjection`: match the named input rows and use Z's definition for the receiving structure assertions. Arrow equivalence uses the same endpoints and rowwise equality of that rule. This does not infer Route-A's definition from cabinet behavior alone.

Affirmative q states: `Under K, Cab-7's observed outputs for {L,R} match Route-A's declared outputs. Dropping cabinet layout, manufacturer details and Route-A's M branch is acceptable for preparing a fault-isolation check list restricted to the observed inputs L and R.` The current case compares L→1 with L→1 and R→2 with R→2; both match. The resulting check list is “for L, inspect output 1; for R, inspect output 2”; that use needs neither the omitted cabinet details nor the M branch. The judgement is therefore `satisfies` for this bounded use. A changed configuration or another input requires new case facts. Missing output observations yield `cannot decide`; an observed mismatch yields `fails` without changing q's polarity.

The unused expression `Realises(Cab-7, Route-A)` has no supplied direct predicate or governor in this fixture. It contributes nothing to the judgement. Placement of r and q in E.18 likewise supplies no case fact.

**Show 2 — Fourier near-miss and positive branch.** In the ordinary case, X and Y both concern sampled signal run `Signal-17`; X uses a time-domain representation and Y a frequency-domain representation. Use A.6.3.RT for this representation change. Under its declared conditions, Parseval's relation gives the energy-preservation equality; the spectrum notation still represents the same EntityOfConcern. If that mathematical correspondence or its conditions are unsettled for the receiving use, use C.29 to establish their adequacy before relying on the equality.

A positive A.6.4 branch opens only if C.2.1 separately identifies, for example, exact signal run `Signal-17` and exact spectral-distribution object `Spectrum-17` as the two EntitiesOfConcern. The receiving use must actually concern `Spectrum-17`—for example, comparing its peak distribution with another spectrum—rather than merely read another representation of `Signal-17`. Then r relates the two epistemes; affirmative q states the spectral-comparison proposition and may cite the Fourier relation and Parseval test. The current-case judgement is `satisfies` only when the named facts meet q's conditions and criterion while lost time localization remains visible.

**Show 3 — Dataset to model.** X concerns dataset D; Y concerns fitted model M, independently identified under the applicable model pattern. Affirmative q states the predictive invariant, visible losses, named prediction use, and conditions. The exact fit result and held-out test outcome are current-case facts; the judgement is `satisfies` when those facts meet q's conditions and invariant criterion. Individual observations and unmodelled distinctions remain visible losses, and any other dataset claim needs its own transfer basis. The fitting application and Work remain separate from r, q, and the judgement.

