---
chunk_kind: "child"
pattern_id: "G.1"
pattern_title: "Author a Reusable CG-Frame Generator and Selector Kit"
section_id: "G.1:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/G.1/G.1__001_intro.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "G.1 — Author a Reusable CG-Frame Generator and Selector Kit"
  - "G.1:intro — Intro"
line_start: 135253
line_end: 135271
dependencies:
  - "A.10"
  - "A.15.2"
  - "A.15.3"
  - "A.19.CN"
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

## G.1 - Author a Reusable CG-Frame Generator and Selector Kit

> **Status:** Stable

**Tag.** architectural pattern; *generator chassis* (design‑time kit / authoring scaffold)
**Normativity.** normative, except sections explicitly marked *informative*
**Stage.** *design‑time* authoring of a generator‑kit with a *run‑time* execution façade (policy‑governed; edition‑aware)
**Primary output.** Publish the six cards `M1…M6` as a reusable CG‑Frame kit. The versioned **kit manifest**, identified by `CGKitId`, binds all six by their card ids.
**Primary hooks.** see **§12 Relations** (notably `G.Core`, `G.0`, `G.2`, `G.5`, `G.10`, `G.11`)
**Working‑model first (informative).** prefer working models and didactic micro‑examples; escalate to formal harnesses only when risk warrants (per E.8).


**Start here when.** You are authoring a reusable generator, selector, or set-result scaffold rather than a one-off plan, one-off comparison, or tool-specific method recipe.


**Neighboring FPF patterns.** Use `G.2` for the local SoTA set, `G.5` for governed set-return selection, `G.10` for shipping surfaces, `G.11` for refresh wiring, and `F.17` when the result must also land on a human-facing UTS surface.

**Use another pattern when.** For a one-off governed comparison, use `A.19.CPM` to compare an admitted profile pair under an explicit comparator, with `G.0` for comparison legality; use `G.5` for a shortlist. For project alignment, use `A.15`. When authoring a kit, make the chassis and its bindings explicit before choosing implementation tooling.

