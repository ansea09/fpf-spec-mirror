---
chunk_kind: "child"
pattern_id: "A.1.1"
pattern_title: "U.BoundedContext Semantic Frame"
section_id: "A.1.1:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.1/A.1.1__007_archetypal-grounding.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "A.1.1 — U.BoundedContext Semantic Frame"
  - "A.1.1:5 — Archetypal Grounding"
line_start: 1840
line_end: 1880
dependencies:
  - "A.1"
  - "A.15"
  - "A.6.5"
  - "C.2.1"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.D1"
  - "E.24"
  - "E.24.PUB"
  - "F.0.1"
  - "F.18"
  - "F.9"
  - "U.Holon"
keywords:
---

### A.1.1:5 - Archetypal Grounding

#### A.1.1:5.1 - Hospital Operating Room Context

`Hospital.OR_2025` is a bounded context for operating-room work in a named hospital edition.

```text
BoundedContextSlotRelation:
  contextIdentity: Hospital.OR_2025
  contextBoundary: operating-room policy and procedure edition for 2025
  localVocabulary: case, sterile field, time-out, circulating nurse, independent auditor
  localInvariantSet: time-out required before incision; surgeon and independent auditor roles incompatible for one case
  localRoleTaxonomy: SurgeonRole, ScrubNurseRole, CirculatingNurseRole, IndependentAuditorRole
  bridgeRelationSet: billing-code bridge, hospital-wide staffing bridge
```

The context does not perform surgery. Systems in roles perform work. The context defines the local meanings and constraints under which those role assignments and work claims are interpreted.

#### A.1.1:5.2 - Special Relativity Context

`Theory.SpecialRelativity.SelectedEdition` is a bounded context for a selected episteme tradition.

```text
BoundedContextSlotRelation:
  contextIdentity: Theory.SpecialRelativity.SelectedEdition
  contextBoundary: selected postulates, vocabulary, reference schemes, and admissible derivations
  localVocabulary: inertial frame, proper time, Lorentz transformation
  localInvariantSet: constant light speed postulate; covariance constraints
  localRoleTaxonomy: not current for theory claims
  localEpistemeUseAndStatusRelationSet: postulate-status relation; evidence-use relation; derived-claim status relation
  bridgeRelationSet: bridge to Newtonian mechanics under low-speed approximation; bridge to general relativity under selected assumptions
```

The context frames meaning. It does not make the theory true by itself and does not act. Systems in roles publish, teach, test, or revise epistemes that use this context.

#### A.1.1:5.3 - FPF Pattern Quality Context

`FPF.PatternQuality.E21` is a bounded context for evaluating FPF pattern quality. Terms such as "recognition text", "assurance text", "semio-bias resistance", and "first-use affordability" have local meanings. A different context may use "quality" for product reliability, manufacturing yield, safety assurance, or service satisfaction.

Cross-context reuse of a quality term requires a bridge relation. Spelling alone does not carry the meaning.

