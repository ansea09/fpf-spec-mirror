---
chunk_kind: "child"
pattern_id: "C.3.2"
pattern_title: "Kind Intent, Membership Judgment, and Extension"
section_id: "C.3.2:5"
section_title: "KindSignature Declaration"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.2/C.3.2__007_kindsignature-declaration.md"
commit_sha: "5801dc610c657ac7b1efee349b18e80ce6d7df6f"
heading_path:
  - "C.3.2 — Kind Intent, Membership Judgment, and Extension"
  - "C.3.2:5 — KindSignature Declaration"
line_start: 43789
line_end: 43803
dependencies:
  - "A.14"
  - "A.2.6"
  - "A.6.0"
  - "C.2.1"
  - "C.2.3"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.3"
  - "C.3.4"
  - "E.24.UK"
keywords:
---

### C.3.2:5 - KindSignature Declaration

Author a reusable `KindSignature` only when a named receiving use needs the criterion and assumptions to persist across more than one classification. Its claim content declares:

- the exact kind that is its `EntityOfConcern`;
- the candidate `ValueKind` or exact value interpretation admitted as input;
- the membership condition in terms of directly governed candidate qualities, relations, constructive grounding, epistemes, registrations, certifications, publications, legal statuses, or other exact conditions;
- the exact `U.ContextSlice` applicability in which the evaluation may be formed;
- the effective `U.ReferenceScheme`;
- named assumptions, dependencies, standards, versions, units, and temporal policy;
- its `U.Formality`; and
- an optional `ExtentRule` for a named extension-consuming use.

In A.6.0 terms, `SubjectKind` is the broad candidate kind and `RangedValueKind` is `{true, false, unknown}`. `not-applicable` is returned before this ranged evaluation. `ExtentRule` is declaration content, not a new ontic relation. Formality characterizes the declaration episteme, not the kind, candidate, truth, or extension. A changed membership condition, candidate-domain declaration, `EntityOfConcern`, applicability, or effective scheme identifies another signature edition; C.3.1 separately decides kind continuity.

