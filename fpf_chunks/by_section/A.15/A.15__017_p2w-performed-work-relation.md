---
chunk_kind: "child"
pattern_id: "A.15"
pattern_title: "System-Role–Method–Work Alignment"
section_id: "A.15:12d"
section_title: "P2W Performed-Work Relation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15/A.15__017_p2w-performed-work-relation.md"
commit_sha: "322625be006f38158e4e7d600f662558f03df77a"
heading_path:
  - "A.15 — System-Role–Method–Work Alignment"
  - "A.15:12d — P2W Performed-Work Relation"
line_start: 24274
line_end: 24279
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.15.3"
  - "A.15.4"
  - "A.15.5"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.20"
  - "A.21"
  - "A.3"
  - "A.6"
  - "A.6.5"
  - "A.7"
  - "B.3"
  - "C.28"
  - "C.29"
  - "C.3"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.ROLE"
  - "E.17.EFP"
  - "E.18.1"
  - "F.6"
  - "U.SystemRoleAssignment"
keywords:
  - "Method"
  - "MethodDescription"
  - "WorkPlan"
  - "assignment"
  - "attribution"
  - "dated Work"
  - "readiness"
  - "result boundary"
  - "system-role kind"
---

### A.15:12d - P2W Performed-Work Relation

When E.18.1 reaches performed Work, keep `U.Work` as the admitted kind and identify one exact dated occurrence under it. `WorkEnactment` is not a second kind or pseudo-object between plan and occurrence.

A performed-work record is a separate `U.Episteme`. It may cite a WorkPlan, planned baseline, and exact Work occurrence. It can state bindings, performed values, substitutions, variance, telemetry, outputs, outcome claims, and result references only through independently obtaining relations; none is stored in or constituted by the Work occurrence. Comparator, transport, `PrincipleFrame`, formal-substrate signature, evidence, assurance, and gate relations remain separate.

