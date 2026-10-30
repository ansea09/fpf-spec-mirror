---
chunk_kind: "child"
pattern_id: "C.2.LS"
pattern_title: "Language-State Facet Profile: Publish Readings and Use Conditions Together"
section_id: "C.2.LS:13"
section_title: "Worked Examples and Composition Notes"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.LS/C.2.LS__014_worked-examples-and-composition-notes.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "C.2.LS — Language-State Facet Profile: Publish Readings and Use Conditions Together"
  - "C.2.LS:13 — Worked Examples and Composition Notes"
line_start: 53125
line_end: 53177
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.18"
  - "A.19"
  - "B.4.1"
  - "B.5.2.0"
  - "C.2.1"
  - "C.2.2a"
  - "C.2.3"
  - "C.2.4"
  - "C.2.4-C.2.7"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "E.18"
  - "E.24.PUB"
  - "F.9"
  - "F.9.1"
keywords:
  - "articulation"
  - "closure"
  - "facet profile"
  - "local thresholds"
  - "representation factors"
  - "source and use claims"
---

### C.2.LS:13 - Worked Examples and Composition Notes

#### C.2.LS:13.1 - Operator-facing early alert
In this constructed case, the console publishes `Pump-alert-21` for an operator comparing diagnostic alternatives before selecting a check:

> At sample t21, Pump P7 indicates 70 kPa, below its alarm threshold of 90 kPa: `p_indicated(P7,t21) < 90 kPa`. Which of sensor bias, low supply, or an open bypass explains this indication? Keep these three alternatives live until an observation distinguishes them.

For this comparison, the three candidates have these stated implications:

| Candidate | Distinguishing implication in this case |
|---|---|
| Sensor bias | An accepted independent reference gauge would read at least 90 kPa despite the indicated 70 kPa. |
| Low supply | The reference gauge would read below 90 kPa and the upstream pressure below 80 kPa. |
| Open bypass | The reference gauge would read below 90 kPa and the bypass would be open. |

Initially no reference-gauge reading, upstream-pressure reading, or bypass-state observation is available. The alert makes the contrasts explicit without excluding a candidate or selecting a diagnostic route. Its receiving use is comparison within this stated candidate field. The console connects the alert to the operator's acknowledgement and selection of the next diagnostic check.

The alert's code component uses eight indicator units in this order: `NORMAL`, `LOW_PRESSURE`, `HIGH_PRESSURE`, `LOW_FLOW`, `HIGH_TEMPERATURE`, `VIBRATION`, `SENSOR_FAULT`, `LINK_LOSS`. Exactly one unit is active at a time. The fixed decoder assigns the active unit its corresponding report label; `LOW_PRESSURE` denotes the alarm predicate above. Thus `[0,1,0,0,0,0,0,0]` denotes this low-pressure alert. For this code comparison, the local criterion calls an active-unit fraction at most `1/4` sparse and a greater fraction dense.

The profile states:

- its formality assessment covers the displayed alert condition and question: the pressure variables and units are defined, the threshold predicate is explicit, and the question and diagnostic contrasts are expressed in prose;
- `AE = AE4` for the initial diagnostic question, because its subject, indicated condition, alternatives, contrasting implications, and bounded receiving use give a complete branch-appropriate expression (C.2.4:4.2);
- `CD = CD1`, because the contrasts weakly stabilize the stated candidate field while all three alternatives remain live and no route is selected (C.2.5:4.2);
- the C.2.6 account states that the console connects the alert to the operator's acknowledgement and diagnostic-check selection; this action condition is separate from the chart readings;
- `RepresentationFactorBundle = {local, sparse, symbolic}` for the indicator-code component: one unit identifies the report, the active fraction `1/8` satisfies the stated local criterion, and the named units have an explicit decoding rule (C.2.7:4.1). These readings concern the code; assess the surrounding prose separately if its representation factors matter.

**Changed condition.** Suppose an accepted reference-gauge reading for the same sample t21 becomes available: 72 kPa. Under the stated case implications it excludes sensor bias, while low supply and an open bypass remain live. The meaningful reduction from three candidates to two supports `CD2`; it selects neither remaining route. The updated diagnostic question still has its complete expression, and the pressure vocabulary, alarm predicate, indicator code, and operator-loop connection are unchanged. Apply the receiving pattern's own conditions when choosing the next question, check, or endpoint use.

The alert has a complete question and still-open diagnostic alternatives. Its code factors and operator-loop connection answer different questions; no one facet replaces the others.

#### C.2.LS:13.2 - Research cue before lexical repair
An inquiry note reporting a mismatch noticed through bodily observation may state:

- low `AE`,
- very low `CD`,
- the observer, bodily observation and reported mismatch, with a trace reference if an instrumental observation also contributes,
- and representation-wise mixed because the cue is partly verbal, partly kinesthetic, partly exemplar-based.

Use the profile to identify what the next question still needs. `A.16.1` preserves the cue; `A.6.P` can recover an unclear relation, and `B.5.2` starts from an admissible `U.AbductivePrompt`. Apply the receiving pattern's conditions when choosing the move.

#### C.2.LS:13.3 - Architecture-description case
A viewpoint-bound note about the adequacy of an architecture description may state its constraints through explicit typed predicates, be moderately high in `AE`, still mid-level in `CD` and symbolic in its representation-factor bundle. Its C.2.6 account identifies the document edition and assertions used for the adequacy judgement. The profile keeps description-side adequacy distinct from system-side engineering quality.

#### C.2.LS:13.4 - Same `F`, different profile
Two notes may supply the same required expression properties and still differ sharply in articulation, closure, source and use conditions, and representation factors. One may be used in an operator's check procedure with diagnostic alternatives still open; another may assess a document's assertions with comparatively closed alternatives. The profile bundle keeps that difference visible instead of letting `F` behave like a master factor.

#### C.2.LS:13.5 - Reuse the selection while readings or thresholds change

In :13.1, the facet definitions and record form remain available after the reference-gauge reading arrives. The closure assessment changes from `CD1` to `CD2`; retain the assessed alert edition and the new grounds in the updated assessment. This is reuse of the facet selection with changed claim content, not reuse of the earlier closure reading.

Now consider two stipulated receiving rules for that same assessment. A diagnostic-comparison meeting requires an explicit question and contrasting alternatives; it can use the available `AE4` reading. An action-selection rule additionally requires a selected diagnostic route. `CD2` still leaves two alternatives live, so that rule's condition is not met. The same readings support these different conclusions because the receiving conditions differ. If both assessments publish their threshold conditions, their full contents differ; the common readings may be cited once. Neither rule changes what `AE4` or `CD2` means, and each applies only to the stated receiving use.

