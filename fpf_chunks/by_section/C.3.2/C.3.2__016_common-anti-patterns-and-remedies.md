---
chunk_kind: "child"
pattern_id: "C.3.2"
pattern_title: "Kind Intent, Membership Judgment, and Extension"
section_id: "C.3.2:14"
section_title: "Common Anti-Patterns and Remedies"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.2/C.3.2__016_common-anti-patterns-and-remedies.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "C.3.2 — Kind Intent, Membership Judgment, and Extension"
  - "C.3.2:14 — Common Anti-Patterns and Remedies"
line_start: 43841
line_end: 43854
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
  - "E.24.UK"
keywords:
---

### C.3.2:14 - Common Anti-Patterns and Remedies

| Anti-pattern | Remedy |
| --- | --- |
| Treating a kind and its `KindSignature` as one object | Identify the kind and declaration episteme separately. |
| Returning `unknown` for a candidate outside ValueKind or applicability | Return `not-applicable` and form no judgment. |
| Returning `false` for missing support | Preserve `unknown`; let the receiving guard decide whether to decline use. |
| Treating any evidence item or record as membership | Ask whether the criterion directly concerns that governed episteme, relation, status, or publication occurrence. If not, keep it only as support. |
| Reusing A.14 `MemberOf` or minting a relation by notation | Keep the result as a classification judgment unless a direct relation pattern is justified. |
| Treating an extension or braces as ontology | Keep the candidate domain and extension as representations; use C.29 when claim-bearing. |
| Attaching scope or formality to the kind | Keep them on their declaration or assertion epistemes. |
| Editing an extension to hide a subkind counterexample | Repair the relation proposal, declaration alignment, or distinct-kind bridge. |
| Classifying a record as actual Work | Recover an independently grounded `W : U.Work`; keep its record separate. |

