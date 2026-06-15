---
chunk_kind: "child"
pattern_id: "A.6.4"
pattern_title: "U.EpistemicRetargeting — EntityOfConcern retargeting morphism"
section_id: "A.6.4:5"
section_title: "Archetypal grounding (Tell-Show-Show)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.4/A.6.4__006_archetypal-grounding-tell-show-show.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "A.6.4 — U.EpistemicRetargeting — EntityOfConcern retargeting morphism"
  - "A.6.4:5 — Archetypal grounding (Tell-Show-Show)"
line_start: 12984
line_end: 13012
dependencies:
  - "A.6.2"
  - "A.6.3"
  - "A.6.5"
  - "A.7"
  - "C.2"
  - "C.2.1"
  - "C.3"
  - "E.10.D2"
  - "E.18"
  - "F.9"
keywords:
---

### A.6.4:5 - Archetypal grounding (Tell-Show-Show)

**Tell.**
EpistemicRetargeting captures **“same invariant, different EntityOfConcern”** moves:

* the source episteme describes “this cabinet”, while the receiving episteme describes “the routing function it realises”;
* the source episteme describes “this signal over time”, while the receiving episteme describes “its spectrum over frequency”;
* the source episteme describes “this dataset”, while the receiving episteme describes “a model class with parameters θ learned from it”.

In each case, what remains stable is an **invariant** (behaviour, energy, likelihood), not the EntityOfConcern itself.

**Show 1 — StructuralReinterpretation in E.18.**
* `X` describes a physical module holon `S_phys`.
* `Y` describes a function holon `S_func`.
* A `KindBridge(S_phys, S_func)` expresses “this module realises that function”.
* An `E.18` `StructuralReinterpretation` locus can be governed as an instance of `U.EpistemicRetargeting` when its invariant is the behaviour relation between `S_phys` and `S_func`.

**Show 2 — Signal↔Spectrum.**
* `X` describes a time‑domain signal `s(t)`; `EntityOfConcernRef(X) = S_time`.
* `Y` describes its spectrum `S(ω)`; `EntityOfConcernRef(Y) = S_freq`.
* `KindBridge(S_time, S_freq)` encodes Fourier duality in the relevant ReferencePlane.
* The invariant is energy (or inner product), expressed as a KD‑CAL statement; EpistemicRetargeting ensures that energy‑related claims in `Y` are entailed by `X`.

**Show 3 — Data→Model.**
* `X` describes a dataset `D` (observations); `EntityOfConcernRef(X) = S_data`.
* `Y` describes a model `M` (e.g. a parametric family with learned parameters); `EntityOfConcernRef(Y) = S_model`.
* `KindBridge(S_data, S_model)` encodes the intended data→model relation (e.g. MLE, Bayesian posterior).
* The invariant is likelihood or predictive performance; the retargeting laws ensure `Y` does not claim more about this invariant than is warranted by `X`.

