---
chunk_kind: "child"
pattern_id: "E.4.PFR"
pattern_title: "Pattern-Framework Relation and Edition Discipline"
section_id: "E.4.PFR:3"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFR/E.4.PFR__004_solution.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "E.4.PFR — Pattern-Framework Relation and Edition Discipline"
  - "E.4.PFR:3 — Solution"
line_start: 71238
line_end: 71361
dependencies:
  - "A.10"
  - "A.6.0"
  - "A.6.5"
  - "A.6.6"
  - "A.6.P"
  - "A.6.RCD"
  - "B.3"
  - "C.2.1"
  - "C.32.PAD"
  - "C.33"
  - "C.33-C.35"
  - "C.34"
  - "C.35"
  - "E.11"
  - "E.11.PUR"
  - "E.17"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.24.PUB"
  - "E.4"
  - "E.4.DPF.DA"
  - "E.4.FPF"
  - "E.4.PFAD"
  - "E.5.3"
  - "E.9"
  - "F.18"
  - "G.11"
  - "G.2"
  - "G.5"
keywords:
---

### E.4.PFR:3 - Solution

Select the lightest lane that changes the named receiver's next action. A more elaborate representation is not intrinsically better.

#### E.4.PFR:3.1 - Lane 1: ordinary subject assertion

Name the exact subject or claim, exact relation function, exact defining or constraining ClaimGraph, assertion polarity, and current facts or constituting history. A pattern id, heading, field, file, or carrier may locate that ClaimGraph but does not own the subject and creates no governance relation.

If no actual formal-premise use or criterion selection is claimed, stop. Create no PFR row, actual-use predicate assertion, candidate universe, basis analysis, scope/time placeholder, edition pin, witness wrapper, evidence or assurance result, accepted-use record, or relation occurrence merely to make the sentence look complete.

#### E.4.PFR:3.2 - Lane 2: optional relation-specific maintenance row

Open a row only when a named maintainer, edition-impact check, comparison tool, publication/dependency repair, or refresh action consumes stable relation form. The row faithfully represents an already identified assertion.

```text
PatternFrameworkRelationRecord@Context:
  relationId
  sourceRef
  targetRef
  relationFunction
  governedUse
  subjectAssertionRef?
  relationFunctionClaimRef?
  dependencyOrEditionEffect?
  preservationOrAdmissionRef?
  blockedStrongerReading
  sourceReturnCondition?
  refreshOrSupersessionCondition?
```

`relationFunctionClaimRef`, when present, resolves the exact defining or constraining ClaimGraph used by the subject assertion. It is not an owner field, pattern-authority assertion, provenance claim, or actual-use predicate. `subjectAssertionRef` is present only when the receiver needs stable reference to the exact C.2.1 assertion. Source and target remain the exact endpoints for this relation function; row order creates no direction.

Dependency, specialization, publication, source reuse, quality, access, preservation, admission, and refresh retain their existing semantics. A PFR row translates none into derivation, evaluation, evidence, assurance, permission, authority, Work, or relation occurrence.

Use these companion forms only for their named maintenance receivers:

```text
FrameworkEditionDependencyRecord@Context:
  frameworkEditionRef
  dependsOnEditionRefs
  dependencyReason
  compatibilityBoundary
  deprecationOrSupersessionRefs?
  refreshConditionRefs?
  e53ConformanceNote

FrameworkPackageManifest@Context:
  frameworkEditionRef
  selectedPatternSetPublicationRef
  relationRecordRefs
  dependencyAndEditionRecordRefs
  editionStatus
  deprecationOrSupersessionRefs?
  sourcePackRefs
  qualityEvidenceRefs
  refreshPlanOrCurrentnessRefs
  firstEntryCarrierRefs
  blockedRuntimeOrBuildReading
```

The manifest is a package-like index for a domain principle framework or local practice framework when authors actually need one. The form of FPF itself uses E.4.FPF and its `FPFFormMap`. A manifest entry, relation row, identifier, citation, or file path creates neither the referenced object nor any relation.

#### E.4.PFR:3.3 - Relation functions keep their own semantics

