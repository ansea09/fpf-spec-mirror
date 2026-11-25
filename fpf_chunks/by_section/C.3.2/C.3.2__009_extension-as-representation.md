---
chunk_kind: "child"
pattern_id: "C.3.2"
pattern_title: "Kind Intent, Membership Judgment, and Extension"
section_id: "C.3.2:7"
section_title: "Extension as Representation"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.2/C.3.2__009_extension-as-representation.md"
commit_sha: "423f9d3fef92bafec7b092b910e8ce056a0f607d"
heading_path:
  - "C.3.2 — Kind Intent, Membership Judgment, and Extension"
  - "C.3.2:7 — Extension as Representation"
line_start: 58167
line_end: 58178
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

### C.3.2:7 - Extension as Representation

Materialize `KindExtension(k, slice)` only when a named query, quantification, comparison, review, or publication needs the current true-candidate set.

- Pin the signature edition even though the compact name shows only `k` and `slice`.
- State the candidate domain without inventing `U.EntitySet`.
- Include each admissible candidate whose judgement is `true`. Their number answers how many candidates have been individually confirmed. To answer a question about the population total, establish what bounds the number of members. In a complete inventory, confirmed members give one lower bound. Adding every other candidate whose membership remains possible gives one upper bound. These bounds can be loose. If exactly one of two identified units qualifies and the evidence leaves open which one, together they contribute exactly one. An established cap on the entire population can give an upper bound even when its inventory is incomplete. Use a sufficient bound for a threshold, and establish identities and coverage for a complete list. An `unknown` judgement records an inconclusive evaluation. An unevaluated candidate has no judgement yet. An inadmissible request returns `not-applicable` without a judgement.
- Treat braces, rows, indexes, or database results as representations. They create neither a collection holon, A.14 membership occurrence, direct classification relation, nor criterion condition.
- Use C.29 when interpretation, preservation or transfer of the represented set leaves a separate mathematical question. Otherwise finish the local calculation under the kind and query rules.

Candidate state or a later slice can change an extension without changing the signature or kind. An extension row cannot repair an inconsistent declaration or subkind fact.

