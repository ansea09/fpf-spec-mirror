---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transformation Flow Structure"
section_id: "E.18:15b"
section_title: "E.23 Improvement-Loop Boundary Relation"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__019_e-23-improvement-loop-boundary-relation.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "E.18 — Transformation Flow Structure"
  - "E.18:15b — E.23 Improvement-Loop Boundary Relation"
line_start: 86129
line_end: 86134
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

### E.18:15b - E.23 Improvement-Loop Boundary Relation

When a transformation-flow structure contains a cycle, budgeted retry path, monitor/escalate path, or slice-local refresh relation, `E.18` defines the selected structure: loci, transfer relation, path or slice, gate positions, pins, and refresh locality. The cycle becomes an `E.23` quality-improvement loop only when a named object version is changed and then re-evaluated by a declared object-under-improvement evaluation. Otherwise it remains a transformation-flow structure, work-control cue, gate relation, or refresh relation; apply the pattern whose Solution answers that exact claim.

Agent-loop diagrams often contain both kinds. A monitor/retry/escalate loop over physical execution state may be a valid `TransformationFlowStructure` and may include an `A.21` gate, but it does not prove that the controlled object improved. If the harness itself is improved, use the E.23 object-version improvement definition and test; if the harness only runs work, use the A.15 family to identify and test the work occurrence.

