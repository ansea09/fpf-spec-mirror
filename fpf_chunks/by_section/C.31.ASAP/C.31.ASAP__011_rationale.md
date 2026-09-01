---
chunk_kind: "child"
pattern_id: "C.31.ASAP"
pattern_title: "Architecture Scale-Amenability Preference"
section_id: "C.31.ASAP:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31.ASAP/C.31.ASAP__011_rationale.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "C.31.ASAP — Architecture Scale-Amenability Preference"
  - "C.31.ASAP:10 — Rationale"
line_start: 63144
line_end: 63149
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.CPM"
  - "A.2.6"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18.1"
  - "C.19.1"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.31"
  - "C.31.RSA"
  - "C.32"
  - "C.32.ACS"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
  - "RG"
  - "ScaleClaimTriage"
  - "architecture alternatives"
  - "architecture scale preference"
  - "coarse-graining"
  - "platform scale claim"
  - "scale amenability"
  - "scale variable"
  - "scale window"
  - "source-return condition"
  - "waiver reason"
---

### C.31.ASAP:10 - Rationale

C.31.ASAP is added because `C.31` and `C.31.RSA` can expose scale-sensitive characteristics and reusable-structure residue, but they should not themselves decide which architecture alternative is preferable under scale. C.31.ASAP governs this architecture scale-preference claim family; it is narrower than general BLP and broader than one measurement card.

The pattern adapts BLP-style scale-amenability to architecture: prefer the alternative that preserves or improves reusable structure over a declared scale window when safety, law-domain, and assurance boundaries are comparable. It requires the scale mechanism and evidence instead of accepting modularity, reuse, platform practice, or mathematical coarse-graining as the preference basis.

