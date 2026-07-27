---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti-Explosion Control for Role and Status Name Families"
section_id: "F.14:1"
section_title: "Intent and applicability"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__002_intent-and-applicability.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "F.14 — Anti-Explosion Control for Role and Status Name Families"
  - "F.14:1 — Intent and applicability"
line_start: 91530
line_end: 91555
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
  - "E.17"
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

### F.14:1 - Intent and applicability

**Intent.** Keep role-like and status-like vocabularies small without losing real distinctions. F.14 is a control pass over candidate names and local name families. It does not define `U.Role`, does not define status ontology, and does not assign a holder. It asks what each proposed name is trying to name and blocks new durable names when the needed value is already a role value, role-relation expression, status family, status value, status window, qualifier, direct-pattern value, local phrase, or alias.

**Applicability.** Use F.14 when a project proposes several new role, status, access, evidence, requirement, source, method, capability, or work-like labels and the vocabulary starts to grow faster than the underlying distinctions. Use it before adding RoleDescriptions, Concept-Set rows, public names, cross-context rows, or role-relation names.

**Primary EntityOfConcern in plain terms.** One anti-explosion control pass over a candidate family of names in a bounded context or bridge family. The EoC is not the role value, not the status value, not the holder, not the work occurrence, and not a publication.

**Admissible move in plain terms.** Recover the kind of each candidate name, choose reuse or direct-pattern naming where possible, and record why no new durable role or status name is needed unless F.8 and F.18 admit it.

**Primary working reader.** A method author, terminology steward, architect, manager, or checker who sees names such as `NightOperatorRole`, `EvidenceRole`, `SeniorReviewer`, `AtRiskStatus`, `PreValidated`, `AccessRole`, or `RequestApproverRole` and must stop the vocabulary from becoming a second ontology.

**Use this when.** Use F.14 when name growth hides one of these questions:

1. Is this one work-facing `U.Role`, a RoleDescription label, a role-relation expression, a role assignment, a capability requirement, a method name, a work name, or only a local phrase?
2. Is this one status family, status value, status window, status-use relation, evidence-use relation, source-use relation, requirement-use relation, or presentation label?
3. Is the candidate cross-context and therefore dependent on F.9 or F.17 before durable reuse?

**What goes wrong if missed.** Role labels become capability models, status labels become role families, access-control labels become work roles, and role-relation expressions become fake holders. The corpus then gets many small near-duplicate names that look precise but hide different kinds.

**What this buys.** A smaller vocabulary with stronger type separation: fewer durable names, clearer role relation structure, cleaner status families, fewer aliases with hidden claims, and more reliable F.8 and F.18 naming decisions.

**Not this pattern when.** Not F.14 when the question is one candidate expression only; use F.8. Not F.14 when the question is assigning a holder or attributing performed work; use A.2.1, F.6, and A.15.1. Not F.14 when the question is a status-use or evidence-use claim; use F.10, A.10, B.3, or the direct governing pattern. Not F.14 when the question is public terminology publication; use F.17 and F.18 after kind recovery.

**Recognition versus assurance note.** The recognition block is the name-growth situation plus the first kind-recovery move. The assurance block is the record, invariants, role-relation and status-family boundaries, conformance tests, and SoTA note. Assurance text tightens the same anti-explosion control pass; it must not turn F.14 into role ontology, status ontology, or naming authority for every value.

