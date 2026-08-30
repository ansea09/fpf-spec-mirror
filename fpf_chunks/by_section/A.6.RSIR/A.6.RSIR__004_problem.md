---
chunk_kind: "child"
pattern_id: "A.6.RSIR"
pattern_title: "Relation, Signature, Interface, Role, and Slot Precision Restoration"
section_id: "A.6.RSIR:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.RSIR/A.6.RSIR__004_problem.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "A.6.RSIR — Relation, Signature, Interface, Role, and Slot Precision Restoration"
  - "A.6.RSIR:2 — Problem"
line_start: 17359
line_end: 17370
dependencies:
  - "A.10"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.3.4.P"
  - "A.6.0"
  - "A.6.1"
  - "A.6.5"
  - "A.6.A"
  - "A.6.F"
  - "A.6.M"
  - "A.6.P"
  - "A.6.REL"
  - "C.2.1"
  - "C.2.P"
  - "C.2.P.DR"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.ROLE"
  - "E.17"
  - "F.10"
  - "F.18"
  - "F.19"
  - "G.6"
keywords:
  - "API"
  - "RelationSignature"
  - "SlotSpec"
  - "ambiguous role wording"
  - "direct relation participant"
  - "interface"
  - "operation declaration and binding"
  - "participant meaning"
  - "port"
  - "reduced-use source label"
  - "relation-signature-interface-role-slot recovery"
  - "representation position"
  - "system-role assignment"
  - "system-role kind"
---

### A.6.RSIR:2 - Problem

Without this pattern:

1. **Lexical cues create shadow kinds.** Interface, role, slot, endpoint, and function words become local root kinds because they sound technical.
2. **Participant, declaration, and representation uses become system roles.** A direct relation-participant meaning, declaration-local `SlotKind`, argument, field, endpoint, or representation position is renamed as a system-role kind. Evidence-use, transformation, and interface claims then lose their direct relations and patterns.
3. **System-role kinds become declaration or representation labels.** A real context-local system-role kind is demoted into a declaration-local `SlotKind` or source-schema field, so its `KindSignature`, exact assignment occurrence and window, `SystemRoleAssignmentStateRelation`, and Work consequences can no longer be recovered.
4. **Signatures absorb implementations.** A law-governed `U.Signature` is used as if it were a mechanism, method, work-start gate decision, interface conformance proof, or publication.
5. **Participant, declaration, application, and representation boundaries are skipped.** A field or parameter is edited without deciding whether it denotes a direct relation-participant meaning or actual participant, a declaration-local `SlotSpec`, an A.6.1 argument or result declaration, one exact operation application and actual binding, or a position in a selected representation.
6. **Evidence and status uses keep old role grammar.** An episteme, standard, report, publication, or badge is said to have a role instead of being used in an evidence-use, source-use, status-use, publication-use, assurance-use, or gate relation.
7. **Neighboring patterns are copied locally.** A pattern repeats negative catalogues such as "not proof, not permission, not gate" instead of recovering the current object and applying the pattern that defines or constrains the claim.

