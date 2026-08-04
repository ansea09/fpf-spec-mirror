---
chunk_kind: "child"
pattern_id: "C.25"
pattern_title: "Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
section_id: "C.25:4"
section_title: "Solution - Q-Bundle normal form"
source_path: "FPF-Spec.md"
output_path: "by_section/C.25/C.25__005_solution-q-bundle-normal-form.md"
commit_sha: "7ba40a95a967ca5c69afc63aeca381e6adedc8da"
heading_path:
  - "C.25 — Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
  - "C.25:4 — Solution - Q-Bundle normal form"
line_start: 53073
line_end: 53115
dependencies:
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

`C.25` defines a lightweight authoring normal form for engineering quality families. A publisher facing a quality term first decides whether the intended endpoint is:

- **one admissible CHR characteristic**, or
- **one structured quality bundle** whose measurable slots, scope slots, mechanisms, statuses, and evidence remain explicit.

#### C.25:4.1 - Endpoint split

Use a **single `U.Characteristic`** when the quality claim is genuinely one measurable aspect with one declared scale and ordinary CHR legality.

Use a **Q-Bundle** when the quality family depends on more than one of the following:

- one or more measurable characteristics,
- a declared claim/work scope,
- mechanism or status requirements,
- qualification windows,
- evidence anchors that are not reducible to one scalar.

#### C.25:4.2 - Q-Bundle shape

`Q-Bundle := <Name, QualityBearer, ClaimScope?, WorkScope?, Measures[CHR], QualificationWindow?, Mechanisms?, Status?, Evidence?>`

The pattern adds no new Kernel kind for these slots. It reuses existing kinds and keeps them in one disciplined authoring structure.

#### C.25:4.3 - Field meanings

- **Name.** The engineering quality family label, such as `Availability`, `Resilience`, or `Security`.
- **QualityBearer.** The bearer of the quality claim: typically `U.System`, `U.PromiseContent`, or `U.Episteme`.
- **ClaimScope / WorkScope.** USM sets over `U.ContextSlice` describing where the claim holds or where the capability can deliver. These are **set-valued scope objects**, not characteristics.
- **Measures[CHR].** One or more admissible CHR characteristics, each bound to one declared scale.
- **QualificationWindow.** The temporal policy under which the quality claim is judged.
- **Mechanisms / Status.** References to `U.Mechanism` realizations, control presences, certification states, or similar gating structures. They are not measurements.
- **Evidence.** Anchors that justify the measures, mechanisms, or scope claims.

#### C.25:4.4 - Guard reading

A conforming quality guard typically has the conceptual form:

`Scope covers TargetSlice AND Measures meet thresholds AND QualificationWindow is valid AND required Mechanisms/Status are present`

This keeps coverage, thresholding, and admissibility in separate typed slots instead of hiding them inside one quality adjective.

