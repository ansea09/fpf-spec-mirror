---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
section_id: "E.17.1:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__008_conformance-checklist.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "E.17.1 — U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
  - "E.17.1:7 — Conformance Checklist"
line_start: 62713
line_end: 62722
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

### E.17.1:7 - Conformance Checklist

- `CC-VBL-0` Within one library edition, each `ViewFamilyId` **SHALL** identify exactly one `U.ViewpointBundle`.
- `CC-VBL-1` Every viewpoint in a bundle **SHALL** have `EntityOfConcernClassSpec` compatible with the bundle's declared `EntityOfConcernClassSpec`.
- `CC-VBL-2` A `U.MultiViewDescribing` family that declares a `ViewFamilyId` **SHALL** import only viewpoints from the referenced bundle.
- `CC-VBL-3` `ViewFamilyId` **MUST NOT** be used as a `publication-face kind`, publication-face kind, or carrier kind.
- `CC-VBL-4` Bundles intended for non-expert reuse **SHOULD** provide archetypal grounding coverage for their viewpoints.
- `CC-VBL-5` Changes to bundle membership or meaning **SHALL** be editioned rather than silently mutating an existing family id.
- `CC-VBL-6` If a family combines several bundles, the contributing `ViewFamilyId` values **SHALL** remain explicit.

