---
chunk_kind: "child"
pattern_id: "C.2.1"
pattern_title: "U.Episteme — Epistemes and their slot graph"
section_id: "C.2.1:8"
section_title: "Alignment with E.17. (Multi‑View Describing & Publication)  (normative)*"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.1/C.2.1__009_alignment-with-e-17-multi-view-describing-publication-normative.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "C.2.1 — U.Episteme — Epistemes and their slot graph"
  - "C.2.1:8 — Alignment with E.17. (Multi‑View Describing & Publication)  (normative)*"
line_start: 33519
line_end: 33572
dependencies:
  - "A.1"
  - "A.6.2"
  - "A.6.4"
  - "A.6.5"
  - "B.1.3"
  - "C.2"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.2"
  - "U.EffectFreeEpistemicMorphing"
  - "U.EpistemicRetargeting"
  - "U.EpistemicViewing"
  - "U.MultiViewDescribing"
  - "U.RelationSlotDiscipline"
keywords:
  - "ClaimGraphSlot"
  - "DescribedEntitySlot"
  - "EpistemeSlotGraph"
  - "GroundingHolonSlot"
  - "ReferenceScheme"
  - "RepresentationScheme"
  - "Viewpoint and View"
  - "ViewpointSlot"
  - "episteme"
---

### C.2.1:8 - Alignment with E.17.* (Multi‑View Describing & Publication)  *(normative)*

`U.EpistemeSlotGraph` underpins the E.17 cluster:
* E.17.0 `U.MultiViewDescribing`
* E.17.1 `U.ViewpointBundleLibrary`
* E.17.2 `TEVB — Typical Engineering Viewpoints Bundle`
* E.17 `MVPK — Multi‑View Publication Kit`

#### C.2.1:8.1 - Multi‑View Describing (E.17.0)

`U.MultiViewDescribing` organises **families of descriptions/specifications** over a shared entity‑of‑interest:
* The **EoIClass** parameter of E.17.0 is a species constraint on the ValueKind of `DescribedEntitySlot` (`EoIClass ⊑ U.Entity`).
* Each member of a multi‑view family is a `…Description`/`…Spec` episteme with:
  * `describedEntityRef` into that EoIClass,
  * `viewpointRef` drawn from a `U.ViewpointBundle`,
  * `subjectRef` decoding to DescriptionContext.

Within this pattern:
* `U.Viewpoint` is **exactly** the ValueKind of `ViewpointSlot` in C.2.1.
* `U.View` is `U.EpistemeView`, a species of `U.Episteme` whose `content` is already restricted to a particular `U.Viewpoint` and often also to a particular `U.RepresentationScheme`.

C.2.1 thus supplies the **per‑episteme** structure that E.17.0 rearranges into multi‑view families.

#### C.2.1:8.2 - Viewpoint bundles (E.17.1/E.17.2)

`U.ViewpointBundleLibrary` and TEVB specialise the `U.Viewpoint` node:
* A ViewpointBundle is a **set of `U.Viewpoint` instances** tailored to a class of DescribedEntities (e.g., holons in engineering contexts).
* TEVB fixes `EoIClass = U.Holon` (typically `U.System` or `U.Episteme`) and provides canonical engineering viewpoints: functional, structural, role‑enactor, interface‑oriented, etc.

From the C.2.1 perspective:

* these bundles populate the ValueKind of `ViewpointSlot`;
* engineering episteme species that want to be “TEVB‑aligned” must restrict `viewpointRef` to TEVB’s `EngineeringVPId` set, while keeping the same DescribedEntitySlot discipline.

#### C.2.1:8.3 - MVPK (E.17) as publication over C.2.1 views

MVPK treats `U.View` (i.e. `U.EpistemeView`) as its primary input:
* it uses `U.EpistemicViewing` species (A.6.3) to generate publication‑oriented views from engineering or logical views;
* it then publishes these `U.View` epistemes as `U.Surface` values with declared publication viewpoints and faces.

C.2.1’s distinction between:

* `U.Viewpoint` (intensional, epistemic perspective) and
* `U.PresentationCarrier` (carrier in C.2.1+ and L-SURF)

keeps **epistemic perspective and physical medium separate**:
* MVPK operates on `U.View` epistemes and then on carriers;
* the same View can be realised on multiple carriers without changing its describedEntity or ClaimGraph.

Any MVPK species that claims to be C.2.1‑conformant **MUST**:
* treat `U.View` as a `U.EpistemeView` with a valid C.2.1 core,
* document which C.2.1 slots it reads/writes (typically only representation/carrier‑related ones, leaving `DescribedEntitySlot` and `GroundingHolonSlot` untouched),
* refrain from introducing new claims about the described entity beyond what is in the source `U.View`’s ClaimGraph.

