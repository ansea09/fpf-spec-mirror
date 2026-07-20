---
chunk_kind: "child"
pattern_id: "E.20"
pattern_title: "Mechanism Introduction Protocol"
section_id: "E.20:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/E.20/E.20__003_problem.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "E.20 — Mechanism Introduction Protocol"
  - "E.20:2 — Problem"
line_start: 82371
line_end: 82380
dependencies:
  - "A.15.3"
  - "A.6.1"
  - "A.6.7"
  - "E.10"
  - "E.15"
  - "E.18"
  - "E.19"
  - "E.8"
  - "E.9"
  - "F.18"
  - "G.2"
  - "G.Core"
  - "G.x"
keywords:
  - "MIP-run manifest"
  - "P2W seam"
  - "PQG profiles"
  - "SlotKind lexicon discipline"
  - "alias docking"
  - "authoring protocol"
  - "canonical card-first"
  - "governing-definition assignment"
  - "mechanism introduction"
  - "no dangling …IntensionRef"
  - "regression envelope"
  - "suite boundary hygiene"
  - "typed RSCR triggers"
---

### E.20:2 - Problem

When a new mechanism (or mechanism family) is introduced without an explicit authoring protocol:

1. **Governing-definition ambiguity** causes partial changes: a suite enumerates a new `...MechanismDefinitionRef`, but the canonical `U.Mechanism` definition card is missing or inconsistent.
2. **Boundary erosion** occurs: suite descriptions start to define mechanism semantics; method wiring starts to redefine kernel meaning; publication/telemetry becomes a hidden tail.
3. **Plan/enactment confusion** appears: planned slot fillings start to carry launch values, witnesses, or gate decisions.
4. **Terminology drift** breaks citations: renames happen silently; tokens fragment across registers; downstream references become unstable.
5. **Review becomes non‑local**: every introduction is a bespoke scavenger hunt across patterns, making training, review, and refresh unreliable.

