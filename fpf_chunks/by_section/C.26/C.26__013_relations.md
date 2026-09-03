---
chunk_kind: "child"
pattern_id: "C.26"
pattern_title: "Quantum-Like Modeling Lens"
section_id: "C.26:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.26/C.26__013_relations.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "C.26 — Quantum-Like Modeling Lens"
  - "C.26:12 — Relations"
line_start: 54723
line_end: 54744
dependencies:
  - "A.10"
  - "A.15"
  - "A.19"
  - "A.3"
  - "A.6"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.25"
  - "C.26.1"
  - "C.26.1-C.26.3"
  - "C.26.2"
  - "C.26.3"
  - "E.17"
  - "E.17.EFP"
  - "E.24.PUB"
  - "E.8"
  - "E.9"
  - "F.9"
keywords:
  - "QL-NQ"
  - "QL-lite"
  - "incompatible probes"
  - "instrument update"
  - "minimal admissible output"
  - "order effect"
  - "probe frame"
  - "quantum-like"
  - "source-loss coarsening"
  - "state export"
---

### C.26:12 - Relations

**C.28 causal-use relation.**

- C.28 governs causal-use question, causality-ladder rung, causal estimand, identification, counterfactual sampling realizability, causal evidence support basis, causal-use verdict, causal fairness, causal policy, and causal method parity.
- This pattern keeps residual quantum-like probe, frame, order, export, or coarsening discipline after ordinary causal-use explanation has been tried.
- Non-admissible use: intervention, causal effect, causal fairness, causal policy, counterfactual comparison, causal method parity, or counterfactual-rung-data realizability do not activate quantum-like modeling by themselves.
- Exit: when the question under repair is causal, cite `C.28` before retaining QL-lite or QL-NQ.

**C.27 temporal-claim relation.**

- C.27 may flag: ordinary state/rate/rate-change, effort-window, rhythm, braking, coasting, or intervention-timing claims before any quantum-like cue is considered.
- This pattern keeps: residual quantum-like probe, frame, order, export, or coarsening discipline.
- Non-admissible use: discreteness, finite differences, typed states, state-space reduction, tokenization, dashboards, probes, measurement plans, speed words, rhythm words, or Dyn2 words do not activate quantum-like modeling by themselves.
- Boundary: use C.27 and ordinary FPF patterns first; use C.26 only where residual probe, frame, order, export, or coarsening cue remains after those relations are named.

- Builds on: `E.8`, `E.9`, `C.11`, `C.16`, `C.25`, `A.6`, `A.6.P`, `F.9`, `E.24.PUB`, `E.17`, `E.17.EFP`, `A.15`, `A.10`, `B.3`, `A.3`, `C.18`, `C.19`, `A.19`.
- Constrains: QL wording in `C.26.1`, `C.26.2`, and `C.26.3`.
- Carries: state-representation coarsening as a card inside `C.26:4.5`, not as a separate pattern.
- Does not cover: physical quantum claims, a generic probe ontology, a generic state ontology, a service/cell pattern, or a field-like synchronization pattern.
- Name boundary: `Quantum-Like Modeling Lens` is a pattern label for a modeling lens and modeling discipline, not `U.Lens`, not `QuantumLikeArchitecture`, not `Quantum Substrate`, not `Quantum Ontology`, and not a universal architecture doctrine.

