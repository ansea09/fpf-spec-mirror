---
chunk_kind: "child"
pattern_id: "C.34"
pattern_title: "Assess Structural Correspondence for Architecture Use (Equivalence and Morphisms)"
section_id: "C.34:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.34/C.34__005_solution.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "C.34 — Assess Structural Correspondence for Architecture Use (Equivalence and Morphisms)"
  - "C.34:4 — Solution"
line_start: 80151
line_end: 80169
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

Establish what must survive for the next architecture action and what the correspondence preserves. State any material loss or uncertainty. Use the optional note when it helps retain or share that account.

Work in this order:

1. Name the selected source structures and selected target structures. Do not start from labels, diagrams, or tool objects alone.
2. Name the intended architecture use: view correspondence, candidate comparison, structure recovery, generated-output admission, realization check, eval support, decision repair, or another receiving claim.
3. Select a warranted mapping mode sufficient for the use. A weaker sufficient correspondence can finish the work; an already established stronger result can be reused within its scope. Use `exactEquivalence` only when preservation of the entire selected structure is established within the declared scope.
4. State preserved relations or constraints in clear domain terms. Use FPF distinctions where the claim depends on them. Include relation-type semantics when edge or link meaning changes the use.
5. State directionality and scope or scale window, with any material lost or hidden structure. Distinguish an observed loss from preservation left unestablished by incomplete observation. Neither supports a claim requiring the missing preservation, but each selects a different next inquiry or repair.
6. Cite `C.29` only when a mathematical object, graph match, functor, invariant, entropy, or formal mapping is being used as a lens.
7. Cite `C.30.ASV`, `C.30.AD`, or their correspondence records when the relation is view or architecture-description correspondence.
8. Cite `A.6.3.NAR` when the target episteme or representation is a narrative rendering whose ordering rationale, preserved selected source structure, source-return condition, and any unresolved stronger assertion with the pattern that defines it must stay inspectable.
9. Use `F.9` for cross-context or cross-tradition substitution or claim transport that requires a Bridge. Use `F.15` when the receiving use needs its static or regression conformance tests.
10. Stop when the supported use and its grounds are clear, with any material limitation and the condition for resolving it. Apply an additional mapping, Bridge or conformance rule when that use requires it.

CGUS-aware neighbor use: when a route-shaped publication card, narrative sequence, generated route card, framework publication, or demonstrative slice is claimed to preserve a constraint-governed unfolding structure, use C.34 only to check the sameness relation. The result names selected source and target structures, mapping mode, preserved constraints, preserved ordering or branching relations, lost alternatives, directionality, and admissible use. `A.22.CGUS`, `E.18.3`, `C.32.P2S`, or another direct structure pattern continues to define or constrain the selected unfolding `U.Structure`; cite an exact `ClaimGraph` only if that structure claim must travel independently. A demonstrative slice is a `U.Episteme` that presents one traversal of a qualified CGUS. Its correspondence to that structure may be checked here; `DemonstrativeUnfoldingSlice@Context` is a readable lineage cue, not an exact slice identity. When that presentation is a narrative, `A.6.3.NAR` defines its source selection, ordering and connective account, preservation/loss, use, and return, not the selected structure. The C.34 result says only whether the target is same enough for the declared architecture use.

