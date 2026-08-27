---
chunk_kind: "child"
pattern_id: "C.25"
pattern_title: "Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
section_id: "C.25:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.25/C.25__008_conformance-checklist.md"
commit_sha: "322625be006f38158e4e7d600f662558f03df77a"
heading_path:
  - "C.25 — Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
  - "C.25:7 — Conformance Checklist"
line_start: 52667
line_end: 52676
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

### C.25:7 - Conformance Checklist

- `CC-C.25-1` If an engineering quality claim is intended as one measurement characteristic, the publisher **SHALL** bind it to one named `U.Characteristic` with one declared scale.
- `CC-C.25-2` If the claim requires multiple measures, scope slots, mechanism slots, status slots, or qualification windows, the publisher **SHALL** use Q-Bundle-shaped ClaimGraph content rather than an undeclared scalar surrogate.
- `CC-C.25-3` `ClaimScope` and `WorkScope` **SHALL** remain USM set-valued scope objects; they **MUST NOT** be treated as ordinal or numeric quality levels.
- `CC-C.25-4` Mechanism or status slots **MUST NOT** be conflated with `Measures[CHR]`.
- `CC-C.25-5` Any scalar comparison or thresholding inside a Q-Bundle **SHALL** apply only to declared CHR measures, not to scope slots.
- `CC-C.25-6` When cross-context comparison is current, the publisher **SHALL** align the exact bundle heads or slots, resolve the two exact `F.17` local senses, test the direct `F.9` Bridge predicate, and state a separate bounded-use claim only if that Bridge obtains. The comparison and its reliance **MUST NOT** change any Q-Bundle slot; ordinary reliance uses `A.10`, while `B.3` opens only when an actual named assurance claim is current.
- `CC-C.25-7` A materialized Q-Bundle **SHALL** be recoverable as content of one exact `C.2.1` episteme with one independently identified QualityBearer as EntityOfConcern and one effective ReferenceScheme. A gate, publication, comparison, proxy, or roll-up **MUST NOT** cite a field list as though it were an independently identified bundle object.

