---
chunk_kind: "child"
pattern_id: "C.3.2"
pattern_title: "Kind Intent, Membership Judgment, and Extension"
section_id: "C.3.2:4"
section_title: "Four Objects and One Applicability Result"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.2/C.3.2__006_four-objects-and-one-applicability-result.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "C.3.2 — Kind Intent, Membership Judgment, and Extension"
  - "C.3.2:4 — Four Objects and One Applicability Result"
line_start: 43866
line_end: 43878
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

### C.3.2:4 - Four Objects and One Applicability Result

| Object | Meaning | Identity and governor |
| --- | --- | --- |
| `U.Kind` individual and order | The intensional kind and any obtaining `U.SubkindOf` facts used by typed reasoning. | C.3 and C.3.1; not this declaration, a practice/source label, or a new public-kind admission. |
| `KindSignature` | A `U.Signature` declaration episteme whose exact `EntityOfConcern` is the kind. | A.6.0 and C.2.1 govern the episteme and its editions. |
| classification judgment | One evaluation for an admissible exact candidate, kind, signature edition, and slice, returning `true`, `false`, or `unknown`. | C.3.2; it is not a direct relation occurrence or guard result by default. |
| `KindExtension(k, slice)` | An optional set-valued representation of admissible candidates judged `true` for the pinned signature edition and slice. | Local calculation unless C.29 governs a claim-bearing use. |

`ClassificationAdmissibility(candidate, kind, signatureEdition, slice)` returns `admissible` or `not-applicable`. It is a precondition result, not another kind or membership value. `not-applicable` means the candidate fails the declared candidate `ValueKind`/interpretation or the slice falls outside signature applicability; no classification judgment is formed.

Scope is not attached to the kind. A `KindSignature` episteme may have its own `U.ClaimScope`; a separate classification assertion has the scope of that assertion; and `U.ContextSlice` remains an evaluation input.

