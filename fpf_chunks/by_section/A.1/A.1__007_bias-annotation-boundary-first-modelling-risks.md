---
chunk_kind: "child"
pattern_id: "A.1"
pattern_title: "Holonic Foundation: Entity → Holon"
section_id: "A.1:6"
section_title: "Bias-Annotation — Boundary-first modelling risks"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1/A.1__007_bias-annotation-boundary-first-modelling-risks.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "A.1 — Holonic Foundation: Entity → Holon"
  - "A.1:6 — Bias-Annotation — Boundary-first modelling risks"
line_start: 1411
line_end: 1422
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.14"
  - "A.2"
  - "B.1"
  - "U.Boundary"
  - "U.Episteme"
  - "U.Holon"
  - "U.System"
keywords:
  - "U.Episteme"
  - "U.System"
  - "entity"
  - "holon"
  - "part-whole composition"
  - "system boundary"
---

### A.1:6 - Bias-Annotation — Boundary-first modelling risks

This kernel distinction is intentionally **boundary‑first**: it treats “where the boundary is” as a modelling decision that shapes everything downstream. That framing is powerful, but it can also smuggle bias if boundary choices are made implicitly or for political convenience.

| Lens | Typical bias risk | Mitigation in this pattern |
|---|---|---|
| **Gov** | Boundary decisions become “org charts”, not defensible model choices. | Record boundary rationale in the working model and require the **Inside/Outside test** (A.1:4.4) for contested cases. |
| **Arch** | Over‑modularisation: every interaction becomes a “system” with hard edges. | Prefer **permeable boundaries** when the phenomenon is gradient‑like; keep the `U.Entity`/`U.Holon` split minimal and push dynamics into Roles (A.2) and Work (A.15). |
| **Onto/Epist** | Category error: treating epistemes as physical actors (or vice versa). | Keep `U.Episteme` passive; model transformations as actions of a `U.System` in role, acting via explicit carriers (see A.10). |
| **Prag** | “Holon” becomes jargon that slows teams down. | Use `U.System` / `U.Episteme` in day‑to‑day models; reserve “holon” for kernel‑level discourse (see naming guidance in A.1:4.5 and CC‑A1.8). |
| **Didactic** | Readers infer semantics from overloaded labels or inconsistent headings. | Keep canonical titles and the `U.*` prefixes explicit; avoid informal deontic language in normative clauses (E.8). |

