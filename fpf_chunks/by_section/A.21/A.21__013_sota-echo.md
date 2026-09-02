---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "Gate Decisions from Independent Check Results"
section_id: "A.21:11"
section_title: "SoTA echo"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__013_sota-echo.md"
commit_sha: "421266f0a37ab295b1ffd9e214ace6541e21f5be"
heading_path:
  - "A.21 — Gate Decisions from Independent Check Results"
  - "A.21:11 — SoTA echo"
line_start: 35428
line_end: 35436
dependencies:
  - "A.10"
  - "A.15.5"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.20"
  - "B.3"
  - "C.3.2"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.19"
  - "F.6"
  - "F.9"
  - "G.11"
  - "G.6"
keywords:
---

### A.21:11 - SoTA echo

| Practice line already used by A.21 | Adopted move | Limit |
| --- | --- | --- |
| Join-semilattice aggregation in distributed-systems practice | Use an associative, commutative, idempotent worst-result join after explicit mapping. | Algebra does not make unknown or unrun input neutral. |
| Policy evaluation and safety decision tables | Identify the applicable rule, subject, inputs, outcome mapping, and action consequence. | A profile label or default-looking branch is not policy application or authority. |
| Attestation and provenance practice, including in-toto and SLSA lineage | Publish refs and rationale when audit, transfer, or reuse is current. | An attestation, log, or dashboard does not create the gate decision or source truth. |
| Compositional crossing checks | Apply crossing equations to an exact structural crossing when its rule requires them. | A crossing does not imply a semantic Bridge, and a non-crossing gate needs neither. |

