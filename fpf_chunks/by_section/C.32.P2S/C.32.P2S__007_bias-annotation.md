---
chunk_kind: "child"
pattern_id: "C.32.P2S"
pattern_title: "Problem-to-Structure Architecturing Transformation Flow"
section_id: "C.32.P2S:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.P2S/C.32.P2S__007_bias-annotation.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "C.32.P2S — Problem-to-Structure Architecturing Transformation Flow"
  - "C.32.P2S:6 — Bias-Annotation"
line_start: 59486
line_end: 59497
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.3.4"
  - "B.2"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.2"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.HCS"
  - "C.32.MLAO"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.17"
  - "E.18"
  - "E.23"
  - "E.24.PUB"
  - "G.11"
  - "G.5"
keywords:
  - "ProblemToStructureArchitecturingFlowCard@Project"
  - "actual-structure feedback"
  - "architecture work flow"
  - "owner-specific return"
  - "problem-to-structure architecturing flow"
  - "selected structures"
  - "structural uncertainty"
---

### C.32.P2S:6 - Bias-Annotation

Use these rows as repair cues for source pressure, not as a catalogue of mistakes.

| Source pressure | Risk in P2S use | Repair |
|---|---|---|
| Description-first source | A view, model, diagram, ADR-like record, dashboard, or memo starts to carry architecture, decision, and work authority at once. | Recover selected structures and current use. Send description adequacy to `C.30.AD` or `C.30.ASV`, decision to `C.32.PAD`, projection to `C.32.ADR`, and work claims to A.15-family patterns. |
| Single-winner source | A score, workshop favorite, generated candidate, or apparent best alternative hides structurally different candidates. | Restore candidate plurality through `C.32`; keep archive, front, pool, selected-set, comparison, local-choice, or decision use with its owner. |
| Eval-shaped source | A metric, benchmark, source-side fitness-function term, eval result, or telemetry event is treated as the characteristic or the decision. | Recover characteristic, bearer, scale, eval program, measurement, and receiving use. Use `C.32.ACE`, `C.16`, `C.25`, and then the comparison, selected-set, local-choice, or decision owner. |
| Transformer-hidden source | Desired transformed-holon architecture is stated without asking whether the changing holon can produce it. | Open `C.32.CONWAY`; name changing relation, transformer, transformed holon, selected structures on both sides, affected characteristics, candidate changes, and bounded mismatch condition. |
| Work-shaped source | A schedule, task list, method recipe, or performed-work record is treated as the architecturing flow. | Keep work owners intact. P2S records method, readiness, work-plan, and performed-work refs only when they realize or evaluate selected structures. |

