---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti-Explosion Control for System-Role and Status Name Families"
section_id: "F.14:10"
section_title: "Worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__011_worked-cases.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "F.14 — Anti-Explosion Control for System-Role and Status Name Families"
  - "F.14:10 — Worked cases"
line_start: 94846
line_end: 94905
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.3.1"
  - "A.3.2"
  - "A.6.5"
  - "B.3"
  - "E.10.D2"
  - "E.24.PUB"
  - "F.10"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.8"
  - "F.9"
  - "U.SystemRoleAssignment"
keywords:
  - "NameCard"
  - "assignment"
  - "designation"
  - "evidence use"
  - "permission"
  - "reuse"
  - "status names"
  - "system-role names"
  - "term row"
  - "vocabulary explosion"
---

### F.14:10 - Worked cases

#### F.14:10.1 - Requester and approver

Candidate family: `RequesterSystemRole`, `ApproverSystemRole`, `RequestApproverSystemRole`, `SeniorApprover`.

Result:

* `RequesterSystemRole` and `ApproverSystemRole` are exact local system-role kinds with separate `SystemRoleKindDescription` epistemes when descriptions are needed.
* `RequestApproverSystemRole` is blocked as a fused kind. Use an A.2.7 bundle relation when the two kinds travel together.
* If the same holder must not carry both assignments in the same change window, use the A.2.7 incompatibility relation. Recover the two assignment occurrences through A.2.1 and any applicable A.2.5 currentness condition. Use F.6 only if a separate claim says that dated Work was performed under one of them.
* `SeniorApprover` is not proof of independence or assurance. Recover the intended local system-role kind, exact assignment-state predicate or relation, capability, assurance, or policy claim before durable naming.

#### F.14:10.2 - Operators across shifts

Candidate family: `OperatorSystemRole`, `NightOperatorSystemRole`, `RemoteOperatorSystemRole`, `OnCallOperatorSystemRole`.

Result:

* `OperatorSystemRole` is the exact local system-role kind.
* `night`, `remote`, and `on-call` are source qualifiers whose governed conditions must be recovered—for example, a schedule, location relation, `SystemRoleAssignmentStatePredicate`, WorkPlan, or policy condition.
* A new system-role kind is blocked unless A.2 with C.3 independently admits a distinct local kind from its bounded work-facing contribution identity and a non-circular `KindSignature`. Its criterion may use, for example, a capability, Work, or an assignment established separately, but assignment conditions, a Method, and Work implications are not universal requirements. The naming ReferenceScheme does not create the kind or its difference.

#### F.14:10.3 - SLO compliance labels

Candidate family: `Compliant`, `AtRisk`, `Grace`, `Breached`, `Waived`.

Result:

* These are not system-role-kind names.
* F.10 recovers status family, status value, status window, confidence, or deontic or policy use.
* Presentation labels may stay local or be named by the direct status pattern. They do not become a system-role kind, `SystemRoleKindDescription`, or relation structure among system-role kinds.

#### F.14:10.4 - Evidence and requirement suffixes

Candidate family: `EvidenceRole`, `RequirementRole`, `StandardRole`, `SourceRole`.

Result:

* No work-facing system-role kind is recovered from suffix alone.
* Evidence, requirement, standard, source, and publication uses go to A.10, B.3, E.10.D2, E.24.PUB, or the direct requirement or source pattern.
* A durable name may be admitted for the recovered relation, but not as a local system-role kind.

#### F.14:10.5 - Same spelling across two local-sense bases

A plant team uses `Operator` for one local system-role kind. An access-control team uses `Operator` for one permission grouping. Recover both independently under their direct patterns; neither spelling nor organizational proximity makes them one value.

For local use, keep the existing expressions and stop. If one named cross-local naming use is later proposed, resolve its exact F.17 `SchemeSenseCell` endpoints and test F.9. Cite a Bridge only when its predicate obtains, then state the use direction, rule, tolerated loss, polarity, and reliance separately. A Bridge, NameCard, cell, or row imports no access permission as `U.SystemRoleAssignment`, capability, authority, or performed Work. Publish an F.17 row only when the public or durable reuse threshold independently holds.

#### F.14:10.6 - Ordinary composite role-like phrases

A project says: "Vasya is an engineer, he works on musical robots, and he is also a musician who teaches robots to play music."

Result:

* Ordinary prose may remain `robotics engineer and musician` or `engineer-musician` when the sentence is clear and no FPF claim relies on either noun as an exact classification. Create no Tech kind merely to explain the phrase, and do not require a `SystemRole` suffix in ordinary prose.
* If the sentence supports a load-bearing FPF claim, apply E.10.ROLE and recover only the supported branch: for example, a local system-role kind and classification, an assignment occurrence, a capability, a participation or contribution relation, a Method or Work claim, or a finding that no pattern yet defines the needed claim. Do not infer two kinds from the two nouns.
* Any claim about an engineering or music-teaching Method, robot-training Work, or performed music Work stays under its direct pattern and remains separate from the ordinary phrase. Such a claim does not by itself justify a system-role-kind name.
* A durable qualified system-role-kind name becomes a candidate only after A.2 with C.3 independently admits that exact local kind and its bounded contribution identity. Differences in, for example, assignment conditions, capability expectations, incompatibilities, or Method or Work implications matter only when the `KindSignature` or named use actually consumes them. A readable suffix does not perform that admission.

