---
chunk_kind: "child"
pattern_id: "E.18.3"
pattern_title: "Constraint-Governed Transformation-Flow Unfolding Structure"
section_id: "E.18.3:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.3/E.18.3__009_conformance-checklist.md"
commit_sha: "036c056e98c38522172c6b7b3ad08214281cc4e4"
heading_path:
  - "E.18.3 — Constraint-Governed Transformation-Flow Unfolding Structure"
  - "E.18.3:7 — Conformance Checklist"
line_start: 85157
line_end: 85173
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.PROD"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.4"
  - "A.6.3.NAR"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.30.TFS-REL"
  - "C.32.CONWAY"
  - "C.32.P2S"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.18.3"
  - "E.18.NET"
  - "E.23"
  - "G.11"
  - "G.5"
  - "U.Transfer"
keywords:
---

### E.18.3:7 - Conformance Checklist

| ID | Passing condition | Failed-check repair |
| --- | --- | --- |
| **CC-E18.3-1 One selected structure.** | One exact `U.Structure` has the four A.22 identity discriminators and satisfies the E.18.3 transformation-flow condition; no reciprocal generic/narrower structure or ambient-context identity exists. | Recover the A.22 discriminator or keep the artifact provisional. |
| **CC-E18.3-2 Flow case and substrate.** | The E.18 substrate is independently identified, current, and distinct from `selectedCGUSRef`; every bounded `U.Transformation` binding used by it was independently grounded under A.3.4; transformation subjects and kinds are exact; and the use is classified as several valuations on one TFS, one internal `SubflowRef`, or one E.18.NET network over independent members and exact crossings. | Recover the missing transformation, binding, or substrate identity; remove valuation-created flows, detail-created members, reciprocal CGUS identity, and giant-flow flattening; return to E.18 or E.18.NET. |
| **CC-E18.3-2a Position admission.** | Every transformation position maps the same exact admitted `CGUSPositionLocator` through an exact `FlowPositionRef` and binding; a network position additionally agrees with the selected network, complete member path and leaf TFS. No raw parallel position list exists. | Return the mismatched structure, TFS, network, path, leaf, constituent or binding; admit the missing position or keep it provisional. |
| **CC-E18.3-2b Relation and local state.** | Every selected internal `U.Transfer`, dependency relation, cross-member relation, or independently defined guard-relation occurrence has an exact predicate-definition source, participant order, applicability conditions, and current facts. A relation-reference episteme has that occurrence as EntityOfConcern and agrees in kind, predicate-definition source, optional signature when replay needs it, participants, current basis, and any network endpoint bindings. An internal transfer is an exact `U.Transfer` inside one TFS; a dependency predicate makes one admitted continuation, state, or value depend on another and preserves direction; a cross-member relation has ordered endpoints bound to admitted positions in different selected E.18.NET members. E.18 `GateCrossing` is outside the relation-reference field, and no summary label substitutes for the exact relation. Valuations, slices, and tags remain TFS- or leaf-local. | Apply the A.6.RCD blocker selection stated in `4.1`; otherwise return the missing predicate definition, facts, occurrence, record, endpoint, or binding and remove global state or ungrounded edges. |
| **CC-E18.3-2c Continuation-condition branch.** | Every condition is discriminated as an applied constraint or condition claim with its test and current facts, an E.18 `GuardFail` event with its E.18/A.21 gate-assignment facts, or an independently defined exact relation occurrence. No claim or event appears in `relationReferenceEpistemeRefs[]`, and a guard label alone admits none of the three. | Restore the actual claim, event, or relation basis; remove fabricated relation references and do not reject a valid claim or event merely because no guard relation exists. |
| **CC-E18.3-3 Neighboring values.** | Every `neighboringValueUseRows[]` entry names the exact independently identified neighboring kind and ref, free-text question, rationale, and an already-obtaining supporting relation with its participants, direction, and identity. A stronger neighboring claim also states in ordinary content-bearing language what the neighboring content contributes; bare category labels do not pass. A definition, constraint, predicate, test, evidence rule, or assurance rule may supply the applicable criterion and current basis. A Method contribution states its reusable way of doing and applicability or bounds; any truth, result, evidence, assurance, or Work claim about its use has a separate applicable rule and current facts or evidence. Exact content identity is required only when it changes the selected stronger use, and a pattern ref appears only when it locates that content. Stops and reconsideration conditions remain use boundaries unless separately admitted as relations. | Keep the objects separate, record the attempted question, and name the exact missing supporting relation, criterion, facts, evidence, or concrete contribution. |
| **CC-E18.3-4 Preserved and omitted structure.** | Preserved structures are exact refs; captured, expected-but-uncaptured, lost or hidden structure needed by the use is stated in exact C.33 epistemes. | Add the exact structures and C.33 claims or narrow the use. |
| **CC-E18.3-5 Stop, reconsideration and currentness.** | An ordinary stop is separate from reconsideration conditions that name the condition claim, affected structure and next question. E.18 one-TFS refresh, E.18.NET member/network change and the G.11 source-currentness test remain distinct. Neither stop nor reconsideration creates a receiver. | Add the exact boundary or keep a one-use explanation. |
| **CC-E18.3-6 Non-chain topology.** | Branches, joins, cycles, partial orders and guarded alternatives are preserved or explicitly omitted. Membership is acyclic; exact feedback relations may cycle when their predicates and constraints admit them. | Keep a linear path provisional or state its exact loss in the post-admission slice. |
| **CC-E18.3-7 Explanation and demonstration separation.** | An ordinary provisional explanation may remain ordinary text and separate from the selected structure. Constitute a C.2.1 provisional episteme only when persistence or replay makes its narrower claim current. Whole-structure-description and post-admission demonstrative epistemes remain separate from the selected structure; one-TFS or network locator-family completeness is required only for the corresponding admitted demonstration use, and the selected family is complete and mutually exclusive. | Remove default episteme materialization from ordinary explanation and stop. When persistence, replay, or an admitted demonstration is current, constitute the correct separate episteme and restore only its applicable complete locator family. |
| **CC-E18.3-8 Method and Work threshold.** | Pattern refs, intended realization, recommendations, imperatives, displayed order and table completion admit no MethodDescription, Method, plan, Work or actual Transformation. Apply the A.3.2, A.15.1 and A.3.4 membership or occurrence tests to exact independent objects when those claims are current. | Apply the relevant test or narrow the claim. |
| **CC-E18.3-9 Plain move and ordinary-first branch.** | `move` denotes the exact current pattern-use action or independently identified object. Before optional formal recovery, the ordinary branch names the concrete transformation subject, two recognizable places or states, the proposed connection or guard, the current continuation question, and one useful provisional result or an honest stop naming the missing fact or rule. Exact identity, position mappings, C.2.1 materialization, publication, evidence, or assurance open only for a named stronger use. The seven application steps remain guidance, not a mantra, Method, plan or performed sequence. | Restore the ordinary action, result, and stop before formal recovery; remove default materialization or assurance. Replace any generic move/step reading with the exact object and state a stronger claim's concrete contribution. A Method contribution states its way of doing and applicability or bounds; a truth, result, evidence, or assurance claim cites its separate applicable rule and current basis. |

