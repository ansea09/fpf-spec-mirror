---
chunk_kind: "child"
pattern_id: "B.2.2"
pattern_title: "Meta-System Transition (MST)"
section_id: "B.2.2:7"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.2/B.2.2__008_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "B.2.2 — Meta-System Transition (MST)"
  - "B.2.2:7 — Common Anti-Patterns and How to Avoid Them"
line_start: 30040
line_end: 30047
dependencies:
  - "A.1"
  - "B.2"
  - "B.2.1"
keywords:
  - "physical emergence"
  - "super-system"
  - "system emergence"
---

### B.2.2:7 - **Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Manager's View: What It Looks Like | How FPF Prevents It (Conceptually) |
| :--- | :--- | :--- |
| **The "Big Bag of Parts"** | A collection of systems is given a collective name (e.g., "The Platform"), but there is no unified interface, no shared objective, and no active coordination. | **CC-B2.2.1** requires evidence for all four B-O-S-C triggers. A simple collection without boundary closure or a supervisory loop does not qualify for MST. It remains an aggregate, not a meta-system. |
| **The "Emergence by Fiat"** | A manager declares that a new, synergistic capability has emerged, but there is no underlying mechanism to sustain it. The "improvement" is a temporary artifact of heroic effort, not a stable property of the system. | **CC-B2.2.3** mandates the existence of an identifiable supervisor. If there is no feedback loop to maintain the new behavior, no MST has occurred. |
| **The "Hidden God-Controller"** | A system appears to be a self-organizing swarm, but its behavior is actually dictated by a hidden, external, centralized controller that is not part of the model. | The FPF's **Transformer Principle (A.12)** and **Boundary rules (A.1)** require that all external influences are made explicit. The controller must either be modeled as part of the meta-system (and thus inside its new boundary) or as an external `Transformer`. |

