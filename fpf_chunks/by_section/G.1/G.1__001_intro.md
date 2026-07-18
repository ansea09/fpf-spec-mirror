---
chunk_kind: "child"
pattern_id: "G.1"
pattern_title: "CG‑Frame‑Ready Generator"
section_id: "G.1:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/G.1/G.1__001_intro.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "G.1 — CG‑Frame‑Ready Generator"
  - "G.1:intro — Intro"
line_start: 91609
line_end: 91627
dependencies:
  - "A.10"
  - "A.15.3"
  - "A.19"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.23"
  - "E.10"
  - "E.19"
  - "E.8"
  - "G.0"
  - "G.10"
  - "G.11"
  - "G.2"
  - "G.3"
  - "G.4"
  - "G.5"
  - "G.Core"
keywords:
  - "CGFrameLibraryId"
  - "CGKitId manifest"
  - "RSCR linkage surfaces"
  - "RefreshReadinessCardId"
  - "ShortlistId"
  - "SoTA_SetId"
  - "UTS/Name Cards"
  - "VariantPoolId"
  - "and set-result scaffold"
  - "edition pins"
  - "generator"
  - "generator chassis"
  - "selector"
  - "set-result outcome"
  - "set-return selection"
  - "shipping and refresh boundaries"
  - "six-card kit (M1-M6)"
---

## G.1 - CG‑Frame‑Ready Generator

**Tag.** architectural pattern; *generator chassis* (design‑time kit / authoring scaffold)
**Status.** stable (Phase‑2 universalisation)
**Normativity.** normative, except sections explicitly marked *informative*
**Stage.** *design‑time* authoring of a generator‑kit with a *run‑time* execution façade (policy‑governed; edition‑aware)
**Primary output.** the **six‑card chassis** `M1…M6` published as a **complete, reusable CG‑Frame kit**, plus a versioned **kit manifest** `CGKitId` that binds the six cards as a single reusable unit (view‑friendly inventory + wiring surface)
**Primary hooks.** see **§12 Relations** (notably `G.Core`, `G.0`, `G.2`, `G.5`, `G.10`, `G.11`)
**Working‑model first (informative).** prefer working models and didactic micro‑examples; escalate to formal harnesses only when risk warrants (per E.8).
**Non‑duplication note.** Universal Part‑G invariants (tri‑state guard, set-return, penalties→`R_eff`‑only, crossing visibility, typed RSCR triggers, Default Governing Definition Index, P2W split, linkage discipline, shipping boundary) are governed in `G.Core` and are **only cited** here.

**Start here when.** You are authoring a reusable generator, selector, or set-result scaffold rather than a one-off plan, one-off comparison, or tool-specific method recipe.

**First output.** The six-card chassis `M1…M6` published as a reusable `CGKitId`-bound kit with a scope anchor, local SoTA set, variant pool, shortlist surface, and refresh-ready wiring.

**Neighboring FPF patterns.** Use `G.2` for the local SoTA set, `G.5` for governed set-return selection, `G.10` for shipping surfaces, `G.11` for refresh wiring, and `F.17` when the result must also land on a human-facing UTS surface.

**Common wrong neighboring-pattern changes.** If the real entry load is only a one-off governed comparison or shortlist, use `A.19`, `G.0`, or `G.5`; if the real entry load is project alignment rather than kit authoring, use `A.15`; if tooling choice is being treated as the first kit candidate, keep the case here only after the chassis and its bindings are explicit.

