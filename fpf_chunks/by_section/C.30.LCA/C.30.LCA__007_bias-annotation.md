---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__007_bias-annotation.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:6 — Bias-Annotation"
line_start: 62160
line_end: 62168
dependencies:
  - "A.10"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.3.3"
  - "B.2.5"
  - "B.3"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "E.17.0"
  - "E.18"
  - "G.6"
keywords:
  - "control layer"
  - "control-structure view"
  - "controller and plant"
  - "layered control architecture"
  - "proof overread"
  - "rate band"
  - "supervisor loop"
---

### C.30.LCA:6 - Bias-Annotation

* **Diagram authority bias.** A neat feedback diagram can look more persuasive than the structure, source-to-use path, work-reliance relation, or claim it actually supports. Repair by naming each object or relation and the pattern used to state or test the claim.
* **Stratification-label bias.** A `layer`, `level`, `tier`, or `stack` label can hide whether it names a control relation, rate band, aggregation, scale, organization, Work scope, evidence scope, deployment, or publication section. Repair with `C.30.STRAT`; C.30.LCA applies only to the recovered control-specific case.
* **Supervisor anthropomorphism.** A supervisor label can make an episteme, policy, assignment, or dashboard sound agentive. Repair by recovering the supervision relation first. If action is claimed, name the performer System, dated Work, enacted Method, assignment occurrence and its declared species, and F.6 attribution; recover authority, responsibility, gate, safety, and evidence separately.
* **Transformation-flow and LCA conflation.** A transformation-flow graph expression and a control description/view can inform each other, but neither replaces the other. Repair by naming the exact EntityOfConcern, structure kind, and direct relations for each.

This checklist verifies the preceding guidance after the practitioner has chosen the selected repair action; it is not a required project control form and not a substitute for the note, description episteme, conformance occurrence, direct control relation, or repair guidance above.

