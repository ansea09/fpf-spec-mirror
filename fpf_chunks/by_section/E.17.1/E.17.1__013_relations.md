---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
section_id: "E.17.1:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__013_relations.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "E.17.1 — U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
  - "E.17.1:12 — Relations"
line_start: 79640
line_end: 79650
dependencies:
  - "A.16.0"
  - "A.22"
  - "A.6.2-A.6.4"
  - "A.7"
  - "C.13"
  - "C.2.1"
  - "C.2.2a"
  - "C.29"
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.17.2"
  - "E.18"
  - "E.24.PUB"
  - "E.7"
  - "F.9"
  - "F.9.1"
keywords:
  - "alias discipline"
  - "engineering/management/research bundles"
  - "governance"
  - "import discipline"
  - "reusable viewpoint family"
  - "viewpoint bundle"
---

### E.17.1:12 - Relations

- **Builds on:** `C.2.1` for library and member-episteme identity; `E.17.0` for exact P membership, reference resolution, singular use selection, and sole E/P view-membership rule; `C.13` for explicit imported collections; `A.22` for any separately selected organization; `A.6.2-A.6.4` for optional episteme-construction histories; `A.7`, `E.7`, and `E.10` for carrier, authoring, and naming discipline; `E.24.PUB` for publication; and `C.29` for representation.
- **Constrains:** E.17.0 consumers whenever they import a reusable family; an import narrows eligible references but neither selects one P for a use nor proves conformance.
- **Coordinates with:** `C.2.2a`, `A.16.0`, `E.17`, `E.17.2`, `E.18:5.12`, `F.9`, `F.9.1`, and domain-specific families requiring stable reuse.
- **Protects:** exact separation among library edition, bundle edition, `ViewFamilyId`, `U.ViewpointRef`, P designator, P, candidate/View E, any A.22 structure, form, carrier, publication occurrence, and C.29 representation.

#### E.17.1:12.1 - Typed annex manifests for thin bundles

`VF.*` and other reusable viewpoint bundles may reference typed `AnnexManifestRef` assets with roles such as `lexical`, `bridge`, `movePublication`, `examples`, optional `sota`, and optional `pilotTrace`. This keeps the bundle itself thin while allowing A.16 move-publication notes, lexical baggage, and bridge annexes to remain explicit and typed rather than folded into the bundle core.

