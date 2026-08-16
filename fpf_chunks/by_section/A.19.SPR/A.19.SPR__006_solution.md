---
chunk_kind: "child"
pattern_id: "A.19.SPR"
pattern_title: "State-Family Precision Restoration"
section_id: "A.19.SPR:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SPR/A.19.SPR__006_solution.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "A.19.SPR — State-Family Precision Restoration"
  - "A.19.SPR:4 — Solution"
line_start: 29083
line_end: 29151
dependencies:
  - "A.10"
  - "A.16"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.20"
  - "A.21"
  - "A.3.3"
  - "A.6.P"
  - "B.3"
  - "C.16"
  - "C.16.P"
  - "C.16.Q"
  - "C.2.2a"
  - "C.2.P"
  - "C.27"
  - "C.29"
  - "C.30.P"
  - "E.10"
  - "E.10.ARCH"
  - "E.11"
  - "E.17"
  - "E.19"
  - "E.21"
  - "E.8"
  - "E.9.DA"
  - "F.18"
keywords:
---

### A.19.SPR:4 - Solution

Repair state-family wording by producing a `StateFamilyPrecisionRepair` or an equivalent local rewrite.

Minimum shape:

```text
StateFamilyPrecisionRepair:
  triggerSpan:
  boundedTextSpan:
  bearerRef:
  stateFrameOrPatternLocator:
  stateValueOrClassification:
  criteriaOrEvidenceRef?:
  admissibleUse:
  nonAdmissibleOverread:
  validityWindowOrReopenCondition?:
  finalWordingOrBlocker:
  remainingReaderUse:
```

Use the full shape only when the repair must remain inspectable. A direct rewrite is enough when one sentence names the bearer, state frame, value, use boundary, and subject pattern.

#### A.19.SPR:4.1 - Recovery sequence

1. **Capture trigger and bounded text.** Copy the encountered state-family word and the sentence, row, card, or field that uses it.
2. **Recover the bearer.** Name the item whose state-like value is being claimed: holon, role, source, evidence path, assurance claim, publication face, `PublicationUnit`, gate record, temporal claim, lens-use card, `DRR`, pattern version, project-side administrative record, review record, dispatch record, release or admission record, source-control record, or another FPF kind named by value.
3. **Recover the state frame or subject pattern.** Decide whether the frame is `A.19` `CharacteristicSpace`, `A.3.3` dynamics, `A.2.5` system-role-assignment-state assertion, `C.2.2a` language-state chart, `A.10` evidence path, `B.3` assurance, `A.20` constraint or adjudication state, `A.21` gate decision, `E.17` publication use, `C.27` temporal-claim state, `C.29` lens-use admissibility, `E.9.DA` DRR-decision adequacy, `E.21` pattern quality, or a project-side administrative, review, dispatch, release, admission, or source-control record.
4. **Recover the value set or classification.** If a local field remains, list its possible values or the neighboring pattern governing that claim that defines them. If no value set is recoverable, do not keep the state-family head as a field.
5. **Recover criteria or evidence only when that claim is being made.** Name threshold rule, observation, source currentness, evidence path, assurance tuple, validation regime, gate record, or witness only when the subject pattern for that claim is selected.
6. **State admissible and non-admissible use.** Say what the reader may do with this value and what adjacent claim remains blocked.
7. **State validity window or reopen condition.** If currentness, readiness, release or admission, validation, assurance, or administrative state can decay, name what changes the value.
8. **Rewrite or demote.** Replace broad wording with the state-like field or subject-pattern phrase named by value; otherwise mark quote-only, reduced-use cue, blocked transfer, or incomplete rewrite.
9. **Use the subject pattern.** Do not let the repair become the subject Solution unless the pattern is itself about state-family precision restoration.

#### A.19.SPR:4.2 - Subject pattern assignments

| Recovered state-like claim | First subject pattern or locus |
| --- | --- |
| position in a declared `CharacteristicSpace` | `A.19`, with `A.17`, `A.18`, `C.16`, and `C.16.P` when construction is hidden |
| reusable transition law, trajectory, or dynamics model | `A.3.3` |
| system-role-assignment-state assertion, system-role assignment, or work-admitting state | `A.2.5` for `SystemRoleAssignmentStateRelation` and `A.15` or the direct Work pattern when Work is claimed |
| language-state position for episteme or publication wording | `C.2.2a` and `A.16.*` after `C.2.P` when source-publication recovery is needed |
| source use, source currentness, source publication, or source-use disposition | `C.2.P`, `E.17`, `E.9.DA`, or source-use field named by value |
| evidence path state, evidence relation, or reliance disposition | `A.10` |
| assurance result, assurance claim, assurance input, or engineering-justification use | `B.3` |
| constraint, local CV, gate, or release readiness | `A.20`, `A.21`, or release or gate pattern governing the claim |
| publication use, publication face, form, or unit value, source-finding use | `E.17`, `E.17.0`, `E.17.AUD`, or publication pattern governing the claim |
| Description episteme admitted for specification use or specification refinement | `A.7`, plus the specification-granting neighbouring pattern named by value: `A.6.2`, `C.2.3`, `A.21`, `C.16`, `E.17`, `E.10`, or another named pattern |
| temporal claim status or temporal-use classification | `C.27`, retaining `dynClaimPosture` only as a declared C.27 field |
| mathematical-lens use admissibility | `C.29`, retaining `LensUseAdmissibilityValue` only as a declared C.29 field |
| `DRR` decision-adequacy result or source-use classification | `E.9.DA` |
| pattern-quality result or pattern-quality review status | `E.21`, with `E.19` only as review or admission profile |
| administrative, review, dispatch, release or admission, or source-control state | the project-side administrative, review, dispatch, release or admission, or source-control record; not pattern prose unless the pattern's own `EntityOfConcern` is that record |

#### A.19.SPR:4.3 - Retained local field rule

A local `...Posture`, `...Status`, `...Readiness`, or `...State` field is admissible only when the text declares:

- field name;
- bearer kind;
- subject pattern;
- value set or declared classification source;
- admissible use;
- non-admissible overread;
- validity window, decay rule, or reopen condition when applicable.

If any of those are missing, either complete them now or rename the field to the phrase or record required by the subject pattern. A narrowing adjective does not count as kind recovery.

