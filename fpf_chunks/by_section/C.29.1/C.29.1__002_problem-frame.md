---
chunk_kind: "child"
pattern_id: "C.29.1"
pattern_title: "Mathematical Result Transfer"
section_id: "C.29.1:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.1/C.29.1__002_problem-frame.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "C.29.1 — Mathematical Result Transfer"
  - "C.29.1:1 — Problem frame"
line_start: 60127
line_end: 60142
dependencies:
  - "A.3.3"
  - "A.6.3.RT"
  - "B.5"
  - "B.5.MPC"
  - "C.29"
keywords:
---

### C.29.1:1 - Problem frame

**Use this when** you have two mathematical accounts of a working situation, or a proposed change of representation, and want to carry a result from one to the other. The difficulty is whether the correspondence preserves the operation, distinction or condition on which that result depends. A stock total is to support reservations; route summaries are to support cost calculations; new coordinates are to make a coupled calculation easier.

Mathematical Lens Use, C.29, covers choosing a mathematical account and returning its consequence to a working question. Within that broader use, this pattern develops transfer of a mathematical result: construct the correspondence, compare the relevant operations, and obtain a consequence that survives the change. The work is to establish when a result obtained in one account can serve as an answer or premise in the other.

**What changes in practice.** Instead of accepting a familiar formula because the symbols look similar, you identify what its inputs represent and show why the intended conclusion follows after the change. The first useful result can be an equality, a sufficient bound, or two allowed cases that the representation merges although they require different answers. That last result tells you what to retain or which question to weaken.

For example, one item on hand can be unreserved or already reserved. Both situations have stock total one, but only one permits another reservation. The pair immediately exposes why total stock cannot by itself decide availability. You can then construct available stock as on-hand stock minus reserved stock and compare the reservation updates in the two accounts.

**Ordinary non-use boundary.** Use a familiar result directly when the correspondence and its conditions are already established for the present use. A symbol rename or conversion under an established notation rule normally needs only A.6.3.RT. If the mathematical object or result is still missing, construct it in the relevant mathematical practice; C.29 helps choose the account and B.5 helps organize the missing reasoning. Transfer cannot provide an absent theorem by itself. If the mathematical relation is established but its physical interpretation or execution remains unresolved, use B.5.MPC to connect those contributions.

Be able to identify what the source quantities mean and follow the operation being transferred, or obtain its explanation from a suitable mathematical contributor. The worked cases explain their elementary constructions.

Enter here with an available proof, calculation, model, summary or proposed mapping. There is no preliminary requirement to repeat lens selection or fill a full lens card.

