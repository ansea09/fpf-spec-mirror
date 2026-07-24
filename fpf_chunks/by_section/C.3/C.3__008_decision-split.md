---
chunk_kind: "child"
pattern_id: "C.3"
pattern_title: "Kinds, Intent and Extent, and Typed Reasoning"
section_id: "C.3:6"
section_title: "Decision Split"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3/C.3__008_decision-split.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "C.3 — Kinds, Intent and Extent, and Typed Reasoning"
  - "C.3:6 — Decision Split"
line_start: 44138
line_end: 44156
dependencies:
  - "A.1"
  - "A.11"
  - "A.2.6"
  - "A.22.CGUS"
  - "A.6.0"
  - "A.7.1"
  - "A.8"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.2"
  - "C.3.3"
  - "C.3.5"
  - "C.3.A"
  - "E.24.UK"
  - "F.18"
  - "F.8"
  - "F.9"
keywords:
  - "KindBridge"
  - "SubkindOf"
  - "bounded-context local kind"
  - "effective ReferenceScheme"
  - "intent-bearing KindSignature"
  - "optional slice-indexed extension"
  - "three-valued candidate judgment"
---

### C.3:6 - Decision Split

| Current question | Governing pattern |
| --- | --- |
| What local kind does this claim quantify over? | `C.3` and `C.3.1` |
| Is one local kind a subkind of another, or does the same kind continue across a declaration change? | `C.3.1` |
| Does this exact candidate satisfy this local kind under this declaration edition and context slice? | `C.3.2` |
| Does a receiving use need the represented set of true members? | `C.3.2`; `C.29` when the representation itself changes a claim-bearing use |
| Does the assertion hold in a target slice? | `A.2.6` for its `U.ClaimScope`; do not attach that scope to the kind |
| Does a typed claim cross into another bounded context? | `C.3.3` for the `KindBridge` between the exact local kinds; add F.9 only when the local senses also need alignment |
| Did only the effective reference scheme change within one bounded context? | `C.3.2` for another `KindSignature` edition and `C.3.1` for the same-kind continuity decision; the scheme change alone is not a context bridge |
| Did only the context slice change? | `C.3.2` for another judgment input and possible `KindExtension`; the slice change alone is not a context bridge |
| Is the local kind being proposed as a durable public FPF `U.*` kind? | `E.24.UK`, followed by the applicable naming patterns |
| Is a candidate, quality, relation, construction, or work occurrence being identified? | The direct subject pattern; C.3 consumes the governed result and does not create it |

When typed reasoning is part of a structural construction-to-representation passage from a constructive representation or working model to a target kind or logical representation, cite `StructuralCT2RTypingGroundingUnfoldingStructureBlock` from `B.3.5`. C.3 contributes only the local kind, judgment, subkind, and bridge loci inside that B.3.5-governed local `A.22.CGUS` specialization. It does not create separate unfolding-structure authority and does not make a constructive trace, working-model relation, proof, evidence relation, or classification true by label. For a general diagnostic return from an inadequate working account to the exact subject construction, use `A.7.1`; classification remains one possible locus rather than a general ontology-return method.

The unfolding is admitted only when the block names the starting representation, target kind or logical representation, current bridge when one is used, preserved structure, lost or collapsed structure, `CL` or `CL^k`, admissible reuse, blocked substitution, and the proof or evidence governing pattern when that stronger claim is current.

