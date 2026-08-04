---
chunk_kind: "child"
pattern_id: "C.3.2"
pattern_title: "Kind Intent, Membership Judgment, and Extension"
section_id: "C.3.2:7"
section_title: "Extension as Representation"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.2/C.3.2__009_extension-as-representation.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "C.3.2 — Kind Intent, Membership Judgment, and Extension"
  - "C.3.2:7 — Extension as Representation"
line_start: 44982
line_end: 44993
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
---

### C.3.2:7 - Extension as Representation

Materialize `KindExtension(k, slice)` only when a named query, quantification, comparison, review, or publication needs the current true-candidate set.

- Pin the `KindSignature` edition used by the representation even though the compact name shows only `k` and `slice`.
- State the declared candidate domain without inventing `U.EntitySet`.
- Include exactly the candidate values whose pinned judgment is `true`; do not insert `unknown` candidates as false or silently omit their unresolved status when the receiving use needs it.
- Treat braces, rows, indexes, or database results as representations. They do not create a collection holon, an A.14 membership occurrence, a direct classification relation, or the candidate features.
- Use C.29 when the mathematical lens or represented set changes a claim-bearing use. Otherwise the extension may remain a local calculation.

A changed candidate state or later context slice can change `KindExtension(k, slice)` without changing the signature or local kind. A changed extension row cannot repair an inconsistent declaration or subkind link.

