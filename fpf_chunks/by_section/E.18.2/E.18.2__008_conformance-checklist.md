---
chunk_kind: "child"
pattern_id: "E.18.2"
pattern_title: "Transformation Flow Mathematical Description"
section_id: "E.18.2:5"
section_title: "Conformance checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.2/E.18.2__008_conformance-checklist.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "E.18.2 — Transformation Flow Mathematical Description"
  - "E.18.2:5 — Conformance checklist"
line_start: 86882
line_end: 86894
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.6.0"
  - "A.6.5"
  - "B.3"
  - "C.2.1"
  - "C.29"
  - "C.30"
  - "C.30.TFS-REL"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.18.3"
  - "E.18.NET"
  - "U.Episteme"
  - "U.Signature"
  - "U.Transformation"
keywords:
---

### E.18.2:5 - Conformance checklist

- `CC-E18.2-1` The current EntityOfConcern is `TransformationFlowMathematicalDescription@Context`, not the selected E.18 TFS or E.18.NET network itself.
- `CC-E18.2-2` Exactly one described ontic subject branch is present: `DescribedTransformationFlowStructureRef?` or `DescribedTransformationFlowStructureNetworkRef?`. The optional `DescribedSliceOrLocusRef?` resolves through the selected E.18 or E.18.NET subject and does not duplicate its fields.
- `CC-E18.2-3` The mathematical expression family is named without minting a new U-kind.
- `CC-E18.2-4` Preserved structure, lost structure, declared use, and boundary stop are named when the expression is claim-bearing.
- `CC-E18.2-5` C.29 is used when mathematical-lens adequacy, payoff, obstruction, preserved/lost structure, or stop condition is being evaluated beyond the local description relation.
- `CC-E18.2-6` Graph, path, slice, morphism, algebra, category, tuple, quotient, fold, refinement, factorization, wiring, and network-expression language stays mathematical-description language unless the practitioner has independently selected the ontic subject by applying E.18 or E.18.NET.
- `CC-E18.2-7` No mathematical expression proves work occurrence, authorizes action, passes a gate, settles evidence, or establishes architecture adequacy by itself.
- `CC-E18.2-8` A rendered graph, table, equation, diagram, or other publication face remains separate from the mathematical description and is handled through `E.17`; changing it alone reidentifies neither the description nor its selected TFS or network subject.
- `CC-E18.2-9` When selected TFS, selected network, work, method, mechanism, signature, evidence, gate, decision, architecture, function, module-interface, or reusable-structure claims are current, apply the exact contribution named for that claim in §4.4 and keep the result it returns. E.18.2 records only the mathematical-description relation for one already selected ontic subject.
- `CC-E18.2-10` A source expression or publication face that carries several claims is split into records by current EntityOfConcern and relation position, not by the expression's or publication's name.

