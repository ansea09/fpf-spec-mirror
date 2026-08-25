---
chunk_kind: "child"
pattern_id: "C.3"
pattern_title: "Kinds, Intent and Extent, and Typed Reasoning"
section_id: "C.3:4"
section_title: "Four Objects and a Pre-judgment Check"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3/C.3__006_four-objects-and-a-pre-judgment-check.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "C.3 — Kinds, Intent and Extent, and Typed Reasoning"
  - "C.3:4 — Four Objects and a Pre-judgment Check"
line_start: 43536
line_end: 43550
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

### C.3:4 - Four Objects and a Pre-judgment Check

Keep these four objects separately recoverable:

| Object | Meaning | Subject pattern |
| --- | --- | --- |
| `U.Kind` individual and any `U.SubkindOf` facts | One intensional classification distinction, recovered through its candidate domain, operative membership condition, intended member/non-member boundary, and continuity rule. `U.SubkindOf` facts form a preorder; mutually obtaining facts state classification equivalence for the declared alignment and do not merge kind identities. | `C.3`, `C.3.1`, and accepted E.24.UK results for `U.Kind` and `U.SubkindOf` |
| `KindSignature` | One `U.Signature` declaration episteme whose exact EntityOfConcern is the kind and whose claim content declares candidate `ValueKind`, criterion, applicability, reference scheme, assumptions, dependencies, formality, and any current `ExtentRule`. | `C.3.2`, `A.6.0`, and `C.2.1` |
| classification judgment | One evaluation for an admissible exact candidate, kind, signature edition, and context slice with result `true`, `false`, or `unknown`. It is not a direct relation occurrence by default. | `C.3.2` |
| `KindExtension(k, slice)` | An optional set-valued representation of candidates whose admissible judgment is `true` for the fixed signature edition and slice. | `C.3.2`, with `C.29` when the representation changes a claim-bearing use |

Before the judgment, C.3.2 returns `admissible` or `not-applicable`. Candidate mismatch with the declared `ValueKind`, or a slice outside declared applicability, is `not-applicable` and no three-valued judgment is formed. Missing support or an unavailable dependency for an admissible candidate instead yields `unknown`.

Scope is not a fifth part of the kind. A `KindSignature` episteme may carry its own `U.ClaimScope`, and a separate classification assertion carries the scope of that assertion. The `U.ContextSlice` is an evaluation input.

