---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transduction Graph Architecture (E.TGA)"
section_id: "E.18:4"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__005_forces.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "E.18 — Transduction Graph Architecture (E.TGA)"
  - "E.18:4 — Forces"
line_start: 59694
line_end: 59704
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

### E.18:4 - Forces

| Force                                            | Tension                                                                                                                                                                    |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Universality vs specialization**               | One architecture needs to cover supply chains, water networks, ML functionals, and the P2W first-principles-to-work path, **without** baking in any one morphism set. |
| **Publication neutrality vs auditability**       | Keep faces notation‑neutral and non‑mechanistic ↔ require **pins**, **ComparatorSet**, **Bridge/CL**, and **PublicationScope**.                                            |
| **Set-return discipline vs business pressure for totals** | Preserve **return sets and declared partial orders** ↔ stakeholders demand single numbers.                                                                                     |
| **Cross‑Context reuse vs safety**                | Enable reuse across `U.BoundedContext` ↔ require **Bridge/CL** with **R‑only penalties**.                                                                                  |
| **Agility vs reproducibility**                   | Permit evolving CG‑Spec/UNM/Comparator editions ↔ require **edition pins** and **re‑emission** on change.                                                                  |
| **Cycles vs convergence**                        | Allow Selection↔Planning iteration ↔ impose **budget** and **slice‑scoped** refresh to prevent thrash.                                                                     |

