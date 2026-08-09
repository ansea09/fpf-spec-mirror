---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:10"
section_title: "Static conformance rules for a UTS"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__012_static-conformance-rules-for-a-uts.md"
commit_sha: "036c056e98c38522172c6b7b3ad08214281cc4e4"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:10 — Static conformance rules for a UTS"
line_start: 95994
line_end: 96015
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

### F.17:10 - Static conformance rules for a UTS

Use these checks before citing a row outside its immediate sheet.

| Rule | Check |
| --- | --- |
| UTS-SCR-01 | The row resolves to one C.2.1 row episteme whose EntityOfConcern is one exact governed value; it points separately to that value's kind, the pattern that defines or constrains it, and the exact F.18 naming-settlement episteme. |
| UTS-SCR-02 | One row carries one naming decision and one governed value/use branch; mixed values or independently different uses are split. |
| UTS-SCR-03 | Every local sense resolves to one exact by-value ReferenceScheme, local expression, and local-sense claim; id, description, source publication, card, or basis relation replaces none of them. |
| UTS-SCR-04 | F.14 was applied before the current card, cell, and row; the light dispositions—no durable name, existing designation, alias, local expression, a name already used for the value, and admitted row reuse—were tested first. |
| UTS-SCR-05 | The Tech and Plain designation expressions agree with the exact current F.18 NameCard without becoming the governed value; aliases and rejected candidates remain separate. |
| UTS-SCR-06 | Any cited `LocalSenseBasisRelation` has only its exact cell and basis episteme as participants; source-unit and publication facts remain qualifiers or neighboring objects. |
| UTS-SCR-07 | Apply all four Bridge probes: same scheme plus same `LocalSenseClaim` plus another expression is a designation question and adds no Bridge; same scheme plus a different claim opens F.9 and, only for a named row use, the separate use-claim/reliance branch; a different scheme opens only the Bridge question and establishes none; no current correspondence use creates no Bridge or use claim regardless of scheme count. |
| UTS-SCR-08 | Any cited F.9 Bridge has exact endpoint cells and editions, an applicable relation-semantic profile, a true kind-defined predicate, and every required dependency. The separate affirmative C.2.1 use claim states direction, correspondence rule, and loss tolerance, with current A.10 or B.3 reliance. A negative use claim rejects that exact row use; non-passing reliance stops or narrows it; neither negates or reidentifies an otherwise obtaining Bridge. |
| UTS-SCR-09 | A role row does not identify RoleDescription, RoleAssignment, capability, method, or Work with the governed role value; a status row does not turn a status family, value, or window into a role. |
| UTS-SCR-10 | Evidence, assurance, source, publication, description, relation, slot, interface, authority, and equivalence claims use the patterns that define, constrain, or test them rather than becoming row truth. |
| UTS-SCR-11 | Row id, block, table position, source title, file, carrier, suffix, and filled-cell count create neither value identity nor row adequacy. |
| UTS-SCR-12 | The row states the exact scheme, receiving use, and reader breadth actually checked; a narrow row claims neither universal nor corpus-wide reuse. |
| UTS-SCR-13 | C.2.1 row succession and E.24.PUB availability are independently recovered; row, edition relation, publication occurrence, form, carrier, rendering Work, and upload Work stay distinct. |

Passing the schema is not the value criterion. A row succeeds only when intended readers can recover the correct naming decision, governed value, and applicable defining or constraining rule for the declared use while avoiding the blocked use. Row count, filled-cell count, label uniformity, block neatness, and stable identifiers are maintenance aids only.

