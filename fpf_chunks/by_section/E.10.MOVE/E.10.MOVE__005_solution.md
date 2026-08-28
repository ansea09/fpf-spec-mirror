---
chunk_kind: "child"
pattern_id: "E.10.MOVE"
pattern_title: "Move and Readiness Wording Precision Restoration"
section_id: "E.10.MOVE:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.MOVE/E.10.MOVE__005_solution.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "E.10.MOVE — Move and Readiness Wording Precision Restoration"
  - "E.10.MOVE:4 — Solution"
line_start: 75618
line_end: 75716
dependencies:
  - "A.1.STM"
  - "A.10"
  - "A.15"
  - "A.15.5"
  - "A.21"
  - "A.22.CGUS"
  - "A.3.4.P"
  - "C.24"
  - "C.30"
  - "E.10"
  - "E.10.ARCH"
  - "E.11.PUR"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.23"
  - "E.24"
  - "F.17"
  - "F.18"
  - "G.11"
keywords:
---

### E.10.MOVE:4 - Solution

**Cheap ordinary use.** When the governed value and its direct pattern are already evident, name them, rewrite the phrase without changing the claim, confirm the remaining reader use, and stop. Do not materialize the repair note or traverse the disposition table. Open the fuller procedure only when the wording remains ambiguous, carries several governed values, imports a source term, or must be replayed later.

Restore the governed target before choosing replacement wording:

1. Name the exact `GovernedTextSpan`, the `ClaimBeingMade`, and the `ObjectUnderWordingRepair`.
2. Decide whether the wording is ordinary prose, a quotation, or wording relied on for an FPF-governed claim. Ordinary and quotation uses can close without inventing a technical target.
3. When the phrase is `mantra move`, first ask which use is present. In a post-qualification A.22.CGUS demonstrative slice that shows pattern use, recover the exact E.11.PUA `PatternUsePracticeContinuationDescription@Context`: its proposed use, expected result and kind, PatternID and name, current condition, and continuation disposition. Keep `mantra move` only as bounded Plain wording for that shown continuation. A.22.CGUS supplies the structure and slice boundary; it does not create a universal displayed-row kind. For a Plain local mantra, name the bounded result and restore the move-like wording through that result's exact predicate or constraint. For a Plain long mantra, name the intended final result and the particular map location whose answer or stop is current, then state the exact answer or blocker and use the subject pattern only as a locator. Do not invent a demonstrated row, collapse the long map into one pattern's Solution, or treat any branch as Work order.
4. When `move`, `movement`, `direction`, or similar wording predicts a later evaluation result, recover `ExpectedEvaluationResultChange@Context` under `E.23`. That value is a coordinate-and-scale-qualified prediction episteme, not an operation, transition, movement, work occurrence, or proof of improvement.
5. For every other governed use, name the exact recovered value or relation, its kind, and its subject pattern. For a relation claim, name the admitted direct predicate and actual participants. Add a `RelationSignature` reference only when an admitted reusable typed declaration is current and the receiving use needs that declaration. If the governed value is already clear, use its pattern directly.
6. Split the text when one phrase carries more than one governed value. A recommendation, method, transformation, readiness claim or result, gate decision, publication relation, and performed Work do not become one value because the same word was used for them.
7. Preserve `RemainingReaderUse`: the repair is complete only when a practitioner can still tell what can be inspected, selected, evaluated, planned, performed, or returned to next.

#### E.10.MOVE:4.1 - MoveAndReadinessWordingRepairNote

```text
MoveAndReadinessWordingRepairNote:
  EncounteredWording:
  GovernedTextSpan:
  ClaimBeingMade:
  ObjectUnderWordingRepair:
  WordingUseDispositionValue: boundedDemonstratedContinuation | evaluationResultChangePrediction | directGovernedUse | importedSourceWording | ordinaryProse | quoteOnly
  SubjectPatternLocator?: PatternID, locating the pattern whose content defines, constrains, or tests the recovered value
  RecoveredGovernedValueRef?: U.EntityRef
  RecoveredGovernedValueKindRef?: U.KindRef
  RecoveredRelationSignatureRef?: U.EntityRef, referencing one RelationSignature
  RetainedPlainWording?:
  BlockedOverread:
  SplitDisposition?:
  FinalWordingOrBlocker:
  RemainingReaderUse:
  QualificationWindow:
  CurrentnessBasis:
  ReopenCondition:
```

The governed-value ref and kind ref are both present or both absent. The relation-signature ref is present only when an admitted reusable typed declaration is current and the receiving use needs that declaration. Otherwise a relation claim names the admitted direct predicate and actual participants without a signature ref. A governed use has a non-semantic `SubjectPatternLocator`: an ordinary PatternID that identifies the pattern whose content defines, constrains, or tests the recovered value. The locator creates no `U.Method`, `U.MethodDescription`, or Method-use relation. Ordinary prose and quote-only uses may leave those positions absent and record why no FPF object is being claimed. The `...Ref` fields carry references of the declared RefKinds; they do not carry the referenced values or kinds. A materialized note also states the edition, source, context, or time window in which the repair is relied on, the current pattern or source basis for that interpretation, and the smallest change that reopens it. Use `G.11` only when actual refresh orchestration is current; the note merely records its own currentness boundary. The note is a temporary wording-restoration aid, not a project result, method, plan, gate decision, or work occurrence. Ordinary immediate repair need not materialize the note.

