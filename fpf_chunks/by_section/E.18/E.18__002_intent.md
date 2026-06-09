---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transduction Graph Architecture (E.TGA)"
section_id: "E.18:1"
section_title: "Intent"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__002_intent.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "E.18 — Transduction Graph Architecture (E.TGA)"
  - "E.18:1 — Intent"
line_start: 66186
line_end: 66209
dependencies:
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.7"
  - "E.10"
  - "E.17"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "CSLC normalize-then-compare"
  - "CV⇒GF (ConstraintValidity → GateFit)"
  - "DesignRunTag"
  - "MVPK faces"
  - "OperationalGate(profile)"
  - "PathSlice/Sentinel refresh"
  - "Set-return selection"
  - "SquareLaw"
  - "UNM declaration locus"
  - "edge=U.Transfer (single-edge kind)"
  - "nodes=morphisms"
  - "transduction graph"
---

### E.18:1 - Intent

Provide a notation-independent architecture for transduction graphs. The EntityOfConcern is a `TransductionGraph`: a typed, editioned directed multigraph whose nodes are morphisms, whose edges are one typed `U.Transfer` relation, and whose flows are valuations over paths or path slices inside the same graph object. Crossings appear at gates; publication faces appear through MVPK; comparable claims pin editions, reference planes, Bridge/CL notes, and refresh scope.

**Use this when.** Use E.TGA when the question under repair is whether a project description needs one graph object, path, path slice, crossing, gate, flow valuation, or refresh locus over `U.Transfer` rather than an ordered work narrative, method narrative, or wording-use cue.

**First useful move.** Name the graph object, the node kinds, the single `U.Transfer` edge kind, and the exact crossing, path, or path slice whose pins are required. For the ordinary case, this is enough: `TransductionGraph`, active `PathId` or `PathSliceId` when a path or slice is live, node kinds, one `U.Transfer`, and only the crossings or pins that are live.

**Graph ontology.** E.TGA keeps these distinctions primary:

| Construct | What it carries | Boundary |
|---|---|---|
| `TransductionGraph` | the graph object, node kinds, one `U.Transfer` edge kind, and graph-wide budgets or edition pins | not a work procedure or method sequence |
| flow valuation | a path, path slice, state, guard, comparator, or budget over the graph | not a second graph kind |
| crossing or gate | a context, plane, edition, launch, or work-boundary change | not internal step validity or gate-decision publication by itself |
| MVPK face | publication of selected graph, path, or crossing material | not the graph semantics and not evidence by itself |
| refresh locus | the smallest path slice, crossing, edition pin, or publication face affected by change | not a whole-flow rewrite unless the whole flow is the changed locus |

**Not this pattern when.** Use `A.20` for internal step validity, `A.21` for gate-decision publication, `E.20` for mechanism-governing-definition placement, the A.15 family for work planning or performed work, `E.17` for publication faces, and `E.10` for wording-use repair when the graph, path, crossing, or flow valuation is not live.

**What goes wrong if missed.** A practitioner may treat a reference flow, a wording-use cue such as `transition`, or a tool pipeline as a new graph kind or a hidden prescribed workflow, then lose comparability, crossing evidence, and slice-local refresh boundaries.

**What this buys.** E.TGA lets the practitioner keep graph structure, publication pins, crossings, CV/GF separation, and refresh locality in one current architecture without turning every domain path into its own flow doctrine.

