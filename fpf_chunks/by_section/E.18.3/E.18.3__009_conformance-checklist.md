---
chunk_kind: "child"
pattern_id: "E.18.3"
pattern_title: "Constraint-Governed Transformation-Flow Unfolding Structure"
section_id: "E.18.3:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.3/E.18.3__009_conformance-checklist.md"
commit_sha: "308edacfa2bdb2c60d07e4e10c0deb1f260a6a31"
heading_path:
  - "E.18.3 — Constraint-Governed Transformation-Flow Unfolding Structure"
  - "E.18.3:7 — Conformance Checklist"
line_start: 83725
line_end: 83737
dependencies:
  - "A.10"
  - "A.15"
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
| **CC-E18.3-1 Transformation substrate.** | Bounded transformations, transformed entity and kind, and typed transformation positions are named. | Use `A.22.CGUS` or another direct pattern instead of E.18.3. |
| **CC-E18.3-2 Flow structure.** | Exact transfer, dependency, crossing, and guard relation refs; one-TFS path and path-slice refs; demonstrations; and optional one-TFS valuation are recoverable without union fields. | Lower to a route card, graph description, or ordinary explanation. |
| **CC-E18.3-2a Network position admission.** | Every position ref agrees with the selected network, complete member path, and leaf TFS position and maps to the same exact position already present in both `transformationPositionRefs[]` and the demonstrative slice's `includedStructurePositionRefs[]`; no parallel raw-position list is created. | Return the mismatched network, path, or leaf; admit the missing typed position or remove the network mapping and keep the graph provisional. |
| **CC-E18.3-2b Network relation and local-state admission.** | Every selected network relation row comes from a current record of that same network and is paired with a relation-reference episteme already present in an applicable E.18.3 reference field, with occurrence, kind, governor, signature, participant order, endpoints, and bindings equal. Valuations, path slices, and tags remain leaf-local and are absent as network-global fields. | Return the exact network, record, relation, endpoint, binding, or governor blocker; remove global state and consume only admitted refs in the post-admission slice. |
| **CC-E18.3-3 Governing-position connections.** | Every neighboring position has exact kind, ref, governing pattern, connection kind, and rationale. Every connection except `comparisonPeer` has an exact supporting relation; for `comparisonPeer`, this connection relation itself states the exact pair and rationale. | Add the typed connection or remove the neighboring-position claim. |
| **CC-E18.3-4 Preserved and omitted structure.** | Preserved transformation structures are exact refs; relevant loss and hiddenness are C.33 adequacy notes for the declared use. | Add the exact structures and C.33 notes before relying on the slice. |
| **CC-E18.3-5 Stop and return.** | Stop boundary and returns to exact governing patterns are separate; E.18 slice-local refresh and G.11 currentness remain distinct. | Add exact boundaries or keep the slice as a one-use example. |
| **CC-E18.3-6 Non-chain topology.** | Branches, joins, cycles, partial orders, and guarded alternatives are preserved or explicitly lost when the flow is graph-shaped. | Keep a linear path provisional before admission; after admission, a separate demonstrative slice may present it but never replaces the whole flow structure. |

