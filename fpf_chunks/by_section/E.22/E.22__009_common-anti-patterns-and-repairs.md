---
chunk_kind: "child"
pattern_id: "E.22"
pattern_title: "Improvement-Oriented Quality-Read Question Framing"
section_id: "E.22:8"
section_title: "Common anti-patterns and repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/E.22/E.22__009_common-anti-patterns-and-repairs.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "E.22 — Improvement-Oriented Quality-Read Question Framing"
  - "E.22:8 — Common anti-patterns and repairs"
line_start: 66883
line_end: 66901
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

### E.22:8 - Common anti-patterns and repairs

| Anti-pattern | Failure | Repair |
|---|---|---|
| **"Review this" prompt.** | The reviewer chooses a purpose implicitly. | Add `QualityReadPurposeSelection` and the object-under-improvement evaluation. |
| **Blocker audit sold as improvement.** | The result only reaches the floor while the requester expected exceptional improvement. | Add `exceptionalImprovementRead` and per-coordinate improvement questions. |
| **Maximal rewrite sold as review.** | The result proposes broad optimization when only readiness was asked. | Narrow to `floorRead` or state the extra purpose explicitly. |
| **All-to-five Goodharting.** | Visible values rise while ordinary use, affordability, locality, or corpus ecology falls. | Add `paretoTradeoffRead` and protected trade-offs. |
| **Open-question silence.** | The reviewer answers the given checklist but misses a missing governing question. | Add `openQuestionDiscoveryRead` and a classification rule. |
| **Applied-count absorption.** | Absorption reports how many suggestions were applied but not what quality changed. | Add `absorptionRead` and impact classification. |
| **Checklist-count quality closure.** | A discharge table says every row is closed, and that count is treated as the quality result. | Run or cite the object-under-improvement evaluation on the changed object; keep row discharge as executor evidence, not quality closure. |
| **Full-loop capture.** | `E.22` starts governing repeated improvement, method-family selection, or stop or switch decisions across passes. | Use `E.22` only to frame each quality read; use `E.23` for the repeated quality-improvement method. |
| **Object-under-improvement evaluation theft.** | The frame starts defining coordinates that belong to `E.21`, `E.9.DA`, `C.16`, `C.25`, a local rubric, or another object-under-improvement evaluation. | Keep `E.22` to purpose declaration; run the exact object-under-improvement evaluation for the read. |
| **Portfolio-quality blur.** | A request asks whether "the portfolio is good" while mixing candidate quality, front/archive semantics, selected-set publication, parity, and refresh. | Name the exact object version under quality read and the governing pattern: `C.17`, `C.18`, `C.19`, `G.5`, `G.9`, or `G.11`; keep `E.22` to the read purpose and non-use boundary. |
| **Recommendation smuggled as reading.** | A read result says what to do next as if it had already decided, planned, approved, or scheduled the move. | Keep the result as a candidate improvement proposal or next-admissible-move hypothesis, or open `C.11`, `C.24`, `A.15`, `A.20`, `A.21`, `A.10`, `B.3`, `G.5`, `G.9`, or `G.11` for the claim that exceeds the quality-read frame. |
| **Unguided candidate change dressed as exploration.** | Candidate material is changed or generated without saying what object-under-improvement evaluation movement the change is meant to test. | Run candidateImprovementProposalRead; state expected movement, affected locus, protected trade-offs, closure test, and OEE/NQD neighbour exit before generation or candidate change. |
| **Single-improvement narrowing.** | The read chooses one improvement when the live request needs a proposal portfolio for NQD comparison or OEE exploration. | Return bounded proposal rows and hand generation, selection, front or archive handling, selected-set publication, parity, and refresh to `C.18`, `C.19`, `G.5`, `G.9`, or `G.11`. |
| **Reputation-medal prompt.** | The request asks the reviewer to score higher because the object is popular, reviewed, landed, awarded, or already used, or lower because it is new and unused. | Rewrite the signal into an exact content-evidence question governed by the object-under-improvement evaluation, or exclude it from the quality value. |

