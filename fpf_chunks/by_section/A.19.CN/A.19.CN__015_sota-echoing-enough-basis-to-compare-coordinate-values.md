---
chunk_kind: "child"
pattern_id: "A.19.CN"
pattern_title: "CN-frame: Specify and Maintain Comparability and Normalization"
section_id: "A.19.CN:14"
section_title: "SoTA-Echoing — enough basis to compare coordinate values"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CN/A.19.CN__015_sota-echoing-enough-basis-to-compare-coordinate-values.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "A.19.CN — CN-frame: Specify and Maintain Comparability and Normalization"
  - "A.19.CN:14 — SoTA-Echoing — enough basis to compare coordinate values"
line_start: 34042
line_end: 34053
dependencies:
  - "A.19"
  - "A.6.1"
  - "C.16"
  - "F.9"
  - "G.0"
keywords:
  - "CL/loss notes"
  - "CN-Spec"
  - "CN-frame"
  - "RSG admission hooks"
  - "SCR/RSCR harness"
  - "WLNK discipline"
  - "bridges"
  - "chart"
  - "comparability modes"
  - "conformance checklist"
  - "indicator policy refs"
  - "normalization refs"
  - "registry"
  - "Γ-fold governance"
---

### A.19.CN:14 - SoTA-Echoing — enough basis to compare coordinate values

**Practice question.** What must accompany two chart values before a practitioner treats them as comparable? The selected best-known line identifies the bearer/property, value-producing procedure or evaluation rule, relevant time and result basis alongside Scale/Unit meanings. A serious smaller alternative is to carry only the quantity kind, value and unit, converting units before comparison.

The [QUDT quantity model](https://www.qudt.org/pages/QUDToverviewPage.html) is the useful comparator: it separates Quantity, QuantityKind, QuantityValue and Unit and supports precise quantity descriptions. **Adopt** that discipline where a Unit applies. Using only that portion is cheaper and sufficient when the same property, procedure and observation basis are already fixed outside the record. **Reject** treating it alone as evidence that two independently obtained readings answer the same question; this is a limit of that reduced use, not a claim that QUDT forbids richer descriptions.

The [SOSA/SSN 2023-edition working draft of 24 September 2026](https://www.w3.org/TR/2026/WD-vocab-ssn-2023-20260924/) supplies the compared observation/procedure line: it distinguishes the feature, observed property, procedure, result and temporal qualifications. **Adapt** that separation in CN-Spec's bearer, cs_basis and chart, CC-A19.D1-1/-3/-11, and SCR-S01. The source is work in progress and does not establish FPF admission, Scale lawfulness, certification independence or a Bridge; those retain their direct rules. An evaluated coordinate keeps its actual rule and basis rather than acquiring a fictive measurement or Unit.

At comparable effort, both alternatives start from the same pair of readings and existing method records. The selected line adds the references that can change this comparison, reusing common frame-level values rather than repeating a full observation history for every cell. The SRE case in §8.2 shows the gain: equal millisecond units cannot make client end-to-end latency and server processing latency the same Characteristic. Keep them separate or obtain values for the same declared characteristic and observation basis. The added references cost more than a bare numeric pair; that cost is accepted when the basis is not already common and recoverable.

Reopen when a proposed comparison changes the property, value-producing rule, reference state or relevant window, or when a smaller representation demonstrably retains all the distinctions needed by that use. These sources support the compared representational choices; they do not validate every CN-frame or make its registry self-certifying.

