---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "Static and Regression Conformance Harness for Unification"
section_id: "F.15:8"
section_title: "Static conformance rules for local material"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__010_static-conformance-rules-for-local-material.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "F.15 — Static and Regression Conformance Harness for Unification"
  - "F.15:8 — Static conformance rules for local material"
line_start: 86038
line_end: 86065
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "B.3"
  - "E.10.D1"
  - "E.10.D2"
  - "E.17"
  - "F.1"
  - "F.1-F.14"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
  - "U.BoundedContext"
  - "U.Role"
keywords:
  - "SenseCell testing"
  - "acceptance tests"
  - "regression tests"
  - "static checks"
  - "validation"
---

### F.15:8 - Static conformance rules for local material

All local rules stay inside one `U.BoundedContext`.

**SCR-F15-S1 (Context in view).**
`Seed sigma has context C -> C is among the slice contexts.`
Every harvested seed lives in a bounded context that is deliberately in view for this slice.

**SCR-F15-S2 (Attestation currentness).**
`Occurrence omega attests seed sigma -> omega states edition and locus.`
A Local-Sense can be reconstructed from attestations rather than from memory or a fashionable label.

**SCR-F15-S3 (In-context clustering).**
`Local-Sense lambda clusters seeds sigma_i -> every sigma_i belongs to context(lambda).`
No cross-context items are hidden inside one Local-Sense.

**SCR-F15-S4 (Two registers).**
`Local-Sense lambda -> Unified Tech label and Plain label both refer to lambda.`
The two labels differ in register, not in kind or sense.

**SCR-F15-S5 (Minimal gloss).**
`gloss(lambda) -> states only the needed local meaning.`
The gloss does not smuggle behavior, permission, evidence, source authority, publication status, or global sameness.

**SCR-F15-S6 (Context-local normal form).**
`normalize_C(sourceExpression) = n -> n is used only inside C unless F.9 or F.17 admits wider use.`
Normalization inside one context does not create a global name.

