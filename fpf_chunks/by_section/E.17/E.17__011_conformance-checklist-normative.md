---
chunk_kind: "child"
pattern_id: "E.17"
pattern_title: "Multi‑View Publication Kit"
section_id: "E.17:9"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17/E.17__011_conformance-checklist-normative.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "E.17 — Multi‑View Publication Kit"
  - "E.17:9 — Conformance Checklist (normative)"
line_start: 78631
line_end: 78674
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

### E.17:9 - Conformance Checklist (normative)

`CC-MVPK-FD` is the functional-description guard in §5.1a. It is conditional on a functional-description publication face and does not function as the first universal MVPK gate.

A conformance check is kept only if it changes the next bounded use of the publication face, blocks a concrete overclaim, or preserves a source reference or reopen condition needed for the declared bounded use.

#### E.17:9.1 - Core ordinary checks

| ID | Requirement | Practical test |
| --- | --- | --- |
| **CC-MVPK-1 (Source, reader, and use visible)** | Each ordinary publication form points to the current source account and exposes the separate reader/use declaration it serves. | A cold reader can find the source, understand why this form exists, and see material omissions. |
| **CC-MVPK-1b (`U.View` claim conditional)** | Only when the selected episteme exposed through a face is claimed as a `U.View` does the publication resolve an exact `publicationViewpointRef` and cite the obtaining E.17.0 conformance relation. | A form label, layout, or packaged reference alone is rejected as membership evidence. |
| **CC-MVPK-1a (Publication relations explicit when load-bearing)** | When availability, recurrence, dispute, external exchange, or reliance depends on publication identity, name the selected edition, audience, bounded use, form, carrier, expression relation, bearing relation, and publication occurrence. | The exact values resolve only for that stronger use; an ordinary face is not rejected for lacking an unused identity dossier. |
| **CC‑MVPK‑3 (No content extension)** | `PlainView`, `TechCard`, and `InteropCard` add **no new claims** beyond the underlying Description epistemes, including Description epistemes admitted for specification use. | Red‑line vs Description episteme, including any exact specification-use source, shows only formatting or indexing. |
| **CC-MVPK-4 (Pins and source references when material)** | Numeric or comparable claims relied on through a publication form retain the units, scale, reference plane, edition, and source references that change their interpretation; an ordinal-only claim stays comparison-only and is neither averaged nor converted to a z-score. | Relevant pins are visible, and an ordinal-only face contains no mean or z-score; a qualitative ordinary form carries no irrelevant pin dossier. |
| **CC-MVPK-4j (Publication bound visible)** | Alongside every selected form, the separate bounded-use declaration is visible; identify exact `U.PublicationScope` when that bound must travel or constrain a stronger use. | The ordinary use line is readable, and any load-bearing scope reference resolves without granting work or reliance. |
| **CC-MVPK-5 (Return and carrier boundary)** | Every selected form retains a return to source; identify the carrier, the needed A.10 evidence/provenance path or G.6 path citation, and any G.11 currentness result only when carrier identity, carrier work, reliance, evidence, replay, or currentness is material. | Source return is visible; stronger carrier/provenance references appear only where used. |



#### E.17:9.2 - Conditional checks

