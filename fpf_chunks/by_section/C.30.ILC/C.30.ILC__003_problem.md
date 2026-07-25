---
chunk_kind: "child"
pattern_id: "C.30.ILC"
pattern_title: "Cross-Scope Architecture Residual Triage"
section_id: "C.30.ILC:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.ILC/C.30.ILC__003_problem.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "C.30.ILC — Cross-Scope Architecture Residual Triage"
  - "C.30.ILC:2 — Problem"
line_start: 61174
line_end: 61183
dependencies:
  - "A.10"
  - "A.22"
  - "A.6.F"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.LCA"
  - "C.30.TFS-REL"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.MLAO"
  - "C.32.PAD"
  - "D.3"
  - "D.4"
  - "G.5"
  - "G.6"
keywords:
  - "cross-scope residual"
  - "declared scope"
  - "first architecture move"
  - "frustration"
  - "interlevel conflict"
  - "local repair"
  - "residual-bearing locus"
  - "structure kind"
---

### C.30.ILC:2 - Problem

Architecture work often starts from a residual: a local fix works in one declared holon level or declared scope and fails in another. Component optimization increases whole-holon or product-line integration cost. A new module boundary reduces local complexity and increases exceptions at the product-line scope. A control layer improves local safety and creates accountability or latency claims elsewhere. A reusable evidence set reduces repeated work and hides a new source-return condition.

The useful architecture intuition is narrower than a new `Frustration` kind: local optimization at one declared holon level or declared scope can create a persistent residual in another declared holon level, declared scope, or level-bearing structure relation. Depending on the claim being made, that residual is governed by `C.29` only when a recoverable multilevel mapping, scale mapping, or coarse-graining mapping is being claimed; by `C.31.ASAP` when architecture scale preference over declared alternatives is being claimed; by `C.32.MLAO` and `C.32` when residual-reducing candidate architecture work is current; and by `G.5` only when selected-set publication is current. An ordinary conflict between structures is not enough for the RG lens or frustration mathematical lens, but a conflict between structures assigned to different declared holon levels or scale windows may be enough when the mapping, preserved-structure line, and lost-structure line are recoverable. The first C.30.ILC output is only the grounded triage record.

Without a pattern, teams either discuss the residual as vague `complexity`, treat it as an ordinary negotiation problem, jump into measurement, use mathematical frustration language as proof, or jump to candidate generation too early. `C.30.ILC` keeps the first move small: identify whether the residual is architecture-shaping and name the first admissible architecture move or governing-pattern application.

The practical work is often not to draw another view. It is to assign the residual to the locus named by value that can bear it: declared holon level, declared scope, level-bearing selected structure, structure kind, constraint, characteristic or Q-bundle, evidence-reuse boundary, source-return condition, or non-architecture claim kind.

