---
chunk_kind: "child"
pattern_id: "E.18.NET"
pattern_title: "Network of Transformation-Flow Structures"
section_id: "E.18.NET:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.NET/E.18.NET__004_forces.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "E.18.NET — Network of Transformation-Flow Structures"
  - "E.18.NET:3 — Forces"
line_start: 119318
line_end: 119328
dependencies:
  - "A.1.STM"
  - "A.12"
  - "A.15"
  - "A.15.6"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.4"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.6.REL"
  - "C.2.1"
  - "C.29"
  - "C.30.TFS-REL"
  - "C.32.CONWAY"
  - "E.11"
  - "E.11.PUA"
  - "E.17"
  - "E.18"
  - "E.18.2"
  - "E.18.3"
  - "F.18"
keywords:
---

### E.18.NET:3 - Forces

| Force | Tension to hold |
| --- | --- |
| Local autonomy vs one engineering question | The selected structure shows how the members are coordinated. Each member retains its identity, and local state stays at the leaf TFS where it is defined. |
| Recursive reuse vs finite membership paths | A member may be a network, but membership paths must remain finite and acyclic. |
| Plain diagrams vs exact relations | A readable edge helps recognition, but only an obtaining relation of an admitted kind contributes to identity. |
| Boundary exposure vs flattening | A parent can use a nested boundary position without copying the nested member's internal structure. |
| Useful local state vs false global state | A valuation uses the connection and cut domain of its leaf TFS. A path slice belongs to a path in that TFS, and a `DesignRunTag` belongs to a position binding in it. |
| Stable selection vs evolving members | Reidentify only when an A.22 discriminator changes; records, renderings, and selection Work remain separate. |

