---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local-First Unification Naming Protocol"
section_id: "F.18:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__006_solution.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "F.18 — Local-First Unification Naming Protocol"
  - "F.18:4 — Solution"
line_start: 81743
line_end: 81827
dependencies:
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "A.6.RSIR"
  - "C.2.P"
  - "E.10"
  - "F.0.1"
  - "F.1"
  - "F.1-F.17"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.8"
  - "F.9"
  - "G.10"
  - "G.2"
  - "G.6"
keywords:
---

### F.18:4 - Solution

Use a local-first naming protocol:

1. Recover the governed value and its direct governing pattern.
2. Decide whether the name is only local wording or a durable reusable name.
3. If durable, create or update a `NameCard`.
4. Choose the Tech label and Plain label from a visible candidate set.
5. Record why the selected pair is better for the declared use than rejected candidates.
6. Use `F.17` only when the name needs public, Core-facing, durable, or cross-context publication.
7. Keep bridge, status, evidence, slot, role, method, work, and interface claims in their own governing patterns.

#### F.18:4.1 - Naming Invariants

Every durable name must satisfy these invariants.

| Invariant | Required content |
| --- | --- |
| Governed value first | Name the governed value or value family before naming the label. |
| Governing pattern visible | Cite the pattern that owns the value: for example `A.2` for role value, `A.2.1` for role assignment, `A.6.5` for relation slot discipline, `F.10` or `A.19.SPR` for status value use, `A.10` for evidence use. |
| Bounded context visible | The name lives in one bounded context or in a declared cross-context publication row. |
| Local sense visible | The name resolves to a local sense, Concept-Set row, or direct-pattern value. |
| Two labels when reusable | The Tech label is precise; the Plain label helps ordinary readers. Both point to the same governed value. |
| Candidate comparison visible | At least two plausible head families are considered unless a cited external standard fixes the label. |
| Bridge only for cross-context sameness | A spelling match does not establish sameness. |
| Lineage visible | Rename, split, merge, retirement, and alias decisions are recorded. |

#### F.18:4.2 - `NameCard` Fields

Use this compact form when a durable name is live:

```text
NameCard:
  NameCardId:
  GovernedValueRef:
  GoverningPatternRef:
  BoundedContextRef:
  LocalSenseRef:
  TechLabel:
  PlainLabel:
  CandidateSet:
  RejectedCandidates:
  SelectionRationale:
  BridgeRefs:
  UnifiedTermRowRef:
  LineageEntries:
  RefreshCondition:
```

Field discipline:

- `GovernedValueRef` names the value, relation, slot, claim record, or local concept being named. It is not a row id by default.
- `GoverningPatternRef` names the pattern that decides the value, not the pattern that merely publishes or teaches the name.
- `CandidateSet` records the plausible labels considered, grouped by head-term family.
- `RejectedCandidates` records why tempting names were not selected.
- `UnifiedTermRowRef` is present only when `F.17` term-row publication is current.
- `RefreshCondition` says when the name must be reconsidered: context edition change, bridge change, governing-pattern change, or repeated reader error.

#### F.18:4.3 - Candidate Selection

Do not pick a durable label in one stroke. Build a small candidate set, normally five to ten candidates, from at least two head-term families. Judge candidates on:

- semantic fidelity: does the label preserve the governed value without adding or losing required conditions?
- reader ergonomics: can the intended reader say and remember it?
- morphology fit: does the word shape fit the kind being named, for example role value, method, work, description, relation, slot, characteristic, or status value?
- alias risk: will a careful reader import a wrong sense from nearby FPF patterns or external practice?

Use these as ordinal comparisons. Do not average them into one score. If a Pareto-front or quality-diversity method is used, the dimensions and dominance rule must be visible on the card.

One candidate can win even when it is not perfect, but the `SelectionRationale` must say what it buys and what risk remains.

#### F.18:4.4 - Public Term Rows

Use `F.17` when the name becomes public, Core-facing, durable across contexts, or cross-context. The term row carries the publication object:

- row id;
- governed object kind or governed value reference;
- direct governing pattern;
- Tech and Plain labels;
- sense cells;
- bridge references;
- edition and currentness condition.

The term row is not the governed value. A row for `ReviewerRole` publishes the role name; it does not create the role. A row for `EvidenceUseRelation` publishes a relation name; it does not make an episteme into a role. A row for `SlotKind` or `EndpointSlot` publishes slot vocabulary; it does not create a generic interface ontology.

