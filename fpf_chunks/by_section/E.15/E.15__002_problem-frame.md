---
chunk_kind: "child"
pattern_id: "E.15"
pattern_title: "Pattern Change, Edition Continuity, and Impact Analysis"
section_id: "E.15:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.15/E.15__002_problem-frame.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "E.15 — Pattern Change, Edition Continuity, and Impact Analysis"
  - "E.15:1 — Problem Frame"
line_start: 80981
line_end: 80994
dependencies:
  - "C.18"
  - "C.19"
  - "E.10"
  - "E.19"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.24.PUB"
  - "E.8"
  - "E.9"
  - "F.0.1"
  - "F.1"
  - "F.15"
  - "F.9"
keywords:
---

### E.15:1 - Problem Frame

Use this pattern when an existing FPF pattern is being corrected, clarified, reorganized, refreshed from current sources, split, merged, renamed, or changed semantically, and someone needs to know what may continue and what must be reconsidered.

The primary `EntityOfConcern`—the thing being changed—is one exact existing FPF pattern edition. The candidate is its proposed successor. The useful result is that candidate plus a bounded account of what actually changed, which uses may be affected, which predecessor ideas remain, and which checks were rerun. Put that account in the decision, review, campaign, or landing result that needs it; this pattern does not require a separate trace object.

**First useful move.** Put the predecessor and candidate side by side and finish this sentence in ordinary language:

> A reader or user who relied on `<predecessor passage>` may now read, do, check, or conclude `<difference>`.

If the truthful answer is “nothing”, test that claim against the affected passages and stop after the smallest adequate repair and check. If the answer is uncertain because several materially different repairs remain plausible, open the alternative-comparison branch.

Not this pattern when authoring a first pattern seed with no predecessor; use E.8 and the subject-owning patterns. Do not use E.15 merely to run a wording check, make a design decision, perform a quality review, publish a pattern, or land a candidate: E.10, E.9, E.19 or E.21, E.24.PUB, and the landing process own those distinct questions. Return here when one of those activities changes an existing pattern edition and edition continuity or affected use is in question.

