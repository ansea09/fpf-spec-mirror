---
chunk_kind: "child"
pattern_id: "C.34"
pattern_title: "Structural Correspondence, Equivalence, and Morphism Adequacy"
section_id: "C.34:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.34/C.34__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "C.34 — Structural Correspondence, Equivalence, and Morphism Adequacy"
  - "C.34:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 65980
line_end: 65991
dependencies:
  - "A.22"
  - "A.6.3.NAR"
  - "A.6.M"
  - "C.16"
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
  - "C.32.PAD"
  - "E.18"
  - "F.15"
  - "F.9"
keywords:
  - "directionality"
  - "equivalence"
  - "lost structure"
  - "mapping mode"
  - "morphism"
  - "preserved structure"
  - "scope"
  - "structural correspondence"
---

### C.34:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair move |
| --- | --- | --- |
| Edge-isomorphism overread | Isomorphic graphs can preserve shape while changing edge meaning, relation observation class, or use. | Record relation-type semantics, preserved relation, lost relation, and non-admissible use. |
| Semantic-loss hiding | A projection or coarsening can look clean because it drops exactly the structure that the next decision needs. | Name lost structure and preservation-loss return condition before comparison, decision repair, or candidate admission. |
| Exact-equivalence overclaim | Exact equivalence is stronger than most architecture uses need and is often false. | Choose the weakest adequate mapping mode: correspondence, projection, abstraction, coarsening, simulation relation, or near-sameness when that is enough. |
| Generated graph proof overclaim | A generated graph can match labels or topology while hiding dynamic wiring, confidence, or unexplored regions. | Use C.34 only for the preservation claim; route generated-carrier admission to `C.35` and evidence, assurance, gate, or release claims to their governing patterns. |
| Narrative-order equivalence overclaim | A narrative can preserve a useful path through selected source structure while dropping alternatives, relation semantics, measurements, or directionality. | Record the weakest adequate correspondence, preserved structure, lost structure, directionality, and non-admissible use; use `A.6.3.NAR` for the narrative rendering relation. |
| Formal lens laundering | A morphism, functor, entropy value, or graph match sounds rigorous but may be local to a mathematical object. | Route lens use to `C.29`; return to C.34 only after preserved structure, lost structure, mapping mode, and architecture use are stated. |
| Bridge-governance bypass | A cross-context or cross-tradition mapping can preserve local structure while losing local sense. | Use `F.9` for the bridge and `F.15` for later regression or conformance strengthening before substitution is relied on. |

