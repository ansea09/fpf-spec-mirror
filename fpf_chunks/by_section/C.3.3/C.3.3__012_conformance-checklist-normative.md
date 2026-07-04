---
chunk_kind: "child"
pattern_id: "C.3.3"
pattern_title: "KindBridge & CL^k — Cross‑context Mapping of Kinds"
section_id: "C.3.3:11"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.3/C.3.3__012_conformance-checklist-normative.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "C.3.3 — KindBridge & CL^k — Cross‑context Mapping of Kinds"
  - "C.3.3:11 — Conformance Checklist (normative)"
line_start: 41249
line_end: 41272
dependencies:
  - "A.2.6"
  - "C.2.2"
  - "C.3.1"
  - "C.3.2"
keywords:
  - "CL^k"
  - "KindBridge"
  - "R penalty"
  - "cross-context mapping"
  - "type-congruence"
---

### C.3.3:11 - Conformance Checklist (normative)

| ID        | Requirement                                                                                                                                          |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **KB‑01** | A KindBridge **maps** `KindSignature`(s) and an explicitly declared subset of `⊑` links.                                                             |
| **KB‑02** | A KindBridge **MUST NOT** map Scope; Scope uses USM Bridge (Part B).                                                                                 |
| **KB‑03** | Bridge records **SHALL** include Contexts/versions, kind mapping/rules, order‑preservation claims, **`CL^k`**, **loss notes**, and **definedness area**. |
| **KB‑04** | Mapping **MUST** be **deterministic** given fixed versions/rules (no “latest”).                                                                      |
| **KB‑05** | Preserved order links **MUST** stay **monotone**: `k₁ ⊑ k₂` ⇒ `translateₖ(k₁) ⊑′ translateₖ(k₂)`.                                                    |
| **KB‑06** | **No inversions**: preserved links cannot invert order; otherwise mark **not preserved** and add loss notes.                                         |
| **KB‑07** | **Collapses** are allowed but **MUST** list merged subkinds and lost properties.                                                                     |
| **KB‑08** | **`CL^k`** **SHALL** reuse CL anchors and be labeled **“kind‑congruence.”**                                                                           |
| **KB‑09** | **Penalties:** when classification uses KindBridge, apply **Ψ(`CL^k`)** to **R**; **MUST NOT** adjust **F/G**.                                        |
| **KB‑10** | **Chaining:** effective `CL^k` across a chain is **min** (weakest‑link).                                                                              |
| **KB‑11** | **Loss notes** **SHALL** enumerate non‑preserved invariants and collapsed subkinds.                                                                  |
| **KB‑12** | **Definedness:** bridge **SHALL** state its valid area; guards **fail closed** outside it.                                                           |

**Integration requirements with Part B (bridges):**

* **B‑P1.** Part B (Bridges) **SHALL** list **KindBridge** as a distinct bridge class alongside USM Scope bridges.
* **B‑P2.** Part B **SHALL** state that **`CL^k` penalties route to R** via a monotone **Ψ**, never to **F/G**.
* **B‑P3.** Part B **SHALL** define **chaining = min** for both **CL** and **`CL^k`** (weakest‑link).
* **Templates.** ESG/Method templates should expose fields for **Scope Bridge (CL)** and **KindBridge (`CL^k`)** with loss notes & definedness.

