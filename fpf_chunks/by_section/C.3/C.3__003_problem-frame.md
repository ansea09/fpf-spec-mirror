---
chunk_kind: "child"
pattern_id: "C.3"
pattern_title: "Kinds, Intent and Extent, and Typed Reasoning"
section_id: "C.3:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3/C.3__003_problem-frame.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "C.3 — Kinds, Intent and Extent, and Typed Reasoning"
  - "C.3:1 — Problem Frame"
line_start: 44549
line_end: 44554
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

Across source ontologies, reference schemes, and project slices, “type” can mean ontology class, programming type, schema shape, category, source label, local kind, or public FPF U-kind. C.3 provides the smaller typed-reasoning architecture. A locally constituted `U.Kind` can be used now without being promoted to a durable public kind; its identity basis, declared intent, candidate judgment, current extension representation, and the scope of any assertion remain separate objects.

Start with the local identity basis, not coordinates. If a typed claim crosses from one named practice or source boundary to another, check the exact source and target kinds through C.3.3 even when both uses cite the same reference-scheme edition or observationally equivalent slices: a different constituting practice, membership law, or institutional meaning can still change what counts. A C.3.3 `KindBridge` relates the exact source and target kinds. When the crossing also changes local wording or interpretation, an F.9 relation connects the corresponding F.17 cells; it does not map or change a `U.ReferenceScheme` as a whole. Within one local boundary, a changed effective scheme identifies another `KindSignature` episteme edition, after which the C.3.1 continuity test determines whether the same local kind continues. A `U.ContextSlice` only selects the classification and `KindExtension` evaluation; changing the slice alone creates neither a new local kind identity nor a bridge.

