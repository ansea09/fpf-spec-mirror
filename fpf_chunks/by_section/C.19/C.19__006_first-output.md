---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore-Exploit Live-Pool Governor"
section_id: "C.19:0.4"
section_title: "First output"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__006_first-output.md"
commit_sha: "7f7c592f4d633e54cdb202d622d6e0e05df41517"
heading_path:
  - "C.19 — Explore-Exploit Live-Pool Governor"
  - "C.19:0.4 — First output"
line_start: 48214
line_end: 48223
dependencies:
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "B.3"
  - "C.11"
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

### C.19:0.4 - First output

For loop-engineering practice, use this first output only when the live question is pool policy over still-live candidates such as loops, harnesses, workflows, method families, or framework seeds. A `C.19` record may say that the pool should widen, keep its frontier, narrow to an internal subset, or sunset a line under a declared lens. If the question leaves pool policy, finish this record and use the handoff in `C.19:4.4`.

The first useful output is one explicit pool-policy record that names the live pool, `governingLens`, one `currentTreatment` token from the closed set `widen | keep_frontier | narrow_to_subset | sunset_line`, and the exact event that would justify changing that treatment next. If another question has become current, set `nextQuestionPatternLocator` from `C.19:4.4` instead of inventing another `currentTreatment`.

The word `result` in `PoolPolicyResult` means the stated conclusion of this pool-policy pass; it does not mint a universal result kind. The record and its inputs create neither an actual Problem nor a `ProblematicForRelation`, improvement-result or work-result identity, project Work or work parthood, `ChoiceResult`, public shortlist, work permission, nor refreshed edition. When a durable claim episteme about the pool treatment is needed, constitute that episteme separately under `C.2.1` and keep its exact EntityOfConcern and claim content explicit.

That record states pool treatment only. Use `C.19:4.4` for the next result rather than adding its fields or claims to `PoolPolicyResult`. If the output still cannot name the pool, governing lens, current treatment, and change trigger honestly, the current `C.19` pass is unfinished.

