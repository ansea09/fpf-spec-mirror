---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:13.0"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__016_rationale.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:13.0 — Rationale"
line_start: 24102
line_end: 24105
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.15.5"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.6"
  - "A.2.8.PER"
  - "A.3.1"
  - "A.3.2"
  - "B.1"
  - "B.1.6"
  - "B.3"
  - "C.2.1"
  - "C.27.TA"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "U.Capability"
  - "U.Method"
  - "U.MethodDescription"
  - "U.ReferenceScheme"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.System"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "EpisodeOf_work"
  - "TemporalPartOf_work"
  - "actuals"
  - "concurrent work part"
  - "operational work part"
  - "performed enactment"
  - "trace"
  - "work occurrence"
---

### A.15.1:13.0 - Rationale

`U.Work` is kept as a dated occurrence because method, method description, work plan, affected entity, actual change, evaluation-result episteme, delivered entity, and downstream effect are different FPF objects. The same wording in a source episteme, publication occurrence, method description, or work plan can point to several of them, but performed-work claims need occurrence grounding, temporal bounds, role assignment, enacted method, and affected referent rather than a convenient method or plan label. This keeps work mereology, resource aggregation, and P2W carry-through grounded in what happened.

