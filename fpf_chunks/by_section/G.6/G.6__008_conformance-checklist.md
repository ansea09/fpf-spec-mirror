---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
section_id: "G.6:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__008_conformance-checklist.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "G.6 — Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
  - "G.6:7 — Conformance Checklist"
line_start: 101724
line_end: 101738
dependencies:
  - "A.10"
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
| `CC-G6-05` Work boundary | Are reusable Method and MethodDescription, dated Work, each actual performer and its F.6 attribution, any cited assignment identifier, resources, direct participation, and A.6.1 bindings distinct? | Use A.15.1, A.2.1, and F.6 to establish the complete Work account for each performer; a compact path may omit an unused assignment identifier. Use A.6.1 for actual operation bindings and the exact direct relation for every other participant claim. |
| `CC-G6-06` Result boundary | Are produced entity, subject result, result episteme, carrier, outcome, assurance, and later action distinct and independently identified under exact predicates? | Handle each through the exact predicates and assertions located in A.15.PROD, the domain result pattern, C.2.1, E.17/C.29, B.3, or the later-action source. |
| `CC-G6-07` Source and representation | Are source publication, carrier, copy/transform chain, and C.29 correspondence explicit when current? | Recover those relations before treating the graph rendering as source truth. |
| `CC-G6-08` Time and crossing | Are bounded context, plane, window, bridge/loss, edition, policy, source order, and G.11 currentness visible where they limit use? | Add the exact refs or narrow/block the path slice. |
| `CC-G6-09` Provenance and use | Are A.2.4/A.10 evidence/status use, A.10 provenance/reliance, downstream work, and exact use relation separate? | Recover the direct use; path citation or membership is not actual reliance. |
| `CC-G6-10` Ledger boundary | Does the ledger merely index already established objects and relations, with `NotCarried`, gaps, and local reopen triggers? | Remove process status, generic result fields, and fact-creating language. |

