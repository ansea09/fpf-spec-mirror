---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "GateProfilization: OperationalGate(profile) (GateFit core)"
section_id: "A.21:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__010_consequences.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "A.21 — GateProfilization: OperationalGate(profile) (GateFit core)"
  - "A.21:9 — Consequences"
line_start: 34190
line_end: 34204
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

### A.21:9 - Consequences

**Benefits**

* **Deterministic gating.** Join-semilattice aggregation makes decisions order-independent and idempotent (modulo declared equivalence), enabling consistent audit and replay.
* **Clean CV and GF separation.** Activation boundary keeps profile concerns out of mechanism validity.
* **Profile clarity.** Fold policies (`error|timeout|unknown`) are explicit and profile-bound, making safety review result inspectable.
* **Publication hygiene.** MVPK faces remain pins and references (no new numeric claims), and DecisionLog captures rationale without procedural commitments.

**Trade-offs**

* **More decision records to publish.** Decisions are not just binary pass-or-fail values: they require rationales, pins, and logs.
* **Two-stage reasoning.** Users need the rule “GF does not apply until `CV.Status=pass` holds”; mitigated by explicit inapplicability rules and optional narratives only when applicable.
* **Scope complexity.** Multi-scope merge semantics can feel heavy; mitigated by union + worst-wins + preserved rationales.

