---
chunk_kind: "child"
pattern_id: "C.3"
pattern_title: "Kinds, Intent and Extent, and Typed Reasoning"
section_id: "C.3:9"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3/C.3__011_conformance-checklist.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "C.3 — Kinds, Intent and Extent, and Typed Reasoning"
  - "C.3:9 — Conformance Checklist"
line_start: 44387
line_end: 44401
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

### C.3:9 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-C3-1` | The local `U.Kind` and any `U.SubkindOf` order remain distinct from durable FPF U-kind admission. |
| `CC-C3-2` | Kind, `KindSignature`, classification judgment, and optional `KindExtension` are separately recoverable; the effective reference scheme is claim content of the exact signature edition, not a property stored on the kind. |
| `CC-C3-3` | The judgment names an exact candidate, kind, signature edition, context slice, and one of `true`, `false`, or `unknown`. |
| `CC-C3-4` | Direct governed candidate features decide classification; evidence or representation does not create membership. |
| `CC-C3-5` | Missing evidence, unavailable dependency, and out-of-domain input yield `unknown`, not `false`. |
| `CC-C3-6` | Kind scope is absent; declaration and assertion scopes remain on their own epistemes, and `U.ContextSlice` remains an evaluation input. |
| `CC-C3-7` | An extension is a representation of true candidates, not `U.EntitySet`, A.14 `MemberOf`, a collection holon, or a direct relation occurrence. |
| `CC-C3-8` | Public `U.*` admission uses `E.24.UK`; cross-context kind use uses `C.3.3`. |
| `CC-C3-9` | `U.Work`, an exact `W : U.Work`, and any episteme about W remain distinct. |
| `CC-C3-10` | Bounded-context locality is the outer cross-context trigger: a shared scheme or equivalent slices do not remove it, while a scheme-edition or slice change inside one context does not create it. |

