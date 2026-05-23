---
chunk_kind: "child"
pattern_id: "C.3.5"
pattern_title: "KindAT — Intentional Abstraction Facet for Kinds (K0…K3)"
section_id: "C.3.5:4"
section_title: "Manager Heuristics (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.5/C.3.5__005_manager-heuristics-informative.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "C.3.5 — KindAT — Intentional Abstraction Facet for Kinds (K0…K3)"
  - "C.3.5:4 — Manager Heuristics (informative)"
line_start: 37543
line_end: 37553
dependencies:
  - "C.3.1"
keywords:
  - "K0-K3"
  - "KindAT"
  - "abstraction tier"
  - "informative facet"
  - "planning"
---

### C.3.5:4 - Manager Heuristics (informative)

| Decision area       | K0                               | K1                          | K2                                         | K3                                      |
| ------------------- | -------------------------------- | --------------------------- | ------------------------------------------ | --------------------------------------- |
| **ΔF investment**   | Prefer F5/6 executable semantics | F3→F4 acceptance predicates | F4→F7 (predicates/proofs)                  | F7→F9 (proof‑carrying, higher equality) |
| **ΔR design**       | Slice‑focused checks             | Behavioral diversity        | Variant/subkind coverage                   | Equivalence witnesses at boundaries     |
| **Bridge style**    | Instance map                     | Pattern map                 | Type map                                   | Up‑to‑iso / functorial                  |
| **Expected `CL^k`** | Low outside Context                 | Medium                      | Med/High                                   | High where iso holds                    |
| **Refactoring**     | Aggregate to K2 when stable      | Crystallize invariants → K2 | Maintain lattice; promote masks → subkinds | Keep iso constraints explicit           |


