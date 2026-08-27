---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti-Explosion Control for System-Role and Status Name Families"
section_id: "F.14:10"
section_title: "Worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__011_worked-cases.md"
commit_sha: "3f6714ae3235e0d771dce32835be7696f626d2ee"
heading_path:
  - "F.14 — Anti-Explosion Control for System-Role and Status Name Families"
  - "F.14:10 — Worked cases"
line_start: 95825
line_end: 95888
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

Premise: the local practice has already admitted `RequesterSystemRole` and `ApproverSystemRole` as exact local system-role kinds under A.2 with C.3. If that independent basis is absent, the case returns two candidates whose kind status is unresolved; the spellings do not admit them.

Result after that premise:

* Reuse the two admitted kinds and keep separate `SystemRoleKindDescription` epistemes only when descriptions are needed.
* `RequestApproverSystemRole` is blocked as a fused kind. Use an A.2.7 bundle relation when the two kinds travel together.
* If the same holder must not carry both assignments in the same change window, use the A.2.7 incompatibility relation. Recover the two assignment occurrences through A.2.1 and any applicable A.2.5 currentness condition. Use F.6 only if a separate claim says that dated Work was performed under one of them.
* `SeniorApprover` is not proof of independence or assurance. Recover the intended local system-role kind, exact assignment-state predicate or relation, capability, assurance, or policy claim before durable naming.

#### F.14:10.2 - Operators across shifts

Candidate family: `OperatorSystemRole`, `NightOperatorSystemRole`, `RemoteOperatorSystemRole`, `OnCallOperatorSystemRole`.

Premise: A.2 with C.3 has independently admitted `OperatorSystemRole` as an exact local system-role kind. Without that basis, `OperatorSystemRole` is still a candidate name and the case makes no kind claim.

Result after that premise:

* Reuse the admitted `OperatorSystemRole` kind.
* `night`, `remote`, and `on-call` are qualifiers in the proposed wording. Recover the claim each qualifies—for example, a schedule, location relation, `SystemRoleAssignmentStatePredicate`, WorkPlan, or policy condition—and use the pattern that defines, constrains, or tests that claim.
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
* Route each recovered claim separately: bounded evidence reliance goes to A.10; an actual named assurance claim goes to B.3; description-use ambiguity goes to E.10.D2 for recovery only; and publication occurrence, form, or carrier goes to E.24.PUB. A requirement, standard, source, access, or policy use goes to the pattern that directly defines, constrains, or tests that exact claim. If none exists, return `missing-governor`.
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

