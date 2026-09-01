---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:6"
section_title: "Reasoning Checks"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__008_reasoning-checks.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:6 — Reasoning Checks"
line_start: 95009
line_end: 95025
dependencies:
  - "A.11"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.6.RCD"
  - "A.7"
  - "A.8"
  - "C.11"
  - "C.2.1"
  - "C.3"
  - "E.10"
  - "E.10.ARCH"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.24.UK"
  - "E.9"
  - "F.1"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.8"
  - "F.9"
keywords:
  - "admission before naming"
  - "alias"
  - "designation"
  - "durable naming"
  - "governed value or relation"
  - "local phrase"
  - "proposed naming use"
  - "row use"
  - "subject before name"
---

### F.8:6 - Reasoning Checks

Use these as reading checks, not as a required notation or record.

| Situation | Decision |
| --- | --- |
| The expression is present but the governed value or relation is not known. | Stop F.8. Use E.10 for phrase repair or the subject-recovery route for the object. |
| The expression, governed value or relation, subject pattern, and proposed use are present. | Choose the lightest disposition for that value and use. The naming decision neither establishes the value nor makes a relation obtain. |
| A local phrase or existing designation is sufficient. | Stay local or reuse it; create no cell, NameCard, row, or identifier. |
| An alias is proposed. | Preserve the governed kind, scope, occurrence identity, admitted use, and lineage to the selected designation. |
| The same spelling appears under another ReferenceScheme or local-sense claim. | Infer neither sameness nor an F.9 Bridge. Use a Bridge only when its predicate obtains between the relevant F.17 cells. |
| `L` is proposed for a local system-role kind `K`. | A.2 and C.3 govern `K`; F.5 governs `L`; F.18 opens only for a durable settlement. F.4 is used only for a separately needed description `D`, while A.2.1 governs any assignment `A`. For precise performed Work, A.13 first recovers the exact actual performer and A.15.1 independently admits the Work; F.6 is added only when this naming case or receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment. |
| A role-like expression is actually about another governed use—for example, evidence, status, policy, source, publication, or a relation position. | Recover that subject through its pattern before selecting a durable designation. |
| An F.17 row is proposed for reuse. | Reuse it only for its `AdmissibleUse`; the row supplies neither equivalence nor a wider use. |
| A receiving claim needs the decision occurrence itself. | Use §4.5. Recover the decision or choice pattern, predicate, participants, applicability, and identity basis. If no such governor is available, return `missing-governor`; keep any C.11 result and decision-making Work separate. |
| An expression is offered as a new U-kind before E.24.UK has settled admission. | Return `blockOrLowerUse`. Use E.24.CD if the governed object is unclear and send any surviving U-kind proposal to E.24.UK. Re-enter F.8 only for the object identified by the stable result. |

