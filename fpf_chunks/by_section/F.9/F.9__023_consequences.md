---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:22"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__023_consequences.md"
commit_sha: "646b0b9b164f7c13258633a33b92d2d0a569da28"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:22 — Consequences"
line_start: 74995
line_end: 75002
dependencies:
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.6.3.CSC"
  - "A.6.5"
  - "A.6.9"
  - "B.3"
  - "C.26"
  - "C.26.1"
  - "C.26.2"
  - "C.29"
  - "E.10.D1"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9.1"
  - "U.BoundedContext"
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

### F.9:22 - Consequences

**Benefits.** F.9 lets FPF compare, translate, and partially reuse ideas across contexts without collapsing them into one vocabulary. It gives downstream rows, claims, and assurance reasoning an explicit Bridge Card instead of relying on prose similarity.

**Costs.** The pattern adds explicit bridge declaration and can feel heavier than informal comparison. Mitigation: use Naming-only or Explanation-only when that is enough, and reserve higher-scope uses for Bridges that carry the required `CL`, invariants, and direct-pattern boundaries.

**Failure mode avoided.** A Bridge can no longer be used as a quiet substitute for role assignment, status transfer, evidence authority, publication authority, or performed-work attribution.

