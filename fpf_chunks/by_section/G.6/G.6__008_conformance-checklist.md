---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
section_id: "G.6:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__008_conformance-checklist.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "G.6 — Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
  - "G.6:7 — Conformance Checklist"
line_start: 102706
line_end: 102720
dependencies:
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.1"
  - "A.2.4"
  - "A.6.1"
  - "B.1.6"
  - "B.3"
  - "C.16"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.17"
  - "E.18"
  - "E.18.2"
  - "F.10"
  - "F.6"
  - "F.9"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.9"
keywords:
  - "EvidenceGraph"
  - "NotCarried"
  - "PathCitationRecord"
  - "PathId"
  - "PathSliceId"
  - "actual-use relation"
  - "direct governors"
  - "downstream work"
  - "exact direct relations"
  - "exact represented objects"
  - "local refresh"
  - "obtaining claims"
  - "provenance ledger"
  - "representation correspondence"
  - "source/currentness"
  - "unresolved gaps"
---

### G.6:7 - Conformance Checklist

| ID | Check | Repair if missing |
| --- | --- | --- |
| `CC-G6-01` Exact use | Is one relied-on claim or bounded downstream use named? | Name it, or stay in local A.10 source recovery. |
| `CC-G6-02` Object projection | Does every node cite an exact independently governed object, kind, governor, qualification, and representation ref? | Recover the object or record an unresolved gap; do not mint a graph-only world object. |
| `CC-G6-03` Relation prerequisite | Does every asserted edge cite one exact direct relation, its actual participants, governor, obtaining claim, and context? | Establish the direct relation first or remove the edge from the relied-on path. |
| `CC-G6-04` No fallback edge | Are legacy or display labels prevented from acting as universal relations? | Replace each with the exact formal, measurement, work, production, publication, representation, provenance, temporal, status-use, or later-use relation. |
| `CC-G6-05` Work boundary | Does each represented Work cite one independently admitted A.15.1 Work ref and its A.13-qualified actual performer refs? Are assignment occurrence and F.6 refs included only when the path expressly consumes precise assignment-bound attribution, with a missing attribution recorded as a gap rather than loss of the Work node? Are Method, MethodDescription, resources, direct participation, and A.6.1 bindings still separate? | Use A.13 and A.15.1 for the already-established performer and Work. Cite A.2.1/F.6 only for an expressly consumed attribution, A.6.1 for actual operation bindings, and the exact direct relation for every other participant claim. |
| `CC-G6-06` Result boundary | Are produced entity, subject result, result episteme, carrier, outcome, assurance, and later action distinct and independently identified under exact predicates? | Handle each through the exact predicates and assertions located in A.15.PROD, the domain result pattern, C.2.1, E.17/C.29, B.3, or the later-action source. |
| `CC-G6-07` Source and representation | Are source publication, carrier, copy/transform chain, and C.29 correspondence explicit when current? | Recover those relations before treating the graph rendering as source truth. |
| `CC-G6-08` Time and crossing | Are bounded context, plane, window, bridge/loss, edition, policy, source order, and G.11 currentness visible where they limit use? | Add the exact refs or narrow/block the path slice. |
| `CC-G6-09` Provenance and use | Are A.2.4/A.10 evidence/status use, A.10 provenance/reliance, downstream work, and exact use relation separate? | Recover the direct use; path citation or membership is not actual reliance. |
| `CC-G6-10` Ledger boundary | Does the ledger merely index already established objects and relations, with `NotCarried`, gaps, and local reopen triggers? | Remove process status, generic result fields, and fact-creating language. |

