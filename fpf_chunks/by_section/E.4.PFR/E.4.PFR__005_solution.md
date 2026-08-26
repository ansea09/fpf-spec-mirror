---
chunk_kind: "child"
pattern_id: "E.4.PFR"
pattern_title: "Pattern-Framework Relation and Edition Discipline"
section_id: "E.4.PFR:3"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFR/E.4.PFR__005_solution.md"
commit_sha: "c7ac61bbaa8d3c10165b1a5a4a350956c87d77c9"
heading_path:
  - "E.4.PFR — Pattern-Framework Relation and Edition Discipline"
  - "E.4.PFR:3 — Solution"
line_start: 69660
line_end: 69805
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

Choose the smallest stable form the named receiver consumes. Use `PatternFrameworkRelationRecord` when a cross-relation comparison or maintenance index needs common endpoint, relation-function, use, and blocked-reading fields. Use `FrameworkEditionDependencyRecord` when an edition-impact or refresh receiver needs the relied-on content, dependency reason, direction, and refresh fields. Choose one by default; either form faithfully represents an already identified assertion and creates no relation.

If one named receiver genuinely needs both views, both cite the same `subjectAssertionRef`, the dependency record cites the generic row through `genericRelationRecordRef`, and every overlapping value is derived from that assertion. Rebuild both views when the assertion changes; never maintain duplicate facts independently.

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
  subjectAssertionRef
  dependencyPredicateClaimRef
  directionConstraintClaimRef
  genericRelationRecordRef?
  dependentEditionRef
  reliedOnEditionRef
  reliedOnContentRefs
  namedUse
  dependencyDirection
  dependencyReason
  refreshConditionRefs
  compatibilityClaimRefs?

FrameworkPackageManifest@Context:
  frameworkEditionRef
  selectedPatternSetResultRef
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

The dependency record mirrors exactly one already stated direct dependency and cites that assertion through `subjectAssertionRef`. It names one dependent edition, one relied-on edition, the exact content from that relied-on edition, the named use, direction, reason, and refresh conditions as one unit. If one edition has several direct dependencies, write one record per relied-on edition or use a keyed collection of those records; never pair parallel edition and content lists or read them as a cross-product. A useful aggregate is only a projection over those direct records, not a second maintained truth. The record contains no compatibility boundary. `compatibilityClaimRefs`, when present, points only to a separately stated pairwise compatibility claim because a named maintenance receiver needs that connection. The reference does not create or complete the compatibility claim. `genericRelationRecordRef` is present only when the same receiver also consumes the generic row; both views derive overlapping values from `subjectAssertionRef` and refresh together. Deprecation and supersession likewise remain separate assertions; a package manifest may index them when its named maintenance use needs those refs.

The manifest is a package-like index for a domain principle framework or local practice framework when authors actually need one. It indexes whichever generic relation rows or dependency-specific records its named operation consumes; either list may be empty, and one indexed form never requires its duplicate. When the operation genuinely needs both linked views, the manifest may index both without making either a second semantic source. The form of FPF itself uses E.4.FPF and its `FPFEditionRebuildabilityRecord`. A manifest entry, relation row, identifier, citation, or file path creates neither the referenced object nor any relation.

#### E.4.PFR:3.3 - Relation functions keep their own semantics

| Relation function | Admissible use | Exact defining or constraining locus |
| --- | --- | --- |
| Pattern-use recommendation | Recommends or sequences a candidate pattern use for a concern; actual application remains separate. | `E.11.PUR` |
| Specialization | Narrows parent content through exact inherited content plus child delta and stated use boundary. | parent content and `E.8` |
| Framework-architecture answer: initial pattern-relation choices | Asserts each direct relation among selected initial patterns whose truth changes the selected architecture answer or its stated consequences, using the predicate that defines that relation; the one `E.9` answer records which choices were selected and why. Add a PFR row only when a named maintenance use needs a stable representation. | the pattern that defines or constrains each asserted relation; `E.9` for the selected answer; `E.4.PFAD` for its framework-specific profile |
| Publication relation | Makes selected content available through a publication occurrence, form, unit, view, carrier, readme, preface, card, or table of contents. | `E.11`, `E.17`, `E.24.PUB` |
| Access relation | Describes bounded access to selected framework content or guidance through a skill pack, MCP-backed service, retrieval route, or assistant integration. | exact access claim plus `E.11`/`E.17`; `C.35`, `A.15`, `A.10`, `B.3`, `E.9`, or `G.11` only when their distinct output is current |
| Framework edition dependency | States that one dependent edition's content or result for a named use requires exact content from one relied-on edition: removing that content or changing it in a way relevant to the use would invalidate the dependent content/result or require that use to be reopened. It makes no compatibility claim. | E.4.PFR:3.4 for the defining predicate; `E.5.3` only for allowed direction and Core acyclicity; `G.11` only for currentness and refresh |
| Framework edition compatibility | States whether one exact pair supports a named overlapping use across a stated difference or interface, with its impact and reopen condition. If the basis is insufficient, make no positive compatibility claim. | C.2.1 assertion identity and E.4.PFR:3.4 |
| Preservation relation | States that one carrier, edition, profile, or projection preserves selected structure for a licensed use. | `C.34`, with `C.33` for local carrier loss |
| Produced-carrier admission | Admits generated, searched, mined, or transformed carrier content as input under declared conditions. | `C.35` |
| Quality framing, evaluation, or improvement | Frames a question, evaluates FPF/DPF/pattern adequacy, or records repeated improvement. | `E.22`, `E.2.DA`, `E.4.DPF.DA`, `E.21`, `E.23` as selected by the exact object |
| Selected-set result declaration | States the selector-facing result kind, exact scope, selection or inclusion conditions, members, ordering, named use when required, and basis pins. It establishes no availability occurrence. | Use `G.5` for this declaration. If publication is separately current, use `E.17` for a source-backed face and return to source and `E.24.PUB` for the publication occurrence and audience availability. |
| Source or decision reuse | Uses an exact source line, SoTA pack, DRR, selected answer, accepted decision, or evidence/source claim by value for a bounded use. | `G.2` for source/SoTA; `E.9` for the DRR and selected answer; the exact separate acceptance decision plus its authority relation or local rule for accepted-decision reuse; `A.10` only for an evidence-use claim |
| Direct subject relation | States one exact relation or classification under its defining predicate and current case facts. | the exact subject pattern and C.2.1 assertion identity |

