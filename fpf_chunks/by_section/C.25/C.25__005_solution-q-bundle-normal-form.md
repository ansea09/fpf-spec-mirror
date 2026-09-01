---
chunk_kind: "child"
pattern_id: "C.25"
pattern_title: "Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
section_id: "C.25:4"
section_title: "Solution - Q-Bundle normal form"
source_path: "FPF-Spec.md"
output_path: "by_section/C.25/C.25__005_solution-q-bundle-normal-form.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "C.25 — Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
  - "C.25:4 — Solution - Q-Bundle normal form"
line_start: 53487
line_end: 53529
dependencies:
  - "A.10"
  - "A.15"
  - "A.16.0"
  - "A.18"
  - "A.2.6"
  - "A.6.1"
  - "B.3"
  - "C.16"
  - "C.16.P"
  - "C.16.Q"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.2.2a"
  - "C.26.3"
  - "C.33"
  - "C.34"
  - "C.35"
  - "F.9"
  - "F.9.1"
keywords:
  - "admissible quality-family use"
  - "characteristic plus scope"
  - "endpoint classification"
  - "failure mode"
  - "ility"
  - "mechanism/status slots"
  - "proxy metric"
  - "quality bundle"
  - "quality family"
  - "viability envelope"
---

### C.25:4 - Solution - Q-Bundle normal form

`C.25` defines a lightweight normal form for the claim content of engineering quality families. A publisher facing a quality term first decides whether one claim episteme should state:

- **one admissible CHR characteristic**, or
- **one structured quality bundle** whose measurable slots, scope slots, mechanisms, statuses, and evidence remain explicit.

#### C.25:4.1 - Endpoint split

Use the **single-characteristic branch** when one exact `U.Characteristic`, one declared Scale, and the ordinary CHR laws carry the quality claim. The claim-bearing result is still one `C.2.1` episteme about its exact bearer; C.25 adds no bundle record.

Use the **Q-Bundle branch** when several differently typed contributors are part of one quality claim. The result is one `C.2.1` episteme whose ClaimGraph contains the record-shaped Q-Bundle content below.

#### C.25:4.2 - Q-Bundle shape and identity boundary

The full escalation form is:

`Q-Bundle := <Name, QualityBearer, ClaimScope?, WorkScope?, Measures[CHR], QualificationWindow?, Mechanisms?, Status?, Evidence?>`

`Q-Bundle` names a C.25-local record-shaped part of one exact `U.ClaimGraph`. It is not a new Kernel kind, an independently identified world object, or a second identity beside the enclosing episteme. That episteme supplies the exact claim content, one independently identified `QualityBearer` as its EntityOfConcern, and the effective `U.ReferenceScheme` under which the quality claim is read.

The `?` is operative: omit any optional slot unless changing it could change the current claim or receiving action. A bundle may therefore contain only Name, QualityBearer, Measures, and one load-bearing scope or window. The full tuple is an escalation aid, not a form every author must fill.

Changing any bundle content that changes the quality claim changes the ClaimGraph and therefore identifies another episteme under `C.2.1`. A changed layout, form, publication occurrence, or carrier can leave that episteme unchanged. A gate, publication, proxy, comparison, or roll-up cites the exact episteme or one exact `C.2.1 ClaimAddress`, meaning the exact edition plus an intrinsic claim identity declared by that edition's ClaimGraph. Later `ClaimAddress` uses in C.25 mean that same value; a field list or raw record reference is not enough.

#### C.25:4.3 - Field meanings

- **Name.** The engineering quality family label inside the claim content, such as `Availability`, `Resilience`, or `Security`; it is not an identity key.
- **QualityBearer.** The one independently identified EntityOfConcern of the enclosing claim episteme. It may be an exact `U.System`, `U.PromiseContent`, `U.Episteme`, or another exact entity under its direct identity pattern. When selected organization is the subject, use one `A.22` `U.Structure` with exact constituents, selected obtaining relations, applied constraints, and one selection-use frame. A list of local system-role kinds and assignment occurrences does not by itself identify a bearer.
- **ClaimScope / WorkScope.** USM sets over `U.ContextSlice` describing where the claim holds or where the capability can deliver. These are **set-valued scope objects**, not characteristics.
- **Measures[CHR].** One or more admissible CHR characteristics, each bound to one declared scale.
- **QualificationWindow.** The temporal policy under which the quality claim is judged.
- **Mechanisms / Status.** References to `U.Mechanism` realizations, control presences, certification states, or similar gating structures. They are not measurements.
- **Evidence.** Anchors that justify the measures, mechanisms, or scope claims.

#### C.25:4.4 - Guard reading

A quality guard is conjunctive only over the truth conditions that the current claim actually declares. For example:

`declared scope covers TargetSlice AND declared measures satisfy their own laws AND each other declared prerequisite holds`

An absent optional slot contributes no condition. Each measure keeps its own Scale and comparison law; a trade-off, alternative, weighted combination, or partial order must be stated under the pattern that defines it rather than being smuggled into `AND`. If this typed decomposition cannot express what makes the claim true, do not force the family into C.25.

