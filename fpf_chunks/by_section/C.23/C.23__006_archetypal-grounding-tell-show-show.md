---
chunk_kind: "child"
pattern_id: "C.23"
pattern_title: "MethodFamily Evidence & Maturity (Method‑SoS‑LOG)"
section_id: "C.23:5"
section_title: "Archetypal Grounding (Tell–Show–Show)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.23/C.23__006_archetypal-grounding-tell-show-show.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "C.23 — MethodFamily Evidence & Maturity (Method‑SoS‑LOG)"
  - "C.23:5 — Archetypal Grounding (Tell–Show–Show)"
line_start: 63433
line_end: 63474
dependencies:
  - "A.10"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.22"
  - "E.10"
  - "E.18"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.8"
  - "G.9"
keywords:
  - "MethodFamily"
  - "SoS-LOG"
  - "abstain"
  - "admission rules"
  - "admit"
  - "degrade"
  - "evidence"
  - "maturity"
  - "selector"
---

### C.23:5 - Archetypal Grounding (Tell–Show–Show)

The following are constructed branch examples. For each later branch, stipulate that the named family and policy editions resolve and R0 passes; the QD case also passes R0.QD. Every Admit below additionally requires the complete R1 Eligibility, evidence and Acceptance basis. If a stipulated prerequisite is missing, use the early-Abstain result in §4.2.1 instead.

**Show‑1 - Continuous dynamics (ODE task).**
*S2 excerpt.* `DataShape=ODE; stiff?=unknown; Hamiltonian=unknown; Size≈10^3; Objective={↓error@ratio, ↑throughput@ratio}; Jacobian_sparsity=high; Missingness=MAR`. A declared safety predicate tests the required ordinal safety level.
*Families.* `Implicit‑BDF` vs `Explicit‑RK` vs `Symplectic`.
*Rules.*
- `Implicit‑BDF`: with `Jacobian_sparsity=high`, its declared unknown-handling branch permits `Degrade(probe-only)` under exploration policy `EE-ODE-1` and Acceptance-bound guards `Probe-ODE-1`. An applicable L3 maturity judgement remains cited. If later observations establish `stiff?=true` and `Hamiltonian=false`, and the complete R1 basis for the intended use holds, that new input can receive `Admit`; the original unknown is not silently converted to true.
- `Explicit‑RK`: requires `stiff?=false` for ordinary use. Its declared unknown branch permits `Degrade(sandbox)` after R0 and eligibility are checked for that bounded use.
- `Symplectic`: requires `Hamiltonian=true`; its declared branch for the live `unknown` returns `Abstain`, without reporting a false Hamiltonian judgement.
*Didactic anchor.* This mirrors C.22’s typed‑signature discipline and CHR legality (no ordinal means; unit alignment for **ratio**).

> The cited ecosystem examples of these families (post‑2015) are organised in **DifferentialEquations.jl**, which exposes multiple solver **families** under one call surface—precisely the pattern G.5 expects. ([Journal of Open Research Software][17])

**Show‑2 - Planning/scheduling (MIP task).**
*S2 excerpt.* `DataShape=MIP; NoiseModel=deterministic; Objective={↓cost@ratio, ↑service_level@ordinal}; Size≈10^5 vars; convex_relaxation=available`.
*Families.* `MILP (branch‑and‑bound)`, `Constraint‑Programming`, `Heuristic meta‑search`.
*Rules.*
- `MILP`: **Eligibility** requires `convex_relaxation=available`; the cited L3 MaturityCard edition names the registered family, evidence profile, benchmark basis, claim scope, qualification window, and intended selector use ⇒ `Admit`.
- `Constraint‑Programming`: **MaturityCard**=`L2`; the ordinal `service_level≥B` Acceptance predicate is met. Baseline parity is an additional CAL condition, not a missing R0 minimum in this example. Its declared failure behavior permits `Degrade(scope-narrow)` while parity is unresolved, after R0 and eligibility pass for the narrowed use. If that parity basis were required by R0, the result would be `Abstain`.
- `Heuristic meta‑search`: **MaturityCard**=`L1`. The applicable AcceptanceClause and family failure policy decide between a permitted `Degrade(sandbox)` branch and `Abstain`; L1 alone supplies neither outcome.
*Didactic anchor.* G.5 declares a `Shortlist` of the non-dominated retained candidates, with its comparison basis and unresolved ties; no cross-ordinal weighting is introduced.

> The cited “single call / many solvers” packaging that motivates MethodFamily rows is exemplified by **JuMP** (2017–2022), which cleanly separates **model description** from solver choice. ([Miles Lubin][18])

- *DifferentialEquations.jl* illustrates **family‑based** solver packaging (multi‑method under one interface), 2017–2024 ecosystem. ([Journal of Open Research Software][17])
- *JuMP* illustrates **model/solver separation** and registry‑like selection (2021–2022 papers, site). ([Miles Lubin][18])
- *Science of Science* review (2018) supports the emphasis on replication/benchmarks in maturity assessment. ([Science][19])

**Show‑3 - QD archive (policy search).**
*S2 excerpt.* `PortfolioMode=Archive; CharacteristicSpaceRef(d=2); ArchiveConfig(CVT, res=1k cells, K=1, DistanceDefRef.edition=v2, InsertionPolicyRef=dyn‑elite); EmitterPolicyRef=v3; DominanceRegime=ParetoOnly`.
*Rules.* After `Admit`, G.5 declares a `Shortlist` drawn from the QD archive, with exact members, ordering and basis under G.5:4.4b–4.4e. The archive remains its source. Illumination is reported separately; changes to `DistanceDef` or the emitter are editioned in SCR; dominance remains **ParetoOnly**.

**Show‑4 - Open‑ended GeneratorFamily (POET‑class).**
*S2 excerpt.* `GeneratorIntent{GeneratorFamilyRef=GF‑01, EnvironmentValidityRegion=EVR‑A, TransferRulesRef=TR‑A, CoverageMetric=…}; PortfolioMode=Archive`.
*Rules.* After `Admit`, G.5 declares a `Shortlist` over eligible `{environment, method}` pairs with its source and selection basis; `Degrade(scope-narrow)` if `TransferRules`=`unknown`, as permitted by the family policy under R7. Telemetry publishes the declared **coverage and regret** with their edition and policy basis. This use requires no QD search or illumination report. If a later receiving use needs **IlluminationSummary**, obtain its C.17:5.1 measurement basis and retain the governing policy id on improvements.

[17]: https://openresearchsoftware.metajnl.com/articles/10.5334/jors.151 "DifferentialEquations.jl – A Performant and Feature-Rich … "
[18]: https://mlubin.github.io/pdf/jump-sirev.pdf "JuMP: A Modeling Language for Mathematical Optimization"
[19]: https://www.science.org/doi/10.1126/science.aao0185 "Science of science"

