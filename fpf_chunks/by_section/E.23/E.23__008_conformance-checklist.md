---
chunk_kind: "child"
pattern_id: "E.23"
pattern_title: "Quality Improvement Loop Method"
section_id: "E.23:7"
section_title: "Conformance checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.23/E.23__008_conformance-checklist.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "E.23 — Quality Improvement Loop Method"
  - "E.23:7 — Conformance checklist"
line_start: 68912
line_end: 68936
dependencies:
  - "A.19.ECS"
  - "C.17-C.19"
  - "C.19.1"
  - "C.22.1"
  - "C.24"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.9.DA"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.23:7 - Conformance checklist

| ID | Requirement | Why |
|---|---|---|
| `CC-E23-1` | A quality-improvement loop SHALL name the exact `ObjectUnderImprovementRef` and object version under improvement. | Prevents campaigns, chats, source bundles, or task lists from replacing the object under improvement. |
| `CC-E23-2` | A quality-improvement loop SHALL name the exact `ObjectUnderImprovementEvaluationRef` before values, floors, or stop meanings are used; if none exists, the object-under-improvement evaluation `CharacteristicSpace` SHALL be constructed or repaired through `A.19.ECS` before the loop opens. | Prevents `E.23` from inventing quality values. |
| `CC-E23-3` | The first quality review in the loop SHALL be framed through `E.22` or an explicitly equivalent object-under-improvement evaluation question frame. | Keeps one-read question framing distinct from the repeated method. |
| `CC-E23-4` | Returned actionable findings SHALL be row-atomic, with expected object-under-improvement evaluation movement and closure test recoverable. | Prevents "handled overall" improvement claims. |
| `CC-E23-5` | Row-discharge evidence SHALL NOT be treated as coordinate improvement until the changed object version is re-read by the object-under-improvement evaluation. | Blocks checklist-count and discharge-count substitution. |
| `CC-E23-6` | Every continue decision SHALL state the expected object-under-improvement evaluation movement for the next pass. | Prevents unbounded retry. |
| `CC-E23-7` | Every operation family selected for a loop SHALL name expected object-under-improvement evaluation movement, failure mode, cost and risk reason, protected trade-offs, and stop or removal condition. | Blocks automatic bureaucracy and optional-operation drift. |
| `CC-E23-8` | A method-family selection SHALL state the characteristic-space fit and BLP cost boundary for the object under improvement. | Prevents importing PDCA or PDSA, POOGI, OODA, Ralph-like, or specialized cycles as universal sequences. |
| `CC-E23-9` | A loop SHALL record protected trade-offs and what got worse whenever visible coordinates improve. | Prevents Goodhart-style improvement. |
| `CC-E23-10` | A loop SHALL keep `A.19.ECS`, `E.21`, `E.9.DA`, `E.2.DA`, `F.18`, `C.25`, `C.16.Q`, `C.19.1`, `C.22.1`, and `C.24` in their governed roles when those roles are live. | Prevents neighbour theft. |
| `CC-E23-11` | A loop result SHALL NOT be reused as evidence, assurance, gate, release, safety, compliance, or work authority without opening the exact neighbouring FPF pattern for that claim. | Keeps project-side claims out of the improvement method. |
| `CC-E23-12` | A clean `floorRead` SHALL be allowed to stop through `E.22` plus the object-under-improvement evaluation without opening this method. | Keeps ordinary quality reads affordable. |
| `CC-E23-13` | An all-exceptional or all-`5` result SHALL carry an explicit object-under-improvement evaluation coordinate-value table over the changed object version. | Prevents floor pass, landing, or praise from becoming exceptional-value evidence. |
| `CC-E23-14` | Load-bearing source, authority, basis, support, record, and view wording SHALL recover exact kind or relation under `E.10`. | Keeps loop prose from reintroducing umbrella language. |
| `CC-E23-15` | A closed loop pass SHALL leave a `QualityImprovementLoopRecord` with object version under improvement, object-under-improvement evaluation, applied rows, object-under-improvement evaluation re-read, trade-offs, cost and risk account, and stop decision recoverable by value. | Prevents quality closure from being reconstructed from chat memory, praise, or checklist closure. |
| `CC-E23-16` | If `E.22` returns a proposal portfolio, the loop SHALL keep proposal rows, selected changes to the object version under improvement, rejected proposals, object-under-improvement evaluation re-read, and neighbour exits distinct. | Prevents a review portfolio from becoming a hidden selector result. |
| `CC-E23-17` | If the object-under-improvement evaluation is the `Q` side of NQD/OEE, the loop SHALL name the `Q` components, external comparison basis, comparison set or current front, expected `Q` movement, protected trade-offs, and neighbour exits for generation, archive or front handling, selected-set publication, parity, and refresh. | Lets improvement move candidates in NQD without stealing OEE/NQD semantics or self-assigning exceptional status. |
| `CC-E23-18` | An all-`5`, all-exceptional, current-front-reaching, or current-front-improving result SHALL be treated as a local stop condition for this object-under-improvement evaluation and comparison set, not as proof that further development is impossible. | Prevents maturity-ceiling stagnation while still allowing this loop to close. |
| `CC-E23-19` | A source-bearing loop that claims `SoTA` reach, `SoTA` maintenance, or front improvement SHALL name the external source of that front and SHALL state the source or practice lines composed, object-under-improvement evaluation coordinates affected, and protected characteristics preserved. | Prevents "we cited SoTA" from becoming a self-assigned `SoTA` claim. |
| `CC-E23-20` | When a loop composes several accepted source or practice lines, it SHALL assign each line a contribution, keep contribution strata distinguishable, and state the `SourceComposedResultClaim` before claiming movement toward or maintenance of the external front. | Keeps SoTA reach and maintenance architectural rather than decorative. |

