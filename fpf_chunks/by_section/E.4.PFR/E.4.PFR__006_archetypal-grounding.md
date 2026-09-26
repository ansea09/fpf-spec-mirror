---
chunk_kind: "child"
pattern_id: "E.4.PFR"
pattern_title: "Pattern-Framework Relation and Edition Discipline"
section_id: "E.4.PFR:4"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFR/E.4.PFR__006_archetypal-grounding.md"
commit_sha: "7bba05916e6e8ad42f868ed3aad0a7644fe0c354"
heading_path:
  - "E.4.PFR — Pattern-Framework Relation and Edition Discipline"
  - "E.4.PFR:4 — Archetypal Grounding"
line_start: 81235
line_end: 81306
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

### E.4.PFR:4 - Archetypal Grounding

#### E.4.PFR:4.1 - Ordinary subject assertion without PFR

In one CGUS position, `selectedConstituentRef` designates `result-42`. The exact C.11 `ChoiceResult` definition classifies that record from its stated disposition, selected option, comparison basis, rule, and stop-probing reason; A.22.CGUS constrains the position locator and selected-constituent reference. That sentence is the first useful output. It adds no owner field, PFR row, actual-use predicate, or basis analysis.

If a later Core relation-function maintenance replay must enumerate every CGUS position whose constituent-kind assertion cites a defining ClaimGraph, add one compact row for this position with the governed use, subject assertion ref, and exact C.11 definition ClaimGraph ref. That named receiver—not the importance of the relation—opens PFR.

#### E.4.PFR:4.2 - Framework edition dependency

Start with the readable dependency assertion:

> `CodexProcessFramework@current` uses the selected `FPFCorePatternSet@current` authoring and quality rules as required constraints on local process authoring. Without those rules, or after a relevant change to them, the affected local guidance cannot remain current without recheck. `CodexProcessFramework@current` therefore depends on that exact Core content for local process authoring.

Choose the representation from the receiver's job. A cross-relation comparison may use one generic PFR row. An edition-impact or refresh receiver may use one dependency-specific record. This receiver needs the relied-on content and refresh fields, so it uses only the dependency record:

```text
FrameworkEditionDependencyRecord@CodexProcessFramework:
  subjectAssertionRef: CodexProcessFramework-CoreDependencyAssertion
  dependencyPredicateClaimRef: E.4.PFR:3.4-framework-edition-dependency-predicate
  directionConstraintClaimRef: E.5.3-local-to-Core-direction-and-Core-acyclicity
  dependentEditionRef: CodexProcessFramework@current
  reliedOnEditionRef: FPFCorePatternSet@current
  reliedOnContentRefs: [selected_Core_authoring_and_quality_rules]
  namedUse: local_process_authoring
  dependencyDirection: local_to_Core
  dependencyReason: the selected Core rules are required constraints on the affected local guidance; removing or relevantly changing them invalidates or reopens that guidance
  refreshConditionRefs: [G.11-Core_pin_or_selected_rule_change]
```

If one named cross-relation receiver also needs the generic view, add one `PatternFrameworkRelationRecord`, give both forms the same `subjectAssertionRef`, and set the dependency record's `genericRelationRecordRef` to that row. In the generic row, `relationFunctionClaimRef` points to the E.4.PFR:3.4 dependency predicate, `dependencyOrEditionEffect` states the E.5.3-constrained direction, and `refreshOrSupersessionCondition` cites the G.11 refresh condition. Derive their shared endpoints, use, direction/effect, and refresh condition from the subject assertion. A change to that assertion refreshes both views together; neither carries an independently maintained copy of the dependency fact.

If this same pair also has a supported compatibility result for an overlapping use, state that C.2.1 assertion separately. Add its ref to `compatibilityClaimRefs` only when the named edition-impact receiver must traverse from this dependency record to that claim. The dependency record proves neither dependency nor compatibility, and E.5.3 does not own either edition.

#### E.4.PFR:4.3 - Source and decision reuse

```text
PatternFrameworkRelationRecord@HydroponicCucumberDomain:
  relationId: PFR-HC-SRC-001
  sourceRef: G2-HC-nutrient-source-pack
  targetRef: HC.NutrientMonitoringPattern@draft
  relationFunction: Source or decision reuse
  governedUse: the solution uses selected source-pack claims by value for nutrient-monitoring guidance
  subjectAssertionRef: HC-NutrientSourceUseAssertion
  relationFunctionClaimRef: exact G.2 bounded source-use ClaimGraph
  preservationOrAdmissionRef: C.33-source-pack-summary-loss-note
  blockedStrongerReading: not framework dependency, specialization, publication, derivation, evidence, or assurance
  sourceReturnCondition: reconsider when including an omitted rival horticulture tradition could change the selected source answer or bounded nutrient-monitoring use
```

A hydroponic framework may separately carry a Core-edition dependency, publication relation to its all-in-one carrier, access relation to a grower-assistant skill pack, specialization relation for a narrowed authoring pattern, and quality relations for evaluated drafts. Each remains a different assertion and optional row.

#### E.4.PFR:4.4 - Genuine overlap conflict

A named automated replay receiver whose contract requires acceptance and witness has two exact, accepted, witnessed, independently sufficient bases for the same subject, use, scope, and time cell, and their consequences conflict. Lane 1 can state the conflict but cannot give that receiver a stable closed family-plus-pairwise result. The basis analysis retains both alternatives, records the exact pairwise conflict, returns `established-conflict`, and leaves unrelated work available. It selects no winner, grants no permission, and changes no actual-use fact.

#### E.4.PFR:4.5 - Establishment, minimality and a total answer

For a receiving derivation of p under ordinary premise introduction, both {p} and {p,q} are sufficient without any undeclared premise. Both can be established when their required axes are true; only {p} is inclusion-minimal among their sub-bases. If the receiver requires a minimal family and that additional search is incomplete, the minimal-family answer stays qualified while establishment of these two bases survives.

| Bounded cell case | Exactly one disposition and retained distinction |
| --- | --- |
| Closed universe {{p},{p,q}}, required axes true, both yield p and their required pair is compatible | `established-compatible`; optional minimality can remain unknown without changing that result. |
| Closed universe with one otherwise sufficient candidate and an unknown witness required by this receiver | `open-no-established`; the missing witness leaves the conjunction unresolved. |
| Closed universe with one candidate whose exactness is false and required witness unknown | `closed-insufficient`; false exactness decisively defeats it. |
| One established candidate in an open universe | `established-with-open-candidates`; retain the candidate while admitting further alternatives may matter. |
| Two independently sufficient, established bases with known incompatible consequences for the same overlapping use | `established-conflict`, even if another candidate is unresolved; neither established basis is deleted. |
| Closed empty universe and an exact supported absent-needed-content claim | `missing-candidates`. |
| Closed empty universe with no supported claim that content is needed | `closed-empty-unresolved-need`. |

In evaluate mode, criterion “value ≥ 80” and an applicable exact value 70 suffice to obtain `fail` under that evaluation rule. With the other required axes true, the candidate is established even though the evaluated object fails. The criterion/value set's sufficiency says nothing about whether a particular evaluation actually selected and used it; Lane 3's actual-use predicates still need their own facts.

