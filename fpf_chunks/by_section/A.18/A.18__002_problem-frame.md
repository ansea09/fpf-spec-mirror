---
chunk_kind: "child"
pattern_id: "A.18"
pattern_title: "Minimal CSLC in Kernel (Characteristic ⟷ Scale ⟷ Level ⟷ Coordinate) (A.CSLC‑KERNEL)"
section_id: "A.18:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.18/A.18__002_problem-frame.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "A.18 — Minimal CSLC in Kernel (Characteristic ⟷ Scale ⟷ Level ⟷ Coordinate) (A.CSLC‑KERNEL)"
  - "A.18:1 — Problem Frame"
line_start: 28297
line_end: 28308
dependencies:
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.CN"
  - "A.3.3"
  - "B.3"
  - "C.16"
  - "D.4"
  - "E.10"
  - "F.9"
  - "G.0"
  - "U.Dynamics"
keywords:
  - "CSLC"
  - "Characteristic"
  - "Coordinate"
  - "Level"
  - "Scale"
  - "lawful comparability"
  - "measurement interpretability"
  - "no illegal averaging"
  - "one-characteristic-one-scale rule"
  - "ordinal vs cardinal scale"
  - "polarity"
---

### A.18:1 - Problem Frame

We often need to **characterize some aspect** of a subject, whether the subject is one entity or a relationship between entities. Whether it’s recording a physical quantity, an architectural property, or a performance rating, the characterization must:

-   remain _domain-neutral_ (work for engineering metrics, subjective scores, etc.),

-   ensure that two measurements are **comparable if and only if** they share the same defined aspect and scale, and

-   accommodate both **ordered tiers** (qualitative levels like Low/Medium/High) and **numeric magnitudes** (continuous or interval values) without mixing them up.

In FPF’s kernel, the **CSLC pattern** (CG‑frame–Scale–Level–Coordinate) provides the minimal vocabulary and constraints to achieve this. It defines how one **Characteristic** ties to one **Scale**, and how any measured **value** can be treated as a **Coordinate** on that scale (with an optional named **Level** if the scale is discrete or tiered). The context here is the need for a _unified Standard_ so that every single measurement can be interpreted and compared on common grounds.

