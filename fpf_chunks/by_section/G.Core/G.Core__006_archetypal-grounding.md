---
chunk_kind: "child"
pattern_id: "G.Core"
pattern_title: "Discipline SoTA Kit Invariants, Defaults and Refresh Triggers (Part G)"
section_id: "G.Core:5"
section_title: "Archetypal grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/G.Core/G.Core__006_archetypal-grounding.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "G.Core — Discipline SoTA Kit Invariants, Defaults and Refresh Triggers (Part G)"
  - "G.Core:5 — Archetypal grounding"
line_start: 134772
line_end: 134782
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

### G.Core:5 - Archetypal grounding

**Tell.**
A Part G pattern can present a short normative Core linkage section alongside its pattern-scoped `Extensions`. A direct reference with its use conditions also suffices (§4.2). Authors cite the governing definitions of universal obligations, including `A.6.7`, `A.15.3`, `A.19`, `G.0`, and `A.19.CHR`. Typed RSCR trigger kinds and `DefaultGoverningDefinitionRef` references point to named definitions.

**Show 1: Refresh triggers without semantic drift.**
`G.11` uses trigger tokens `T0…T7`. `G.Core` keeps them as aliases and maps them to canonical trigger kinds (e.g., `TelemetryDelta`, `EditionPinChange`, `CrossingBundleEdit`). This makes RSCR reason codes consistent across patterns and avoids re-explaining trigger semantics in every pattern.

**Show 2: Resolving competing defaults.**
If several patterns imply a default for `PortfolioMode`, the Default Governing Definition Index points to the governing definition, `CC‑G5.23`. Other patterns, including bundle and log patterns, must leave the definition there and cite or delegate to it. A separate local wording could change how their readers interpret the default.

