---
chunk_kind: "child"
pattern_id: "C.3"
pattern_title: "Kinds, Intent and Extent, and Typed Reasoning"
section_id: "C.3:5"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3/C.3__007_solution.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "C.3 — Kinds, Intent and Extent, and Typed Reasoning"
  - "C.3:5 — Solution"
line_start: 43366
line_end: 43379
dependencies:
  - "A.1"
  - "A.11"
  - "A.2.6"
  - "A.22.CGUS"
  - "A.6.0"
  - "A.7.1"
  - "A.8"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.2"
  - "C.3.3"
  - "C.3.5"
  - "C.3.A"
  - "E.24.UK"
  - "F.18"
  - "F.8"
  - "F.9"
keywords:
  - "KindSignature"
  - "SubkindOf preorder"
  - "admissibility"
  - "admitted U.Kind individual"
  - "distinct-kind KindBridge"
  - "membership distinction"
  - "optional extension"
  - "true/false/unknown judgment"
---

### C.3:5 - Solution

Use the lightest object that answers the current typed-reasoning question.

1. **Recover the kind.** Name the candidate domain and the operative membership distinction: what an intended member must satisfy and what separates a relevant non-member. Record the continuity rule used when that distinction changes. Keep practice/source provenance as a cue to compare definitions, not as an automatic identity key. Do not store the current use, ClaimScope, context slice, or reference scheme on the kind.
2. **Use C.3.1 for subkind and continuity.** A `U.SubkindOf` fact obtains through exact criterion entailment under an aligned interpretation or through exhaustive evaluation over a deliberately closed finite domain. The facts form a preorder. Opposite facts between distinct kinds may express classification equivalence for that applicability; a consumer may order the resulting equivalence groups without identifying the kinds.
3. **Use C.3.2 for declaration and admissible judgment.** A repeated condition may justify a `KindSignature`. First check candidate `ValueKind` and applicability. Only an admissible application returns `true`, `false`, or `unknown`.
4. **Let the governed criterion condition decide.** A direct quality, relation, construction, episteme, registration, certification, publication occurrence, legal status, or other governed condition makes the criterion hold when the criterion actually names it. An observation, record, or source used merely as evidence does not constitute an independently governed condition. Use each condition's direct pattern.
5. **Keep four outcomes distinct.** `not-applicable` means the judgment should not be formed. For an admissible candidate, a satisfied criterion gives `true`, a known failed criterion gives `false`, and missing support or an unavailable required dependency gives `unknown`. A guard may decline use without rewriting any of these results.
6. **Materialize an extension only for use.** A query, quantification, comparison, or review may need `KindExtension(k, slice)`. It represents admissible candidates judged `true`; notation, rows, or set membership do not create an ontic collection or classification relation.
7. **Keep scope, formality, Work, and publication separate.** Formality characterizes the declaration episteme. Scope belongs to claims or capabilities. `U.Work` is a kind and `W : U.Work` is one independently grounded dated work occurrence. Plans, logs, cards, field bundles, carriers, and rows remain their own objects.

Typed reasoning composes with F-G-R and USM in this order: recover kind compatibility; check classification admissibility and, when admissible, the exact judgment; separately check claim-scope coverage; then apply support, assurance, freshness, and any justified bridge consequence required by the receiver.

