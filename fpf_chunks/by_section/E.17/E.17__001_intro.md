---
chunk_kind: "child"
pattern_id: "E.17"
pattern_title: "Multi‑View Publication Kit"
section_id: "E.17:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17/E.17__001_intro.md"
commit_sha: "3f6714ae3235e0d771dce32835be7696f626d2ee"
heading_path:
  - "E.17 — Multi‑View Publication Kit"
  - "E.17:intro — Intro"
line_start: 81210
line_end: 81254
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

## E.17 - Multi‑View Publication Kit
> **Status:** Stable
> **Type:** Part E publication pattern
> **Normativity:** Normative unless explicitly marked informative

**At a glance.** Use `E.17` when one already accepted engineering account must be published in one or more readable faces for different readers without changing its claims.

**Use this when.** The source account is already accepted for the present work, but a reader needs a plain explanation, technical card, interoperability card, or evidence-facing lane. The publication task is to expose the same account for that reader, not to create a new engineering claim, perform work, pass a gate, or establish assurance by presentation.

**What goes wrong if missed.** A readable face can silently add, widen, or hide claims. The opposite failure is to make every publication start with a four-face kit, a newly authored viewpoint or bundle, and an assurance dossier even when one small face would answer the reader's question.

**What this buys.** Each current reader gets the smallest useful face, the source remains recoverable, omitted detail and bounded use stay visible, and stronger identity or assurance apparatus is added only when a downstream use needs it.

**First action.** Point to the current source account and the engineering object or relation it describes, name the reader and what that reader must be able to understand or do, and choose only the face or faces needed for that use. Resolve an existing viewpoint when one already fits; do not author a new viewpoint or bundle merely to start publication.

**First output.** One useful publication face, or the smallest necessary set, that names the source, intended reader/use, what it preserves or omits, and how to return to the source. No ClaimGraph, formal profile, viewpoint bundle, evidence package, or four-face completion is required for this ordinary result.

**Working publication move.** Select the current source; choose the minimum face set for the named readers; copy or conservatively arrange only source-backed claims; mark material omissions and the bounded use; publish and stop. If a face will carry safety, release, evidence, cross-context, or other consequential reliance, strengthen only that face with the relations and records that the reliance needs.

**Ordinary formality rule.** A source pointer, reader/use line, readable face, and visible omission or return note are enough when the face is used for orientation, inspection, explanation, comparison, exchange preparation, or planning preparation and no downstream identity depends on it.

**High-reliance formality rule.** When reliance changes the engineering move, identify the exact source edition; resolve the exact viewpoint and E.17.0 conformance only if `U.View` membership matters; identify the E.24.PUB publication occurrence, form, carrier, and bounded use when their identities matter; and cite the concrete evidence, gate, release, provenance, or assurance record that carries the downstream claim. These additions do not turn the face itself into that record.

**Stop condition.** Stop as soon as every current reader has a useful face that preserves the needed claims and exposes its return to source. Do not create unused faces, fields, viewpoints, bundles, or assurance records for kit completeness.

| Publication case | Smallest useful result | Overread to block |
| --- | --- | --- |
| A project lead needs a plain account and an integrator needs the corresponding typed details from one accepted interface account. | Publish only a plain face and a technical card, both pointing to the same source and stating their omissions. | The two faces are treated as different engineering claims or as a mandatory four-face bundle. |
| A release or safety decision will rely on one face. | Strengthen that face with the exact source edition, any material viewpoint conformance, publication identity, and the separate gate, evidence, or assurance references. | The readable face or `AssuranceLane` is treated as the gate, evidence, assurance result, or release permission. |
| A card is labelled `PlainView`, `TechCard`, or carries `viewpointRef`. | Treat the label or reference as publication metadata until the exact E.17.0 conformance relation for the selected episteme obtains. | A face label, readable layout, or packaged reference is taken to establish `U.View` membership. |
| A skill pack or callable access service exposes a framework face or pattern card. | Use it for access, source-finding, and bounded orientation with edition and source return visible. | Protocol availability is treated as framework architecture, source evidence, permission, performed work, gate authority, or release authority. |
| A README, preface, front matter, or other publication carrier states scope, edition, intended use, or source pointers. | Use it for orientation, source-finding, and edition awareness. | Publication appearance is treated as truth, currentness proof, authorization, assurance, gate passage, or work readiness. |

**Boundary aid pointer.** Use `E.17:5.1d` only when a publication-facing unit begins to carry a distinct work, evidence, gate, approval, status, explanation, comparison, or reduced-use claim. Ordinary publication of a source-backed face does not require that boundary map.

At the first screen, keep only the current source, named reader/use, minimum useful face set, visible omissions, and return to source.

**Not this pattern when.** Use `A.15.1` for a performed-work claim, `A.10` for an evidence or provenance path, `B.3` for assurance or engineering justification, `A.20`/`A.21` for constraint or gate decisions, `A.7` for carrier work, and the relevant release or authority rule when that is the actual problem. E.17 only publishes the already accepted account and keeps those downstream claims separate.

> **Tech-name:** `MultiViewPublicationKit` (**MVPK**)

> **General publication-face form:** In E.17, `MVPK face` refers by default to the publication form. The selected source episteme, any separately constructed receiving episteme, the bounded-use declaration, the publication occurrence, and the carrier remain different objects and are named explicitly whenever one of them is meant. A face is not a U-kind and does not become a `U.View`, evidence, assurance, gate decision, work occurrence, authority, or release permission by its label or readability. Source-edition, viewpoint, scope, occurrence, form, carrier, pin, or downstream-record identities are stated when they change the receiving use.
> **USM binding (overview):** when publication-scope identity must travel, `U.PublicationScope` under A.2.6 carries that bound; an ordinary bounded-use line can precede that exact record. See §5.0.
> **Episteme-side view position.** MVPK can publish an already recognized `U.View`, or it can publish another selected episteme without claiming view membership. When `U.View` membership is material, E.17.0 tests that same episteme against the exact `U.Viewpoint` episteme resolved from `publicationViewpointRef`; `PublicationVPId` is the viewpoint episteme's designator, not the reference. A.6.3 construction, E.17.0 conformance, E.24.PUB publication occurrence/form/carrier, and C.29 representation remain separate relations.

