---
chunk_kind: "child"
pattern_id: "A.19.SPR"
pattern_title: "State-Family Precision Restoration"
section_id: "A.19.SPR:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SPR/A.19.SPR__006_solution.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "A.19.SPR — State-Family Precision Restoration"
  - "A.19.SPR:4 — Solution"
line_start: 30451
line_end: 30557
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

Start with the direct sentence:

1. name the exact item;
2. say what value, relation, result, or claim is current; and
3. name the rule or criterion when the sentence is not understandable or usable without it.

Stop there when the intended reader can act safely. Add evidence, time, allowed-use, or blocked-inference detail only when that detail changes the receiving action or prevents a likely harmful conclusion.

Use a `StateFamilyPrecisionRepair` note only when another person or tool must replay the repair, or when the claim has enough consequence that its extra basis must remain inspectable:

```text
StateFamilyPrecisionRepair:
  triggerSpan:
  finalSentence:
  recoveredObjectRef?:
  recoveredClaimValueRelationOrResult?:
  definingOrTestingPatternLocator?:
  predicateRef?:
  criteriaOrEvidenceRef?:
  allowedUse?:
  blockedInference?:
  checkAgainWhen?:
```

The optional fields are triggered separately:

| Add this field | Only when... |
| --- | --- |
| `predicateRef` | the direct pattern defines or needs a reusable predicate. |
| `criteriaOrEvidenceRef` | a receiving decision relies on the criterion or evidence identity. |
| `allowedUse` | the same value could drive materially different actions. |
| `blockedInference` | a likely adjacent inference would be harmful, such as treating readiness as gate passage. |
| `checkAgainWhen` | the value can expire or change during the intended use. |
| exact references and machine fields | automation, audit, comparison, or later replay needs those identities. |

A direct relation, classification, assertion episteme, evaluation result, decision result, or record field keeps its own form. The repair note does not turn it into a new state predicate or result kind.

#### A.19.SPR:4.1 - Direct repair

For ordinary prose, inspect only the current sentence:

1. **Find the item.** For system-role wording, distinguish an exact local system-role kind, an obtaining assignment, its state condition, the world-side assignment-state relation, and an assertion about either. Do not stop at bare `role`.
2. **Write the claim.** Say that the item has a value, that a relation obtains, that an assertion or result says something, or that a project record has a field value.
3. **Use the direct rule.** Cite the applicable pattern when its criterion or distinction matters. If the direct rule already settles the sentence, A.19.SPR has finished its job.

Add a time boundary, evidence basis, allowed use, or blocked inference only under the triggers above. If the item or claim still cannot be recovered, keep the wording as a quotation or navigation cue, narrow its use, or state the exact blocker.

##### A.19.SPR:4.1.1 - Assignment-state exits

| Recovered claim | Direct exit |
| --- | --- |
| One exact system-role assignment or its holder, with no state condition claimed | `A.2.1`; the assignment itself is not readiness. |
| A reusable condition for assignments to one exact local system-role kind | A.2.5 `SystemRoleAssignmentStatePredicate`, by value. |
| One exact assignment satisfies that condition during the relevant interval | The world-side A.2.5 `SystemRoleAssignmentStateRelation` occurrence. |
| An affirmative or negative claim about the assignment or an established relation occurrence | A.2.5 `SystemRoleAssignmentStateAssertion : U.Episteme`; the assertion is not its EntityOfConcern. |
| Evidence, currentness, reliance, or an evaluation concerning that assertion episteme | `A.2.4`, `A.10`, or the direct evaluation pattern. Keep the assertion episteme distinct from the assignment and world-side relation. |
| Whether intended Work may enter now | `A.15.5` or the direct receiving pattern. A.2.5 may supply an assignment-state input; it does not publish the admission result, gate decision, or Work occurrence. |

##### A.19.SPR:4.1.2 - Readiness exits

When `readiness` or `ready` still hides which governed value is meant, use `E.10.MOVE` first. Once the claim is recovered, leave the wording repair through exactly one direct exit:

