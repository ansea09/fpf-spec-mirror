---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment & Bridge across Contexts"
section_id: "F.9:8"
section_title: "The Bridge Card (compact sketch)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__009_the-bridge-card-compact-sketch.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "F.9 — Alignment & Bridge across Contexts"
  - "F.9:8 — The Bridge Card (compact sketch)"
line_start: 63277
line_end: 63295
dependencies:
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.9"
  - "A.6.Q"
  - "B.3"
  - "C.25"
  - "C.26"
  - "C.26.1"
  - "E.10.D1"
  - "E.17.1"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.7"
  - "F.8"
  - "F.9.1"
  - "U.BoundedContext"
  - "U.Mechanism"
keywords:
  - "Bridge-supported use"
  - "CL"
  - "bridge"
  - "bridge reading"
  - "cross-context alignment"
  - "direction"
  - "loss notes"
  - "state export"
  - "weakest-link scope"
---

### F.9:8 - The Bridge Card (compact sketch)

> A **thought-format** (not a form). Every bullet can be said in a sentence.

* **Cells.** `A@contextA` - `B@contextB`.
* **senseFamily.** *Role, Status, Measurement, Type-structure, Method, or Execution ...*
* **Kind.** *Equivalence / Narrower-than / Broader-than / Partial-overlap / Disjoint / Design-spec -> Run-trace / Measure-of / Policy-implies*.
* **Direction.** *A -> B* (if non-symmetric) or *A <-> B*.
* **CL.** *0–3* with a short **why**.
* **Loss Notes (bullets).** What fails to carry (units, scope, granularity, preconditions, time stance).
* **Counter-example.** The crispest case where substitution would mislead.
* **Supported use.** *Naming-only / Role Assignment & Enactment-eligible / Type-structure / Explanation-only*.
* **Didactic hook.** The helpful sentence a careful engineer can remember.

*If it does not fit on a screen, you are describing the Contexts, not the Bridge.*

**Registry-reference note (normative).** `BridgeId` and any policy/edition identifiers cited by a Bridge Card are **registry references** (keys into registries), not semantic symbols exported by signatures. Therefore they MUST NOT be demanded via `SignatureManifest.provides` (or "satisfied" via `imports` closure); conformance is checked by validating that the referenced registry entries exist and, where required, are edition-pinned (see F.15).


