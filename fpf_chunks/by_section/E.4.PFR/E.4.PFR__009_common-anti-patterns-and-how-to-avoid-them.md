---
chunk_kind: "child"
pattern_id: "E.4.PFR"
pattern_title: "Pattern-Framework Relation and Edition Discipline"
section_id: "E.4.PFR:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFR/E.4.PFR__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "E.4.PFR — Pattern-Framework Relation and Edition Discipline"
  - "E.4.PFR:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 66991
line_end: 67001
dependencies:
  - "A.10"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.11"
  - "E.11.PUR"
  - "E.17"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.4"
  - "E.4.DPF.DA"
  - "E.4.FPF"
  - "E.4.PFAD"
  - "E.5.3"
  - "E.9"
  - "F.18"
  - "G.11"
  - "G.2"
  - "G.5"
keywords:
---

### E.4.PFR:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Related-pattern flattening | A relation list hides relation function and owner. | Convert load-bearing rows into `PatternFrameworkRelationRecord@Context`. |
| Dependency as specialization | A framework edition dependency is read as child-pattern inheritance. | Use `FrameworkEditionDependencyRecord@Context` and state any specialization separately. |
| Compatibility by version label | A new edition number is assumed to settle impact. | Add compatibility boundary, deprecation, supersession, and refresh conditions. |
| Generated graph as relation authority | A produced graph decides relation meaning. | Use `C.35` for admission, then record relation functions through PFR. |
| Callable route as dependency | A skill, MCP endpoint, API route, or assistant integration is read as framework edition dependency, runtime import, or method order. | Record an `Access relation` with bounded use and blocked stronger reading; route tool/work behavior, generated outputs, and currentness claims to their owners. |
| Source prose as relation authority | A paragraph says a source or DRR "supports" a pattern but does not state bounded use, owner, or return condition. | Record `Source or decision reuse` with `G.2`, `E.9`, or `A.10` as owner and a source-return condition. |

