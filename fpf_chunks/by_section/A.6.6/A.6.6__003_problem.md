---
chunk_kind: "child"
pattern_id: "A.6.6"
pattern_title: "U.BaseDeclarationDiscipline - Kind-explicit, scoped, witnessed base declaration discipline (with base-change lexicon)"
section_id: "A.6.6:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.6/A.6.6__003_problem.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "A.6.6 — U.BaseDeclarationDiscipline - Kind-explicit, scoped, witnessed base declaration discipline (with base-change lexicon)"
  - "A.6.6:2 — Problem"
line_start: 15209
line_end: 15245
dependencies:
  - "A.10"
  - "A.14"
  - "A.2.4"
  - "A.2.6"
  - "A.6.0"
  - "A.6.3"
  - "A.6.3-A.6.4"
  - "A.6.4"
  - "A.6.5"
  - "A.6.P"
  - "A.7"
  - "C.2.1"
  - "C.3.3"
  - "E.10"
  - "E.18"
  - "E.8"
  - "F.15"
  - "F.18"
  - "F.9"
  - "U.RelationSlotDiscipline"
keywords:
  - "SWBD"
  - "anchoring"
  - "base declaration"
  - "baseRelation"
  - "basedness"
  - "rebase"
  - "rescope"
  - "retime"
  - "scope"
  - "support-as-basedness"
  - "witnesses"
  - "Γ_time"
---

### A.6.6:2 - Problem

Typical failure modes this pattern is designed to eliminate:

1. **Relation-kind elision.**
   One verb phrase is used to cover: ID-to-registry reference, claim-to-evidence admissibility, calibration-to-standard, property-to-object attribution, policy gating, etc. Rules and invariants cannot be stated because the relation kind is unspecified.

2. **Perspective flip (dependent-view vs base-view).**
   The same situation is described alternately as “X is anchored/grounded” and “Y is an anchor/ground”, with incompatible naming, hidden directionality, and silent re-typing of the ends.

3. **Base–witness confusion.**
   Evidence, pins, certificates, or proofs are treated as “the base”, even when they are only witnesses for a base relation (or conversely: a true base is treated as a mere witness).

4. **Scope/time collapse.**
   Based declarations are treated as timeless truths; time dependence is smuggled in via “current/latest/recently”, violating explicit `Γ_time` discipline.

5. **`Γ_time` used as a proxy for freshness.**
   Authors treat `Γ_time` as “freshness” or “evidence decay”, collapsing TimePolicy with witness-timespan/freshness predicates.

6. **Decision use without witnesses.**
   Declarations that gate work, publication, or assurance are asserted without a witness/pin, breaking auditability and enabling folklore.

7. **Grounding conflation.**
   “Grounding” is used as if it were one relation, while FPF already distinguishes at least:
   * constructive grounding of a model-edge by a trace (`tv:groundedBy`),
   * situational/empirical grounding of an episteme via a grounding holon (C.2.1),
   * semantic meaning assignment (SenseCell/ConceptSet lane; not a base declaration).

8. **Slot/basing conflation.**
   A.6.5 disambiguates positions in n-ary relations (SlotKind) vs fillers (ValueKind) vs stored references (RefKind). Umbrella basing language reintroduces confusion at the next layer: “why this link exists” (BaseRelation) is missing, and slot-edit operations are conflated with base-declaration edits.

9. **Anchor relapse (Context/meaning surrogate).**
   “Anchor/anchoring” is used to mean “the context”, “the meaning”, “the global reference”, or “the thing that makes this true”. This collapses D.CTX + SenseCell/ConceptSet lanes into a metaphor and makes review/tooling impossible.

10. **Support bucket relapse.**
    “Support”, “support basis”, “support relation”, or “support record” is used as a generic container for unlike relations. Some cases are SWBD basedness; others are evidence polarity, assurance input, causal-use support basis, mathematical-lens use, work enablement, source-description, publication companion, or ordinary help. Treating all of them as one undifferentiated support relation recreates the same under-described dependence that A.6.6 exists to repair.

