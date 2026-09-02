---
chunk_kind: "child"
pattern_id: "E.18.NET"
pattern_title: "Network of Transformation-Flow Structures"
section_id: "E.18.NET:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.NET/E.18.NET__008_conformance-checklist.md"
commit_sha: "421266f0a37ab295b1ffd9e214ace6541e21f5be"
heading_path:
  - "E.18.NET — Network of Transformation-Flow Structures"
  - "E.18.NET:7 — Conformance Checklist"
line_start: 87740
line_end: 87756
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
| **CC-E18-NET-07 Direct relations** | Every selected cross-flow relation has an admitted kind, applicable predicate, exact positive obtaining occurrence, complete participant order, and grounded endpoint bindings. The governing pattern's relation result remains distinct from E.18.NET selection blockers. | Carry that pattern's exact `missing-governor`, `missing-information`, `factually unsupported`, or positive result; carry an inapplicable or negative result only when that pattern defines it and the case basis establishes it. After a positive result, name a missing endpoint binding separately; do not rewrite it as a relation failure. |
| **CC-E18-NET-08 N-ary preservation** | Participant count, order, kinds, positions, and direction match the direct relation. | Restore the direct signature and remove invented binary decompositions. |
| **CC-E18-NET-09 Record and row-locator separation** | Member rows and relation rows describe already identified objects and occurrences; the record does not create them, and every `NetworkCrossFlowRelationRowRef` resolves exactly one nested row by record, occurrence, and ordered endpoint-binding identity. | Separate the C.2.1 episteme from the selected `U.Structure`; repair or remove any locator that resolves zero or several rows. |
| **CC-E18-NET-10 Non-agentivity** | The network, record, graph, pattern, architecture reading, and demonstrative slice do not act, build, select, decide, warrant, or perform Work. Network identity needs no actor or selection-Work claim. | Describe the network through direct members, selected obtaining occurrences, endpoint bindings, applied constraints, and its use frame. If actual selection Work is current, cite every precise performer's A.13 core and the independent A.15.1 Work admission; cite F.6 only when exact assignment-bound attribution is also current. Keep result episteme, choice, decision, and accountability relations separate. |
| **CC-E18-NET-11 Representation boundary** | Mathematical descriptions, graphs, views, publications, and demonstrations are identified separately and state preserved/lost structure when relied on. | Apply E.18.2, C.29, E.17, A.22.CGUS, or E.18.3 as appropriate. |
| **CC-E18-NET-12 Useful result or stop** | The practitioner receives one exact network ref and return condition, or a proposed description with one exact reason selection cannot close: the governing pattern's relation-claim result, or a separate absent member, applied constraint, use frame, endpoint, or position binding. | Restore the exact result or blocker at its own layer; do not end with a local status taxonomy or make a network-selection blocker change the relation result. |

