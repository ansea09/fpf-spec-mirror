---
chunk_kind: "child"
pattern_id: "A.15"
pattern_title: "System-Role–Method–Work Alignment"
section_id: "A.15:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15/A.15__002_problem-frame.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "A.15 — System-Role–Method–Work Alignment"
  - "A.15:1 — Problem frame"
line_start: 23394
line_end: 23408
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.15.3"
  - "A.15.4"
  - "A.15.5"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.20"
  - "A.21"
  - "A.3"
  - "A.6"
  - "A.6.5"
  - "A.7"
  - "B.3"
  - "C.28"
  - "C.29"
  - "C.3"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.ROLE"
  - "E.17.EFP"
  - "E.18.1"
  - "F.6"
  - "U.SystemRoleAssignment"
keywords:
  - "Method"
  - "MethodDescription"
  - "WorkPlan"
  - "assignment"
  - "attribution"
  - "dated Work"
  - "readiness"
  - "result boundary"
  - "system-role kind"
---

### A.15:1 - Problem frame

Complex work requires several independent distinctions: what a System is; which local system-role kind classifies it; which assignment occurrence obtains and which declared `U.SystemRoleAssignment` species it instantiates; how Work is done through `U.Method`; whether an episteme is a `U.MethodDescription`; which holder capability is relied on; what `U.WorkPlan` states; which dated Work happened; and which separate assertions, records, results, and evidence concern that Work.

A.15 brings these already defined values together without creating a new process object or redefining their ontologies:

* **A.2 and C.3** identify a local system-role kind and any classification judgment. Classification neither creates an assignment nor proves Work.
* **A.2.1** identifies an assignment occurrence and its declared species under `U.SystemRoleAssignment`. The species declares `HolderSystemSlot`, a declaration-local `AssignedSystemRoleKindSlot` with its local system-role-kind domain, its predicate and applicability, any additional participants, and its occurrence-identity rule. The occurrence supplies the actual participants and extent. Taxonomy, scheme, signature, assertion, evidence, and interval may interpret or describe the claim; they are not generic participants.
* **F.6** relates one dated Work occurrence to one exact assignment occurrence through `performedUnderAssignment` and projects the actual performer from `RA.HolderSystemSlot`.
* **A.3.1 and A.3.2** keep `U.Method` distinct from `U.MethodDescription`.
* **A.15.1 and A.15.2** keep actual dated Work distinct from intended WorkPlan and from every record about either.
* **A.2.2, A.10, and neighboring direct patterns** keep capability-fit claims, evidence use, source currentness, publication, responsibility, authority, access, results, and assurance outside assignment and Work identity.

Use `E.10`, `E.10.ARCH`, and `E.10.ROLE` when source wording such as *process*, *workflow*, *action*, *activity*, *schedule*, or *role* has not yet been resolved. The wording chooses no FPF object by itself. Recover the exact Method, MethodDescription, WorkPlan, Work, Transformation, Dynamics, evidence, gate, source, publication use, participation relation, declaration slot, or ordinary non-technical use that the claim actually needs.

