---
chunk_kind: "child"
pattern_id: "C.37"
pattern_title: "Use-Bounded Representation Selection and Co-Use"
section_id: "C.37:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.37/C.37__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "C.37 — Use-Bounded Representation Selection and Co-Use"
  - "C.37:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 67878
line_end: 67890
dependencies:
  - "A.10"
  - "A.2.4"
  - "A.22"
  - "A.6.3.RT"
  - "C.11"
  - "C.13"
  - "C.2.1"
  - "C.2.P.DR"
  - "C.29"
  - "E.17.0"
  - "E.24.PUB"
keywords:
---

### C.37:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| Best representation overall | A candidate is ranked without a receiver, action, exact claim, or tolerated loss. | Start a one-use account and compare only claims that can change that action. |
| Evidence-use classification as warrant | A.2.4 is treated as a positive reliance or authorization result. | Add A.10 only when reliance is material and keep the direct receiving result separate. |
| Provenance as decision | A current source or authentic carrier is treated as selecting or permitting the action. | Use provenance only inside the exact bounded path; require the direct choice, gate, permission, or domain result. |
| Publication as representation authority | A published diagram is accepted because it is available and readable. | Recover the direct subject result, any exact conformance or correspondence, and the relied-on claim; E.24.PUB supplies availability only. |
| Co-use as composition | Several rows become a collection, structure, integrated view, or graph by adjacency. | Keep independent rows; open C.13, A.22, E.17.0, C.29, or a domain integration pattern only for an additional named claim. |
| Duplicate account | An owning domain result and a standalone C.37 episteme repeat the same one-use claims. | Embed once when the owner exists; otherwise use one standalone ordinary episteme. |
| Cross-use carryover | A row selected for one decision is silently reused for tailoring, learning, maintenance, or another action. | Start another account and re-evaluate direct result, loss, path, disposition, and receiving result. |
| Diagram-first ontology | A graph, table, card, or route shape decides what exists or what happened. | Recover the direct object and relation first; then state the exact representation use or `none`. |

