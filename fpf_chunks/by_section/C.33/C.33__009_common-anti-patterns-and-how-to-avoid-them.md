---
chunk_kind: "child"
pattern_id: "C.33"
pattern_title: "Assess Structural Information for Architecture Use"
section_id: "C.33:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.33/C.33__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "870fb0c2a5dcfe1e0165a111fdf2cf8659c85a54"
heading_path:
  - "C.33 — Assess Structural Information for Architecture Use"
  - "C.33:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 80822
line_end: 80832
dependencies:
  - "A.22"
  - "A.6.3.NAR"
  - "A.6.M"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.2.8"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ADR"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.18"
  - "F.15"
  - "F.9"
  - "G.5"
keywords:
  - "ADR"
  - "captured structure"
  - "diagram"
  - "missing structure"
  - "observer boundary"
  - "partial description"
  - "relation graph"
  - "source return"
  - "structural information adequacy"
---

### C.33:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair move |
| --- | --- | --- |
| Diagram as complete architecture | The diagram may show modules or links while hiding placement, runtime dependency, control authority, evidence structure, bearer constraints, or data custody. | Write the C.33 note from the diagram: captured structure, missing structure, lost relation semantics, admissible use, and the condition that reopens the next dependent claim or question. Add its exact predicate and assertion identity only when that identity must travel independently. |
| ADR as realized structure proof | A decision record can carry decision memory and method expectation without showing what was built or how it behaves. | Use `C.32.PAD` for the project decision claim and `C.32.ADR` for its record projection; use C.33 only for the structural content and loss carried by the record; state realization claims using the exact architecture or evidence predicate and cite the pattern that defines or tests it when that reference is needed. |
| Narrative as complete architecture | A narrative can preserve a route through selected structures while hiding placement, alternatives, measurements, interfaces, or realized structure. | Use `A.6.3.NAR` for the structure-to-narrative rendering relation and C.33 for captured and lost selected structure before architecture reuse. |
| Code-agent graph as safe-change authority | A graph can expose observed and inferred relations while leaving unknown regions and hidden invariants. | Add observation class, confidence, unexplored regions, and non-admissible use. Use the patterns that define the safe-change, assurance, gate, and release checks when those claims are current. |
| Metric as structural adequacy | A score, entropy value, epiplexity estimate, benchmark trace, or dependency F1 supports only the conclusion established by its calculation, measurement or evaluation conditions. | Retain the mathematical model and correspondence needed by a computed value; use `C.16` when measurement is claimed, `C.25` for a current Q-bundle claim, and `C.32.ACE` for architecture evaluation. Use `C.29` for an unresolved mathematical-representation choice, transfer, or reliance question. |
| Neural label import | Terms such as attention, SSM, router, expert, cache, pruning, distillation, and NAS can hide several structure kinds and characteristics. | Recover the selected structure kind, relation, bearer, affected characteristic, preserved structure, and lost structure needed by the architecture claim, and identify the next claim plus the rule or test it needs before relying on the label for that use. |

