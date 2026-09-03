---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:11"
section_title: "Regression and stability rules"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__013_regression-and-stability-rules.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:11 — Regression and stability rules"
line_start: 98726
line_end: 98738
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
  - "E.10.LRN"
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

### F.17:11 - Regression and stability rules

Recheck only the rows affected by the changed object, name, scheme, sense, Bridge, basis, or source.

| Rule | Trigger | Response when triggered |
| --- | --- | --- |
| UTS-RSCR-01 | Reference-scheme value, local expression, or local-sense claim changes | Preserve the old coordinate when it is still cited and create or cite the new exact coordinate; do not silently reuse the old address. |
| UTS-RSCR-02 | The defining or constraining rule changes the underlying value kind or admissible use | Recheck the governed value, its kind, the applicable pattern, admitted use, and blocked use. |
| UTS-RSCR-03 | F.18 changes the selected name or NameCard decision | Recheck Tech name, Plain name, NameCardRef, aliases, coordinate expression, and rationale. |
| UTS-RSCR-04 | F.9 changes a Bridge endpoint or relation-semantic profile, or C.2.1/A.10/B.3 changes the bounded-use claim or reliance basis | Recheck the changed object only: BridgeRefs for endpoint or profile change; row use, rationale, and notes for changed direction, rule, tolerance, polarity, evidence, reliance, or assurance. |
| UTS-RSCR-05 | Row relocation between blocks | Keep the row id stable and state that relocation between blocks has no ontological force. |
| UTS-RSCR-06 | A system-role, status, evidence, source, publication, or description row is reused under another semantic-context projection or by another reader group | Recheck the pattern that defines or constrains the governed value, the exact sense coordinate, and any required Bridge before reuse. |

