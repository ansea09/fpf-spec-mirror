---
chunk_kind: "child"
pattern_id: "C.3"
pattern_title: "Kinds, Intent and Extent, and Typed Reasoning"
section_id: "C.3:9"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3/C.3__011_conformance-checklist.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "C.3 — Kinds, Intent and Extent, and Typed Reasoning"
  - "C.3:9 — Conformance Checklist"
line_start: 43768
line_end: 43781
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
  - "C.3.5"
  - "C.3.A"
  - "E.24.UK"
  - "F.18"
  - "F.8"
keywords:
  - "classification"
  - "extension"
  - "intension"
  - "kind"
  - "subkind"
  - "type"
  - "typed reasoning"
  - "vocabulary"
---

### C.3:9 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-C3-1` | The local `U.Kind` and any `U.SubkindOf` order remain distinct from durable FPF U-kind admission. |
| `CC-C3-2` | Kind, `KindSignature`, classification judgment, and optional `KindExtension` are separately recoverable. |
| `CC-C3-3` | The judgment names an exact candidate, kind, signature edition, context slice, and one of `true`, `false`, or `unknown`. |
| `CC-C3-4` | Direct governed candidate features decide classification; evidence or representation does not create membership. |
| `CC-C3-5` | Missing evidence, unavailable dependency, and out-of-domain input yield `unknown`, not `false`. |
| `CC-C3-6` | Kind scope is absent; declaration and assertion scopes remain on their own epistemes, and `U.ContextSlice` remains an evaluation input. |
| `CC-C3-7` | An extension is a representation of true candidates, not `U.EntitySet`, A.14 `MemberOf`, a collection holon, or a direct relation occurrence. |
| `CC-C3-8` | Public `U.*` admission uses `E.24.UK`; cross-context kind use uses `C.3.3`. |
| `CC-C3-9` | `U.Work`, an exact `W : U.Work`, and any episteme about W remain distinct. |

