---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "GateProfilization: OperationalGate(profile) (GateFit core)"
section_id: "A.21:9"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__010_rationale.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "A.21 — GateProfilization: OperationalGate(profile) (GateFit core)"
  - "A.21:9 — Rationale"
line_start: 27753
line_end: 27762
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

### A.21:9 - Rationale

* The microkernel framing preserves a single graph semantics: checks are nodes and publications, not an external pipeline; this keeps a second hidden process order outside the gate core.
* The join lattice provides a minimal, monotone aggregation that supports:

  * early absorption at `block` without specifying execution strategy, and
  * deterministic publication semantics (commutative + associative + idempotent).
* CV⇒GF activation is the mechanism that keeps orthogonality strict while still publishing a single gate decision publication: GF results do not replace CV failures.
* Explicit folds for `error|timeout|unknown` make safety posture reviewable and profile-specific without inventing new decision values.

