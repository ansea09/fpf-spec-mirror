---
chunk_kind: "child"
pattern_id: "F.16"
pattern_title: "Worked-Example Template (Cross-Domain)"
section_id: "F.16:8"
section_title: "Worked micro-example"
source_path: "FPF-Spec.md"
output_path: "by_section/F.16/F.16__009_worked-micro-example.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "F.16 — Worked-Example Template (Cross-Domain)"
  - "F.16:8 — Worked micro-example"
line_start: 95667
line_end: 95682
dependencies:
  - "A.10"
  - "A.15"
  - "A.3"
  - "A.6.1"
  - "A.6.RCD"
  - "B.1.5"
  - "B.3"
  - "C.16.P"
  - "E.10.D1"
  - "E.13"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.12"
  - "F.15"
  - "F.17"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.6"
  - "F.7"
  - "F.9"
keywords:
  - "actual values"
  - "boundary"
  - "direct relations"
  - "evidence"
  - "exact sources"
  - "optional cell"
  - "optional comparison table"
  - "practical gain"
  - "working situation"
---

### F.16:8 - Worked micro-example

**Title and situation.** *An alarm log does not by itself prove monthly uptime.* Operations has an approved runbook and a month of IEC task and alarm logs; a service report must judge the exact ITIL promise-content claim.

**Worked claim.** June uptime is judged from admissible observations of the promised service outcome over the stated population and window. Alarm and command records may contribute evidence only through explicit relations and coverage limits.

**Actual subjects and routes.** The ITIL promise content and its promise-use, delivery, and fulfilment relations use A.2.3; the service-delivery Work and separate evaluation Work use A.15.1; the exact observations, availability characteristic, scale, and values use C.16; A.6.1 identifies the evaluation application and result binding; F.12 supplies the evaluation shape; A.10 supplies evidence use; and B.3 applies only if assurance is claimed or reliance is material. The runbook is a MethodDescription under A.3.2 only when its claims concern one admitted Method, and its edition is surfaced here only if it changes the evaluation result or replay.

**Source basis.** Cite the ITIL edition and promise passage, IEC edition and task and alarm passages, observation source and procedure, and any source-local meaning needed to interpret *availability* or *alarm*.

**Relations and limits.** State which observations concern which Work. First ask whether the observation and measurement model directly concerns the promised availability characteristic. If it does, use C.16 and A.10 and add no proxy. If alarm-state intervals instead indicate a distinct unavailable-service characteristic, name both participants and the pattern that defines or tests that relation, with covered modes and blind spots. Use C.16.P to recover the relation and stop at A.6.RCD `missing-governor` when no such rule exists. Use E.13 only when the indicator is optimized or drives a target, incentive, gate, release argument, reputation signal, repair, or decision. F.9 is needed only if the exact local meanings of *alarm state* and *unavailable service* are themselves related.

**Result.** A System performs evaluation Work, enacts the evaluation Method, and applies the declared availability rule to June's in-scope observations. The A.6.1 application binds those inputs and returns a result on the declared acceptance scale. Map it to `RequirementStatus=Satisfied` or `RequirementStatus=Violated` only through the exact F.10 rule. If the evidence is inadequate, use `EvidenceStatus=Inconclusive` and leave `RequirementStatus=Pending`, or return the exact local result declared by the scale. Create a verdict episteme only if another use needs it. Plainly: met, not met, or cannot judge. The approved runbook establishes none of these results or statuses.

**Checks.** Actual subjects; a defining or testing pattern for each relation; direct-measurement-before-proxy; evaluation Work, application and result binding; declared result scale; separate EvidenceStatus and RequirementStatus; matching window and population; visible indicator limit; and no row-created fact.

