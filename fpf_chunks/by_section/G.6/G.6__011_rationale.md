---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
section_id: "G.6:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__011_rationale.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "G.6 — Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
  - "G.6:10 — Rationale"
line_start: 99110
line_end: 99117
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

### G.6:10 - Rationale

A.10 recovers one relied-on claim, its source/provenance account, and bounded reliance. G.6 adds stable graph-path identity, slicing, shared citation, and path-local refresh when several downstream consumers need the same dependency-closed representation.

That representational gain does not justify a second ontology of evidence edges. Work, participants, products, subject results, result epistemes, outcomes, sources, provenance, currentness, and later uses already have direct governors. G.6 therefore projects their exact refs and direct relations, and C.29 governs the representation correspondence when current. This makes a complex chain readable without allowing graph topology to create facts.

The ledger is likewise an index over established provenance, not a result store or process log. Missing relation evidence remains a visible gap; it is never repaired by drawing a more persuasive path.

