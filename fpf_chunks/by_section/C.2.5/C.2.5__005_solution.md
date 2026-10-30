---
chunk_kind: "child"
pattern_id: "C.2.5"
pattern_title: "Language-State Closure Degree — How Fixed Is the Current Candidate Space?"
section_id: "C.2.5:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.5/C.2.5__005_solution.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "C.2.5 — Language-State Closure Degree — How Fixed Is the Current Candidate Space?"
  - "C.2.5:4 — Solution"
line_start: 53527
line_end: 53575
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.18"
  - "B.4.1"
  - "B.5.2.0"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.LS"
keywords:
  - "CD0–CD5"
  - "candidate-space closure"
  - "closure degree"
  - "frame space"
  - "reopen"
  - "route space"
  - "settledness"
---

### C.2.5:4 - Solution
Language-state closure degree (`CD`) characterizes how firmly a specified candidate space is fixed in the position expressed by an episteme for a named use. The candidates may be answers, frames or possible next moves. Identify which choice is being assessed and which alternatives remain live. The ordinal Scale in :4.2 describes the progression from open exploration to stronger fixation.

#### C.2.5:4.0a - Characteristic, reading and assessment

Closure degree is the Characteristic; `CD0`–`CD5` name values on its ordinal Scale. A reading attributes a supported value, or a set of remaining possible values, to an identified episteme edition within a stated assessment scope and receiving use. A language-state chart binds the Characteristic and Scale in a slot under A.19. The Characteristic, its Scale values, a reading and the chart slot remain distinct under A.18/A.19.

A closure assessment states the actual fixity and its grounds. Claims about a binding route commitment, gate or authority relation follow their own rules and case facts. A note or C.2.LS profile can express the closure assessment; its reusable form and the filled assessment remain distinct.

#### C.2.5:4.5 - Recover the choice before assigning a level

Name the question or choice whose candidate space matters. Recover the live alternatives, any selected route or frame, and the reason that limits further choice. State the scope of that fixation and what would justify reopening it. The different sources of narrowing in :16.2 determine what must be reconsidered when conditions change.

Use that ordinary account directly when it supplies the receiving decision's condition. Assign a `CD` reading when the work needs comparison on this Scale, a chart position or a test against a declared threshold. Match the actual narrowing and reopening conditions to :4.2; retain an unresolved reading when the available grounds do not establish them. A level does not replace the surviving alternatives or the reason for their treatment.

The Scale's order describes greater fixity, not a universal improvement. Inquiry may need several alternatives kept live; a particular operational use may need one route fixed under a separately justified rule. C.2.4 assesses how explicit this content is. Writing out the alternatives and the decision rule can improve articulation without changing closure. New evidence or a changed use can instead reopen one choice while other commitments remain fixed. Preserve the supported observations and surviving choices, then revise only the conclusions affected by the change, using A.16.2 when a publication move is needed.

#### C.2.5:4.1 - Characteristic specification
- **Assessed subject:** the identified episteme edition, with the candidate space, assessment scope and receiving use stated.
- **Scale discipline:** ordinal.
- **What rises:** the candidate space or selected route becomes more fixed for the named use. Any binding force comes from its separately established rule.
- **What does not follow automatically:** truth, trust, formality, or quality.

#### C.2.5:4.2 - Starter anchor set
| Anchor | Reading | Typical interpretation for use |
|---|---|---|
| `CD0` | exploratory-open | broad rival space remains live |
| `CD1` | weakly stabilized | some contrasts are present, but rival routes remain normal |
| `CD2` | narrowed candidate space | explicit rivals remain, but the field is meaningfully reduced |
| `CD3` | selected route or framing | one route is chosen, though reopening remains routine |
| `CD4` | publication- or operation-fixed under guard | changes require named justification |
| `CD5` | strongly fixed | relaxation requires an explicit `A.16.2` move and governance note |

#### C.2.5:4.3 - Non-collapse rules
`LanguageStateClosureDegree` is not:

- `F`;
- articulation explicitness;
- gate decision;
- evaluator confidence;
- warrant strength.

A text may be highly explicit but low-closure, or low-explicitness but already high-closure by policy. Those states shall not be collapsed.

#### C.2.5:4.4 - Change discipline
Increasing `CD` requires narrowing candidate space, route space, or frame space explicitly. Lowering `CD` is admissible only through a named move such as `reopen`, `sketchBackoff`, or `respecify`, with a retained-witness and discarded-assumption note.

An ordinary PatternID in `governingPatternRef` locates the FPF rule relevant to the closure claim. Use a separate `relationFunctionClaimRef` for its exact defining or constraining `ClaimGraph` only when admissible interpretation, comparison, migration, publication, or reuse depends on that exact rule identity (`E.10`, `E.4.PFR`). Use `authoritySourceRef` when a non-pattern source carries the relevant authority.

