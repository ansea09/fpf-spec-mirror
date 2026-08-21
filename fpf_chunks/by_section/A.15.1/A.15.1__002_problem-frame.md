---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__002_problem-frame.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:1 — Problem Frame"
line_start: 23757
line_end: 23762
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
  - "F.6"
  - "U.Capability"
  - "U.Method"
  - "U.MethodDescription"
  - "U.ReferenceScheme"
  - "U.System"
  - "U.SystemRoleAssignment"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "actual performer U.System"
  - "admitted U.Work kind"
  - "containing System"
  - "covering U.SystemRoleAssignment"
  - "enacted Method"
  - "optional direct bindings and resource use"
  - "performedUnderAssignment"
  - "separate result or consequence"
  - "temporal extent"
  - "world-side dated occurrence"
---

### A.15.1:1 - Problem Frame

After we have separated **which system-role assignment obtains** (via `U.SystemRoleAssignment`), **what capability is being relied on** (via `U.Capability`), **how in principle** the Work is done (the exact `U.Method`), and which claim-bearing episteme, if selected, describes that Method (`U.MethodDescription`), we still need a precise concept for **what happened as performed Work** in real time and space.

Every Work individual has actual performer-system, covering-assignment, enacted-method, temporal, and at least one locally declared containing-system relation. Several such relations may obtain under different exact system boundaries. A Work stands in a direct work-to-referent, binding, or resource-use relation only when that relation obtains world-side; none is a field stored in the occurrence. A separate assertion or description may designate that individual and state the relations, but the episteme neither creates the relations nor becomes the Work occurrence.

