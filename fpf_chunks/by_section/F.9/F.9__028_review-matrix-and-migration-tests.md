---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment & Bridge across Contexts"
section_id: "F.9:26"
section_title: "Review Matrix and Migration Tests"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__028_review-matrix-and-migration-tests.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "F.9 — Alignment & Bridge across Contexts"
  - "F.9:26 — Review Matrix and Migration Tests"
line_start: 71442
line_end: 71453
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

### F.9:26 - Review Matrix and Migration Tests

A reader can test bridge integrity with six questions:

1. **Are the two cells and contexts explicit?**
2. **Is the bridge kind the least-committing truthful kind rather than the friendliest one?**
3. **Does `CL` match the published counter-example or invariant evidence?**
4. **Are Loss Notes specific enough that the Bridge-supported use is really bounded?**
5. **If a row or bundle cites the bridge, does it stay within the Bridge-supported use?**
6. **If a stance overlay exists, does it stay within the bridge card's kind, direction, `CL`, and Loss Notes?**

Migration from legacy "same/equivalent/align/map" prose should therefore recover the Bridge Card first, then any row support, then any optional stance overlay. Doing it in the opposite order recreates silent equivalence under new vocabulary.
