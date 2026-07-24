---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "GateProfilization: OperationalGate(profile) (GateFit core)"
section_id: "A.21:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__008_conformance-checklist.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "A.21 — GateProfilization: OperationalGate(profile) (GateFit core)"
  - "A.21:7 — Conformance Checklist"
line_start: 33820
line_end: 33858
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

### A.21:7 - Conformance Checklist

**Conformance use.** This checklist is evidence for the gate-decision publication guidance already stated in the Solution. It is not the first entry text for ordinary use and not a full audit regime by default; a checklist row is applied only when its corresponding gate, check set, decision, crossing, launch, publication, or assurance relation is present. Before applying any row, name the Solution relation it tests; if no such practitioner use is present, treat the row as orientation-only or not applicable rather than expanding the applied assurance or conformance material.

**Conformance groups.** Ordinary gate use starts with the current gate, check set, CV aggregate, `GateDecision`, and `DecisionLogRef`. Crossing and launch rows apply only when the gate is a GateCrossing or `LaunchGate`. Publication and assurance rows apply only when MVPK faces, evidence references, decision stability, or replay are present. Extension and change rows apply only when lexical tokens, profile variants, or neighboring policy or evidence loci are being changed or consumed.

Minimum unified conformance for A.21 and for any `PathSlice` or gate-bearing transformation-flow value where GateFit discipline is asserted:

#### A.21:7.1 - Core gate semantics

* [ ] **CC‑TFS‑06**: all GateCrossings (CtxState changes, and work-boundary crossings via LaunchGate) are mediated by `OperationalGate(profile)` and have a `DecisionLog`.
* [ ] **CC‑TFS‑07**: CV=>GF activation predicate holds (`CV.Status!=pass => GF=abstain`).
* [ ] **CC-TFS-21**: decision stability witness is present on the `DecisionLog` record as an `A.21` `EquivalenceWitness` or `EquivalenceWitnessRef`.
* [ ] **CC‑TFS‑21a**: aggregation is the join on `GateDecision` values `abstain <= pass <= degrade <= block`; `GateDecisionExplanation` is optional and non-decisional.
* [ ] **CC‑TFS‑22**: `error|timeout` folds are profile-bound; `unknown` folds per GateCheck policy.
* [ ] **Gate-looking display boundary**: a dashboard state, green tile, readiness badge, conformance label, CV result, safety-envelope note, or release screen is not gate passage unless current `OperationalGate(profile)`, effective `GateCheckRef` set, aggregate, `GateDecision`, `DecisionLogRef`, scope, currentness, and effective window are recoverable.

#### A.21:7.2 - LaunchGate discipline (pre-run barrier)

* [ ] **CC‑TFS‑08**: every performed `U.Work` launch boundary has one and only one `LaunchGate` with mandatory `FreshnessUpToDate` and `DesignRunTagConsistency`; **pre‑run barrier:** if `ConstraintValidityStatus!=pass` over the declared ingress predecessor set or ingress cut-set for the addressed `PathSlice`, then all LaunchGate GateFit checks are `abstain` and the overall `GateDecision=block` (logged).

* [ ] **Pre‑Run barrier** is satisfied for any `U.Work` where `FinalizeLaunchValues` is possible.

#### A.21:7.3 - Publication and evidence

* [ ] **CC‑TFS‑20**: `PublishMode=Lite` changes face reduction only; required GateChecks remain intact.

* [ ] **CC‑TFS‑25**: AssuranceLane carries `GateProfile`, `GateCheckRef` list, edition pins, `GateDecision`, and `DecisionLogRef` with the two-part evidence scheme (SCR or RSCR plus VALATA).

#### A.21:7.4 - Cross-boundary additions (when the gate is a crossing)

* [ ] **CC‑TFS‑11**: crossings publish `BridgeId + UTS + CLPlane` and `CL^plane`; penalties appear in the R-channel only.
* [ ] **CC‑TFS‑23**: SquareLaw holds on crossings; mismatch yields `block|degrade` per profile and is logged.

#### A.21:7.5 - Lexical norms (E.10 discipline)

* [ ] Tech names are ASCII and twin-labeled; required token classes are registered under LEX (including `GateProfile`, `GateCheckKind`, `GateCheckRef`, `DecisionLog`).
* [ ] Any lexical alias view is trace-only and cannot change `GateDecision`.

