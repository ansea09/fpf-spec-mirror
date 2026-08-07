---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:7"
section_title: "Row schema"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__009_row-schema.md"
commit_sha: "1602a8d0a6934a99a79ead914610b070cedd86d2"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:7 — Row schema"
line_start: 95793
line_end: 95822
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.19.SPR"
  - "A.2"
  - "A.2.1"
  - "A.2.7"
  - "A.22.CGUS"
  - "A.6.5"
  - "A.6.P"
  - "B.3"
  - "C.2.1"
  - "C.2.P"
  - "E.10"
  - "E.10.D2"
  - "E.10.MOVE"
  - "E.11"
  - "E.17.0"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
  - "G.11"
keywords:
---

### F.17:7 - Row schema

Use these positions when they are current. Presence means that the exact referenced object or claim is independently recoverable; it is not a form-completion target.

| Position | Presence condition | Meaning |
| --- | --- | --- |
| `UTSRowId` | yes | Stable row designator; an external row reference must resolve the exact C.2.1 episteme rather than trust this string. |
| `Unification thread` | yes | Sheet-local navigation designator with no locality or ontology force. |
| `Block` | optional | Didactic navigation label only. |
| `Governed value` / C.2.1 `EntityOfConcern` | yes | Exact independently governed value named by the decision. |
| `NameCardRef` | yes at the current F.18 public-row gate | Separate C.2.1 naming-settlement episteme whose selected designations this row projects. |
| `Governed value kind` | yes | Exact kind of that value; `U.Kind` when the value is a kind token. |
| `Defining or constraining pattern` | yes | Pattern whose rules define or constrain the value, its kind, its identity, or any obtaining semantics used by the row. |
| `Reference scheme` | yes | Effective by-value naming `U.ReferenceScheme` used in this row's C.2.1 constitution. |
| `Unified Tech name` | yes | Selected Tech designation expression. |
| `Unified Plain name` | yes | Selected Plain designation expression. |
| `SenseCellRefs` | one or more | Exact scheme-based local-sense coordinates needed by this row. |
| `BridgeRefs` | only for an actual cross-local relation used by the row | Exact obtaining F.9 occurrences; the separate use claim and reliance stay in rationale or notes. |
| `Row rationale` | yes | Why these projections form one row decision. |
| `Admissible use` | yes | Exact citation use supported by the row; it grants no authorization or occurrence. |
| `Not this use` | yes | Nearest tempting overread that remains blocked. |
| `Row edition id` | yes | Designator for this exact row episteme edition. |
| `EpistemeEditionRelationRef` | only when C.2.1 historical continuation obtains | Separate relation from an exact earlier row episteme to this later one. |
| `Currentness condition` | yes | Claim stating what reopens review; not a self-proving currentness relation. |
| `Notes` | optional | Short lineage, teaching, homonym, use-claim, or reliance note. |

For `SenseCellRefs`, recover the exact by-value scheme, expression, and local-sense claim. Cite `LocalSenseBasisRelation` only when an actual basis relation obtains. A NameCard selects designations; it does not fill the cell or basis positions. A source title, file, carrier, locality label, selected structure, row id, or description substitutes for none of them.

Publication availability is not a row column. When current, maintain the exact E.24.PUB relation occurrences, form, carrier, audience, and bounded use beside the selected row edition. Publication change does not silently change the row episteme or its C.2.1 edition relation.

