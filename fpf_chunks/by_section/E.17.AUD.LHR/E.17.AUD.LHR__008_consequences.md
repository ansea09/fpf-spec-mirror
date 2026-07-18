---
chunk_kind: "child"
pattern_id: "E.17.AUD.LHR"
pattern_title: "PublicationUnit Stability Discipline and Local Head Restoration - repair the overloaded local lexical head before the publication unit inherits it"
section_id: "E.17.AUD.LHR:7"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.AUD.LHR/E.17.AUD.LHR__008_consequences.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "E.17.AUD.LHR — PublicationUnit Stability Discipline and Local Head Restoration - repair the overloaded local lexical head before the publication unit inherits it"
  - "E.17.AUD.LHR:7 — Consequences"
line_start: 77896
line_end: 77905
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.20"
  - "A.21"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.RT"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.2.P"
  - "E.10"
  - "E.14"
  - "E.17.AUD"
  - "E.17.AUD.OOTD"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "F.18"
keywords:
---

### E.17.AUD.LHR:7 - Consequences

Used well, this pattern:
- prevents one vague local lexical head from governing a whole section by accident;
- keeps local repair cheap instead of escalating too early;
- makes later publication-unit stability review cleaner because the local lexical head question has already been restored;
- gives authors and reviewers one common language for saying `the problem is still local`.

Used badly, it can become one more vocabulary exercise. If the publication unit still has unstable EntityOfConcern or carried-move reading after local repair, do not keep polishing the overloaded local lexical head forever. Apply the governing pattern for the remaining problem situation.

