---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:15a"
section_title: "P2W Performed-Work Use Relation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__020_p2w-performed-work-use-relation.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:15a — P2W Performed-Work Use Relation"
line_start: 25021
line_end: 25026
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
  - "U.Role"
  - "U.RoleAssignment"
  - "U.System"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "actual performer U.System"
  - "admitted U.Work kind"
  - "containing system"
  - "covering U.RoleAssignment"
  - "enacted method"
  - "optional direct bindings and resource use"
  - "performedUnderAssignment"
  - "separate result or consequence"
  - "temporal extent"
  - "world-side dated occurrence"
---

### A.15.1:15a - P2W Performed-Work Use Relation

When `E.18.1` reaches performed work, identify one Work individual admitted under `U.Work`, then recover each actual performer `U.System`, the exact obtaining `U.RoleAssignment` under which it performed and any explicit F.6 attribution, plus the separately obtaining enacted-method, temporal, and containing-system relations. Add binding, resource-use, or work-to-referent relations only when the receiving use needs them. When P2W continues into a result or consequence claim, select the exact §4.6 row and carry that object under its own governor.

A Work occurrence may be designated by an episteme that also cites a `U.WorkPlan`, exact A.15.3 planned-filling claim, or prior readiness claim as a baseline. State every actual participant, parameter, premise, operation argument or result, resource use, and work-to-referent fact only through its obtaining direct relation or exact A.6.1 application binding. Do not copy a result or consequence into Work; follow the concrete §4.6 route.

