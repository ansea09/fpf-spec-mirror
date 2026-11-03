---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transformation Flow Structure"
section_id: "E.18:7.1"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "c1926cf444afeb1994d6b1fe791593dc248b3838"
heading_path:
  - "E.18 — Transformation Flow Structure"
  - "E.18:7.1 — Common Anti-Patterns and How to Avoid Them"
line_start: 110963
line_end: 110972
dependencies:
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.6.RCD"
  - "A.7"
  - "C.29"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.17"
  - "E.18.1"
  - "E.18.2"
  - "E.18.NET"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.18:7.1 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Graph expression as selected structure | A mathematical graph, morphism chain, or tool pipeline is treated as the `TransformationFlowStructure` itself. | Separate selected structure from mathematical description; use `E.18.2` and `C.29` when lens adequacy is live. |
| Flow as performed work | A valuation or path is treated as a work occurrence or work procedure. | Keep work planning and performed work with the A.15 family. |
| Gate everywhere | Internal step validity, crossing, launch, and gate-decision publication are collapsed. | Use `A.20` for internal constraint validity, `A.21` for gate fit, aggregation, and decision, and `E.17` for publication. |
| Publication face as evidence | An MVPK face or dashboard view is treated as evidence, gate passage, release authorization, or deontic permission. | Use `E.17` for publication, `A.10` for evidence/currentness, `A.21` for gate effects, `A.2.9` for an issuing act, `A.2.8.PER` for strong/weak permission, exercise, non-violation, or conflict, `A.2.8` only for an actual duty/recommendation/prohibition commitment, and the actual release authority for release. |
| Whole-flow refresh | Any small edition or source-use change triggers a whole-structure rewrite, or the first detected slice is treated as the whole dependency scope. | Follow 5.13 through every actual dependent branch, join and consuming face; address the needed slices and preserve independent uses. |

