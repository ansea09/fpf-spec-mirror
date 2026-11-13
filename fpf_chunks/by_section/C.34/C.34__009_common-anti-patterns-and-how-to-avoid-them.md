---
chunk_kind: "child"
pattern_id: "C.34"
pattern_title: "Assess Structural Correspondence for Architecture Use (Equivalence and Morphisms)"
section_id: "C.34:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.34/C.34__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "C.34 — Assess Structural Correspondence for Architecture Use (Equivalence and Morphisms)"
  - "C.34:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 84870
line_end: 84881
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
| Semantic-loss hiding | A projection or coarsening can look clean because it drops the structure that the next decision needs. | Name lost structure and preservation-loss return condition before comparison, decision repair, or candidate admission. |
| Exact-equivalence overclaim | Exact equivalence is stronger than most architecture uses need and is often false. | Use a warranted correspondence, projection, abstraction, coarsening, simulation relation or near-sameness when sufficient. Exact equivalence may be retained when independently justified. |
| Generated graph proof overclaim | A generated graph can match labels or topology while hiding dynamic wiring, confidence, or unexplored regions. | Use C.34 only for the preservation claim; handle generated-carrier admission under `C.35`, and apply the rules that define evidence, assurance, gate, or release claims when those claims are current. |
| Narrative-order equivalence overclaim | A narrative can preserve a useful path through selected source structure while dropping alternatives, relation semantics, measurements, or directionality. | Record a warranted correspondence sufficient for the use, preserved structure, lost structure, directionality, and non-admissible use; use `A.6.3.NAR` for the narrative rendering relation. |
| Formal result mistaken for architecture adequacy | A morphism, functor, entropy value, or graph match establishes a result under its mathematical conditions; its architecture use also depends on what the mapping preserves. | Establish the preserved structure, any material loss or uncertainty, mapping mode and intended architecture use. Use `C.29` for a remaining mathematical-representation choice, transfer, or reliance question. |
| Bridge-governance bypass | A cross-context or cross-tradition mapping can preserve local structure while losing local sense. | Use `F.9` for the Bridge. Apply `F.15` when the current or changed use needs its conformance tests; reuse an adequate existing result. |

