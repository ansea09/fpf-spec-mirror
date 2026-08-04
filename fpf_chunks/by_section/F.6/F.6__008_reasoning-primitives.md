---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "RoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:6"
section_title: "Reasoning Primitives"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__008_reasoning-primitives.md"
commit_sha: "7ba40a95a967ca5c69afc63aeca381e6adedc8da"
heading_path:
  - "F.6 — RoleAssignment and Performed-Work Attribution Check"
  - "F.6:6 — Reasoning Primitives"
line_start: 91354
line_end: 91374
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.4"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.3.1"
  - "A.3.2"
  - "A.6.REL"
  - "E.10"
  - "E.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.9"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.Work"
keywords:
  - "actual performing U.System"
  - "assignment coverage"
  - "exact U.RoleAssignment"
  - "performedUnderAssignment"
  - "separate assertion and evidence"
  - "world-side attribution"
---

### F.6:6 - Reasoning Primitives

```text
RA : U.RoleAssignment is one exact obtaining assignment-relation occurrence
  and W : U.Work is one exact dated Work occurrence
  and RA.HolderSystemSlot actually performs W under RA.RoleValueSlot
  and the assignment predicate for RA obtains throughout the attributed work interval
  -> performedUnderAssignment(W, RA) obtains.
```

```text
An attribution assertion lacks adequate current support
  -> reliance on the assertion is unresolved;
  -> do not infer that performedUnderAssignment(W, RA) is false.
```

```text
A source episteme names a performer or role
  -> do not claim that performedUnderAssignment obtains until exact W and RA are recovered.
```

