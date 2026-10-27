---
chunk_kind: "child"
pattern_id: "G.Core"
pattern_title: "Discipline SoTA Kit Invariants, Defaults and Refresh Triggers (Part G)"
section_id: "G.Core:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/G.Core/G.Core__001_intro.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "G.Core — Discipline SoTA Kit Invariants, Defaults and Refresh Triggers (Part G)"
  - "G.Core:intro — Intro"
line_start: 124391
line_end: 124405
dependencies:
  - "A.15.3"
  - "A.19"
  - "A.19.CHR"
  - "A.6.7"
  - "E.10"
  - "E.19"
  - "E.8"
  - "G.0"
  - "G.13"
  - "G.Core"
keywords:
  - "Default Governing Definition Index"
  - "ID continuity"
  - "Part‑G invariants"
  - "RSCR trigger kinds"
  - "core linkage"
  - "delegation-first core"
---

## G.Core - Discipline SoTA Kit Invariants, Defaults and Refresh Triggers (Part G)

> **Status:** Stable


**Tag.** Architectural pattern for shared Part G rules
**Stage.** *design‑time*: authoring and stable citation
**Primary hooks.** E.8 (pattern template), E.10 (lexical/ontological rules), E.19 (conformance discipline), A.6.7 (SuiteObligations + suite protocol pins), A.15.2 (edition/reference baseline), A.15.3 (typed planned filling when applicable), A.19.CN (CN‑Spec), G.0 (CG‑Spec), A.19.CHR (CHR suite boundary), C.23 (SoS‑LOG), F.17 (UTS), F.15 (unification SCR/RSCR).

**Normativity.** Normative unless explicitly marked informative

**Purpose.** Keep Part G invariants tied to their governing definitions, with stable references for defaults and refresh triggers. Use the **RSCR trigger kind catalogue** and **Default Governing Definition Index** below when authoring or changing Part G patterns.

**Pattern placement.** New Part‑G `PatternId`s are permitted when (i) they introduce a new **kit/pack class** (typically in `G.2–G.5`), or (ii) they are required to preserve **one governing pattern per wiring extension** and wiring-only separation. Method/discipline/generator specifics SHOULD still default to `GPatternExtension` modules under `G.x:Extensions` (scoped by `PatternScopeId = G.x:Ext.*` and `GoverningPatternId`), rather than adding new Part‑G patterns.

