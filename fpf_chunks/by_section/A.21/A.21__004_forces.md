---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "GateProfilization: OperationalGate(profile) (GateFit core)"
section_id: "A.21:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__004_forces.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "A.21 — GateProfilization: OperationalGate(profile) (GateFit core)"
  - "A.21:3 — Forces"
line_start: 30539
line_end: 30547
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

### A.21:3 - Forces

* **Separation vs convenience.** Keeping CV internal and GF profile-bound keeps the boundary explicit, but demands a crisp activation boundary.
* **Determinism vs incompleteness.** Gate decisions stay deterministic even when evidence is missing or partial (`unknown`).
* **Safety vs throughput.** Some profiles treat ambiguity as `block`, others as `degrade`.
* **Human comprehension vs formal minimality.** Optional narratives help practitioners understand a gate decision, but are not used as decisions.
* **Reuse vs freshness.** Decision reuse requires explicit equivalence; otherwise re-aggregation is mandatory.
* **Scope granularity vs complexity.** Checks are declared with scopes (`lane|locus|subflow|profile`) and merged; duplicates preserve evidence rather than overwrite it.

