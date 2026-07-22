---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:28"
section_title: "Review matrix"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__029_review-matrix.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:28 — Review matrix"
line_start: 89505
line_end: 89518
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

### F.9:28 - Review matrix

A reader can test bridge integrity with seven questions:

1. Are the two cells and contexts explicit?
2. Is the bridge kind the least-committing truthful kind rather than the friendliest one?
3. Does `CL` match the published counter-example or invariant evidence?
4. Are Loss Notes specific enough that the admitted use is really bounded?
5. If a row or bundle cites the Bridge, does it stay within the Bridge's admitted use?
6. If a stance overlay exists, does it stay within the Bridge Card's kind, direction, `CL`, Loss Notes, and admitted use?
7. If a role, status, evidence, source, publication, assurance, gate, decision, method, work, or mathematical-lens claim appears, has the direct governing pattern been opened instead of letting F.9 carry that claim?

Repair from same, equivalent, align, and map prose should therefore recover the Bridge Card first, then any row use, then any optional stance overlay. Doing it in the opposite order recreates silent equivalence under new vocabulary.

