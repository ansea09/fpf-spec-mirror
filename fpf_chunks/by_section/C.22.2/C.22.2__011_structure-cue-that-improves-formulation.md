---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard@Context"
section_id: "C.22.2:10"
section_title: "Structure Cue That Improves Formulation"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__011_structure-cue-that-improves-formulation.md"
commit_sha: "cb17c555f343780e31e5fea236a74adc69295736"
heading_path:
  - "C.22.2 — ProblemCard@Context"
  - "C.22.2:10 — Structure Cue That Improves Formulation"
line_start: 45611
line_end: 45632
dependencies:
  - "A.10"
  - "A.15"
  - "A.19"
  - "A.21"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.Q"
  - "C.18"
  - "C.19"
  - "C.2.P"
  - "C.22"
  - "C.22.1"
  - "C.24"
  - "C.25"
  - "C.27"
  - "C.28"
  - "C.29"
  - "E.10"
  - "E.16"
  - "E.17"
  - "E.17.ID.CR"
  - "E.18"
  - "E.18.1"
  - "E.2"
  - "E.9"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
  - "P2W-ready"
  - "Thin problem card"
  - "first-principles cue"
  - "freshness and unknown disposition"
  - "problem card"
  - "problem signal"
  - "problem-side record"
  - "safe-probe-needed"
  - "setContextRef"
  - "support posture"
  - "validation boundary"
---

### C.22.2:10 - Structure Cue That Improves Formulation

`C.29` carries mathematical-lens use for first-principles or mathematical structure cues used by `ProblemCard@Context`.

`firstPrinciplesCue` is a local cue label for a formulation-changing structure and a cue to apply `C.29`; it is not a local mathematical-lens kind or a substitute for a `C.29` lens-use result.

The problem card may ask whether a first-principles or mathematical structure helps find or improve the problem formulation, not only whether an already-mentioned mathematical expression helps the problem formulation. Useful cues include state space, graph, boundary, topology, symmetry, invariant, variational or constrained-optimization structure, probability or information structure, resource bound, obstruction, scale window, composition, or coarse-graining choice.

The practitioner move is:

> State the structure that improves the problem formulation, the preserved structure, the lost structure, the practical payoff, the problem-formulation next-move reason, and the stop condition.

Distribution by principles:

| Source-side cue | Current FPF pattern or relation | `C.22.2` use |
|---|---|---|
| Zero-principles and first-principles invariants, constraints, symmetry, composition, multi-scale description, variational structure, probability or information, and resource limits | `C.29`, with `A.19`, `C.16`, `C.25`, and `G.9` when characteristics, measurement characterization, quality bundles, or parity are current | Carry a first-principles or mathematical structure cue and apply the governing pattern for the claim being made, relation, or boundary. |
| Second-principles method-family implications | `G.5`, `A.15`, `E.18`, `A.19` as applicable | Name the method-family cue; do not perform method selection in the problem card. |
| Third-principles reproducibility, checks, templates, records, logs, rollback, evidence | `A.10`, `G.6`, `B.3`, `A.21`, `G.11`, `E.16` as applicable | Name the reproducibility or evidence cue and apply the governing pattern for the claim kind named by value before relying on that claim. |

When no useful mathematical structure survives, record that absence and proceed without forcing mathematical prose into the problem card.

