---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "Role Taxonomy"
section_id: "A.2:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__007_archetypal-grounding.md"
commit_sha: "792091cf6f89f21f3423d75c72238bb0982777f2"
heading_path:
  - "A.2 — Role Taxonomy"
  - "A.2:5 — Archetypal Grounding"
line_start: 2118
line_end: 2149
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.13"
  - "A.15"
  - "A.2.1-A.2.6"
  - "A.6.5"
  - "A.6.RSIR"
  - "E.24"
keywords:
  - "U.RoleAssignment"
  - "assignment"
  - "context"
  - "function vs identity"
  - "holder"
  - "responsibility"
  - "role"
---

### A.2:5 - Archetypal Grounding


#### A.2:5.1 - Pump in a Cooling Loop

```text
PumpUnit-3#CoolingCirculatorRole:Plant-A@2026-06-01..open
```

The holder is `PumpUnit-3`, a system. The role value is `CoolingCirculatorRole`. The context is `Plant-A`. The assignment window is open from a named date.

This does not say the pump has the capability to circulate under every condition. Capability claims stay under `A.2.2`. It does not say which method is used or which work occurred. Method, method description, work plan, and work claims stay under `A.15`.

#### A.2:5.2 - Standard Used in Design Work

"RFC-9110 has the protocol-standard role in this design" is source-side wording that must be repaired.

Current FPF expression:

- the RFC publication is an episteme or publication used as source, standard, requirement, or method-description source;
- the design service, engineer, or team is the system or acting holon holding any work-facing role;
- the design work is performed by that holder under a role assignment;
- the RFC does not perform the work and does not hold `U.Role`.

#### A.2:5.3 - Reviewer and Review Report

A person, team, or agent service can hold `ReviewerRole` for a review context. The review report produced by that work is an episteme. Later, another project may use the report as evidence or status input. That use is an evidence-use or status-use relation around the report, not a role assignment to the report.

#### A.2:5.4 - Relation Argument Named "Role"

In a relation signature, "role" may mean an argument position. If the claim is about a relation position, use `A.6.5` SlotSpec discipline. Do not create a `U.Role` merely because the source says "argument role".

