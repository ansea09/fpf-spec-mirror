---
chunk_kind: "child"
pattern_id: "A.15"
pattern_title: "System-Role–Method–Work Alignment"
section_id: "A.15:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15/A.15__011_rationale.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "A.15 — System-Role–Method–Work Alignment"
  - "A.15:10 — Rationale"
line_start: 24531
line_end: 24538
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

### A.15:10 - Rationale

The practical failure is simple: teams often store classification, assignment, recipe, plan, capability, execution, result, and evidence in one “process” record, then cannot tell which fact changed. A.15 keeps the values separate and adds only the two alignment relations needed most often: performed-Work attribution and Method enactment.

The separation follows established ontology and practice distinctions among enduring systems, relation occurrences, event-like Work, and epistemes. Process-theory formalisms such as Petri nets and process calculi remain source lineage for dynamic interaction, but their word *process* is recovered here to Method, MethodDescription, WorkPlan, dated Work, Dynamics, Transformation, or a separate episteme rather than imported as one FPF object. FPF adapts the useful distinctions through local system-role kinds, assignment species and their occurrences, a common holder projection, Methods, WorkPlans, dated Work, and neighboring relations; it does not import a foreign hierarchy.

The distinction is operationally useful. When work fails, a team can ask whether the wrong system was assigned, the assignment did not cover the Work, the Method was unsuitable, the MethodDescription was wrong, the plan was stale, the capability claim was unsupported, or the performed occurrence departed from the Method. Correcting one answer need not rewrite the others.

