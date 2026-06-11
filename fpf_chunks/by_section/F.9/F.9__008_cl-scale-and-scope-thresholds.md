---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment & Bridge across Contexts"
section_id: "F.9:7"
section_title: "CL scale and scope thresholds"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__008_cl-scale-and-scope-thresholds.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "F.9 — Alignment & Bridge across Contexts"
  - "F.9:7 — CL scale and scope thresholds"
line_start: 71920
line_end: 71938
dependencies:
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.9"
  - "B.3"
  - "C.16.Q"
  - "C.25"
  - "C.26"
  - "C.26.1"
  - "E.10.D1"
  - "E.17.1"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.7"
  - "F.8"
  - "F.9.1"
  - "U.BoundedContext"
  - "U.Mechanism"
keywords:
  - "Bridge-supported use"
  - "CL"
  - "bridge"
  - "bridge reading"
  - "cross-context alignment"
  - "direction"
  - "loss notes"
  - "state export"
  - "weakest-link scope"
---

### F.9:7 - CL scale and scope thresholds

CL expresses how safely meaning carries over.

| CL    | Name              | Intuition                                            | Typical loss             | Row scope supported (thresholds) |
| ----- | ----------------- | ---------------------------------------------------- | -------------------- | -------------------------------- |
| **0** | **Opposed**       | Intentionally contrastive or disjoint                | n/a                  | none                             |
| **1** | **Comparable**    | Talk under a shared label; senses differ materially  | material sense divergence | **Naming-only** (`CL >= 1`) |
| **2** | **Translatable**  | Bounded loss; consistent examples & counter-examples | small, stated losses     | **Role Assignment & Enactment-eligibility** (`CL >= 2`) |
| **3** | **Near-identity** | Invariants match; no material counter-example        | profile-level only       | **Type-structure** (`CL = 3`) |

* **Thresholds (normative):**

  * Publishing a **Naming-only** row requires **CL >= 1** across the row's Cells.
  * Publishing a **Role Assignment & Enactment-eligible** row requires **CL >= 2**, the **same senseFamily**, and compatible stance.
  * Publishing a **Type-structure** row requires **CL = 3** **and** matched invariants (acyclicity, anti-symmetry, units, etc.).

* **Penalty use (informative):** B.3 may convert **CL** into an assurance penalty when a cross-context claim is made.

