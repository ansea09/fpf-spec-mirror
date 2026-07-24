---
chunk_kind: "child"
pattern_id: "G.Core"
pattern_title: "Part G Core Invariants"
section_id: "G.Core:5"
section_title: "Archetypal grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/G.Core/G.Core__006_archetypal-grounding.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "G.Core — Part G Core Invariants"
  - "G.Core:5 — Archetypal grounding"
line_start: 94145
line_end: 94155
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
In Phase‑2 refactoring, `G.Core` is the hub that allows each `G.x` to become structurally predictable: (a) a short, normative “Core linkage” slice, and (b) pattern‑scoped `Extensions`. Universal obligations cite canonical governing definitions such as `A.6.7`, `A.15.3`, `A.19`, `G.0`, and `A.19.CHR`, while RSCR trigger kinds and `DefaultGoverningDefinitionRef` references become typed and cite named definitions.

**Show 1: Refresh triggers without semantic drift.**
`G.11` already uses trigger tokens `T0…T7`. `G.Core` keeps them as aliases and maps them to canonical trigger kinds (e.g., `TelemetryDelta`, `EditionPinChange`, `CrossingBundleEdit`). This makes RSCR reason codes consistent across patterns and avoids re-explaining trigger semantics in every pattern.

**Show 2: Resolving competing defaults.**
If multiple patterns imply a default for `PortfolioMode`, the Default Governing Definition Index points to one governing definition (currently `CC‑G5.23`). Other patterns (e.g., bundles/log patterns) must cite that governing definition or delegate to it, rather than restating the default with slightly different wording. This preserves intent while preventing drift and ambiguity.

