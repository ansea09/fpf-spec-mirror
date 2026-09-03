---
chunk_kind: "child"
pattern_id: "C.31.RSA"
pattern_title: "Reusable Structure Accounting"
section_id: "C.31.RSA:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31.RSA/C.31.RSA__008_conformance-checklist.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "C.31.RSA — Reusable Structure Accounting"
  - "C.31.RSA:7 — Conformance Checklist"
line_start: 63044
line_end: 63060
dependencies:
  - "A.10"
  - "A.19"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.31"
  - "C.31.ASAP"
  - "G.5"
  - "G.6"
keywords:
  - "accounting basis"
  - "bespoke residue"
  - "refactoring opportunity"
  - "report-only share"
  - "reusable share"
  - "reusable-structure accounting"
  - "source return"
---

### C.31.RSA:7 - Conformance Checklist

| ID | Check |
| --- | --- |
| `CC-C31.RSA-1` | The text starts from `ReusableStructureTriage` unless an accounting basis and structure refs are already named. |
| `CC-C31.RSA-2` | Any accounting description names `accountingBasisRef`, `structureRefs`, `structuralAspectRefs`, reusable slots, bespoke residue slots, residual uncertainty slots, admissible use, and non-admissible use. |
| `CC-C31.RSA-3` | Report-only shares are marked report-only unless every outside-RSA use being made and named in the claim-use boundary is governed by its governing pattern. |
| `CC-C31.RSA-4` | No text treats RSA as proof of modularity, quality, or any outside-RSA use named in the claim-use boundary. |
| `CC-C31.RSA-5` | Heterogeneous slot labels are not summed unless a declared accounting basis and aggregation rule make the operation admissible. |
| `CC-C31.RSA-6` | Each bespoke residue interpretation states a repair direction, bounded-exception condition, source-return condition, or governing-pattern application. |
| `CC-C31.RSA-7` | Evidence reuse and assurance reuse apply `A.10`, `B.3`, or `G.6` when validity, assurance, or safety-case reliance is being claimed. |
| `CC-C31.RSA-8` | RSA does not duplicate the C.31 characteristic taxonomy; it uses C.31 only when a modularity characteristic under evaluation, such as bespoke residue, evidence reuse, or residual uncertainty, must govern the accounting interpretation. |
| `CC-C31.RSA-9` | Source-return condition is present when accounting hides action-relevant source distinctions. |
| `CC-C31.RSA-10` | Outside-RSA comparison, ranking, selection, gate use, or decision use names comparator admission named by value such as `CG-Spec`, `ComparatorSetRef`, or a comparator-governing reference named by value; otherwise the RSA share remains report-only. |
| `CC-C31.RSA-11` | The RSA note names reopen or lowering conditions for source distinction change, accounting-basis change, structure-edition change, implicit-interface change, comparator change, evidence or assurance decay, downstream reliance, repeated bounded exception, and reuse move side effects when those conditions are needed for the record. |
| `CC-C31.RSA-12` | Source labels such as block, layer, expert, cache, router, gate, or pruning mask use `C.30.STRAT` before they become `structureRefs`, `structuralAspectRefs`, accounting-basis fields, repair actions, or source-return conditions. |

