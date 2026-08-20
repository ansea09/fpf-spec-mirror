---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.SystemRoleAssignment - Contextual System-Role Assignment"
section_id: "A.2.1:6"
section_title: "Bias Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__008_bias-annotation.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "A.2.1 — U.SystemRoleAssignment - Contextual System-Role Assignment"
  - "A.2.1:6 — Bias Annotation"
line_start: 3374
line_end: 3386
dependencies:
  - "A.1.1"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.3"
  - "A.6.5"
  - "A.6.9"
  - "A.6.REL"
  - "C.2.1"
  - "C.27"
  - "C.27.TA"
  - "C.3.3"
  - "F.6"
  - "F.9"
keywords:
  - "assignment predicate"
  - "direct assignment species"
  - "holder System"
  - "identity"
  - "maximal interval"
  - "performedUnderAssignment"
  - "system-role kind"
---

### A.2.1:6 - Bias Annotation

| Bias risk | Failure | Repair |
| --- | --- | --- |
| Record-first bias | A roster row or identifier is treated as the assignment occurrence. | State the species predicate and uninterrupted occurrence identity; keep the row as an assertion or publication. |
| Universal-signature bias | One broad root signature hides several participant laws. | Admit direct species with exact local domains and real participants. |
| Generic-duplicate bias | A stronger appointment is accompanied by a weaker assignment occurrence. | Let the specialized occurrence itself satisfy `U.SystemRoleAssignment` and use its common holder projection. |
| Universal-context bias | Every assignment receives a context or optional model-use participant. | Keep context-denoted objects in their direct relation; declare a required participant only in a genuinely dependent species. |
| Assignment-as-classification drift | Assignment is used as proof of kind membership. | Evaluate the C.3.2 judgment; use assignment only if the signature names its independently obtaining predicate. |
| Assignment-as-Work drift | Current assignment is treated as completed Work. | Name `W : U.Work`, exact `RA`, and `performedUnderAssignment(W, RA)`. |
| Episteme-as-holder drift | A standard, report, model, or dataset fills `HolderSystemSlot`. | Keep the episteme in its evidence, reliance, external-rule, source-use, or publication relation. |
| Responsibility or authority drift | The kind or assignment is treated as the responsibility or authority result. | Cite the direct admitted predicate and actual bearer, or return `missing-governor`. |

