---
chunk_kind: "child"
pattern_id: "E.17"
pattern_title: "Multi‑View Publication Kit"
section_id: "E.17:7"
section_title: "Objects used by the optional formal profile"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17/E.17__008_objects-used-by-the-optional-formal-profile.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "E.17 — Multi‑View Publication Kit"
  - "E.17:7 — Objects used by the optional formal profile"
line_start: 80658
line_end: 80670
dependencies:
  - "A.15.4"
  - "A.22"
  - "A.6.2"
  - "A.6.3"
  - "A.6.9"
  - "A.7"
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

| Object or symbol | Exact job | Boundary |
|---|---|---|
| source episteme E | carries the selected claims about exact EntityOfConcern | identified under C.2.1 |
| `publicationViewpointRef` | resolves exact publication viewpoint episteme P | designator and reference remain distinct from P |
| `F_face` | finite C.13 collection of face-use designators or descriptions for this profile | not a viewpoint bundle or `U.ViewFamily` |
| `Emit_s`, `FaceObj_s`, `FaceMorph_s`, `PromoteFace` | conceptual-form symbols for constructing and checking face content | governed as representation-side formalism; no U-kind membership follows |
| receiving face episteme, when constructed | separately identified episteme whose claims are checked against the source and P | A.6.3 construction and E.17.0 conformance are independent claims |
| publication occurrence, form, carrier | makes the selected episteme available to a declared audience and use | E.24.PUB owns identity and obtaining |

The author selects exact source E, exact P, and face profile `F_face`. A system performs any authoring, rendering, checking, or publication work. MVPK names the publication method and constraints; it neither acts nor mints a view-family entity.

