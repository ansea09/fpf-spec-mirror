---
chunk_kind: "child"
pattern_id: "C.3.2"
pattern_title: "Kind Intent, Membership Judgment, and Extension"
section_id: "C.3.2:4"
section_title: "Four Objects, Not One"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.2/C.3.2__006_four-objects-not-one.md"
commit_sha: "1eb56cd0cfd6dccad65143e03d28509373bd8dd5"
heading_path:
  - "C.3.2 — Kind Intent, Membership Judgment, and Extension"
  - "C.3.2:4 — Four Objects, Not One"
line_start: 44981
line_end: 44991
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
  - "C.3.5"
  - "C.3.A"
  - "E.24.UK"
keywords:
  - "KindExtension representation"
  - "KindSignature declaration episteme"
  - "candidate classification"
  - "local kind"
  - "true/false/unknown"
---

### C.3.2:4 - Four Objects, Not One

| Object | Meaning | Identity and owner |
| --- | --- | --- |
| local `U.Kind` and order | The context-local kind and any `U.SubkindOf` links used by typed reasoning. | C.3 and C.3.1; not this declaration or a public-kind admission. |
| `KindSignature` | A `U.Signature` declaration episteme whose exact `EntityOfConcern` is the local kind. | A.6.0 and C.2.1 govern the signature episteme and its editions. It is not the kind or another root U-kind. |
| classification judgment | One evaluation of the declared criterion for an exact candidate, kind, signature edition, and context slice, returning `true`, `false`, or `unknown`. | C.3.2; it is not a direct relation occurrence or claim-status value by default. |
| `KindExtension(k, slice)` | An optional set-valued representation of the declared candidate values whose judgment is `true` for the pinned signature edition and slice. | Local calculation unless the representation changes a claim-bearing use, when C.29 governs it. |

Scope is not a fifth object attached to the kind. A `KindSignature` episteme may have its own `U.ClaimScope`; a separate classification assertion has the scope of that assertion; and `U.ContextSlice` remains an explicit evaluation input.

