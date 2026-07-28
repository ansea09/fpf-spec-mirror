---
chunk_kind: "child"
pattern_id: "C.3.1"
pattern_title: "U.Kind and U.SubkindOf Core"
section_id: "C.3.1:7"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.1/C.3.1__009_archetypal-grounding.md"
commit_sha: "17edd955485f60cafb16159c7d90e20f4ad21844"
heading_path:
  - "C.3.1 — U.Kind and U.SubkindOf Core"
  - "C.3.1:7 — Archetypal Grounding"
line_start: 44516
line_end: 44528
dependencies:
  - "A.1"
  - "A.11"
  - "A.2.6"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "A.8"
  - "C.2.1"
  - "C.2.3"
  - "C.29"
  - "C.3"
  - "C.3.2"
  - "C.3.3"
  - "E.24.UK"
  - "F.5"
  - "F.8"
keywords:
  - "U.SubkindOf direct relation"
  - "assertion episteme"
  - "local kind"
  - "partial order"
  - "relation occurrence"
  - "relation-obtaining predicate"
---

### C.3.1:7 - Archetypal Grounding

| Situation | C.3.1 move | Boundary |
| --- | --- | --- |
| `CoolingPumpKind` is below `PumpKind`. | State that the direct `U.SubkindOf` relation obtains for the two kinds under the named reference scheme; create a C.2.1 assertion episteme only when that assertion is separately needed. | Test the aligned candidate/slice judgments; do not infer a durable `U.CoolingPump` or treat an edge as the occurrence. |
| A signature edition adds a clarified unit conversion but preserves the declared cooling-pump identity. | Keep the kind, identify the new signature edition, and retain edition-specific judgments. | Do not rewrite earlier judgments as if the new edition had been used. |
| A signature changes from physical cooling performance to a schema label. | Treat the declaration as changed and reject automatic kind continuity unless an explicit local identity case survives. | Do not hide the mismatch by editing the extension. |
| Pump #14 changes state in a later plant slice. | Re-evaluate the candidate and allow the represented extension to change. | Candidate-state change alone does not create a new kind or signature. |
| `InspectionWorkKind` is used locally. | Classify only an independently identified `W : U.Work`. | `U.Work`, a work plan, or a log row cannot occupy W's candidate position. |
| `WorkPlan` depends on Work. | Use the governing work or E.24.UK relation. | Do not encode dependency as `U.SubkindOf` unless a real kind partial order is being claimed. |
| Safety-critical function is a kind of function. | Use a local `U.Kind` and subkind order for the current typed claim. | Intent and candidate judgment go to C.3.2; public FPF naming follows governed U-kind admission. |
| A project proposes public `U.CoolingPump`. | Take the recovered local kind to `E.24.UK`, then use `A.11`, `A.8`, and the applicable Part F naming pattern as needed. | Local `U.SubkindOf` does not admit or publish the durable kind. |

