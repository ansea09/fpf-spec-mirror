---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "RoleStateRelation - Windowed Role-State Recognition and Work Admission"
section_id: "A.2.5:0.1"
section_title: "Kind Settlement"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__003_kind-settlement.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "A.2.5 — RoleStateRelation - Windowed Role-State Recognition and Work Admission"
  - "A.2.5:0.1 — Kind Settlement"
line_start: 4441
line_end: 4450
dependencies:
  - "A.15"
  - "A.2.1"
keywords:
  - "RSG"
  - "enactability"
  - "role state"
  - "role-state evolution"
  - "state machine"
---

### A.2.5:0.1 - Kind Settlement

`RoleStateRelation` is admitted as a direct relation kind under `U.Relation`. It is not a new root kind, a role value, or a state graph.

`RoleStatePredicate` is a local ValueKind declared by this pattern, not another root U-kind. One value specifies a truth condition and temporal reading interpreted through the role assignment's `RoleTaxonomyEpistemeSlot` and `EffectiveReferenceSchemeSlot`. A state name such as `InspectionReady` can designate that predicate under the effective scheme; the name alone does not supply predicate identity.

A `RoleStateAssertion` is a `U.Episteme` whose EntityOfConcern is the exact `U.RoleAssignment` or an explicitly individuated `RoleStateRelation` occurrence, according to the claim. Its ClaimGraph names the `RoleStatePredicate`, the exact direct role-state claim family, and `assertionPolarity: affirmative | negative` for the direct obtaining predicate. An affirmative claim may state the known actual role-state extent only when A.2.5 independently establishes obtaining; a receiving evaluation may separately state its target window. `A.2.4` governs only the compact first evidence-use or status-use classification, while fuller evidence-provenance remains under `A.10`. `A.10` or the separately constituted receiving-evaluation result or reliance assertion owns supported, refuted, or unresolved reliance for the declared use. Neither negative polarity nor unresolved reliance fabricates a world-side occurrence; assertion, reliance posture, evidence episteme, evidence-use relation, and world-side role-state occurrence remain different objects.

A representation episteme may describe predicates, possible configurations, and possible changes. A statechart or state-machine display uses a mathematical or representational lens for that purpose; neither the episteme nor its graph becomes a role-state relation occurrence by displaying one.

