---
chunk_kind: "child"
pattern_id: "C.37"
pattern_title: "Select and Use Representations for One Action"
section_id: "C.37:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.37/C.37__006_archetypal-grounding.md"
commit_sha: "6226816d8005a4c8ee3af338bb3752f6732449a9"
heading_path:
  - "C.37 — Select and Use Representations for One Action"
  - "C.37:5 — Archetypal Grounding"
line_start: 86379
line_end: 86409
dependencies:
  - "A.10"
  - "A.2.4"
  - "A.22"
  - "A.6.3.RT"
  - "C.11"
  - "C.13"
  - "C.2.1"
  - "C.2.P.DR"
  - "C.29"
  - "E.17.0"
  - "E.24.PUB"
keywords:
  - "co-use"
  - "diagram"
  - "exposure"
  - "loss"
  - "model"
  - "plan"
  - "receiving action"
  - "record"
  - "representation selection"
---

### C.37:5 - Archetypal Grounding

#### C.37:5.1 - Qualified premises for a bounded-trial decision

`MethodEngineer-ME1` must choose between keeping the current Method edition for Work item `WP4` and preparing and running a one-hour trial of `MethodChange-MC7`. The commissioning rule admits a proposal only when its estimated total time fits a three-hour budget. The current edition fits. MC7 requires an estimated four hours of preparation before the one-hour trial. Both figures charge the same time budget.

Under C.11 the result `CR7` is `choose now`: retain the current edition for WP4. The preparation estimate alone exceeds the ceiling. The planned hour gives the fuller estimate of five hours. This calculation settles eligibility under the stated planning rule. How long preparation would actually take remains unmeasured.

| Source considered | What the source supports | Use in this decision |
| --- | --- | --- |
| The commissioning rule, the setup estimate for MC7 and the estimate for retaining the current edition | The applicable ceiling and the estimated time required by each option under the trial conditions. | `select` for the budget comparison. Reopen it if the rule, estimate, alternatives or trial conditions change. |
| Trial item in `WorkPlan-WP4` | A.15.2 identifies a planned one-hour slot. A.10 path `P-WP4` supports that limited claim (`pass`). | `select` for estimating the full trial time. The four-hour setup estimate is already sufficient to exclude MC7. A claim that the trial took place would require a record of the Work. |
| Workflow diagram in `MethodDescription-MD5`, edition 5 | A.3.2 identifies the MethodDescription and its proposed order of work. Path `P-MD5` supports reading that order (`pass`). | `decline` as a premise for choosing on budget. The engineer can use the diagram to prepare an eligible trial. Revisit the estimate if a change of order changes the work it covers. |
| `WorkRecord-W19` about the earlier `Work-W19` | A.13 and A.15.1 establish the earlier assignments and Work. The record identified under C.2.1 reports rework in those conditions. Path `P-W19` supports that observation within its comparability limit (`degrade`). | `decline` for the budget comparison. The record explains why the change was proposed. It supplies neither the new setup estimate nor evidence that MC7 prevents the old breakdown. |

Raise the ceiling to five hours with the estimates unchanged. MC7 now meets the budget rule. If the engineer was asked only whether the trial fits, they can answer yes on the estimates. Choosing it over the current edition would require a reason to prefer it among the eligible options. To guarantee completion by the deadline, establish that every admissible duration meets it. To rule out timely completion, establish that every admissible duration exceeds it. A reliable upper bound at or below the deadline establishes the first claim. A lower bound strictly above it establishes the second. A five-hour upper bound against a three-hour limit leaves open the possibility of finishing sooner. An estimate alone settles neither claim.

#### C.37:5.2 - Failed diagram use

A release team receives a polished architecture diagram and wants to authorize deployment. E.24.PUB establishes that the diagram edition is available through a current carrier. C.2.P.DR repairs one route-shaped arrow that had been read as operational authority. Neither result establishes view conformance, a representation correspondence, runtime structure, evidence reliance, or deployment permission.

Until the needed direct subject result, reliance basis, and permission or gate result are available, the row is `unresolved`. Use A.10 when the source-to-use account remains implicit or must be replayable. Visual polish and provenance cannot upgrade it.

If the direct release gate or permission pattern instead returns a negative result because its required basis is absent, the row is `decline`; classification, publication, provenance, and repair facts cannot override that direct result.

#### C.37:5.3 - One decision now and a later reader's need

The engineer can finish the current comparison by giving the planning rule, the estimates and the resulting choice. The source of the four-hour estimate matters even though the workflow diagram and the earlier work record have identifiable editions. Neither supplies that estimate.

A later reviewer may need to reconstruct the choice. Give them the estimates used, what each covered, the budget in force and the alternatives compared. If they also need to reconstruct why MC7 was proposed, give them the earlier rework record and its comparability limit. Keep this basis once in the existing decision account when it can serve those uses.

