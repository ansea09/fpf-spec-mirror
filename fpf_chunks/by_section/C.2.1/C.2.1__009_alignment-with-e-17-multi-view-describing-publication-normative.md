---
chunk_kind: "child"
pattern_id: "C.2.1"
pattern_title: "U.Episteme - Epistemes and their slot relation"
section_id: "C.2.1:8"
section_title: "Alignment with E.17. (Multi‑View Describing & Publication)  (normative)*"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.1/C.2.1__009_alignment-with-e-17-multi-view-describing-publication-normative.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "C.2.1 — U.Episteme - Epistemes and their slot relation"
  - "C.2.1:8 — Alignment with E.17. (Multi‑View Describing & Publication)  (normative)*"
line_start: 35713
line_end: 35766
dependencies:
  - "A.1"
  - "A.6.2-A.6.4"
  - "A.6.5"
  - "A.7"
  - "B.1.3"
  - "C.2"
  - "E.10.D2"
  - "E.17"
  - "E.17.0-E.17.2"
  - "E.18"
keywords:
---

### C.2.1:8 - Alignment with E.17.* (Multi‑View Describing & Publication)  *(normative)*

`U.EpistemeSlotRelation` underpins the E.17 cluster:
* E.17.0 `U.MultiViewDescribing`
* E.17.1 `U.ViewpointBundleLibrary`
* E.17.2 `TEVB — Typical Engineering Viewpoints Bundle`
* E.17 `MVPK — Multi‑View Publication Kit`

#### C.2.1:8.1 - Multi‑View Describing (E.17.0)

`U.MultiViewDescribing` organises **families of Description epistemes and Description epistemes admitted for specification use** over a shared entity of concern:
* The **EntityOfConcernClass** parameter of E.17.0 is a species constraint on the ValueKind of `EntityOfConcernSlot` (`EntityOfConcernClass ⊑ U.Entity`).
* Each member of a multi‑view family is a `…Description`/`…Spec` episteme with:
  * `entityOfConcernRef` into that EntityOfConcernClass,
  * `viewpointRef` drawn from a `U.ViewpointBundle`,
  * `subjectRef` decoding to DescriptionContext.

Within this pattern:
* `U.Viewpoint` is **exactly** the ValueKind of `ViewpointSlot` in C.2.1.
* `U.View` is `U.EpistemeView`, a species of `U.Episteme` whose `content` is already restricted to a particular `U.Viewpoint` and often also to a particular `U.RepresentationScheme`.

C.2.1 thus supplies the **per‑episteme** structure that E.17.0 rearranges into multi‑view families.

#### C.2.1:8.2 - Viewpoint bundles (E.17.1/E.17.2)

`U.ViewpointBundleLibrary` and TEVB specialise the `U.Viewpoint` node:
* A ViewpointBundle is a **set of `U.Viewpoint` instances** tailored to a class of entities of concern (e.g., holons in engineering contexts).
* TEVB fixes `EntityOfConcernClass = U.Holon` (typically `U.System` or `U.Episteme`) and provides canonical engineering viewpoints: functional, structural, role‑enactor, interface‑oriented, etc.

From the C.2.1 perspective:

* these bundles populate the ValueKind of `ViewpointSlot`;
* engineering episteme species that want to be “TEVB‑aligned” must restrict `viewpointRef` to TEVB’s `EngineeringVPId` set, while keeping the same EntityOfConcernSlot discipline.

#### C.2.1:8.3 - MVPK (E.17) as publication over C.2.1 views

MVPK treats `U.View` (i.e. `U.EpistemeView`) as its primary input:
* it uses `U.EpistemicViewing` species (A.6.3) to generate publication‑oriented views from engineering or logical views;
* it then publishes these `U.View` epistemes through publication face/form values with declared publication viewpoints and faces.

C.2.1’s distinction between:

* `U.Viewpoint` (epistemic perspective specification) and
* `U.PresentationCarrier` (carrier in C.2.1+ and publication-face/form discipline)

keeps **epistemic perspective and physical medium separate**:
* MVPK operates on `U.View` epistemes and then on carriers;
* the same View can be realised on multiple carriers without changing its entityOfConcern or ClaimGraph.

Any MVPK species that claims to be C.2.1‑conformant **MUST**:
* treat `U.View` as a `U.EpistemeView` with a valid C.2.1 core,
* document which C.2.1 slots it reads/writes (typically only representation/carrier‑related ones, leaving `EntityOfConcernSlot` and `GroundingHolonSlot` untouched),
* refrain from introducing new claims about the EntityOfConcern value beyond what is in the source `U.View`’s ClaimGraph.

