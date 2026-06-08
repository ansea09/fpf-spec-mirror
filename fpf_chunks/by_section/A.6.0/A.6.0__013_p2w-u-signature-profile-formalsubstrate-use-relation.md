---
chunk_kind: "child"
pattern_id: "A.6.0"
pattern_title: "U.Signature - Universal, law‑governed declaration for a SubjectKind on a BaseType"
section_id: "A.6.0:10a"
section_title: "P2W U.Signature(profile=FormalSubstrate) Use Relation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.0/A.6.0__013_p2w-u-signature-profile-formalsubstrate-use-relation.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "A.6.0 — U.Signature - Universal, law‑governed declaration for a SubjectKind on a BaseType"
  - "A.6.0:10a — P2W U.Signature(profile=FormalSubstrate) Use Relation"
line_start: 9139
line_end: 9157
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

### A.6.0:10a - P2W `U.Signature(profile=FormalSubstrate)` Use Relation

When `E.18.1` uses a first-principles or mathematical cue to select, declare, or cite a `U.Signature(profile=FormalSubstrate)` declaration, this pattern governs only that declaration: SubjectBlock, Vocabulary, Laws, Applicability, effect discipline, inference kinds, imported-symbol dependencies, and the no-realization pin. `E.18.1` may carry the cue and select the next admissible relation. `C.29` governs whether a mathematical-lens use is admissible for the stated use.

#### A.6.0:10a.1 - `profile=FormalSubstrate` signature, mathematical object, and lens-use slot discipline

Do not decide whether source wording names a `U.Signature(profile=FormalSubstrate)` declaration, a general `U.Signature` declaration, or a mathematical-lens use by lexical replacement. Decide which relation position is live. The same mathematical object, formalism, or family may fill more than one relation position, but the position changes the admissible claim.

| Live relation position | Governing pattern | Required recovery | Non-admissible overread |
|---|---|---|---|
| `U.Signature(profile=FormalSubstrate)` declaration | `A.6.0` | `U.Signature(profile=FormalSubstrate)` with SubjectBlock, Vocabulary, Laws, Applicability, effect discipline, inference kinds, imports and provides, and no-realization pin. | The declaration is not a mechanism, empirical identity claim, evidence proof, work authorization, gate passage, or mathematical-lens use result. |
| Mathematical-lens use | `C.29` | Candidate mathematical object or formalism, mapping mode, preserved structure, lost structure, visible payoff, admissible use, non-admissible use, and stop condition. | Lens-use adequacy does not declare the signature profile and does not settle handler semantics, mechanism realization, empirical truth, evidence, work, gate, or decision authority. |
| Mechanism consumption or realization | `A.6.1` and downstream mechanism patterns | A mechanism cites the signature by import or reference, publishes operation algebra, law set, admissibility conditions, transport, and any monotone realization relation when that relation is being made. | A mechanism does not rewrite the imported signature laws by use, and a realization does not become a new `U.Signature(profile=FormalSubstrate)` declaration unless a new signature is declared. |
| P2W carry-through cue | `E.18.1` | Source cue, carried distinction, live next relation, selected application, stop condition, and any return trigger. | P2W does not mint `U.SubstrateFormalization`, does not decide mathematical-lens admissibility, and does not replace A.6.0 or C.29. |

Old or source-local wording such as `SubstrateFormalization` recovers as a move to author, select, or cite a `U.Signature(profile=FormalSubstrate)` unless the claim being made is actually a `C.29` mathematical-lens use, an `A.6.1` mechanism relation, or another neighboring relation. In slot terms, the mathematical object can fill a `CandidateMathObject` position in `C.29`, a vocabulary or law position in a `U.Signature(profile=FormalSubstrate)` declaration, or an imported-signature position in a mechanism. Those are relation positions, not separate object kinds and not `U.Role`s.

The Rodin-style lesson used here is constructive rather than slogan-like: formal languages, axioms, rules, and mathematical objects help model a world-facing or episteme-facing EntityOfConcern only when their representational and operational limits are declared. A.6.0 therefore stores the formal-deductive declaration. C.29 stores the declared use of a mathematical lens. A.6.1, bridge, measurement, evidence, work, gate, and decision patterns store the later relations that apply, test, authorize, or use that declaration.

