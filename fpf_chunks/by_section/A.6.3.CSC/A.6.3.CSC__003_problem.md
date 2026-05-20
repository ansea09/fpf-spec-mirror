---
chunk_kind: "child"
pattern_id: "A.6.3.CSC"
pattern_title: "Controlled Semantic Coarsening"
section_id: "A.6.3.CSC:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.CSC/A.6.3.CSC__003_problem.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "A.6.3.CSC — Controlled Semantic Coarsening"
  - "A.6.3.CSC:2 — Problem"
line_start: 10285
line_end: 10298
dependencies:
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.P"
  - "C.26"
  - "C.26.1"
  - "E.10"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.19"
  - "E.8"
  - "F.18"
  - "F.9"
  - "F.9.1"
keywords:
  - "coarsened rendering"
  - "controlled semantic coarsening"
  - "dashboard tile"
  - "lookup handle"
  - "narrower admissible use"
  - "non-admissible downstream use"
  - "redaction"
  - "reopen trigger"
  - "source-bearing episteme or source publication"
  - "state-representation shortcut"
---

### A.6.3.CSC:2 - Problem

FPF often needs a coarsened form of a source-bearing side: a manager summary, a redacted disclosure note, a dashboard tile, a lookup surrogate, a workshop simplification, or a didactic compression. The coarsened form can be valuable, but it becomes dangerous when readers forget that its admissible use is narrower than the source-bearing side.

The core failure is not ordinary omission by itself. The failure appears when the coarsened rendering stays honest only under an admissible-use card like this:

- the source-bearing side remains governing;
- the coarsened rendering has a declared `source-loss mode` or reduced recoverability;
- the target makes only the narrower use admissible;
- downstream use is non-admissible from the coarsened rendering alone;
- downstream use reopens the source-bearing side or moves to the exact governing FPF pattern or `authoritySourceRef` target that supports the requested use.

Without a named pattern for that relation, neighboring patterns repeat partial coarsening rules locally. The repetition hides the shared load and makes it too easy for coarsened renderings to travel as if they were the source-bearing side.

