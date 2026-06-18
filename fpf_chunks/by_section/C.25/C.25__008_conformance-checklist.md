---
chunk_kind: "child"
pattern_id: "C.25"
pattern_title: "Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
section_id: "C.25:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.25/C.25__008_conformance-checklist.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "C.25 — Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
  - "C.25:7 — Conformance Checklist"
line_start: 45912
line_end: 45920
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

### C.25:7 - Conformance Checklist

- `CC-C.25-1` If an engineering quality claim is intended as one measurement characteristic, the publisher **SHALL** bind it to one named `U.Characteristic` with one declared scale.
- `CC-C.25-2` If the claim requires multiple measures, scope slots, mechanism slots, status slots, or qualification windows, the publisher **SHALL** use a Q-Bundle rather than an undeclared scalar surrogate.
- `CC-C.25-3` `ClaimScope` and `WorkScope` **SHALL** remain USM set-valued scope objects; they **MUST NOT** be treated as ordinal or numeric quality levels.
- `CC-C.25-4` Mechanism or status slots **MUST NOT** be conflated with `Measures[CHR]`.
- `CC-C.25-5` Any scalar comparison or thresholding inside a Q-Bundle **SHALL** apply only to declared CHR measures, not to scope slots.
- `CC-C.25-6` Cross-context penalties and bridge losses **SHALL** apply to `R` per `B.3` / `F.9`; they **MUST NOT** silently alter the type of the bundle's `F`, scope, or CHR type authority.

