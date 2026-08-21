---
chunk_kind: "child"
pattern_id: "E.18.3"
pattern_title: "Constraint-Governed Transformation-Flow Unfolding Structure"
section_id: "E.18.3:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.3/E.18.3__009_conformance-checklist.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "E.18.3 — Constraint-Governed Transformation-Flow Unfolding Structure"
  - "E.18.3:7 — Conformance Checklist"
line_start: 82799
line_end: 82815
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
keywords:
---

### E.18.3:7 - Conformance Checklist

| ID | Passing condition | Failed-check repair |
| --- | --- | --- |
| **CC-E18.3-1 One selected structure and profile.** | One `U.Structure` has the four A.22 discriminators, its CGUS locus bindings and potential topology satisfy A.22.CGUS, and one E.18 substrate case supplies the mapped flow positions, bindings, and obtaining occurrences. No reciprocal structure or ambient-context identity exists. | Recover the missing A.22, CGUS, or E.18.3 membership value; otherwise keep the artifact as an explanation. |
| **CC-E18.3-2 Flow case and substrate.** | The E.18 substrate is independently identified, current, and distinct from `selectedCGUSRef`; every bounded `U.Transformation` binding used by it was independently grounded under A.3.4; transformation subjects and kinds are exact; and the use is classified as several valuations on one TFS, one internal `SubflowRef`, or one E.18.NET network over independent members and exact crossings. | Recover the missing transformation, binding, or substrate identity; remove valuation-created flows, detail-created members, reciprocal CGUS identity, and giant-flow flattening; return to E.18 or E.18.NET. |
| **CC-E18.3-2a Locus-to-flow mapping.** | Every transformation position maps the same `CGUSLocusBinding` through an E.18 `FlowPositionRef` and current binding; a network position also agrees with its network, member path, and leaf TFS. No raw parallel position list or free-standing SlotSpec exists. | Return the mismatched structure, locus, constituent, TFS, network, path, leaf, or binding; restore the mapping or keep it provisional. |
| **CC-E18.3-2b Relation and local state.** | Every selected internal `U.Transfer`, dependency relation, cross-member relation, or independently defined guard-relation occurrence has an exact predicate-definition source, participant order, applicability conditions, and current facts. A relation-reference episteme has that occurrence as EntityOfConcern and agrees in kind, predicate-definition source, optional signature when replay needs it, participants, current basis, and any network endpoint bindings. An internal transfer is an exact `U.Transfer` inside one TFS; a dependency predicate makes one admitted continuation, state, or value depend on another and preserves direction; a cross-member relation has ordered endpoints bound to admitted positions in different selected E.18.NET members. E.18 `GateCrossing` is outside the relation-reference field, and no summary label substitutes for the exact relation. Valuations, slices, and tags remain TFS- or leaf-local. | Apply the A.6.RCD blocker selection stated in `4.1`; otherwise return the missing predicate definition, facts, occurrence, record, endpoint, or binding and remove global state or ungrounded edges. |
| **CC-E18.3-2c Continuation judgement.** | Every candidate cites its actual basis: an applied claim with test, applicability, inputs, and facts; an E.18 `GuardFail` with assignment facts; or an independently obtaining relation occurrence. Its result records the dependent occurrences, window, and `enabled`, `disabled`, `unknown`, or `error` outcome. The current set may contain zero, one, or several enabled candidates without changing membership. | Restore the missing basis or return the candidate unknown. Do not infer success from currentness, a guard label, or a relation name, and do not revoke the structure because the current set is empty. |
| **CC-E18.3-3 Neighboring values.** | Every `neighboringValueUseRows[]` entry names the exact independently identified neighboring kind and ref, free-text question, rationale, and an already-obtaining supporting relation with its participants, direction, and identity. A stronger neighboring use cites its exact independently governed claim or relation and that item's own kind or predicate; no broad use classifier substitutes for it. The row also states in ordinary language what the neighboring content contributes, while exact content identity and a pattern locator appear only when they matter to the selected use. Stops and reconsideration conditions remain use boundaries unless separately admitted as relations. | Keep the objects separate, record the attempted question, and name the exact missing supporting relation, stronger-use claim or relation, criterion, facts, evidence, or concrete contribution. |
| **CC-E18.3-4 Description adequacy when used.** | A description or slice states preserved and omitted structure for its declared use; an exact C.33 episteme is required only when carrier loss affects that use. | Narrow or repair the description. Missing C.33, publication, or assurance material does not deny an independently established structure. |
| **CC-E18.3-5 Stop, reconsideration and currentness.** | An ordinary stop is separate from reconsideration conditions that name the condition claim, affected structure and next question. E.18 one-TFS refresh, E.18.NET member/network change and the G.11 source-currentness test remain distinct. Neither stop nor reconsideration creates a receiver. | Add the exact boundary or keep a one-use explanation. |
| **CC-E18.3-6 Potential topology and current set.** | Potential branches, joins, cycles, partial orders, and alternatives remain in the structure even when the case- and time-indexed enabled set has zero or one member. A slice states any topology it omits. | Restore the potential topology or narrow the slice; do not use current cardinality as a membership test. |
| **CC-E18.3-7 Explanation and demonstration separation.** | An ordinary provisional explanation may remain ordinary text and separate from the selected structure. Constitute a C.2.1 provisional episteme only when persistence or replay makes its narrower claim current. Whole-structure-description and post-admission demonstrative epistemes remain separate from the selected structure; one-TFS or network locator-family completeness is required only for the corresponding admitted demonstration use, and the selected family is complete and mutually exclusive. | Remove default episteme materialization from ordinary explanation and stop. When persistence, replay, or an admitted demonstration is current, constitute the correct separate episteme and restore only its applicable complete locator family. |
| **CC-E18.3-8 Method and Work threshold.** | Pattern refs, intended realization, recommendations, imperatives, displayed order and table completion admit no MethodDescription, Method, plan, Work or actual Transformation. Apply the A.3.2, A.15.1 and A.3.4 membership or occurrence tests to exact independent objects when those claims are current. | Apply the relevant test or narrow the claim. |
| **CC-E18.3-9 Plain move and ordinary-first branch.** | `move` denotes the exact current pattern-use action or independently identified object. Before optional formal recovery, the ordinary branch names the concrete transformation subject, two recognizable places or states, the proposed connection or guard, the current continuation question, and one useful provisional result or an honest stop naming the missing fact or rule. Exact identity, position mappings, C.2.1 materialization, publication, evidence, or assurance open only for a named stronger use. The seven application steps remain guidance, not a mantra, Method, plan or performed sequence. | Restore the ordinary action, result, and stop before formal recovery; remove default materialization or assurance. Replace any generic move/step reading with the exact object and state a stronger claim's concrete contribution. A Method contribution states its way of doing and applicability or bounds; a truth, result, evidence, or assurance claim cites its separate applicable rule and current basis. |

