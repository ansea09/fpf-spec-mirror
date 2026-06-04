---
chunk_kind: "child"
pattern_id: "E.21"
pattern_title: "FPF Pattern-Quality Evaluation CharacteristicSpace"
section_id: "E.21:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.21/E.21__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "3d19010169827708d0bca36d0551af8323908640"
heading_path:
  - "E.21 — FPF Pattern-Quality Evaluation CharacteristicSpace"
  - "E.21:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 68418
line_end: 68442
dependencies:
  - "A.17-A.19"
  - "A.19.ECS"
  - "A.6.P"
  - "C.16"
  - "C.2.P"
  - "C.25"
  - "E.10"
  - "E.11"
  - "E.19"
  - "E.2.DA"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9.DA"
  - "F.18"
  - "J.4"
keywords:
  - "and admissibility predicates are not written as duties"
  - "definitions"
  - "invariants"
  - "state agent obligations only"
  - "typing rules"
---

### E.21:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Why it fails | Repair |
|---|---|---|---|
| **Quality score illusion** | `Pattern quality = 87/100`. | Hides ordinal scale differences, hard blockers, and trade-offs. | Publish a `PatternQualityQBundle` with eligibility, coordinates, status, and stop condition. |
| **Administrative proxy quality** | `FormalClaimLegalityAndLensFit = 3 because not yet externally reviewed` or `CaseCountercaseAndTransferCoverage = 4 because already landed`. | Measures process state instead of the pattern property being claimed. | Score the coordinate from the pattern text and content evidence; put review, landing, release, or monolith state in `ClaimScope`, `QualificationWindow`, or the receiving review/release pattern. |
| **Reputation medal quality** | `ActionPathGuidance = 5 because many people use it`, `SoTABindingAndCurrentness = 4 because reviewers liked it`, or `UseAffordabilityAndApparatusProportionality = 3 because nobody has tried it yet`. | Measures social uptake or absence of uptake instead of the pattern property being evaluated. | Convert any observation into exact pattern-content evidence or ignore it for the coordinate value: name the pattern version, reader, use, scope, qualification window, observed property, coordinate affected, and lowering or raising condition. |
| **Template-complete but inert** | All sections exist, but the reader cannot tell what to do first. | E.8 form is being mistaken for action guidance. | Repair `firstMoveRecoverability`, `WorkingSituationAndUseBoundaryRecognizability`, and `ActionPathGuidance`; repair Problem frame and Solution. |
| **Checklist-as-solution** | The conformance checklist carries the main method. | The checklist tests guidance; it does not replace guidance. | Move action guidance into `Solution`; make CC items test it. |
| **Decorative SoTA shelf** | Sources are listed but the pattern would read the same without them. | SoTA has no content-bearing effect. | State adopt/adapt/reject and change a live boundary, example, relation, or checklist. |
| **Lexical polishing without kind recovery** | Terms sound cleaner but kind, relation, or claim-justification basis remains ambiguous. | The repair is lexical, not ontological. | Repair `SemanticKindAndNameRecoverability`; run `F.18 -> A.6.P -> E.10` when durable or cross-pattern names are live. |
| **Apparatus maximalism** | Every draft gets telemetry, archive, review cards, and extra companion files. | Reader and maintainer cost rises without added admissible use. | Use the one-screen card unless consequence or reuse makes heavier evidence or companion apparatus live. |
| **All-high-values Goodharting** | Every visible coordinate is marked `4` or `5`, but the pattern is harder to read, costlier to maintain, or less useful in the declared ordinary case. | The coordinate set became a proxy for value and stopped measuring full pattern-use value. | Activate `UseAffordabilityAndApparatusProportionality`, `RepairLocalityAndChangeImpactPredictability`, and `ProxyForValueSubstitutionResistance`; narrow to high-assurance use if the extra apparatus is only justified there. |
| **Cost-hidden tie-breaker** | Reader, author, maintainer, entry or projection, retrieval, relation, or corpus-ecology cost is treated only as a tie-breaker while it changes admissible use. | A live quality loss is being kept outside the dominance relation. | Promote the cost question into `UseAffordabilityAndApparatusProportionality`, `RepairLocalityAndChangeImpactPredictability`, `ExternalEntryAndProjectionIntegrity`, `PatternLanguageEcologyFit`, `ProxyForValueSubstitutionResistance`, or another active coordinate. |
| **One-domain breadth claim** | The pattern claims transdisciplinary reach with only IT or ML examples. | Example breadth does not justify claim breadth. | Repair `CaseCountercaseAndTransferCoverage` or narrow the claim. |
| **Endless perfection loop** | Authors keep improving because a better wording is always imaginable. | Open-ended evolution lacks a local stop condition. | Stop when eligibility passes, the candidate is non-dominated for scope, floors are met, and remaining issues are bounded non-use or a named receiving pattern; use `EvolutionFrontAndRefreshDiscipline` plus `ClosureAndBoundedNonUseRecoverability` to keep the stop local. |
| **Quality veto theatre** | A reviewer blocks use with phrases such as "not ready", "low quality", "not FPF enough", or "needs more review", but does not name an activated eligibility row, coordinate, content evidence, status payload, and first admissible repair or bounded non-use. | The quality read is being used as authority pressure rather than content guidance. | Rewrite the veto as a pattern-quality finding using `E.21:4.10a`, or remove it from the quality read. |
| **Reviewer preference laundering** | A stylistic, political, role-control, or process preference is encoded as low `ActionPathGuidance`, `SoTABindingAndCurrentness`, `SemanticKindAndNameRecoverability`, or another coordinate without content evidence. | A preference is being laundered into a pattern-quality defect. | Move the preference to the correct neighbouring decision/process locus, or state the actual content defect. |
| **Projection-quality shadow track** | A ToC row, J.4 cue, dashboard tile, status badge, generated summary, or retrieval snippet restates the quality result without scope, status payload, non-use boundary, or source read ref. | A projection is becoming a second semantic track or authority face. | Activate `ExternalEntryAndProjectionIntegrity`; make the projection a thin echo by value and scope, or name the exact publication/projection pattern application. |
| **Corpus-local win, pattern-language loss** | A local pattern edit improves wording or evidence but increases relation fanout, name collision, entry noise, stale echoes, or neighbouring authority confusion. | Local quality improved while FPF corpus ecology degraded. | Activate `PatternLanguageEcologyFit`; narrow the edit, name the exact receiving pattern for the claim, or repair the entry/name/relation locus. |
| **Quality result as project certificate** | A clean pattern-quality read is cited as product safety, compliance, release, or assurance evidence. | Pattern quality is not project-world truth. | Open `A.10`, `B.3`, `A.20`, `A.21`, `A.15`, or another exact receiving pattern for the project-side claim. |
| **Evidence theatre** | The pattern adds evidence refs, review findings, telemetry, or coordinate-evidence cards, but none of them changes a coordinate value, boundary, worked case, or stop condition. | Justification material is being used as authority decoration. | Remove it or state the exact coordinate, status, or stop effect it justifies. |
| **Legacy flattening** | An older pattern that remains useful as source-basis use, historical rationale, or expert-only reference use is forced into ordinary-use repair instead of narrowing its use honestly. | The quality read treats "not ordinary-use admissible" as "worthless". | Use `admissibleWithNarrowerUse`, state the source-basis, reference-only, or historical use, and assign broader use to repair or replacement under the exact receiving pattern. |
| **Narrow-use hiding** | A pattern cannot serve ordinary use, but the quality read still claims broad `admissibleForDeclaredUse`. | A real scope narrowing is hidden to preserve an unwarranted status label. | Change status to `admissibleWithNarrowerUse` and state the narrowed reader, use, or scope. |

