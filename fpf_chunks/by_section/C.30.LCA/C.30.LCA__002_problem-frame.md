---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__002_problem-frame.md"
commit_sha: "e3fedf42dc7cb5d12905913b5a0b0e951ed7d254"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:1 — Problem frame"
line_start: 53337
line_end: 53361
dependencies:
  - "A.10"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.3.3"
  - "B.2.5"
  - "B.3"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.LCA"
  - "C.30.STRAT"
  - "C.30.TGA-FLOW-REL"
  - "E.18"
  - "G.6"
keywords:
  - "control layer"
  - "control-structure view"
  - "controller/plant"
  - "layered control architecture"
  - "proof overread"
  - "rate band"
  - "supervisor loop"
---

### C.30.LCA:1 - Problem frame

Use this pattern when a selected control structure or control-structure relation changes the next architecture move: a controller regulates a plant, an observer or estimator changes what can be known, a planner provides references to lower-rate control, a supervisor constrains a subsystem, a policy loop changes allowed behavior, or an LCA cue makes roles, rates, observation boundaries, actuation boundaries, feedback, or externalities architecture-relevant.

The first-minute working situation is ordinary engineering talk: a diagram says the supervisor watches a subsystem, a controller regulates a plant, an observer estimates state, a planner gives references to a lower-rate controller, or a policy relation or control relation changes allowed controller behavior. The useful first move is to recover a `ControlStructureView@Context`: which architecture claim is being described, which control roles and relations are present, which rate bands or recovered control-layer relations are live, which feedback or externality boundaries are named, and which neighboring pattern carries any additional live claim. If the source only says `layer`, `level`, `tier`, or `stack` without a control-specific relation, use `C.30.STRAT` first.

What goes wrong if C.30.LCA is missed: a control diagram becomes proof; stratification labels bypass `C.30.STRAT` and start carrying undeclared scope; and `B.2.5`, Transduction Graph Architecture (TGA), or Layered Control Architecture (LCA) prose is overread as control adequacy.

What C.30.LCA buys in practice: the practitioner can keep useful controller, plant, observer, regulator, supervisor, feedback, rate, and control-layer language while recovering the control-structure view and the exact governing pattern that carries any proof or exact claim.

Not this pattern when the live issue is generic stratification or source-label repair, only a TGA path slice, function description, module boundary, measurement head, causal intervention, or safety case. Use `C.30.STRAT`, `C.30.TGA-FLOW-REL`, `A.6.F`, `A.6.M`, `C.16`, `C.28`, or the exact assurance or evidence pattern as appropriate.

The primary `EntityOfConcern` for this pattern use is the selected control structure or control-structure relation set under an `ArchitectureOf@Context`. The `ControlStructureView@Context` is a describing episteme for that selected structure; proof, safety, evidence, gate, and architecture-as-whole claims remain neighboring claim refs under their exact patterns. Ordinary use may stop with a typed control-structure view note:

```text
ControlStructureViewNote ordinary minimum:
  architecture claim or described holon plus context:
  one control relation:
  loop state: closed | one-way | unclear:
  control-layer or rate label recovered?: yes | no | C.30.STRAT needed:
  proof, evidence, causal, gate, or assurance governing pattern if live:
  stop condition:
```

The full `ControlStructureView@Context` opens when the live control claim needs declared roles, relations, rates, recovered control-layer labels, boundary refs, or explicit exact governing pattern applications beyond that note.
