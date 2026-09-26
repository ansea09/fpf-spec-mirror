---
chunk_kind: "child"
pattern_id: "A.6.A"
pattern_title: "Affordance and Action-Invitation Precision Restoration (ACT-INV)"
section_id: "A.6.A:11"
section_title: "SoTA-Echoing — choose wording recovery or a domain form by the receiving task"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.A/A.6.A__012_sota-echoing-choose-wording-recovery-or-a-domain-form-by-the-receiving-task.md"
commit_sha: "7bba05916e6e8ad42f868ed3aad0a7644fe0c354"
heading_path:
  - "A.6.A — Affordance and Action-Invitation Precision Restoration (ACT-INV)"
  - "A.6.A:11 — SoTA-Echoing — choose wording recovery or a domain form by the receiving task"
line_start: 19794
line_end: 19818
dependencies:
  - "A.15"
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.3"
  - "A.6.B"
  - "A.6.P"
  - "A.6.REL"
  - "A.7"
  - "B.4.1"
  - "B.5.2.0"
  - "C.16.Q"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "F.17"
  - "F.18"
  - "F.9"
keywords:
  - "action-first language"
  - "affordance"
  - "detection"
  - "inquiry question"
  - "physical opportunity"
  - "wording recovery"
---

### A.6.A:11 - SoTA-Echoing — choose wording recovery or a domain form by the receiving task

**Practice question.** For §5.2's “This handle affords pulling,” should the receiver first recover the supported claim or directly produce a domain-specific action representation? The selected answer for ambiguous documentation is §4.0a's six-step recovery, stopping at the useful statement, inquiry or missing basis. The serious alternative is to apply the source's established interpretation and manipulation method directly. **Adopt** that shorter route when the intended meaning and receiving interface are already settled. **Reject** choosing an operational form merely because the sentence contains “affords.”

[ReKep, PMLR 270 (2025)](https://proceedings.mlr.press/v270/huang25g.html) supplies a concrete form-and-method alternative: language instructions and RGB-D observations can be converted into constraints over 3D keypoints, then used in optimization for robot actions. It is a serious alternative for an actual manipulation task, not a proposed general theory of wording. **Adapt** its explicit interface demand to the last branch in §5.2: use the representation when the receiver needs that plan and has the required inputs. Its manipulation results do not establish the truth of this pattern's handle claim or validate the six-step recovery.

Compare one author pass over the same supplied handle case and receiving question; do not compare that pass with a robot experiment or count absent observations as free inputs:

| Receiving task and available basis | Direct source-specific method or form | Recovery-first choice and accepted cost |
| --- | --- | --- |
| Explain whether the supplied R2/G1/CP3 names support pulling; the physical rule and readings are absent. | A domain expert can immediately name the missing physical grounds. Attempting a manipulation representation requires additional observations and still leaves that evidential question to its domain rule. | §5.2 returns the bounded question and missing grounds. The six steps add interpretation work for a reader who has not yet distinguished opportunity, detection and command; no speed advantage over the informed expert is claimed. |
| Produce actions from an already understood instruction, with the domain method and required observations available. | Apply the method's representation and planning procedure directly. | Reuse the established interpretation and continue to that method. Another recovery note has no required role. The ordinary sentence alone does not deliver the executable plan. |
| Explain differing detections with physical handle facts held fixed, as in §5.3. | A manipulation-command form serves a different output; a source-specific inquiry method is suitable if it preserves that question. | Return the detector question first, then use an inquiry method only if further construction is needed. This avoids silently replacing inquiry with a movement target. |

This is a **local inference** about the stated tasks, supplied information and required outputs. It motivates §4.0a steps 1/5/6, the optional forms in §4.5, and the explicit domain-method continuation in §5.2. It establishes neither a robot effect nor a measured reduction in author effort. The deliberate trade-off is some interpretive work before committing to a form, with that work omitted when an adequate interpretation already exists.

The supporting sources constrain different claims:

* **Hansen (2024), §2**, distinguishes action possibilities from obligations and allows possibilities to escape immediate perception. **Adopt** those distinctions for the physical case; his account of perception supplies no universal ontology for metaphorical invitations. ([Frontiers][1])
* **Vauclin and colleagues (2023)** review attunement and action calibration in human person-plus-object systems. **Adapt** the distinction to the question about changed detection versus changed capabilities or physical conditions. The human findings do not establish the robot case; its physical rule and evidence remain necessary. ([Springer][2])
* **Pezzulo and colleagues**, in *Neural representation in active inference*, distinguish roles of generative models in action-perception, planning and imagination. **Adapt** that distinction when recovering a model-side claim from “the model wants”; the model tendency establishes no duty, explicit rationale or performed Work. ([UCL Discovery][3])
* **MOKA (2024)** supplies a compact point-based interface between image predictions and robot manipulation. **Adopt** the principle of an intermediate form with an actual receiver. Its robot-interface use neither makes such a form compulsory for an inquiry nor provides one obtaining predicate for every invitation. ([Robotics: Science and Systems][4])

Reopen the affected recovery when a source-specific meaning or physical criterion changes the supported interpretation, when new observations answer the named gap, or when the receiver now needs an executable interface. Recompare the method if a serious alternative preserves these distinctions with less required work. A new source's date, another field in a record, or shared terminology alone changes none of those conditions.

