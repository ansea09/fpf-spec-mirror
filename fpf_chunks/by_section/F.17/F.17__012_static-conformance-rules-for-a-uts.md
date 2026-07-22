---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:10"
section_title: "Static conformance rules for a UTS"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__012_static-conformance-rules-for-a-uts.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:10 — Static conformance rules for a UTS"
line_start: 92231
line_end: 92249
dependencies:
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
  - "C.2.P"
  - "E.10"
  - "E.10.D2"
  - "E.10.MOVE"
  - "E.11"
  - "E.17"
  - "F.1"
  - "F.1-F.12"
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

Use these checks before citing a UTS row outside its local sheet.

| Rule | Check |
| --- | --- |
| UTS-SCR-01 | Every row has row id, unification-thread id, block, governed value, governed value kind, direct pattern, Tech name, Plain name, sense-cell refs, row rationale, admissible use, blocked use, row edition, and currentness condition. |
| UTS-SCR-02 | A row names one governed term decision. If the wording hides multiple typed values, split the row or cite the direct pattern that keeps them distinct. |
| UTS-SCR-03 | Every local sense is scoped to bounded context and edition. |
| UTS-SCR-04 | Every cross-context sameness, near-identity, retargeting, or loss claim cites `F.9`. |
| UTS-SCR-05 | The Tech and Plain names satisfy `F.5` and `F.18`; they are not lifted from one local context unless the bridge and rationale justify that choice. |
| UTS-SCR-06 | A role row names `U.Role` or a governed role value; it does not treat RoleDescription, RoleAssignment, capability, method, or work as the same value. |
| UTS-SCR-07 | A status row names the status-family or status-window value governed by `F.10` or `A.19.SPR`; it does not create a role. |
| UTS-SCR-08 | Evidence, assurance, source, publication, and description-use rows cite their direct patterns and do not become generic "evidence roles". |
| UTS-SCR-09 | Blocks remain didactic. No subtype, part-of, role, status, or priority claim follows from block placement. |
| UTS-SCR-10 | The sheet as a whole shows enough context breadth for its claim. If breadth is narrow, the sheet says so. |

Passing the row schema is not the value criterion. A row succeeds only when its intended readers can recover the correct governed value and direct pattern for the declared use and avoid the blocked use. Row count, filled-cell count, label uniformity, block neatness, and stable identifiers are maintenance aids, not evidence that the term decision is useful or semantically adequate.

