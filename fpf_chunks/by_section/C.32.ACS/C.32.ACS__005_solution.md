---
chunk_kind: "child"
pattern_id: "C.32.ACS"
pattern_title: "Architecture Characteristic Criteria Set for Improvement Cycles"
section_id: "C.32.ACS:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACS/C.32.ACS__005_solution.md"
commit_sha: "5801dc610c657ac7b1efee349b18e80ce6d7df6f"
heading_path:
  - "C.32.ACS — Architecture Characteristic Criteria Set for Improvement Cycles"
  - "C.32.ACS:4 — Solution"
line_start: 62311
line_end: 62375
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
  - "anti-Goodhart guard"
  - "architecture characteristic criteria set"
  - "criteria row"
  - "improvement cycle"
  - "protected counter-characteristic"
  - "proxy risk"
---

### C.32.ACS:4 - Solution

Build an `ArchitectureCharacteristicCriteriaSet@Project` from starter heads, source catalogues, architecture constraints, and the project improvement question.

#### C.32.ACS:4.1 - Kind settlement

`ArchitectureCharacteristicCriteriaSet@Project` is a C.32.ACS-local project working record: it holds criteria-row references and use classifications for improvement work. Each `draftProjectCriteriaRows` entry is another local record form, not the referenced `U.Characteristic`, Q-Bundle slot, scale, predicate, measurement result, eval program, or eval result. The set and rows create no new `U.*` kind and replace none of those direct objects.

An architecture characteristic is the property or quality-like head under discussion. A C.25 Q-Bundle is the structured form for a composite quality family. A scale row binds one characteristic or Q-Bundle slot to a bearer, scale form, use class, and receiving use. A row whose scale form exposes exception growth, interface variation, or another scale-sensitive characteristic remains a criterion row; a preference between architecture alternatives over a declared scale window is a separate `C.31.ASAP` claim. An architecture-characteristic eval program belongs to `C.32.ACE`; it frames evaluation of one declared row, coupled rows, Q-Bundle slots, or C.32 candidate palettes while each actual typed result remains with its subject pattern.

#### C.32.ACS:4.2 - Criteria-set construction

Work in this order:

1. Name the described holon, architecture use, and improvement cycle or one-pass eval use. For every proposed row, bind the exact claim scope and selected context slices, effective reference scheme and plane, and qualification or evaluation window. Designate a selected A.1.1 `BoundedModelUseStructure` only when it independently changes that row's interpretation.
2. Start from a `C.32.HCS` starter pack when the project has no draft criteria rows yet. Use source catalogues only as input, not as the criteria set.
3. Build draft project criteria rows. There may be dozens of draft rows when broad scanning is needed, but each row must have a possible bearer, use reason, and pattern for the next question.
4. For each source or starter head, decide whether it is one architecture characteristic, one C.25 Q-Bundle, one Q-Bundle slot, or only source vocabulary.
5. Narrow the optimization-indicator core. The ordinary target is three to five rows. More rows require an explicit reason, such as a regulated trade-off study or a multi-team decision use.
6. Classify remaining admitted rows as `monitoredGuardrail` or `contextOnly`. A guardrail protects against a loss caused by optimizing another row; a context-only row helps interpretation but does not drive optimization now.
7. Bind each admitted row to bearer or selected structure, scale form, polarity, current reading or no-reading reason, proxy risk, protected counter-characteristics, receiving use, and source-return condition.
8. Reference `C.32.ACE` only after the row exists and an eval program is needed for current characterization, candidate comparison, monitoring, or preparing inputs for `A.19.SelectorMechanism`.
9. Reopen the criteria set when the holon family changes, a B.2 whole reidentification changes the bearer, a guardrail degrades, an eval program no longer fits its declared parity frame, or the source-currentness relation changes the acceptable trade-off.

#### C.32.ACS:4.3 - Row use classes

Use `optimizationIndicator` only when the row can responsibly guide architecture changes now. A project normally carries only three to five such rows.

Use `monitoredGuardrail` when the row protects against a loss caused by optimizing another row. Guardrails can have readings and eval results, but they do not define the cycle's optimization direction.

Use `contextOnly` when the row helps interpretation but should not drive improvement, comparison, or selection in the current cycle.

**Stop condition.** Stop C.32.ACS when the criteria set names draft rows, use class, bearer or selected structure, scale form, proxy risk, protected counter-characteristics, receiving use, source-return condition, and any C.32.ACE or Q-Bundle reference that the current use actually needs.

**Lowering condition.** Lower an `optimizationIndicator` to `monitoredGuardrail` or `contextOnly` when it no longer guides the next architecture change or its proxy risk is not controlled. Lower a draft row to source vocabulary when bearer, scale form, use reason, receiving use, or protected counter-characteristics are missing. Use `C.32.HCS` when the holon-family starting point is wrong, to `C.25` when the row is really composite, and to the named pattern for the next question when measurement, eval, comparison, publication, local choice, evidence, assurance, or decision work is current.

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

The row prepares improvement work. It does not carry a claim outside its declared scale and use. An eval result is a reading over a declared row; another pattern may use it as source material for an A.10 evidence relation, improvement feedback, comparison input, selection input, or decision input only when that pattern for the next question is named by value. It does not become the characteristic, the declared architecture concern, the architecture choice, or the optimization direction.

