---
chunk_kind: "child"
pattern_id: "G.Core"
pattern_title: "Part G Core Invariants"
section_id: "G.Core:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/G.Core/G.Core__001_intro.md"
commit_sha: "646b0b9b164f7c13258633a33b92d2d0a569da28"
heading_path:
  - "G.Core — Part G Core Invariants"
  - "G.Core:intro — Intro"
line_start: 78449
line_end: 78465
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

## G.Core - Part G Core Invariants


**Tag.** Architectural pattern (Part‑G core invariants hub; refactoring/deduplication)
**Stage.** *design‑time* (authoring discipline + ID‑stable citation discipline; no run‑time mechanism)
**Primary hooks.** E.8 (pattern template), E.10 (lexical/ontological rules), E.19 (conformance discipline), A.6.7 (SuiteObligations + suite protocol pins), A.15.3 (planned baseline), A.19 (CN‑Spec), G.0 (CG‑Spec), A.19.CHR (CHR suite boundary), C.23 (SoS‑LOG), F.17 (UTS), F.15 (RSCR).

**Status.** Stable
**Placement.** Part G core section before `G.0` (without renumbering `G.0…G.13`).
**Normativity.** Normative unless explicitly marked informative

**Purpose.** Provide *one governing definition* for Part‑G‑wide invariants (**delegation-first citation and change-control discipline**), plus a typed **RSCR trigger kind catalogue** and a **Default Governing Definition Index**, so Part G can be refactored without semantic drift or public‑ID breakage.

**Phase‑2 constraint.** `G.Core` is the only new Part‑G pattern introduced in Phase‑2; discipline/method/generator specifics remain in `G.x` as `Extensions`, citations to existing governing patterns, or Phase‑3 seeds (appendix) without new Phase‑2 norms.

**Post‑Phase‑2 evolvability policy.** The Phase‑2 restriction above is historical. From Phase‑3 onward, new Part‑G `PatternId`s are permitted when (i) they introduce a genuinely new **kit/pack class** (typically levels `G.2–G.5`), or (ii) they are required to preserve **one governing pattern per wiring extension** and wiring-only separation. Method/discipline/generator specifics SHOULD still default to `GPatternExtension` modules under `G.x:Extensions` (scoped by `PatternScopeId = G.x:Ext.*` and `GoverningPatternId`), rather than adding new Part‑G patterns.

