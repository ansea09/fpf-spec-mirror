---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard@Context"
section_id: "C.22.2:8"
section_title: "Portfolio, Archive, and Set-Return Treatment"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__009_portfolio-archive-and-set-return-treatment.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "C.22.2 — ProblemCard@Context"
  - "C.22.2:8 — Portfolio, Archive, and Set-Return Treatment"
line_start: 42912
line_end: 42936
dependencies:
  - "A.10"
  - "A.15"
  - "A.19"
  - "A.21"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.P"
  - "A.6.Q"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22"
  - "C.22.1"
  - "C.24"
  - "C.25"
  - "C.27"
  - "C.28"
  - "C.29"
  - "E.10"
  - "E.10.SEMIO"
  - "E.16"
  - "E.17"
  - "E.17.ID.CR"
  - "E.18"
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

Archive, portfolio, pool, front, shortlist, selected-set, and set-return material remain source and set cues for the current problem-side record. `ProblemCard@Context` preserves `setContextRef`, source-set kind, selection or retention basis, and the non-scalar next move when live; portfolio and archive governance stays with the named receiving patterns and does not become a local problem-card kind.

Archive, portfolio, palette, front, shortlist, ranked shortlist, selected set, live pool, and set-return material remain live source distinctions, but their current FPF receiving patterns are already available:

| Source wording | Current FPF receiving pattern | Required problem-card preservation when live |
|---|---|---|
| Problem archive | `C.18`, `C.19`, `A.10`, `G.6` | Preserve source set or reference, retention basis, candidate status, and provenance relation. |
| Problem portfolio | `G.5`, `C.19`, `G.9`, `G.11` | Preserve selection or retention basis, budget or window, review cadence, and selected-set or live-pool relation. |
| Palette | `C.18`, `C.19`, `G.5` | Preserve candidate-family or option-set reading without turning it into evidence or approval. |
| Front | `C.18`, `A.19`, `C.25`, `G.5` | Preserve declared characteristics and non-dominated set reading. |
| Shortlist | `G.5`, with `G.9` when comparison pins matter | Preserve selected-set basis and downstream use. |
| Ranked shortlist | `G.5` only when an admissible order is declared | Preserve ranking basis or narrow to selected set with tie notes. |
| Selected set | `G.5` | Preserve selected-set output, basis pins, and unknown handling. |
| Live pool | `C.19` | Preserve pool policy, current treatment, and change trigger. |
| Set-return | `G.5`, `C.18`, `A.6.Q`, declared comparison records | Preserve set-valued result when total order is not admissible. |

A singleton problem card is the degenerate case. If it came from a portfolio, front, archive, or pool, the selected problem remains traceable through `setContextRef`: the lightweight reference to the source set kind, source reference, selection or retention basis, budget or window, review cadence, and receiving pattern when live. `setContextRef` is a reference field, not a new `SetContext` kind, and is not evidence, gate passage, approval, portfolio object, or work authority.

`setContextRef` must preserve the recoverable source-set form when live: `Palette`, `Front`, `Archive`, `ExplorationArchive`, `Shortlist`, `RankedShortlist`, `SelectedSet`, `LivePool`, or another accepted source-set form. If the source-set form is not recoverable, the card may keep a source cue, but it must not claim selected-set readiness or archive-derived readiness.

When multiple plausible problem formulations remain live, `C.22.2` must not bind one `TaskSignature` prematurely. Each optional `rivalProblemFormulationRef` must state the rival formulation, described entity, context, preserved concern, lost concern, reason not selected yet, and next discrimination move. It is not a `CG-Frame`, not the E.8 `Problem Frame`, and not a representation-frame object.
The next discrimination move may be to characterize, compare, retarget, reopen the source, choose a local problem formulation, or exit to the relation-bearing pattern. Reframing is triggered when context grounding, described entity, viewpoint, scope cut, or cause-theory cue changes the problem representation enough that support or readiness cannot be inherited by wording continuity.

