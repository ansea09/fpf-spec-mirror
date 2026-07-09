---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
section_id: "E.17.1:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__013_relations.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "E.17.1 — U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
  - "E.17.1:12 — Relations"
line_start: 73440
line_end: 73448
dependencies:
  - "A.16.0"
  - "A.6.2-A.6.4"
  - "A.7"
  - "C.2.1"
  - "C.2.2a"
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.17.2"
  - "E.18"
  - "E.7"
  - "F.9"
  - "F.9.1"
  - "U.MultiViewDescribing"
keywords:
  - "alias discipline"
  - "engineering/management/research bundles"
  - "governance"
  - "import discipline"
  - "reusable viewpoint family"
  - "viewpoint bundle"
---

### E.17.1:12 - Relations
- **Builds on:** `C.2.1` slot discipline through `ViewpointSlot` / `ViewSlot`, `A.6.2-A.6.4`, `A.7`, `E.7`, and `E.10`.
- **Constrains:** `E.17.0 U.MultiViewDescribing` whenever it imports viewpoint families from reusable bundles.
- **Coordinates with:** `C.2.2a`, `A.16.0`, `E.17`, `E.17.2`, `E.18:5.12`, `F.9`, `F.9.1`, and any domain-specific viewpoint family that needs stable reuse.
- **Protects:** lexical and ontological separation between viewpoint families, concrete views, publication faces, and publication forms.
#### E.17.1:12.1 - Typed annex manifests for thin bundles

`VF.*` and other reusable viewpoint bundles may reference typed `AnnexManifestRef` assets with roles such as `lexical`, `bridge`, `movePublication`, `examples`, optional `sota`, and optional `pilotTrace`. This keeps the bundle itself thin while allowing A.16 move-publication notes, lexical baggage, and bridge annexes to remain explicit and typed rather than folded into the bundle core.

