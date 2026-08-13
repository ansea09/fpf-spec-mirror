---
chunk_kind: "child"
pattern_id: "E.18.NET"
pattern_title: "Network of Transformation-Flow Structures"
section_id: "E.18.NET:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.NET/E.18.NET__008_conformance-checklist.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "E.18.NET — Network of Transformation-Flow Structures"
  - "E.18.NET:7 — Conformance Checklist"
line_start: 86206
line_end: 86222
dependencies:
  - "A.1.STM"
  - "A.12"
  - "A.15"
  - "A.15.6"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.4"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.6.REL"
  - "C.2.1"
  - "C.29"
  - "C.30.TFS-REL"
  - "C.32.CONWAY"
  - "E.11"
  - "E.11.PUA"
  - "E.17"
  - "E.18"
  - "E.18.2"
  - "E.18.3"
  - "F.18"
  - "U.Transfer"
keywords:
---

### E.18.NET:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-E18-NET-01 Three-way discriminator** | The case is explicitly distinguished from several valuations of one exact TFS and from one E.18 `SubflowRef`. | Return to member identity and relation basis; do not decide from diagram shape, team labels, or stage names. |
| **CC-E18-NET-02 A.22 identity** | Exact direct members, selected obtaining cross-flow occurrences, applied constraints, and one concrete selection-use frame are recoverable. | Recover the missing discriminator or stop at a proposed description. |
| **CC-E18-NET-03 Independent members** | Every member keeps its own TFS or independently identified E.18.NET-conforming network identity, transformations, Work, valuations, boundaries, and local state. | Split any merged object; reidentify each member under E.18 or E.18.NET and restore its own Work, valuation, boundary, and state. |
| **CC-E18-NET-04 Finite acyclic membership** | Every member path is finite and no member path returns to the same network. | Repair the selected member set or return the cyclic-membership blocker; do not add level kinds. |
| **CC-E18-NET-05 Exposed position** | Every `ExposedFlowPositionRef` resolves hop by hop to an exposed leaf TFS position. | Recover the missing member hop or boundary exposure; do not flatten the nested network. |
| **CC-E18-NET-06 Leaf-local state** | Every valuation, path slice, and `DesignRunTag` remains attached to one exact leaf-TFS binding. | Remove the network-global state field and restore the local bindings. |
| **CC-E18-NET-07 Direct relations** | Every cross-flow relation has an admitted kind, applicable predicate, affirmative case facts, exact obtaining occurrence, full signature, grounded endpoint bindings, and a recoverable predicate and occurrence-identity rule. | Use the pattern that defines or tests that relation: return `missing-governor` only for a missing kind or predicate; otherwise name unresolved grounding, false predicate, or missing endpoint binding exactly. |
| **CC-E18-NET-08 N-ary preservation** | Participant count, order, kinds, positions, and direction match the direct relation. | Restore the direct signature and remove invented binary decompositions. |
| **CC-E18-NET-09 Record and row-locator separation** | Member rows and relation rows describe already identified objects and occurrences; the record does not create them, and every `NetworkCrossFlowRelationRowRef` resolves exactly one nested row by record, occurrence, and ordered endpoint-binding identity. | Separate the C.2.1 episteme from the selected `U.Structure`; repair or remove any locator that resolves zero or several rows. |
| **CC-E18-NET-10 Non-agentivity** | The network, record, graph, pattern, architecture reading, and demonstrative slice do not act, build, decide, warrant, or perform Work. | Name only an admitted `U.System` as the actor. For actual Work, apply A.15.1 and F.6; keep any local system-role kind and classification separate. Describe the selected network through `directMemberRefs[]`, selected relation occurrences, applied constraints, and `networkUseFrame`. Keep the result episteme and selection or decision relation separate; any accountability, duty, responsibility, or authority claim needs its own direct predicate and participants. |
| **CC-E18-NET-11 Representation boundary** | Mathematical descriptions, graphs, views, publications, and demonstrations are identified separately and state preserved/lost structure when relied on. | Apply E.18.2, C.29, E.17, A.22.CGUS, or E.18.3 as appropriate. |
| **CC-E18-NET-12 Useful result or stop** | The practitioner receives one exact network ref and return condition, or one exact proposed description with the reason selection cannot close: an absent member, applied constraint, or use frame; a missing relation kind or predicate; unresolved facts; a false predicate; or a missing endpoint binding. | Restore the action and visible result or one of those truthful stops; do not end with only a taxonomy or warning list. |

