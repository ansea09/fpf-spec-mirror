---
chunk_kind: "child"
pattern_id: "A.6.1"
pattern_title: "U.Mechanism - Law-governed application to a SubjectKind over a RangedValueKind"
section_id: "A.6.1:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.1/A.6.1__010_consequences.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "A.6.1 — U.Mechanism - Law-governed application to a SubjectKind over a RangedValueKind"
  - "A.6.1:9 — Consequences"
line_start: 10623
line_end: 10641
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

### A.6.1:9 - Consequences

| Benefit | Cost or caution |
| --- | --- |
| Mechanism families share one kernel declaration shape. | Teams must name slots, laws, guards, and transport policy explicitly. |
| Reuse becomes auditable across contexts and planes. | Bridge and Reliability penalty relations cannot be skipped for convenience. |
| Realizations can vary without relaxing laws. | Implementations must be checked against signature and imported-law opacity. |
| Method, mechanism, work, evidence, and gate claims stay separated. | Source labels often need `E.10.ARCH` recovery before typed assignment. |
| Comparison and normalization mechanisms stop hiding scale-incompatible arithmetic. | Some familiar single-score practices become inadmissible until a scorer is declared. |

#### A.6.1:9.1 - Quick use cards

* **Mechanism = operation algebra plus laws.** Add guards, transport, time, plane, audit, and realization discipline.
* **Method is not mechanism.** A method can use or fill a mechanism slot; it does not become the mechanism by name.
* **Guards fail closed.** Unknown guard results become `degrade` or `abstain`.
* **Transport is Bridge-only.** Crossings need Bridge, ReferencePlane, and Reliability penalty relation.
* **SlotKinds travel.** Positional parameters do not replace SlotSpecs.
* **Realizations tighten.** A realization may specialize but not relax mechanism laws.

