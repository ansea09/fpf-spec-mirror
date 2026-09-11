---
chunk_kind: "child"
pattern_id: "A.3.3"
pattern_title: "U.Dynamics: State-Space and Transition-Law Episteme"
section_id: "A.3.3:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3/A.3.3__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "cda9087f48e0bce2c5f9d5f4389e7e025c7678f5"
heading_path:
  - "A.3.3 — U.Dynamics: State-Space and Transition-Law Episteme"
  - "A.3.3:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 9246
line_end: 9256
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.19"
  - "A.20"
  - "A.21"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "B.3"
  - "C.27"
  - "C.27.TA"
  - "C.29"
keywords:
  - "calibration"
  - "dynamics"
  - "observation relation"
  - "prediction"
  - "simulation"
  - "state space"
  - "transition law"
---

### A.3.3:8 - Common Anti-Patterns and How to Avoid Them

| Recognizable failure | Repair |
| --- | --- |
| Inferring a transition law from procedure text or a workflow diagram's layout | Recover the actual assertion under :4.8, then test for both a state space and a transition law under :4.1. |
| Treating telemetry as a law | Declare the proposed law, derive the observed coordinates through :4.5 and compare its consequences with the telemetry. |
| Using dashboard labels as state coordinates without their meanings | Recover the characteristics, units, scales and comparability rules, and check whether the chosen coordinates retain the needed predictive information. |
| Treating a simulation as release approval | Check its predicted result against the receiving decision's conditions in :4.6, then obtain that decision. |
| Extrapolating beyond established model conditions | State the applicable region, source-currentness condition and lowering condition; use :4.7 if the use requires transfer. |
| Relying on a learned prediction without its domain and error conditions | State its training domain, observation relation, error or uncertainty policy and applicability window before reliance. |

