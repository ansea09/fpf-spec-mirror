---
chunk_kind: "child"
pattern_id: "A.6.RCD"
pattern_title: "Needed Relation Claim Derivation and Relation-Kind Admission"
section_id: "A.6.RCD:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.RCD/A.6.RCD__005_forces.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "A.6.RCD — Needed Relation Claim Derivation and Relation-Kind Admission"
  - "A.6.RCD:3 — Forces"
line_start: 16980
line_end: 16991
dependencies:
  - "A.11"
  - "A.6.0"
  - "A.6.5"
  - "A.6.P"
  - "A.6.REL"
  - "B.3"
  - "C.2.1"
  - "C.29"
  - "E.24"
  - "E.24.UK"
  - "F.17"
  - "F.18"
  - "F.9"
  - "G.11"
  - "U.Signature"
keywords:
---

### A.6.RCD:3 - Forces

| Force | Tension to resolve |
| --- | --- |
| Exact semantics vs readable use | Authors MUST make each conforming derivation replayable without making every practitioner read formal notation. |
| Local affordability vs repeated reuse | One local claim should stay cheap; repeated semantics should not be copied inconsistently. |
| Expressive claims vs small ontology | FPF should permit compound truths without minting one kind per compound predicate. |
| Reuse vs hidden dependencies | Reusable definitions need visible base-relation and substrate editions. |
| Truth conditions vs occurrence semantics | A predicate can be satisfied without supplying a way to reidentify relation occurrences. |
| Formal power vs substrate authority | Constructor names are available only where the selected substrate gives them semantics. |
| Mathematical representation vs ontology | A formula, path, graph, or query can represent a rule without making that rule obtain in the world. |

