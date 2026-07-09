---
chunk_kind: "child"
pattern_id: "E.24.CD"
pattern_title: "Ontic Candidate Detection"
section_id: "E.24.CD:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.CD/E.24.CD__006_solution.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "E.24.CD — Ontic Candidate Detection"
  - "E.24.CD:4 — Solution"
line_start: 80916
line_end: 81031
dependencies:
  - "A.19"
  - "A.19.ECS"
  - "A.6.5"
  - "C.2.1"
  - "E.10"
  - "E.10.ARCH"
  - "E.2.DA"
  - "E.21"
  - "E.24"
  - "E.24.PUB"
  - "E.24.UK"
  - "E.9.DA"
  - "F.18"
  - "F.19"
  - "U.CharacteristicSpace"
keywords:
---

### E.24.CD:4 - Solution

Use an `OnticCandidateCluster` as a local detection aid. It is not a `U.*` kind, not a permanent registry entry, and not the ontic. It is a compact description of why the author is considering an E.24 decision.

```text
OnticCandidateCluster:
  RecognizableConcern:
  VisibleSourceForms:
  CompressedTypedValues:
  CandidateSemanticArea:
  CandidateOntologicalNeighborhood:
  PossibleSlotRelation:
  ExistingGoverningPatterns:
  HiddenFormClassification:
  UKindPressure:
  FirstUseGain:
  NonUseDisposition:
  NextPattern:
```

Read the rows this way:

- `RecognizableConcern` names what users or authors are trying to think or act with, before choosing a new kind.
- `VisibleSourceForms` names the forms that revealed the concern: cards, records, tables, schemas, diagrams, views, source rows, examples, or project data structures.
- `CompressedTypedValues` lists the separate FPF values being compressed, such as method, method description, mechanism, work plan, work occurrence, evidence, gate, source, publication, characteristic, structure, role assignment, bounded context, or transformation value.
- `CandidateSemanticArea` names the meaning area where the concern is recognizable.
- `CandidateOntologicalNeighborhood` names the current FPF patterns that already govern nearby values.
- `PossibleSlotRelation` sketches the candidate relation only enough to decide whether E.24 should open.
- `ExistingGoverningPatterns` lists direct patterns that may already close the case.
- `HiddenFormClassification` selects one of the dispositions below.
- `UKindPressure` names any `U.*`, type, kind, subkind, title, filename, heading, ToC row, or structural name whose public shape could over-admit durable FPF kindhood.
- `FirstUseGain` says what becomes easier, safer, or more action-facing if the candidate becomes an ontic.
- `NonUseDisposition` blocks the main overread if no durable ontic is selected.
- `NextPattern` names the next governing pattern: usually `E.24`, `E.24.UK`, `E.24.PUB`, `A.19.ECS`, a direct subject pattern, or `E.10.ARCH`.

#### E.24.CD:4.1 - Detection Signals

Open E.24.CD when several signals cohere around one recognizable concern and a possible slot relation that current patterns do not already make easy to use. The judgement is expert sufficiency, not a score gate: a repeated word alone is a wording-use trigger, and a useful form alone is a publication form or local use frame. Two or more signals can serve as a quick suspicion threshold only when they support the same concern, preserve the typed values involved, and make the possible slot relation worth inspecting.

Useful signals include:

1. **Stable concern across forms.** Several source forms point to the same recognizable concern even when the publication form changes.
2. **Typed-value spread.** The concern repeatedly involves several governed values whose relation matters for use.
3. **Copied slot doctrine.** Several patterns repeat the same field list, slot list, boundary warning, or local relation shape.
4. **Claim-impact from relation changes.** Changing one filler changes what can be claimed, compared, relied on, repaired, or stopped.
5. **Weak identity in current text.** The concern is used as if it has identity, but the identity criterion is missing or inconsistent.
6. **Direct-pattern strain.** Existing governing patterns carry the values, but users still need a stable relation among them.
7. **Publication-form temptation.** A card, record, table, schema, diagram, view, source row, or data structure is treated as the object because it is visible.
8. **U-kind pressure.** A `U.*` spelling, earlier type/kind wording, heading, title, filename, or ToC row appears to claim kindhood before the governed object is recovered.
9. **Dependent-pattern burden.** Nearby patterns need a shared settlement and would otherwise copy the same local ontology.

