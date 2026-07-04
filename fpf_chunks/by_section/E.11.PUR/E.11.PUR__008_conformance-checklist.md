---
chunk_kind: "child"
pattern_id: "E.11.PUR"
pattern_title: "Pattern-Use Recommendation and Pattern-Use Sequence"
section_id: "E.11.PUR:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PUR/E.11.PUR__008_conformance-checklist.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "E.11.PUR — Pattern-Use Recommendation and Pattern-Use Sequence"
  - "E.11.PUR:7 — Conformance Checklist"
line_start: 70984
line_end: 70998
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.3"
  - "A.15.5"
  - "A.16"
  - "A.21"
  - "C.24"
  - "C.30"
  - "C.30.AD"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.MOVE"
  - "E.11"
  - "E.17"
  - "E.18.1"
  - "E.24"
  - "E.8"
keywords:
---

### E.11.PUR:7 - Conformance Checklist

| ID | A conforming use... | Check |
| --- | --- | --- |
| `CC-E11PUR-1` | names the project concern before recommending a pattern use. | The concern is not replaced by a pattern id alone. |
| `CC-E11PUR-2` | separates applicability from recommendation. | `ApplicabilityFinding` and `RecommendedPatternUse` are both recoverable when both claims are made. |
| `CC-E11PUR-3` | blocks stronger uses. | Work, plan, gate, decision, source, publication, architecture, and transformation overreads are named only when their governing pattern is current. |
| `CC-E11PUR-4` | preserves the remaining reader use. | The result says what the practitioner can inspect, write, decide, or apply next. |
| `CC-E11PUR-5` | uses `PatternUseSequence@Context` only for pattern-use relations. | The sequence is not a work plan, workflow, lifecycle, or performed work. |
| `CC-E11PUR-6` | keeps didactic move language plain. | "First useful move" can remain in teaching prose, but durable FPF text names the recovered relation. |

#### E.11.PUR:7.1 - Lowering and Reopen Conditions

Lower, reject, or reopen the recommendation when the project concern changes, a candidate pattern becomes inapplicable, the expected output shape no longer answers the concern, a stronger neighboring claim becomes current, a proxy pattern id is being optimized instead of practical gain, or the first applied result shows that the recommended pattern use did not produce the promised inspection, decision input, or work-preparation value.

