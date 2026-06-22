---
chunk_kind: "child"
pattern_id: "A.6.1"
pattern_title: "U.Mechanism - Law-governed application to a SubjectKind over a RangedValueKind"
section_id: "A.6.1:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.1/A.6.1__006_archetypal-grounding.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "A.6.1 — U.Mechanism - Law-governed application to a SubjectKind over a RangedValueKind"
  - "A.6.1:5 — Archetypal Grounding"
line_start: 10543
line_end: 10560
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.19"
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.3.1"
  - "A.3.2"
  - "A.6.0"
  - "B.3"
  - "C.16"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.D1"
  - "E.18"
  - "E.20"
  - "F.18"
  - "U.BoundedContext"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Signature"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "AdmissibilityConditions"
  - "Bridge‑only"
  - "LawSet"
  - "Mechanism"
  - "OperationAlgebra"
  - "Transport"
---

### A.6.1:5 - Archetypal Grounding

#### A.6.1:5.1 - Selector mechanism

A team needs to select one method from candidate methods. The selection method can be `U.Method`; the selector mechanism declares operations over candidate sets, criteria, comparison results, context, and selected value. It states admissibility predicates for candidate completeness, comparison availability, and time window. The selected method remains a method value; the selector mechanism is not the selected method.

#### A.6.1:5.2 - Scope mechanism

A project uses context slices to decide where a claim applies. USM declares the slice set, operations, laws, admissibility predicates, bridge policy, and time policy. A source statement such as "scope covers target slice" is admissible only if the guard predicate can be evaluated in the bounded context.

#### A.6.1:5.3 - Normalization mechanism

A benchmark group normalizes scores before comparing systems. UNM declares admissible normalization methods, equivalence, transforms by scale type, and comparison-compliance conditions. Ordinal averaging is rejected because the mechanism cannot make scale-incompatible arithmetic admissible.

#### A.6.1:5.4 - Publication mechanism

A publication mechanism emits selector-ready packs, refresh cues, and crossing records. The mechanism declares operations and admissibility predicates; actual publication work, telemetry, evidence, and gate decisions stay with their governing patterns.

