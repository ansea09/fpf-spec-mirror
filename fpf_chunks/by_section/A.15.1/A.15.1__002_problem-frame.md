---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__002_problem-frame.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:1 — Problem Frame"
line_start: 24270
line_end: 24275
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.15.5"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.6"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "B.1.4"
  - "B.1.6"
  - "B.3"
  - "C.2.1"
  - "C.27.TA"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "U.Capability"
  - "U.Method"
  - "U.MethodDescription"
  - "U.ReferenceScheme"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.System"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "U.Work admitted kind"
  - "actual binding"
  - "affected referent"
  - "enactsMethod"
  - "episode"
  - "no automatic transformation"
  - "occurrence assertion and record separation"
  - "overlap"
  - "performed resource-use fact"
  - "performedBy"
  - "retry"
  - "work continuity"
  - "work part"
  - "world-side dated occurrence"
---

### A.15.1:1 - Problem Frame

After we have separated **who is assigned** (via `U.RoleAssignment`), **what capability is being relied on** (via `U.Capability`), **how in principle** the work is done (the exact `U.Method`), and which claim-bearing episteme describes that method when current (`U.MethodDescription`), we still need a precise concept for **what happened as performed work** in real time and space.

A Work individual stands in actual performer, method, temporal, containing-system, affected-referent, binding, and resource-use relations only when those relations obtain world-side; they are not fields stored in the occurrence. A separate assertion or description may designate that individual and state the relations, but the episteme neither creates the relations nor becomes the Work occurrence.