| Recovered readiness-like claim | Direct exit |
| --- | --- |
| A subject such as a patient or system has a value in a still-hidden state frame | `A.19.SPR`, followed by the subject pattern that defines or tests that value. |
| An assignment satisfies an assignment-state condition | `A.2.5`. |
| One intended performance satisfies a work-entry criterion | `A.15.5` work-entry readiness result. |
| A distinct `OperationalGate(profile)` consumes declared checks and publishes a decision | `A.21`; a ready label alone is not gate passage. |
| A publication use, permission claim, or dated performed Work is meant | `E.17`, the direct permission pattern, or `A.15.1`, respectively. Readiness wording establishes none of them. |

#### A.19.SPR:4.2 - Where the repaired claim belongs

| What the sentence means | Use this pattern or record |
| --- | --- |
| position in a declared `CharacteristicSpace` | `A.19`, with `A.17`, `A.18`, `C.16`, and `C.16.P` when construction is hidden |
| reusable transition law, trajectory, or dynamics model | `A.3.3` |
| exact system-role assignment with no state condition claimed | `A.2.1`; do not treat assignment as readiness |
| by-value assignment-state condition, obtaining assignment-state relation, or assertion episteme about either | `A.2.5`, keeping `SystemRoleAssignmentStatePredicate`, `SystemRoleAssignmentStateRelation`, and `SystemRoleAssignmentStateAssertion` distinct |
| evidence, currentness, reliance, or evaluation concerning an assignment-state assertion | `A.2.4`, `A.10`, or the direct evaluation pattern; the assertion episteme does not become its subject |
| work-entry use of an assignment-state claim | `A.15.5` or the direct receiving pattern; A.2.5 supplies only the exact assignment-state input |
| language-state position for episteme or publication wording | `C.2.2a` and `A.16.*` after `C.2.P` when source-publication recovery is needed |
| source use, source currentness, source publication, or source-use disposition | `C.2.P`, `E.17`, `E.9.DA`, or source-use field named by value |
| evidence path state, evidence relation, or reliance disposition | `A.10` |
| assurance result, assurance claim, assurance input, or engineering-justification use | `B.3` |
| constraint or local CV | `A.20` or the direct constraint pattern |
| ambiguous `readiness` or `ready` wording | `E.10.MOVE` until the governed value is recovered |
| work-entry readiness | `A.15.5` |
| distinct gate decision | `A.21` only when an `OperationalGate(profile)` consumes declared checks and publishes that decision |
| release or permission claim | the direct release or permission pattern; a readiness value establishes neither |
| publication use, publication face, form, or unit value, source-finding use | `E.17`, `E.17.0`, `E.17.AUD`, or publication pattern governing the claim |
| Description episteme admitted for specification use or specification refinement | `A.7`, plus the specification-granting neighbouring pattern named by value: `A.6.2`, `C.2.3`, `A.21`, `C.16`, `E.17`, `E.10`, or another named pattern |
| temporal claim status or temporal-use classification | `C.27`, retaining `dynClaimPosture` only as a declared C.27 field |
| mathematical-lens use admissibility | `C.29`, retaining `LensUseAdmissibilityValue` only as a declared C.29 field |
| `DRR` decision-adequacy result or source-use classification | `E.9.DA` |
| pattern-quality result or pattern-quality review status | `E.21`, with `E.19` only as review or admission profile |
| administrative, review, dispatch, release or admission, or source-control state | the project-side administrative, review, dispatch, release or admission, or source-control record; not pattern prose unless the pattern's own `EntityOfConcern` is that record |

#### A.19.SPR:4.3 - Keeping a technical state field

A technical field such as `...Status`, `...Readiness`, or `...State` may stay when the text makes three things clear: what item the field describes, which values it can take, and which rule or criterion gives those values meaning.

Add an allowed-use boundary only when the field changes a receiving action. Add a blocked inference only when a likely misreading would be harmful. Add a validity window or recheck condition only when the value can change during the intended use. Machine-readable identifiers belong only to automation, audit, comparison, or replay that consumes them.

If the three basic facts are missing, complete them or replace the field with the ordinary sentence the reader actually needs. A narrowing adjective alone does not recover the claim.

