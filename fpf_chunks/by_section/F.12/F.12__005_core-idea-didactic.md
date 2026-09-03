---
chunk_kind: "child"
pattern_id: "F.12"
pattern_title: "Service Acceptance–Work Evidence Link"
section_id: "F.12:4"
section_title: "Core idea (didactic)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.12/F.12__005_core-idea-didactic.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "F.12 — Service Acceptance–Work Evidence Link"
  - "F.12:4 — Core idea (didactic)"
line_start: 96925
line_end: 96940
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

Before reporting the result, name nine things:

1. the exact **`U.PromiseContent` claim** being evaluated;
2. the actual **Work occurrence or defined Work population** whose delivery is in question;
3. the promised outcome or characteristic and its scope;
4. the relevant **observations and measured values**, including scale and unit;
5. the explicit **window** and population boundary;
6. the evaluation **Method** and the System's dated evaluation **Work** that enacts it;
7. the exact A.6.1 operation application, including its selected inputs and result binding;
8. the acceptance rule and declared result scale, such as a Boolean, trichotomous, graded, `N/A`, or `Inconclusive`-including scale when that scale is actually declared; and
9. the PromiseContentUse, delivery, fulfilment, measurement, evidence-use, any separately defined indicator or proxy, reliance, and status relations that actually connect these claims.

The operation's result value comes first. A RequirementStatus assertion of `Satisfied` or `Violated` is available only through the exact acceptance result and its F.10 rule. Insufficient evidence can support `EvidenceStatus=Inconclusive` and leave `RequirementStatus=Pending`, or it can yield a locally declared result such as `Inconclusive` when the acceptance scale says so; it never silently creates a mixed universal scale. A plain summary may say **met**, **not met**, or **cannot judge** while retaining that exact distinction. A SchemeSenseCell may help address a local meaning, but it cannot bear the promise, Work, observation, value, result, evidence, or status. A comparison table may display the argument, but it cannot establish any of it.

