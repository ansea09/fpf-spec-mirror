---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "SystemRoleAssignmentStateRelation - Assignment-State Recognition and Work Admission"
section_id: "A.2.5:0.1"
section_title: "Kind Settlement"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__003_kind-settlement.md"
commit_sha: "421266f0a37ab295b1ffd9e214ace6541e21f5be"
heading_path:
  - "A.2.5 — SystemRoleAssignmentStateRelation - Assignment-State Recognition and Work Admission"
  - "A.2.5:0.1 — Kind Settlement"
line_start: 4922
line_end: 4941
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.7"
  - "A.21"
  - "A.6.5"
  - "A.6.REL"
  - "C.3"
keywords:
  - "Work admission"
  - "assignment-state predicate"
  - "assignment-state relation"
  - "evidence boundary"
  - "state condition"
  - "time window"
---

### A.2.5:0.1 - Kind Settlement

`SystemRoleAssignmentStateRelation` is admitted as a direct relation kind under `U.Relation`. It is not a new root kind, a system-role kind, an assignment, a displayed state value, or a state graph.

`SystemRoleAssignmentStatePredicate` is a local ValueKind declared by this pattern, not another root U-kind. One predicate value is identified by:

1. the exact local system-role kind for whose assignments it is defined;
2. normalized truth-condition ClaimGraph clauses naming the governed qualities or relations tested;
3. its temporal reading;
4. its applicability conditions; and
5. the exact semantic basis whose edition changes meaning, including a `KindSignature`, reference scheme, bridge, or model-use structure only when the clauses depend on it.

A displayed name such as `InspectionReady` can designate the predicate. The name alone does not identify it. `Ready@InspectorSystemRole` and `Ready@ApproverSystemRole` are different predicate values unless one separately declared predicate has one exact common domain and identical clauses, temporal reading, applicability, and semantic basis.

A compatible semantic-basis edition preserves the predicate only through an explicit predicate-continuity decision showing that those identity-bearing facts continue. A changed system-role kind, truth clause, temporal reading, applicability condition, or meaning-bearing semantic basis yields another predicate.

A `SystemRoleAssignmentStateAssertion` is a `U.Episteme` whose EntityOfConcern is the exact assignment or an explicitly individuated state-relation occurrence, according to the claim. Its ClaimGraph names the predicate, direct claim family, and `assertionPolarity: affirmative | negative`. An affirmative claim may state a known actual extent only after A.2.5 independently establishes obtaining. A receiving evaluation may separately state its target window. Supported, refuted, or unresolved reliance belongs to `A.10` or a separately constituted evaluation result or reliance assertion. Assertion, reliance posture, evidence episteme, evidence-use relation, and world-side occurrence remain different objects.

A representation episteme may describe predicates, possible configurations, and possible changes. A statechart or state-machine display is a mathematical or representational lens; neither the episteme nor its graph becomes a `SystemRoleAssignmentStateRelation` occurrence by displaying one.

