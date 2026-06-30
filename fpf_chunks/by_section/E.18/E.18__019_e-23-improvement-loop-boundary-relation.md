---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transformation Flow Structure"
section_id: "E.18:15b"
section_title: "E.23 Improvement-Loop Boundary Relation"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__019_e-23-improvement-loop-boundary-relation.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "E.18 — Transformation Flow Structure"
  - "E.18:15b — E.23 Improvement-Loop Boundary Relation"
line_start: 76500
line_end: 76505
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

### E.18:15b - E.23 Improvement-Loop Boundary Relation

When a transformation-flow structure contains a cycle, budgeted retry path, monitor/escalate path, or slice-local refresh relation, `E.18` governs the selected structure: loci, transfer relation, path or slice, gate positions, pins, and refresh locality. The cycle becomes an `E.23` quality-improvement loop only when a named object version is changed and then re-evaluated by a declared object-under-improvement evaluation. Otherwise the cycle remains a transformation-flow structure, work-control cue, gate relation, or refresh relation governed by its direct owner.

Agent-loop diagrams often contain both kinds. A monitor/retry/escalate loop over physical execution state may be a valid `TransformationFlowStructure` and may include an `A.21` gate, but it does not prove that the controlled object improved. If the harness itself is improved, `E.23` governs that object-version improvement; if the harness only runs work, the A.15 family governs the work occurrence.

