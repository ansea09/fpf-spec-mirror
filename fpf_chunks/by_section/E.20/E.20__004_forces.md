---
chunk_kind: "child"
pattern_id: "E.20"
pattern_title: "Mechanism Introduction Protocol: Introduce or Revise FPF Mechanisms"
section_id: "E.20:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/E.20/E.20__004_forces.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "E.20 — Mechanism Introduction Protocol: Introduce or Revise FPF Mechanisms"
  - "E.20:3 — Forces"
line_start: 120571
line_end: 120580
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
| **Extensibility and kernel stability** | Authors need to add mechanisms while keeping kernel reference points minimal and citeable. |
| **One governing definition vs cross-locus reach** | Each mechanism meaning, suite change, WorkPlan planned-baseline change, wiring module, or token migration needs one governing definition while a mechanism introduction often spans suites, plans, wiring, and lexicon. |
| **Didactic usability vs inspectability** | Humans need clear recognition text and examples, while declarations, obligations, and pins must remain checkable at their governing loci. |
| **SoTA evolution and semantic integrity** | Methods evolve quickly. Mechanism meaning SHALL NOT change silently through a wiring update. |
| **Local naming freedom and global reference continuity** | Contexts need local labels. References must remain stable across editions and refactors. |

