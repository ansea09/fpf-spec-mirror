---
chunk_kind: "child"
pattern_id: "C.22.PFR"
pattern_title: "Problematic-For Relation"
section_id: "C.22.PFR:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.PFR/C.22.PFR__011_rationale.md"
commit_sha: "17edd955485f60cafb16159c7d90e20f4ad21844"
heading_path:
  - "C.22.PFR — Problematic-For Relation"
  - "C.22.PFR:10 — Rationale"
line_start: 51260
line_end: 51265
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.19"
  - "A.3.4"
  - "A.6.5"
  - "A.6.REL"
  - "B.3"
  - "C.22"
  - "C.22.2"
  - "E.18.1"
  - "E.23"
  - "G.11"
keywords:
  - "actual adverse condition"
  - "actual adverse episode"
  - "assessment and evidence separation"
  - "condition-to-predicate input rule"
  - "exact problem-for entity and use"
  - "independent criterion-applicability relation"
---

### C.22.PFR:10 - Rationale

Applicability is independently useful: it states which predicate applies to which entity and use under which declared criterion-applicability window even when no adverse condition currently exists. Keeping those four participants canonical there prevents disagreements between duplicated fields, while maximal continuous actual obtaining distinguishes repeated applicability occurrences without adding a fifth participant. PFR adds the exact missing fact: the named actual condition is adverse for that applicability occurrence.

The maximal continuous adverse episode resolves a genuine identity collision, but its completed interval value is not a stable reference key. Participant references plus actual adverse inception retain one occurrence reference before and after closure; the derived end completes its extent. Actual non-adverse behavior ends the occurrence and later renewed adverse truth starts another. Assessments can support, refute, or leave those boundary claims unresolved, but they neither supply the world-side boundary nor create the occurrence.

