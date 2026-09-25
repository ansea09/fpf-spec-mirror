---
chunk_kind: "child"
pattern_id: "G.2"
pattern_title: "Harvest and Synthesize SoTA for a CG-Frame"
section_id: "G.2:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/G.2/G.2__001_intro.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "G.2 — Harvest and Synthesize SoTA for a CG-Frame"
  - "G.2:intro — Intro"
line_start: 111566
line_end: 111585
dependencies:
  - "A.10"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.21"
  - "E.10"
  - "E.19"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.0"
  - "G.1"
  - "G.10"
  - "G.11"
  - "G.13"
  - "G.3-G.5"
  - "G.6"
  - "G.7"
  - "G.Core"
keywords:
  - "BridgeMatrix"
  - "DeclaredSubstrateAtlasView"
  - "FlowRecord"
  - "GammaEpistSynthId"
  - "SoTA Synthesis Pack@CG-Frame"
  - "SoTA harvest"
  - "SoTAPaletteDescription"
  - "Tradition"
  - "TraditionAtlasView"
  - "TypedSetViews"
  - "palette-first"
  - "state of the art"
  - "synthesis"
---

## G.2 - Harvest and Synthesize SoTA for a CG-Frame

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative *(unless explicitly marked informative)*
>
> **Purpose.** Provide a repeatable, auditable way to **discover**, **triage**, and **synthesize** state‑of‑the‑art (SoTA) across competing `Tradition` lineages *before* minting CHR/CAL/LOG assets for a `CG‑Frame`.
>
> **Start here.** Write the question the receiving CHR, CAL or selector work must answer. Before counting coverage, fix the source population and what counts as the same family. Distill the first source claims with their editions, evidence and limits, keeping competing lineages separate. The first useful result is a claim set that can answer part of that question and expose what is still missing. Use the manifest below when developing it into a conforming synthesis pack; a single-source fact lookup can return its source directly without creating such a pack.
> The primary output is a **`SoTA Synthesis Pack@CG‑Frame`** that feeds:
>
> * naming/publication (UTS),
> * CHR authoring (G.3),
> * CAL authoring (G.4),
> * method/generator registries and dispatch (G.5).
>
> **Scope note.** This pattern **governs** the harvesting + synthesis *generator* in Part G. Use **G.10** to ship the pack and **G.11** to orchestrate refresh.
>
> **Terminology note (normative).** In normative clauses below, **`Tradition`** refers to the *Tech* token `Tradition` (a plural lineage with internally coherent commitments). Plain “tradition” is allowed only as a 1:1 synonym.

