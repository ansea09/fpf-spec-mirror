---
chunk_kind: "child"
pattern_id: "C.32.ACS"
pattern_title: "Architecture Characteristic Criteria Set"
section_id: "C.32.ACS:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACS/C.32.ACS__005_solution.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "C.32.ACS — Architecture Characteristic Criteria Set"
  - "C.32.ACS:4 — Solution"
line_start: 76596
line_end: 76662
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.CPM"
  - "A.2.6"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.25"
  - "C.30"
  - "C.30.P"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.HCS"
  - "C.32.PAD"
  - "E.13"
  - "E.22"
  - "E.23"
  - "G.5"
keywords:
  - "Q-Bundle"
  - "architecture criteria"
  - "attainable observation"
  - "protected qualities"
  - "proxy risk"
  - "required result"
  - "structural alternatives"
---

### C.32.ACS:4 - Solution

Construct or reuse criteria from the project improvement question, architecture constraints and relevant starter or source contributions. Use the criteria-set record when it helps keep their bindings and use classes recoverable.

#### C.32.ACS:4.1 - Kind settlement

`ArchitectureCharacteristicCriteriaSet@Project` is a C.32.ACS-local project working record: it holds criteria-row references and use classifications for improvement work. Each `draftProjectCriteriaRows` entry is another local record form, not the referenced `U.Characteristic`, Q-Bundle slot, scale, predicate, measurement result, eval program, or eval result. The set and rows create no new `U.*` kind and replace none of those direct objects.

For a particular architecture decision, a characteristic is architecturally relevant when it matters to a required result or constraint and a difference between the considered structures can change its attainable expression under stated conditions. Name the bearer, relevant structural alternatives and reason for that connection. A domain or functional quality can satisfy this condition; the name of an `-ility` alone cannot. Architectural relevance frames a hypothesis or justified dependence, not proof of a causal effect.

A C.25 Q-Bundle is the structured form for a composite quality family. A scale row binds one characteristic or Q-Bundle slot to a bearer, scale form, use class, and receiving use. A row whose scale form exposes exception growth, interface variation, or another scale-sensitive characteristic remains a criterion row; a preference between architecture alternatives over a declared scale window is a separate `C.31.ASAP` claim. An architecture-characteristic eval program belongs to `C.32.ACE`; it frames evaluation of one declared row, coupled rows, Q-Bundle slots, or C.32 candidate palettes while each actual typed result remains under the pattern that defines and tests that result.

#### C.32.ACS:4.2 - Criteria-set construction

Work in this order:

1. Name the described holon, architecture use, and improvement cycle or one-pass eval use. Connect the receiving role and situation to a needed result, the quality that matters, the structural alternatives that could change it, and an attainable observation. Keep a Method, its description, a performed Work occurrence and the performing System distinct when choosing that bearer. For every admitted row, bind the claim scope and relevant context slices, effective reference scheme and applicable plane, and qualification or evaluation window. A proposed row can retain a missing binding as an explicit question until admission. Designate a selected A.1.1 `BoundedModelUseStructure` only when it independently changes that row's interpretation.
2. Use C.32.HCS when a family starting point is needed. Directly recoverable project pressure or adequate existing criteria can supply the starting point. Source catalogues supply possible heads whose project bindings still need examination.
3. Build draft project criteria rows. There may be dozens of draft rows when broad scanning is needed, but each row must have a possible bearer, use reason, and pattern for the next question.
4. For each source or starter head, decide whether it is one architecture characteristic, one C.25 Q-Bundle, one Q-Bundle slot, or only source vocabulary.
5. Narrow the optimization-indicator core. Three to five rows is an attention heuristic. More rows require a use reason, such as a regulated trade-off study or a multi-team decision. Preserve every applicable non-compensable constraint and necessary guardrail; the small core does not limit their number.
6. Classify remaining admitted rows as `monitoredGuardrail` or `contextOnly`. A guardrail protects a binding condition or guards against a loss caused by optimizing another row; a context-only row helps interpretation but does not drive optimization now.
7. Bind each admitted row to its bearer or selected structure, scale form, applicable polarity, current reading or no-reading reason and receiving use. Examine material proxy risk and protect the characteristics or constraints it could compromise. Add a source-return condition when returning to omitted source detail can change that use.
8. Reference `C.32.ACE` only after the row exists and an eval program is needed for current characterization, candidate comparison, monitoring, or preparing inputs for `A.19.SelectorMechanism`.
9. Reopen the criteria set when the holon family changes, a B.2 whole reidentification changes the bearer, a guardrail degrades, an eval program no longer fits its use conditions, including a parity frame when the inference relies on one, or the source-currentness relation changes the acceptable trade-off.

#### C.32.ACS:4.3 - Row use classes

Use `optimizationIndicator` only when the row can responsibly guide architecture changes now. A project normally carries only three to five such rows.

Use `monitoredGuardrail` when the row protects a binding condition or guards against a loss caused by optimizing another row. Guardrails can have readings and eval results, but they do not define the cycle's optimization direction.

Use `contextOnly` when the row helps interpretation but should not drive improvement, comparison, or selection in the current cycle.

**Stop condition.** Stop C.32.ACS when the criteria needed for the receiving question have their use class, bearer or selected structure, scale form, relevant scope and conditions, material proxy risk and protected losses, plus any ACE, Q-Bundle or source-return contribution that the use needs. A precise unresolved draft can finish a question about what remains missing; it cannot stand in for a usable criterion.

**Lowering condition.** Remove optimization use when a row no longer guides the next change or its material proxy risk is uncontrolled. Classify it as a guardrail or context only when it can support that use; otherwise retain the unresolved question and stop reliance on it. A missing scale or other binding can remain in a draft for repair. Keep a term as source vocabulary only when its project concern or use cannot be recovered. Use C.32.HCS for a missing family starting point and C.25 for a composite quality; measurement, evaluation, comparison and decision uses retain their own conditions.

#### C.32.ACS:4.4 - Improvement-cycle use

When a row is used inside an improvement cycle, add:

```text
ArchitectureCharacteristicImprovementRow@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureCriteriaProjectUseRelationRef?: U.RelationRef governed by the exact improvement-row-use or work-use pattern
  criteriaRowRef:
  rowClaimScopeRef: U.EntityRef referencing one U.ClaimScope
  selectedContextSliceRefs:
  modelUseStructureRef?:
  effectiveReferenceScheme:
  referencePlane?:
  qualificationOrEvaluationWindow:
  useClass:
  currentArchitectureReadingRefOrQualitativeState:
  evalResultRefs?:
  intendedArchitectureChangeDirection:
  candidateSelectedStructureChangeRefs?:
  expectedGain:
  protectedLosses:
  observedReadingAfterChange?:
  nextSynthesisTrigger?:
  stopContinueOrSourceReturnCondition:
```

The row prepares improvement work. It does not carry a claim outside its declared scale and use. A reading or other typed eval result over a declared row retains its result kind and conditions; another pattern may use it as source material for bounded claim reliance under A.10, improvement feedback, comparison input, selection input, or decision input only when that pattern for the next question is named by value. It does not become the characteristic, the declared architecture concern, the architecture choice, or the optimization direction.

