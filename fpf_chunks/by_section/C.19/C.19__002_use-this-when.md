---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore-Exploit Live-Pool Governor"
section_id: "C.19:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__002_use-this-when.md"
commit_sha: "0c6ade275e9360f0c5ab9715d8f05c0dbaa13cf8"
heading_path:
  - "C.19 — Explore-Exploit Live-Pool Governor"
  - "C.19:0 — Use this when"
line_start: 58048
line_end: 58086
dependencies:
  - "A.10"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "B.3"
  - "C.11"
  - "C.11.CRC"
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.22.PFR"
  - "C.24"
  - "C.28"
  - "C.32"
  - "C.32.P2S"
  - "C.35"
  - "E.10.LRN"
  - "E.17"
  - "E.24.PUB"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "already-live candidate pool"
  - "audience availability"
  - "change trigger"
  - "explore-exploit"
  - "governing lens"
  - "keep frontier"
  - "narrow to subset"
  - "pool-policy result"
  - "publication face"
  - "publication occurrence"
  - "selector-facing declaration"
  - "sunset line"
  - "widen"
---

### C.19:0 - Use this when

- several candidate lines, family regions, or frontier segments remain live under one declared exploration and exploitation policy and the question is now policy over that pool rather than one more local choice result
- the next result should say whether to widen, keep the frontier, narrow to a subset, or sunset a line
- if the question is no longer pool policy, the C.19 use closes by naming the next subject pattern and the reason that pattern now applies
- the governing lens or policy state must be explicit rather than inferred from vague exploration language

If a proposed pool-policy premise is expressed as *learning progress*, information gain, novelty, or an articulated former cue, recover its exact result owner first. Use `E.10.LRN` only while learning wording hides that result, `A.10` only when an evidence-bearing or source-bearing claim is actually relied on, `C.17` or `C.18` only when characterization or possibility-space change is current, `C.11.CRC` only when a finite configuration-relative comparison is missing, and `C.11` for local option or probe choice. Stop before C.19 unless the remaining question is policy over a still-live pool.

#### C.19:0.1 - What goes wrong if missed

- scalarized top-1 picks are mislabeled as "the frontier", so it becomes unclear whether the result names one lens-ranked winner or the admissible live set
- exploration continues without one named pool, one named governing lens, or one explicit next treatment
- local option choice, pool policy, enactment planning, selector-result declaration, and publication availability collapse into one blurred result

#### C.19:0.2 - What this buys

- one explicit pool-governance result for exploration, graduation, narrowing, and sunset treatment
- one explicit link from lens or policy state to the next pool-side treatment
- one repeatable way to preserve heterogeneity and frontier discipline without forcing inadmissible totalization

#### C.19:0.3 - First-minute questions

- Which still-live pool, frontier segment, or family region is actually under governance now?
- Which lens or policy state is governing it?
- Is the next admissible pool treatment to widen, keep the frontier, narrow to a subset, or sunset a line?
- If none of those treatments is current, which subject pattern now applies, and why is the question no longer pool policy?
- What justifies active exploration or cheaper retention now, and what change would end that justification? Readiness for exploitation is a separate question.

#### C.19:0.4 - First output

For loop-engineering practice, use this first output only when the live question is pool policy over still-live candidates such as loops, harnesses, workflows, method families, or framework seeds. A `C.19` record may say that the pool should widen, keep its frontier, narrow to an internal subset, or sunset a line under a declared lens. If the question leaves pool policy, finish this record and use the handoff in `C.19:4.4`.

The first useful output is one explicit pool-policy record that names the live pool, `governingLens`, one `currentTreatment` token from the closed set `widen | keep_frontier | narrow_to_subset | sunset_line`, and the exact event that would justify changing that treatment next. If another question has become current, set `nextQuestionPatternLocator` from `C.19:4.4` instead of inventing another `currentTreatment`.

The word `result` in `PoolPolicyResult` means the stated conclusion of this pool-policy pass; it does not mint a universal result kind. The record and its inputs create neither an actual Problem nor a `ProblematicForRelation`, improvement-result or work-result identity, project Work or work parthood, `ChoiceResult`, public shortlist, work permission, nor refreshed edition. When a durable claim episteme about the pool treatment is needed, constitute that episteme separately under `C.2.1` and keep its exact EntityOfConcern and claim content explicit.

That record states pool treatment only. Use `C.19:4.4` for the next result rather than adding its fields or claims to `PoolPolicyResult`. If the output still cannot name the pool, governing lens, current treatment, and change trigger honestly, the current `C.19` pass is unfinished.

