---
chunk_kind: "child"
pattern_id: "C.26.3"
pattern_title: "Viability-Envelope Boundary Regulation"
section_id: "C.26.3:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.26.3/C.26.3__002_problem-frame.md"
commit_sha: "eaafd3a43b9173706e1f8388a3bc94c6445397e4"
heading_path:
  - "C.26.3 — Viability-Envelope Boundary Regulation"
  - "C.26.3:1 — Problem frame"
line_start: 46766
line_end: 46788
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

Use this pattern when architecture work is maintaining, recovering, or changing viable operating ranges across boundaries. The working problem is not "optimize one metric"; it is "keep a bundle of characteristics inside a viable region while disturbances, probes, actuators, boundary conditions, and operating regimes change."

Most envelope work covered by this pattern is ordinary control, quality, SRE, causal, or work discipline, not QL. FEP, allostasis, and active inference are source analogies for envelope discipline, sensor and action coupling, and partial observability; ordinary control, SRE, quality-bundle, causal, and work patterns remain primary unless probe, order, export, or coarsening cue remains load-bearing after ordinary viability, quality, dynamics, measurement, boundary, and work patterns have carried their part.

| Working card | Value |
| --- | --- |
| Primary reader | Architect, platform lead, reliability lead, product manager, or operations lead preserving viability under changing conditions. |
| Primary EntityOfConcern | A viability-envelope claim or plan over a declared viability bearer, with protected promise/function named separately. |
| Admissible move | Name the bearer, envelope variables, disturbance, sensors/probes, actuators, boundary condition, adaptation cost, and failure mode. |
| Outside work | One-metric quality tuning, generic control theory, biological proof, full FEP doctrine, and ordinary feedback without an envelope/boundary claim. |
| What changes in practice | The team stops treating one dashboard value as viability and designs the actual envelope-regulation move. |

Plain glosses:
- `viability bearer`: the `U.System`, collective system, delivery system, role configuration, organism-as-system, or explicitly modelled market slice whose viable range is being regulated.
- `protected promise / function`: the `U.PromiseContent`, stakeholder value, function, operating regime, commitment payload, or delivery promise the bearer is trying to keep viable.
- `service situation`: an `A.6.8` facet-binding lens that identifies access point, delivery system, provider principal, promise content, commitment, delivery work, and evidence; it is not itself a new root bearer unless the relevant system facet is declared.
- `viability envelope`: the region where the bearer can still keep the relevant promise or function, across several dimensions.
- `envelope variable`: one characteristic that must stay within bounds, such as latency, reliability, support load, compliance exposure, safety margin, energy, or operator attention.
- `actuator`: a work move that can change the situation, such as cache policy, throttle, staffing, routing, bridge rewrite, protocol, access, escalation, or measurement design.
- `allostasis`: preserving function by changing settings, environment, boundary condition, actuation, or operating regime when circumstances change.

