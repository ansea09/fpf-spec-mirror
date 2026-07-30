---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:10"
section_title: "Static conformance rules for a UTS"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__012_static-conformance-rules-for-a-uts.md"
commit_sha: "308edacfa2bdb2c60d07e4e10c0deb1f260a6a31"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:10 — Static conformance rules for a UTS"
line_start: 94232
line_end: 94250
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
  - "E.17"
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
  - "U.BoundedContext"
keywords:
---

### F.17:10 - Static conformance rules for a UTS

Use these checks before citing a UTS row outside its local sheet.

| Rule | Check |
| --- | --- |
| UTS-SCR-01 | Every row has row id, unification-thread id, block, governed value, governed value kind, direct pattern, Tech name, Plain name, scheme-based sense-cell refs, row rationale, admissible use, blocked use, row edition, and currentness condition. |
| UTS-SCR-02 | A row names one governed term decision. If the wording hides multiple typed values, split the row or cite the direct pattern that keeps them distinct. |
| UTS-SCR-03 | Every local sense resolves to one exact by-value reference scheme, local expression, and local-sense claim; no context holon is required or inferred. |
| UTS-SCR-04 | A row that proposes use between different semantic-context projections cites an obtaining F.9 Bridge for the exact endpoint cells and editions, then separately cites an affirmative C.2.1 claim for the row's exact use, direction, correspondence rule, and loss tolerance; current reliance follows the exact A.10 or B.3 branch. Apply four probes: same scheme plus same `LocalSenseClaim` plus a different expression routes to designation and no Bridge; same scheme plus a different `LocalSenseClaim` opens the F.9 question and, for a named row use, the separate claim-and-reliance branch; a different scheme opens only the Bridge question and never establishes one; no current correspondence use creates no Bridge or use claim regardless of scheme count. A negative bounded-use claim rejects the exact named row use; a non-passing reliance result stops or narrows the current use according to its exact A.10 or B.3 disposition; neither changes whether the Bridge obtains or how it is identified. |
| UTS-SCR-05 | The Tech and Plain names satisfy F.5 and F.18; spelling or a familiar context label supplies neither local-sense identity nor a Bridge. |
| UTS-SCR-06 | A role row names `U.Role` or a governed role value; it does not treat RoleDescription, RoleAssignment, capability, method, or work as the same value. |
| UTS-SCR-07 | A status row names the status-family or status-window value governed by F.10 or A.19.SPR; it does not create a role. |
| UTS-SCR-08 | Evidence, assurance, source, publication, and description-use rows cite their direct patterns and do not become generic evidence roles. |
| UTS-SCR-09 | Blocks remain didactic. No subtype, part-of, role, status, or priority claim follows from block placement. |
| UTS-SCR-10 | The sheet states the scheme and reader breadth actually tested. A narrow row does not claim universal or corpus-wide reuse. |

Passing the row schema is not the value criterion. A row succeeds only when its intended readers can recover the correct governed value and direct pattern for the declared use and avoid the blocked use. Row count, filled-cell count, label uniformity, block neatness, and stable identifiers are maintenance aids, not evidence that the term decision is useful or semantically adequate.

