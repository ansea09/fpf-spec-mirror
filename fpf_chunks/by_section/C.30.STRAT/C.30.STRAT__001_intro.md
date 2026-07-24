---
chunk_kind: "child"
pattern_id: "C.30.STRAT"
pattern_title: "Stratification Wording Precision Restoration"
section_id: "C.30.STRAT:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.STRAT/C.30.STRAT__001_intro.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "C.30.STRAT — Stratification Wording Precision Restoration"
  - "C.30.STRAT:intro — Intro"
line_start: 60173
line_end: 60188
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.SPR"
  - "A.2"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.2.P"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.10.ARCH"
  - "E.11"
  - "E.17"
  - "E.18"
  - "E.8"
  - "F.18"
  - "G.5"
  - "G.6"
  - "I.2"
keywords:
---

## C.30.STRAT - Stratification Wording Precision Restoration

> **Type:** Architectural precision-restoration subpattern under `C.30`
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** Stratification and architecture-operation source-label repair.

**Intent.** Recover source wording such as `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, and `gate` by completing the `E.10.ARCH` recovery row for that wording use: `semanticAreaBaseConcept`, `semanticAreaSenseFamily`, selected `ontologicalNeighborhood`, primary `EntityOfConcern` kind, encountered FPF kind or reference, relation to the primary `EntityOfConcern`, recovered kind, relation, or claim-use, source-use disposition, governing pattern, admissible use, non-admissible use, and remaining reader use. No conforming `C.30.STRAT` use mints `U.Layer`, `U.Level`, `U.Tier`, `U.Stack`, `U.Ladder`, `U.Rung`, `U.Block`, `U.Expert`, `U.Cache`, or one universal `U.Stratification`.

**Builds on.** `E.10`, `E.10.ARCH`, `E.8`, `F.18`, `C.30.P`, `A.22`, and `C.30`.

**Coordinates with.** `C.30.ASV`, `C.30.LCA`, `C.30.TFS-REL`, `C.30.ILC`, `A.6.M`, `A.6.F`, `E.18`, `C.16.P`, `C.16`, `A.19.SPR`, `C.2.P`, `E.17`, `C.29`, `C.28`, `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `A.15`, `A.2`, `G.5`, and `C.11`.

**E.10.ARCH governing relation.** When `E.10` encounters a stratification or architecture-operation source label whose `ontologicalNeighborhood`, primary `EntityOfConcern` kind, recovered kind, relation, claim-use, source-use disposition, or governing pattern is hidden, `E.10.ARCH` selects `C.30.STRAT` only until those row fields are recovered or the wording is lowered to ordinary source label, quote-only wording, reduced-use cue, blocked use, or incomplete rewrite. `C.30.STRAT` then stops at the source-label repair row; the governing pattern carries any recovered non-source-label claim or relation.

