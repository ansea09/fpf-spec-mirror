---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "Gate Decisions from Independent Check Results"
section_id: "A.21:7"
section_title: "Check the ordinary gate decision"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__009_check-the-ordinary-gate-decision.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "A.21 — Gate Decisions from Independent Check Results"
  - "A.21:7 — Check the ordinary gate decision"
line_start: 35379
line_end: 35399
dependencies:
  - "A.10"
  - "A.15.5"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.20"
  - "B.3"
  - "C.3.2"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.19"
  - "F.6"
  - "F.9"
  - "G.11"
  - "G.6"
keywords:
---

### A.21:7 - Check the ordinary gate decision

1. **Decision.** Name the gate, the action or transition being decided, its scope, and its time window.
2. **Applicable rule.** Point to the profile rule and edition that apply to this gate and subject. Recover its required checks, mappings, consequences, scope and window, and any authority the rule itself requires.
3. **Checks.** For each check, name its subject, criterion and edition, case, requirement, evaluation state, source result, and mapping rule.
4. **Nothing missing.** Keep every required check visible, including `notRun`, `unknown`, error, and failure.
5. **Worst result wins.** Aggregate only after the rule has mapped every required result. A missing or unrun required result cannot support `pass`.
6. **Next action.** State what `pass`, `degrade`, `block`, or `abstain` means for this action and when to decide again.
7. **Boundary.** Do not turn the decision into work-entry readiness or performed Work, and add no crossing, Bridge, publication, or assurance claim that is absent.

#### A.21:7.1 - Triggered additions

| Current use | Add | Direct pattern |
| --- | --- | --- |
| Launch decision | Prospective work-entry claim and only the checks selected by the applicable profile | `A.15.5`, `E.18`, and the pattern defining each check |
| Structural crossing | Changed-binding and crossing facts; SquareLaw only when its crossing rule applies | `E.18` |
| Semantic correspondence | Separate Bridge and bounded-use claim; optional evidence or publication apparatus only when used | `F.9`, `F.17`, `E.17` |
| Publication | Form, carrier, publication occurrence, and the minimum decision refs | `E.17` |
| Evidence, safety, regulation, or assurance | Exact source result and its evidence or assurance relation | `A.10`, `B.3`, or the applicable domain pattern |
| Reuse or replay | Decision log or equivalence witness covering the claimed reuse inputs | `G.6`, `G.11`, and the publication pattern when published |

