---
chunk_kind: "child"
pattern_id: "E.17"
pattern_title: "Multi‑View Publication Kit"
section_id: "E.17:7"
section_title: "Objects used by the optional formal profile"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17/E.17__008_objects-used-by-the-optional-formal-profile.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "E.17 — Multi‑View Publication Kit"
  - "E.17:7 — Objects used by the optional formal profile"
line_start: 83136
line_end: 83148
dependencies:
  - "A.10"
  - "A.15.4"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.2"
  - "A.6.3"
  - "A.6.9"
  - "A.7"
  - "B.3"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "E.10"
  - "E.10.D2"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.17.AUD"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.24.PUB"
  - "E.8"
  - "F.9"
  - "F.9.1"
  - "U.View"
keywords:
---

### E.17:7 - Objects used by the optional formal profile

| Object or symbol | Function | Boundary |
|---|---|---|
| source episteme E | carries the selected claims about its EntityOfConcern | identified under C.2.1 |
| `publicationViewpointRef` (conditional) | resolves publication viewpoint episteme P only for a material `U.View` claim or viewpoint-dependent formal operation | designator and reference remain distinct from P |
| `F_face` | finite C.13 collection of publication-form designators for this profile | not a viewpoint bundle or `U.ViewFamily` |
| `Emit_s`, `FaceObj_s`, `FaceMorph_s`, `PromoteFace` | conceptual-form symbols for constructing and checking publication-form content | defined only in the representation-side formalism; no U-kind membership follows |
| receiving episteme, when separately constructed | its claims are checked against the source and, only for a material `U.View` claim, against P | A.6.3 construction and E.17.0 conformance are independent claims |
| publication occurrence, form, carrier | makes the selected episteme available to a declared audience and use | E.24.PUB identifies these participants and tests whether the publication relations obtain |

In the optional morphism profile, the author selects source E and publication-form profile `F_face`; P is selected only for a material `U.View` claim or a formal operation whose definition depends on that viewpoint. A system performs any authoring, rendering, checking, or publication work. MVPK names the publication method and constraints; it neither acts nor mints a view-family entity.

