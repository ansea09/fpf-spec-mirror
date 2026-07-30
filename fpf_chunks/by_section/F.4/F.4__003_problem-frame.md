---
chunk_kind: "child"
pattern_id: "F.4"
pattern_title: "Role Description - Description Episteme for U.Role"
section_id: "F.4:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/F.4/F.4__003_problem-frame.md"
commit_sha: "308edacfa2bdb2c60d07e4e10c0deb1f260a6a31"
heading_path:
  - "F.4 — Role Description - Description Episteme for U.Role"
  - "F.4:1 — Problem Frame"
line_start: 89414
line_end: 89421
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.7"
  - "C.2.1"
  - "E.10.D2"
  - "E.24"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.18"
  - "F.3"
  - "F.6"
  - "F.8"
  - "F.9"
keywords:
  - "Role Characterisation Space (RCS)"
  - "RoleStateGraph (RSG)"
  - "invariants"
  - "role template"
  - "status template"
---

### F.4:1 - Problem Frame

Role descriptions are useful because a role value needs a recognizable description before people can assign it, name it, compare it, or use it in a method requirement. A role such as `InspectorRole` is not self-explanatory. The project needs to know which bounded context gives it meaning, what kind of holder can bear it, which role invariants matter, and which neighboring checks may become current.

The recurring failure is to make the role description carry too much. A compact card is tempting: put role, status, permission, evidence, capability, method, assignment, work, and publication cues into one "assignable" template. That looks convenient but creates duplicate ontology. A standard used as a requirement source becomes a "standard role"; a report used as evidence becomes an "evidence role"; an access-control label becomes a behavioral role; a role name becomes proof of capability or proof that work occurred.

F.4 therefore treats a role description as a description episteme about a work-facing `U.Role`. It may mention neighboring relations, but it does not absorb them.

