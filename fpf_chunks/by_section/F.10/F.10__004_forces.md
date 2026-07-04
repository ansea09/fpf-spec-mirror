---
chunk_kind: "child"
pattern_id: "F.10"
pattern_title: "Status Families Mapping: Evidence, Standard, and Requirement Status"
section_id: "F.10:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/F.10/F.10__004_forces.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "F.10 — Status Families Mapping: Evidence, Standard, and Requirement Status"
  - "F.10:3 — Forces"
line_start: 84344
line_end: 84354
dependencies:
  - "A.2.4"
  - "B.3"
  - "F.1"
  - "F.18"
  - "F.3"
  - "F.9"
keywords:
  - "applicability windows"
  - "evidence"
  - "polarity"
  - "requirement"
  - "standard"
  - "status"
---

### F.10:3 - Forces

| Force | Tension this pattern resolves |
| --- | --- |
| Local fidelity versus reuse | Every status value belongs to one bounded context, but projects need to compare and reuse statuses across contexts. |
| Compact label versus typed relation | Status labels must stay quick to read, while the target, scope, window, source, and intended use must remain recoverable when reliance depends on them. |
| Evidence versus standard versus requirement | Evidence status is epistemic; standard and requirement statuses are deontic in different ways. Treating them as synonyms breaks reasoning. |
| Design-time stance versus run-time standing | Standards usually govern design or method choice; evidence usually comes from observed or measured work; requirements span both. |
| Display cue versus source relation | Status displays help humans find a source, but the display is not automatically the source, decision, permission, or assurance. |
| Ordinary speech versus FPF kind discipline | People say "the role of this status" or "the standard's role"; FPF recovers status-use, standard-use, requirement-use, or evidence-use relations instead of making epistemes role holders. |

