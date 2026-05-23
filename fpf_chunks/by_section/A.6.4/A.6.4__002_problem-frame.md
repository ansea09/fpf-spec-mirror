---
chunk_kind: "child"
pattern_id: "A.6.4"
pattern_title: "U.EpistemicRetargeting — describedEntity‑retargeting morphism"
section_id: "A.6.4:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.4/A.6.4__002_problem-frame.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.6.4 — U.EpistemicRetargeting — describedEntity‑retargeting morphism"
  - "A.6.4:1 — Problem frame"
line_start: 11511
line_end: 11534
dependencies:
  - "A.1"
  - "A.6.2"
  - "C.2"
  - "C.2.1"
  - "E.18"
  - "E.TGA"
  - "F.9"
  - "U.EpistemeSlotGraph"
  - "U.EpistemicRetargeting"
keywords:
  - "KindBridge"
  - "SquareLaw-retargeting"
  - "StructuralReinterpretation"
  - "describedEntity shift"
  - "retargeting"
  - "subject retargeting"
---

### A.6.4:1 - Problem frame

Many important operations on descriptions **change the described entity** while preserving a structural or behavioural invariant:

* **Physical vs functional reinterpretation.**
  An episteme about a physical module (cabinet, rack, device) is re‑interpreted as an episteme about a function‑holon it realises. This is precisely what StructuralReinterpretation nodes in E.TGA attempt to do.

* **Signal vs spectrum.**
  A time‑domain signal description is re‑targeted to a description of its frequency‑domain spectrum. The underlying invariant (typically energy or inner‑product) is preserved, but the described entity changes from `time→value` trajectories to `frequency→amplitude/phase` distributions.

* **Data vs model.**
  An episteme about raw observations (dataset) is turned into an episteme about a learned or estimated model, keeping an invariant such as likelihood, sufficient statistics, or predictive performance.

All of these are **Ep→Ep transforms** that:
* do **not** change the Intension (`I`) directly (they operate on descriptions/specifications),
* do **not** merely slice or re‑express an episteme of the same entity (that would be EpistemicViewing, A.6.3),
* but **do change** the **DescribedEntity‑bundle** (`DescribedEntitySlot` and usually `GroundingHolonSlot`) under a formal bridge between kinds.

We need a single, reusable notion of **“epistemic retargeting”** that captures these operations as:
* **effect‑free** at the level of Work/Mechanism (EFEM discipline),
* **describedEntity-retargeting** in a controlled way,
* **invariant‑conservative** (no violation of the declared invariant between kinds),
* and **functorial** (retargetings compose cleanly and align with Bridges).

