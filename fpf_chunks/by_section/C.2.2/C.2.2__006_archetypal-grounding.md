---
chunk_kind: "child"
pattern_id: "C.2.2"
pattern_title: "Reliability R in the F–G–R triad"
section_id: "C.2.2:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.2/C.2.2__006_archetypal-grounding.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "C.2.2 — Reliability R in the F–G–R triad"
  - "C.2.2:5 — Archetypal Grounding"
line_start: 43248
line_end: 43277
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.2.6"
  - "A.21"
  - "A.6.3.RT"
  - "B.1.3"
  - "B.3"
  - "B.3.3"
  - "B.3.4"
  - "C.16"
  - "C.2"
  - "C.2.3"
  - "C.21"
  - "C.29"
  - "C.3"
  - "C.3.3"
  - "C.3.A"
  - "E.14"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.9"
  - "G.2"
  - "G.6"
  - "G.7"
keywords:
  - "ClaimScope (G)"
  - "Congruence Level (CL / CL^k / CL^plane)"
  - "F–G–R"
  - "Reliability (R)"
  - "TA/VA/LA lanes"
  - "direct relation"
  - "evidence-bound"
  - "no implicit averaging"
  - "pathwise justification (PathId)"
  - "warrant"
  - "weakest-link"
---

### C.2.2:5 - Archetypal Grounding

Informative; non-binding.

#### C.2.2:5.1 - System illustration

**System.** A brake controller `S` has a claim:

> `c1:` “For road friction μ ∈ [0.2, 0.9] and vehicle mass m ∈ [900, 2200] kg, wheel slip stays in [0.05, 0.25] under ABS control.”

* `F(c1)=F5` because the controller and constraints are expressed as a machine-checkable model plus executable test harness (C.2.3).
* `G(c1)` has the stated μ/m bounds, but this illustration leaves the speed domain and admissible tire set unspecified. Under A.2.6, those domains and any coupled restrictions are needed to decide membership of a slice satisfying the stated bounds; that membership remains unresolved here. A product set in `(μ, m, speed, tire)` space is justified only if its scope predicate admits every combination of the selected domains.
* Evidence:

  * VA: model-checking of a simplified plant/controller model (strong, but only for the simplified plant).
  * LA: HIL simulation + track tests under sampled conditions with recorded telemetry windows (freshness required).
  * TA: typed alignment between “μ” in simulations, “μ” in the estimation pipeline, and “μ” inferred from real-world sensors.

If track telemetry is used as evidence for the road claim, establish the exact A.10 or B.3 evidence-use and reliance claim, including the road claim, telemetry edition, operating scope, validity window, and intended use. Apply only the fit or loss declared for that evidence reuse; `G(c1)` changes only through a separate A.2.6 scope revision.

#### C.2.2:5.2 - Episteme illustration

**Episteme.** A paper asserts two claims about an algorithm `A`:

* `c2:` “A terminates for all inputs in domain D.” (axiomatic / proof-carrying)
* `c3:` “A achieves ≥ 0.92 F1 on dataset family F under deployment preprocessing P.” (empirical)

`c2` can achieve high VA with a proof carrier; its LA lane may be N/A, but its TA lane remains relevant because the intended meaning of “domain D” must align with the implementation’s input model.
`c3` requires LA evidence and a freshness or shift policy because dataset and preprocessing drift can change both scope and warrant. For production use, state the exact dataset/preprocessing relation and the A.10 or B.3 evidence-reuse claim, then apply its declared loss to `R_eff`; change `G` separately if the production claim has another scope.

