---
chunk_kind: "child"
pattern_id: "F.12"
pattern_title: "Evaluate Promise Fulfilment from Work Evidence (Service Acceptance)"
section_id: "F.12:4"
section_title: "Core idea (didactic)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.12/F.12__005_core-idea-didactic.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "F.12 — Evaluate Promise Fulfilment from Work Evidence (Service Acceptance)"
  - "F.12:4 — Core idea (didactic)"
line_start: 130305
line_end: 130324
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.3"
  - "A.3.2"
  - "A.6.1"
  - "A.6.RCD"
  - "B.3"
  - "C.16"
  - "C.16.P"
  - "C.2"
  - "E.13"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.11"
  - "F.17"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.9"
  - "U.PromiseContent"
keywords:
  - "EvidenceStatus"
  - "PromiseContent"
  - "RequirementStatus"
  - "declared result scale"
  - "delivery Work"
  - "evaluation Work"
  - "indicator recovery"
  - "measured value"
  - "observation"
  - "operation result binding"
---

### F.12:4 - Core idea (didactic)

For an ordinary evaluation, the delivery facts, adequate observations, acceptance rule and supported result may suffice. Recover the evaluation’s performance history when it is claimed or used. Recover the following content as needed to justify the result:

1. the exact **`U.PromiseContent` claim** being evaluated;
2. the actual **Work occurrence or defined Work population** whose delivery is in question;
3. the promised outcome or characteristic and its scope;
4. the relevant **observations and measured values**, including scale and unit;
5. the explicit **window** and population boundary;
6. the evaluation Method and, when its performance history is claimed or consumed, the independently admitted dated evaluation Work that enacts it;
7. the selected evaluation inputs, applied rule and result; recover the exact A.6.1 application and result binding when that identity is claimed or required by the governing rule;
8. the acceptance rule and the result scale it declares; examples include Boolean, trichotomous, graded, `N/A`, and `Inconclusive`-including scales; and
9. the PromiseContentUse, delivery, fulfilment, measurement, evidence-use, any separately defined indicator or proxy, reliance, and status relations that connect these claims.

The operation's result value comes first. A RequirementStatus assertion of `Satisfied` or `Violated` is available only through the exact acceptance result and its F.10 rule. Insufficient evidence can support `EvidenceStatus=Inconclusive` and leave `RequirementStatus=Pending`, or it can yield a locally declared result such as `Inconclusive` when the acceptance scale says so; it never silently creates a mixed universal scale.

A plain summary may say **met**, **not met**, or **cannot judge** while distinguishing the result on its declared scale, the standing of the evidence and the status of the requirement.

A SchemeSenseCell addresses a local meaning; the evaluation still concerns the exact promise, Work, observations, values, result and status-use relation. A comparison table may display the argument; display alone does not establish those claims.

