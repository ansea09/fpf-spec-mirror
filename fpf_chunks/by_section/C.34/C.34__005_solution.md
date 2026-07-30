---
chunk_kind: "child"
pattern_id: "C.34"
pattern_title: "Structural Correspondence, Equivalence, and Morphism Adequacy"
section_id: "C.34:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.34/C.34__005_solution.md"
commit_sha: "308edacfa2bdb2c60d07e4e10c0deb1f260a6a31"
heading_path:
  - "C.34 — Structural Correspondence, Equivalence, and Morphism Adequacy"
  - "C.34:4 — Solution"
line_start: 67047
line_end: 67067
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

### C.34:4 - Solution

Create one `StructuralPreservationAdequacyNote@Context` before relying on the same-enough claim.

Read the note as a disciplined "same enough" card. It does not ask for perfect identity unless the use requires it; it asks what must survive for the next architecture action and what loss remains visible.

Work in this order:

1. Name the selected source structures and selected target structures. Do not start from labels, diagrams, or tool objects alone.
2. Name the intended architecture use: view correspondence, candidate comparison, structure recovery, generated-output admission, realization check, eval support, decision repair, or another receiving claim.
3. Choose the weakest mapping mode that is adequate for the use. Use `exactEquivalence` only when empty loss is justified.
4. State preserved relations or constraints in domain and FPF terms. Include relation-type semantics when edge or link meaning changes the use.
5. State lost structure, hidden structure, directionality, and scope or scale window.
6. Cite `C.29` only when a mathematical object, graph match, functor, invariant, entropy, or formal mapping is being used as a lens.
7. Cite `C.30.ASV`, `C.30.AD`, or their correspondence records when the relation is view or architecture-description correspondence.
8. Cite `A.6.3.NAR` when the target structure is a narrative rendering whose ordering rationale, preserved selected source structure, and source-or-governing-pattern return condition must stay inspectable.
9. Cite `F.9` or `F.15` when the claim crosses bounded contexts, source traditions, or later conformance strengthening.
10. Stop when admissible use, non-admissible use, preservation-loss return condition, receiving governing pattern, and receiving claim kind are named.

CGUS-aware neighbor use: when a route-shaped publication card, narrative sequence, generated route card, framework publication, or demonstrative slice is claimed to preserve a constraint-governed unfolding structure, C.34 checks only the sameness relation. It names selected source and target structures, mapping mode, preserved constraints, preserved ordering or branching relations, lost alternatives, directionality, and admissible use. `A.22.CGUS`, `E.18.3`, `C.32.P2S`, `A.6.3.NAR`, or another local governing pattern still governs the selected unfolding `U.Structure`; a `DemonstrativeUnfoldingSlice@Context` is a `U.Episteme` presentation or traversal whose correspondence to that structure may be checked here. C.34 only says whether the target is same enough for the declared architecture use.

