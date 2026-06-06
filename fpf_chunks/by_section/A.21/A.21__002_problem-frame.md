---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "GateProfilization: OperationalGate(profile) (GateFit core)"
section_id: "A.21:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__002_problem-frame.md"
commit_sha: "e3fedf42dc7cb5d12905913b5a0b0e951ed7d254"
heading_path:
  - "A.21 — GateProfilization: OperationalGate(profile) (GateFit core)"
  - "A.21:1 — Problem frame"
line_start: 27663
line_end: 27704
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

### A.21:1 - Problem frame

#### A.21:1.1 - Intent & scope

This pattern is the governing locus for canonical gate-decision publication content for `OperationalGate(profile)`: `GateCheckRef` as the GateFit check-catalog boundary, gate aggregation, `GateDecision` terminology, `GateDecisionRationale`, `GateDecisionExplanation`, `DecisionLog` minima, profile-bound folds, and A.21 decision equivalence. A.20 governs CV class meaning; an A.21 gate-decision relation may consume referenced CV results but does not define CV class semantics. Receiving patterns govern the domain truth conditions of their checks.

Within that boundary, A.21:

* aggregates per-check outcomes into a single **published** `GateDecision` using the join lattice,
* states the **CV⇒GF** activation boundary: GateFit checks are inactive until `CV.Status=pass`,
* defines the minimal **publication faces** and `DecisionLog` content required to make gate outcomes auditable and replayable,
* applies **SWP at the gate**: `OperationalGate(profile)` and its `GateCheck`s are **ref-only** with respect to editions, registries, and domain publications or records; A.21 publishes **only** `GateDecision` + `DecisionLog` pins and refs, and MUST NOT declare or mutate edition families.
This pattern is **about the semantics of what is published** (and how it composes), not about procedural execution.

#### A.21:1.2 - GateFit EntityOfConcern

* **`OperationalGate(profile)`** — a gate node (`U.Transduction(kind=Check)`) that mediates any **GateCrossing**: any change in `CtxState = ⟨L,P,E⃗,D⟩` **or** entry to `U.WorkEnactment` (via `LaunchGate`).
* **`GateProfile`** — the profile-bound constraint of the partial function `CtxState_from -> CtxState_to`; this pattern carries the current binding and minimum profile semantics. Fuller project-local profile matrices are support material unless a current governing pattern explicitly admits them.
* **`GateCheckRef`** — the publication lexeme that binds a check to `(aspect, kind, edition, scope)`.
* **`GateDecision` / `GateDecisionRationale` / `GateDecisionExplanation`** — decision value, structured rationale, and optional narrative (non-decision).
* **`DecisionLog`** — append-only audit record linking decisions to check refs, rule anchors, and (where applicable) SquareLaw mismatches.

#### A.21:1.3 - CV vs GF boundary (what “activation” means)

* **ConstraintValidity (CV)** evaluates *internal step validity*;
* **GateFit (GF)** is an aspect label on `GateCheckRef` for checks that evaluate *external admissibility vs `GateProfile`* (planes/crossings, freshness, evidence, roles/channels, regulator conformance, etc.). It is not a `U.Type`, node, record family, module, queue, or stage in the flow.

* **Ordering & activation.** CV is evaluated before GateFit; **while `CV.Status != pass`, all GateFit checks return `abstain`.**

#### A.21:1.4 - Failure cases (diagnostic lens)

* **CV ✔ / GF ✖**: internally valid transformation, but wrong gate/profile/role/timing/evidence.
* **CV ✖ / GF ?**: fix mechanism validity first; GF is inactive.
* **CV ✔ / GF ✔**: the gate may publish admissibility for the declared crossing; for `LaunchGate`, this is admissibility of crossing into `U.WorkEnactment`, not actual work occurrence.

#### A.21:1.5 - Non-goals

* No procedural semantics (no scheduling, no API formats, no automation narratives).
* No “second process order” outside the graph: every **check-point** is an `OperationalGate(profile)` node in the same transduction graph; its **pluggable GateChecks** are declared on the node (no floating checks), and only the declared check set + reaction rules vary across gates.
* No key/hash/cache *formats*: A.21 constrains **equivalence + invalidation conditions**, but not key materialization.
* No lexical “pseudo-gating”: a lexical alias view is non-decisional and MUST NOT be modeled as a GateCheckKind.

