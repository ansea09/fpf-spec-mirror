---
chunk_kind: "child"
pattern_id: "C.30.ASV"
pattern_title: "Architecture Structural View Adequacy (ASV)"
section_id: "C.30.ASV:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.ASV/C.30.ASV__011_rationale.md"
commit_sha: "9b6d71cff42a9ac45e46a2be2d9450f766868bc4"
heading_path:
  - "C.30.ASV — Architecture Structural View Adequacy (ASV)"
  - "C.30.ASV:10 — Rationale"
line_start: 56346
line_end: 56353
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
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "E.24.PUB"
  - "F.18"
  - "G.6"
keywords:
  - "ArchitectureStructureKindRef"
  - "VF.ARCH.STRUCTURE"
  - "architecture structural view"
  - "correspondence"
  - "hidden/lost structure"
  - "source return"
  - "structure kind"
  - "viewpoint bundle"
---

### C.30.ASV:10 - Rationale

C.30.ASV exists because architecture descriptions are multi-view by nature, but FPF cannot let "view" absorb every architecture claim. A structure kind and a viewpoint are different. A structure kind says what kind of selected structure is being described; a viewpoint says how an episteme or view is oriented toward a concern. They may be bound, but they are not interchangeable.

The pattern keeps first use light by providing `ArchitectureStructureKindTriage@Project`. If triage identifies the structure kind under consideration and the next admissible architecture move, no full view record is needed. The full record is used when a view changes action, correspondence, publication, source return, source or reliance use, or non-view claim kind.

The TEVB decision is conservative. TEVB remains the small engineering viewpoint bundle over holons. Architecture may import it, but architecture-specific structure kinds and view-record bindings are defined beside TEVB rather than mutating TEVB.

