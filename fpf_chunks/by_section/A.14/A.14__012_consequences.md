---
chunk_kind: "child"
pattern_id: "A.14"
pattern_title: "Advanced Mereology: Components, Portions, Aspects & Phases"
section_id: "A.14:11"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.14/A.14__012_consequences.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.14 — Advanced Mereology: Components, Portions, Aspects & Phases"
  - "A.14:11 — Consequences"
line_start: 19439
line_end: 19453
dependencies:
  - "A.1"
  - "B.1.1"
keywords:
  - "ComponentOf"
  - "PhaseOf"
  - "PortionOf"
  - "composition"
  - "mereology"
  - "part-of"
---

### A.14:11 - Consequences

**Benefits**

* **Predictable composition.** Σ‑additivity for portions and identity‑through‑time for phases make Γ‑proofs straightforward.
* **History without confusion.** Temporal slicing is explicit and audit‑ready; no paradoxical overlaps.
* **Cleaner integration with roles and recipes.** The firewall prevents “functional object” creep into structure.
* **Compatibility with engineering practice.** Mirrors *product breakdown* (components) vs *functional breakdown* (roles) vs *material stocks* (portions) vs *versioning* (phases).

**Trade‑offs / mitigations**

* **Modelling energy.** Authors must pick μ and declare units; provide a short μ‑catalog per project.
* **More relation names.** Two extra sub‑relations increase vocabulary; mitigated by the decision table (§ 6) and spot‑tests (§ 9).
* **Escalation discipline.** Deciding PhaseOf vs MHT requires judgement; A.14 provides criteria, and B.2 captures true re‑identification.

