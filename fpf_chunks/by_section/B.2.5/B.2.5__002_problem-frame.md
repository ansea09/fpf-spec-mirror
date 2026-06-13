---
chunk_kind: "child"
pattern_id: "B.2.5"
pattern_title: "Supervisor-Subholon Feedback Loop"
section_id: "B.2.5:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.5/B.2.5__002_problem-frame.md"
commit_sha: "cb17c555f343780e31e5fea236a74adc69295736"
heading_path:
  - "B.2.5 — Supervisor-Subholon Feedback Loop"
  - "B.2.5:1 — Problem frame"
line_start: 32041
line_end: 32053
dependencies:
  - "A.1"
  - "A.12"
  - "A.15"
  - "A.2"
  - "A.3"
  - "A.7"
  - "B.2"
  - "C.30.LCA"
keywords:
  - "control architecture"
  - "feedback loop"
  - "layered control"
  - "stability"
  - "supervisor"
---

### B.2.5:1 - Problem frame

Use this pattern when a holon is described as being supervised, regulated, steered, corrected, constrained, or coordinated through a feedback loop between a supervisor role and one or more subordinate holons.

The first-minute working situation is familiar: a fleet controller supervises drones, a plant supervisor changes allowed operating modes, a policy role constrains teams, or a scientific community reviews and revises a theory. The useful first move is to recover the feedback-loop relation: who or what is the supervised holon, which `Transformer` or transformer-bearing system plays the supervisor role, what signal or publication channel carries state or observations, what influence or constraint returns, and what objective or constraint the loop is trying to maintain.

What goes wrong if B.2.5 is missed: the supervised holon, supervisor transformer, shared medium, returned influence, and loop-closure condition remain unnamed; then layer labels, diagrams, publication channels, or supervisor words start carrying claims that belong elsewhere.

What B.2.5 buys in practice: the practitioner can keep useful supervisor/subholon language while naming the acting role, medium, returned influence, and governing pattern for any stronger claim being made.
Not this pattern when the issue under repair is only a control-structure view, reusable dynamics law, rate/timing claim, causal intervention claim, evidence or assurance claim, gate decision, or module-interface relation. Use `C.30.LCA`, `A.3.3`, `C.27`, `C.28`, `A.10`/`G.6`, `B.3`, `A.20`/`A.21`, or `A.6.M` as appropriate.

The primary EntityOfConcern is one supervisor-subholon feedback-loop relation. Stability, safety, evidence sufficiency, gate readiness, causal validity, or assurance claims remain neighboring claims under their governing patterns when those claims are being made.

