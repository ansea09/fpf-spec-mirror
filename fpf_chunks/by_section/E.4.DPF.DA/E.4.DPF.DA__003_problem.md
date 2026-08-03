---
chunk_kind: "child"
pattern_id: "E.4.DPF.DA"
pattern_title: "Domain Principle Framework Package-Adequacy Evaluation CharacteristicSpace"
section_id: "E.4.DPF.DA:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.DPF.DA/E.4.DPF.DA__003_problem.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "E.4.DPF.DA — Domain Principle Framework Package-Adequacy Evaluation CharacteristicSpace"
  - "E.4.DPF.DA:2 — Problem"
line_start: 70864
line_end: 70875
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.19.ECS"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.22"
  - "A.3.1"
  - "A.3.2"
  - "A.6.1"
  - "C.2.1"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.11"
  - "E.17"
  - "E.19"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.24.PUB"
  - "E.4"
  - "E.4.DPF"
  - "E.4.PFAD"
  - "E.4.PFR"
  - "F.18"
  - "G.11"
  - "G.2"
  - "U.Method"
keywords:
---

### E.4.DPF.DA:2 - Problem

DPF packages will often be produced quickly from source material, prompts, external literature, local practice, or generated candidates. Some are good enough as seeds; some can answer a domain question for an AI agent; some are public-ready publication carriers; some are only source summaries wearing pattern headings.

Without a DPF-specific adequacy evaluation, teams tend to use one of three wrong substitutes:

- they apply `E.2.DA` and ask whether the package is "FPF-like in general", even though the package is meant for one domain;
- they average `E.21` scores of individual patterns and miss package-level failures such as missing source packs, broken dependency direction, poor first entry, or stale edition records;
- they inspect section presence and conclude that an all-in-one carrier, map, or seed package is adequate because it has patterns, a table of contents, a readme, a preface, maps, and sources.

The result is adoption risk. A reader may get a fluent local framework that does not know its domain boundary, does not preserve rival source traditions, duplicates FPF Core ontology, hides relation functions, has no refresh route, or cannot tell a practitioner what typical problem is live, which known failure mode to avoid, and which SoTA solution move to try first.