The direct assertions, not a PFAD or PFR row, state the architecture-bearing relation facts. The `E.9` DRR records their selection and rationale; `E.4.PFAD` adds no relation or second decision result. An optional PFR row may point to an exact assertion for maintenance, but it neither creates that relation nor becomes a condition for accepting the answer.

There is no `Subject-pattern relation`. When earlier prose says that one pattern contains the defining content for or governs a value, claim, boundary, relation, record form, or use, recover the subject assertion and exact relation function. Preserve genuine non-pattern ownership, legal or institutional authority, source attribution, evidence, and other direct relations.

#### E.4.PFR:3.4 - Edition and package discipline

Domain and local frameworks depend toward more stable editions. A local practice framework may depend on a domain principle framework and FPF Core. A domain principle framework may depend on FPF Core. FPF as a First Principles Framework edition is handled through E.4.FPF; Core does not depend on domain or local frameworks except through a deliberate Core amendment.

Framework-edition dependency obtains for one dependent edition, one relied-on edition, exact content in the relied-on edition, and one named use only when the dependent edition's current content or result for that use requires the relied-on content: removing it or changing it in a way relevant to the use would invalidate the dependent content/result or require that use to be reopened. State that case fact and why the content is required. Edition labels, joint publication, joint-use membership, and an allowed direction do not establish dependency.

> `Domain@D` uses `Core@C` relation semantics as required constraints on framework review. Without those semantics, or after a relevant change to them, the affected review guidance cannot remain current without recheck. `Domain@D` therefore depends on that exact `Core@C` content for framework review.

E.5.3 constrains the allowed dependency direction and Core acyclicity after the relation has been identified. G.11 governs the edition pin, currentness, and refresh condition. Neither supplies the dependency predicate or makes the case fact obtain.

Compatibility answers whether one exact pair can support an overlapping use despite a stated difference or interface. State it separately and only when current:

> `Domain@D` and `Core@C` are compatible for framework review across relation-semantics interface I. Difference X changes no admitted review operation within boundary B; reopen when I, X, B, or either edition changes.

If that basis is insufficient, state the unresolved pair, overlap, or impact and make no positive compatibility claim. A dependency record may cite the independently stated compatibility claim only when a named maintenance consumer needs the link. Both claims may obtain for the same pair; neither is shorthand for the other. Deprecation and supersession are also separate claims and are indexed only when current.

Do not import binary compatibility, runtime import, build, module-call, API permission, or performed-work semantics. An edition label alone establishes no dependency, compatibility, deprecation, supersession, or refresh result.

These are heterogeneous neighboring objects, not members of one type: a selected pattern-set result; its stable public identity when one is needed; a publication occurrence; an access carrier; a relation row; a dependency pin; an edition status; a source-pack pin; a quality result; a refresh plan; and a first-entry carrier. Listing an access means—for example, a skill package, MCP endpoint, API route, or assistant integration—records only the exact access claim that obtains; it creates no framework dependency, method order, tool permission, or authority. Use G.5 for selector-facing set-result declaration, E.17 for a source-backed publication face and return to source, E.24.PUB for the publication occurrence and audience availability, G.11 for currentness, and C.33 or C.34 when a carrier is used as architecture or preservation evidence.

#### E.4.PFR:3.5 - Lane 3: exact actual rule-content use

