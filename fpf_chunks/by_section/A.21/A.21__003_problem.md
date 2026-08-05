---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "GateProfilization: OperationalGate(profile) (GateFit core)"
section_id: "A.21:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__003_problem.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "A.21 — GateProfilization: OperationalGate(profile) (GateFit core)"
  - "A.21:2 — Problem"
line_start: 33962
line_end: 33970
dependencies:
  - "A.19"
  - "A.2.6"
  - "A.20"
  - "A.7"
  - "C.18"
  - "C.19"
  - "E.17"
  - "E.18"
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

* Gate decisions become ad hoc, **order-dependent**, and hard to audit (especially with multiple independent checks).
* Gate logic enters CV: plane claims, comparator claims, freshness claims, or role-channel claims appear “inside steps”, collapsing the CV and GF separation.
* “Unknown”, “timeout”, or “error” behavior becomes implicit and inconsistent across cases, undermining reproducibility and safety.
* Publication faces drift into “extra semantics” (computed scalars or tool encodings) rather than pins and references, breaking MVPK discipline.

