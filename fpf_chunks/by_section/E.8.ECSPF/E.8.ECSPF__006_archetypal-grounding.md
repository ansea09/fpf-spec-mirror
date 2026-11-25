---
chunk_kind: "child"
pattern_id: "E.8.ECSPF"
pattern_title: "Author an FPF Pattern from an Accepted Evaluation CharacteristicSpace Specification"
section_id: "E.8.ECSPF:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8.ECSPF/E.8.ECSPF__006_archetypal-grounding.md"
commit_sha: "423f9d3fef92bafec7b092b910e8ce056a0f607d"
heading_path:
  - "E.8.ECSPF — Author an FPF Pattern from an Accepted Evaluation CharacteristicSpace Specification"
  - "E.8.ECSPF:5 — Archetypal Grounding"
line_start: 104612
line_end: 104657
dependencies:
  - "A.19.ECS"
  - "C.25"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9.DA"
  - "F.18"
  - "F.19"
keywords:
---

### E.8.ECSPF:5 - Archetypal Grounding

Guidance based on an evaluation `CharacteristicSpace` becomes reusable in FPF only when a practitioner can recognize the evaluated object and use before reading the coordinate table. The publication form must teach practitioners how to carry out the evaluation. A list of values alone is insufficient. The following slice shows the author's move from an accepted specification to practitioner-facing content.

**Accepted specification.** An author has an accepted `EvaluationCharacteristicSpaceSpec` for one version of a field-service handover instruction.

| Accepted value | Selected content |
|---|---|
| Evaluated object and use | One field-service handover instruction version, judged for readiness for a supervised first use. |
| Working reader and qualification window | A maintenance lead who did not author the instruction; the result remains qualified only while the named equipment configuration and safety-procedure edition remain unchanged. |
| Discriminating cases | A usable handover instruction; an instruction of the same kind that hides its stop condition; and a spare-parts catalogue, which is outside the evaluated object kind. |
| `FirstMoveRecoverability` | `0` when the lead cannot identify the first move in the trial. `1` when it is identifiable but the lead needs help beyond the instruction to state or perform it, or can complete only part of that task. `2` when the lead states and carries out the first move from the instruction. |
| `HazardBoundaryVisibility` | Judge the instruction and the guidance it cites and makes available for this use. `0` when no usable stop or escalation condition is recoverable from these materials. `1` when it can be recovered only from that cited guidance or from a passage placed after the first move. `2` when the instruction itself gives the applicable condition before the first move and says when to stop or escalate. |
| Evidence and missingness | Observe one cold-reader trial and cite the instruction locus used for each value. Use a configuration in which the supervised first move can be observed under the applicable safety conditions. If the move may not be attempted, record the execution evidence as missing. An observed difficulty can warrant a low value. An unobserved required performance leaves the judgement dependent on it open. |
| Result and trade-off | Each row contains coordinate, value, adjacent-value rationale, evidence locus, and missingness. Improving first-move wording must not hide or weaken the hazard boundary. |
| Status and stop | Return `ready for supervised use` when current observations establish `2` on both coordinates. A demonstrated value below `2` warrants `repair`, including when the other value is missing. If the available evidence establishes no value below `2` and a required observation is missing, withhold the readiness decision until admissible evidence is available. Reopen after an equipment-configuration or safety-procedure change. |

**Corresponding recognition lines in the authored pattern.**

> Use this pattern when you must decide whether a field-service handover instruction is ready for a supervised first use by a maintenance lead who did not write it. Use it only for the named equipment configuration and safety-procedure edition. Give that reader the current instruction. Ask them to identify the first move and the condition for stopping or escalation. In the supervised trial observe whether they can carry out the move when its conditions permit. Record where they obtained the stop condition. A spare-parts catalogue is outside this evaluation.

These lines carry the selected object kind, use, reader, qualification window, first move, and wrong-kind boundary. The citation “see `A.19.ECS`” alone would not convey them.

**Minimal Solution and result form.** The pattern then tells the practitioner to use the current instruction version, observe the cold-reader trial, judge both coordinates from their stated value meanings, and record both coordinate results. For example:

| Coordinate | Value | Adjacent-value rationale | Evidence locus | Missingness |
|---|---:|---|---|---|
| `FirstMoveRecoverability` | `2` | The lead both named and carried out the move from the instruction. | Opening instruction and both observations in the supervised trial. | checked |
| `HazardBoundaryVisibility` | `1` | The lead had to consult a separate cited source for the condition. | The instruction points to the safety reference after the first action. Only that reference states the boundary. | checked |

The result is `repair` because one coordinate is below the declared ready value. The revised instruction puts the stop condition before the first move and states when to stop or escalate. In a cold supervised trial, a lead who did not write the instruction states the first move from it, identifies why the condition permits proceeding, and carries out that move. These observations support both `2` values and `ready for supervised use` for this configuration and edition. A spare-parts catalogue returns to evaluation selection before these rows are opened.

A simple `A.10` citation is enough to locate the evidence-use discipline for this ordinary case; identify the assertion or `ClaimGraph` only if later interpretation or reuse depends on its identity.

**Near miss, proxy improvement.** A shorter instruction makes the first move easier to find. In the stipulated cold trial the lead also states and performs it from the instruction, establishing `FirstMoveRecoverability` at `2`. The editor removed the only statement of the stop condition and its reference, so `HazardBoundaryVisibility` is `0`. Finding the shorter sentence alone would leave performance untested.

The author must not add or average those ordinal values and call the rewrite better. The protected safety trade-off has been lost, so the pattern returns `repair` and the accepted specification must be reopened if its current status rule would reward that rewrite.

**Pattern-quality evaluation.** `E.21` is an evaluation for one FPF pattern version. Its publication form must still open with the working question "is this pattern good enough for the declared use?" before showing coordinates such as first-action recoverability, boundary fit, and SoTA binding.

**Local rubric.** A project team defines a temporary rubric for choosing a meeting room. The `A.19.ECS` specification may be adequate locally, but no durable FPF pattern is needed because the evaluated object kind and use do not recur across FPF practice.

**Object-kind boundary.** A nuclear-plant evaluation can judge nuclear plants and declared comparable power-generation alternatives. A plant inspection report can supply evidence about the plant but is outside that evaluated-object kind: before the evaluation is opened, select a suitable evaluation; after a forced invocation, record an object-kind-fit defect/value rather than treating it as a weak nuclear plant or skipping declared coordinates.

The pattern publication form must show that boundary before readers try to use the coordinate table.

