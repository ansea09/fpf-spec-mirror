---
chunk_kind: "child"
pattern_id: "E.8.ECSPF"
pattern_title: "FPF Pattern Publication Form for Evaluation Guidance"
section_id: "E.8.ECSPF:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8.ECSPF/E.8.ECSPF__006_archetypal-grounding.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "E.8.ECSPF — FPF Pattern Publication Form for Evaluation Guidance"
  - "E.8.ECSPF:5 — Archetypal Grounding"
line_start: 72866
line_end: 72905
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

**Tell.** Guidance based on an evaluation `CharacteristicSpace` becomes reusable in FPF only when a practitioner can recognize the evaluated object and use before reading the coordinate table. The publication form must teach the evaluation use, not merely list the values. The following slice shows the author's move from an accepted specification to practitioner-facing content.

**Accepted specification.** An author has an accepted `EvaluationCharacteristicSpaceSpec` for one version of a field-service handover instruction.

| Accepted value | Selected content |
|---|---|
| Evaluated object and use | One field-service handover instruction version, judged for readiness for a supervised first use. |
| Working reader and qualification window | A maintenance lead who did not author the instruction; the result remains qualified only while the named equipment configuration and safety-procedure edition remain unchanged. |
| Discriminating cases | A usable handover instruction; an instruction of the same kind that hides its stop condition; and a spare-parts catalogue, which is outside the evaluated object kind. |
| `FirstMoveRecoverability` | `0`: the first move cannot be found; `1`: it can be recovered only with author help or an undeclared source; `2`: the working reader can state and carry out the first move from the instruction. |
| `HazardBoundaryVisibility` | `0`: the hazard or stop boundary is absent; `1`: it is recoverable only by chasing another source; `2`: it appears before the first move and says when to stop or escalate. |
| Evidence and missingness | Observe one cold-reader trial and cite the instruction locus used for each value. An unchecked coordinate is `missing` and cannot be treated as `2`. |
| Result and trade-off | Each row contains coordinate, value, adjacent-value rationale, evidence locus, and missingness. Improving first-move wording must not hide or weaken the hazard boundary. |
| Status and stop | `ready for supervised use` requires `2` on both coordinates with current evidence. Otherwise return `repair`. Reopen after an equipment-configuration or safety-procedure change. |

**Corresponding recognition lines in the authored pattern.**

> Use this pattern when you must decide whether a field-service handover instruction is ready for a supervised first use by a maintenance lead who did not write it. Use it only for the named equipment configuration and safety-procedure edition. First give the current instruction to that reader and ask them to identify the first move and the condition that requires stopping or escalation. A spare-parts catalogue is outside this evaluation.

These lines carry the selected object kind, use, reader, qualification window, first move, and wrong-kind boundary. Merely writing “see `A.19.ECS`” would not.

**Minimal Solution and result form.** The pattern then tells the practitioner to use the current instruction version, observe the cold-reader trial, judge both coordinates from their stated value meanings, and record both rows. For example:

| Coordinate | Value | Adjacent-value rationale | Evidence locus | Missingness |
|---|---:|---|---|---|
| `FirstMoveRecoverability` | `2` | `1` would understate independent recovery; no higher value exists. | Opening instruction and observed first move. | checked |
| `HazardBoundaryVisibility` | `1` | `0` would ignore the recoverable safety reference; `2` would overstate visibility before action. | Safety reference after the first action. | checked |

The returned status is `repair`, because one coordinate remains below its declared ready value. If both checked rows were `2`, the instruction would reach `ready for supervised use`; a spare-parts catalogue would return to evaluation selection before these rows were opened. A simple `A.10` citation is enough to locate the evidence-use discipline for this ordinary case; a particular assertion or `ClaimGraph` is needed only if later interpretation or reuse depends on that identity.

**Near miss, proxy improvement.** An editor shortens the instruction so the first move is easier to find, but deletes the visible stop condition. `FirstMoveRecoverability` rises to `2` while `HazardBoundaryVisibility` falls to `0`. The author must not add or average those ordinal values and call the rewrite better. The protected safety trade-off has been lost, so the pattern returns `repair` and the accepted specification must be reopened if its current status rule would reward that rewrite.

**Show, pattern-quality evaluation.** `E.21` is an evaluation for one FPF pattern version. Its publication form must still open with the working question "is this pattern good enough for the declared use?" before showing coordinates such as first-action recoverability, boundary fit, and SoTA binding.

**Show, local rubric that should not become an FPF pattern.** A project team defines a temporary rubric for choosing a meeting room. The `A.19.ECS` specification may be adequate locally, but no durable FPF pattern is needed because the evaluated object kind and use do not recur across FPF practice.

**Show, object-kind boundary.** A nuclear-plant evaluation can judge nuclear plants and declared comparable power-generation alternatives. A chair or FPF pattern is outside that evaluated-object kind: before the evaluation is opened, select a suitable evaluation; after a forced invocation, record an object-kind-fit defect/value rather than treating it as a weak nuclear plant or skipping declared coordinates. The pattern publication form must show that boundary before readers try to use the coordinate table.

