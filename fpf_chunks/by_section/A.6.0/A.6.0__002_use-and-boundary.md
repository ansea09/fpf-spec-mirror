---
chunk_kind: "child"
pattern_id: "A.6.0"
pattern_title: "U.Signature - Universal, law-governed declaration for a SubjectKind over a RangedValueKind"
section_id: "A.6.0:0"
section_title: "Use and boundary"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.0/A.6.0__002_use-and-boundary.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "A.6.0 — U.Signature - Universal, law-governed declaration for a SubjectKind over a RangedValueKind"
  - "A.6.0:0 — Use and boundary"
line_start: 9965
line_end: 9976
dependencies:
  - "A.2.6"
  - "A.6.1"
  - "A.6.5"
  - "D.CTX"
  - "E.10"
  - "E.10.D1"
  - "E.5.3"
  - "E.8"
  - "U.Mechanism"
  - "U.RelationSlotDiscipline"
keywords:
  - "RFC 2119"
  - "applicability"
  - "bounded context"
  - "laws"
  - "signature"
  - "vocabulary"
---

### A.6.0:0 - Use and boundary

Use this pattern when you need to publish or check a reusable `U.Signature` declaration for a theory, mechanism family, method family, discipline vocabulary, `U.Signature(profile=FormalSubstrate)`, or `PrincipleFrame`, and the current question is: what subject kind is declared, over what ranged value kind, with which vocabulary, laws, and applicability?

Do not use this pattern when the claim being made is that some implementation runs, a handler realizes an effect, a method is authorized for work, a gate has passed, evidence supports a result claim, a measurement is comparable, or a bridge preserves enough structure across contexts. Those claims use A.6.1, A.15, gate, evidence, characterization, normalization, bridge, or decision patterns after the signature declaration is stable.

First useful move: write the four-row Signature Block before writing examples or realizations: `SubjectBlock`, `Vocabulary`, `Laws`, `Applicability`. Then add a `SignatureManifest` only when another signature imports this one or downstream text depends on its exported symbols.

What goes wrong if missed: a project may treat implementation detail, tutorial prose, bridge policy, measurement comparability, or handler behavior as if it were part of the public declaration. That makes reuse brittle because downstream work cannot tell what law is being reused and what later realization merely happened to satisfy it.

What this buys: the same declaration shape can be reused for mechanisms, methods, disciplines, `U.Signature(profile=FormalSubstrate)` declarations, and principle frames, while realizations, measurements, bridges, and work authorization stay in their own governing patterns.