Use `derivedUsingRuleContent(dependentContent, baseContent)` only when one identified derivation claim used the exact nonempty base subgraph as a formal premise under a declared inference rule or application to produce the exact dependent ClaimGraph. Use `evaluatedAgainstRuleContent(dependentContent, baseContent)` only when one identified criterion-selection claim selected the exact base for one bounded evaluation claim concerning that dependent ClaimGraph. These predicates are declared by `RuleContentBasisFindingDefinition@R7`; definition, constraint, applicability, consultation, influence, source use, evidence, evaluation Work, result, sufficiency, assurance, reliance, permission, and publication are independent.

Each positive or negative actual-use assertion is an ordinary C.2.1 episteme. It names exact subject `S`, dependent graph `U`, base subgraph `B`, mode, exact derivation or evaluation-and-selection claim identity, bounded receiving use, effective scheme, and only independently current scope, time, interpretation, source, or witness qualifications. A same-scheme use invents no Bridge. The serialized form is a representation, not a relation occurrence or new kind.

#### E.4.PFR:3.6 - Optional high-cost basis analysis

Open a basis analysis only for a named automated candidate comparison, reproducible cross-edition replay, same-subject conflict whose resolution can change the exact cell disposition or named receiver action, or bounded reliance/assurance receiver. One analysis is one C.2.1 episteme identified by `<AnalysisClaimGraph, BasisAnalysisQuestion@QGroup, effective ReferenceScheme>`. The question includes every independently current discriminator: `S`, `U`, derive/evaluate mode, bounded receiving use, exact actual-use claim identities, the receiving edition whenever changing it can change candidate applicability, the exact cell disposition, or the named receiver action, effective scheme, optional exact ClaimScope, and exact temporal-policy branch.

The analysis ClaimGraph carries a finite candidate universe containing only bases whose inclusion or exclusion can change the exact cell disposition or named receiver action. It carries a closure claim only when the enumeration rule, source boundary, completeness evidence, qualification window, and exclusion argument are exact. Each candidate is a finite nonempty set of semantic-base subgraphs used conjunctively. Each `CandidateEvaluation` keeps exactness, applicability, acceptance, witness, sufficiency, and minimality independent, with supporting claim refs and a reconsideration condition for every unresolved or negative axis. Duplicate graphs under one scheme collapse to one semantic atom while retaining source qualifications. Independently sufficient bases remain separate alternatives; jointly necessary bases remain one conjunctive alternative.

Compatibility is pairwise, not a candidate property. Every overlapping established pair whose resolution can change the exact cell disposition or named receiver action receives an exact result naming both alternatives, overlap, supporting claims, and, when conflicting, incompatible consequences plus a bounded E.9 decision. Candidate axes, pairs, conflicts, and receiving-edition distinctions enter the analysis only under that same effect test. The temporal partition is maximal and non-overlapping under the selected policy and this candidate set. A no-time-dependence policy yields one atemporal cell. Changes to scope, temporal policy, candidate inclusion, or applicability reopen only the assertions and cells whose disposition or named receiver action can change.

Exactly one disposition follows in each cell:

| Disposition | Truth condition |
| --- | --- |
| `established-conflict` | The established family is nonempty and at least one required overlapping pair conflicts. |
| `established-with-open-candidates` | The family is nonempty and has no established conflict, but the universe is open or an in-scope axis or required pair remains unresolved. |
| `established-compatible` | The family is nonempty, the universe is closed, all in-scope axes and required pairs are resolved, and all required pairs are compatible. |
| `open-no-established` | The family is empty and the universe is open or an in-scope required axis remains unresolved. |
| `closed-insufficient` | The universe is closed and nonempty, all required axes are resolved, and no candidate passes the conjunction. |
| `missing-candidates` | No candidate meeting the stated subject/use and source-boundary selection rule exists, and an exact absent-need claim states the needed content, subject/use, search boundary, and reconsideration condition. |

The basis answer is non-permissive. A downstream A.10 bounded-reliance claim or B.3 assurance result cites the exact analysis edition or cell-answer subgraph and supplies its own evidence, freshness, rival explanation, attempted use, and disposition. Neither grants permission, gate passage, decision, Work, actual use, publication, or authority. A reverse consumer lookup is derived rather than inserted into the upstream ClaimGraph.

#### E.4.PFR:3.7 - Bootstrap and stopping rule

A direct C.2.1 assertion always precedes optional PFR representation. The selected generic row or dependency-specific record cites the assertion and its exact defining or constraining ClaimGraph only when the named maintenance receiver needs that form. Neither representation can provide circular evidence for its own semantics.

After each assertion, ask: what named next action consumes more structure? If none, stop. A true stop has no pattern for the next question. When reconsideration is needed, state the condition or question and name a candidate pattern whose entry accepts it; do not model the pattern as receiver or destination.

