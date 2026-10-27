---
chunk_kind: "child"
pattern_id: "C.2.5"
pattern_title: "U.LanguageStateClosureDegree — How Fixed Is the Current Candidate Space?"
section_id: "C.2.5:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.5/C.2.5__005_solution.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "C.2.5 — U.LanguageStateClosureDegree — How Fixed Is the Current Candidate Space?"
  - "C.2.5:4 — Solution"
line_start: 53032
line_end: 53070
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
`U.LanguageStateClosureDegree` is an ordinal characteristic over how fixed the current candidate set, framing, and admissible next moves are in a published position claim in the declared language-state chart over `U.CharacteristicSpace`.

#### C.2.5:4.0a - Kind and characteristic boundary

`U.LanguageStateClosureDegree` names the Characteristic assessed here. The `CD0`–`CD5` readings belong to its ordinal Scale. A language-state chart binds that Characteristic and Scale in a basis slot under A.19; the Characteristic, a value on its Scale and the chart slot remain distinct. Claims about local route commitments, gates, or authority states remain separate from the closure-degree claim. When one matters to the current use, test it against its applicable rule and current case facts.

#### C.2.5:4.1 - Characteristic specification
- **Kind:** CHR characteristic.
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

