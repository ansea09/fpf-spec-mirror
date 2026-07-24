---
chunk_kind: "child"
pattern_id: "C.31.RSA"
pattern_title: "Reusable Structure Accounting"
section_id: "C.31.RSA:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31.RSA/C.31.RSA__011_rationale.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "C.31.RSA — Reusable Structure Accounting"
  - "C.31.RSA:10 — Rationale"
line_start: 62743
line_end: 62750
dependencies:
  - "A.10"
  - "A.19"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.31"
  - "C.31.ASAP"
  - "C.32.P2S"
  - "G.5"
  - "G.6"
keywords:
  - "accounting basis"
  - "bespoke residue"
  - "refactoring opportunity"
  - "report-only share"
  - "reusable share"
  - "reusable-structure accounting"
  - "source return"
---

### C.31.RSA:10 - Rationale

C.31.RSA is separate from C.31 because accounting over reusable structure has a different reusable-structure accounting question from choosing modularity characteristics. C.31 asks which characteristic changes action. C.31.RSA asks where reusable structure and bespoke residue are located under a declared accounting basis.

The pattern refuses `StructureAmount` because architecture is selected structure in context, not a substance. A useful accounting description can still report shares, but only under declared structure refs, structural aspects, and an accounting basis.

The pattern also keeps residue ethically and practically neutral until interpreted. Bespoke residue can be a defect, a local necessity, a safety boundary, a regulatory constraint, or a deliberately accepted exception. The repair is to name which one.

