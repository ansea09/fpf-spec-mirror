---
chunk_kind: "child"
pattern_id: "A.15"
pattern_title: "Role–Method–Work Alignment"
section_id: "A.15:12d"
section_title: "P2W Performed-Work Relation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15/A.15__017_p2w-performed-work-relation.md"
commit_sha: "1f413fcd23f4ea26956a45d67dde57bb233f6ad9"
heading_path:
  - "A.15 — Role–Method–Work Alignment"
  - "A.15:12d — P2W Performed-Work Relation"
line_start: 24322
line_end: 24327
dependencies:
  - "A.10"
  - "A.12"
  - "A.15"
  - "A.15.1-A.15.5"
  - "A.15.4"
  - "A.15.5"
  - "A.2"
  - "A.20"
  - "A.21"
  - "A.4"
  - "A.6"
  - "A.6.B"
  - "A.6.C"
  - "B.3"
  - "C.24"
  - "C.26.2"
  - "C.28"
  - "C.29"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ARCH"
  - "E.16"
  - "E.17"
  - "E.17.EFP"
  - "E.18.1"
keywords:
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.WorkPlan"
  - "actual U.Work"
  - "appearance-based reliance boundary"
  - "contextual enactment"
  - "coordinated-work evidence"
  - "role-method-work distinction"
  - "work admission display"
  - "work-entry readiness"
---

### A.15:12d - P2W Performed-Work Relation

When `E.18.1` reaches performed work, this family keeps `U.Work` as the admitted kind and identifies one exact dated Work occurrence under it. `WorkEnactment` is not a second kind and should not be used as a pseudo-object between a plan and the occurrence.

A performed-work record is a separate `U.Episteme` that may cite a `U.WorkPlan`, planned baseline, and the exact Work occurrence. It may state actual launch bindings, performed values, substitutions, variance, telemetry, outputs, outcome claims, and result-record references only by citing their independently obtaining relations; none is stored in or constituted by the Work occurrence. Comparator, transport, `PrincipleFrame`, `U.Signature(profile=FormalSubstrate)`, evidence, assurance, and gate relations remain separately governed.

