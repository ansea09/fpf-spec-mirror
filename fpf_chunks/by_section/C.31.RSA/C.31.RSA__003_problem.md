---
chunk_kind: "child"
pattern_id: "C.31.RSA"
pattern_title: "Reusable Structure Accounting"
section_id: "C.31.RSA:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31.RSA/C.31.RSA__003_problem.md"
commit_sha: "434e17ec848bb7f49e6da99dfc268effb2b5b9af"
heading_path:
  - "C.31.RSA — Reusable Structure Accounting"
  - "C.31.RSA:2 — Problem"
line_start: 62496
line_end: 62503
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

### C.31.RSA:2 - Problem

Architecture teams often say that structure is reusable, repeated, templated, common, standardized, or bespoke. Those phrases are useful, but they do not say what is being counted, described, or compared. Structure can be selected from functions, flows, control relations, module interfaces, work methods, evidence packages, regulatory arguments, data schemas, deployment constraints, or exception networks.

Functional, flow, control, module-interface, work, evidence, and assurance structures may be included only when their declared `accountingBasisRef` and evidence relation named by value, assurance relation, source relation, or source-return condition are declared when those relations are being claimed.

The practical question is: which reusable loci matter, which bespoke residue remains, what source distinctions are lost by accounting, and what repair or source return follows?

