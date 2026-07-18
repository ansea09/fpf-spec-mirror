---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:23"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__024_rationale.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:23 — Rationale"
line_start: 87038
line_end: 87046
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

### F.9:23 - Rationale

The core move of F.9 is simple: cross-context work is unavoidable, but silent sameness is unacceptable. A Bridge therefore does two jobs at once:

* it preserves practical comparison and bounded reuse where the relation is genuinely available,
* it keeps non-identity visible through direction, Loss Notes, `CL`, and weakest-link use.

Without that discipline, every shared label becomes a hidden ontology merger. With it, cross-context comparison stays teachable, auditable, and compatible with direct governing patterns.

