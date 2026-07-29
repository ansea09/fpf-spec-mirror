---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "RoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:13"
section_title: "SoTA-Echoing and Source Use"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__015_sota-echoing-and-source-use.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "F.6 — RoleAssignment and Performed-Work Attribution Check"
  - "F.6:13 — SoTA-Echoing and Source Use"
line_start: 89866
line_end: 89876
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

### F.6:13 - SoTA-Echoing and Source Use

| Source line | Contribution | FPF use |
|---|---|---|
| FPF `A.2.1`, `A.2.5`, and `A.15.1` | Separate assignment occurrence, role-state relation, and dated work occurrence. | Adopt directly: `performedUnderAssignment` relates exact work and assignment occurrences without importing state or evidence as participants. |
| Almeida, Guizzardi, Sales, and Fonseca, [gUFO](https://arxiv.org/abs/2603.20948), 2026 preprint | Current foundational-ontology comparator separates role-like classification, relation aspects, and explicit relation occurrences. | Keep `U.Role`, `U.RoleAssignment`, and `performedUnderAssignment` distinct; use FPF's own system-holder and occurrence-identity rules rather than importing the comparator's hierarchy. |
| W3C [PROV-O](https://www.w3.org/TR/prov-o/), mature 2013 Recommendation used as representation lineage | Qualified association distinguishes activity, agent, role, and plan inside a provenance description. | Preserve the useful separation while keeping the provenance episteme distinct from world-side work, assignment, and attribution obtaining. |
| [OCEL 2.0 Specification](https://www.ocel-standard.org/specification/overview/), 2024 event-log representation practice | Events, objects, event-to-object relations, object-to-object relations, and relation qualifiers are represented explicitly. | Use an OCEL row as an assertion or evidence only after work and assignment identities are recovered; qualified log relations do not become the performed work or its world-side attribution by storage form. |

These lines discipline the examples rather than supply a foreign ontology. FPF takes the useful separation pressure and retains its own constructive relation, work, role-assignment, episteme, and evidence distinctions.

