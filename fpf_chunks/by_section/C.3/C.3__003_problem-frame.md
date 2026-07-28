---
chunk_kind: "child"
pattern_id: "C.3"
pattern_title: "Kinds, Intent and Extent, and Typed Reasoning"
section_id: "C.3:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3/C.3__003_problem-frame.md"
commit_sha: "17edd955485f60cafb16159c7d90e20f4ad21844"
heading_path:
  - "C.3 — Kinds, Intent and Extent, and Typed Reasoning"
  - "C.3:1 — Problem Frame"
line_start: 44286
line_end: 44291
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

### C.3:1 - Problem Frame

Across source ontologies, reference schemes, and project slices, "type" can mean ontology class, programming type, schema shape, category, source label, local kind, or public FPF U-kind. C.3 provides the smaller typed-reasoning architecture. A context-local `U.Kind` can be used now without being promoted to a durable public kind; its declared intent, candidate judgment, current extension representation, and the scope of any assertion remain separate objects.

Start with locality, not coordinates. If a typed claim crosses from one `U.BoundedContext` to another, check the source and target local kinds through C.3.3 even when both contexts cite the same reference-scheme edition or observationally equivalent slices: different authority, membership law, or institutional meaning can still change what counts. A C.3.3 `KindBridge` relates the exact source and target local kinds. When the crossing also changes local vocabulary or interpretation, an F.9 `Bridge` relates the corresponding `SenseCell`s; it does not map or change a `U.ReferenceScheme` as a whole. Within one context, a changed effective reference scheme identifies another `KindSignature` episteme edition, after which C.3.1 decides kind continuity. A `U.ContextSlice` only selects the classification and `KindExtension` evaluation; changing the slice alone creates neither a new semantic locality nor a bridge.

