---
chunk_kind: "child"
pattern_id: "E.20"
pattern_title: "Mechanism Introduction Protocol: Introduce or Revise FPF Mechanisms"
section_id: "E.20:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/E.20/E.20__004_forces.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "E.20 — Mechanism Introduction Protocol: Introduce or Revise FPF Mechanisms"
  - "E.20:3 — Forces"
line_start: 98214
line_end: 98223
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

### E.20:3 - Forces

| Force | Tension |
|---|---|
| **Extensibility vs Kernel stability** | New mechanisms need to be addable ↔ kernel reference loci need to remain citeable and minimal. |
| **One governing definition vs cross-locus reach** | Each mechanism meaning, suite change, WorkPlan planned-baseline change, wiring module, or token migration needs one governing definition while a mechanism introduction often spans suites, plans, wiring, and lexicon. |
| **Didactic usability vs inspectability** | Humans need clear recognition text and examples, while declarations, obligations, and pins must remain checkable at their governing loci. |
| **SoTA evolution vs semantic integrity** | Methods evolve fast ↔ mechanism meaning SHALL NOT silently shift via wiring updates. |
| **Local naming freedom vs global reference continuity** | Context-local labels are necessary ↔ references need to remain stable across editions and refactors. |

