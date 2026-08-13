---
chunk_kind: "child"
pattern_id: "E.18.NET"
pattern_title: "Network of Transformation-Flow Structures"
section_id: "E.18.NET:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.NET/E.18.NET__010_consequences.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "E.18.NET — Network of Transformation-Flow Structures"
  - "E.18.NET:9 — Consequences"
line_start: 86236
line_end: 86247
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
  - "U.Transfer"
keywords:
---

### E.18.NET:9 - Consequences

| Gain | Cost or trade-off |
| --- | --- |
| Independent flows can be coordinated without losing their identity or local change boundary. | Members and cross-flow relations must be grounded before the network can be claimed. |
| Recursive networks scale without numbered levels. | Exposed positions require finite path resolution and explicit boundary selection. |
| Cross-flow relations keep their participant meanings and n-ary signatures. | A missing relation kind or predicate remains visible instead of being hidden by a convenient generic edge. |
| Local valuations and tags remain usable without becoming global state. | A network record carries more explicit member and endpoint references than a simple graph. |
| Graphs and mantras remain useful descriptions. | Their distinct claims use E.18.2 or E.17 for descriptions and publications, A.22.CGUS or E.18.3 for demonstrations, C.30.TFS-REL for architecture use, A.15 for Work, and E.18.NET for the selected network. |

Adoption test: use E.18.NET only when the current question needs independently identified members and at least one exact relation across their boundaries. If one TFS or one parent-relative `SubflowRef` answers the question, the added network, endpoint, and member-path apparatus buys nothing and stays absent.

