---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "GateProfilization: OperationalGate(profile) (GateFit core)"
section_id: "A.21:11"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__012_relations.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "A.21 — GateProfilization: OperationalGate(profile) (GateFit core)"
  - "A.21:11 — Relations"
line_start: 27776
line_end: 27784
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

### A.21:11 - Relations

* **E.TGA →coordinates→ A.21.** GateFit-scoped GateChecks are aggregated by `OperationalGate(profile)`; enumeration and publication shape of GateChecks live here.
* **A.20 →couples_to→ A.21 via CV=>GF.** CV is evaluated inside transformations; while `CV.Status!=pass`, GF is `abstain` and GF explanations do not apply.
* **A.21 GateProfile binding.** A.21 carries the current profile binding, inheritance boundary, and minimum mandatory check-set semantics. Fuller matrix support is not a separate current authority unless a current governing pattern explicitly admits it.
* **E.18 / G.11 →provide→ scope and refresh boundaries.** `subflow` scope is bounded and restartable through PathSlice and refresh wiring where live; weakening check sets SHALL use a new `PathSlice`.
* **F.9 / F.17 / E.17 / E.18 →required_by→ any edition-citing face.** Whenever gate faces cite editions, the compatibility reference (BridgeCard + UTS + `CL/CLPlane`) is required for downstream consumption.
* **A.21 / G.6 / G.11 →define→ equivalence for decision stability.** Gate decisions are stable only under the declared equivalence witness; evidence-path or refresh implications use `G.6` or `G.11` where live.

