---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "GateProfilization: OperationalGate(profile) (GateFit core)"
section_id: "A.21:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__013_relations.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "A.21 — GateProfilization: OperationalGate(profile) (GateFit core)"
  - "A.21:12 — Relations"
line_start: 33839
line_end: 33848
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

### A.21:12 - Relations

* **`E.18` transformation-flow structure →coordinates→ A.21.** GateFit-scoped GateChecks are aggregated by `OperationalGate(profile)`; GateCheck enumeration and publication shape are governed here.
* **A.20 →couples_to→ A.21 via CV=>GF.** CV is evaluated inside transformations; while `CV.Status!=pass`, GF is `abstain` and GF explanations do not apply.
* **A.15.5 →separates→ work-entry readiness from gate decision.** Full-kit and work-entry readiness labels may be cited by A.21 only when they are declared GateChecks under a current `GateProfile`; otherwise `WorkEntryReadiness@Context` remains governed by A.15.5.
* **A.21 GateProfile binding.** A.21 carries the current profile binding, inheritance boundary, and minimum mandatory check-set semantics. Fuller project-local profile matrix material is not separately governing unless a current governing pattern includes it by value.
* **E.18 and G.11 →provide→ scope and refresh boundaries.** `subflow` scope is bounded and restartable through PathSlice and refresh wiring where present; weakening check sets use a new `PathSlice`.
* **F.9, F.17, E.17, and E.18 →required_by→ any edition-citing face.** Whenever gate faces cite editions, the compatibility reference (BridgeCard + UTS + `CL` and `CLPlane`) is required for downstream consumption.
* **A.21, G.6, and G.11 →define→ equivalence for decision stability.** Gate decisions are stable only under the declared equivalence witness; evidence-provenance or refresh implications use `G.6` or `G.11` where present.

