---
chunk_kind: "child"
pattern_id: "A.6.4"
pattern_title: "EntityOfConcern retargeting"
section_id: "A.6.4:5"
section_title: "Archetypal Grounding (Tell-Show-Show)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.4/A.6.4__006_archetypal-grounding-tell-show-show.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "A.6.4 — EntityOfConcern retargeting"
  - "A.6.4:5 — Archetypal Grounding (Tell-Show-Show)"
line_start: 15364
line_end: 15375
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

**Tell.** Retargeting means “different EntityOfConcern, one supported invariant, visible loss, one named use”.

**Show 1 — Physical module to function.** X concerns cabinet `Cab-7`; Y concerns routing function `Route-A`. C.2.1 identifies the cabinet and function independently. Affirmative q states that the routing-behaviour invariant makes the visible loss acceptable for fault-isolation planning. The obtaining `Realises(Cab-7, Route-A)` relation and behaviour test are current case facts; here the judgement is `satisfies`. Y drops cabinet layout and manufacturer details. E.18 placement identifies neither r nor q and supplies no judgement.

**Show 2 — Fourier near-miss and positive branch.** In the ordinary case, X and Y both concern sampled signal run `Signal-17`; X uses a time-domain representation and Y a frequency-domain representation. Route first through C.29 and then A.6.3.RT. Parseval's relation may support energy preservation, but it does not turn the spectrum notation into another EntityOfConcern.

A positive A.6.4 branch opens only if C.2.1 separately identifies, for example, exact signal run `Signal-17` and exact spectral-distribution object `Spectrum-17` as the two EntitiesOfConcern. The receiving use must actually concern `Spectrum-17`—for example, comparing its peak distribution with another spectrum—rather than merely read another representation of `Signal-17`. Then r relates the two epistemes; affirmative q states the spectral-comparison proposition and may cite the Fourier relation and Parseval test. The current-case judgement is `satisfies` only when the named facts support that use while lost time localization remains visible.

**Show 3 — Dataset to model.** X concerns dataset D; Y concerns fitted model M, independently identified under the applicable model pattern. The fit result and held-out test support q's predictive-invariant claim. Individual observations and unmodelled distinctions are visible losses. The claim supports the named prediction use, not a claim that M is D or that every dataset claim transfers to M. The fitting application and Work remain separate from r and q.

