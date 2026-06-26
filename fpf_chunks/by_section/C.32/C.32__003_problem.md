---
chunk_kind: "child"
pattern_id: "C.32"
pattern_title: "Architecture Candidate Synthesis"
section_id: "C.32:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32/C.32__003_problem.md"
commit_sha: "f1d0f9319cf1f93129b7691a328a281022252c4e"
heading_path:
  - "C.32 — Architecture Candidate Synthesis"
  - "C.32:2 — Problem"
line_start: 58686
line_end: 58699
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.22"
  - "A.3.4"
  - "A.6.F"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.HCS"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.18"
  - "E.22"
  - "E.23"
  - "G.5"
keywords:
  - "CandidateArchitecturePalette@Project"
  - "architecture candidate synthesis"
  - "architecture characteristics"
  - "candidate configurations"
  - "retained alternatives"
  - "selected structures"
  - "synthesis structure map"
  - "trade-off front"
---

### C.32:2 - Problem

Architecture synthesis is the constructive middle of architecture work. A practitioner may already know the described holon, bounded context, some selected structures, and some concerns, but still need to configure those structures together before later comparison or decision can be honest.

The typical synthesis problem is multi-structure. Required functions or effects must be borne by candidate modules, roles, work methods, control relations, transformation-flow structures, placement structures, information structures, or evidence structures. A control relation can improve supervision while increasing timing or accountability burden; an information structure can improve maintenance access when exposed through a digital-twin view while still hiding source-return loss; a team structure can improve flow while failing to match module or deployment structure.

A functional architecture is not enough by itself. A function graph, use case decomposition, workflow, neural cell graph, method step, or cultural practice function can enter architecture synthesis only after a possible bearer is named. If no admitted module, role, method, resource, placement, control relation, or evidence structure can carry the required function under current constraints, the candidate must be repaired before it enters comparison, selection, local choice, or decision work.

The typical synthesis problem is also multi-characteristic. Architecture characteristics such as cohesion, coupling, substitutability, evidence reuse, work repeatability, latency, locality, control separation, source-return cost, and composite quality families often compete. Functional demands describe what the holon is to do; architecture characteristics describe whether the selected structures make those demands maintainable, controllable, evolvable, replaceable, inspectable, and otherwise acceptable in the current context.

One recurring candidate-generation heuristic is idealization: ask whether an existing selected structure or resource can carry an additional required function, whether a support bearer can disappear, or whether a more general scale-amenable bearer can replace several special bearers. Admit that heuristic only as a candidate. The candidate must name the functions transferred to a bearer, the bearer removed or generalized, the architecture characteristics improved and worsened, and any BLP scale window or waiver when scale advantage is claimed.

C.32 makes the constructive translation explicit. It creates a small palette whose candidates answer: which selected structures are configured together, which architecture characteristics improve or worsen, which constraints remain admissible, what source detail must remain recoverable, and which receiving pattern governs the next use.