#### E.10.MOVE:4.2 - Trigger groups

Run this restoration when one of these wording groups carries an FPF-governed use:

- `move`, `step`, `action`, `application`, `solution`, and `next action`;
- `readiness`, `ready`, `full kit`, `work entry`, and `launch-ready`;
- `movement`, `direction`, or `shift` used for an expected evaluation-result change;
- `route`, `workflow`, `process`, `path`, `loop`, or `flow` used for a demonstrated continuation, selected structure, transformation, method, work, gate, publication, decision, or currentness claim;
- imported source wording such as TameFlow `MOVE`.

The trigger group only opens the repair. It does not supply a replacement vocabulary or choose the governed-value kind.

##### E.10.MOVE:4.2.1 - Readiness exits

Stay in E.10.MOVE only while `readiness`, `ready`, `full kit`, `work entry`, or a similar cue still hides which governed value is meant. Once that value is recovered, use the direct pattern:

| Recovered claim | Direct pattern |
| --- | --- |
| A patient, system, or other subject has a value in a still-hidden state frame | `A.19.SPR`, then the subject pattern that defines or tests the recovered value. |
| An exact system-role assignment satisfies a by-value assignment-state condition | `A.2.5`; keep its predicate, world-side relation occurrence, and assertion episteme distinct. |
| One intended performance satisfies a work-entry criterion | `A.15.5`; its local readiness result is not a gate decision or performed target Work. |
| A distinct `OperationalGate(profile)` consumes declared checks and publishes a decision | `A.21`; a ready label or readiness result alone is not gate passage. |
| A publication use, permission claim, preparation Work, or target Work is meant | `E.17`, the direct permission pattern, or `A.15.1` as applicable. Keep each claim separate. |

If the direct pattern and value were already clear, bypass this table and use that pattern immediately.

#### E.10.MOVE:4.2a - No synonym closure

Replacing `move` with `step`, `action`, `use`, or `application` does not close the repair. Close only after recovering the governed value and its subject pattern. When responsibility is claimed, name the admitted System, direct domain predicate, actual participants, and applicability, or return the exact A.6.RCD missing governor; an assignment is not a responsibility result. Individuate the responsibility-relation occurrence separately only when a named receiving use needs to distinguish that occurrence. Ordinary-prose or quote-only use closes only when no FPF-governed value is claimed.

#### E.10.MOVE:4.3 - Wording-use dispositions

`WordingUseDispositionValue` is a local finite enumeration for choosing a repair branch. It is not a U-kind, relation kind, state frame, or claim about the project value being repaired.

| `WordingUseDispositionValue` | Selected recovery |
| --- | --- |
| `boundedDemonstratedContinuation` | One E.11.PUA `PatternUsePracticeContinuationDescription@Context` shown inside a post-qualification demonstrative slice. A.22.CGUS supplies the structure and slice boundary, not a wrapper-row kind. Retain the complete bounded use and send stronger claims to their direct patterns. |
| `evaluationResultChangePrediction` | One E.23 `ExpectedEvaluationResultChange@Context` with evaluation pattern, coordinate, scale, current result, one expected value, range, or closed direction, proposal basis, and protected tradeoffs. |
| `directGovernedUse` | The exact governed value or relation, its kind, and its subject pattern. For a relation claim, name the admitted direct predicate and actual participants; include a `RelationSignature` reference only when an admitted reusable typed declaration is current and the receiving use needs it. The wording disposition itself contributes no project ontology. |
| `importedSourceWording` | Preserve the source expression only as source wording; recover every FPF use under its direct pattern. |
| `ordinaryProse` | Keep or lightly rewrite after recording that no FPF-governed value is being asserted. |
| `quoteOnly` | Preserve the quotation and block stronger project use not licensed by the quoted source. |

#### E.10.MOVE:4.4 - Relation to A.3.4.P

Use `A.3.4.P` first when the claim is about a change situation or transformation-flow structure. Use `E.10.MOVE` only for the remaining wording-use question. If the same sentence also recommends a pattern use, claims readiness, or names a demonstrated continuation, split those claims and use its direct pattern for each.

#### E.10.MOVE:4.5 - Durable name repair

A durable name states the recovered subject value or relation; it does not retain an implementation head merely because the fields are typed.

| Misleading durable name | Repair |
| --- | --- |
| `localMoveLocus` | Name the exact local value or relation and its subject pattern. Do not preserve `locus` as a cross-pattern grouping head. |
| `ExpectedEvaluationMovement` | Use `ExpectedEvaluationResultChange@Context` only when the E.23 prediction positions are recoverable. |
| `FirstMoveRecord@Context` | Name the actual first result or relation governed by the direct pattern. |
| `Pattern-Use Sequence` | Use `PatternUseCoordination@Context` or `PatternUsePairwiseOrderingRelation@Context` when that exact relation is current. |

These are repair demonstrations, not a global replacement table.

