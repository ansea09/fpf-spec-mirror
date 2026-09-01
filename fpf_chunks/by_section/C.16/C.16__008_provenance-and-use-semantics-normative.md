---
chunk_kind: "child"
pattern_id: "C.16"
pattern_title: "Measurement & Metrics Characterization (MM‑CHR)"
section_id: "C.16:7"
section_title: "Provenance and use semantics (Normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16/C.16__008_provenance-and-use-semantics-normative.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "C.16 — Measurement & Metrics Characterization (MM‑CHR)"
  - "C.16:7 — Provenance and use semantics (Normative)"
line_start: 47923
line_end: 47933
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.6.1"
  - "B.1.6"
  - "B.3"
  - "C.11"
  - "C.16.P"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "G.11"
  - "G.4"
  - "G.6"
keywords:
  - "C.2.1 result episteme"
  - "Characteristic"
  - "Level/Coordinate"
  - "Scale"
  - "Unit"
  - "actual bindings"
  - "bounded later use"
  - "calibration"
  - "comparability"
  - "dated measurement work"
  - "input/output quantities"
  - "measurand"
  - "measurement result"
  - "measurement subject"
  - "method"
  - "model"
  - "polarity"
  - "provenance"
  - "uncertainty"
---

### C.16:7 - Provenance and use semantics (Normative)

#### C.16:7.1 - What an EvidenceStub is and is not

`U.EvidenceStub` is an optional compact locator from the reading claim to an exact provenance path. It may identify a source publication, calibration record, instrument output, model edition, work occurrence, transformation, or other ground, but A.10/G.6 govern the path and its citations.

- The stub is not evidence in the abstract, a result, an instrument output, a work record, an assurance claim, or a provenance-as-result object.
- Several stubs form a list of locators, not a measurement algebra. Their union is not uncertainty propagation and does not guarantee stronger warrant.
- A provenance edge may be asserted only after its direct source relation, work fact, participation, production, representation, or citation relation is independently established.
- A later user states the exact relied-on claim and local `RelianceDisposition`; material reliance or an assurance claim enters B.3. Mere availability, citation, or graph membership does not establish actual use.

