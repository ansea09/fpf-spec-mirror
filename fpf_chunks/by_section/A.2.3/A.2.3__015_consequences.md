---
chunk_kind: "child"
pattern_id: "A.2.3"
pattern_title: "U.PromiseContent (Promise Content)"
section_id: "A.2.3:10.1"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.3/A.2.3__015_consequences.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "A.2.3 — U.PromiseContent (Promise Content)"
  - "A.2.3:10.1 — Consequences"
line_start: 3319
line_end: 3326
dependencies:
  - "A.1.1"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.6"
  - "A.2.8"
  - "A.3.1"
  - "A.3.2"
  - "A.6.8"
  - "A.6.C"
  - "E.10"
  - "F.12"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.ClaimScope"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.Scope"
  - "U.Work"
  - "U.WorkPlan"
  - "U.WorkScope"
keywords:
  - "SLA"
  - "SLO"
  - "Work evidence"
  - "acceptanceSpec"
  - "accessSpec"
  - "claim scope (G)"
  - "promise content"
  - "provider/consumer roles"
---

### A.2.3:10.1 - Consequences

| Consequence | Benefit | Cost or boundary |
| --- | --- | --- |
| Promise content becomes explicit | Work can be judged against the promised outcome, access or eligibility, and acceptance criteria instead of against a vague service label. | Teams must separate promise content from provider, access point, method, ticket, and work occurrence. |
| Commitments stay distinct | A promise-content clause can be reused as payload for `U.Commitment` without becoming the deontic commitment relation itself. | Accountability still needs `A.2.8`, role assignment, and source relations when those claims are current. |
| Work evidence has a target | `claimsPromiseContent`, `deliversPromisedOutcome`, and `fulfilsPromiseContent` can cite the promise and outcome spec. | The promise content does not prove delivery; delivery remains work plus evidence. |

