---
chunk_kind: "child"
pattern_id: "A.2.4"
pattern_title: "Episteme Evidence-Use and Status-Use Relations"
section_id: "A.2.4:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.4/A.2.4__007_bias-annotation.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "A.2.4 — Episteme Evidence-Use and Status-Use Relations"
  - "A.2.4:6 — Bias-Annotation"
line_start: 3771
line_end: 3783
dependencies:
  - "A.10"
  - "A.2"
  - "A.2.1"
  - "A.2.4"
  - "A.6.5"
  - "B.3"
  - "C.2.1"
  - "C.28"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.2"
  - "E.17.EFP"
  - "F.10"
  - "G.6"
  - "U.Role"
  - "U.RoleAssignment"
keywords:
  - "claim"
  - "episteme"
  - "evidence-use"
  - "provenance"
  - "source-use"
  - "status-use"
---

### A.2.4:6 - Bias-Annotation

This pattern mainly blocks six biases:

* **episteme-as-role-holder bias**: an episteme is placed in `U.RoleAssignment` because it is useful as evidence or status;
* **evidence-name-as-kind bias**: local evidence-use labels become `U.Role` names;
* **status-display-as-authority bias**: a visible badge or status cell becomes gate passage, permission, or assurance;
* **work-as-evidence-use collapse**: producing work, produced episteme, and later evidence use are treated as one relation;
* **scope-free evidence bias**: target claim, grounding holon, claim scope, polarity, time, assurance use, or provenance constraints are omitted;
* **causal laundering bias**: causal evidence classes are changed by source vocabulary rather than by `C.28` causal-use reasoning.

The repair is to recover the episteme first, then recover the evidence-use, status-use, source-use, publication-use, assurance-use, or causal-use relation that is current.

