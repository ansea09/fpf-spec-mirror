---
chunk_kind: "child"
pattern_id: "G.1"
pattern_title: "CG‑Frame‑Ready Generator"
section_id: "G.1:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/G.1/G.1__002_problem-frame.md"
commit_sha: "c7ac61bbaa8d3c10165b1a5a4a350956c87d77c9"
heading_path:
  - "G.1 — CG‑Frame‑Ready Generator"
  - "G.1:1 — Problem frame"
line_start: 98477
line_end: 98495
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

### G.1:1 - Problem frame

You are authoring a **CG‑Frame** and want a **repeatable scaffold** that connects:

* a declared **scope anchor** (`CG‑FrameContext`, `entityOfConcern`, governing spec refs),
* a **local SoTA set** (scoped and provenance‑anchored),
* a **variant pool** (candidate ideas / decision options / method variants),
* a **shortlist** (a set-result outcome, not a forced singleton),
* **publication‑ready bindings** into Part‑F artefacts (UTS rows, Name Cards, RSCR tests, worked examples),
* and **refresh readiness** (telemetry hooks + RSCR wiring) without redefining refresh or shipping.

This pattern is intentionally **a chassis**, not a method specification:

* harvesting semantics are governed by `G.2`,
* selection/dispatch semantics are governed by `G.5`,
* CHR/CAL payload semantics are governed by `G.3` / `G.4`,
* shipping semantics are governed by `G.10`,
* refresh orchestration governing definition is `G.11`.

