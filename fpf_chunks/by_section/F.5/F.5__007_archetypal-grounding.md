---
chunk_kind: "child"
pattern_id: "F.5"
pattern_title: "Naming Discipline for U-kind Names and RoleDescription Labels"
section_id: "F.5:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/F.5/F.5__007_archetypal-grounding.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "F.5 — Naming Discipline for U-kind Names and RoleDescription Labels"
  - "F.5:5 — Archetypal Grounding"
line_start: 78886
line_end: 78923
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "E.10"
  - "E.10.ARCH"
  - "E.24.UK"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "U-kind naming"
  - "lexical rules"
  - "morphology"
  - "naming conventions"
  - "role-description labels"
  - "twin registers"
---

### F.5:5 - Archetypal Grounding

#### F.5:5.1 - Cross-Context Type Name

A Concept-Set row compares:

- SOSA `Observation`;
- metrology `measurement result`;
- ML practice `metric reading`;
- a dashboard value exported for subsequent comparison.

The row does not justify naming the U-kind `Observation` merely because one source tradition uses that word. It also does not justify `DashboardValue` if the dashboard is only one publication form. A name such as `Reading` or `Result` is admissible only if the row shows the shared invariant: produced value or record admitted for comparison in the declared context.

#### F.5:5.2 - Work-Facing Role Label

In `PlantMaintenance_2026`, the role-description episteme describes `PumpInspectorRole`.

```text
NamedValueSlot: PumpInspectorRole
NamedValueKindSlot: U.Role
MeaningSourceSlot: RoleDescription for PlantMaintenance_2026
TechLabelSlot: PumpInspectorRole
PlainLabelSlot: pump inspector role
NeighboringUseBoundarySlot: inspection report is evidence use; inspection method is method; assigned technician is RoleAssignment holder.
```

The label helps readers identify the role. It does not say Robot-7 holds the role, can inspect pumps, followed the inspection method, or produced an admissible report.

#### F.5:5.3 - Evidence Use Is Not a Role Name

Source text may say `ModelFitEvidenceRole`. The repair is not to invent a prettier role name. The project first recovers the current claim: a dataset, report, or model-output episteme is being used as evidence for a target claim under a scope, polarity, relevance window, assurance use, weight model, and provenance constraints.

The durable name, if needed, is a name for that evidence-use relation or status-use value under the direct governing pattern. It is not a work-facing `U.Role` and not a RoleDescription label.

#### F.5:5.4 - Relation Position Is Not a Role Name

In a relation signature, "provider role" may mean "the provider argument position". F.5 does not make `ProviderRole` a `U.Role` name. Use `A.6.5` to recover `ProviderSlot`, its admitted `ValueKind`, and its reference mode. If a provider system also has a work-facing role in a method, that is a separate `U.Role` claim and, when assigned, a separate `U.RoleAssignment` claim.

