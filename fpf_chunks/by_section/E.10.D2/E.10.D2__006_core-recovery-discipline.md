---
chunk_kind: "child"
pattern_id: "E.10.D2"
pattern_title: "EntityOfConcern, Description Episteme, and Specification-Use Discipline"
section_id: "E.10.D2:4.1"
section_title: "Core recovery discipline"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D2/E.10.D2__006_core-recovery-discipline.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "E.10.D2 — EntityOfConcern, Description Episteme, and Specification-Use Discipline"
  - "E.10.D2:4.1 — Core recovery discipline"
line_start: 76329
line_end: 76367
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.2.6"
  - "A.3.2"
  - "A.7"
  - "B.3"
  - "C.2.1"
  - "C.2.3"
  - "C.29"
  - "E.10"
  - "E.10.D1"
  - "E.17"
  - "E.17.0"
  - "E.24.PUB"
  - "F.15"
  - "F.4"
  - "F.5"
  - "F.8"
  - "F.9"
  - "G.11"
keywords:
  - "Description episteme"
  - "DescriptionContext"
  - "EntityOfConcern"
  - "specification use"
  - "testable"
  - "verifiable"
---

### E.10.D2:4.1 - Core recovery discipline

#### E.10.D2:4.1.1 - EntityOfConcern

`EntityOfConcern` is the one exact independently identified `U.Entity` about which the selected claim-bearing whole makes its claims. It may be a system, work occurrence, method, episteme, direct relation occurrence, characteristic, structure, pattern, or another admitted entity. It is neither a universal object bucket nor the authoring target merely because the author is editing it.

A ClaimGraph may designate several other entities as participants in relational, comparative, negative, counterfactual, or modal claims. Those designations do not by themselves create a joint EntityOfConcern. Select a relation occurrence, collection, or structured whole only after its direct pattern independently identifies that entity.

#### E.10.D2:4.1.2 - Description episteme

A description episteme is an ordinary `U.Episteme` whose exact `U.ClaimGraph` contains descriptive claims about its exact EntityOfConcern under its effective `U.ReferenceScheme`. Its identity is the C.2.1 constitution triple; E.10.D2 adds no `subjectRef`, description slot, `isDescriptionOf` relation, context constituent, or peer description ontology.

Its ClaimGraph may contain labels, characterizations, criteria, structural or behavioral claims, diagrams interpreted under a scheme, or other claim-bearing content. Those claims and representations do not become parts or properties of the EntityOfConcern unless the corresponding direct subject pattern establishes them.

For one describing use, the E.17.0-owned `DescriptionContext` selects the exact viewpoint from which this episteme is read. That use qualification is not an episteme identity discriminator, does not establish viewpoint conformance or `U.View` membership, and is not locally redefined here.

#### E.10.D2:4.1.3 - Specification-use admission

Use a `...Spec` name only when the receiving use depends on specification force and all applicable conditions are recoverable:

1. the exact description episteme and its C.2.1 constitution;
2. checkable claims, invariants, criteria, or acceptance conditions in its ClaimGraph;
3. a named harness, validation, conformance, measurement, or evaluation relation capable of checking those claims for the stated use;
4. a preserved or explicitly updated E.17.0 `DescriptionContext` for that describing use.

Declared formality, notation discipline, comparators, tolerances, and measurement rules are named when the claims depend on them. They do not substitute for the checkable claims or the harness. If the conditions are absent, call the episteme a description and present proposed criteria as proposals; a `Spec` suffix, schema, signature, approval, or publication does not supply specification force.

Specification use does not create another episteme identity. A revision that changes ClaimGraph, EntityOfConcern, or effective ReferenceScheme identifies another episteme under C.2.1; a changed harness, evaluation result, publication, or relying use changes its own neighboring object or relation.

#### E.10.D2:4.1.4 - Model-use structure

A `BoundedModelUseStructure` is selected only when the receiving assertion, calculation, interpretation, comparison, or other use depends on the organization of admitted model-applicability, model-use, and coherence relations governed by A.1.1. The receiving use designates that exact structure through its direct relation. The structure is never a constituent of description-episteme identity merely because the episteme is used inside it.

If a proposed dependent relation species genuinely requires one exact model-use structure as an identity-bearing participant, its own pattern must declare that participant and its obtaining and identity rules. E.10.D2 supplies no generic context relation as a shortcut.

#### E.10.D2:4.1.5 - Episteme about an episteme

When an episteme is being described, use ordinary recursion: the earlier episteme is the exact EntityOfConcern of the description episteme; the latter has its own ClaimGraph and effective ReferenceScheme. A publication, rendering, or representation of either remains separate. No mandatory context recursion, meta-description kind, or second episteme ontology is needed.

