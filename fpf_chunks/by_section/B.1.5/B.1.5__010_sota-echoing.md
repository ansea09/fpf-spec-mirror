---
chunk_kind: "child"
pattern_id: "B.1.5"
pattern_title: "Gamma_method - Order-Sensitive Method Composition and Work Enactment"
section_id: "B.1.5:8"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5/B.1.5__010_sota-echoing.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "B.1.5 — Gamma_method - Order-Sensitive Method Composition and Work Enactment"
  - "B.1.5:8 — SoTA-Echoing"
line_start: 36026
line_end: 36034
dependencies:
  - "A.1"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.3.1"
  - "A.3.2"
  - "A.6.0"
  - "A.6.1"
  - "B.1"
  - "B.1.4"
  - "B.1.6"
  - "B.2"
  - "B.3"
  - "B.3.5"
  - "C.13"
  - "C.29"
  - "E.10"
  - "E.20"
  - "G.5"
  - "U.Method"
  - "U.MethodDescription"
keywords:
  - "MIC"
  - "assurance hooks"
  - "capability continuity"
  - "method composition"
  - "method relation structure"
  - "method/work granularity"
  - "order-sensitive method"
  - "submethod"
  - "typed join"
  - "work enactment"
---

### B.1.5:8 - SoTA-Echoing

| Source line | Selected source examples already carried by neighbouring hosts | What FPF takes | What FPF does not take |
| --- | --- | --- | --- |
| Current workflow, case, decision, process-mining, and object-centric event-log practice separates process models from event logs and resource records. | `A.15` carries BPMN, CMMN, DMN, DDD, service-design, and ITIL source use; `A.15.1` carries dated work-occurrence identity. | B.1.5 keeps method, method description, work plan, dated work, event trace, and resource aggregation separate while still allowing evidence return from work occurrence to method admission. | A workflow notation, event log, or trace is not the composite method. |
| Typed functional, effect, protocol, and workflow-composition practice treats composition as constrained by interfaces, preconditions, postconditions, handlers, and admissible order. | `A.3.1` and `A.3.2` carry method versus method-description separation, constructor-theory or process-theory source-material use, scoped-effect analogy, and return discipline for method-description references. | B.1.5 requires typed joins, adapters, exposed or encapsulated interactions, preconditions, outputs, and failure conditions before admitting a composite method. | A type signature, process-theory description, or source-material description alone does not ground dated work occurrence. |
| Systems and software architecture practice uses interface exposure and encapsulation to make composed behavior reliable and substitutable. | `A.15.2` carries plan versus occurrence discipline; `A.15` carries role-assignment and method-enactment alignment. | B.1.5 makes method-interface exposure part of method identity when outside work, planning, substitution, or assurance relies on it. | Publication layout or diagram position does not decide whether an interaction is exposed, forwarded, or encapsulated. |
| FPF holon and whole-reidentification patterns require parts, whole-forming relations, whole-level commitments, and higher-level participation. | `A.1`, `B.2`, `A.14`, `C.13`, and `B.3.5` provide neighbouring holon, whole-reidentification, and structural-parthood tests. | Composite method admission is a method-holon grounding question with method-side whole-forming relations, not a structural-component parthood shortcut. | Method-composition order is not automatically A.14 component parthood. |

