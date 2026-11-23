---
chunk_kind: "child"
pattern_id: "F.10"
pattern_title: "Apply and Interpret Evidence, Standard and Requirement Statuses"
section_id: "F.10:5"
section_title: "Archetypal grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/F.10/F.10__006_archetypal-grounding.md"
commit_sha: "6226816d8005a4c8ee3af338bb3752f6732449a9"
heading_path:
  - "F.10 — Apply and Interpret Evidence, Standard and Requirement Statuses"
  - "F.10:5 — Archetypal grounding"
line_start: 131051
line_end: 131078
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.4"
  - "A.6.1"
  - "B.3"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.17"
  - "E.24.PUB"
  - "F.17"
  - "F.18"
  - "F.9"
  - "G.11"
  - "G.6"
keywords:
  - "EvidenceStatus"
  - "RequirementStatus"
  - "StandardStatus"
  - "direct result"
  - "governed target"
  - "interpretation rule"
  - "scope"
  - "status families"
  - "status value"
  - "window"
---

### F.10:5 - Archetypal grounding

#### F.10:5.1 - Service acceptance from runtime evidence

July uptime is first recovered as an exact C.16 measurement result, stated by a distinct C.2.1 episteme. A.2.4 classifies that episteme for the uptime claim, and F.10 may assert `EvidenceStatus=Measured` for that exact claim, scheme, scope, and July window.

The SLO clause and service target are independently recovered. Dated evaluation work applies the SLO rule to the measurement result through exact bindings and produces a requirement-evaluation result claim. A separate `RequirementStatus=Satisfied` claim for this clause and window needs a result that meets the clause’s evaluation rule. Here the dated evaluation Work supplies that result.

If the comparison relies on a semantic correspondence between the monitoring and service-management senses, test the F.9 Bridge and the bounded use. If the evaluation draws on the `Measured` status itself, use `StatusInterpretationRelation` to check whether the rule admits that status for the clause question. The measurement, evidence status, bridge, interpretation, evaluation work/result, requirement status, dashboard display, gate, assurance, and release decision remain distinct.

For a different July clause, suppose the service is available whenever either of two channels is available and the promise allows no interruption. Each channel was down for one hour. If those hours coincided the promise was missed. If they were disjoint it was met. Recover the overlap, or a direct service observation that settles it. A question about the recorded downtime of one channel can use that channel’s result directly.

#### F.10:5.2 - Approved method description

One exact safety-controller MethodDescription is `StandardStatus=Approved` only under the named standard/profile edition, source relation, scheme, scope, window, and selection use. That status neither creates the MethodDescription nor proves an approval speech act, permission, method enactment, or response-time satisfaction.

For a controller run independently admitted as `U.Work` under A.15.1, keep that occurrence separate from its response-time measurement result. That result and its evidence-use relation can enter direct clause evaluation. A separate requirement status may follow from the evaluation; it does not inherit `Approved` by label or family edge.

#### F.10:5.3 - Model card and fairness requirement

A model card reports high cross-validation AUC. Recover the exact predictive-performance result and claim episteme first; distinguish that claim from the card's publication or display. F.10 may assert an `EvidenceStatus` for that predictive claim under its validation scheme and window.

The AUC result leaves the clause “demographic parity delta ≤ 0.1” open. Apply the clause's selection-rate definition to the eligible groups and production window. Measurement can supply the rates. If both groups are nonempty and the evidence establishes the same constant decision for every eligible member throughout the window, their rate difference is zero. A promised measurement procedure or trace has its own completion condition. For a status assertion, retain the policy clause, evidence used, rule application and result. Recover dated evaluation Work when its history is claimed or consumed.

#### F.10:5.4 - Status display cue

A release dashboard cell shows `Ready`. The cell is only a cue until exact source assertion, target, value cell, scheme, scope, window, provenance/currentness, and intended use are recoverable. Display or list membership does not establish a status-use occurrence or actual reliance. If the status is consumed for a gate, release, assurance, admission, permission, or decision, the subject pattern must admit the separate use and result.

