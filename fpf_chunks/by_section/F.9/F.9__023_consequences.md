---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment & Bridge across Contexts"
section_id: "F.9:21"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__023_consequences.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "F.9 — Alignment & Bridge across Contexts"
  - "F.9:21 — Consequences"
line_start: 71378
line_end: 71385
dependencies:
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.9"
  - "B.3"
  - "C.16.Q"
  - "C.25"
  - "C.26"
  - "C.26.1"
  - "E.10.D1"
  - "E.17.1"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.7"
  - "F.8"
  - "F.9.1"
  - "U.BoundedContext"
  - "U.Mechanism"
keywords:
  - "Bridge-supported use"
  - "CL"
  - "bridge"
  - "bridge reading"
  - "cross-context alignment"
  - "direction"
  - "loss notes"
  - "state export"
  - "weakest-link scope"
---

### F.9:21 - Consequences

**Benefits.**
F.9 lets FPF compare, translate, and partially reuse ideas across Contexts without collapsing them into one vocabulary. It gives downstream rows, claims, and assurance reasoning an explicit Bridge Card record instead of relying on prose intuition.

**Trade-offs / mitigations.**
The pattern adds explicit bridge declaration and may feel heavier than informal comparison. Mitigation: use Naming-only scope when explanation is enough, and reserve higher-scope uses for Bridges that carry the required `CL` and invariants.

