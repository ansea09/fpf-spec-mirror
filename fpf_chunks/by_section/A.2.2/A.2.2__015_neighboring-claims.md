---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "System Capability: Conditions, Measures and Fit"
section_id: "A.2.2:14"
section_title: "Neighboring Claims"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__015_neighboring-claims.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "A.2.2 — System Capability: Conditions, Measures and Fit"
  - "A.2.2:14 — Neighboring Claims"
line_start: 4432
line_end: 4448
dependencies:
  - "A.1"
  - "A.15"
  - "A.2.3"
  - "A.2.6"
  - "C.2.1"
  - "E.23.CDI"
keywords:
  - "attained bounds"
  - "capability fit"
  - "currentness"
  - "holder ability"
  - "qualification"
  - "support"
  - "work conditions"
---

### A.2.2:14 - Neighboring Claims

Keep the direct governor of each neighboring value needed by the ability or fit claim:

- local system-role kind, direct system-role assignment, `SystemRoleAssignmentStateRelation`, structure of relations among system-role kinds, or system-role-kind description;
- method, method family, method description, or algorithm description;
- work plan, work occurrence, run record, or measurement trace;
- evidence graph, source record, model card, standard, report, dashboard, publication, or specification-use relation;
- promise content, commitment, permission, authority relation, or policy decision;
- `U.Characteristic`, scale row, coordinate, score, metric, indicator, or threshold;
- `C.25` Q-Bundle, quality-family label, mechanism, status, or evidence slot;
- architecture-characteristic starter head, project criteria row, eval program, eval reading, selected-structure adequacy claim, or architecture-description concern;
- capability-fit predicate, gate, admission relation, or work-entry readiness record;
- structural part, module, interface, port, or functional structure unless the current claim is the ability of a holder system expressed through that structure.

These values may contribute to a holder-ability claim, its support or a receiving fit check. Name the neighboring value, record, relation, or predicate through its own governing pattern when that neighboring claim is current.

