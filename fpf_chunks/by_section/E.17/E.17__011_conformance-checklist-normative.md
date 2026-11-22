---
chunk_kind: "child"
pattern_id: "E.17"
pattern_title: "Multi‑View Publication Kit"
section_id: "E.17:9"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17/E.17__011_conformance-checklist-normative.md"
commit_sha: "4ee69807f8e5d4fa438e8c9b5de001d91275cc31"
heading_path:
  - "E.17 — Multi‑View Publication Kit"
  - "E.17:9 — Conformance Checklist (normative)"
line_start: 115540
line_end: 115583
dependencies:
  - "A.10"
  - "A.15.4"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.3.RT.OE"
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

`CC-MVPK-FD` is the functional-description guard in §5.1a. It is conditional on a functional-description publication face and is not a prerequisite for every MVPK publication.

A conformance check is kept only if it changes the next bounded use of the publication face, blocks a concrete overclaim, or preserves a source reference or reopen condition needed for the declared bounded use.

#### E.17:9.1 - Core ordinary checks

| ID | Requirement | Practical test |
| --- | --- | --- |
| **CC-MVPK-1 (Source, reader, and use visible)** | Each ordinary publication form points to the current source account and states the bounded reader/use it serves. | A cold reader can find the source, identify the purpose and recognize material omissions. For a claimed decision, check that the recipient can recover the needed conditions from the face or from an authorized source available before acting. |
| **CC-MVPK-1b (`U.View` claim conditional)** | Only when the selected episteme exposed through a face is claimed as a `U.View` does the publication resolve `publicationViewpointRef` and cite the obtaining E.17.0 conformance relation. | A form label, layout, or packaged reference alone is rejected as membership evidence. |
| **CC-MVPK-1a (Publication relations explicit when load-bearing)** | When availability, recurrence, dispute, external exchange, or reliance depends on publication identity, name the selected edition, audience, bounded use, expression, selected form, carrier, expression relation, bearing relation, and publication occurrence. | The identified values resolve only for that stronger use; an ordinary face is not rejected for lacking an unused identity dossier. |
| **CC‑MVPK‑3 (No content extension)** | `PlainView`, `TechCard`, and `InteropCard` add **no new claims** beyond the underlying source epistemes, including those admitted for specification use. | Compare the claims, conditions and strength of the face with the source. A faithful paraphrase, a supported consequence or an attributed quotation can preserve them. Recover a ground for each decision-changing assertion. |
| **CC-MVPK-4 (Pins and source references when material)** | Numeric or comparable claims relied on through a publication form retain the units, scale, reference plane, edition, and source references that change their interpretation. An ordinal-only claim stays comparison-only and is neither averaged nor converted to a z-score. | Relevant pins are visible, and an ordinal-only face contains no mean or z-score. A qualitative ordinary form carries no irrelevant pin dossier. |
| **CC-MVPK-4j (Publication bound visible)** | Alongside every selected form, the separate bounded-use declaration is visible; identify `U.PublicationScope` when that bound must travel or constrain a stronger use. | The ordinary use line is readable, and any load-bearing scope reference resolves without granting work or reliance. |
| **CC-MVPK-5 (Return and carrier boundary)** | Every selected form retains a return to source. Identify the carrier, the needed A.10 evidence/provenance path or G.6 path citation, and any G.11 currentness result only when carrier identity, carrier work, reliance, evidence, replay, or currentness is material. | Source return is visible. Stronger carrier/provenance references appear only where used. |



#### E.17:9.2 - Conditional checks