| Relation function | Admissible use | Exact defining or constraining locus |
| --- | --- | --- |
| Pattern-use recommendation | Recommends or sequences a candidate pattern use for a concern; actual application remains separate. | `E.11.PUR` |
| Specialization | Narrows parent content through exact inherited content plus child delta and stated use boundary. | parent content and `E.8` |
| Framework-architecture answer: initial pattern-relation choices | Asserts each material relation among selected initial patterns with the predicate that defines it; the one `E.9` answer records which choices were selected and why. Add a PFR row only when a named maintenance use needs a stable representation. | the pattern that defines or constrains each asserted relation; `E.9` for the selected answer; `E.4.PFAD` for its framework-specific profile |
| Publication relation | Makes selected content available through a publication occurrence, form, unit, view, carrier, readme, preface, card, or table of contents. | `E.11`, `E.17`, `E.24.PUB` |
| Access relation | Describes bounded access to selected framework content or guidance through a skill pack, MCP-backed service, retrieval route, or assistant integration. | exact access claim plus `E.11`/`E.17`; `C.35`, `A.15`, `A.10`, `B.3`, `E.9`, or `G.11` only when their distinct output is current |
| Framework edition dependency | States reliance on a more stable framework edition, exact dependent use, compatibility boundary, and refresh condition. | `E.5.3`, `G.11` |
| Preservation relation | States that one carrier, edition, profile, or projection preserves selected structure for a licensed use. | `C.34`, with `C.33` for local carrier loss |
| Produced-carrier admission | Admits generated, searched, mined, or transformed carrier content as input under declared conditions. | `C.35` |
| Quality framing, evaluation, or improvement | Frames a question, evaluates FPF/DPF/pattern adequacy, or records repeated improvement. | `E.22`, `E.2.DA`, `E.4.DPF.DA`, `E.21`, `E.23` as selected by the exact object |
| Selected-set publication | Publishes a selected set with exact scope and selection conditions. | `G.5`, coordinated with `E.17`/`E.24.PUB` |
| Source or decision reuse | Uses an exact source line, SoTA pack, DRR, selected answer, accepted decision, or evidence/source claim by value for a bounded use. | `G.2` for source/SoTA; `E.9` for the DRR and selected answer; the exact separate acceptance decision plus its authority relation or local rule for accepted-decision reuse; `A.10` only for an evidence-use claim |
| Direct subject relation | States one exact relation or classification under its defining predicate and current case facts. | the exact subject pattern and C.2.1 assertion identity |

The direct assertions, not a PFAD or PFR row, state the architecture-bearing relation facts. The `E.9` DRR records their selection and rationale; `E.4.PFAD` adds no relation or second decision result. An optional PFR row may point to an exact assertion for maintenance, but it neither creates that relation nor becomes a condition for accepting the answer.

There is no `Subject-pattern relation`. When earlier prose says that one pattern contains the defining content for or governs a value, claim, boundary, relation, record form, or use, recover the subject assertion and exact relation function. Preserve genuine non-pattern ownership, legal or institutional authority, source attribution, evidence, and other direct relations.

#### E.4.PFR:3.4 - Edition and package discipline

Domain and local frameworks depend toward more stable editions. A local practice framework may depend on a domain principle framework and FPF Core. A domain principle framework may depend on FPF Core. FPF as a First Principles Framework edition is handled through E.4.FPF; Core does not depend on domain or local frameworks except through a deliberate Core amendment.

Compatibility practice is narrow: name the compatibility boundary, exact dependency impact, deprecation, supersession, and refresh conditions. An edition label alone establishes none. Do not import binary compatibility, runtime import, build, module-call, API permission, or performed-work semantics.

A selected pattern-set publication, access carrier, relation row, dependency pin, edition status, source-pack pin, quality result, refresh plan, and first-entry carrier remain different objects. Listing a skill package, MCP endpoint, API route, or assistant integration records only the exact access claim that obtains; it creates no framework dependency, method order, tool permission, or authority. Use G.5 for selected-set publication, G.11 for currentness, and C.33/C.34 when a carrier is used as architecture or preservation evidence.

#### E.4.PFR:3.5 - Lane 3: exact actual rule-content use

