---
chunk_kind: "child"
pattern_id: "E.20"
pattern_title: "Mechanism Introduction Protocol: Introduce or Revise FPF Mechanisms"
section_id: "E.20:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/E.20/E.20__003_problem.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "E.20 — Mechanism Introduction Protocol: Introduce or Revise FPF Mechanisms"
  - "E.20:2 — Problem"
line_start: 98228
line_end: 98237
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
  - "alias docking"
  - "authoring protocol"
  - "declaration-local operation members"
  - "governing-definition assignment"
  - "mechanism introduction"
  - "planned baseline"
  - "resolvable MechanismDefinitionRef"
  - "suite boundary"
  - "trigger triage"
  - "wiring"
---

### E.20:2 - Problem

When a new mechanism (or mechanism family) is introduced without an explicit authoring protocol:

1. **Governing-definition ambiguity** causes partial changes: a suite enumerates a new `MechanismDefinitionRef`, but that designator has no resolvable A.6.1 `U.Mechanism` episteme or resolves only to a card-shaped placeholder without mechanism identity and content.
2. **Boundary erosion** occurs: suite descriptions start to define mechanism semantics; method wiring starts to redefine kernel meaning; publication/telemetry becomes a hidden tail.
3. **Plan/enactment confusion** appears: planned slot fillings start to carry launch values, witnesses, or gate decisions.
4. **Terminology drift** breaks citations: renames happen silently; tokens fragment across registers; downstream references become unstable.
5. **Review becomes non‑local**: every introduction is a bespoke scavenger hunt across patterns, making training, review, and refresh unreliable.

