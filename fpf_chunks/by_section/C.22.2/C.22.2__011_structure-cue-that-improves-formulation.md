---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard"
section_id: "C.22.2:10"
section_title: "Structure Cue That Improves Formulation"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__011_structure-cue-that-improves-formulation.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "C.22.2 — ProblemCard"
  - "C.22.2:10 — Structure Cue That Improves Formulation"
line_start: 62972
line_end: 62993
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.5"
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
  - "C.2.1"
  - "C.2.P"
  - "C.22"
  - "C.22.1"
  - "C.22.PFR"
  - "C.24"
  - "C.25"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.32.P2S"
  - "E.10"
  - "E.10.MOVE"
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
---

### C.22.2:10 - Structure Cue That Improves Formulation

Use an adequate domain equation, model or calculation directly when it answers the formulation question. Enter `C.29` when choosing or transferring a representation could supply a missing inference, or when reliance on a representation exceeds its supported correspondence.

`firstPrinciplesCue` is a local label for a structure that may change the formulation. It is neither a mathematical-lens kind nor a requirement to produce a C.29 record.

The problem card may ask whether a first-principles or mathematical structure helps find or improve the problem formulation, not only whether an already-mentioned mathematical expression helps the problem formulation. Useful cues include state space, graph, boundary, topology, symmetry, invariant, variational or constrained-optimization structure, probability or information structure, resource bound, obstruction, scale window, composition, or coarse-graining choice.

The practitioner-facing use is:

> Identify the structure, obtain its relevant consequence, and say how that consequence changes the formulation. When the inference relies on a representation or transfer, explain the correspondence, assumptions and omitted distinctions that bound its use.

Distribution by principles:

| Source-side cue | Current FPF pattern or relation | `C.22.2` use |
|---|---|---|
| Zero-principles and first-principles invariants, constraints, symmetry, composition, multi-scale description, variational structure, probability or information, and resource limits | `C.29`, with `A.19`, `C.16`, `C.25`, and `G.9` when characteristics, measurement characterization, quality bundles, or parity are current | Carry a first-principles or mathematical structure cue and apply the subject pattern for the claim being made, relation, or boundary. |
| Second-principles method-family implications | `G.5`, `A.15`, `E.18`, `A.19` as applicable | Name the method-family cue; do not perform method selection in the problem card. |
| Third-principles reproducibility, checks, templates, records, logs, rollback, evidence | `A.10`, `G.6`, `B.3`, `A.21`, `G.11`, `E.16` as applicable | Name the reproducibility or evidence cue and apply the subject pattern for the claim kind named by value before relying on that claim. |

When no useful mathematical construction is needed, proceed with the ordinary formulation. Keep an unresolved candidate cue only when it can guide the next observation or construction.

