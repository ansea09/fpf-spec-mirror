---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti-Explosion Control for System-Role and Status Name Families"
section_id: "F.14:8"
section_title: "Invariants"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__009_invariants.md"
commit_sha: "c7ac61bbaa8d3c10165b1a5a4a350956c87d77c9"
heading_path:
  - "F.14 — Anti-Explosion Control for System-Role and Status Name Families"
  - "F.14:8 — Invariants"
line_start: 94650
line_end: 94662
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
  - "F.6"
  - "F.8"
  - "F.9"
  - "U.SystemRoleAssignment"
keywords:
  - "NameCard"
  - "assignment"
  - "designation"
  - "evidence use"
  - "permission"
  - "reuse"
  - "status names"
  - "system-role names"
  - "term row"
  - "vocabulary explosion"
---

### F.14:8 - Invariants

1. **Governed value first.** No durable naming object is added until the exact value or relation, kind, proposed use, and the pattern contribution that defines, constrains, or tests each needed claim are recoverable.
2. **Lightest sufficient disposition.** Prefer the dispositions `no durable name`, existing designation, alias, or local expression whenever one supports the use without hiding a distinction.
3. **No status roles.** Status, evidence, requirement, source, publication, and access uses do not become system-role kinds by suffix.
4. **No assignment by name.** A designation, `SystemRoleKindDescription`, system-role-kind relation expression, card, cell, or row assigns no system and proves no Work.
5. **No hybrid kind by convenience.** Exact A.2.7 relations remain relations unless A.2 with C.3 independently admits a different local system-role kind.
6. **No capability or authority by label.** System-role-kind and status names prove no capability, skill, permission, assurance, evidence use, Method validity, or publication authority.
7. **Local senses do not globalize.** Same spelling and different local-sense projections establish neither governed-value identity nor an F.9 Bridge.
8. **Naming objects remain optional and distinct.** Expression, designation, alias, cell, NameCard, row, identifier, publication occurrence, form, and carrier neither imply nor replace one another.
9. **Selected structure is conditional.** A `BoundedModelUseStructure` is cited only when its organization changes the exact naming use and never becomes a locality slot or naming identity field.
10. **Lineage is not ontology.** Historical spelling may be recorded as lineage without carrying its former fused commitments forward.

