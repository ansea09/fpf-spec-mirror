---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "GateProfilization: OperationalGate(profile) (GateFit core)"
section_id: "A.21:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__011_rationale.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "A.21 — GateProfilization: OperationalGate(profile) (GateFit core)"
  - "A.21:10 — Rationale"
line_start: 33673
line_end: 33682
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

### A.21:10 - Rationale

* The microkernel framing preserves a single graph semantics: checks are gate/check loci and decision publications, not an external execution sequence; this keeps a second hidden execution order outside the gate core from appearing.
* The join lattice provides minimal, monotone aggregation with two useful properties:

  * early absorption at `block` without specifying execution strategy, and
  * deterministic publication semantics (commutative, associative, and idempotent).
* CV⇒GF activation is the mechanism that keeps orthogonality strict while still publishing a single gate decision publication: GF results do not replace CV failures.
* Explicit folds for `error|timeout|unknown` make safety review result inspectable and profile-specific without inventing new decision values.

