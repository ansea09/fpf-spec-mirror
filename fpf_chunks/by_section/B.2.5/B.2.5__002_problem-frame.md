---
chunk_kind: "child"
pattern_id: "B.2.5"
pattern_title: "Supervisor-Subholon Feedback Loop"
section_id: "B.2.5:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.5/B.2.5__002_problem-frame.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "B.2.5 — Supervisor-Subholon Feedback Loop"
  - "B.2.5:1 — Problem frame"
line_start: 31169
line_end: 31181
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

What goes wrong if B.2.5 is missed: a drawn loop, layer label, publication channel, or supervisor word is read as proof of stability, safety, causality, evidence sufficiency, gate validity, or assurance.

What B.2.5 buys in practice: the practitioner can keep useful supervisor/subholon language while naming the acting role, medium, returned influence, and exact governing pattern that carries any proof or exact claim.
Not this pattern when the live issue is only a control-structure view, a reusable dynamics law, a rate/timing claim, a causal intervention claim, an evidence claim, an assurance claim, a gate decision, or a module-interface relation. Use `C.30.LCA` for control-structure view adequacy, `A.3.3` for dynamics, `C.27` for temporal/rate adequacy, `C.28` for causal-use claims, `A.10`/`G.6` for evidence claim, `B.3` for assurance, `A.20`/`A.21` for constraint validity or gate decisions, and module/interface patterns for interface commitments.

The governed object is one supervisor-subholon feedback-loop relation. It is not proof that the loop is stable, safe, evidence-sufficient, gate-ready, causally valid, or assured.

