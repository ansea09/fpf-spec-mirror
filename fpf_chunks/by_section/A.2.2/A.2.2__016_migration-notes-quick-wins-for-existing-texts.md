---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "U.Capability"
section_id: "A.2.2:15"
section_title: "Migration notes (quick wins for existing texts)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__016_migration-notes-quick-wins-for-existing-texts.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "A.2.2 — U.Capability"
  - "A.2.2:15 — Migration notes (quick wins for existing texts)"
line_start: 2506
line_end: 2513
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.3"
  - "A.3"
  - "U.BoundedContext"
  - "U.Dynamics"
  - "U.PromiseContent"
  - "U.RoleAssignment"
keywords:
  - "ability"
  - "action"
  - "measures"
  - "performance"
  - "skill"
  - "work scope"
---

### A.2.2:15 - Migration notes (quick wins for existing texts)

1. **Underline WorkScopes.** For every “can do” sentence, add **conditions** and **measures**; otherwise treat it as background color, not a gate.
2. **Pull thresholds out of roles.** Move “≤ 0.2 mm”, “≥ 0.90 optimality” from role labels into **step requirements**; leave roles clean (assignments).
3. **Pin contexts.** Add the bounded context name to each capability table (“Capability Sheet — AssemblyLine\_2025”).
4. **Snapshot validity.** Add a “valid through” column (software version or calibration horizon).
5. **Separate recipe/execution.** Move flowcharts under **MethodDescription**, runs under **Work**; link the capability to the **holder** with references to those specs.

