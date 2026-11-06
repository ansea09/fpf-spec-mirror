---
chunk_kind: "child"
pattern_id: "C.2.2"
pattern_title: "Reliability R in the F–G–R triad"
section_id: "C.2.2:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.2/C.2.2__006_archetypal-grounding.md"
commit_sha: "d8dd955fddb923b5b946d2c5865d0665cff5a67e"
heading_path:
  - "C.2.2 — Reliability R in the F–G–R triad"
  - "C.2.2:5 — Archetypal Grounding"
line_start: 52722
line_end: 52751
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.2.6"
  - "A.21"
  - "A.6.3.RT"
  - "A.6.3.RT.OE"
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
  - "pathwise justification (PathId)"
  - "qualitative synthesis"
  - "support dependencies"
  - "warrant"
  - "weakest-link limits"
---

### C.2.2:5 - Archetypal Grounding

Informative; non-binding.

#### C.2.2:5.1 - System illustration

**System.** A brake controller `S` has a claim:

> `c1:` “For road friction μ ∈ [0.2, 0.9] and vehicle mass m ∈ [900, 2200] kg, wheel slip stays in [0.05, 0.25] under ABS control.”

* The formality assessment of `c1` identifies the declared model variables, constraint predicates and execution semantics of the test harness under C.2.3. These properties enable the specified checks and tests; their results and the model's fit to the physical plant require the separate evidence below.
* `G(c1)` has the stated μ/m bounds, but this illustration leaves the speed domain and admissible tire set unspecified. Under A.2.6, those domains and any coupled restrictions are needed to decide membership of a slice satisfying the stated bounds; that membership remains unresolved here. A product set in `(μ, m, speed, tire)` space is justified only if its scope predicate admits every combination of the selected domains.
* Evidence:

  * VA: model-checking of a simplified plant/controller model (strong, but only for the simplified plant).
  * LA: HIL simulation + track tests under sampled conditions, with the observation windows and any currentness qualification required by the receiving claim.
  * TA: typed alignment between “μ” in simulations, “μ” in the estimation pipeline, and “μ” inferred from real-world sensors.

If track telemetry is used as evidence for the road claim, establish the grounds for that reuse, including the road claim, telemetry edition, operating scope, intended use, and any validity window on which that use depends. Apply only the fit or loss declared for that evidence reuse; `G(c1)` changes only through a separate A.2.6 scope revision.

#### C.2.2:5.2 - Episteme illustration

**Episteme.** A paper asserts two claims about an algorithm `A`:

* `c2:` “A terminates for all inputs in domain D.” (axiomatic / proof-carrying)
* `c3:` “A achieves ≥ 0.92 F1 on dataset family F under deployment preprocessing P.” (empirical)

`c2` can achieve high VA through its proof under the stated axioms and domain; an empirical LA contribution may be N/A. If the conclusion is also used for an implementation, establish the correspondence between “domain D,” the proved algorithm and that implementation’s input and execution model.
`c3` needs empirical support for its stated dataset and preprocessing conditions. For production use, establish the dataset/preprocessing applicability and the grounds for reusing that evidence, then apply the warranted loss of that reuse to `R_eff`; change `G` separately if the production claim has another scope. Use B.3.4 when changed conditions or an applicable review rule can alter that support; retain any required validity window or shift condition. An unchanged bounded use with still-applicable support needs no new freshness policy.

