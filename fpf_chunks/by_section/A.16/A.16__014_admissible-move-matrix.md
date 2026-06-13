---
chunk_kind: "child"
pattern_id: "A.16"
pattern_title: "Language-State Transduction Coordination"
section_id: "A.16:13"
section_title: "Admissible Move Matrix"
source_path: "FPF-Spec.md"
output_path: "by_section/A.16/A.16__014_admissible-move-matrix.md"
commit_sha: "cb17c555f343780e31e5fea236a74adc69295736"
heading_path:
  - "A.16 — Language-State Transduction Coordination"
  - "A.16:13 — Admissible Move Matrix"
line_start: 22166
line_end: 22184
dependencies:
  - "A.16.0"
  - "A.16.0-A.16.2"
  - "A.16.1"
  - "A.16.2"
  - "A.18"
  - "A.19"
  - "A.6.A"
  - "A.6.P"
  - "B.4.1"
  - "B.5.2.0"
  - "C.16.Q"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "E.18"
keywords:
  - "admissible moves"
  - "handoff"
  - "language-state"
  - "reopen"
  - "respecify"
  - "retire"
  - "sketch-backoff"
  - "transduction"
---

### A.16:13 - Admissible Move Matrix

#### A.16:13.1 - Typical publication consequences
| Move | Typical source publication state | Typical resulting publication state or form | What must become explicit |
|---|---|---|---|
| `notice` | observation trace, low-articulation cue, provisional note | preservation-worthiness of the cue becomes explicit | why the cue counts as worth preserving |
| `stabilize` | low-articulation preserved cue | `U.PreArticulationCuePack` or equivalent early preservation form becomes admissible | cue nucleus, anchors, witnesses, and preservation rationale |
| `route` | cue pack or stabilized note | `RoutedCueSet` or equivalent route-bearing publication becomes admissible | route plurality, selected route if any, route rationale, route authority state |
| `projection` | routed cue or selected route | a typed route-bounded publication form rendered on an existing MVPK face | what is foregrounded, what is omitted, and how reopen remains admissible |
| `formalize` | explicit but not yet formal-enough publication | a named `U.EpistemePublication` form with higher articulation or closure governed by a later formal pattern becomes admissible | new symbolic or slot structure and governing-pattern entry |
| `operationalize` | method-facing, work-facing, or gate-facing publication | a method-facing, work-facing, or gate-facing `U.EpistemePublication` form governed by a later method, work, or gate pattern becomes admissible | hook governing pattern, guard, authority basis, and work crossing if any |
| `reopen` | route-bearing or endpoint-bound publication | same family with reduced closure | which rivals reopen and what authority falls |
| `sketchBackoff` | over-rigid form | exploratory cue-bearing form such as `U.PreArticulationCuePack` or `RoutedCueSet` | withdrawn authority and retained witnesses |
| `respecify` | plausible family under wrong framing scaffold | same family with revised framing scaffold or route specification | replaced framing commitments and invariants that stay fixed |
| `retire` | cue pack, route-bearing publication, or branch | retired / withdrawn state with successor or no-successor note | why continuation stopped and what now carries authority |

#### A.16:13.2 - Invariance reminder
An admissible move may change articulation, closure, representation, route, authority, or publication form, but it shall not silently rewrite governing pattern boundaries. A move is not permission to retype a cue into any convenient governing pattern.

