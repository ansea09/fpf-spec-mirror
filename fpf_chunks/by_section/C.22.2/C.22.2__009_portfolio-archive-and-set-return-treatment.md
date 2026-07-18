---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard@Context"
section_id: "C.22.2:8"
section_title: "Portfolio, Archive, and Set-Return Treatment"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__009_portfolio-archive-and-set-return-treatment.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "C.22.2 — ProblemCard@Context"
  - "C.22.2:8 — Portfolio, Archive, and Set-Return Treatment"
line_start: 48659
line_end: 48683
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.5"
  - "A.19"
  - "A.21"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.Q"
  - "C.18"
  - "C.19"
  - "C.2.P"
  - "C.22"
  - "C.22.1"
  - "C.24"
  - "C.25"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.32.P2S"
  - "E.10"
  - "E.10.MOVE"
  - "E.16"
  - "E.17"
  - "E.17.ID.CR"
  - "E.18"
  - "E.18.1"
  - "E.2"
  - "E.9"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
  - "P2W-ready"
  - "Thin problem card"
  - "first-principles cue"
  - "freshness and unknown disposition"
  - "problem card"
  - "problem signal"
  - "problem-side record"
  - "safe-probe-needed"
  - "setContextRef"
  - "support posture"
  - "validation boundary"
---

### C.22.2:8 - Portfolio, Archive, and Set-Return Treatment

Archive, portfolio, pool, front, shortlist, selected-set, and set-return material remain source and set cues for the current problem-side record. `ProblemCard@Context` preserves `setContextRef`, source-set kind, selection or retention criterion, and the non-scalar next use when current; portfolio and archive governance stays with the named governing patterns and does not become a local problem-card kind.

Archive, portfolio, palette, front, shortlist, ranked shortlist, selected set, `LivePool`, and set-return material remain current source distinctions, but their current FPF governing patterns are already available:

| Source wording | Current FPF pattern or relation | Required problem-card preservation when the corresponding claim is being made |
|---|---|---|
| Problem archive | `C.18`, `C.19`, `A.10`, `G.6` | Preserve source set or reference, retention criterion, candidate status, and provenance relation. |
| Problem portfolio | `G.5`, `C.19`, `G.9`, `G.11` | Preserve selection or retention criterion, budget or window, review cadence, and selected-set or `LivePool` relation. |
| Palette | `C.18`, `C.19`, `G.5` | Preserve candidate-family or option-set interpretation without turning it into evidence or approval. |
| Front | `C.18`, `A.19`, `C.25`, `G.5` | Preserve declared characteristics and non-dominated set interpretation. |
| Shortlist | `G.5`, with `G.9` when comparison pins matter | Preserve selected-set criterion and downstream use. |
| Ranked shortlist | `G.5` only when a declared order is declared | Preserve ranking criterion or narrow to selected set with tie notes. |
| Selected set | `G.5` | Preserve selected-set output, selection pins, and unknown handling. |
| `LivePool` | `C.19` | Preserve pool policy, current treatment, and change trigger. |
| Set-return | `G.5`, `C.18`, `C.16.Q`, declared comparison records | Preserve set-valued result when no total order is declared. |

A singleton problem card is the degenerate case. If it came from a portfolio, front, archive, or pool, the selected problem remains traceable through `setContextRef`: the lightweight reference to the source set kind, source reference, selection or retention criterion, budget or window, review cadence, and pattern reference named by value when current. `setContextRef` is a reference field, not a new `SetContext` kind and not a downstream claim carrier.

`setContextRef` preserves the recoverable set-source relation when current: `Palette`, `Front`, `Archive`, `ExplorationArchive`, `Shortlist`, `RankedShortlist`, `SelectedSet`, `LivePool`, or another accepted source-set form. If the set-source relation is not recoverable, the card may keep a set-finding cue, but it does not claim selected-set readiness or archive-derived readiness.

When multiple plausible problem formulations remain current, `C.22.2` does not bind one `TaskSignature` prematurely. Each optional `rivalProblemFormulationRef` states the rival formulation, EntityOfConcern, context, preserved concern, lost concern, reason not selected yet, and next discrimination action. It is not a `CG-Frame`, not the E.8 `Problem Frame`, and not a representation-frame kind.
The next discrimination action may be to characterize, compare, retarget, reopen the source material or source relation, choose a local problem formulation, or apply the relation-bearing pattern. Reframing is triggered when context grounding, EntityOfConcern, viewpoint, scope cut, or cause-theory cue changes the problem representation enough that readiness or use-boundary cannot be inherited by wording continuity.

