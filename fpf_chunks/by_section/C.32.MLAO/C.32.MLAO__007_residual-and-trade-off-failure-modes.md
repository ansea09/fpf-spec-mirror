---
chunk_kind: "child"
pattern_id: "C.32.MLAO"
pattern_title: "Multilevel Architecture Residual Optimization"
section_id: "C.32.MLAO:6"
section_title: "Residual And Trade-Off Failure Modes"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.MLAO/C.32.MLAO__007_residual-and-trade-off-failure-modes.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "C.32.MLAO — Multilevel Architecture Residual Optimization"
  - "C.32.MLAO:6 — Residual And Trade-Off Failure Modes"
line_start: 64776
line_end: 64792
dependencies:
  - "A.10"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.6.M"
  - "B.2"
  - "B.2.P"
  - "B.3"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.29"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.PAD"
  - "E.10"
  - "E.10.ARCH"
  - "G.5"
keywords:
  - "Pareto front"
  - "declared level"
  - "declared scope"
  - "ideality pressure"
  - "multilevel architecture residual optimization"
  - "residual-reducing candidate frame"
  - "scale amenability"
  - "stepping stone"
---

### C.32.MLAO:6 - Residual And Trade-Off Failure Modes

| Failure mode | C.32.MLAO repair action |
|---|---|
| **Local improvement shifts the residual elsewhere** | Record the scope and selected structure that improved, the scope and selected structure that worsened, and the new burden created. |
| **Universal optimizer is assumed** | Treat optimization as bounded residual reduction over declared holon-level refs or declared scope refs, with comparison inputs, receiving pattern, and stop condition. |
| **Proxy result substitutes for comparison or choice claim** | When a score, vector, graph partition, front, DSM, or C.29 lens output is used to prefer a candidate, name the selected structures, preserved structure, lost structure, architecture characteristic, and receiving pattern. |
| **Level or scale word is not typed** | Recover level, layer, tier, scope, and scale wording through `E.10.ARCH`, `C.30.STRAT`, and `C.16.P` as applicable; recover BOSC, MHT, MET, MFT, and emergence-family wording through `E.10` and `B.2.P` before declaring holon-level refs, scope refs, scale windows, B.2 whole reidentification, or C.32.MLAO residual claims. |
| **Software-source overfit** | Treat software examples as domain lineage; admit other holons only after selected structures and affected scopes are recoverable. |
| **Lossless repair is assumed** | Every residual-reducing candidate names the new burden it creates. |
| **Front member is treated as durable optimum** | A front member is an archive or front relation under an evolution window, not a durable architecture optimum. |
| **Stepping stone is erased too early** | Keep retained stepping stones visible through `C.18` or `C.19` when they preserve future residual-reduction reach. |
| **Transformer-transformed residual is hidden** | A residual between the changing holon and the changed holon must open `C.32.CONWAY`; prepare transformer-side, transformed-side, joint, and bounded-mismatch candidates as comparison inputs or downstream candidate alternatives. |
| **Ideality is used as optimum** | Treat ideality as direction for candidate generation, not as an adequacy claim that a bearer may be removed. |
| **Universal bearer is admitted without scale window** | A general bearer still needs declared criteria rows, scale window, safety and admissibility boundaries, and an eval result when the claim depends on a reading. |
| **Functional graph has no feasible bearer** | A functional architecture that lacks feasible bearers is an unfit candidate, not an optimized architecture. |

