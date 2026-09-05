---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__001_intro.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:intro — Intro"
line_start: 40037
line_end: 40053
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
---

## B.3.5 - Working-Model Relations & Grounding (CT2R-LOG)
> **Status:** Stable
> **Type:** Pattern

**At a glance.** Use B.3.5 when a human-facing structural relation or a collection's own belongs-to relation has been selected for an additional assurance account without exposing constructive machinery as the public vocabulary.

**Use this when.** Use this assurance profile only when a publication choice or named current requirement elects it for a direct relation claim. State the readable relation first. After election, structural parthood and collection belonging follow separate trace and `validationMode` obligations. The trace reports independently grounded facts for inspection; it creates neither the relation occurrence nor the entity it describes.

**What goes wrong if missed.** The readable relation and its assurance account collapse: authors either lose usable relation sentences, treat collection belonging as parthood, prohibit separately grounded parthood by label, or make a trace look like the cause of the claim.

**What this buys.** Working-Model relations stay readable, while an elected assurance branch supplies the right inspectable account without changing the direct relation kind.

**Not this pattern when.** Not this pattern when a direct relation claim is sufficient and no publication choice or current requirement elects this assurance profile. Also not this pattern when the current question is how to construct the trace (`C.13`), which mereology relation kind is intended (`A.14`), whether a new holon exists (`B.2`), or whether a candidate name deserves durable U-kindhood (`E.24.UK`).

> **One‑line summary.**
> CT2R-LOG keeps **ComponentOf**, ordinary belongs-to sentences, **PortionOf**, and **AspectOf** readable while respecting their different relation kinds. When this assurance profile is elected, structural parthood uses its applicable construction account; collection belonging uses a current `C.13 set` trace. Neither branch changes what makes the direct relation obtain, and neither trace decides whether a separate part relation is possible.

