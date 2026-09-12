---
chunk_kind: "child"
pattern_id: "C.2"
pattern_title: "Epistemic holon composition (KD-CAL)"
section_id: "C.2:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2/C.2__008_conformance-checklist.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "C.2 — Epistemic holon composition (KD-CAL)"
  - "C.2:7 — Conformance Checklist"
line_start: 42860
line_end: 42867
dependencies:
  - "A.1"
  - "A.10"
  - "A.6.3.RT"
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
  - "F-G-R"
  - "Formality"
  - "Reliability"
  - "assurance"
  - "epistemic"
  - "evidence"
  - "knowledge"
  - "provenance"
  - "trust"
---

### C.2:7 - Conformance Checklist

1. **C2-1 (Episteme constitution and neighbors).** Every `U.Episteme` **MUST** satisfy C.2.1 constitution through exact claim content, one exact EntityOfConcern, and one effective `U.ReferenceScheme`. Empirical grounding and edition are stated through their separate C.2.1 relations. Viewpoint selection and `U.View` conformance use E.17.0; representation uses C.29/A.6.3.RT; publication occurrence, form, and carrier use E.17/E.24.PUB. None is treated as an episteme slot or identity component merely because a record or notation places it beside the constitution values.
2. **C2‑2 (Coordinates).** Each episteme **SHALL** declare `[F,G,R]` for its exact claim and use with a brief rationale; where R has no justified numerical model, retain its unquantified support and bounded conclusion. Formal validity needs no empirical score; **F** is `U.Formality ∈ {F0…F9}` per **C.2.3**, **exactly one episteme‑level F** computed as the **min over essential parts**. CL is declared for **pairs only**. A named notation scheme **MAY** use sub‑anchors (e.g., `F4[OCL]`, `F7[HOL]`), which **MUST** preserve the global order and **map to their parent anchor** from C.2.3.
3. **C2‑3 (Composition).** Authors **SHALL** identify support roles and dependencies under B.1.3/C.2.2 before combining inputs. Any numerical R or loss **MUST** have justified meanings, scales, assumptions, and a receiving model under B.3; no universal min/max or F-to-R conversion applies. Otherwise return separate support and a bounded synthesis. F uses the minimum over essential formal constituents; G uses applicable path intersections and supported SpanUnion under A.2.6. Every reuse **MUST** name the actual direct relation and retain its warranted limitation; do not hide contrary evidence or unsupported scope.
4. **C2‑4 (NotationBridge).** Multi‑notation representation components **SHOULD** register `NotationBridge` edges with CL and loss note; any cross‑notation reasoning **MUST** cite the bridge’s CL.
5. **C2‑5 (No action).** Epistemes **MUST NOT** be assigned actions; work is executed by systems in role.

