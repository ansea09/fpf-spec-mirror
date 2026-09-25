---
chunk_kind: "child"
pattern_id: "A.2.8"
pattern_title: "U.Commitment — Individual Duties to Act or Refrain"
section_id: "A.2.8:10"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.8/A.2.8__013_consequences.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "A.2.8 — U.Commitment — Individual Duties to Act or Refrain"
  - "A.2.8:10 — Consequences"
line_start: 7317
line_end: 7332
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.3"
  - "A.2.6"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.6.B"
  - "A.6.C"
  - "A.6.RCD"
  - "A.7"
  - "C.3"
  - "F.6"
keywords:
  - "actual bearer"
  - "constitutive rule"
  - "do not identify an individual bearer or institute a duty. Adapt"
  - "individual duty"
  - "instituting basis"
  - "obligation"
  - "prohibition"
  - "recommendation-as-duty"
  - "validity interval"
---

### A.2.8:10 - Consequences

**Benefits**

- Generic policy content and actual duty no longer collapse.
- Actual bearers are directly recoverable.
- Modality, scope, referents, and validity remain lintable.
- Assignment and responsibility independence is explicit.
- Assurance can be added proportionately without becoming universal process overhead.

**Costs and mitigations**

- A positive individual-duty claim needs more than a policy sentence. This is the necessary cost of claiming a world-side relation; generic policy content remains cheap to state.
- Domains with another instituting basis need the pattern that defines that basis. Until then, return the exact `missing-governor` result.
- Conflict resolution remains outside this pattern. Preserve each current commitment plus the exact source, independently obtaining authority relation, and selecting rule required by the named conflict or choice use; apply D.3/D.4 for an interlevel ethical conflict, C.11 for an explicit choice among available options, or return `missing-governor[commitment conflict resolution]` when no direct result rule exists.

