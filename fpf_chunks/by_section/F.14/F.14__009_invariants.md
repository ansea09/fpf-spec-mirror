---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti-Explosion Control for Role and Status Name Families"
section_id: "F.14:8"
section_title: "Invariants"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__009_invariants.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "F.14 — Anti-Explosion Control for Role and Status Name Families"
  - "F.14:8 — Invariants"
line_start: 94786
line_end: 94798
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.3.1"
  - "A.3.2"
  - "A.6.5"
  - "B.3"
  - "E.10.D2"
  - "E.24.PUB"
  - "F.10"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.8"
  - "F.9"
  - "U.Role"
  - "U.RoleAssignment"
keywords:
  - "bundles"
  - "guard-rails"
  - "reuse"
  - "separation-of-duties"
  - "vocabulary growth"
---

### F.14:8 - Invariants

1. **Governed value first.** No durable naming object is added until the exact value or relation, kind, direct owner, and proposed use are recoverable.
2. **Lightest sufficient disposition.** Prefer the dispositions `no durable name`, existing designation, alias, or local expression whenever one supports the use without hiding a distinction.
3. **No status roles.** Status, evidence, requirement, source, publication, and access uses do not become work-facing roles by suffix.
4. **No assignment by name.** A designation, RoleDescription, role-relation expression, card, cell, or row assigns no holder and proves no Work.
5. **No hybrid role by convenience.** Exact A.2.7 relations remain relations unless the direct role owner independently admits a different role value.
6. **No capability or authority by label.** Role and status names prove no capability, skill, permission, assurance, evidence use, method validity, or publication authority.
7. **Local senses do not globalize.** Same spelling and different local-sense projections establish neither governed-value identity nor an F.9 Bridge.
8. **Naming objects remain optional and distinct.** Expression, designation, alias, cell, NameCard, row, identifier, publication occurrence, form, and carrier neither imply nor replace one another.
9. **Selected structure is conditional.** A `BoundedModelUseStructure` is cited only when its organization changes the exact naming use and never becomes a locality slot or naming identity field.
10. **Lineage is not ontology.** Historical spelling may be recorded as lineage without carrying its former fused commitments forward.