Use `derivedUsingRuleContent(dependentContent, baseContent)` only when one identified derivation claim used the exact nonempty base subgraph as a formal premise under a declared inference rule or application to produce the exact dependent ClaimGraph. Use `evaluatedAgainstRuleContent(dependentContent, baseContent)` only when one identified criterion-selection claim selected the exact base for one bounded evaluation claim concerning that dependent ClaimGraph. These predicates are declared by `RuleContentBasisFindingDefinition@R7`; definition, constraint, applicability, consultation, influence, source use, evidence, evaluation Work, result, sufficiency, assurance, reliance, permission, and publication are independent.

Each positive or negative actual-use assertion is an ordinary C.2.1 episteme. It names exact subject `S`, dependent graph `U`, base subgraph `B`, mode, exact derivation or evaluation-and-selection claim identity, bounded receiving use, effective scheme, and only independently current scope, time, interpretation, source, or witness qualifications. A same-scheme use invents no Bridge. The serialized form is a representation, not a relation occurrence or new kind.

#### E.4.PFR:3.6 - Optional high-cost basis analysis

Open a basis analysis only for a named automated candidate comparison, reproducible cross-edition replay, material same-subject conflict, or bounded reliance/assurance receiver. One analysis is one C.2.1 episteme identified by `<AnalysisClaimGraph, BasisAnalysisQuestion@QGroup, effective ReferenceScheme>`. The question includes every independently current discriminator: `S`, `U`, derive/evaluate mode, bounded receiving use, exact actual-use claim identities, receiving edition when material, effective scheme, optional exact ClaimScope, and exact temporal-policy branch.

The analysis ClaimGraph carries a finite material candidate universe and a closure claim only when the enumeration rule, source boundary, completeness evidence, qualification window, and exclusion argument are exact. Each candidate is a finite nonempty set of semantic-base subgraphs used conjunctively. Each `CandidateEvaluation` keeps exactness, applicability, acceptance, witness, sufficiency, and minimality independent, with supporting claim refs and a reconsideration condition for every unresolved or negative axis. Duplicate graphs under one scheme collapse to one semantic atom while retaining source qualifications. Independently sufficient bases remain separate alternatives; jointly necessary bases remain one conjunctive alternative.

Compatibility is pairwise, not a candidate property. Every overlapping established pair receives an exact result naming both alternatives, overlap, supporting claims, and, when conflicting, incompatible consequences plus a bounded E.9 decision. The temporal partition is maximal and non-overlapping under the selected policy and material candidate set. A no-time-dependence policy yields one atemporal cell. Scope, temporal policy, material candidates, and applicability changes reopen only affected assertions and analysis cells.

Exactly one disposition follows in each cell:

| Disposition | Truth condition |
| --- | --- |
| `established-conflict` | The established family is nonempty and at least one required overlapping pair conflicts. |
| `established-with-open-candidates` | The family is nonempty and has no established conflict, but the universe is open or a material axis or pair remains unresolved. |
| `established-compatible` | The family is nonempty, the universe is closed, all material axes and pairs are resolved, and all required pairs are compatible. |
| `open-no-established` | The family is empty and the universe is open or a required material axis remains unresolved. |
| `closed-insufficient` | The universe is closed and nonempty, all required axes are resolved, and no candidate passes the conjunction. |
| `missing-candidates` | No material candidate exists and an exact absent-need claim states the needed content, subject/use, search boundary, and reconsideration condition. |

The basis answer is non-permissive. A downstream A.10 bounded-reliance claim or B.3 assurance result cites the exact analysis edition or cell-answer subgraph and supplies its own evidence, freshness, rival explanation, attempted use, and disposition. Neither grants permission, gate passage, decision, Work, actual use, publication, or authority. A reverse consumer lookup is derived rather than inserted into the upstream ClaimGraph.

#### E.4.PFR:3.7 - Bootstrap and stopping rule

A direct C.2.1 assertion always precedes optional PFR representation. The PFR row may cite the assertion and exact relation-function ClaimGraph only when its named maintenance receiver needs it. It cannot provide circular evidence for its own semantics.

After each assertion, ask: what named next action consumes more structure? If none, stop. A true stop has no pattern for the next question. When reconsideration is needed, state the condition or question and name a candidate pattern whose entry accepts it; do not model the pattern as receiver or destination.

