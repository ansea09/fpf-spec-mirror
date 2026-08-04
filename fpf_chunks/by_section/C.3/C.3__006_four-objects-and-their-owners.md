---
chunk_kind: "child"
pattern_id: "C.3"
pattern_title: "Kinds, Intent and Extent, and Typed Reasoning"
section_id: "C.3:4"
section_title: "Four Objects and Their Owners"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3/C.3__006_four-objects-and-their-owners.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "C.3 — Kinds, Intent and Extent, and Typed Reasoning"
  - "C.3:4 — Four Objects and Their Owners"
line_start: 44617
line_end: 44629
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
  - "KindBridge"
  - "SubkindOf"
  - "bounded-context local kind"
  - "effective ReferenceScheme"
  - "intent-bearing KindSignature"
  - "optional slice-indexed extension"
  - "three-valued candidate judgment"
---

### C.3:4 - Four Objects and Their Owners

Keep these four objects separately recoverable:

| Object | Meaning | Direct owner |
| --- | --- | --- |
| context-local `U.Kind` and `U.SubkindOf` order | The kind value used by the typed-reasoning claim and its local partial order. | `C.3` and `C.3.1` |
| `KindSignature` | One `U.Signature` declaration episteme whose exact EntityOfConcern is the local kind and whose claim content declares the candidate `ValueKind`, criterion, slice conditions, reference scheme, assumptions, dependencies, formality, and any current `ExtentRule`. It is neither the kind nor another root U-kind. | `C.3.2`, `A.6.0`, and `C.2.1` |
| classification judgment | One evaluation for an exact candidate, local kind, signature edition, and context slice with result `true`, `false`, or `unknown`. It is not a direct relation occurrence by default. | `C.3.2` |
| `KindExtension(k, slice)` | An optional set-valued representation of the declared candidates whose judgment is `true` for the fixed signature edition and slice. | `C.3.2`, with `C.29` when the representation changes a claim-bearing use |

Scope is not a fifth part of the kind. A `KindSignature` episteme may carry its own `U.ClaimScope`, and a separate classification assertion carries the scope of that assertion. The `U.ContextSlice` is an explicit input to the judgment.

