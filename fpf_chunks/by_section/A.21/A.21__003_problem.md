---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "GateProfilization: OperationalGate(profile) (GateFit core)"
section_id: "A.21:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__003_problem.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "A.21 — GateProfilization: OperationalGate(profile) (GateFit core)"
  - "A.21:2 — Problem"
line_start: 27476
line_end: 27484
dependencies:
  - "A.19"
  - "A.2.6"
  - "A.20"
  - "A.7"
  - "C.18"
  - "C.19"
  - "E.17"
  - "E.18"
  - "E.TGA"
  - "F.17"
  - "F.9"
  - "G.0"
  - "G.11"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
  - "CV⇒GF"
  - "DecisionLog"
  - "EquivalenceWitness"
  - "GateChecks"
  - "GateDecision"
  - "GateFit"
  - "GateProfile"
  - "LaunchGate"
  - "OperationalGate"
  - "join-semilattice"
---

### A.21:2 - Problem

Without a unified GateFit core:

* Gate admissibility becomes ad-hoc, **order-dependent**, and hard to audit (especially with multiple independent checks).
* Gate logic enters CV (planes/comparators/freshness/roles appear “inside steps”), collapsing the CV/GF separation.
* “Unknown / timeout / error” behavior becomes implicit and inconsistent across cases, undermining reproducibility and safety.
* Publication faces drift into “extra semantics” (computed scalars / tool encodings) rather than pins + refs, breaking MVPK discipline.

