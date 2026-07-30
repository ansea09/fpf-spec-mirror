---
chunk_kind: "child"
pattern_id: "C.3.2"
pattern_title: "Kind Intent, Membership Judgment, and Extension"
section_id: "C.3.2:14"
section_title: "Common Anti-Patterns and Remedies"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.2/C.3.2__016_common-anti-patterns-and-remedies.md"
commit_sha: "308edacfa2bdb2c60d07e4e10c0deb1f260a6a31"
heading_path:
  - "C.3.2 — Kind Intent, Membership Judgment, and Extension"
  - "C.3.2:14 — Common Anti-Patterns and Remedies"
line_start: 45189
line_end: 45201
dependencies:
  - "A.14"
  - "A.2.6"
  - "A.6.0"
  - "C.2.1"
  - "C.2.3"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.3"
  - "C.3.4"
  - "C.3.5"
  - "C.3.A"
  - "E.24.UK"
keywords:
  - "KindExtension representation"
  - "KindSignature declaration episteme"
  - "candidate classification"
  - "local kind"
  - "true/false/unknown"
---

### C.3.2:14 - Common Anti-Patterns and Remedies

| Anti-pattern | Remedy |
| --- | --- |
| Treating a kind and its `KindSignature` as one object | Identify the local kind and the declaration episteme separately. |
| Using a measurement, observation, schema label, or source row as membership | Recover the direct candidate features; use the item only as governed support. |
| Returning `false` for missing or unusable information | Return `unknown`; let the receiving guard decide whether to decline use. |
| Reusing A.14 `MemberOf` or minting a direct relation by notation | Keep the C.3.2 result as a classification judgment unless a domain-specific direct pattern is justified. |
| Restoring `U.EntitySet` or treating braces as ontology | Describe the candidate domain and extension as a representation; use C.29 when claim-bearing. |
| Attaching scope or formality to the kind | Keep scope and formality on the declaration or assertion episteme that owns them. |
| Editing an extension to hide a subkind counterexample | Repair the link, incompatible editions, or missing bridge. |
| Classifying a record as actual Work | Recover an independently grounded `W : U.Work`; keep its record as a separate episteme. |

