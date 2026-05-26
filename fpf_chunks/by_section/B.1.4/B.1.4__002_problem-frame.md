---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Contextual & Temporal Aggregation (Γ\\_ctx & Γ\\_time)"
section_id: "B.1.4:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__002_problem-frame.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "B.1.4 — Contextual & Temporal Aggregation (Γ\\_ctx & Γ\\_time)"
  - "B.1.4:1 — Problem frame"
line_start: 29544
line_end: 29554
dependencies:
  - "A.12"
  - "A.14"
  - "A.15"
  - "B.1"
  - "B.1.1"
keywords:
  - "composition"
  - "order-sensitive"
  - "temporal aggregation"
  - "time-series"
---

### B.1.4:1 - Problem frame

The universal algebra **Γ** (B.1) assumes local commutativity and locality for most structures. But many real‑world compositions are **not** order‑indifferent (recipes, proofs that unfold by steps, manufacturing routes), and many composites are **nothing but** a history (asset history, model revisions, experiment runs). For these cases FPF offers two universal flavours:


* **Γ\_ctx** — **procedural composition** (where SerialStepOf / ParallelFactorOf edges are present; see B.1.5 Γ_method for typing and joins; A.14 governs only mereological edges such as PortionOf/PhaseOf).
**Γ\_time** — *temporal* aggregation for **phase composition of the same carrier** (where `PhaseOf` edges from **A.14** are present).

Both flavours **inherit WLNK and MONO** from the Quintet (B.1) and remain compatible with **A.12** (Transformer Principle) and **A.15** (Strict Distinction): they do *order* and *time*, not structure, mapping, or cost.


