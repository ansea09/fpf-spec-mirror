---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard@Context"
section_id: "C.22.2:5"
section_title: "Relation to C.22"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__006_relation-to-c-22.md"
commit_sha: "646b0b9b164f7c13258633a33b92d2d0a569da28"
heading_path:
  - "C.22.2 — ProblemCard@Context"
  - "C.22.2:5 — Relation to C.22"
line_start: 45508
line_end: 45515
dependencies:
  - "A.10"
  - "A.15"
  - "A.19"
  - "A.21"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.Q"
  - "C.18"
  - "C.19"
  - "C.2.P"
  - "C.22"
  - "C.22.1"
  - "C.24"
  - "C.25"
  - "C.27"
  - "C.28"
  - "C.29"
  - "E.10"
  - "E.16"
  - "E.17"
  - "E.17.ID.CR"
  - "E.18"
  - "E.18.1"
  - "E.2"
  - "E.9"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
  - "P2W-ready"
  - "Thin problem card"
  - "first-principles cue"
  - "freshness and unknown disposition"
  - "problem card"
  - "problem signal"
  - "problem-side record"
  - "safe-probe-needed"
  - "setContextRef"
  - "support posture"
  - "validation boundary"
---

### C.22.2:5 - Relation to C.22

`C.22` remains the foundation for `ProblemProfile`, `TaskKind`, `TaskFamilyRef`, and `TaskSignature`. `ProblemCard@Context` is earlier and more explicit: it explains why this problem, under this context, is usable for P2W, search, comparison, characterization, refresh, retirement, or governing-pattern application.

A `ProblemCard@Context` may prepare a candidate `ProblemProfile`, bind an existing `ProblemProfile`, emit a candidate `TaskSignature`, or bind a `TaskSignature` only when P2W or selector readiness is declared. If several downstream signatures remain plausible, keep them as candidate signatures instead of binding one chosen `TaskSignature`.

This relation does not move problem-card field detail into `TaskSignature`. `TaskSignature` stays minimal for eligibility, acceptance, and selection. Downstream method, work, result, evidence, gate, autonomy, archive, portfolio, and selected-set claims remain with their governing patterns.

