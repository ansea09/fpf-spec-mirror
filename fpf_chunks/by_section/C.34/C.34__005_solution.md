---
chunk_kind: "child"
pattern_id: "C.34"
pattern_title: "Assess Structural Correspondence for Architecture Use (Equivalence and Morphisms)"
section_id: "C.34:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.34/C.34__005_solution.md"
commit_sha: "dba39812b83cac74dd2a3251c134cdc23dfaec86"
heading_path:
  - "C.34 — Assess Structural Correspondence for Architecture Use (Equivalence and Morphisms)"
  - "C.34:4 — Solution"
line_start: 85105
line_end: 85135
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

State the decision that will use the correspondence. Identify the entities being matched and the relation on which the decision depends. A conclusion about the source carries over in the direction for which the mapping preserves the facts needed to reach it. To infer absence in the target from absence in the source, also show why any relevant target occurrence would have a source counterpart. Extra target connections can change the answer.

For a grouping, ask how membership is determined. If both models define membership by the same rule and the correspondence preserves everything that rule uses, derive the target grouping. If membership is assigned independently, inspect the assignments or an applicable allocation rule and the facts it uses. For an assignment whose preservation is in doubt, keep the matched entities and links fixed. Could two different assignments fit them? When this changes who may act, the correspondence alone leaves that decision open. Correspondence between two disciplinary models can matter even when both are at L2. A claim of model refinement has its own test in `B.5.MR:4.3`.

When reviewing a comparison someone produced, distinguish the correspondence supplied in the assignment from the choices the person or AI agent made. Applying a supplied match can establish that the comparison gave the right result. To credit someone with constructing a disciplinary model of correspondence, recover how they selected the entities, interpreted the links and justified the matching rule for further comparisons. An earlier decision record can show those choices. A new task can leave them open. Use `C.39.QR:4.3` when the attribution changes what you entrust to the agent.

Work in this order:

1. Name the selected source structures and selected target structures. Do not start from labels, diagrams, or tool objects alone.
2. Name the intended architecture use: view correspondence, candidate comparison, structure recovery, generated-output admission, realization check, eval support, decision repair, or another receiving claim.
3. Select a warranted mapping mode sufficient for the use. A weaker sufficient correspondence can finish the work; an already established stronger result can be reused within its scope. Use `exactEquivalence` only when preservation of the entire selected structure is established within the declared scope.
4. State preserved relations or constraints in domain terms. Use FPF distinctions where the claim depends on them. Include relation-type semantics when edge or link meaning changes the use.
5. State directionality and scope or scale window, with any material lost or hidden structure. Distinguish an observed loss from preservation left unestablished by incomplete observation. Neither supports a claim requiring the missing preservation, but each selects a different next inquiry or repair.
6. Retain the mathematical definition, mapping and proof conditions needed by a formal preservation claim. Use `C.29` when choosing, transferring, or relying on that mathematical representation remains unresolved.
7. Cite `C.30.ASV`, `C.30.AD`, or their correspondence records when the relation is view or architecture-description correspondence.
8. Cite `A.6.3.NAR` when the target episteme or representation is a narrative rendering whose ordering rationale, preserved selected source structure, source-return condition, and any unresolved stronger assertion with the pattern that defines it must stay inspectable.
9. Use `F.9` for cross-context or cross-tradition substitution or claim transport that requires a Bridge. Use `F.15` when the receiving use needs its static or regression conformance tests.
10. Stop when the supported use and its grounds are clear, with any material limitation and the condition for resolving it. Apply an additional mapping, Bridge or conformance rule when that use requires it.

CGUS-aware neighbor use: when a route-shaped publication card, narrative sequence, generated route card, framework publication, or demonstrative slice is claimed to preserve a constraint-governed unfolding structure, use C.34 only to check the sameness relation. The result names selected source and target structures, mapping mode, preserved constraints, preserved ordering or branching relations, lost alternatives, directionality, and admissible use.

`A.22.CGUS`, `E.18.3`, `C.32.P2S`, or another structure pattern continues to define or constrain the selected unfolding `U.Structure`; cite a `ClaimGraph` only if that structure claim must travel independently.

A demonstrative slice is a `U.Episteme` that presents one traversal of a qualified CGUS. Its correspondence to that structure may be checked here; `DemonstrativeUnfoldingSlice@Context` is a lineage cue, not a slice identity.

When that presentation is a narrative, `A.6.3.NAR` defines its source selection, ordering and connective account, preservation/loss, use, and return, not the selected structure.

The C.34 result says only whether the target is same enough for the declared architecture use.