If the signals do not cohere around one concern, do not open E.24.CD only to collect them. Use the direct governing pattern, `E.10.ARCH`, `E.24.PUB`, or a local-use disposition.

#### E.24.CD:4.2 - Hidden Form Classifications

Classify the detected construct before opening E.24:

| Classification | Meaning | Next use |
| --- | --- | --- |
| Durable ontic candidate | The concern appears to need stable identity, a type-level slot relation, semantic area, ontological neighborhood, and dependent-pattern reliance. | Open `E.24`. |
| U-kind admission pressure | The remaining question is whether a visible `U.*` spelling or earlier type/kind wording should survive in a structural location or public name. | Recover the concern and typed values, then use `E.24.UK`; candidate detection does not admit the U-kind. |
| Local use frame | The relation is useful in one bounded use family, but all filled values are already governed elsewhere and no dependent pattern needs a reusable ontic. | Keep local; cite governing patterns for fillers. |
| Direct governing-pattern use | One existing pattern already carries the claim. | Use that pattern directly. |
| Publication-form-only case | The visible object is a card, record, table, schema, diagram, view, packet, or source form that publishes or organizes another EoC. | Use `E.24.PUB` or the relevant publication pattern. |
| Source wording only | The source label compresses several values but should not enter current FPF vocabulary. | Keep quote-only or reduced-use; use `E.10.ARCH` if repair is needed. |
| Evaluation-construction case | The current problem is comparing pattern-set architecture alternatives. | Build the evaluation `CharacteristicSpace` through `A.19.ECS`. |

#### E.24.CD:4.3 - Sufficiency Rationale

If the classification is durable ontic candidate, write a short sufficiency rationale before opening E.24:

```text
OnticCandidateSufficiencyRationale:
  CandidateEoC:
  StableIdentityHint:
  PossibleSlotRelation:
  ExistingValuesPreserved:
  SemanticArea:
  OntologicalNeighborhood:
  DependentPatternNeed:
  DuplicateOntologyRiskIfSkipped:
  FirstUseGain:
  MainNonUseBoundary:
```

The rationale is sufficient only when it shows both gain and restraint. Gain: the candidate would reduce duplicated ontology, make claims easier to inspect, and give dependent patterns a reusable relation. Restraint: existing typed values keep their governing patterns, publication forms stay downstream, and a local frame remains local when no durable ontic is needed.

#### E.24.CD:4.4 - Project Data-Structure Recovery

Project data structures often hide ontic candidates. Treat them as signals, not conclusions.

When a project data structure or publication form has fields such as `status`, `owner`, `type`, `target`, `source`, `evidence`, `decision`, `problem`, `view`, `flow`, `quality`, or `architecture`, do not accept the field heads as ontology. Recover:

1. the project concern that the form is helping the team handle;
2. the FPF typed values that may fill those fields;
3. the relation among those values;
4. the publication or record form that carries the visible form;
5. the governing patterns that already own each value;
6. the one overread blocked by this recovery.

Example: an "ArchitectureDecisionRecord" may carry an architecture move, selected structure, decision, evidence, source freshness, gate condition, responsible role assignment, and publication date. That record is not a root `U.ArchitectureDecisionRecord` ontic by appearance. It may be a publication form over values governed by `C.30`, decision, gate, evidence, source, role-assignment, and `E.24.PUB` patterns. Only if the relation itself needs stable identity and dependent-pattern reliance does E.24 open.

#### E.24.CD:4.5 - Stop Conditions

Stop E.24.CD when one of these dispositions is reached:

- **Open E.24:** durable ontic candidate is selected for a full ontic-introduction decision.
- **Open E.24.UK:** the concern is recovered and the remaining decision is root or dependent U-kind admission, C.3 typed-reasoning governance, non-U disposition, or structural-name repair.
- **Use existing pattern:** a direct governing pattern carries the claim.
- **Keep local:** a bounded local use frame is enough and is explicitly non-`U.*`.
- **Use publication discipline:** the problem is confusion among the ontic, its description, and publication form.
- **Use evaluation construction:** the problem is comparing architecture alternatives.
- **Keep quote-only or reduced-use:** the source wording should not become current FPF vocabulary.

Do not keep E.24.CD open as a standing registry of possibilities. Once the disposition is clear, move to the selected governing pattern.