| ID | Requirement | Practical test |
| --- | --- | --- |
| **CC-MVPK-0 (Lean conditional guard)** | A Lean face checks only features it carries: the comparison criteria for a bounded source contrast, declared set or order semantics for a selection or ordering, relevant pins for numeric or plane-dependent claims, an F.9 Bridge plus bounded-use claim for a semantic crossing, and a selected `ReferencePlane` plus applicable rule for a plane-dependent value. | No absent selection, ordering, number, semantic crossing, or plane dependency creates a placeholder field or failed check. |
| **CC‑MVPK‑2 (Functoriality)** | The declared action on arrows preserves identities and composition throughout the claimed domain. | Establish the laws by derivation, by a generating presentation with its relations, or by checking the identities and every composable pair in the stated finite domain. A local comparison establishes its specified composite. |
| **CC-MVPK-3b (Boundary claim-set integrity)** | For a published boundary, interface or protocol with an A.6.B claim set (`L-*`, `A-*`, `D-*`, `E-*`), trace the operative terms on a face to that set, preferably by claim ID. | Check the attributed text against the governing edition, including any clauses the recipient must read offline. Correct unsupported clauses and keep the source authoritative. |
| **CC‑MVPK‑4b (Lean evidence-facing lane)** | If `AssuranceLane-Lite` is used, presence bits for current evidence or bridge references suffice; full evidence-carrier lists remain with the evidence source. | Presence bits are visible, and no assurance or sufficiency claim is inferred from the lane. |
| **CC-MVPK-4c (Input and Output vs publication)** | When a morphism face exposes input/output information, the signature-side declarations remain authoritative. Provide an accessible return to those declarations or carry the needed source-attributed content for detached use. | The face creates no independent Input/Output specification; its receiving use can recover the needed declarations and material pins. |
| **CC-MVPK-4d (Published comparison and ordering)** | A source contrast keeps its declared comparison criteria. A published selection or ordering keeps its source-defined set or order semantics and comparator, citing **ComparatorSet** when that formal family is used. | No hidden scalarization or decision by display order; an ordinary bounded contrast needs no invented ranking or comparator family. |
| **CC-MVPK-4e (Use Signature for a signature)** | Use **Signature** on a face only for an object that is a signature under its applicable pattern. Use **TechName** or **PlainName** for the face's name. | A cited signature remains identifiable; a face label is not presented as a signature. |
| **CC‑MVPK‑4f (Numeric and optional-PC discipline)** | Numeric or comparable claims retain the source pins that affect interpretation; when the optional PC profile is selected, its PC and CHR/CG references are explicit. | Cards show the material unit, scale, reference-plane, and edition pins; selected PC fields resolve without making PC classification a prerequisite for an ordinary face. |
| **CC‑MVPK‑4g (Characteristic and mathematical meaning)** | Faces name the characteristic, slot, space or mathematical construction. | The terms preserve the source meaning and the interpretation needed by the bounded use; literal mathematical axes, dimensions and planes remain admissible. |
| **CC‑MVPK‑4h (Edition pins on defs)** | Where maps, distances, or spaces are cited, the face pins `DescriptorMapRef.edition` and `DistanceDefRef.edition` as applicable. Identify the space by `CharacteristicSpaceRef`. When the use depends on its exact definition, pin the separate `characteristicSpaceDescriptionRef: U.EpistemeRef` under A.19:5.1.1.1. | Required references resolve. The description supplies the defining components of that same space. |
| **CC‑MVPK‑4i (Crossing references)** | A semantic crossing cites its F.9 Bridge and separate bounded-use claim; a plane-dependent value cites its selected `ReferencePlane` and applicable rule. A B.3 `CL`/`Φ(CL)` reference appears only when the current assurance use consumes that integration relation. | F.9 and plane references resolve; any B.3 penalty belongs to the assurance-bearing integration relation, not to the face. |
| **CC‑MVPK‑4k (Subset‑of underlier)** | A face selecting `E` retains each applicable `ClaimScope` bound. If it presents a qualified holder-ability claim `C` about holder System `H` for work admission, also require `PublicationScope ⊆ WorkScope(C)`; use the intersection when both bounds apply. Reindexing **does not widen** publication scope. | The capability description has EntityOfConcern `H`; `C` designates its work-condition basis. All applicable subset witnesses pass; promotion diff shows no widening. |
| **CC‑MVPK‑6 (Γ‑separation)** | Publication morphisms do not consume cost, time, or data resources. | Any published resource claim retains its accounting subject and measured, estimated or derived basis. A claim about performed Work retains that independently admitted occurrence and its actual resource-use grounds. |
| **CC‑MVPK‑7 (Reindexing monotone)** | If `s ⪯ t`, then `Emit_s(x) ⪯ Emit_t(x)`. | `TechCard` ≤ `InteropCard` (more structure, same claims). |
| **CC‑MVPK‑8 (`publication-face kind` discipline)** | Only literal `publication-face kind` values **publication face/form** or **interop publication form** are used; faces are named **...View**, **...Card**, or **...Lane**. | Token scan; no “rendering” or “presentation” as `publication-face kind` values. |
| **CC‑MVPK‑9 (Reindexing naturality)** | Each required `PromoteFace[s->t]` component is total in the selected formal substrate and its naturality square commutes for every arrow of the claimed domain. | Compare the two composites in §6. A domain-wide derivation, complete finite check or sufficient check on generators supports naturality. One square supports the local promotion claim for that arrow. |
| **CC‑MVPK‑10 (Iso‑preservation)** | Isomorphisms in `U` remain isomorphisms under each selected `Emit_s`. | Cards show mapped inverses or an iso‑witness. |
| **CC‑MVPK‑11 (Typing & totality)** | Ill-typed composites are rejected at `FaceObj_s` rather than weakening the selected conceptual-form rules. | Type-check fails early; no best-effort composition claim appears on cards. |
| **CC‑MVPK‑12 (Crossing distinctions)** | A cross-context semantic face keeps the F.9 Bridge, bounded-use claim, and reliance result distinct; a ReferencePlane-dependent face keeps its characteristic, plane, and transfer or comparison rule distinct. Optional F.9 `CL` and B.3 integration `CL` remain in their own uses. | The face exposes only the references consumed by its bounded use and grants no crossing, reliance, or assurance by display. |

