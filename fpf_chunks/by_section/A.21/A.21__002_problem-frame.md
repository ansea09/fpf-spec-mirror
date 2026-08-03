---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "GateProfilization: OperationalGate(profile) (GateFit core)"
section_id: "A.21:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__002_problem-frame.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "A.21 — GateProfilization: OperationalGate(profile) (GateFit core)"
  - "A.21:1 — Problem frame"
line_start: 33981
line_end: 34021
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

### A.21:1 - Problem frame

#### A.21:1.1 - Intent & scope

This pattern is the governing locus for canonical gate-decision publication content for `OperationalGate(profile)`: `GateCheckRef` as the GateFit check-catalog boundary, gate aggregation, `GateDecision` terminology, `GateDecisionRationale`, `GateDecisionExplanation`, `DecisionLog` minima, profile-bound folds, and A.21 decision equivalence. A.20 governs CV class meaning; an A.21 gate-decision relation may consume referenced CV results but does not define CV class semantics. Neighboring governing patterns carry the domain truth conditions of their checks.

Within that boundary, A.21:

* aggregates per-check outcomes into a single **published** `GateDecision` using the join lattice,
* states the **CV⇒GF** activation boundary: GateFit checks are inactive until `CV.Status=pass`,
* defines the minimal **publication faces** and `DecisionLog` content required to make gate outcomes auditable and replayable,
* applies **SWP at the gate**: `OperationalGate(profile)` and its `GateCheck`s are **ref-only** with respect to editions, registries, and domain publications or records; A.21 publishes **only** `GateDecision` and `DecisionLog` pins and references, and does not declare or mutate edition families.
This pattern is **about the semantics of what is published** (and how it composes), not about procedural execution.

#### A.21:1.2 - Primary EntityOfConcern and gate-profile value family

* **`OperationalGate(profile)`** — a gate/check locus in an `E.18` `TransformationFlowStructure` that mediates any **GateCrossing**: any change in `CtxState = ⟨L,P,E⃗,D⟩` or entry to performed `U.Work` through `LaunchGate`.
* **`GateProfile`** — the profile-bound constraint of the partial function `CtxState_from -> CtxState_to`; this pattern carries the current binding and minimum profile semantics. Fuller project-local profile matrices are auxiliary material unless a current governing pattern includes them by value.
* **`GateCheckRef`** — the publication lexeme that binds a check to `(aspect, kind, edition, scope)`.
* **`GateDecision`, `GateDecisionRationale`, and `GateDecisionExplanation`** — decision value, structured rationale, and optional narrative (non-decision).
* **`DecisionLog`** — append-only audit record linking decisions to check refs, rule references, and (where applicable) SquareLaw mismatches.

#### A.21:1.3 - CV vs GF boundary (what “activation” means)

* **ConstraintValidity (CV)** evaluates *internal step validity*;
* **GateFit (GF)** is an aspect label on `GateCheckRef` for checks that evaluate *fit to the current `GateProfile`*: plane fit, crossing fit, freshness, evidence, role-channel fit, regulator conformance, and similar profile-fit claims. It is not a durable U-kind, graph node, record family, module, queue, or stage in the flow.
* **Ordering & activation.** CV is evaluated before GateFit; **while `CV.Status != pass`, all GateFit checks return `abstain`.**

#### A.21:1.4 - Failure cases (diagnostic lens)

* **CV ✔, GF ✖**: the transformation has passing internal CV, but the gate, profile, role, timing, or evidence fit is wrong.
* **CV ✖, GF ?**: fix the internal constraint-validity failure first; GF is inactive.
* **CV ✔, GF ✔**: the gate publishes a `GateDecision` for the declared crossing; for `LaunchGate`, this is the gate decision for crossing into performed `U.Work`, not actual work occurrence.

#### A.21:1.5 - Non-goals

* No procedural semantics (no scheduling, no API formats, no automation narratives).
* No “second hidden execution order” outside the transformation-flow structure: every **check locus** is an `OperationalGate(profile)` in the same `E.18` `TransformationFlowStructure`; its **pluggable GateChecks** are declared on that gate/check locus (no floating checks), and only the declared check set and reaction rules vary across gates.
* No key, hash, or cache *formats*: A.21 constrains **equivalence and invalidation conditions**, but not key materialization.
* No lexical “pseudo-gating”: a lexical alias view is non-decisional and is not modeled as a GateCheckKind.

