---
chunk_kind: "child"
pattern_id: "C.26.3"
pattern_title: "Viability-Envelope Boundary Regulation"
section_id: "C.26.3:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.26.3/C.26.3__002_problem-frame.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "C.26.3 — Viability-Envelope Boundary Regulation"
  - "C.26.3:1 — Problem frame"
line_start: 55407
line_end: 55435
dependencies:
  - "A.10"
  - "A.15"
  - "A.19"
  - "A.3"
  - "A.6"
  - "B.3"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.25"
  - "C.26"
  - "C.26.1"
  - "C.26.2"
  - "U.Dynamics"
keywords:
  - "allostasis"
  - "boundary regulation"
  - "failure mode"
  - "homeostasis"
  - "metric-induced distortion"
  - "quality bundle"
  - "sensor/probe/actuator split"
  - "service viability"
  - "viability envelope"
---

### C.26.3:1 - Problem frame

Use this pattern when architecture work is maintaining, recovering, or changing viable operating ranges across boundaries. The working problem is not "optimize one metric"; it is "keep a bundle of characteristics inside a viable region while disturbances, probes, candidate interventions, boundary conditions, and operating regimes change."

**What goes wrong if missed.** The team treats one dashboard value, stability slogan, or local metric as viability, while another envelope variable, intervention cost, boundary condition, or failure mode is already breaking the protected promise or function.

**What this buys.** The viability claim becomes an inspectable envelope-regulation decision: the exact object filling the local viability-bearer position and the pattern used to identify it, protected promise or function, variables, disturbances, sensors or probes, candidate interventions, boundary condition, adaptation cost, and failure mode are all named before acting.

Use C.26.3 for the general envelope-regulation claim when several characteristics must remain inside a viable region under a disturbance and a candidate intervention, boundary condition, adaptation cost, or failure mode matters. Continue to use the direct control, quality, SRE, causal, measurement, boundary, and work patterns for the exact objects and claims they define; using them does not make the envelope result leave C.26.3.

QL is an optional coordination branch. Use `C.26` and its QL vocabulary only when a probe, frame, export, coarsening, order, incompatible representation, or measurement-changing-state issue remains load-bearing after the ordinary patterns have carried their part. FEP, allostasis, and active inference remain source analogies rather than a second entry condition.

| Working card | Value |
| --- | --- |
| Primary reader | Architect, platform lead, reliability lead, product manager, or operations lead preserving viability under changing conditions. |
| Primary EntityOfConcern | The exact viability bearer: either one System with its A.1 identity, one A.22 `U.Structure` identified by its four discriminators, or another truthful subject with its direct identity rule. The primary result is a `C.2.1` episteme about that bearer, not a plan or the writing card. |
| Admissible move | Point the local viability-bearer position to that exact object and record the pattern used to identify it; then name envelope variables, disturbance, sensors/probes, candidate interventions, boundary condition, adaptation cost, and failure mode. |
| Outside work | One-metric quality tuning, generic control theory, biological proof, full FEP doctrine, and ordinary feedback without an envelope/boundary claim. |
| What changes in practice | The team stops treating one dashboard value as viability and designs the actual envelope-regulation move. |

Plain glosses:
- `viability bearer`: a local lens position, not a kind or relation. If the bearer is a System, cite that System's A.1 identity. If it is a selected organization of systems, system-role kinds, and assignment occurrences, identify one A.22 `U.Structure` from exact independently identified constituents, exact selected obtaining relation occurrences, exact constraints as applied, and one named selection-use frame. Kind declarations or assignment occurrences listed together do not identify a Structure. A population or market slice instead needs a declared domain and effective reference scheme, membership or scope, and identity basis. If no branch supplies one exact object, stop.
- `protected promise / function`: the separately governed `U.PromiseContent`, stakeholder-value claim, function claim, operating-regime claim, commitment payload, or delivery promise whose continued satisfaction or realization the regulation decision is meant to protect. It is not a slot or part of the object in the local viability-bearer position.
- `service` or market wording: the wording does not itself identify the viability bearer. Apply the A.1 System branch, the four-discriminator A.22 Structure branch above, or the population/market-slice branch, as applicable. Keep promise content, access points, assignments, commitments, Work occurrences, evidence, and direct relations as separate claims. If no branch identifies one exact object, stop; do not turn the phrase or a list of role kinds and assignments into a bearer kind, situation kind, or bundle.
- `viability envelope`: the region of declared characteristic values within which the exact object remains inside the viability bounds stated for the current protected claim or use.
- `envelope variable`: one characteristic that must stay within bounds, such as latency, reliability, support load, compliance exposure, safety margin, energy, or operator attention.
- `actuator` / `candidate intervention`: *actuator* is a control-theory or source label, not an FPF kind and not a synonym for Work. Use *candidate intervention* only as a local prompt until its proposal-side object is recovered: a Method; a `U.MethodDescription` or policy episteme; a proposed setting change; a `U.WorkPlan`; an access or permission claim; or a Bridge proposal or description. Separately identify any dated `U.Work`, independently grounded `U.Transformation`, obtaining relation occurrence, or resulting state claimed to exist. Keep these objects distinct.
- `allostasis`: preserving function through separately governed changes to settings, environment relations, boundary conditions, or operating regime when circumstances change.

