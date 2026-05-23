---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment & Bridge across Contexts"
section_id: "F.9:22"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__024_rationale.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "F.9 — Alignment & Bridge across Contexts"
  - "F.9:22 — Rationale"
line_start: 64629
line_end: 64637
dependencies:
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.9"
  - "A.6.Q"
  - "B.3"
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

### F.9:22 - Rationale

The core move of F.9 is simple: cross-context work is unavoidable, but silent sameness is unacceptable. A Bridge therefore does two jobs at once:

* it preserves practical reuse where bounded transport is genuinely available, and
* it keeps non-identity visible through direction, Loss Notes, `CL`, and weakest-link scope.

Without that discipline, every shared label becomes a hidden ontology merger. With it, cross-context comparison stays teachable, auditable, and compatible with the rest of FPF.

