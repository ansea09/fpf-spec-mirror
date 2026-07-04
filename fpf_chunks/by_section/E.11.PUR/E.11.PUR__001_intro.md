---
chunk_kind: "child"
pattern_id: "E.11.PUR"
pattern_title: "Pattern-Use Recommendation and Pattern-Use Sequence"
section_id: "E.11.PUR:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PUR/E.11.PUR__001_intro.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "E.11.PUR — Pattern-Use Recommendation and Pattern-Use Sequence"
  - "E.11.PUR:intro — Intro"
line_start: 70821
line_end: 70836
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.3"
  - "A.15.5"
  - "A.16"
  - "A.21"
  - "C.24"
  - "C.30"
  - "C.30.AD"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.MOVE"
  - "E.11"
  - "E.17"
  - "E.18.1"
  - "E.24"
  - "E.8"
keywords:
---

## E.11.PUR - Pattern-Use Recommendation and Pattern-Use Sequence

> **Type:** Pattern-language governance pattern (E)
> **Status:** Stable
> **Normativity:** Normative for FPF pattern-use recommendation and pattern-use sequence records.

**At a glance.** `E.11.PUR` governs the relation in which one FPF pattern use, or a short sequence of pattern uses, is recommended for a current project concern. It keeps ordinary "first useful move" speech teachable while preventing a new root `U.Move` kind.

**Use this when.** Use this pattern when a practitioner, manager, or assisting agent needs to decide which FPF pattern use is worth taking next for a recognizable project concern after applicability has been checked.

**Primary EntityOfConcern.** One `PatternUseRecommendation@Context`: the relation between a current project concern, a bounded context, one or more candidate FPF pattern uses, an applicability finding, the recommended pattern use, and the expected practical result.

**First output.** One compact `PatternUseRecommendation@Context` or `PatternUseSequence@Context` record that names the current concern, the recommended pattern use, the reason for recommending it, the expected output shape, blocked stronger uses, and any neighboring governing pattern that becomes current after this use.

**Not this pattern when.** If accepted problem-side material is being carried through P2W, use `E.18.1`. If work is being planned or performed, use the A.15 family. If a gate decision is current, use `A.21`. If a tool-call plan is current, use `C.24`. If the sentence is only about publication, phrase wording, or description use, use `E.8`, `E.17`, or the direct publication or description pattern.

