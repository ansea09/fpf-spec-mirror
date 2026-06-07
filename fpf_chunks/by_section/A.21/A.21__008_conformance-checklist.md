---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "GateProfilization: OperationalGate(profile) (GateFit core)"
section_id: "A.21:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__008_conformance-checklist.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "A.21 — GateProfilization: OperationalGate(profile) (GateFit core)"
  - "A.21:7 — Conformance Checklist"
line_start: 28301
line_end: 28339
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

### A.21:7 - Conformance Checklist

**Conformance use.** This checklist is evidence for the gate-decision publication guidance already stated in the Solution. It is not the first entry text for ordinary use and not a full audit regime by default; an item is applied only when its corresponding gate, check set, decision, crossing, launch, publication, or assurance move is live. Before applying any item, name the Solution move it tests; if no such reader move is live, treat the item as support-only or not applicable rather than expanding the applied assurance or conformance material.

**Conformance groups.** Ordinary gate use starts with the active gate, check set, CV aggregate, `GateDecision`, and `DecisionLogRef`. Crossing/launch items apply only when the gate is a GateCrossing or `LaunchGate`. Publication/assurance items apply only when MVPK faces, evidence carriers, decision stability, or replay are live. Extension/change items apply only when lexical tokens, profile variants, or neighboring policy/evidence loci are being changed or consumed.

Minimum unified conformance for A.21 (and any flow that claims GateFit discipline):

#### A.21:7.1 - Core gate semantics

* [ ] **CC‑TGA‑06**: all GateCrossings (CtxState changes, and work-boundary crossings via LaunchGate) are mediated by `OperationalGate(profile)` and have a `DecisionLog`.
* [ ] **CC‑TGA‑07**: CV=>GF activation predicate holds (`CV.Status!=pass => GF=abstain`).
* [ ] **CC-TGA-21**: decision stability witness is present on the `DecisionLog` record as an `A.21` `EquivalenceWitness` or `EquivalenceWitnessRef`.
* [ ] **CC‑TGA‑21a**: aggregation is the join on `GateDecision` values `abstain <= pass <= degrade <= block`; `GateDecisionExplanation` is optional and non-decisional.
* [ ] **CC‑TGA‑22**: `error|timeout` folds are profile-bound; `unknown` folds per GateCheck policy.
* [ ] **Gate-looking display boundary**: a dashboard state, green tile, readiness badge, conformance label, CV result, safety-envelope note, or release screen is not gate passage unless active `OperationalGate(profile)`, effective `GateCheckRef` set, aggregate, `GateDecision`, `DecisionLogRef`, scope, and currentness/window are recoverable.

#### A.21:7.2 - LaunchGate discipline (pre-run barrier)

* [ ] **CC‑TGA‑08**: every `U.WorkEnactment` has exactly one `LaunchGate` with mandatory `FreshnessUpToDate` + `DesignRunTagConsistency`; **pre‑run barrier:** if `ConstraintValidityStatus!=pass` over the declared ingress predecessor set or ingress cut-set for the addressed `PathSlice`, then all LaunchGate GateFit checks are `abstain` and the overall `GateDecision=block` (logged).

* [ ] **Pre‑Run barrier** is satisfied for any `U.Work` where `FinalizeLaunchValues` is possible.

#### A.21:7.3 - Publication and evidence

* [ ] **CC‑TGA‑20**: `PublishMode=Lite` changes face reduction only; required GateChecks remain intact.

* [ ] **CC‑TGA‑25**: AssuranceLane carries `GateProfile`, `GateCheckRef` list, edition pins, `GateDecision`, and `DecisionLogRef` with the two-part evidence scheme (SCR/RSCR + VALATA).

#### A.21:7.4 - Cross-boundary additions (when the gate is a crossing)

* [ ] **CC‑TGA‑11**: crossings publish `BridgeId + UTS + CLPlane/CL^plane`, penalties appear in the R-channel only.
* [ ] **CC‑TGA‑23**: SquareLaw holds on crossings; mismatch yields `block|degrade` per profile and is logged.

#### A.21:7.5 - Lexical norms (E.10 discipline)

* [ ] Tech names are ASCII and twin-labeled; required token classes are registered under LEX (including `GateProfile`, `GateCheckKind`, `GateCheckRef`, `DecisionLog`).
* [ ] Any lexical alias view is trace-only and cannot change `GateDecision`.

