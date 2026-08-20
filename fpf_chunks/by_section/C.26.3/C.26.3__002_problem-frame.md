---
chunk_kind: "child"
pattern_id: "C.26.3"
pattern_title: "Viability-Envelope Boundary Regulation"
section_id: "C.26.3:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.26.3/C.26.3__002_problem-frame.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "C.26.3 — Viability-Envelope Boundary Regulation"
  - "C.26.3:1 — Problem frame"
line_start: 54367
line_end: 54393
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

Most envelope work covered by this pattern is ordinary control, quality, SRE, causal, or work discipline, not QL. FEP, allostasis, and active inference are source analogies for envelope discipline, sensor and action coupling, and partial observability; ordinary control, SRE, quality-bundle, causal, and work patterns remain primary unless probe, order, export, or coarsening cue remains load-bearing after ordinary viability, quality, dynamics, measurement, boundary, and work patterns have carried their part.

| Working card | Value |
| --- | --- |
| Primary reader | Architect, platform lead, reliability lead, product manager, or operations lead preserving viability under changing conditions. |
| Primary EntityOfConcern | A viability-envelope claim or plan about one exact object already identified under its subject pattern, with the protected promise/function named separately. |
| Admissible move | Point the local viability-bearer position to that exact object and record the pattern used to identify it; then name envelope variables, disturbance, sensors/probes, candidate interventions, boundary condition, adaptation cost, and failure mode. |
| Outside work | One-metric quality tuning, generic control theory, biological proof, full FEP doctrine, and ordinary feedback without an envelope/boundary claim. |
| What changes in practice | The team stops treating one dashboard value as viability and designs the actual envelope-regulation move. |

Plain glosses:
- `viability bearer`: a local lens position, not a kind or relation. It points to one exact object already identified through the pattern for that object. A system reading requires A.1; a selected configuration of system-role kinds and assignments or another structure requires the pattern for its exact relation or structure; a population or market slice requires a declared domain and effective reference scheme, membership or scope, and identity basis. If none is available, stop.
- `protected promise / function`: the separately governed `U.PromiseContent`, stakeholder-value claim, function claim, operating-regime claim, commitment payload, or delivery promise whose continued satisfaction or realization the regulation decision is meant to protect. It is not a slot or part of the object in the local viability-bearer position.
- `service` or market wording: the wording does not itself identify the object in the viability-bearer position. Recover one exact object under the identity rule stated in its pattern, using the system, selected system-role configuration or other structure, or population or market-slice conditions above as applicable; keep promise content, access points, assignments, commitments, Work occurrences, evidence, and direct relations as separately governed claims. If no exact object can be identified, stop; do not turn the phrase into a bearer kind, situation kind, or bundle.
- `viability envelope`: the region of declared characteristic values within which the exact object remains inside the viability bounds stated for the current protected claim or use.
- `envelope variable`: one characteristic that must stay within bounds, such as latency, reliability, support load, compliance exposure, safety margin, energy, or operator attention.
- `actuator` / `candidate intervention`: *actuator* is a control-theory or source label, not an FPF kind and not a synonym for Work. Use *candidate intervention* only as a local prompt until its proposal-side object is recovered: a Method; a `U.MethodDescription` or policy episteme; a proposed setting change; a `U.WorkPlan`; an access or permission claim; or a Bridge proposal or description. Separately identify any dated `U.Work`, independently grounded `U.Transformation`, obtaining relation occurrence, or resulting state claimed to exist. Keep these objects distinct.
- `allostasis`: preserving function through separately governed changes to settings, environment relations, boundary conditions, or operating regime when circumstances change.

