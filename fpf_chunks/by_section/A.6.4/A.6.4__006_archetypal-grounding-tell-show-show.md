---
chunk_kind: "child"
pattern_id: "A.6.4"
pattern_title: "EntityOfConcern retargeting"
section_id: "A.6.4:5"
section_title: "Archetypal Grounding (Tell-Show-Show)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.4/A.6.4__006_archetypal-grounding-tell-show-show.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "A.6.4 — EntityOfConcern retargeting"
  - "A.6.4:5 — Archetypal Grounding (Tell-Show-Show)"
line_start: 15922
line_end: 15933
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

**Show 1 — Physical cabinet to selected functional structure.** X concerns cabinet `Cab-7`; Y concerns selected functional `U.Structure` `Route-A`. C.2.1 identifies the cabinet and structure independently. Affirmative q states that the routing-behaviour invariant makes the visible loss acceptable for fault-isolation planning. A current behaviour-test result compares `Cab-7`'s observed routing under q's named conditions with the routing decisions stated for `Route-A` and meets q's criterion; the judgement is `satisfies`. The source expression `Realises(Cab-7, Route-A)` names an intended relation and its participants but has no current direct predicate or governor, so it stops at `missing-governor` and contributes nothing to that judgement. Y drops cabinet layout and manufacturer details. E.18 placement identifies neither r nor q and supplies no judgement.

**Show 2 — Fourier near-miss and positive branch.** In the ordinary case, X and Y both concern sampled signal run `Signal-17`; X uses a time-domain representation and Y a frequency-domain representation. Route first through C.29 and then A.6.3.RT. Under its declared conditions, Parseval's relation gives the energy-preservation equality; the spectrum notation still represents the same EntityOfConcern.

A positive A.6.4 branch opens only if C.2.1 separately identifies, for example, exact signal run `Signal-17` and exact spectral-distribution object `Spectrum-17` as the two EntitiesOfConcern. The receiving use must actually concern `Spectrum-17`—for example, comparing its peak distribution with another spectrum—rather than merely read another representation of `Signal-17`. Then r relates the two epistemes; affirmative q states the spectral-comparison proposition and may cite the Fourier relation and Parseval test. The current-case judgement is `satisfies` only when the named facts meet q's conditions and criterion while lost time localization remains visible.

**Show 3 — Dataset to model.** X concerns dataset D; Y concerns fitted model M, independently identified under the applicable model pattern. Affirmative q states the predictive invariant, visible losses, named prediction use, and conditions. The exact fit result and held-out test outcome are current-case facts; the judgement is `satisfies` when those facts meet q's conditions and invariant criterion. Individual observations and unmodelled distinctions remain visible losses, and any other dataset claim needs its own transfer basis. The fitting application and Work remain separate from r, q, and the judgement.

