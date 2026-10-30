---
chunk_kind: "child"
pattern_id: "C.2.5"
pattern_title: "Language-State Closure Degree — How Fixed Is the Current Candidate Space?"
section_id: "C.2.5:15"
section_title: "Extension and Migration Notes"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.5/C.2.5__016_extension-and-migration-notes.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "C.2.5 — Language-State Closure Degree — How Fixed Is the Current Candidate Space?"
  - "C.2.5:15 — Extension and Migration Notes"
line_start: 53639
line_end: 53648
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.18"
  - "B.4.1"
  - "B.5.2.0"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.LS"
keywords:
  - "CD0–CD5"
  - "candidate-space closure"
  - "closure degree"
  - "frame space"
  - "reopen"
  - "route space"
  - "settledness"
---

### C.2.5:15 - Extension and Migration Notes

#### C.2.5:15.1 - Local anchor refinement
Contexts may refine the starter closure anchors, but shall keep the ordinal progression and the explicit link to reopen/backoff discipline.

#### C.2.5:15.2 - Migration from readiness language
When routing, endpoint use or reopening depends on words such as "settled", "closed", "final", or "open", recover the claimed fixity and its grounds. Use an explicit `CD` reading when that scale is needed and a named `A.16.2` move when the closure changes. Sufficient ordinary wording needs no separate level solely to repeat it.

#### C.2.5:15.3 - Boundary reminder
`CD` is not warrant strength and not a gate decision. It speaks only about the local fixity of the current episteme or publication position and its candidate space.
