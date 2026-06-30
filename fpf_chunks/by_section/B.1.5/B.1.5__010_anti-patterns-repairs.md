---
chunk_kind: "child"
pattern_id: "B.1.5"
pattern_title: "Γ_method — Order‑Sensitive Method Composition & Work Enactment"
section_id: "B.1.5:9"
section_title: "Anti‑patterns & repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5/B.1.5__010_anti-patterns-repairs.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "B.1.5 — Γ_method — Order‑Sensitive Method Composition & Work Enactment"
  - "B.1.5:9 — Anti‑patterns & repairs"
line_start: 32397
line_end: 32410
dependencies:
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.3.1"
  - "B.1"
  - "B.1.1"
  - "B.1.4"
  - "B.1.6"
  - "B.3"
keywords:
  - "concurrent"
  - "method composition"
  - "plan vs run"
  - "sequential"
  - "workflow"
---

### B.1.5:9 - Anti‑patterns & repairs

| Anti‑pattern           | Symptom                                                       | Repair                                                                             |
| ---------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **Flattened set of steps** | Order lost; results become nondeterministic | Use Γ\_ctx to restore `σ`, then apply Γ\_method^plan. |
| **Cost‑in‑method** | Resources embedded in method definition | Remove costs; move to Work/Γ\_work. |
| **DesignRunTag Chimera** | Spec contains runtime measures; enactment adds planning edges | Split into `MethodDescription` (design) vs `Work` (run); rerun Γ\_method per flavour.                   |
| **DesignRunTag Chimera** | Spec contains runtime measures; enactment adds planning edges | Split into `MethodDescription` vs `Method`; rerun Γ\_method per flavour.                  |
| **Orderless Set**      | Steps modelled as unordered; reordering breaks correctness    | Provide `OrderSpec σ` and recompose with Γ\_method/Γ\_ctx.                         |
| **Silent Adapter**     | A join assumes implicit conversion                            | Add explicit typed **adapter StepSpec/Method** and re‑prove capability continuity. |
| **Inline Costs**       | Method sums time/energy                                       | Move to **Γ\_work**; link the work composition to the same order.                  |
| **Boundary Fog**       | External calls occur ad‑hoc                                   | Define/Update **MIC**; Promote/Forward/Encapsulate explicitly.                     |
| **Emergence by Join**  | Throughput leaps past WLNK with no story                      | Either (i) prove within Γ\_method (cutset/CL/order) or (ii) declare **MHT** (B.2). |

