---
chunk_kind: "child"
pattern_id: "C.30.ILC"
pattern_title: "Cross-Scope Architecture Residual Triage"
section_id: "C.30.ILC:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.ILC/C.30.ILC__003_problem.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "C.30.ILC — Cross-Scope Architecture Residual Triage"
  - "C.30.ILC:2 — Problem"
line_start: 51885
line_end: 51892
dependencies:
  - "A.10"
  - "A.22"
  - "A.6.F"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.LCA"
  - "C.30.TGA-FLOW-REL"
  - "D.3"
  - "D.4"
  - "G.5"
  - "G.6"
keywords:
  - "cross-scope residual"
  - "declared scope"
  - "frustration"
  - "interlevel conflict"
  - "local repair"
  - "source return"
  - "structure kind"
---

### C.30.ILC:2 - Problem

Architecture work often starts from a residual: a local fix works in one scope and fails in another. Component optimization increases system integration cost. A new module boundary reduces local complexity and increases exceptions at the product-line scope. A control layer improves local safety and creates accountability or latency claims elsewhere. A reusable evidence set reduces repeated work and hides a new source-return obligation.

Without a pattern, teams either discuss the residual as vague `complexity`, treat it as ordinary stakeholder conflict, jump into measurement, or open a new architecture synthesis effort too early. `C.30.ILC` keeps the first move small: identify whether the residual is architecture-shaping and name the first admissible architecture move or exact neighboring-pattern exit.

The practical work is often not to draw another view. It is to distribute the residual across the carrier that can actually bear it: declared scope, structure kind, constraint, characteristic or Q-bundle, evidence-reuse boundary, source-return condition, or neighboring-pattern claim kind.

