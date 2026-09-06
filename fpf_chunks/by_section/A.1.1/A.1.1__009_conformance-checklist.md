---
chunk_kind: "child"
pattern_id: "A.1.1"
pattern_title: "Bounded Model-Use Structure and DDD Bounded-Context Recovery"
section_id: "A.1.1:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.1/A.1.1__009_conformance-checklist.md"
commit_sha: "43c46859c3926a371fa60cfb1c76aefa19f9eaf9"
heading_path:
  - "A.1.1 — Bounded Model-Use Structure and DDD Bounded-Context Recovery"
  - "A.1.1:7 — Conformance Checklist"
line_start: 2242
line_end: 2255
dependencies:
  - "A.1"
  - "A.14"
  - "A.15.1"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.22"
  - "A.3.1"
  - "A.3.4"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "E.17.0"
  - "E.24.PUB"
  - "F.17"
  - "F.18"
  - "F.9"
keywords:
---

### A.1.1:7 - Conformance Checklist

1. A positive `BoundedModelUseStructure` exposes all four A.22 discriminators: exact constituents, exact selected obtaining applicability/use/coherence occurrences, exact applied constraints, and one named question/action/stop-or-return selection-use frame.
2. The three direct relation declarations satisfy `WF-A1.1-APP`, `WF-A1.1-USE`, and `WF-A1.1-COH`; any imported-sense receiving use additionally satisfies `WF-A1.1-APP-USE` or `WF-A1.1-COH-USE`. Missing conditions return the named stop rather than a positive assertion.
3. Every `ModelExpressionCoherencePredicate` **value** satisfies the local five-part membership and value-identity rule. Every `ModelExpressionCoherenceRelation` **occurrence** is participant-determined by `<model episteme, expression episteme, predicate value, comparison scheme>` and has no interval discriminator.
4. `BoundedModelUseStructure` is governed as `U.Structure`; its identity uses the four A.22 discriminators and their continuity rule.
5. Reidentification compares all four discriminators and then applies A.1.1:4.3. A changed applied constraint or changed question/action/stop-or-return frame reopens identity even when constituents and relation occurrences are unchanged; a changed optional explanatory guard alone reopens the use it protects; if it changes an applied constraint or frame value, compare that discriminator; a changed page, graph, rendering, or publication does not.
6. Semantic locality follows the direct-value triage in A.1.1:4.4. A local rule, inference, unit, evidence use, or status use remains at its exact subject pattern; a broad label or unrepaired generic-context field cannot manufacture the missing participant.
7. A description episteme designates its exact EntityOfConcern under C.2.1. When a description claim needs empirical grounding, recover one exact obtaining `EpistemeEmpiricalGroundingRelation`.
8. DDD Context Mapping is recovered as method, dated Work, claim-bearing product, proposed or obtaining crossing organization, view conformance, representation, and publication under their separate subject patterns. `WF-A1.1-CROSS` blocks a positive cross-structure member while the direct crossing governor or an A.22 discriminator is missing.
9. A code/schema cue is classified from the exact claim as claim-bearing episteme content, repository/file/form/carrier, or deployed system/structure; the cue itself supplies no common kind.
10. Two model uses over one subsystem yield two structures only when each independently supplies all three obtaining relation families, applied constraints, and its exact selection-use frame. Missing coherence or another discriminator leaves that side at its direct relations.
11. Use the structure only when its joint organization changes a receiving decision. The reader can name the admissible action and the stop or return condition; use F.19:4's plausible-reader test for any optional explanatory guard.

