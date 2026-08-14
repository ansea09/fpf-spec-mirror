---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.SystemRoleAssignment - Contextual System-Role Assignment"
section_id: "A.2.1:8"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__010_conformance-checklist.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "A.2.1 — U.SystemRoleAssignment - Contextual System-Role Assignment"
  - "A.2.1:8 — Conformance Checklist"
line_start: 3399
line_end: 3417
dependencies:
  - "A.1.1"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.3"
  - "A.6.5"
  - "A.6.9"
  - "A.6.REL"
  - "C.2.1"
  - "C.27"
  - "C.27.TA"
  - "C.3.3"
  - "F.6"
  - "F.9"
keywords:
  - "assignment predicate"
  - "direct assignment species"
  - "holder System"
  - "identity"
  - "maximal interval"
  - "performedUnderAssignment"
  - "system-role kind"
---

### A.2.1:8 - Conformance Checklist

| ID | Check |
| --- | --- |
| `CC-A2.1-1` | `U.SystemRoleAssignment` has no permissive root `RelationSignature`; every occurrence belongs to one directly declared species. |
| `CC-A2.1-2` | Every species declares `HolderSystemSlot : U.System` and one declaration-local `AssignedSystemRoleKindSlot` with an exact local system-role-kind domain. |
| `CC-A2.1-3` | Every additional participant changes the predicate or occurrence identity and has an admitted kind and complete SlotSpec. |
| `CC-A2.1-4` | The direct predicate, applicability, and occurrence-identity rule are explicit. |
| `CC-A2.1-5` | One occurrence is the maximal uninterrupted predicate-true interval for fixed participant values; a demonstrated gap creates another occurrence. |
| `CC-A2.1-6` | `assignmentInterval` describes known extent and is not a participant or proof of obtaining. Ordinary interval content stays local; a relied-on positive temporal aspect uses `C.27.TA`, while temporal-claim adequacy uses `C.27`. |
| `CC-A2.1-7` | Taxonomy, scheme, signature, assertion, evidence, publication, and model-use structure are not generic assignment participants. |
| `CC-A2.1-8` | A specialized occurrence is itself a `U.SystemRoleAssignment`; no weaker generic duplicate is created. |
| `CC-A2.1-9` | Every species declares the common holder slot by which F.6 projects the actual holder from an occurrence, without erasing additional participants. |
| `CC-A2.1-10` | Classification and assignment remain independent; assignment is a criterion feature only when the signature explicitly says so. |
| `CC-A2.1-11` | Performed Work uses `performedUnderAssignment(W, RA)` and the actual performer is `RA.HolderSystemSlot`. |
| `CC-A2.1-12` | A `...SystemRoleAssignmentRef` field is typed by `U.RelationRef constrained to U.SystemRoleAssignment`, resolves to one exact occurrence, and keeps its declared species recoverable. |
| `CC-A2.1-13` | Missing evidence yields unresolved or `unknown`; only demonstrated predicate failure ends the occurrence. |
| `CC-A2.1-14` | Reduced use stops before explicit individuation when no receiver needs an assignment reference. |

