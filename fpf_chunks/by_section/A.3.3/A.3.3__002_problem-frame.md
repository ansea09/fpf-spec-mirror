---
chunk_kind: "child"
pattern_id: "A.3.3"
pattern_title: "U.Dynamics: State-Space and Transition-Law Episteme"
section_id: "A.3.3:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3/A.3.3__002_problem-frame.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "A.3.3 — U.Dynamics: State-Space and Transition-Law Episteme"
  - "A.3.3:1 — Problem frame"
line_start: 9046
line_end: 9057
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
  - "C.16"
  - "C.27"
  - "C.27.TA"
  - "C.29"
keywords:
  - "calibration"
  - "configuration"
  - "constraints"
  - "dynamics"
  - "initial data"
  - "observation relation"
  - "permitted alternatives"
  - "prediction"
  - "predictive memory"
  - "probability law"
  - "simulation"
  - "state construction"
  - "transition law"
---

### A.3.3:1 - Problem frame

Use this pattern when you need a reusable account of how a particular subject's state can change: which differences the state must retain, the law relating earlier and later state, and the conditions in which that law applies.

**First useful move.** Name the changing subject and what you want to find about its change. If the state and law are already available, state their meanings in one ordinary sentence; otherwise construct them through :4.4.1. For example: “In this two-substance mixture, the remaining masses in kilograms change from (a,b) to (a/2,b/4) after each treatment cycle; the instrument reports a+b.” The first question is whether the observed total contains enough information to predict the next total. Section 5.6 works out the answer.

If the ordinary statement is sufficient for the current comparison, stop. Add the observation, calibration or assurance account when the receiving use needs it. Before making a prediction, conformance or gate-use claim, name the exact applicability window and any observation relation that use requires; stop that use if a required condition is unavailable.

The practical gain is a model that supports the needed prediction or comparison, or identifies the missing distinction or rule. A model fitted to the wrong state can lose a difference that changes the answer.

This pattern identifies the episteme that states the model's state space and transition law. Section 4.1 gives its membership rule. For a known model and a settled calculation, use the domain calculation directly. When the question instead concerns a procedure, an actual event or another receiving use, use the conditional contributions in :4.3.

