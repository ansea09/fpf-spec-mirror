---
chunk_kind: "child"
pattern_id: "A.6.9"
pattern_title: "Cross-Context Sameness Disambiguation - Repairing cross-context \"same\", \"equivalent\", and \"align\" via explicit Bridges (RPR-XCTX)"
section_id: "A.6.9:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.9/A.6.9__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "A.6.9 — Cross-Context Sameness Disambiguation - Repairing cross-context \"same\", \"equivalent\", and \"align\" via explicit Bridges (RPR-XCTX)"
  - "A.6.9:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 20728
line_end: 20746
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.6"
  - "A.2.1"
  - "A.2.6"
  - "A.2.8.PER"
  - "A.22"
  - "A.6.3.RT"
  - "A.6.6"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.2.1"
  - "C.29"
  - "C.3.2"
  - "C.3.3"
  - "E.17"
  - "E.17.0"
  - "E.19"
  - "E.24.PUB"
  - "F.0.1"
  - "F.17"
  - "F.18"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "A.10/B.3 reliance"
  - "LocalSenseClaim> projections"
  - "actual receiving object"
  - "ambiguous sameness"
  - "different <ReferenceScheme"
  - "direct-owner dispatch"
  - "exact F.17 SchemeSenseCell endpoints"
  - "explicit stop"
  - "relation-only F.9 Bridge"
  - "separate C.2.1 bounded-use claim"
---

### A.6.9:8 - Common Anti-Patterns and How to Avoid Them

| ID | Anti-pattern | Failure | Repair |
| --- | --- | --- | --- |
| `AP-XCTX-1` | Bridge by adjective | *Same* or *aligned* hides relation and action. | Name the action; dispatch it; test F.9 only if semantic correspondence remains. |
| `AP-XCTX-2` | Scheme difference becomes relation | Two schemes differ, so a Bridge is presumed. | Treat difference as a trigger only; establish the direct predicate. |
| `AP-XCTX-3` | Profile as use licence | Direction, rule, or tolerated loss is embedded in profile identity. | Move it to the separate C.2.1 bounded-use claim. |
| `AP-XCTX-4` | Bridge-alone substitution | An obtaining Bridge is cited as sufficient for a use. | Require the affirmative bounded-use claim and current A.10 or B.3 reliance. |
| `AP-XCTX-5` | Mapping witness becomes semantics | A lookup, score, or ETL path proves the relation or use. | Keep it as evidence and test both propositions explicitly. |
| `AP-XCTX-6` | String or id becomes endpoint | A word, file, id, or system fills a SenseCell slot. | Resolve the exact F.17 cell; handle ids under A.6.6. |
| `AP-XCTX-7` | Symmetry grants two use directions | One symmetric occurrence is read as two licences. | State each direction in its own use claim. |
| `AP-XCTX-8` | Loss note becomes tolerance | An observed difference is assumed acceptable. | Keep it in evidence and name accepted loss as `t`. |
| `AP-XCTX-9` | Confidence laundering | Higher `CL` or reviewer approval grants a use. | Treat `CL` as evidence shorthand and recover claim polarity plus reliance. |
| `AP-XCTX-10` | Suitability becomes permission | An affirmative semantic claim is read as authorization. | Apply A.2.8.PER and cite the needed grant, non-prohibition, exercise, or conflict result; if it is absent or unresolved, state that exact result. |
| `AP-XCTX-11` | Named use becomes occurrence | “Publication use” is treated as a publication. | Recover the exact publication occurrence under E.24.PUB, or recover another receiving object and cite the pattern that defines it. |
| `AP-XCTX-12` | Chain upgrade | A-to-B and B-to-C become direct A-to-C equivalence. | Test a direct A-to-C Bridge and composite use independently. |
| `AP-XCTX-13` | Timeless or facetless claim | Edition or compared facet stays hidden. | State applicability and refine endpoint readings. |
| `AP-XCTX-14` | Kernel promotion | A strong Bridge is used to admit one global U-kind. | Apply E.24.UK and A.11 independently. |

