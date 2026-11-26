---
chunk_kind: "child"
pattern_id: "C.3.1"
pattern_title: "Kind Identity and Subkind Relations (U.Kind and U.SubkindOf)"
section_id: "C.3.1:7"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.1/C.3.1__009_archetypal-grounding.md"
commit_sha: "9d38fbfe4ce5b72d8fe05e839cbca0025a5b31cf"
heading_path:
  - "C.3.1 — Kind Identity and Subkind Relations (U.Kind and U.SubkindOf)"
  - "C.3.1:7 — Archetypal Grounding"
line_start: 58004
line_end: 58018
dependencies:
  - "A.1"
  - "A.11"
  - "A.2"
  - "A.2.6"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "A.8"
  - "C.2.1"
  - "C.2.3"
  - "C.29"
  - "C.3"
  - "C.3.2"
  - "C.3.3"
  - "E.24.UK"
  - "F.5"
  - "F.8"
keywords:
  - "U.SubkindOf direct relation"
  - "classification equivalence"
  - "closed finite domain"
  - "continuity"
  - "criterion entailment"
  - "kind identity"
  - "membership criterion"
  - "participant-determined occurrence"
  - "preorder"
---

### C.3.1:7 - Archetypal Grounding

| Situation | C.3.1 move | Boundary |
| --- | --- | --- |
| `CoolingPumpKind` is below `PumpKind`. | Use criterion entailment: the cooling-pump condition already requires the governed pump condition. State the readable relation and its applicability. | Do not infer a public `U.CoolingPump`, and do not use current extension rows as the truth-maker. |
| A closed cabinet inventory contains five cabinets. Four satisfy both criteria. For the fifth, the narrower judgement is `unknown` and the broader is `false`. | Inclusion on this inventory is still open. If the fifth satisfies the narrower criterion it is a counterexample. Establish its narrower classification or use a valid criterion-entailment argument. | An unresolved narrower judgement in a cabinet already known to meet the broader criterion could not conceal that counterexample. Even a settled result for the five cabinets covers only this lot. |
| The shift qualification register and the union register identify the same people on a complete current roster. | Once the identities, register meanings and completeness for this roster are established, the equality gives inclusion in both directions there. | Qualification depends on the shift credential and union membership on enrollment. A later enrollment can change the agreement while both kinds retain their criteria. |
| A signature adds an aligned unit conversion. | Apply section 6, keep the kind, identify the new signature edition, and retain edition-specific judgments. | Do not rewrite earlier judgments as if the new edition had been used. |
| A signature changes from physical cooling performance to a schema label. | The boundary probes expose a changed candidate domain and discriminator; identify another kind. | Do not hide the mismatch by editing the extension. |
| Pump #14 changes state in a later plant slice. | Re-evaluate the admissible candidate and allow the extension to change. | Candidate-state change alone does not create a kind, signature, or relation occurrence. |
| `InspectionWorkKind` is used locally. | Classify only an independently identified `W : U.Work`. | `U.Work`, a plan, or a log row cannot occupy W's candidate position. |
| `WorkPlan` depends on Work. | Use the governing work or E.24.UK relation. | Do not encode dependency as `U.SubkindOf`. |
| `SafetyCriticalFunctionKind` is proposed as a subkind of `FunctionKind`. | First recover both function senses under A.6.F, then use exact criterion entailment or the deliberately closed-domain branch. | The word *function*, a risk label, or current examples establish neither the kinds nor the subkind fact; another public `U.*` name requires E.24.UK. |
| A project proposes public `U.CoolingPump`. | Take the recovered kind to `E.24.UK`, then apply naming patterns if admitted. | Local typed use and `U.SubkindOf` do not admit or publish another durable kind. |

