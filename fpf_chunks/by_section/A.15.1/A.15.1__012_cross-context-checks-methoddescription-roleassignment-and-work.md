---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:10"
section_title: "Cross-Context Checks (MethodDescription, RoleAssignment, and Work)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__012_cross-context-checks-methoddescription-roleassignment-and-work.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:10 — Cross-Context Checks (MethodDescription, RoleAssignment, and Work)"
line_start: 22857
line_end: 22874
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.15.5"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.3.1"
  - "A.3.2"
  - "B.1"
  - "B.1.6"
  - "B.3"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.System"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "EpisodeOf_work"
  - "TemporalPartOf_work"
  - "actuals"
  - "concurrent work part"
  - "operational work part"
  - "performed enactment"
  - "trace"
  - "work occurrence"
---

### A.15.1:10 - Cross-Context Checks (MethodDescription, RoleAssignment, and Work)

When a Work is recorded, perform these **three quick checks**:

1. **Method-description context check.** Does `methodDescriptionRef` refer to a MethodDescription **defined in** the judgement context, or bridged to it, when that reference is current?

   * If **no**, the Work is **out‑of‑context**; either change context or add a Bridge.

1. **RoleAssignment interval and context check.** Does `performedBy` cover the work interval in the same context, or is it bridged?

   * If **no**, the Work is **unassigned** for that context; remedy via a covering `U.RoleAssignment` or a policy exception.

1. **Standard-Outcome Check.** Do the Work inputs, outputs, and metrics satisfy the **acceptance criteria** from the referenced `U.MethodDescription` or declared standard **as interpreted in that context**?

   * If **no**, the Work **fails** or is “conditionally accepted” per context policy.

> **Manager’s mnemonic:** Context, assignment, Standard → **CAC**. Fail any → the Work is not acceptable *here* (perhaps acceptable elsewhere).

