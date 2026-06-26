---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transformation Flow Structure"
section_id: "E.18:7.1"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "E.18 — Transformation Flow Structure"
  - "E.18:7.1 — Common Anti-Patterns and How to Avoid Them"
line_start: 75536
line_end: 75545
dependencies:
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.7"
  - "C.29"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.17"
  - "E.18.1"
  - "E.18.2"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "P2W support"
  - "composition"
  - "crossings"
  - "flow valuation"
  - "guards"
  - "selected transformations"
  - "transformation flow structure"
---

### E.18:7.1 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Graph expression as selected structure | A mathematical graph, morphism chain, or tool pipeline is treated as the `TransformationFlowStructure` itself. | Separate selected structure from mathematical description; use `E.18.2` and `C.29` when lens adequacy is live. |
| Flow as performed work | A valuation or path is treated as a work occurrence or work procedure. | Keep work planning and performed work with the A.15 family. |
| Gate everywhere | Internal step validity, crossing, launch, and gate-decision publication are collapsed. | Use `A.20` for internal constraint validity and `A.21` for gate fit, aggregation, decision, and publication. |
| Publication face as evidence | An MVPK face or dashboard view is treated as evidence, gate passage, release authorization, or deontic permission. | Use `E.17`, `A.10`, `A.21`, `A.2.8`, `A.2.9`, or release-governing patterns according to the claim being made. |
| Whole-flow refresh | Any small edition or source change triggers a whole-structure rewrite. | Refresh the smallest affected path slice, crossing, edition pin, or publication face. |

