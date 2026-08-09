---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "GateProfilization: OperationalGate(profile) (GateFit core)"
section_id: "A.21:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__006_archetypal-grounding.md"
commit_sha: "036c056e98c38522172c6b7b3ad08214281cc4e4"
heading_path:
  - "A.21 — GateProfilization: OperationalGate(profile) (GateFit core)"
  - "A.21:5 — Archetypal Grounding"
line_start: 34213
line_end: 34232
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

### A.21:5 - Archetypal Grounding

#### A.21:5.1 - System vignette — “Regulated release gate”

**Show 0 (green cue, no gate decision).** A dashboard tile says “ready” because a source system returned green. No `OperationalGate(profile)`, `GateCheckRef` set, `GateDecision`, or `DecisionLogRef` is named. The tile remains orientation or source-finding only; it is not gate passage and does not establish A.21 decision reuse.

**Tell.** A `PathSlice` includes a `LaunchGate` immediately before performed `U.Work` that can finalize binding. The current `GateProfile` is `RegulatedX`. The gate publishes a single `GateDecision` and a `DecisionLog` explaining the release-crossing decision, without encoding any execution method.

**Show A (CV ✔, GF ✖).** `CV.Status=pass`, activating GateFit. `RegulatedConformance(X)` is present but evidence references are incomplete (`EvidenceCompleteness` folds to `degrade` under `Core` or `RegulatedX` policy), so the join yields `GateDecision=degrade`. The DecisionLog records which `GateCheckRef` caused the fold and the declared publish reaction for degraded release.

**Show B (CV ✖, GF not applicable).** CV aggregate is `degrade`. All GateFit checks return `abstain` by activation, and any GateFit-oriented explanation is inapplicable. The gate’s published decision is driven by CV; the DecisionLog shows CV status and the “inactive GF” boundary rather than a fabricated GF narrative.

#### A.21:5.2 - Episteme vignette — “Cross-plane comparability gate”

**Tell.** A `PathSlice` includes a comparability-critical step (CSLC). The gate publishes `BridgeId + UTS + CLPlane` and edition pins for downstream consumers, and remains stable under the `A.21` equivalence witness.

**Show A (Core, clean crossing).** The gate publishes `EditionPins{CGSpec, ComparatorSet, TransportRegistryPhi}`, `ComparatorSetRef`, `CL` and `CLPlane`, and a `GateDecision=pass` with a rationale that cites the relevant `GateCheckRef`s and editions.

**Show B (SquareLaw mismatch).** A crossing attempts to change plane pins without the commutative-square witness; the SquareLaw check yields `block` (or `degrade` under a profile with a less strict fold policy), and the DecisionLog records the mismatched pins as the reason.

