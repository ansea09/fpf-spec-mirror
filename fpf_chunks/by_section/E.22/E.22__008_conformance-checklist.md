---
chunk_kind: "child"
pattern_id: "E.22"
pattern_title: "Improvement-Oriented Quality-Read Question Framing"
section_id: "E.22:7"
section_title: "Conformance checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.22/E.22__008_conformance-checklist.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "E.22 — Improvement-Oriented Quality-Read Question Framing"
  - "E.22:7 — Conformance checklist"
line_start: 67671
line_end: 67697
dependencies:
  - "A.19.ECS"
  - "C.17-C.19"
  - "C.25"
  - "E.10"
  - "E.19"
  - "E.2.DA"
  - "E.21"
  - "E.23"
  - "E.9.DA"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.22:7 - Conformance checklist

| ID | Requirement | Why |
|---|---|---|
| `CC-E22-1` | A nontrivial quality read SHALL name the exact object version under quality read. | Prevents chat memory, source bundles, or campaigns from replacing the object. |
| `CC-E22-2` | A nontrivial quality read SHALL name the object-under-improvement evaluation. | Prevents `E.22` from supplying another evaluation's values. |
| `CC-E22-3` | If no read purpose is declared, the read SHALL be treated as `floorRead`. | Prevents false expectation of exceptional improvement. |
| `CC-E22-4` | `exceptionalImprovementRead` SHALL name the coordinates or active characteristic menu whose values may be raised. | Prevents vague "make it excellent" prompts. |
| `CC-E22-5` | `paretoTradeoffRead` SHALL name protected qualities or use the object-under-improvement evaluation's active protected coordinates. | Prevents Goodhart-style coordinate optimization. |
| `CC-E22-6` | `openQuestionDiscoveryRead` SHALL classify unasked questions as existing-coordinate issue, candidate coordinate or overlay, or outside object-under-improvement evaluation. | Prevents unbounded scope expansion. |
| `CC-E22-7` | `absorptionRead` SHALL record quality impact, not only accepted or applied disposition. | Makes returned review absorption improve the object rather than only close a checklist. |
| `CC-E22-8` | A quality-read frame SHALL state a non-use boundary when the result could be overread as project evidence, assurance, gate, release, certification, safety, compliance, work authority, general approval, checklist-count closure, or discharge-count closure. | Keeps neighbouring pattern authority intact and blocks checklist-count overread. |
| `CC-E22-9` | A reviewer SHALL NOT treat `floorRead` success as evidence that no exceptional improvement is possible. | Keeps admissibility separate from optimization. |
| `CC-E22-10` | A reviewer SHALL NOT treat `exceptionalImprovementRead` as permission to damage declared protected trade-offs. | Keeps improvement multi-coordinate and non-Goodhart. |
| `CC-E22-11` | A quality-read frame SHALL keep review-purpose declaration separate from the receiving quality result. | Prevents the prompt from becoming the quality read. |
| `CC-E22-12` | If the read purpose changes during review or absorption, the frame SHALL be updated or the extra result SHALL be marked outside the declared frame. | Keeps the answer replayable. |
| `CC-E22-13` | A quality-read frame SHALL be repaired before the object-under-improvement evaluation runs when it lacks object version, object-under-improvement evaluation, purpose or default, required protected trade-offs, required classification rule, or non-use boundary for an overread-prone result. | Makes frame sufficiency and lowering conditions testable. |
| `CC-E22-14` | A quality-read frame SHALL keep object kind and object-under-improvement evaluation distinct. Pattern reads use `E.21`; `DRR` reads use `E.9.DA`; other objects use their declared characteristic space, quality bundle, rubric, scale set, review profile, or exact FPF evaluation pattern. | Prevents unnecessary specialization while blocking unbounded "review anything" overread. |
| `CC-E22-15` | A quality-read frame SHALL NOT ask the reviewer to raise or lower values from popularity, adoption, prior use, absence of use, review count, reviewer praise, external-review completion, landing, release, or award-like signals. If such a signal matters, the frame SHALL require the object-under-improvement evaluation to rewrite it into object-content evidence or leave it outside the value read. | Prevents reputation medals from entering the question before the object-under-improvement evaluation runs. |
| `CC-E22-16` | Any actionable returned quality-review finding SHALL be represented as a stable `QualityReviewFindingRow` with row id, review locus, object locus, object-under-improvement evaluation effect, expected quality movement, correction direction, closure test, disposition, and discharge evidence when applied. | Prevents narrative findings from becoming uncheckable executor work. |
| `CC-E22-17` | Actionable quality-review findings SHALL be discharged row by row. One edit MAY close several rows, but each affected row SHALL still be revisited with a separate disposition, changed or unchanged object locus, and closure-test evidence. | Catches "I handled the group" and range-closure failures. |
| `CC-E22-18` | If a quality-read result becomes part of repeated improvement, the repeated method SHALL be governed by `E.23` rather than by extra loop doctrine inside `E.22`. | Keeps one-read question framing distinct from the quality-improvement method. |
| `CC-E22-19` | When the object version under quality read is OEE/NQD material, the quality-read frame SHALL name the exact candidate, front, archive, shortlist, parity report, refresh report, or declared transduction result; the governing pattern that carries its semantics; the read purpose; and the non-use boundary that keeps candidate quality, archive/front semantics, selected-set publication, parity, and refresh distinct. | Lets quality reads plug into OEE/NQD without turning `E.22` into generator, selector, archive, parity, or refresh doctrine. |
| `CC-E22-20` | If a read is expected to suggest what to do next, the frame SHALL say that the result is only a candidate improvement proposal or next-admissible-move hypothesis unless the exact neighbouring pattern is opened for decision, planning, work, gate, evidence, assurance, selected-set publication, parity, refresh, or pool-policy authority. | Preserves the pragmatic usefulness of reads without letting review language smuggle project claims beyond the quality-read frame. |
| CC-E22-21 | If a read is used before OEE/NQD candidate generation or candidate change, it SHALL state the object-under-improvement evaluation pressure, expected movement, protected trade-off, and closure test that make each candidate-change proposal worth generating. | Prevents exploration from degrading into unguided candidate changes while keeping generation, pool policy, selected-set publication, parity, and refresh in the governing patterns. |
| `CC-E22-22` | If a read returns a proposal portfolio, it SHALL state that proposal generation, NQD candidate generation, front or archive insertion, proposal selection, selected-set publication, parity, and refresh belong to exact neighbouring patterns rather than to `E.22`. | Lets a review produce useful alternatives without turning the read into an OEE/NQD selection or publication result. |

