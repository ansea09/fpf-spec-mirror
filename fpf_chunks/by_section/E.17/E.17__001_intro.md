---
chunk_kind: "child"
pattern_id: "E.17"
pattern_title: "Multi‑View Publication Kit"
section_id: "E.17:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17/E.17__001_intro.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "E.17 — Multi‑View Publication Kit"
  - "E.17:intro — Intro"
line_start: 60960
line_end: 61005
dependencies:
  - "A.6.2"
  - "A.6.3"
  - "A.6.9"
  - "A.7"
  - "C.2.P"
  - "E.10"
  - "E.10.D2"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.17.AUD"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.8"
  - "F.9"
  - "F.9.1"
  - "U.EffectFreeEpistemicMorphing"
  - "U.EpistemicViewing"
  - "U.MultiViewDescribing"
keywords:
---

## E.17 - Multi‑View Publication Kit

**At a glance.** Use `E.17` when one source-backed episteme, episteme-lane view, morphism, or functional relation must be published in several readable faces for different readers without changing the underlying claim.

**Use this when.** The engineering team needs a plain view, technical card, interoperability card, or assurance lane that helps people read, inspect, exchange, or cite the same source-backed relation without turning the face into work occurrence, evidence, gate passage, engineering justification, control architecture, or release permission by presentation alone.

**First output.** One source-pinned publication face with the underlying `U.Episteme`, `D` episteme, or `S` episteme, publication scope, face kind, admissible publication use, and any live downstream typed value named only as far as the current use needs, such as a `GateDecision`, evidence path, work occurrence, status source, or authority-reference relation.

**Working action spine.** Publish one source-pinned face -> separate source episteme or episteme-lane view, face, carrier, admissible publication use, and any live downstream typed value plus its governing FPF pattern/reference -> use the face for inspection, source-finding, review, exchange, or planning preparation -> output one source-pinned publication face -> apply the exact neighboring FPF pattern if work, evidence, gate, engineering-justification, control, or release use becomes live.

**Ordinary formality rule.** If the face only supports orientation, source-finding, review, comparison, or planning preparation, keep the publication light: one pinned face or compact card plus a clear admissible-use line is enough.

**Load-bearing formality rule.** Add the fuller MVPK record only when the face will support external-impact reliance, cross-context exchange, evidence citation, gate or release pressure, engineering-justification use, disputed interpretation, or another use where a concrete overclaim would change the next engineering move.

**Stop condition.** Do not create a new publication record merely because a face exists. Stop when the current face changes no next engineering move and blocks no concrete overclaim.

**Admissible publication-use examples.**

| Admissible publication use | Source-finding or bounded inspection with no downstream claim or effect | Non-admissible publication use |
| --- | --- | --- |
| A source-pinned MVPK face lets the team inspect one morphism, review it, exchange it, or prepare planning without changing the claim. | A face helps planning support, but the team still needs to recover the exact method, evidence, gate, control, or carrier source before work, evidence, gate, control, carrier, or other downstream use. | A face, screen, export, or diagram is treated as performed work, gate passage, evidence, engineering justification, supervisory relation or control relation, or release permission by layout or readability alone. |


**Boundary aid pointer.** If one encountered publication-facing item is easy to read as work, evidence, gate, approval, status, explanation, comparison, or narrower-use rendering, handle one live claim or effect at a time using `E.17:5.1d`.

Here in the first-screen read, keep only the MVPK publication move: one source-pinned face, one admissible publication use, and exact neighboring FPF patterns or typed downstream values only as far as the current use needs.


**Not this pattern when.** Not this pattern when the live issue is performed `U.Work`, a work plan, evidence path, provenance path, engineering justification, gate decision, control architecture, carrier work, OCR work, or a narrower-use rendering that needs its own source-bearing return. Use the exact FPF pattern that governs that issue.

> **Tech‑name:** `U.MultiViewPublicationKit` (**MVPK**)
> **Plain‑name:** Multi‑view publication kit. The morphism-publication profile is the canonical formal profile.
> **General publication-face form:** one MVPK face is a `U.View` emitted over one source `U.Episteme` or episteme-lane `U.View`, under one publication `U.Viewpoint`, one `U.PublicationScope`, declared pins where needed, one face kind, and one admissible publication use. The face adds no claim by readable form. Evidence use, authority use, gate use, work use, release use, and engineering-justification use require the exact neighboring FPF pattern and typed project-side value/reference that carry that downstream use, such as a `GateDecision`, evidence path, work occurrence, status source, or authority-reference relation.
> **Canonical morphism profile (conceptual form):**  `MVPK : (U.Morphism, Σ_viewpoints) ↦ U.ViewFamily` with per‑viewpoint components
> `ViewObj_s : U.Object → U.ViewObj_s` and `Emit_s(-) : U.Morphism → U.ViewMorph_s`,
> such that `(ViewObj_s, Emit_s)` forms a functor `U → View_s(U)`. For each `s ⪯ t`, a **reindexing coercion**
> `PromoteView[s→t]_X : ViewObj_s(X) → ViewObj_t(X)` exists and is **natural in `X`**: for every `f : X → Y`,
> `PromoteView[s→t]_Y ∘ Emit_s(f) = Emit_t(f) ∘ PromoteView[s→t]_X` (see Rules §6.2).
> **Notation:** `Σ_viewpoints` is abbreviated as `Σ` where convenient.
> **Twin‑register aliases (naming discipline):**
> • **Tech:** `Emit_PlainView`, `Emit_TechCard`, `Emit_InteropCard`, `Emit_AssuranceLane`; `PromoteView[s→t]_-`.
> • **Plain:** `PlainView(x)`, `TechCard(x)`, `InteropCard(x)`, `AssuranceLane(x)`; “Promote to *t*”.

> **USM binding (overview):** `PublicationScope` is a **USM‑class** object that parameterizes MVPK; see §5.0.
> **Episteme lane.** MVPK treats each face as a `U.View` in the sense of C.2.1 and E.17.0 (species `U.EpistemeView`). For any MVPK face, the source is a named `U.Episteme` or episteme-lane `U.View`; the face declares a publication `U.Viewpoint` (`PublicationVPId`) drawn from a `U.ViewpointBundle` (E.17.1 and E.17.2). In the morphism profile, every `Emit_s(f)` has `DescribedEntitySlot` and `DescriptionContext` target `f : U.Morphism`. In a non-morphism publication, the face names the exact source episteme, episteme-lane view, described entity, or claim relation that the face publishes, and no functorial composition claim is live unless the corresponding FPF pattern supplies it. Slot discipline (`ViewSlot` and `ViewRef`) is inherited from C.2.1 and A.6.5 and is not redefined in MVPK.

