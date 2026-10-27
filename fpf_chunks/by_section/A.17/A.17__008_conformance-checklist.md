---
chunk_kind: "child"
pattern_id: "A.17"
pattern_title: "Canonical “Characteristic” (A.CHR-NORM): Name What Is Measured"
section_id: "A.17:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.17/A.17__008_conformance-checklist.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "A.17 — Canonical “Characteristic” (A.CHR-NORM): Name What Is Measured"
  - "A.17:7 — Conformance Checklist"
line_start: 34217
line_end: 34236
dependencies:
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.2.3"
  - "A.3.3"
  - "A.7"
  - "B.3"
  - "C.16"
  - "C.2"
  - "D.3"
  - "E.10"
  - "F.7"
  - "F.9"
keywords:
  - "attribute"
  - "axis"
  - "characteristic"
  - "dimension"
  - "measurement"
  - "preference"
  - "property"
  - "quantity calculation"
  - "scale order"
  - "scoring"
---

### A.17:7 - Conformance Checklist

When authoring or reviewing FPF-compliant measurements, check the following:

1.  **Declared Characteristic:** Have you explicitly named a **Characteristic** for each aspect being measured, instead of using generic terms? (e.g. use _“Reliability”_ as a Characteristic name rather than saying “this dimension”).

2.  **Arity Explicit:** Is it clear whether the Characteristic is unary or relational? If a metric involves a relationship, are the participating entities (pair, tuple, etc.) identified in its definition?

3.  **Separate Scale/Unit:** For each Characteristic, have you defined the **Scale** (and **Unit**, if applicable) separately, rather than embedding units or ordinal terms in the name of the Characteristic? (e.g. _“Length (m)”_ should be captured as Characteristic = _Length_, Unit = _meter_).

4.  **Scale-appropriate operations:** Are you only performing comparisons or calculations that make sense for the declared scale type? (An ordinal encoding alone licenses no arithmetic mean; interval/ratio calculations retain their transformation and unit conditions.)

5. **Calculation or scoring:** Does a quantity calculation use a stated relation with compatible quantities and Scale operations? If values are combined into an overall Score, does the ScoringMethod state the preference it represents and preserve the declared preference in its score order?

6. **Canonical terminology in use:** Do formal descriptions distinguish Characteristic, Scale, Level/Value, Coordinate, Score, ScoringMethod and Unit, with any Plain alias explicitly mapped? Keep disciplinary terms that name different defined subjects instead of mechanically renaming them Characteristic.

7. **State use:** When Characteristics describe modeled change, are their admitted combinations and the transition law sufficient for the question under A.3.3? If a state condition is being recognized, is its predicate and required support determined by that receiving use?

Lexical checks can locate inconsistent terms; deciding the measured aspect, admissible operation and applicability requires the corresponding semantic rules.