| ID | Requirement | Practical test |
| --- | --- | --- |
| **CC-MVPK-0 (Lean conditional guard)** | A Lean face checks only features it actually carries: set or partial-order semantics for a real selection/comparison, relevant pins for numeric or plane-dependent claims, an F.9 Bridge plus bounded-use claim for a semantic crossing, and a selected `ReferencePlane` plus applicable rule for a plane-dependent value. | No absent selection, number, semantic crossing, or plane dependency creates a placeholder field or failed check. |
| **CC‑MVPK‑2 (Functoriality)** | `Emit_s(id)` is identity; `Emit_s(g∘f) = Emit_s(g)∘Emit_s(f)`. | Compose two cards and diff with the card of the composite. |
| **CC-MVPK-3b (Boundary claim-set integrity)** | If a published arrow is a boundary, interface, or protocol and an A.6.B claim set exists (`L-*`, `A-*`, `D-*`, and `E-*`), then normative text on faces is traceable to that claim set (prefer claim-ID citations); faces do not become a second boundary specification. | Lint flags uncited normative clauses; faces reduce to {claim-ID citations + informative commentary}. |
| **CC‑MVPK‑4b (Lean evidence-facing lane)** | If `AssuranceLane-Lite` is used, presence bits for current evidence or bridge references suffice; full evidence-carrier lists remain with the exact evidence source. | Presence bits are visible, and no assurance or sufficiency claim is inferred from the lane. |
| **CC-MVPK-4c (Input and Output vs publication)** | When a morphism face exposes input/output information, it points to the signature-side declarations instead of duplicating them; it carries only source references and pins needed by the face. | The face has no second Input/Output specification and no unused presence-pin dossier. |
| **CC-MVPK-4d (Set-returning ordering)** | Any selection or comparison on faces returns sets or declared partial orders with a **ComparatorSet** citation. | No hidden scalarization; ComparatorSetRef present. |
| **CC‑MVPK‑4e (Signature on faces — banned)** | The term **“signature”** is **not used** on faces; use **TechName** or **PlainName**. | Token scan: no “signature” on faces. |
| **CC‑MVPK‑4f (Numeric and optional-PC discipline)** | Numeric or comparable claims retain the source pins that affect interpretation; when the optional PC profile is selected, its PC and CHR/CG references are explicit. | Cards show the material unit, scale, reference-plane, and edition pins; selected PC fields resolve without making PC classification a prerequisite for an ordinary face. |
| **CC‑MVPK‑4g (No axis or dimension)** | Faces avoid “axis”, “dimension”, and “plane” metaphors except **ReferencePlane**; use CHR terms (**Characteristic**, slot, or **CharacteristicSpace**). | Lexical check flags none; only `ReferencePlane` appears. |
| **CC‑MVPK‑4h (Edition pins on defs)** | Where maps, distances, or spaces are cited, the face pins `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and `CharacteristicSpaceRef.edition?`. | Validation shows edition fields populated. |
| **CC‑MVPK‑4i (Crossing references)** | A semantic crossing cites its F.9 Bridge and separate bounded-use claim; a plane-dependent value cites its selected `ReferencePlane` and applicable rule. A B.3 `CL`/`Φ(CL)` reference appears only when the current assurance use consumes that integration relation. | F.9 and plane references resolve; any B.3 penalty belongs to the assurance-bearing integration relation, not to the face. |
| **CC‑MVPK‑4k (Subset‑of underlier)** | For views about epistemes or capabilities, `PublicationScope ⊆ ClaimScope or WorkScope`; reindexing **does not widen** it. | Subset witness passes; promotion diff shows no widening. |
| **CC‑MVPK‑6 (Γ‑separation)** | No cost, time, or data-spend on publication morphisms. | CI shows proof records or witness records; gate validation passes. |
| **CC‑MVPK‑7 (Reindexing monotone)** | If `s ⪯ t`, then `Emit_s(x) ⪯ Emit_t(x)`. | `TechCard` ≤ `InteropCard` (more structure, same claims). |
| **CC‑MVPK‑8 (`publication-face kind` discipline)** | Only literal `publication-face kind` values **publication face/form** or **interop publication form** are used; faces are named **...View** or **...Card**. | Token scan; no “rendering” or “presentation” as `publication-face kind` values. |
| **CC‑MVPK‑9 (Reindexing naturality)** | Conceptual-form coercions `PromoteFace[s->t]` exist, are total in the selected formal substrate, and commute with composition. | The local witness uses `PromoteFace` and is not overread as a world-side relation. |
| **CC‑MVPK‑10 (Iso‑preservation)** | Isomorphisms in `U` remain isomorphisms under each viewpoint. | Cards show mapped inverses or an iso‑witness. |
| **CC‑MVPK‑11 (Typing & totality)** | Ill-typed composites are rejected at `FaceObj_s` rather than weakening the selected conceptual-form rules. | Type-check fails early; no best-effort composition claim appears on cards. |
| **CC‑MVPK‑12 (Crossing distinctions)** | A cross-context semantic face keeps the F.9 Bridge, bounded-use claim, and reliance result distinct; a ReferencePlane-dependent face keeps its characteristic, plane, and transfer or comparison rule distinct. Optional F.9 `CL` and B.3 integration `CL` remain in their own uses. | The face exposes only the references consumed by its bounded use and grants no crossing, reliance, or assurance by display. |

