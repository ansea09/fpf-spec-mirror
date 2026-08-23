---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:7"
section_title: "Scope Declaration and Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__009_scope-declaration-and-rationale.md"
commit_sha: "7f7c592f4d633e54cdb202d622d6e0e05df41517"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:7 — Scope Declaration and Rationale"
line_start: 24131
line_end: 24136
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
  - "U.System"
  - "U.SystemRoleAssignment"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "actual performer U.System"
  - "admitted U.Work kind"
  - "containing System"
  - "covering U.SystemRoleAssignment"
  - "enacted Method"
  - "optional direct bindings and resource use"
  - "performedUnderAssignment"
  - "separate result or consequence"
  - "temporal extent"
  - "world-side dated occurrence"
---

### A.15.1:7 - Scope Declaration and Rationale

* **Applicability:** Use the same occurrence test for pragmatic costing, architecture use, teaching examples, and source or evidence questions; when the current claim is only about a description, publication, source, or evidence relation, apply the direct pattern for that claim.
* **Scope declaration:** The occurrence head is universal. Temporal semantics use the declared temporal reference. A simple uninterrupted occurrence needs no continuity-policy episteme; identity, episode, retry, resumption, or aggregation claims cite `workContinuityPolicyRef` and its effective `U.ReferenceScheme` only when the named use must resolve an ambiguous boundary. Add claim scope, a qualification window, model-use structure, evidence use, or source-currentness assessment only when changing that neighboring fact would change the receiving assertion or reliance; otherwise omit it.
* **Rationale:** Gives FPF a clean, actionable notion of **occurrence** with admitted performer `U.System`s, a covering occurrence of an exact directly declared `U.SystemRoleAssignment` species for every performer, the corresponding F.6 attribution, and the obtaining `enactsMethod` relation. Costing, quality, and audit then rest on independently identified Work occurrences rather than plans, recipes, assignments made to act, or a generic role-enactment fact.

