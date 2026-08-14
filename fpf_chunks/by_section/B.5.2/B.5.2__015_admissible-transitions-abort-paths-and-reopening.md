---
chunk_kind: "child"
pattern_id: "B.5.2"
pattern_title: "Abductive Loop"
section_id: "B.5.2:14"
section_title: "Admissible Transitions, Abort Paths, and Reopening"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2/B.5.2__015_admissible-transitions-abort-paths-and-reopening.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "B.5.2 — Abductive Loop"
  - "B.5.2:14 — Admissible Transitions, Abort Paths, and Reopening"
line_start: 40363
line_end: 40400
dependencies:
  - "A.10"
  - "A.16"
  - "A.22.CGUS"
  - "A.6.P"
  - "B.3.3"
  - "B.4.1"
  - "B.5"
  - "B.5.2.0"
keywords:
  - "abduction"
  - "candidate hypotheses"
  - "explanatory prompt"
  - "origin trace"
  - "plausibility filters"
  - "route-to-hypothesis"
---

### B.5.2:14 - Admissible Transitions, Abort Paths, and Reopening

The abductive loop is iterative, but it is not formless. Several transition cases need explicit handling so that later stages know whether they are receiving a stable `L0` conjecture, a deferred candidate, or a prompt that should be reopened rather than forced forward.

#### B.5.2:14.1 - Relation to `B.4.1` and `A.16`

`B.4.1` and `A.16` often supply the pre-abductive seam. They help preserve and stabilize upstream publications, including publication forms that carry route-shaped representations when those forms are explicitly governed, before the publication is fit for explicit conjecture. `B.5.2` begins only once the current publication is ready to function as an abductive prompt. This boundary matters because it prevents two opposite errors:

- **premature abduction**, where a low-articulation cue is treated as if it had already earned hypothesis form;
- **delayed abduction**, where a now-stable prompt is kept indefinitely in early cue form even though rival conjectures should already be compared.

#### B.5.2:14.2 - Abort, defer, and split cases

Not every abductive run should end in a prime hypothesis. Three non-selection outcomes are admissible:

1. **Abort.** The prompt dissolves because the initiating anomaly or opportunity was misread, duplicated, or already answered elsewhere.
2. **Defer.** Several candidates remain live, but the discriminating evidence or probe is not yet available. The loop pauses without pretending a winner exists.
3. **Split.** The original prompt turns out to contain several distinct questions. The run should fork into several narrower prompts rather than select one over-broad conjecture.

These outcomes are not failures. They are part of keeping abduction honest.

#### B.5.2:14.3 - Reopening and rival reinstatement

A prime hypothesis may later lose support under deduction, probe results, or new evidence. When that happens, `B.5.2` prefers explicit reopening to silent replacement.

A conforming reopening note should identify:

- which prior prime hypothesis is being reopened,
- whether a stored rival is being reinstated or a new candidate is entering,
- what change in evidence, scope, or internal contradiction triggered the reopening,
- and whether the original prompt itself has changed or only the candidate ranking has changed.

This allows the reasoning cycle to keep continuity without pretending that the earlier abductive choice had never been made.

#### B.5.2:14.4 - Scope discipline during iteration

Abductive drift often comes from silent scope expansion. A conjecture first framed for one target slice quietly becomes a universal explanation. `B.5.2` therefore expects scope discipline to remain explicit during iteration. If a candidate requires a broader or narrower scope than the prompt originally declared, that scope move should be stated rather than smuggled in under the rhetoric of a "better explanation."

