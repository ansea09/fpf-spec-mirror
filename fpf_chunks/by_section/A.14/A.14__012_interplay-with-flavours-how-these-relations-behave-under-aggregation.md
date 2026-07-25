---
chunk_kind: "child"
pattern_id: "A.14"
pattern_title: "Advanced Mereology: Components, Portions, Aspects & Phases"
section_id: "A.14:9.2"
section_title: "Interplay with Γ‑flavours (how these relations behave under aggregation)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.14/A.14__012_interplay-with-flavours-how-these-relations-behave-under-aggregation.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "A.14 — Advanced Mereology: Components, Portions, Aspects & Phases"
  - "A.14:9.2 — Interplay with Γ‑flavours (how these relations behave under aggregation)"
line_start: 23653
line_end: 23662
dependencies:
  - "A.1"
  - "A.15"
  - "A.15.1"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.7"
  - "B.1"
  - "B.1.1"
  - "B.2"
  - "B.3.5"
  - "C.13"
keywords:
  - "ComponentOf"
  - "PhaseOf"
  - "PortionOf"
  - "composition"
  - "mereology"
  - "part-of"
---

### A.14:9.2 - Interplay with Γ‑flavours (how these relations behave under aggregation)

| Γ‑flavour                    | Mereological hooks (what A.14 supplies)                                                                                                                | Key effect                                                                                    |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| **Γ\_sys (B.1.2)**          | Treat **PortionOf** as Σ‑additive stocks; **ComponentOf** must respect boundary integration; **PhaseOf** is not aggregated here.                       | Conserves extensive measures and keeps structural WLNK (weakest‑link) on components.          |
| **Γ\_epist (B.1.3)**         | **PortionOf** of texts/data uses μ = token/byte count; **ConstituentOf** composes arguments/sections; **PhaseOf** versions MethodDescriptions/documents.      | Preserves provenance and avoids trust inflation by keeping constituents vs portions distinct. |
| **Γ\_ctx / Γ\_time (B.1.4)** | **PhaseOf** provides the legal slicing for time; order/dependencies live in **Γ\_ctx** and method graphs (A.15/B.1.5). **PortionOf** is orthogonal (quantities inside steps/runs).                                      | Ensures chronological consistency and monotone coverage.                                      |
| **Γ\_method (B.1.5)**          | Recipes are **MethodDescription** graphs (not parthood). When a recipe refers to stuff‑like inputs, those are **PortionOf** statements on resources.          | Separates recipe composition from structure.                                                  |
| **Γ\_work (B.1.6)**          | Only **Work** carries resource deltas; when logging “consumed 5 kg from Tank A”, model it as **PortionOf** relation to the stock prior to consumption. | Makes Σ‑balance explicit; aligns with CC‑POR‑3/4.                                             |

