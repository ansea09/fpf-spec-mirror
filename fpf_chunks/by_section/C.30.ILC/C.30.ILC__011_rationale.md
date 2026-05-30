---
chunk_kind: "child"
pattern_id: "C.30.ILC"
pattern_title: "Cross-Scope Architecture Residual Triage"
section_id: "C.30.ILC:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.ILC/C.30.ILC__011_rationale.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "C.30.ILC — Cross-Scope Architecture Residual Triage"
  - "C.30.ILC:10 — Rationale"
line_start: 52707
line_end: 52714
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

### C.30.ILC:10 - Rationale

Interlevel conflict and frustration are useful Plain source cues because they point to a recurrent architecture failure: local repair in one scope leaves a residual in another. They are dangerous as generic labels because they can hide which scope, structure kind, relation, or source-return condition is actually responsible.

A local optimum or successful local repair is therefore not treated as whole-architecture adequacy. It becomes architecture-relevant only when the cross-scope residual carrier is recoverable and the next move can be named.

`C.30.ILC` keeps the cue but recovers the object. It treats conflict/frustration as architecture-shaping only when declared scopes and architecture structure kinds are named. This lets FPF support the practical intuition without introducing a second ontology of levels, a hidden measurement pattern, or a prescribed architecture work order.

