---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "Static and Regression Conformance Harness for Unification"
section_id: "F.15:14"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__018_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "036c056e98c38522172c6b7b3ad08214281cc4e4"
heading_path:
  - "F.15 — Static and Regression Conformance Harness for Unification"
  - "F.15:14 — Common Anti-Patterns and How to Avoid Them"
line_start: 95396
line_end: 95413
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.6"
  - "A.2.7"
  - "A.22"
  - "A.6.1"
  - "A.6.5"
  - "B.3"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.24.PUB"
  - "F.1-F.14"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.6"
  - "F.8"
  - "F.9"
  - "G.11"
keywords:
  - "SenseCell testing"
  - "acceptance tests"
  - "regression tests"
  - "static checks"
  - "validation"
---

### F.15:14 - Common Anti-Patterns and How to Avoid Them

| Code | Anti-pattern | Symptom | Why it breaks | Harness catch and repair |
| --- | --- | --- | --- | --- |
| H1 | Row by table shape | A local note or one-cell display is accepted or rejected solely by cell count | F.17 row truth depends on its episteme and gate, not shape; one-cell rows can be valid | SCR-F15-S9 checks the exact row and admitted use |
| H2 | Bridge by label or Card | Same spelling or a filled Card is treated as relation truth | Imports meaning and hides occurrence/predicate boundaries | SCR-F15-S12/S13 require exact cells, profile, truth, dependencies, use claim, and reliance |
| H3 | Silent edition swap | An edition or stable id is cited as continuity | Retcons exact earlier claims | RSCR-F15-E1 names exact refs and the direct continuity/change claim |
| H4 | Locality blur | A local-sense label hides scheme, expression, or claim | Globalizes meaning | SCR-F15-S2/S3 recover the exact basis and SchemeSenseCell triple |
| H5 | Window as type | A time, scale, phase, or confidence variant becomes a new status family | Status inflation | SCR-F15-S14 and RSCR-F15-E11 return to the direct status owner |
| H6 | Role fusion by convenience | Description, bundle, incompatibility, or name becomes one role | Hides value, relation, assignment, and work | SCR-F15-S7/S15 return to F.4 and exact role-relation owners |
| H7 | Alias as merge | Expression lineage hides value, scheme, or sense change | Loses history and identity | RSCR-F15-E7/E8 require exact continuity before alias treatment |
| H8 | `CL` or witness optimism | Evidence shorthand silently strengthens relation or use authority | Confuses evidence, relation truth, and bounded use | RSCR-F15-E9/E10 re-test the exact occurrence and separate use claim |
| H9 | Plain label drift | Plain expression suggests another kind or claim | Reader imports a wrong prototype | SCR-F15-T1-T4 return to the current F.18 settlement |
| H10 | Scope membership as evidence | A member is considered supported because it is listed | Selection has no evidential force | CC-F15-3/9 require exact result and evidence refs |
| H11 | Record performs check | Filling `StaticRuleResults` is treated as an application or Work | Erases occurrence and result identity | Cite A.6.1 application/A.15.1 Work and C.2.1 result separately |
| H12 | Witness is result | A trace, example, or report is labelled `pass` | Carrier presence establishes no claim | Cite the result episteme and A.10 path separately |
| H13 | Description replaces occurrence | Bridge, Structure, status, or row description is checked as the subject itself | Confuses description truth with world-side or governed object | Resolve the exact occurrence/value and keep its description as a neighbor |

