---
chunk_kind: "child"
pattern_id: "C.2"
pattern_title: "Epistemic holon composition (KD-CAL)"
section_id: "C.2:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2/C.2__008_conformance-checklist.md"
commit_sha: "870fb0c2a5dcfe1e0165a111fdf2cf8659c85a54"
heading_path:
  - "C.2 — Epistemic holon composition (KD-CAL)"
  - "C.2:7 — Conformance Checklist"
line_start: 51023
line_end: 51030
dependencies:
  - "A.1"
  - "A.10"
  - "A.6.3.RT"
  - "A.6.3.RT.OE"
  - "B.3"
  - "C.2.1"
  - "C.29"
  - "E.17"
  - "E.17.0"
  - "E.24.PUB"
  - "U.Episteme"
  - "U.View"
keywords:
  - "ClaimScope"
  - "Congruence Level"
  - "F-G-R"
  - "Formality"
  - "KD-CAL"
  - "Reliability"
  - "assurance"
  - "epistemic holon composition"
  - "evidence"
  - "knowledge"
  - "provenance"
  - "trust"
---

### C.2:7 - Conformance Checklist

1. **C2-1 (Episteme constitution and neighbors).** Every `U.Episteme` **MUST** satisfy C.2.1 constitution through exact claim content, one exact EntityOfConcern, and one effective reference scheme. Empirical grounding and edition are stated through their separate C.2.1 relations. Viewpoint selection and `U.View` conformance use E.17.0; expression construction and scheme changes use A.6.3.RT.OE/A.6.3.RT, with C.29 for an unresolved question about choosing, transferring, or relying on a mathematical representation; publication occurrence, form, and carrier use E.17/E.24.PUB. None is treated as an episteme slot or identity component merely because a record or notation places it beside the constitution values.
2. **C2-2 (Assessment meaning).** When a KD-CAL F–G–R assessment is stated or used, `[F,G,R]` **SHALL** be recoverable for one exact claim and use, with a brief rationale. Identifying or publishing an episteme does not by itself require this tuple. F names the relevant expression-property assessment under C.2.3; a local rank requires its declared scale and mapping and is not a global F value. Where R has no justified numerical model, retain its unquantified support and bounded conclusion. Formal validity needs no empirical score. CL is declared for **pairs only**.
3. **C2‑3 (Composition).** Authors **SHALL** identify support roles and dependencies under B.1.3/C.2.2 before combining inputs. Any numerical R or loss **MUST** have justified meanings, scales, assumptions, and a receiving model under B.3; no universal min/max or F-to-R conversion applies. Otherwise return separate support and a bounded synthesis. F requires the properties of the essential constituents and their connections to support the claimed whole under C.2.3; G uses applicable path intersections and supported SpanUnion under A.2.6. For reuse that depends on a changed value or mapping, the actual operation or relation and its warranted limitations **MUST** remain recoverable; do not hide contrary evidence or unsupported scope.
4. **C2‑4 (Cross-notation use).** Cross-notation reasoning **MUST** recover the source and target expressions, their correspondence, and the preservation needed by the inference. A `NotationBridge` edge may record these relations and their limitations. State CL where the receiving rule uses it, including the KD-CAL substitution constraint in §4.1.
5. **C2‑5 (Work performer).** The performer of `U.Work` **MUST** be a System. Keep any guiding episteme distinct from that performer.

