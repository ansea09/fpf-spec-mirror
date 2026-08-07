---
chunk_kind: "child"
pattern_id: "C.30.ASV"
pattern_title: "Architecture Structural View Adequacy (ASV)"
section_id: "C.30.ASV:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.ASV/C.30.ASV__011_rationale.md"
commit_sha: "2729cfe5a3e4a86da8632aabcb859488c06a2d51"
heading_path:
  - "C.30.ASV — Architecture Structural View Adequacy (ASV)"
  - "C.30.ASV:10 — Rationale"
line_start: 62165
line_end: 62172
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.3"
  - "A.6.F"
  - "A.6.M"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.2.1"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.10"
  - "E.10.D2"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "E.24.PUB"
  - "F.18"
  - "G.6"
keywords:
---

### C.30.ASV:10 - Rationale

C.30.ASV exists because architecture descriptions are commonly multi-view, but FPF cannot let "view" absorb every architecture claim. A structure kind and a viewpoint are different. A structure kind says what kind of selected structure is described; a viewpoint is one exact episteme whose fixed rules the candidate description must satisfy. The direct conformance occurrence, not a label or bundle, makes the same episteme a `U.View`.

The pattern keeps first use light by providing `ArchitectureStructureKindTriage@Project`. If triage identifies the structure kind under consideration and the next admissible architecture move, no full view record is needed. The full record is used when exact conformance obtains and a view changes action, correspondence, publication, source return, source or reliance use, or non-view claim kind.

The TEVB decision is conservative. E.17.2 supplies a four-position project-local authoring template, not a current family or importable bundle. Architecture may reuse only exact `U.ViewpointRef` values resolved from a materialized local declaration, with catalogue and member provenance preserved. Architecture-specific structure kinds and candidate-record bindings are defined beside those exact local references rather than mutating their resolved viewpoint epistemes or treating declaration membership as conformance.

