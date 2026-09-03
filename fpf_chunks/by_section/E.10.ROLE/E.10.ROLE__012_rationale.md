---
chunk_kind: "child"
pattern_id: "E.10.ROLE"
pattern_title: "Recovering What “Role” Means in the Current Claim"
section_id: "E.10.ROLE:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.ROLE/E.10.ROLE__012_rationale.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "E.10.ROLE — Recovering What “Role” Means in the Current Claim"
  - "E.10.ROLE:10 — Rationale"
line_start: 77804
line_end: 77809
dependencies:
  - "A.2"
  - "A.2.1"
  - "A.6.5"
  - "A.6.RSIR"
  - "E.10"
  - "E.10.ARCH"
  - "F.18"
  - "F.19"
keywords:
  - "ambiguous role wording"
  - "assignment"
  - "declaration slot"
  - "interface place"
  - "ordinary wording"
  - "relation participant"
  - "representation position"
  - "responsibility"
  - "system-role kind"
---

### E.10.ROLE:10 - Rationale

The recurring problem is word-sense recovery, not a missing universal role category. FPF therefore makes an internal architectural choice: recover the claim expressed in this use, then use the direct pattern for the recovered kind, assignment, participant, declaration place, representation position, or relation. The trigger word neither supplies that ontology nor makes the recovered claim obtain.

The pattern therefore stays thin. It supplies an entry and a stop rule, while C.3, A.2, A.2.1, A.6.RSIR, A.6.5, C.29, A.10, A.15, and other direct patterns retain their own predicates and identity laws.

